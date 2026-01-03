---
nid: 2209
title: "Drupal VM's latest update adds Redis, PHP-FPM support to Apache"
slug: "drupal-vms-latest-update-adds-redis-php-fpm-support-apache"
date: 2016-01-16T05:34:52+00:00
drupal:
  nid: 2209
  path: /blog/2016/drupal-vms-latest-update-adds-redis-php-fpm-support-apache
  body_format: markdown
  redirects: []
tags:
  - ansible
  - drupal
  - drupal planet
  - drupal vm
  - infrastructure
  - php
  - vagrant
---

> **tl;dr**: [Drupal VM 2.2.0 'Wormhole'](https://github.com/geerlingguy/drupal-vm/releases/tag/2.2.0) was released today, and it adds even more features for local dev!

Over the past few months, I've been working towards a more reliable release cadence for Drupal VM, and I've targeted one or two large features, a number of small improvements, and as many bugfixes as I have time to review. The community surrounding Drupal VM's development has been amazing; in the past few months I've noticed:

  - [Lunchbox](https://github.com/LunchboxDevTools/lunchbox), a new Node.js-based app wrapper for Drupal VM for managing local development environments.
  - A mention of using [Drupal VM + docker-selenium](https://twitter.com/kevinquillen/status/688107792272510976) for running Behat tests with Chrome or FireFox, complete with automatic screenshots of test steps!
  - A [great discussion about using Drupal VM with teams](https://github.com/geerlingguy/drupal-vm/issues/305) in the issue queue, along with a [PR](https://github.com/geerlingguy/drupal-vm/pull/378) with some ideas in code.
  - A total of 27 individual contributors to Drupal VM (who have helped me work through 307 issues and 77 pull requests), along with hundreds of contributors for the various Ansible roles that support it.

Drupal VM is the fruit of a lot of open-source effort, and one of the things that I'm most proud of is the architecture—whereas many similar projects (whether they use Docker, Vagrant, or locally-installed software) maintain an 'island' of roles/plugins/configuration scripts within one large project, I decided to build Drupal VM on top of a few dozen _completely separate_ Ansible roles, each of which serves an independent need, can be used for a variety of projects outside of Drupal or PHP-land, and is well tested, even in some cases on multiple platforms via Travis CI and Docker.

For example, the [Apache](https://github.com/geerlingguy/ansible-role-apache) and [Nginx](https://github.com/geerlingguy/ansible-role-nginx) roles that Drupal VM uses are also used for many individual's and companies' infrastructure, even if they don't even use PHP! I'm happy to see that even some other VM-based Drupal development solutions use some of the roles as a foundation, because by sharing a common foundation, all of our tooling can benefit. It's kind of like Drupal using Twig, which benefits not only our community, but all the other PHP developers who are used to Twig!

If you want to kick the tires on Drupal VM (want to [test Drupal 8 with Redis, PHP 7, Nginx, and Maria DB](http://www.midwesternmac.com/blogs/jeff-geerling/drupal-8-redis-php-7-nginx-and), or easily [benchmark Drupal 8 on PHP 7 and HHVM](http://www.midwesternmac.com/blogs/jeff-geerling/benchmarking-drupal-8-php-7-vs-hhvm)?), follow the [Quick Start Guide](https://github.com/geerlingguy/drupal-vm#quick-start-guide) and let me know how it goes!
