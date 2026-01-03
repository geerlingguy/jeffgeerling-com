---
nid: 2504
title: "Vagrant web development - is VMware better than VirtualBox?"
slug: "vagrant-vmware-7-vs-virtualbox-5-benchmarks"
date: 2015-08-21T12:42:42+00:00
drupal:
  nid: 2504
  path: /blogs/jeff-geerling/vagrant-vmware-7-vs-virtualbox-5-benchmarks
  body_format: full_html
  redirects: []
tags:
  - benchmarking
  - drupal
  - drupal 8
  - drupal planet
  - performance
  - vagrant
  - virtualbox
  - vmware
---

[<strong>Update 2015-08-25</strong>: I reran some of the tests using two different settings in VirtualBox. First, I explicitly set KVM as the paravirtualization mode (it was saved as 'Legacy' by default, due to a bug in VirtualBox 5.0.0), which showed impressive performance improvements, making VirtualBox perform 1.5-2x faster, and bringing some benchmarks to a dead heat with VMware Fusion. I also set the virtual network card to use 'virtio' instead of emulating an Intel PRO/1000 MT card, but this made little difference in raw network throughput or any other benchmarks.]

My Mac spends the majority of the day running at between one and a dozen VMs. I do all my development (besides iOS or Mac dev) running code inside VMs, and for many years I used VirtualBox, a free virtualization tool, along with Vagrant and Ansible, to build and manage all these VMs.

Since I use build and rebuild dozens of VMs per day, and maintain a popular Vagrant configuration for Drupal development (<a href="http://www.drupalvm.com/">Drupal VM</a>), as well as dozens of other VMs (like <a href="https://github.com/geerlingguy/ansible-vagrant-examples">Ansible Vagrant Examples</a>), I am highly motivated to find the fastest and most reliable virtualization software for local development. I switched from VirtualBox to VMware Fusion (which requires a <a href="http://www.vagrantup.com/vmware">for-pay plugin</a>) a year ago, as a few benchmarks I ran at the time showed VMware was 10-30% faster.

Since VirtualBox 5.0 was released earlier this year, I decided to re-evaluate the two VM solutions for local web development (specifically, LAMP/LEMP-based Drupal development, but most of these benchmarks apply to any dev workflow).

I benchmarked the raw performance bits (CPU, memory, disk access) as well as some 'full stack' scenarios (load testing and per-page load performance for some CMS-driven websites). I'll present each benchmark, some initial conclusions based on the result, and the methodology I used for each benchmark.

The key question I wanted to answer: <em>Is purchasing VMware Fusion and the required Vagrant plugin ($140 total!) worth it, or is VirtualBox 5.0 good enough?</em>

<h2>Baseline Performance: Memory and CPU</h2>

I wanted to make sure VirtualBox and VMWare could both do basic operations (like copying memory and performing raw number crunching in the CPU) at similar rates; both should pass through as much of this performance as possible to the underlying system, so numbers should be similar:

<p style="text-align: center;">{{< figure src="./memory-and-cpu.jpg" alt="Memory and CPU benchmark - VirtualBox and VMware Fusion" width="650" height="450" >}}</p>

VMware and VirtualBox are neck-in-neck when it comes to raw memory and CPU performance, and that's to be expected these days, as both solutions (as well as most other virtualization solutions) are able to use features in modern Intel processors and modern chipsets (like those in my MacBook Air) to their fullest potential.

CPU or RAM-heavy workloads should perform similarly, though VMware Fusion has a slight edge.

<h3>Methodology - CPU/RAM</h3>

I used <a href="https://github.com/akopytov/sysbench">sysbench</a> for the CPU benchmark, with the command <code>sysbench --test=cpu --cpu-max-prime=20000 --num-threads=2 run</code>.

I used <a href="https://github.com/raas/mbw">Memory Bandwidth Benchmark (mbw)</a> for the RAM benchmark, with the command <code>mbw -n 2 256 | grep AVG</code>, and I used the <code>MEMCPY</code> result as a proxy for general RAM performance.

<h2>Baseline Performance: Networking</h2>

More bandwidth is always better, though most development work doesn't rely on a ton of bandwidth being available. A few hundred megabits should serve web projects in a local environment quickly.

<p style="text-align: center;">{{< figure src="./raw-network-throughput.jpg" alt="Network throughput benchmark - VirtualBox and VMware Fusion" width="650" height="450" >}}</p>

This is one of the few tests in which VMware really took VirtualBox to the cleaners. It makes some sense, as VMware (the company) spends a lot of time optimizing VM-to-VM and VM-to-network-interface throughput since their products are more often used in production environments where bandwidth matters <em>a lot</em>, whereas VirtualBox is much more commonly used for single-user or single-machine purposes.

