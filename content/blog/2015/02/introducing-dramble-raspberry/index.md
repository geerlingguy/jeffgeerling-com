---
nid: 2480
title: "Introducing the Dramble - Raspberry Pi 2 cluster running Drupal 8"
slug: "introducing-dramble-raspberry"
date: 2015-02-26T06:08:48+00:00
drupal:
  nid: 2480
  path: /blogs/jeff-geerling/introducing-dramble-raspberry
  body_format: full_html
  redirects: []
tags:
  - ansible
  - cluster
  - dramble
  - drupal
  - drupal 8
  - drupal planet
  - infrastructure
  - performance
  - raspberry pi
---

<p style="text-align: center;">{{< figure src="./raspberry-pi-dramble-cluster-wired.jpg" alt="Dramble - 6 Raspberry Pi 2 model Bs running Drupal 8 on a cluster" width="475" height="375" >}}
Version 0.9.3 of the <a href="https://github.com/geerlingguy/raspberry-pi-dramble">Dramble</a>—running Drupal 8 on 6 Raspberry Pis</p>

I've been tinkering with computers since I was a kid, but in the past ten or so years, mainstream computing has become more and more locked down, enclosed, lightweight, and, well, <em>polished</em>. I even wrote a blog post about how, nowadays, most <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/computers-are-amazing">computers are amazing</a>. Long gone are the days when I had to worry about line voltage, IRQ settings, diagnosing bad capacitors, and replacing 40-pin cables that went bad!

But I'm always tempted back into my earlier years of more hardware-oriented hacking when I pull out one of my Raspberry Pi B+/A+ or Arduino Unos. These devices are as raw of modern computers as you can get—requiring you to actual touch the silicone chips and pins to be able to even use the devices. I've been building a <a href="https://github.com/geerlingguy/temperature-monitor">temperature monitoring network</a> that's based around a Node.js/Express app using Pis and Arduinos placed around my house. I've also been working a lot lately on a project that incorporates three of my current favorite technologies: The Raspberry Pi 2 model B (<a href="http://www.raspberrypi.org/blog/page/2/#raspberry-pi-2-on-sale">just announced earlier this month</a>), Ansible, and Drupal!

<strong>In short, I'm building a cluster of Raspberry Pis, and designating it a '<a href="https://github.com/geerlingguy/raspberry-pi-dramble">Dramble</a>'—a '<a href="http://elinux.org/Bramble">bramble</a>' of Raspberry Pis running Drupal 8.</strong>

<h2>Motivation</h2>

<p style="text-align: center;">{{< figure src="./rgb-led-breadboard-resistors.jpg" alt="" width="450" height="304" >}}
This LED will light up that wonderful Drupal Blue,&nbsp;<a href="https://www.drupal.org/node/1051644"><span>#0678BE</span></a></p>

I've been giving a number of presentations on managing infrastructure with Ansible in the past couple years. And in the course of writing <a href="http://ansiblefordevops.com/">Ansible for DevOps</a> (available on LeanPub!), I've done a lot of testing on VMs both locally and in the cloud.

But doing this testing on a 'local datacenter'—especially one that fits&nbsp;<em>in the palm of my hand</em>—is great for two reasons:

<ul>
	<li>All networking is local; conferences don't always have the most stable networking, so I can do all my infrastructure testing on my own 'local cloud'.</li>
	<li>It's pretty awesome to be able to hold a cluster of physical servers and a Gigabit network in my hand!</li>
</ul>

<h2>Lessons Learned (so far!)</h2>

<p style="text-align: center;">{{< figure src="./raspberry-pi-2-boxes.jpg" alt="" width="450" height="345" >}}
Drool... <em>I own these!</em></p>

Building out the Pi-based infrastructure has taught me a lot about small-scale computing, efficient use of resources, benchmarking, and also how Drupal 8 differs (<em>spoiler</em>: it's&nbsp;<strong>way</strong> better) from Drupal 7 in terms of multi-server deployment and high-availability/high-performance configurations.

I've also learned:

<ul>
	<li>How to <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/2">control RGB LEDs with the Pi</a> and make an LED 'breathe' Drupal blue :)</li>
	<li>The importance of a <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/4">clean power supply</a> and decent wiring and accessories for a stable Pi cluster.</li>
	<li>Ways to <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/14">measure power consumption</a> and conserve energy when using Raspberry Pis—or any servers that consume energy.</li>
	<li>The <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/7">incredible variety of quality/performance</a> in cheap microSD and SD cards.</li>
	<li>How to <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/11">use Redis (instead of Memcached) for caching in Drupal 8</a>.</li>
	<li>The <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/18">performance of MySQL in a slow I/O, high latency environment</a>—via USB or internal storage.</li>
	<li>How to deploy either <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/23">GlusterFS or NFS for shared Drupal files</a> folders and test both.</li>
	<li>...and much more!</li>
</ul>

<h2>Benchmarking</h2>

<p style="text-align: center;">{{< figure src="./cat5-twisted-pair-network-cables-rj45-connectors.jpg" alt="" width="450" height="294" >}}
Wiring up the mini Cat5e network cables.</p>

I've been benchmarking the heck out of this infrastructure, and besides finding that the major limiting factor with a bunch of low-cost computers is almost always slow I/O, I've found that:

<ul>
	<li>On-the-fly gzip actually&nbsp;<em>harms</em> performance (in general) when your CPU isn't that fast.</li>
	<li>Redis caching gives an immediate 15% speedup for Drupal 8.</li>
	<li>Different microSD cards deliver order-of-magnitude speedups. As an example, one card took 20 minutes to import a 6MB database; another card? 9 seconds.</li>
	<li>Drupal 8 is kinda slow (but <a href="https://www.drupal.org/node/1744302">I don't need to tell you that</a>).</li>
	<li>Still to come: Nginx vs. Apache with php-fpm, Nginx vs. Varnish for load balancing, Redis vs. Memcached for caching. MySQL vs. MariaDB for database. And more!</li>
</ul>

Since I have this nice little cluster of Raspberry Pis humming along using half the power of a standard light bulb, the sky is the limit! And the fact that the servers are slower and have different performance considerations than typical modern cloud-based infrastructure actually helps to expose certain performance-related flaws that I wouldn't have otherwise!

Finally, it helps me stay creative in finding ways to eke out another 50 KB/sec of bandwidth here, or 100 iops there :)

<h2>See the Dramble in person!</h2>

So why am I mentioning all this? Because I want to bring the Dramble with me to some Drupal events, and I'd love to share it with you, explain everything in more detail, and most importantly:&nbsp;<strong>demonstrate modern and <em>easy</em>&nbsp;Drupal 8 deployment with Ansible</strong> on it.

I'll be <a href="http://2015.midcamp.org/session-proposal/ansible-drupal-fortuitous-devops-match">bringing it to #MidCamp</a> in Chicago on Saturday, March 21, and I've also submitted a session for DrupalCon LA: <a href="https://events.drupal.org/losangeles2015/sessions/deploying-drupal-8-bare-metal-ansible-live">Deploying Drupal 8 to Bare Metal with Ansible - Live!</a>

I hope the session is selected and I can bring the Dramble with me to LA in a couple months :)

Also, if you haven't submitted <em>your own</em> session for DrupalCon LA, the deadline is Friday; go <a href="https://events.drupal.org/losangeles2015/submit-session">submit it now</a>!

For more on the Dramble itself, check out the <a href="https://github.com/geerlingguy/raspberry-pi-dramble">Raspberry Pi Dramble project on GitHub</a>, and see what I'm working on over in the <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues">Dramble issue queue</a>.
