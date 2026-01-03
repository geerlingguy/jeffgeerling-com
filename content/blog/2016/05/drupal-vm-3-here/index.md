---
nid: 2653
title: "Drupal VM 3 is here!"
slug: "drupal-vm-3-here"
date: 2016-05-19T21:33:19+00:00
drupal:
  nid: 2653
  path: /blog/2016/drupal-vm-3-here
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - tron
  - vagrant
---

[Drupal VM 3.0.0 "The Light Sailer"](https://github.com/geerlingguy/drupal-vm/releases/tag/3.0.0) was just released, and you can grab it from the [Drupal VM website](http://www.drupalvm.com/) now. We spent a lot of time during DrupalCon New Orleans sprinting on Drupal VM, fixing bugs, and updating ALL THE THINGS to make sure this release solves a lot of pain points for individuals and teams who need a great local development environment.

<p style="text-align: center;"><a href="http://www.drupalvm.com/">{{< figure src="./drupal-vm-homepage.jpg" alt="Drupal VM - Website Homepage" width="500" height="343" class="insert-image" >}}</a></p>

Let's get right into why this is the best release of Drupal VM EVER!

## The fastest and most modern environment

Drupal VM now defaults to Ubuntu 16.04 (which was just released in late April), running MySQL 5.7 and PHP 7. This means you're getting the fastest, most reliable, and most modern development environment for your Drupal 8 projects.

But you can still stick with any of the old OSes and versions of PHP just like you always could: Ubuntu 16.04, 14.04, and 12.04, as well as CentOS 7 and 6, and even Debian Jessie or Wheezy are supported out of the box! _Technically_, you can still run any version of PHP from 5.1 to 7.0 in Drupal VM (depending on OS selection)... but only PHP 5.5+ is supported right now.

Also, for 2.5.1, [Blackfire.io](https://blackfire.io/) support was added, so you can now profile in any PHP version with either Blackfire or XHProf! (There was a [great session on Blackfire](https://events.drupal.org/file/drupalcon-new-orleans-2016-using-blackfireio-profile-your-loading-time) at DrupalCon NOLA.)

## The best team-based development environment

New features in Drupal VM allow teams to do the following:

  - Add Drupal VM as a composer.json dependency (that's right, [Drupal VM is on Packagist!](https://packagist.org/packages/geerlingguy/drupal-vm) - [docs](http://docs.drupalvm.com/en/latest/other/drupalvm-composer-dependency/))
  - Commit a shared `config.yml`, and let developers override only the settings they need in a `local.config.yml` ([docs](http://docs.drupalvm.com/en/latest/other/overriding-configurations/#overriding-variables-in-configyml-with-a-localconfigyml))
  - Use Drupal VM and Vagrant in a subfolder, meaning you don't have to `cd` into the Drupal VM directory to run commands like `vagrant up`
  - Use a custom Vagrantfile to add in or modify Drupal VM's default Vagrant configuration ([docs](http://docs.drupalvm.com/en/latest/other/overriding-configurations/#extending-the-vagrantfile-with-vagrantfilelocal)).
  - Add custom shell scripts and/or Ansible task files to be run before and/or after provisioning ([docs](http://docs.drupalvm.com/en/latest/extras/scripts/))

This is the best release yet for development teams, because Drupal VM can be configured specifically for a particular Drupal site—and then parts of the configuration can be overridden by individual developers without any hacks!

## A stable, reliable upgrade path

During the course of the Drupal VM 2.x series, one of the major pain points was upgrading Drupal VM to newer versions. At the [Drupal VM BoF](https://events.drupal.org/neworleans2016/bofs/drupal-vm-and-local-drupal-development-teams) at DrupalCon, many people mentioned that every time they upgraded Drupal VM, they ended up with some random errors that caused friction. Even if _not_ upgrading, certain Ansible roles would cause problems with older versions of Drupal VM!

Drupal VM now specifies versions of Ansible roles that are used to build the VM (as of 2.5.1), so if you download Drupal VM today, and don't upgrade for a long time, everything should keep working. And if you upgrade to a new version, and read through the release notes, you should have a smooth upgrade process.

## 600+ stars!

When I started working on Drupal VM, I just tossed my own local Vagrant configuration on GitHub and hoped someone else would see some good ideas in it. When the project had 50 stars (then 100, then 200), I was amazed, and wondered when interest in Drupal VM would start waning.

<p style="text-align: center;"><a href="https://galaxy.ansible.com/explore#/">{{< figure src="./ansible-role-downloads-galaxy.jpg" alt="Ansible Galaxy - Explore Role Downloads" width="292" height="300" class="insert-image" >}}</a></p>

Lo and behold, a couple years in, Drupal VM has been starred over 600 times, and all the most downloaded roles on Ansible Galaxy are roles used in Drupal VM! It's also humbling, and quite awesome, to meet a complete stranger at DrupalCon who uses Drupal VM; thank you to all those who have used Drupal VM, have helped with all the open source Ansible Galaxy roles, and also help fight the good fight of _automating all the infrastructure things_ for Drupal!

Special thanks to all the users who have contributed to the last few releases: [oxyc](https://github.com/oxyc), [rodrigoeg](https://github.com/rodrigoeg), [thom8](https://github.com/thom8), [scottrigby](https://github.com/scottrigby), [iainhouston](https://github.com/iainhouston), [quicksketch](https://github.com/quicksketch), [Mogtofu33](https://github.com/Mogtofu33), [stevepurkiss](https://github.com/stevepurkiss), [slimatic](https://github.com/slimatic), [sarahjean](https://github.com/sarahjean), [nerdstein](https://github.com/nerdstein) and [derimagia](https://github.com/derimagia) (this list is not exhaustive, and I know I met more people at DrupalCon who helped but I forgot to mention here—please let me know if I forgot about you in the comments!).

## What the future holds

I'm starting to work on better planning for future releases (e.g. 3.1.0, etc.), and you can always check the [Drupal VM issue queue](https://github.com/geerlingguy/drupal-vm/issues) (especially 'Milestones') to see the latest. Somewhere down the line, parts of Drupal VM will likely start using Docker and/or other containerization tech to make builds and rebuilds much faster. There are already some users exploring the [use of `vagrant-lxc` on Linux](https://github.com/geerlingguy/drupal-vm/issues/649) for speedier builds!

Where will we go for 4.0? I'm not quite sure yet... but I'll keep the guiding principles for my own development environment in mind:

  - Fast and flexible
  - Stable and secure (for local dev, at least)
  - Cross-platform compatible

Please [download Drupal VM](http://www.drupalvm.com/), try it out, and see what you think!
