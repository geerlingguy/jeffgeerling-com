---
nid: 2720
title: "Upgrading Drupal VM in a BLT-powered project"
slug: "upgrading-drupal-vm-blt-powered-project"
date: 2016-12-20T20:28:46+00:00
drupal:
  nid: 2720
  path: /blog/2017/upgrading-drupal-vm-blt-powered-project
  body_format: markdown
  redirects:
    - /blog/2016/upgrading-drupal-vm-blt-powered-project
aliases:
  - /blog/2016/upgrading-drupal-vm-blt-powered-project
tags:
  - acquia
  - blt
  - composer
  - drupal
  - drupal planet
  - drupal vm
  - php
---

> **Update 2017-02-14**: BLT now includes a much simpler method of upgrading the VM (provided you only override VM settings in files separate from the `box/config.yml` file):
> 
>     # Delete the entire VM and remove config.
>     blt vm:nuke
> 
>     # Rebuild the VM with the latest recommended version and config.
>     blt vm

Limiting the amount of surprises you get when developing a large-scale Drupal project is always a good thing. And to that end, Acquia's [BLT](https://github.com/acquia/blt) (Build and Launch Tools) wisely chooses to leave Drupal VM alone when updating BLT itself. Updates to Drupal VM can and should be done independently of install profile and development and deployment tooling.

<p style="text-align: center;">{{< figure src="./composer-require-drupal-vm.png" alt="composer require geerlingguy/drupal-vm:~4.0" width="650" height="244" class="insert-image" >}}</p>

But this creates a conundrum: how do you upgrade Drupal VM within a project that uses BLT and has Drupal VM as one of it's composer dependencies? It's actually quite simple—and since I just did it for one of my projects, I thought I'd document the process here for future reference:

  1. In your project's root, require the newer version of Drupal VM: `composer require --dev geerlingguy/drupal-vm:~4.0` (in my case, I was updating from the latest 3.x release to 4.x).
  2. Edit your `box/config.yml` file—it's best to either use BLT's [current `config.yml` template](https://github.com/acquia/blt/blob/8.x/scripts/drupal-vm/config.yml) as a guide for updating yours, or read through the [Drupal VM release notes](https://github.com/geerlingguy/drupal-vm/releases) to find out what config variables need to be added, changed, or removed.
  3. Commit the updates to your code repository.
  4. (If updating major versions) Instruct all developers to run `vagrant destroy -f`, then `vagrant up` to rebuild their local environments fresh, on the new version. (If updating minor versions) Instruct all developers to run `vagrant provision` to update their environments.

There are a lot of great new features in Drupal VM 4, like the ability to switch PHP versions in the VM on-the-fly. This is great for those testing migrations from PHP 5.6 to 7.0 or even 7.1! There's never been an easier and quicker way to update your projects to the latest VM version.
