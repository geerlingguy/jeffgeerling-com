---
nid: 3026
title: "Drupal VM 6 'Rectifier' is here!"
slug: "drupal-vm-6-rectifier-here"
date: 2020-07-14T17:17:43+00:00
drupal:
  nid: 3026
  path: /blog/2020/drupal-vm-6-rectifier-here
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal 9
  - drupal planet
  - drupal vm
---

<a href="https://www.drupalvm.com">{{< figure src="./drupal-vm-logo-teaser.png" alt="Drupal VM logo and teaser text" width="546" height="193" class="insert-image" >}}</a>

I just released [Drupal VM 6.0.0](https://github.com/geerlingguy/drupal-vm/releases/tag/6.0.0) today, and it is the best version of Drupal VM yet!

The main goals for this new version are **stability** and **compatibility**.

Originally I was going to drop some features that are helpful for people running older Drupal 7 sites, but since [Drupal 7's End of Life was just extended into 2022](https://www.drupal.org/psa-2020-06-24), I decided to extend the support for some features like Drush make files, as many users of Drupal VM still maintain Drupal 7 sites, or use Drupal VM to test the upgrade from Drupal 7 to Drupal 8 or 9.

The default PHP version was upgraded from PHP 7.2 to 7.4 in Drupal VM 6, and this new version should work great with almost any Drupal 7, 8, or 9 website (in fact, PHP 7.3 is Drupal 9's minimum requirement!).

The final major feature is defaulting everything to Drupal 9. Drupal VM gives you easy tools to build a new Drupal 9 website no matter what OS you use, and now when you build a new website, you get Drupal 9 by default!

If you're already using Drupal VM, go check out the [release notes](https://github.com/geerlingguy/drupal-vm/releases/tag/6.0.0) to make sure you update your configuration for the new version, then upgrade to 6.0.0. If you don't use it, now's a great time to [try it out](https://www.drupalvm.com)!
