---
nid: 2767
title: "Composer BoF at DrupalCon Baltimore"
slug: "composer-bof-drupalcon-baltimore"
date: 2017-04-25T20:07:44+00:00
drupal:
  nid: 2767
  path: /blog/2017/composer-bof-drupalcon-baltimore
  body_format: markdown
  redirects: []
tags:
  - appearances
  - baltimore
  - bof
  - composer
  - drupal
  - drupal planet
  - drupalcon
  - php
---

> **Update**: The BoF has come and passed... and I put up a comprehensive summary of the session here: [Composer and Drupal are still strange bedfellows](/blog/2017/composer-and-drupal-are-still-strange-bedfellows).

Tomorrow (Wednesday, April 25), I'm leading a Birds of a Feather (BoF) at DrupalCon Baltimore titled [_Managing Drupal sites with Composer_](https://events.drupal.org/baltimore2017/bofs/managing-drupal-sites-composer) (3:45 - 4:45 p.m. in room 305).

{{< figure src="./logo-composer-transparent.png" alt="Composer for PHP - Logo" width="145" height="178" class="insert-image" >}}

I've built four Drupal 8 websites now, and for each site, I have battle scars from working with Composer (read my [Tips for Managing Drupal 8 projects with Composer](//www.jeffgeerling.com/blog/2017/tips-managing-drupal-8-projects-composer)). Even some of the tools that I use alongside composer—for project scaffolding, managing dependencies, patching things, etc.—have changed quite a bit over the past year.

As more and more Drupal developers adopt a Composer workflow for Drupal, we are solving some of the most painful problems.

For example:

  - Should I use the `composer.json` that's included with Drupal core? If so, why is there also a `.lock` file included? (See issue: [Improve instructions for updating composer.json and /vendor](https://www.drupal.org/node/2867757)).
  - I just installed Webform and now it's yelling at me about front-end libraries. How do I install front-end libraries with Composer, _especially if they're not on Packagist_?
  - What's the best way (or _ways_) to set up your Drupal project using Composer? (See discussions about this on Drupal.org: [1](https://www.drupal.org/node/2845379), [2](https://www.drupal.org/node/2477789), [3](https://www.drupal.org/node/2551607)).
  - Is it a best practice to commit the `vendor` directory or not? Why?
  - Sometimes I see tildes (`~`), other times `^`, and sometimes Composer yells at me when I try to add a module that has a beta release. Why is this stuff so confusing? I just want to add a module!
  - I download tarballs or zip files of modules and drag them into my codebase. What's the best way to install modules like [Search API Solr](https://www.drupal.org/project/search_api_solr) or [Address](https://www.drupal.org/project/address), when they require Composer?

Some of these questions have answers. Some are still being debated on a daily basis!

I'd love to see you come to the BoF tomorrow if you're at DrupalCon, and you want to talk about Composer and Drupal. I'll try to take notes and post them on my blog as well.
