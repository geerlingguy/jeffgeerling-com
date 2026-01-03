---
nid: 2406
title: "2013 VPS Benchmarks - Linode, Digital Ocean, Hot Drupal"
slug: "2013-vps-benchmarks-linode"
date: 2013-05-19T20:30:31+00:00
drupal:
  nid: 2406
  path: /blogs/jeff-geerling/2013-vps-benchmarks-linode
  body_format: full_html
  redirects: []
tags:
  - cpu
  - disk
  - hosting
  - memory
  - performance
  - sysbench
  - vps
aliases:
  - /blogs/jeff-geerling/2013-vps-benchmarks-linode
---

Every year or two, I like to get a good overview of different hosting providers' VPS performance, and from time to time, I move certain websites and services to a new host based on my results.

In the past, I've stuck with <a href="https://www.linode.com/">Linode</a> for many services (their end-to-end UX, and raw server performance is great!) that weren't intense on disk operations, and <a href="http://www.hotdrupal.com/">Hot Drupal</a> for some sites that required high-performance IO (since Hot Drupal's VPSes use SSDs and are very fast). This year, though, after <a href="https://www.digitalocean.com/">Digital Ocean</a> jumped into the VPS hosting scene, I decided to give them a look.

Before going further, I thought I'd give a few quick benchmarks from each of the providers; these are all on middle-range plans (1 or 2GB RAM), and with the exception of Linode, the disks are all SSD, so should be super fast:

<h2>Disk Performance</h2>

<p style="text-align: center;">{{< figure src="./2013-vps-disk-io.png" alt="Disk Performance Chart" width="275" height="235" >}}</p>

(I used the command <code>dd bs=1M count=512 if=/dev/zero of=test conv=fdatasync</code> for a simple benchmark, which writes and reads a 512MB file to disk. These results were averaged over three test runs).

<strong>Linode</strong>: 60.9 MB/s
<strong>Digital Ocean</strong>: 230 MB/s
<strong>Hot Drupal</strong>: 244 MB/s

The clear loser for disk I/O seems to be Linode; since they have spinning disks in RAID, it's not much of a surprise, though. I'm not sure exactly how Digital Ocean and Hot Drupal's SSDs are set up, but I'm presuming they have either a SAN built with SSDs, or an SSD per server (hopefully RAID, but I keep external backups no matter what :D).

<h2>CPU Performance</h2>

<p style="text-align: center;">{{< figure src="./2013-vps-cpu-1-thread.png" alt="CPU Performance Chart - 1 Thread" width="275" height="235" >}} {{< figure src="./2013-vps-cpu-x-threads.png" alt="CPU Performance Chart - X Threads" width="275" height="235" >}}</p>

(I used the command <code>sysbench --test=cpu --cpu-max-prime=20000 run</code> for a simple benchmark (and added <code>--num-threads=X</code> to run a multithreaded version). This requires <code>sysbench</code> to be installed on the server).

<strong>Linode</strong> (8 CPU / 2.26 Ghz / 4533.56 bogomips): 105.5477s on 1 thread, 25.0219s on 8 threads
<strong>Digital Ocean</strong> (2 CPU / 2.0 Ghz / 3999.99 bogomips): 38.8598s on 1 thread, 18.8307s on 2 threads
<strong>Hot Drupal</strong> (6 CPU / 3.2 Ghz / 6400.00 bogomips): 23.7397s on 1 thread, 4.1549s on 6 threads

This was much more surprising; I expected Linode to thrash the other guys in terms of raw CPU performance, but both Digital Ocean, and especially Hot Drupal, killed the CPU test (especially if you increase the number of threads and use all the virtual CPU cores available!).

I've actually noticed that PHP processing time is noticeably faster (from an end user's perspective) on Hot Drupal, and now I have a number to back it up; when browsing around a Drupal site's admin backend, page loads sometimes take .5-1s less on Hot Drupal than on other servers (even my local MAMP server).

Note that this CPU measure is by no means comprehensive... but it does give an overall look at how CPU-bound workloads will be handled by the different VPSes.

<h2>Memory (RAM) Performance</h2>

