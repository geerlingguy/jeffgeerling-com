---
nid: 2918
title: "Drupal VM 5 ('Flynn Lives') brings updates to all the things!"
slug: "drupal-vm-5-flynn-lives-brings-updates-all-things"
date: 2019-04-09T21:10:23+00:00
drupal:
  nid: 2918
  path: /blog/2019/drupal-vm-5-flynn-lives-brings-updates-all-things
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal planet
  - drupal vm
  - local development
  - open source
  - vagrant
---

It's been five years since [Drupal VM](https://www.drupalvm.com)'s first release, and to celebrate, it's time to release **Drupal VM 5.0 "Flynn Lives"**! This update is not a major architectural shift, but instead, a new major version that updates many defaults to use the latest versions of the base VM OS and application software. Some of the new default versions include:

  - Ubuntu 18.04 'Bionic' LTS (was Ubuntu 16.04)
  - PHP 7.2 (was PHP 7.1)
  - Node.js 10.x (was Node.js 6.x)

See the full release notes here: [Drupal VM 5.0.0 "Flynn Lives"](https://github.com/geerlingguy/drupal-vm/releases/tag/5.0.0)

There are also a number of other small improvements (as always), and ever-increasing test coverage for all the Ansible roles that power Drupal VM. And in the Drupal VM 4.x release lifecycle, a new official pre-baked Drupal VM base box was added, the [geerlingguy/drupal-vm](https://app.vagrantup.com/geerlingguy/boxes/drupal-vm) Vagrant base box. Using that base box can speed up new VM builds by 50% or more!

And, as always, it's easy to override _any_ of these settings and versions by adjusting variables in your `config.yml`. Current supported VM OSes include Ubuntu 18.04 or 16.04, Debian 9, and CentOS 7. Current supported PHP versions include PHP 7.1, 7.2, or 7.3 (note that 5.6 still _works_ but is not officially supported—make sure you upgrade your sites soon and stop using this unsupported PHP version!).

Many people have asked if I'm going to turn Drupal VM entirely into a Docker-backed tool, instead of using Vagrant and VirtualBox; I have decided over the past year that I would rather keep the basic architecture I have now, as it's extremely mature, supports a lot of custom use cases, and has some benefits over a Docker-based architecture, especially for Mac or Windows developers. Also, if you _do_ wish to use a Docker-based tool, there are now multiple mature projects to choose from like [Docksal](https://docksal.io), [Ddev](https://www.drud.com/what-is-ddev/), or [Lando](https://docs.devwithlando.io). (I personally use a mixture of Drupal VM and custom docker-compose-based local development environments for my own projects.)

Finally, if you're interested in the current state of local development tools used by the Drupal community, be sure to check out a session I'm co-presenting with Chris Urban at DrupalCon Seattle: [What should I use? 2019 Developer Tool Survey Results](https://events.drupal.org/seattle2019/sessions/what-should-i-use-2019-developer-tool-survey-results).
