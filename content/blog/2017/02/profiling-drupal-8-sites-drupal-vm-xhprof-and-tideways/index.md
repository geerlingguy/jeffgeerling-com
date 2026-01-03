---
nid: 2743
title: "Profiling Drupal 8 Sites in Drupal VM with XHProf and Tideways"
slug: "profiling-drupal-8-sites-drupal-vm-xhprof-and-tideways"
date: 2017-02-11T14:30:23+00:00
drupal:
  nid: 2743
  path: /blog/2017/profiling-drupal-8-sites-drupal-vm-xhprof-and-tideways
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - performance
  - profile
  - tideways
  - tutorial
  - xhprof
---

XHProf, a PHP extension formerly created and maintained by Facebook, has for many years been the de-facto standard in profiling Drupal's PHP code and performance issues. Unfortunately, as Facebook has matured and shifted resources, the XHProf extension maintenance tailed off around the time of the PHP 7.0 era, and now that we're hitting PHP 7.1, even some sparsely-maintained forks are difficult (if not impossible) to get running with newer versions of PHP.

Enter [Tideways](https://tideways.io).

Tideways has basically taken on the XHProf extension, [updated it for modern PHP versions](https://tideways.io/profiler/xhprof-for-php7-php5.6), but also re-branded it to be named 'Tideways' instead of 'XHProf'. This has created a little confusion, since Tideways also offers a branded and proprietary service for aggregating and displaying profiling information through [Tideways.io](https://tideways.io). But **you can use Tideways completely independent from Tideways.io**, as a drop-in replacement for XHProf. And you can even browse profiling results using the same old XHProf UI!

So in this blog post, I want to show you how you can use Drupal VM (version 4.2 or later) to quickly and easily profile Drupal 8 pages using Tideways (the PHP extension), the XHProf UI, and the XHProf Drupal module (all running locally—no cloud connection or paid service required!). You can even get fancy callgraph images!

Here's a video walkthrough for the more visually-inclined:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/U37YkPach3Q" frameborder='0' allowfullscreen></iframe></div>

## Configure Drupal VM to install Tideways

The only thing you need to do to a stock Drupal VM configuration is make sure `tideways` is in your list of `installed_extras`. So, for my VM instance, I created a `config.yml` file and put the following inside:

```
---
installed_extras:
  - drush
  - mailhog
  - tideways
```

You can add whatever other `installed_extras` you need, but for this testing and benchmarking, I'm only including the essentials for my site.

If you want to have Drupal VM build a Drupal 8 site for you, and also automatically `composer require` the XHProf module for Drupal 8, you can also add:

```
drupal_composer_dependencies:
  - "drupal/xhprof:1.x-dev"
```

This will ensure that, after a Drupal 8 codebase is generated, the appropriate `composer require` command will be run to add the [Drupal XHProf module](https://www.drupal.org/project/xhprof) to the codebase and the `composer.json` file. You could even add `xhprof` to the array of `drupal_enable_modules` in `config.yml` if you want the module _installed_ automatically during provisioning!

Run `vagrant up` to start Drupal VM and provision it with Tideways, or run `vagrant provision` if you already have Drupal VM set up and are just adding Tideways to it.

## Install Drupal's XHProf module

After Vagrant finishes provisioning Drupal VM, you can enable the XHProf module with `drush @drupalvm.drupalvm.dev en -y xhprof` (or do it via the 'Extend' page in Drupal's UI). Then, to configure the module to collect profiles for page loads, do the following:

  1. Visit the XHProf configuration page: `/admin/config/development/xhprof`
  2. Check the 'Enable profiling of page views' checkbox.
  3. Make sure the 'Tideways' extension is selected (it should be, by default).
  4. Check the 'Cpu' and 'Memory' options under 'Profile'
  5. Click 'Save' to save the settings.

## Profile a page request!

{{< figure src="./xhprof-profile-link-drupal-module.png" alt="XHProf Profile link from Drupal module" width="325" height="225" class="insert-image" >}}

  1. Visit any page on the site (outside of the admin area, or any of the other paths excluded in the XHProf 'Exclude' configuration).
  2. Find the 'XHProf output' link near the bottom of the page.
  3. Click the link, and you'll see the XHProf module's rendering of the profile for that page.

For more basic profiling, that's all you need to do. But Drupal VM's Tideways integration _also_ automatically sets up the XHProf GUI so you can browse the results in a much more efficient and powerful way. To use the more powerful XHProf GUI:

  1. Visit `http://xhprof.drupalvm.dev/` (or `xhprof.[yoursiteurl]`).
  2. Click on a profile result in the listing.

{{< figure src="./drupal-8-home-profile-xhprof-gui-interface.png" alt="Drupal 8 home page XHProf profile GUI" width="650" height="399" class="insert-image" >}}

In here, you have access to much more granular data, including a full 'callgraph', which is a graphical representation of the _entire_ request flow. Note that it can take a minute or longer to render callgraphs for more complex page loads!

Here's a small snippet of what Drupal 8's home page looks like with empty caches:

{{< figure src="./drupal-8-home-callgraph-logged-in-no-cache.png" alt="Drupal 8 home page callgraph rendered by XHProf GUI" width="650" height="451" class="insert-image" >}}

## Alternatives

If you're still running PHP 5.6 or 7.0, you can still use XHProf, but it seems like XHProf's maintenance is now in a perpetually fuzzy state—nobody's really picked up the ball consistently after Facebook's maintenance of the extension dropped off.

Another service which has a freemium model but requires the use of a web UI rather than a locally-hosted UI is [Blackfire](https://blackfire.io), which is _also_ [supported by Drupal VM](http://docs.drupalvm.com/en/latest/extras/blackfire/) out of the box!