<p style="text-align: center;">{{< figure src="./2013-vps-ram.png" alt="RAM Performance Chart" width="275" height="235" >}}</p>

(I used the command <code>sysbench --test=memory --memory-total-size=1G run</code>). This requires <code>sysbench</code> to be installed on the server).

<strong>Linode</strong>: 89.33 MB/sec
<strong>Digital Ocean</strong>: 650.01 MB/sec
<strong>Hot Drupal</strong>: 433.57 MB/sec

Of the three servers, the Hot Drupal server was by far the most stable, with all three memory tests within 1 MB/sec of each other. Linode and Digital Ocean were +/- 10%. As with the CPU tests, I was surprised by how slow the Linode memory access was in these tests; I would've expected much faster performance.

<h2>General Impressions</h2>

<h3>Linode</h3>

I have a few servers with Linode, and all of them have only been restarted by me. One of the servers is up to 460 days uptime, and the other two are approaching a year. Linode is a very reliable company, and support tickets are closed within minutes. Their management dashboard is very intuitive, and everything I've hosted with them has been reliable and relatively fast. In recent months, they've started providing free upgrades to disk, CPU, and memory for all their plans, but they seem to be on the more expensive side of current VPS plans. Whether that expense is justified depends on how reliable and secure Linode remains.

The fact that their public site is still built on ColdFusion, and thus has <a href="http://arstechnica.com/security/2013/04/coldfusion-hack-used-to-steal-hosting-providers-customer-data/">run into security issues recently</a>, makes me very slightly nervous... but not enough to move some of my existing for-pay services off of Linode VPSes. Plus, their infrastructure, geographic diversity, and management tools are top-notch, and are great for multi-server setups. Their <a href="https://library.linode.com/">Linode Library</a> is my benchmark for Linux how-tos and tutorials, and is very complete. Their <a href="https://forum.linode.com/">Linode Forums</a> also contain a great community and wealth of knowledge.

<h3>Digital Ocean</h3>

Digital Ocean seems to have set up their infrastructure well, but it is nowhere near as mature as Linode. They offer DNS services, but no droplet load balancing, no private network (all inter-server communication is metered with your public bandwidth), only three geographical locations for droplets, and their admin console is a little underwhelming. The signup and provisioning process is very nice, and their billing system is very simple and easy to understand.

The biggest things they have going for them right now are price, and ease of use (in that order). Their <a href="https://www.digitalocean.com/community">Community section</a> has many articles and how-tos, in addition to a growing forum, but is not as complete or concise as the Linode Library. This will improve with time, I'm sure, but Digital Ocean still has a ways to go.

<h3>Hot Drupal</h3>

Hot Drupal is more of a niche hosting provider, but they've been around a while, and offer some very good plans for PHP CMSes, most especially Drupal. I've put some clients on their shared plans, which are much nicer and faster than shared plans from other companies (HostGator, DreamHost, etc.), and on VPSes (which, as noted above, are <em>very</em> fast!).

Hot Drupal is a bit more expensive than other providers, and their admin console is not as full-featured as Linode's (it's more on par with what you get from Digital Ocean), but their support has always been amazing—they'll go out of their way to help you with any hosting-specific problems, and often will even help with Drupal-related problems. Most tickets I've opened with Hot Drupal have been responded to within minutes, and often their support staff will resolve the issue within 5-10 minutes. And did I mention their servers are <em>fast</em>?

<h2>Conclusion</h2>

For now, I'm sticking with a few VPSes across all three services, because none is a 'one-size-fits-all' hosting provider. Linode and Hot Drupal both have great track records (for me, at least), and I will be cautious considering Digital Ocean for larger projects until I've had more experience with them, and seen how fast they respond to outages and support tickets.

Digital Ocean's low, low prices are very tempting, though, for most of my smaller sites and services, and throwing $5/month at a few small servers for experimentation and testing is nothing; many shared hosts are more expensive than that!

If you're thinking of signing up for Linode, please consider using my <a href="http://www.linode.com/?r=dca78b4b11124cbcb5aee9b46c3055ca6379018a">Linode affiliate signup link</a> :)
