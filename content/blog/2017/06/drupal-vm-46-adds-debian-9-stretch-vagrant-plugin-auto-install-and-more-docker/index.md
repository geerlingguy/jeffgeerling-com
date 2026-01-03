---
nid: 2791
title: "Drupal VM 4.6 adds Debian 9 (Stretch), Vagrant plugin auto-install, and more Docker"
slug: "drupal-vm-46-adds-debian-9-stretch-vagrant-plugin-auto-install-and-more-docker"
date: 2017-06-29T12:30:28+00:00
drupal:
  nid: 2791
  path: /blog/2017/drupal-vm-46-adds-debian-9-stretch-vagrant-plugin-auto-install-and-more-docker
  body_format: markdown
  redirects: []
tags:
  - debian
  - docker
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - vagrant
---

[Drupal VM](https://www.drupalvm.com) has been hitting its stride this year; after adding experimental Docker support in 4.5, Docker usage has been refined in 4.6 (with a more stable and _useful_ [drupal-vm Docker image](https://hub.docker.com/r/geerlingguy/drupal-vm/), along with a few other things:

  - Drupal VM now supports running inside a Debian 9 'Stretch' Vagrant box ([Packer build here](https://github.com/geerlingguy/packer-debian-9), and [Vagrant Cloud box here](https://app.vagrantup.com/geerlingguy/boxes/debian9)), _or_ in a Docker container [based on Debian 9](https://hub.docker.com/r/geerlingguy/docker-debian9-ansible/).
  - The official Docker image includes a script that lets you set up a fresh Drupal site (any version supported by Drush!) with the command `docker exec drupalvm install-drupal` (seriously, [check it out!](http://docs.drupalvm.com/en/latest/other/docker/#method-1-get-a-quick-drupal-site-installed-with-drupal-vms-docker-image).
  - Essential Vagrant plugins that automatically update your hosts file and ensure the VM has the right version of VirtualBox Guest Additions are now automatically installed—though you can disable the feature, or even add in additional essential plugins if you so desire.

I think the fact that adding Debian 9 support took less than one hour is a testament to the approach we've* taken with Drupal VM. Every component is mixed in from an upstream Ansible role—all the roles work on multiple OSes, and have [full automated test coverage _on all those OSes_](https://www.jeffgeerling.com/blog/2016/how-i-test-ansible-configuration-on-7-different-oses-docker), and are easily composable (Drupal VM is one of _many_ diverse projects that benefit from the roles' modularity).

{{< figure src="./docker-drupalvm-quick-drupal-install.gif" alt="Drupal VM on Docker - Quick Drupal site installation" width="580" height="350" class="insert-image" >}}

And taking the note about the Docker image's Drupal install script a little further, if you have Docker installed, try the following to see how quick it is to get started with Drupal VM on Docker:

  1. `docker run -d -p 80:80 -p 443:443 --name=drupalvm --privileged geerlingguy/drupal-vm`
  2. `docker exec drupalvm install-drupal` (optionally add a version after a space, like `8.4.x` or `7.56`).
  3. Open your browser, and visit [http://localhost/](http://localhost/)

Read more about [using Drupal VM with Docker](http://docs.drupalvm.com/en/latest/other/docker/) in the official documentation.

I'm beginning some exciting experimentation using [Ansible Container](https://github.com/ansible/ansible-container) to build Docker images 1:1 to many of the Ansible roles I maintain, and I can't wait to share some of the optimizations I'm working on that will make Drupal VM continue to be one of the most flexible and performant development (and even production!) environments for PHP projects.

* I say _we've_, because I am extremely indebted to many consistent contributors to Drupal VM and all the upstream projects. Were it not for their hard work and ideas, I would likely not have tidied up a lot of these niceties in time for a 4.6 release! Thanks especially to co-maintainer [oxyc](https://github.com/oxyc), who somehow has time for fixing all the hard bugs :)
