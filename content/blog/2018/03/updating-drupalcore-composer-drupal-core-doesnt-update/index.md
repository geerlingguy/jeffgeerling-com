---
nid: 2832
title: "Updating drupal/core with Composer - but Drupal core doesn't update"
slug: "updating-drupalcore-composer-drupal-core-doesnt-update"
date: 2018-03-22T14:31:41+00:00
drupal:
  nid: 2832
  path: /blog/2018/updating-drupalcore-composer-drupal-core-doesnt-update
  body_format: markdown
  redirects: []
tags:
  - composer
  - drupal
  - drupal planet
  - update
  - upgrade
---

For the past two minor release Drupal core upgrades, I've had major problems trying to get some of my Composer-based Drupal codebases upgraded. For both 8.3.x to 8.4.0, and now 8.4.x to 8.5.0, I've had the following issue:

  1. I have the version constraint for `drupal/core` set to `~8.0` or `~8.4` in my `composer.json`.
  1. I run `composer update drupal/core --with-dependencies` (as recommended [in Drupal.org's Composer documentation](https://www.drupal.org/docs/8/update/update-core-via-composer-option-4)).
  1. Composer does its thing.
  1. A few things get updated... but not `drupal/core`. It remains stubbornly on the previous minor release.

Looking around the web, it seems this is a _very_ common problem, and a lot of people soon go for the nuclear (or thermonuclear<sup>1</sup>) option:

  1. Run `composer update` (updating everything in the entire project, contrib modules, core, other dependencies, etc.).
  1. Profit?

This _works_, but it's definitely not ideal. If you have a site that uses a number of contrib modules, and maybe even depends on some of their APIs in custom code or in a custom theme... you don't want to be upgrading core and all contrib modules all in one go. You want to update each thing independently so you can test and make sure things don't break.

So, I was searching around for 'how do I figure out why updating something with Composer doesn't update that thing?', and I got a few good answers. The most important is the command `composer prohibits`.

## Use `composer prohibits` to figure out what's blocking an update

`composer prohibits` allows you to see exactly what is preventing a package from being updated. For example, on this codebase, I know I want to end up with `drupal/core:8.5.0`, so I can run:

    composer prohibits drupal/core:8.5.0

This gave me a list of a ton of different Symfony components that seemed to be holding back the upgrade, for example:

```
drupal/core                     8.5.0       requires          symfony/class-loader (~3.4.0)
drupal-composer/drupal-project  dev-master  does not require  symfony/class-loader (but v3.2.14 is installed)
drupal/core                     8.5.0       requires          symfony/console (~3.4.0)
drupal-composer/drupal-project  dev-master  does not require  symfony/console (but v3.2.14 is installed)
drupal/core                     8.5.0       requires          symfony/dependency-injection (~3.4.0)
...
```

## Add any blocking dependencies to `composer update`

So, knowing this, one quick way I can get around this problem is to include `symfony/*` to update the symfony components at the same time as `drupal/core`:

    composer update drupal/core symfony/* --with-dependencies

Unfortunately, it's more difficult to figure out which dependencies _exactly_ are blocking the update. You'd think all of the ones listed by `composer prohibits` are blocking the upgrade, but as it turns out, only the `symfony/config` dependency (which is a dependency of Drush and/or Drupal Console, but not Drupal core) was blocking the upgrade on this particular site!

I learned a bit following the discussion in the Drupal.org issue [composer fail to upgrade from 8.4.4 to 8.5.0-alpha1](https://www.drupal.org/project/drupal/issues/2943546), and I also contributed a new answer to the Drupal Answers question [Updating packages with composer and knowing what to update](https://drupal.stackexchange.com/a/258281/26). Finally, I updated the Drupal.org documentation page [Update core via Composer (option 4)](https://www.drupal.org/docs/8/update/update-core-via-composer-option-4) and added a little bit of the information above in the troubleshooting section, because I'm _certain_ I'm not the only one hitting these issues time and again, every time I try to upgrade Drupal core using Composer!

<hr>

<sup>1</sup> <em>The thermonuclear option with Composer is to delete your vendor directory, delete your lock file, hand edit your `composer.json` with newer package versions, then basically start over from scratch. IMO, this is always a bad idea unless you feel safe upgrading all the things all the time (for some simple sites, this might not be the worst idea, but it still removes all the dependency management control you get when using Composer properly).</em>
