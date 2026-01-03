---
nid: 3008
title: "Watch out if composer update keeps replacing a dependency"
slug: "watch-out-if-composer-update-keeps-replacing-dependency"
date: 2020-05-18T21:30:48+00:00
drupal:
  nid: 3008
  path: /blog/2020/watch-out-if-composer-update-keeps-replacing-dependency
  body_format: markdown
  redirects:
    - /tags/opencv
aliases:
  - /tags/opencv
tags:
  - composer
  - drupal
  - drupal 8
  - drupal planet
  - php
  - update
  - upgrade
---

Recently, while working on the codebase for this very site, I tried running `composer update` to upgrade from Drupal 8.8.4 to 8.8.5. Apparently I did this at just the wrong time, as there was an issue with Drupal's dependencies in `8.9.x-dev` which caused _it_ to be selected as the upgrade candidate, and the default `drupal/core-recommended` Composer setting was to allow `dev` stability, so my site got updated to 8.9.x-dev, which was a bit of a surprise.

"No worries," I thought, "I use _git_, so I'm protected!" A `git reset` later, then change my `composer.json` to use `"minimum-stability": "stable"`, and all is well with the world, right?

Well, no. You see, the problem is Drupal 8.9.x changed from an abandoned package, `zendframework/zend-diactoros`, to a new package, `laminas/laminas-diactoros`, that `replaces` the abandoned package.

When Composer ran the 8.9.x upgrade, it deleted the `zendframework/zend-diactoros` library from my local `vendor` folder, and replaced it with `laminas/laminas-diactoros`. And thus, a frustrating cycle was initiated.

The next time I tried doing a `composer update`, Drupal core was upgraded to 8.8.5... but I noticed my `composer.lock` file switched, again, to `laminas/laminas-diactoros`. And this is bad, because when I deployed this update to my test environment, the environment exploded, with the message:

```
In DiactorosFactory.php line 37:
                                                                 
  Zend Diactoros must be installed to use the DiactorosFactory. 
```

Drush wouldn't work. Drupal wouldn't load pages. I couldn't clear caches (drush, Drupal, or anything).

So then I reverted the `composer.lock` file changes to the previous commit (with Drupal 8.8.4), and pushed the update to my test server. After running `composer install --no-dev`, I got the _exact same error_! How is this possible? The `composer.lock` file doesn't even _list_ the `laminas/laminas-diactoros` dependency, and yet, if I check the `vendor` folder, it's in there—and `zendframework/zend-diactoros` is _not_!

Well, I asked about this in the Drupal Slack #composer channel, and a few kind folks like alexpott, greg.1.anderson, and longwave mentioned that **Composer doesn't actually use the `composer.lock` file as the source of truth if you already have dependencies present in the vendor directory**.

This revelation blew my mind! I know in the past there has been a time or two when I've blown away the vendor directory because I accidentally messed things up badly. But those were my fault. In this case, I thought composer would use what's in the lock file as the source of truth when installing dependencies, but that is _not_ the case. If there's anything in the vendor directory that says it `replaces` a package that's in `composer.lock`, then the package in `composer.lock` will _not_ be installed.

So the solution? Delete the vendor directory entirely. Then run `composer update`. To help prevent these kinds of issues in the future, I think my future local environment workflow will be to do an entire `git clean` of my local repo from time to time (certainly before running any `composer` operations) to make sure nothing's in the vendor directory that can influence what `composer` does.

Apparently this behavior will be corrected in Composer 2.0 (though I couldn't find the issue/PR that fixes the issue explicitly to verify). Hopefully it will bring a little more sanity to my life!
