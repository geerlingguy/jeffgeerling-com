---
nid: 2954
title: "Drupal VM 5.1 ('Recognizer') brings PHP 7.4 support"
slug: "drupal-vm-51-recognizer-brings-php-74-support"
date: 2019-12-03T16:04:25+00:00
drupal:
  nid: 2954
  path: /blog/2019/drupal-vm-51-recognizer-brings-php-74-support
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - php
  - tron legacy
---

{{< figure src="./php-74-drupalvm-drupal-8.png" alt="PHP 7.4.0 running on Drupal VM with Drupal 8&#39;s status report page" width="325" height="174" class="insert-image" >}}

[Drupal VM 5.1.0](https://github.com/geerlingguy/drupal-vm/releases/tag/5.1.0) was just released (release name [Recognizer](https://www.youtube.com/watch?v=j1eI-7XWjho)), and the main feature is PHP 7.4 support; you can now begin running and testing your Drupal sites under PHP 7.4 to check for any incompatibilities.

PHP 7.4 includes some [new features](https://www.php.net/releases/7_4_0.php) like typed properties, arrow functions, and opcache preloading which could help with certain types of code or site deployments (I'm interested to see if opcache preloading could help the startup time of Drupal inside container environments like Kubernetes!).

And with the release of PHP 7.4, PHP 7.1 support was dropped—thus Drupal VM 5.1 is the first version to completely drop support for PHP 5.6, 7.0, and 7.1. In the past, it was _possible_ (though not recommended or supported) to install these older PHP versions. As of Drupal VM 5.1 it is no longer possible. So if you need to still migrate some code from an ancient codebase running on PHP 5.6 or some other unsupported version of PHP, stick with Drupal VM 5.0 until that's done.

There are a few other small bugfixes and compatibility updates in Drupal VM 5.1 (see the [CHANGELOG](https://github.com/geerlingguy/drupal-vm/blob/master/CHANGELOG.md#510-recognizer-2019-12-03) for details), but the headline feature is PHP 7.4 support. Go check it out at [DrupalVM.com](https://www.drupalvm.com)!
