---
nid: 2886
title: "Drupal startup time and opcache - faster scaling for PHP in containerized environments"
slug: "drupal-startup-time-and-opcache-faster-scaling-php-containerized-environments"
date: 2018-11-03T05:07:13+00:00
drupal:
  nid: 2886
  path: /blog/2018/drupal-startup-time-and-opcache-faster-scaling-php-containerized-environments
  body_format: markdown
  redirects:
    - /blog/2018/drupal-startup-time-and-opcache-faster-scaling-drupal-containerized-environments
aliases:
  - /blog/2018/drupal-startup-time-and-opcache-faster-scaling-drupal-containerized-environments
tags:
  - docker
  - drupal
  - drupal 8
  - drupal planet
  - kubernetes
  - opcache
  - performance
  - php
  - scalability
---

Lately I've been spending a lot of time working with Drupal in Kubernetes and other containerized environments; one problem that's bothered me lately is the fact that when autoscaling Drupal, it always takes at _least_ a few seconds to get a new Drupal instance running. Not installing Drupal, configuring the database, building caches; none of that. I'm just talking about having a Drupal site that's already operational, and scaling by adding an additional Drupal instance or container.

One of the principles of the [12 Factor App](https://12factor.net) is:

> **IX. Disposability**
> 
> Maximize robustness with fast startup and graceful shutdown.

Disposability is important because it enables things like easy, fast code deployments, easy, fast autoscaling, and high availability. It also forces you to make your code stateless and efficient, so it starts up fast even with a cold cache. Read more about the [disposability factor](https://12factor.net/disposability) on the 12factor site.

Before diving into the details of how I'm working to get my Drupal-in-K8s instances faster to start, I wanted to discuss one of the primary optimizations, opcache...

## Measuring opcache's impact

I first wanted to see how fast page loads were when they used PHP's opcache (which basically stores an optimized copy of all the PHP code that runs Drupal in memory, so individual requests don't have to read in all the PHP files and compile them on every request.

  1. On a fresh Acquia BLT installation running in Drupal VM, I uninstalled the Internal Dynamic Page Cache and Internal Page Cache modules.
  1. I also copied the codebase from the shared NFS directory `/var/www/[mysite]` into `/var/www/localsite` and updated Apache's virtualhost to point to the local directory (`/var/www/[mysite]`, is, by default, an NFS shared mount to the host machine) to eliminate NFS filesystem variability from the testing.
  1. In Drupal VM, run the command `while true; do echo 1 > /proc/sys/vm/drop_caches; sleep 1; done` to effectively disable the linux filesystem cache (keep this running in the background while you run all these tests).
  1. I logged into the site in my browser (using `drush uli` to get a user 1 login), and grabbed the session cookie, then stored that as `export cookie="KEY=VALUE"` in my Terminal session.
  1. In Terminal, run `time curl -b $cookie http://local.example.test/admin/modules` three times to warm up the PHP caches and see page load times for a quick baseline.
  1. In Terminal, run `ab -n 25 -c 1 -C $cookie http://local.example.test/admin/modules` (requires `apachebench` to be installed).

At this point, I could see that with PHP's opcache enabled and Drupal's page caches disabled, the page loads took on average **688 ms**. A caching proxy and/or requesting cached pages as an anonymous user would dramatically improve that (the anonymous user/login page takes 160 ms in this test setup), but for a heavy PHP application like Drupal, < 700 ms to load every code path on the filesystem and deliver a generated page is not bad.

Next, I set `opcache.enable=0` (was `1`) in the configuration file `/etc/php/7.1/fpm/conf.d10-opcache.ini`, restarted PHP-FPM (`sudo systemctl restart php7.1-fpm`), and confirmed in Drupal's status report page that opcache was disabled (Drupal shows a warning if opcache is disabled). Then I ran another set of tests:

  1. In Terminal, run `time curl -b $cookie http://local.example.test/admin/modules` three times.
  1. In Terminal, run `ab -n 25 -c 1 -C $cookie http://local.example.test/admin/modules`

With opcache disabled, average page load time was up to **1464 ms**. So in comparison:

|Opcache status|Average page load time|Difference|
|---|---|---|
|Enabled|688 ms|baseline|
|Disabled|1464 ms|776 ms (72%, or 2.1x slower)|

> Note: _Exact timings_ are unimportant in this comparison; the _delta_ between different scenarios what's important. Always run benchmarks on your own systems for the most accurate results.

## Going further - simulating real-world disk I/O in VirtualBox

So, now that we know a fresh Drupal page load is almost 4x slower than one with the code precompiled in opcache, what if the disk access were slower? I'm running these tests on a 2016 MacBook Pro with an insanely-fast local NVMe drive, which can pump through many gigabytes per second sequentially, or hundreds of megabytes per second random access. Most cloud servers have disk I/O which is much more limited, even if they say they are 'SSD-backed' on the tin.

Since Drupal VM uses VirtualBox, I can limit the VM's disk bandwidth using the `VBoxManage` CLI (see [Limiting bandwidth for disk images](https://www.virtualbox.org/manual/ch05.html#storage-bandwidth-limit)):

```
# Stop Drupal VM.
vagrant halt

# Add a disk bandwidth limit to the VM, 1 MB/sec.
VBoxManage bandwidthctl "VirtualBox-VM-Name-Here" add Limit --type disk --limit 5M

# Get the name of the disk image (vmdk) corresponding to the VM.
VBoxManage list hdds

# Apply the limit to the VM's disk.
VBoxManage storageattach "VirtualBox-VM-Name-Here" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "full-path-to-vmdk-from-above-command" --bandwidthgroup Limit

# Start Drupal VM.
vagrant up

# (You can update the limit in real time once the VM's running with the command below)
# VBoxManage bandwidthctl "VirtualBox-VM-Name-Here" set Limit --limit 800K
```

I re-ran the tests above, and the average page load time was now **2171 ms**. Adding that to the test results above, we get:

|Opcache status|Average page load time|Difference|
|---|---|---|
|Enabled|688 ms|baseline|
|Disabled|1464 ms|776 ms (72%, or 2.1x slower)|
|Disabled (slow I/O)|2171 ms|1483 ms (104%, or 3.2x slower)|

Not every cloud VM has that slow of disk I/O... but I've seen many situations where I/O gets severely limited, especially in cases where you have multiple volumes mounted per VM (e.g. maximum EC2 instance EBS bandwidth per instance) and they're all getting hit pretty hard. So it's good to test for these kinds of worst-case scenarios. In fact, last year I found that a hard outage was caused by an E_F_S volume hitting a burst throughput limit, and bandwidth went down to 100 Kbps. This caused _so_ many issues, so I had to architect around that potential issue to prevent it from happening in the future.

The point is, if you need fast PHP startup times, slow disk IO can be a very real problem. This could be especially troublesome if trying to run Drupal in environments like Lambda or other Serverless environments, where disk I/O is usually the lowest priority—especially if you choose to allocate a smaller portion of memory to your function! Cutting down the initial request compile time could be immensely helpful for serverless, microservices, etc.

## Finding the largest bottlenecks

Now that we know the delta for opcache vs. not-opcache, and vs. not-opcache on a very slow disk, it's important to realize that compilation is just one in a series of many different operations which occurs when you start up a new Drupal container:

  - If using Kubernetes, the container image might need to be pulled (therefore network bandwidth and image size may have a great affect on startup time)
  - The amount of time Docker spends allocating resources for the new container, creating volume mounts (e.g. for a shared files directory) can differ depending on system resources
  - The latency between the container and the database (whether in a container or in some external system like Amazon RDS or Aurora) can cause tens or even hundreds of ms of time during startup

However, at least in this particular site's case—assuming the container image is already pulled on the node where the new container is being started—the time spent reading in code into the opcache is by far the longest amount of time (~700ms) spent waiting for a fresh Drupal Docker container to serve its first web request.

## Can you precompile Drupal for faster startup?

Well... not really, at least not with any reasonable sanity, currently.

But there is hope on the horizon: There's a possibility PHP 7.4 could add a cool new feature, [Preloading](https://wiki.php.net/rfc/preload)! You can read the gory details in the RFC link, but the gist of it is: when you are building your container image, you could precompile all of your application code (or at least the hot code paths) so when the container starts, it only takes a couple ms instead of hundreds of ms to get your application's code compiled into opcache.

We'll see if this RFC gets some uptake; in the meantime, there's not really much you can do to mitigate the opcache warming problem.

## Conclusion

With [Preloading](https://wiki.php.net/rfc/preload), we might be able to pre-compile our PHP applications—notably beefy ones like Drupal or Magento—so they can start up much more quickly in lightweight environments like Kubernetes clusters, Lambda functions, and production-ready docker containers. Until that time, if it's important to have Drupal serve its first request as quickly as possible, consider finding ways to trim your codebase so it doesn't take half a second (or longer) to compile into the opcache!
