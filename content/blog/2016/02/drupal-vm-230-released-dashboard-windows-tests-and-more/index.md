---
nid: 2619
title: "Drupal VM 2.3.0 released - dashboard, Windows, tests, and more"
slug: "drupal-vm-230-released-dashboard-windows-tests-and-more"
date: 2016-02-22T15:07:49+00:00
drupal:
  nid: 2619
  path: /blog/2016/drupal-vm-230-released-dashboard-windows-tests-and-more
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal planet
  - drupal vm
  - vagrant
---

> Update: I just posted a new video about Drupal VM, [Drupal VM - Quick Introduction](https://www.youtube.com/watch?v=PR9uh_GGZhI), covering some of these new features!

I'm excited to announce the release of [Drupal VM 2.3.0 "Miracle and Magician"](https://github.com/geerlingguy/drupal-vm/releases/tag/2.3.0)—with over 21 new features and bugs fixed!

One of the most amazing improvements is the new Drupal VM dashboard; after you build Drupal VM, visit the VM's IP address to see all the sites, tools, and connection details in your local development environment:

<p style="text-align: center;">{{< figure src="./drupal-vm-dashboard-230.jpg" alt="Drupal VM 2.3.0 release - new dashboard UI" width="650" height="458" >}}</p>

This feature was singlehandedly implemented by [Oskar Schöldström](https://github.com/oxyc)—who also happens to have practically matched my commit activity for the past month or so. I'm pretty sure I owe him something like 100 beers at this point!

Here are some of the other great new features of Drupal VM in 2.3.0:

  - **Greater stability on Windows** and when Ansible is not installed on a Mac/Linux host.
  - **Full test coverage using Docker containers on Travis CI**—instead of just testing syntax, we're fully installing Drupal VM in two Ubuntu 14.04 and one CentOS 7 environment to test every aspect of Drupal VM.
  - **Deployment to a DigitalOcean droplet** - this is an experimental feature for now, but you can easily build a more secure Drupal VM instance on the Cloud using nothing but Ansible.
  - **Vastly improved and expanded documentation**
  - **Support for a local Vagrantfile** - this allows you to easily override the default Vagrant configuration if needed

For more information about this release, check out the [2.3.0 Release Notes](https://github.com/geerlingguy/drupal-vm/releases/tag/2.3.0).
