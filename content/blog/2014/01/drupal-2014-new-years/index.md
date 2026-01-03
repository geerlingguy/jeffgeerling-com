---
nid: 2443
title: "Drupal 2014 - New Year's Resolutions"
slug: "drupal-2014-new-years"
date: 2014-01-01T04:49:45+00:00
drupal:
  nid: 2443
  path: /blogs/jeff-geerling/drupal-2014-new-years
  body_format: full_html
  redirects: []
tags:
  - backdrop
  - drupal
  - drupal 8
  - drupal planet
  - php
aliases:
  - /blogs/jeff-geerling/drupal-2014-new-years
---

2014 is going to be a big year for Drupal. I spent a lot of 2013 sprucing up services like <a href="http://hostedapachesolr.com/">Hosted Apache Solr</a> and <a href="http://servercheck.in/">Server Check.in</a> (both running on Drupal 7 currently), and porting some of my Drupal projects to Drupal 8.

So far I've made great progress on <a href="https://drupal.org/project/honeypot">Honeypot</a> and <a href="https://drupal.org/project/wysiwyg_linebreaks">Wysiwyg Linebreaks</a>, which I started migrating a while back. Both modules work and pass all tests on Drupal's current dev/alpha release, and I plan on following through with the <a href="http://d8cx.org/">D8CX</a> pledges I made months ago.

Some of the other modules I maintain, like <a href="https://drupal.org/project/gallery_archive">Gallery Archive</a>, <a href="https://drupal.org/project/login_as_other">Login as Other</a>, <a href="https://drupal.org/project/simple_mail">Simple Mail</a>, and themes like <a href="https://drupal.org/project/mm">MM - Minimalist Theme</a>, are due to be ported sooner rather than later. I'm really excited to start working with <a href="https://drupal.org/node/2008464">Twig</a> in Drupal 8 (finally, a for-real front-end templating engine!), so I'll probably start working on themes in early 2014.

<h3>Drupal in 2014</h3>

<p style="text-align: center;">{{< figure src="./drupal-8-logo.png" alt="Drupal 8 Logo" width="200" height="205" >}}</p>

2013 was an interesting year for Drupal, with some major growing pains. Drupal 8 is architecturally more complex (yet simpler in some ways) than Drupal 7 (which was more complex than Drupal 6, etc.), and the degree of difference caused some developer angst, even leading to a fork, <a href="http://backdropcms.org/">Backdrop</a>. Backdrop is developing organically under the guidance of Nate Haug, but it remains to be seen what effect it will have on the wider CMS scene, and on Drupal specifically.

One very positive outcome of the fork that some of the major Drupal 8 DX crises (mostly caused by switching gears to an almost entirely-OOP architecture) are being resolved earlier in the development cycle. As with any Drupal release cycle, the constant changes can sometimes frustrate developers (like me!) who decide to start migrating modules well before code/API freeze. But if you've been a Drupal developer long enough, you know that the <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/the-drupal-way">drop is always moving</a>, and the end result will be much better for it.

Drupal 8 is shaping up to be another major contender in the CMS market, as it includes so many timely and necessary features in core (Views, config management, web services, better blocks, Twig, Wysiwyg, responsive design everywhere, great language support, etc.). I argue it's hard to beat Drupal 8 <em>core</em>, much less core + contrib, with any other solution available right now, for any but the simplest of sites.

One remaining concern I have with Drupal 8 is performance; even though you can cover some performance problems with caching layers, the core, uncached Drupal experience is historically pretty slow, even without a bevy of contrib modules thrown in the mix. Drupal's new foundation (<a href="http://symfony.com/">Symfony</a>) will help in some aspects (probably more so in more complicated environments—sometimes Symfony is <a href="http://www.techempower.com/benchmarks/">downright slow</a>), and there are <a href="https://drupal.org/node/1744302">issues</a> open to try to fix some known regressions, but being a performance nut, I like it when I can shave tens to hundreds of ms per request, even on a simple LAMP server!

Unlike Drupal 7's sluggish adoption—it was months before most people considered migrating, mostly because Views, and to a lesser extent, the Migrate module, was not ready for some time after release—I think some larger sites will begin migrating to 8 with the first release candidate (there are already some personal sites and blogs using alpha builds). For example, when I migrate Server Check.in, I can substantially reduce the lines of custom code I maintain, and build a more flexible core, simply because Drupal 8 offers more flexible and reliable solutions in core, most especially with Views and Services.

Drupal 8 is shaping up to be the most exciting Drupal release to date—what are your thoughts as we enter this new year? Oh, and <em>Happy New Year!</em>
