---
nid: 2932
title: "Discovering whether an Ansible component is 'core' or 'community'"
slug: "discovering-whether-ansible-component-core-or-community"
date: 2019-08-13T22:20:08+00:00
drupal:
  nid: 2932
  path: /blog/2019/discovering-whether-ansible-component-core-or-community
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansibot
  - documentation
  - maintenance
  - open source
  - redhat
---

As you get deeper into your journey using Ansible, you might start filing issues on GitHub, chatting in #ansible on Freenode IRC, or otherwise interacting more with the Ansible community. Because the Ansible community has grown tremendously over the years—and as Ansible has been subsumed by Red Hat, which has various support plans for Ansible—there's been a greater distinction between parts of Ansible that are 'core' (e.g. maintained by the Ansible Engineering Team) and those that are not.

When everything works, and when you're living in a world where security and compliance requirements are fairly free, you would never even care about the support for Ansible components (modules, plugins, filters, Galaxy content). But if something goes wrong, or if there are security or compliance concerns, it is important to be able to figure out what's core, what's 'certified' by Red Hat, and what's not.

For Ansible _modules_, it's pretty easy to see the status of a module in Ansible's documentation. Just go to a module's page (e.g. [lineinfile](https://docs.ansible.com/ansible/latest/modules/lineinfile_module.html), scroll to the bottom, and you'll see a note like:

> This module is maintained by the Ansible Core Team.

Or for the [redis](https://docs.ansible.com/ansible/latest/modules/redis_module.html#redis-module) module, you see:

> This module is maintained by the Ansible Community.

Modules are pretty good about showing support status, and you can read all about the different levels of maintenance and support in the doc [Module Maintenance & Support](https://docs.ansible.com/ansible/latest/user_guide/modules_support.html#modules-support).

But what about other Ansible components, like plugins, filters, and the like? And what about content you find on Ansible Galaxy?

First, there is a listing in Red Hat's knowledge base with a [List of Ansible Certified Modules](https://access.redhat.com/articles/3642632). These are modules developed by partner organizations that go through a special certification process and receive a certain level of support if you have a Red Hat subscription.

Then, there is a file in Ansible's codebase which lists out support levels for all the different files/directories in Ansible, called [BOTMETA.yml](https://github.com/ansible/ansible/blob/devel/.github/BOTMETA.yml). It's not the cleanest way in the world to identify support for everything (e.g. for filters, there can be more than one per file, so you have to parse through `core.py` to see what filters are core vs. community), and it also doesn't (currently?) show if component is 'certified' (it marks things as `core`, `community`, or `network` right now).

This file is used by the [ansibot](https://github.com/ansible/ansibullbot) to help label and organize GitHub issues (among other things).

For my purposes, this labeling can be helpful because if you notice an issue is labeled `support:community`, then it will likely not prioritized highly (since there are [more than 4,000 other issues vying for attention](https://github.com/ansible/ansible/issues) from a small team of developers), unless it's a highly visible bug within a community component.

In cases like these, especially for `community` components with no listed maintainer, it's an _opportunity_ for you to—if you want to get the issue fixed—[contribute back to Ansible](https://docs.ansible.com/ansible/latest/community/index.html) with a PR to fix the bug, improve the module, etc. :)
