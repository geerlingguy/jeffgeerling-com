---
nid: 2658
title: "Speeding up Composer-based Drupal installation"
slug: "speeding-composer-based-drupal-installation"
date: 2016-06-06T03:07:07+00:00
drupal:
  nid: 2658
  path: /blog/2016/speeding-composer-based-drupal-installation
  body_format: markdown
  redirects: []
tags:
  - cachier
  - composer
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - drush
  - packagist
  - performance
  - prestissimo
  - vagrant
---

[Drupal VM](http://www.drupalvm.com/) is one of the most flexible and powerful local development environments for Drupal, but one the main goals of the project is to build a fully-functional Drupal 8 site quickly and easily without doing much setup work. The ideal would be to install Vagrant, clone or download the project, then run `vagrant up`. A few minutes later, you'd have a Drupal 8 site ready for hacking on!

In the past, you always had to do a couple extra steps in between, configuring a `drupal.make.yml` file and a `config.yml` file. Recently, thanks in huge part to [Oskar Schöldström's](https://github.com/oxyc) herculean efforts, we achieved that ideal by switching from defaulting to a Drush make-based workflow to a Composer-based workflow (this will come in the 3.1.0 release, very soon!). But it wasn't without trial and tribulation!

Before we switched the _default_ from Drush make to Composer, I wanted to get initial build times down so users didn't have to wait for an excruciatingly long time to download Drupal. At first, using all the defaults, it took twice as long to build a Drupal site from a `composer.json` file or using [drupal-project](https://github.com/drupal-composer/drupal-project) as it did to build the Drupal site from an [equivalent make file](https://github.com/geerlingguy/drupal-vm/blob/master/example.drupal.make.yml). The main reason is that Composer spends a lot more time than Drush in resolving project dependencies (recursively reading all `composer.json` files and downloading all the required projects into the `vendor` directory).

I thought I'd share some of the things we learned concerning speeding up Composer installs and updates for Drupal (and other PHP projects) in a blog post, so the tips aren't buried in issues in Drupal VM's issue queue:

## Use `prestissimo`

[`prestissimo`](https://github.com/hirak/prestissimo) is a Composer plugin that enables parallel installations. All you have to do is `composer global require "hirak/prestissimo:^0.3"`, and all `composer install` commands will use parallel package downloads, greatly speeding up the initial installation of Drupal.

For Drupal VM, the Drupal download time went from [400 seconds to 166 seconds](https://github.com/geerlingguy/drupal-vm/issues/699#issuecomment-223816128)—more than 2x faster for the Composer installation!

## Make sure XDebug is disabled

This one _should_ be rather obvious, but many times, developers leave XDebug enabled on the CLI, and this slows down Composer substantially—sometimes making installs take 2-4x longer! Make sure `php_xdebug_cli_enable` is `0` in Drupal VM's `config.yml` if you have `xdebug` installed in the `installed_extras` list.

## (If using Vagrant) Use `vagrant-cachier`

Many Vagrant power users already use `vagrant-cachier` with their VMs to cache `apt` or `yum` packages so rebuilds are quicker (you don't have to re-download frequently-installed packages anymore); but to use it with Composer, you need add one extra bit of configuration in your `Vagrantfile`:

```
if Vagrant.has_plugin?('vagrant-cachier')
  ... any other cachier configuration ...

  # Cache the composer directory.
  config.cache.enable :generic, :cache_dir => '/home/vagrant/.composer/cache'
end
```

We can't use `vagrant-cachier`'s built-in [Composer bucket](http://fgrehm.viewdocs.io/vagrant-cachier/buckets/composer/), because PHP isn't preinstalled on the base boxes Drupal VM uses. So we use a `:generic` bucket instead, and manually point it at the Composer cache directory inside the VM.

## Things that didn't seem to help

  - **Shallow Git clones**: Some people suggested using shallow Git clones (e.g. following [this Composer PR](https://github.com/composer/composer/pull/4961)), but it didn't make a measurable difference.
  - **`"minimum-stability": "dev"`**: In the past, setting `minimum-stability` to `dev` could speed things up a bit while Composer sorts out the dependency tree (see [this post](https://karsten.dambekalns.de/blog/stability-settings-in-composer.html)). It seems to not have any measurable impact in this case, though.
  - There are still some other areas ripe for improvement, too—for example, the `drupal-packagist` project may be able to [improve it's caching infrastructure](https://github.com/drupal-composer/drupal-packagist/issues/48) to greatly speed up download times.

Please let me know if there are other tips and tricks you may have that can help speed up Composer—we've _almost_ hit the same build times with Composer that we hit with Drush make files, but make files are still slightly faster.