Having 40% more bandwidth available means VMware should be able to perform certain tasks, like moving files between host/VM, or your network connection (if it's fast enough) and the VM, or serving hundreds or thousands of concurrent requests, with much more celerity than VirtualBox—and we'll see proof of this fact with a Varnish load test, later in the post.

<h3>Methodology - Networking</h3>

To measure raw virtual network interface bandwidth, I used <a href="https://iperf.fr/">iperf</a>, and set the VM as the server (<code>iperf -s</code>), then connected to it and ran the benchmark from my host machine (<code>iperf -c drupalvm.dev</code>). iperf is an excellent tool for measuring raw bandwidth, as no non-interface I/O operations are performed. Tests such as file copies can have irregular results due to filesystem performance bottlenecks.

<h2>Disk Access and Shared/Synced Folders</h2>

One of the largest performance differentiators—and one of the most difficult components to measure—is filesystem performance. Virtual Machines use virtual filesystems, or connect to folders on the host system via some sort of mounted share, to provide a filesystem the guest OS uses.

Filesystem I/O perfomance is impossible to measure simply and universally, because every use case (e.g. media streaming, small file reads, small file writes, or database access patterns) benefits from different types of file read/write performance.

Since most filesystems (and even the <a href="https://github.com/geerlingguy/raspberry-pi-dramble/wiki/microSD-Card-Benchmarks">slowest of slow microSD cards</a>) are fast enough for large file operations (reading or writing large files in large chunks), I decided to benchmark one of the most brutal metrics of file I/O, 4k random read/write performance. For many web applications and databases, common access patterns either require hundreds or thousands of small file reads, or many concurrent small write operations, so this is a decent proxy of how a filesystem will perform under the most severe load (e.g. reading an entire PHP application's files from disk, when opcaches are empty, or rebuilding key-value caches in a database table).

I measured 4k random reads and writes across three different VM scenarios: first, using the VM's native share mechanism (or 'synced folder' in Vagrant parlance), second, using NFS, a common and robust network share mechanism that's easy to use with Vagrant, nad third, reading and writing directly to the native VM filesystem:

<p style="text-align: center;">{{< figure src="./disk-performance-random-io.jpg" alt="Disk or drive random access benchmark - VirtualBox and VMware Fusion" width="650" height="450" >}}</p>

The results above, as with all other benchmarks in this post, were repeated at least four times, with the first result set discarded. Even then, the standard deviation on these benchmarks was typically 5-10%, and the benchmarks were <em>wildly</em> different depending on the exact benchmark I used.

I was able to reproduce the <a href="http://mitchellh.com/comparing-filesystem-performance-in-virtual-machines">strange I/O performance numbers in Mitchell Hashimoto's 2014 post</a> when I didn't use direct filesystem access to do reads and writes; certain benchmarks suggest the VM filesystem is capable of over 1 GB/sec of random 4K reads and writes! Speaking of which, running the same benchmarks on <strong>my MacBook Air's internal SSD showed maximum performance of 1891 MB/s read, and 389 MB/s write</strong>.

Passing the <code>-I</code> option to the <code>iozone</code> benchmarking tool makes sure the tests bypass the VM's disk caching mechanisms that masks the <em>actual</em> filesystem performance. Unfortunately, this parameter (which uses <code>O_DIRECT</code> filesystem access) doesn't work with native VM shares, so those numbers may be a bit inflated over real-world performance.

The key takeaway? No matter the filesystem you use in a VM, raw file access is an order of magnitude slower than native host I/O if you have a fast SSD. Luckily, the raw performance isn't horrendous (as long as you're not copying millions of tiny files!), and common development access patterns help filesystem and other caches speed up file operations.

<h3>Methodology - Disk Access</h3>

I used <a href="http://www.iozone.org/">iozone</a> to measure disk access, using the command <code>iozone -I -e -a -s 64M -r 4k -i 0 -i 2 [-f /path/to/file]</code>. I also repeated the tests numerous times with different <code>-s</code> values ranging from 128M to 1024M, but the performance numbers were similar with any value.

If you're interested in diving deeper into filesystem benchmarking, iozone's default set of tests are much broader and applicable across a very wide range of use cases (besides typical LAMP/LEMP web development).

<h2>Full Stack - Drupal 7 and Drupal 8</h2>

When it comes down to it, the most meaningful benchmark is a 'full stack' benchmark, which tests the application I'm developing. In my case, I am normally working on Drupal-based websites, so I wanted to test both Drupal 8 and Drupal 7 (the current stable release) in two scenarios—a clean install of Drupal 8 (with nothing extra added), and a fairly heavy Drupal 7 site, to mirror some of the more complicated sites I have to work with.

First, here's a comparison of 'requests per second' with VirtualBox and VMware. Higher numbers are better, and this test is a decent proxy for how fast the VM is rendering specific pages, as well as how many requests the full stack/server can serve in a short period of time:

<p style="text-align: center;">{{< figure src="./requests-per-second-drupal8.jpg" alt="Drupal 8 requests per second benchmark - VirtualBox and VMware Fusion" width="650" height="450" >}}</p>

The first two benchmarks are very close. When your application is mostly CPU-and-RAM-constrained (Drupal 8 is running almost entirely out of memory using PHP's opcache and MySQL caches), both virtualization apps are about the same, with a very slight edge going to VMware Fusion.

The third graph is more interesting, as it shows a large gap—VMware can serve up 43% more traffic than VirtualBox. When you compare this graph with the raw network throughput graph above, it's obvious VMware Fusion's network bandwidth is the reason it can almost double the requests/sec for a network-constrained benchmark like Varnish capacity.

Developing a site with frequently-changing code requires more disk I/O, since the opcache has to be rebuilt from disk, so I tested raw page load times with a fresh PHP thread:

<p style="text-align: center;">{{< figure src="./page-load-times.jpg" alt="Page load performance for Drupal 7 and 8 - VirtualBox and VMware Fusion" width="650" height="450" >}}</p>

For this test, I restarted Apache entirely between each page request, which wiped out PHP's opcache, causing all the PHP files to be read from the disk. These benchmarks were run using an NFS share, so the main performance increase here (over the load test in the previous benchmark) comes from VMware's slightly faster NFS shared filesystem performance.

In real world usage, there's a perceptible performance difference between VirtualBox and VMware Fusion, and these benchmarks confirm it.

Many people decide to use native synced folders because file permissions and setup can often be simpler, so I wanted to see how much <em>not</em> using NFS affects these numbers:

<p style="text-align: center;">{{< figure src="./file-sharing-page-load-times.jpg" alt="Page load performance for Drupal 7 and 8 with different synced folder methods - VirtualBox and VMware Fusion" width="650" height="450" >}}</p>

As it turns out, NFS has a lot to offer in terms of performance for apps running in a shared folder. Another interesting discovery: VMware's native shared folder performs nearly as good as the ideal scenario in VirtualBox (running the codebase on an NFS mount).

I still highly recommend using NFS instead of native shared folders if you're sharing more than a few files between host and guest.

<h3>Methodology - Full Stack Performance</h3>

I used <code>ab</code>, <code>wrk</code>, and <code>curl</code> to run performance benchmarks and simple load tests:

<ul>
<li>Drupal anonymous cached page load: <code>wrk -d 30 -c 2 http://drupalvm.dev/</code></li>
<li>Drupal authenticated page load: <code>ab -n 500 -c 2 -C "SESS:COOKIE" http://drupalvm.dev/</code> (used the uid 1 user session cookie)</li>
<li>Varnish anonymous proxied page load: <code>wrk -d 30 -c 2 http://drupalvm.dev:81/</code> (a cache lifetime value of '15 minutes' was set on the performance configuration page)</li>
<li>Drupal 8 front page uncached: <code>time curl --silent http://drupalvm.dev/ > /dev/null</code>, run once after clicking 'Clear all caches' on the <code>admin/config/development/performance</code> page, averaged over six runs)</li>
<li>Large Drupal 7 site views/panels page request: <code>time curl --silent http://local.example.com/path > /dev/null</code> (run once after clicking 'Clear all caches' on the `admin/config/development/performance` page, averaged over six runs)</li>
<li></li>
</ul>

Drupal 8 tests were run with a standard profile install of a Drupal 8 site (ca. beta 12) on Drupal VM 2.0.0, and Drupal 7 tests were run using a very large scale Drupal codebase, with over 150 modules.

<h2>Summary</h2>

I hope these benchmarks help you to decide if VMware Fusion is right for <em>your</em> Vagrant-based development workflow. If you use synced folders a lot and need as much bandwidth as possible, choosing VMware is a no-brainer. If you don't, then VirtualBox is likely 'fast enough' for your development workflow.

It's great to have multiple great choices for VM providers for local development—and in this case, the open source option holds its own against the heavyweight proprietary virtualization app!

<h2>Methodology - All Tests</h2>

Since I detest when people post benchmarks but don't describe the system under test and all their reasons behind testing things certain ways, I thought I'd explicitly outline everything here, so someone else with the time and materials could replicate all my test results <em>verbatim</em>.

<ul>
<li>I ran <em>all</em> benchmarks four times (with the exception of some of the disk benchmarks, which I ran six times for better coverage of random I/O variance), discarded the first result, and averaged the remaining results.</li>
<li>All tests were run using an unmodified copy of <a href="http://www.drupalvm.com/">Drupal VM</a> version 2.0.0, with all the example configuration files (though all extra installations besides Varnish were removed), using the included Ubuntu 14.04 LTS minimal base box (which is built using <a href="https://github.com/geerlingguy/packer-ubuntu-1404">this Packer configuration</a>, the same for both VirtualBox and VMware Fusion).</li>
<li>For full stack Drupal benchmarking for Varnish-cached pages, I logged into Drupal and set a minimum cache lifetime value of '15 minutes' on the performance configuration page, and for authenticated page loads, I used the session cookie for the logged in uid 1 user.</li>
<li>All tests were run on my personal 11" Mid 2013 MacBook Air, with a 1.7 GHz Intel Core i7 processor, 8 GB of RAM, and a 256 GB internal SSD. The only other applications (besides headless VMs and Terminal) that were open and running during tests were Mac OS X Mail and Sublime Text 3 (in which I noted benchmark results.</li>
<li>All tests were performed with my Mac disconnected entirely from the Internet (WiFi disabled, and no connection otherwise), to minimize any strange networking problems that could affect performance.</li>
</ul>
