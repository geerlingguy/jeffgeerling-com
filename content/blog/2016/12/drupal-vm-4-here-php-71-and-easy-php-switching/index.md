---
nid: 2717
title: "Drupal VM 4 is Here! With PHP 7.1 and easy PHP switching"
slug: "drupal-vm-4-here-php-71-and-easy-php-switching"
date: 2016-12-10T22:23:09+00:00
drupal:
  nid: 2717
  path: /blog/2016/drupal-vm-4-here-php-71-and-easy-php-switching
  body_format: markdown
  redirects:
    - /blog/2016/drupal-vm-4-here-includes-php-71-easy-version-switching
aliases:
  - /blog/2016/drupal-vm-4-here-includes-php-71-easy-version-switching
tags:
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - open source
  - php
  - vagrant
---

<p style="text-align: center;">{{< figure src="./drupalvm-4-release-tag-picture.jpg" alt="Drupal VM 4.0.0 Release Tag - We&#39;ve Got Company on GitHub" width="600" height="402" class="insert-image" >}}</p>

Seven months after [Drupal VM 3](http://www.jeffgeerling.com/blog/2016/drupal-vm-3-here) introduced PHP 7.0 and Ubuntu 16.04 as the default, as well as more stable team-based development environment tooling, [Drupal VM 4](https://www.drupalvm.com) is here!

Thanks especially to the efforts of [Oskar Schöldström](https://github.com/oxyc) and [Thom Toogood](https://github.com/thom8), who helped push through some of the more tricky fixes for this release!

If you're not familiar with Drupal VM, it's a tool built with Ansible and Vagrant that helps build Drupal development environments. The fourth release brings with it even more flexibility than before. Not only can you choose between Ubuntu and CentOS, Apache and Nginx, MySQL and PostgreSQL, Memcached and Redis... you can now [seamlessly switch among PHP 5.6, 7.0, and 7.1](http://docs.drupalvm.com/en/latest/other/php/)—without having to recreate your entire development environment!

See the [4.0.0 release notes](https://github.com/geerlingguy/drupal-vm/releases/tag/4.0.0) for all the details—here are the highlights:

  - Drush is now optional (you can use the version included with your project, or not use it at all!)
  - PHP 5.6, 7.0 _and_ 7.1 are supported—and switching between them is easier than ever. Just update `php_version` and run `vagrant provision` to switch!

[Download Drupal VM](https://www.drupalvm.com) and try out one of the most popular Vagrant-based development environments.
