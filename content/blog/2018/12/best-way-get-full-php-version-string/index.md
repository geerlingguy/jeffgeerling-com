---
nid: 2898
title: "The best way to get the full PHP version string"
slug: "best-way-get-full-php-version-string"
date: 2018-12-16T20:47:11+00:00
drupal:
  nid: 2898
  path: /blog/2018/best-way-get-full-php-version-string
  body_format: markdown
  redirects: []
tags:
  - bash
  - docker
  - php
  - regex
  - tag
  - tutorial
  - version
---

Recently, to automate building, tagging, and pushing my [`geerlingguy/php-apache`](https://hub.docker.com/r/geerlingguy/php-apache) Docker Hub image ([see this issue](https://github.com/geerlingguy/php-apache-container/issues/9)), I needed to find a way to reliably determine the PHP major.minor.release version string. You'd think this would be simple.

Well, using Docker, I would run the image and then try:

```
# php --version
PHP 7.3.0-1+0~20181206202713.23+stretch~1.gbp076afd (cli) (built: Dec  6 2018 20:27:14) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.3.0-dev, Copyright (c) 1998-2018 Zend Technologies
    with Zend OPcache v7.3.0-1+0~20181206202713.23+stretch~1.gbp076afd, Copyright (c) 1999-2018, by Zend Technologies
```

That's great; it outputs the version right at the start. But there are a few problems here:

  - The actual version is at a different place between older and newer versions of PHP
  - I would have to add regex or string search code in bash to try to extract the version
  - I would have to maintain regex for version matching

Basically, any automated solution I want to use and not have to spend a lot of time maintaining... I avoid regex unless it's the last resort.

{{< figure src="./regex-now-i-have-two-problems-regular-expressions-picard-facepalm.jpg" alt="Regex - I had a problem so I used regular expressions - now I have two problems" width="400" height="263" class="insert-image" >}}

Reading through the [PHP docs on predefined constants](http://php.net/manual/en/reserved.constants.php), I found a really nice one: `PHP_VERSION`. Yay! Testing locally on my Mac:

```
$ php -r 'echo PHP_VERSION . "\n";'
7.2.13
```

Great! Ship it!

But wait, when I tried this in the Docker container on Debian Stretch, I got:

```
# php -r 'echo PHP_VERSION . "\n";'
7.3.0-1+0~20181206202713.23+stretch~1.gbp076afd
```

Nope. Gotta do regex again, not wanting to do that.

So in the end, I used a few other constants to build the string based on the major.minor.release components:

```
# php -r 'echo PHP_MAJOR_VERSION . "." . PHP_MINOR_VERSION . "." . PHP_RELEASE_VERSION . "\n";'
7.3.0
```

Now, why it's `PHP_VERSION`, then the components are `PHP_[something]_VERSION`... I attribute that to PHP's generally-inconsistent and annoying naming and parameter positioning insanity.

> **Note**: If you're just wanting to compare PHP versions, or check if the installed version is greater than/equal to/less than some other version, you don't need to do all this wrangling. PHP includes a built in function [`version_compare()`](http://php.net/manual/en/function.version-compare.php) which should work even with the distro-specific version string output from constants like `PHP_VERSION` and `PHP_VERSION_ID`.
