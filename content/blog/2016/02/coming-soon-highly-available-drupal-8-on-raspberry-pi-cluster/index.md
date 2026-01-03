---
nid: 2625
title: "Coming soon: Highly-available Drupal 8 on a Raspberry Pi Cluster"
slug: "coming-soon-highly-available-drupal-8-on-raspberry-pi-cluster"
date: 2016-02-29T22:21:18+00:00
drupal:
  nid: 2625
  path: /blog/2016/coming-soon-highly-available-drupal-8-on-raspberry-pi-cluster
  body_format: markdown
  redirects: []
tags:
  - appearances
  - drupal
  - drupal 8
  - drupal planet
  - drupalcon
  - phptek
  - raspberry pi
---

I'm going to bring the [Raspberry Pi Dramble](http://www.pidramble.com/) with me to [php[tek]](https://tek.phparch.com/speakers/#70505) on May 25 in St. Louis this year, and I'm hoping to also bring it with me to DrupalCon New Orleans in early May (I submitted the session [Highly-available Drupal 8 on a Raspberry Pi Cluster](https://events.drupal.org/neworleans2016/sessions/highly-available-drupal-8-raspberry-pi-cluster), hopefully it's approved!).

<p style="text-align: center;">{{< figure src="./raspberry-pi-model-3-b.jpg" alt="Raspberry Pi model 3 B from Raspberry Pi Foundation" width="500" height="440" >}}</p>

After this morning's official announcement of the [Raspberry Pi model 3 B](https://www.raspberrypi.org/blog/raspberry-pi-3-on-sale/), I placed two orders with separate vendors as quickly as possible; I'm hoping I can get at least one or two to run some benchmarks and see where the Pi Dramble can get the most benefit from the upgraded ARMv8 processor (it's a 64 bit processor with a higher base clock speed than the model 2); I'm also going to see if any of the other small improvements in internal SoC architecture make an impact on [real-world Drupal and networking benchmarks](http://www.pidramble.com/wiki/benchmarks).

I also now have three Raspberry Pi Zeros that I'm working with to build a creative, battery-powered cluster for educational purposes, but without the quad core processor of the Pi 2/3, speed is a huge limitation in what this smaller cluster (it's tiny!) can do.

At a minimum, I'll have a slightly faster single Pi for running Drupal 8 / [www.pidramble.com](http://www.pidramble.com/) from home while the cluster is on the road, using the [Drupal Pi](https://github.com/geerlingguy/drupal-pi) project!
