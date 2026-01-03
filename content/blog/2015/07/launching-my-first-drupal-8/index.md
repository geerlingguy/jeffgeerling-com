---
nid: 2503
title: "Launching my first Drupal 8 website \u2014 in my basement!"
slug: "launching-my-first-drupal-8"
date: 2015-07-31T17:48:40+00:00
drupal:
  nid: 2503
  path: /blogs/jeff-geerling/launching-my-first-drupal-8
  body_format: full_html
  redirects: []
tags:
  - dramble
  - drupal
  - drupal 8
  - drupal planet
  - infrastructure
  - raspberry pi
aliases:
  - /blogs/jeff-geerling/launching-my-first-drupal-8
---

I've been working with Drupal 8 for a long time, keeping <a href="https://www.drupal.org/project/honeypot">Honeypot</a> and some other modules up to date, and doing some dry-runs of migrating a few smaller sites from Drupal 7 to Drupal 8, just to hone my D8 familiarity.

<p style="text-align: center;"><a href="http://www.pidramble.com/">{{< figure src="./raspberry-pi-dramble-drupal-8-site.jpg" alt="Raspberry Pi Dramble Drupal 8 Website" width="450" height="327" >}}</a></p>

I finally launched a 'for real' Drupal 8 site, which is currently running on Drupal 8 HEAD—on a cluster of Raspberry Pi 2 computers <em>in my basement</em>! You can view the site at <a href="http://www.pidramble.com/">http://www.pidramble.com/</a>, and I've already started posting some articles about running Drupal 8 on the servers, how I built the cluster, some of the limitations of at-home webhosting, etc.

Some of the things I've already learned from building and running this cluster for the past few days:

<ul>
	<li>Drupal 8 (just core, alone) is <em>awesome</em>. Building out simple sites with zero contributed modules, and no custom code, is a real possibility in Drupal 8. Drupal 7 will never feel the same again :(</li>
	<li>Drupal 8 is finally fast; not super fast, but&nbsp;<em>fast enough</em>. And with some recent cache stampede protections that have been added, Drupal 8 is running much more stable in my testing—stable enough that I was finally comfortable launching a site on Drupal 8 on these Raspberry Pis!</li>
	<li>My (very) limited upload bandwidth isn't yet an issue. I only have 4-5 Mbps up, and as long as I host most images externally, serving up tiny 8-10 KB resources for normal page loads allows for a pretty large amount of traffic without a hiccup. Or, more importantly, without interfering with my day-to-day Internet use as a work-from-home employee!</li>
	<li>It's&nbsp;<em>really</em> awesome being able to see the live traffic to the servers using the LEDs on the front. See for yourself: <a href="https://www.youtube.com/watch?v=7Tf2f5gdO4I">Nginx Load Balancer Visualization w/ LEDs</a>. It's fun watching live traffic a few feet away from my desk, especially when I do things like tweet the URL (immediately following, I can see all the requests come in from Twitter-related bots!).</li>
</ul>

I'm hoping to continue writing about my experiences with Drupal 8 (especially on the Pi cluster), etc. in the next few weeks, both here and elsewhere!
