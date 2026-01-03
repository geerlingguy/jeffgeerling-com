---
nid: 3293
title: "Removing official support for Red Hat Enterprise Linux"
slug: "removing-official-support-red-hat-enterprise-linux"
date: 2023-06-23T15:17:19+00:00
drupal:
  nid: 3293
  path: /blog/2023/removing-official-support-red-hat-enterprise-linux
  body_format: markdown
  redirects: []
tags:
  - linux
  - open source
  - red hat
---

For all of my open source projects, effective immediately, I am no longer going to maintain 'official' support for Red Hat Enterprise Linux.

I will still support users of CentOS Stream, Rocky Linux, and Alma Linux, as I am able to test against those targets.

Support will be 'best effort', and if you mention you are using my work on Red Hat Enterprise Linux, I will close your bug/feature/support request as 'not reproducible', since doing so would require I jump through artificial barriers Red Hat has erected to prevent the use of their Linux distribution by the wider community.

For more of my reasoning, see my previous blog post: [Dear Red Hat: Are you dumb?](https://www.jeffgeerling.com/blog/2023/dear-red-hat-are-you-dumb).

This decision will not change until and unless I see evidence Red Hat cares about giving free and open access to the sources required to build and test against their Linux distribution.

## Process

The timeline for this transition to not supporting RHEL is as follows:

**Today**: Removing official support for RHEL in Ansible role metadata, so users searching for roles to work with RHEL will not find my roles (I would rather they find roles that are actually tested against RHEL, because I cannot guarantee my roles will work for these users).

**Ongoing**: As issues crop up on various roles against RHEL, I will decide on a case-by-case basis whether to strip all RHEL-like support (effectively making the project only run on Fedora, Arch, Ubuntu, Debian, or other distros), or attempting to fix the problem so existing users of Rocky Linux, AlmaLinux, and CentOS Stream may still benefit from the fix.
