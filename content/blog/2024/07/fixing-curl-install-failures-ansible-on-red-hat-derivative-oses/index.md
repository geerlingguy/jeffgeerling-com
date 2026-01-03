---
nid: 3395
title: "Fixing curl install failures with Ansible on Red Hat-derivative OSes"
slug: "fixing-curl-install-failures-ansible-on-red-hat-derivative-oses"
date: 2024-07-30T14:40:50+00:00
drupal:
  nid: 3395
  path: /blog/2024/fixing-curl-install-failures-ansible-on-red-hat-derivative-oses
  body_format: markdown
  redirects: []
tags:
  - ansible
  - curl
  - dnf
  - install
---

Over the past few months, I've noticed some of my automation failing on Red Hat-derivative OSes like Rocky Linux and AlmaLinux. The reason for this has to do with the inclusion of a `curl-minimal` package in some distros, which conflicts with `curl` if you try installing the full package.

Unfortunately, the fix for this is a little strange, and so only ends up in Ansible's [dnf](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/dnf_module.html) module, not in the more cross-compatible [package](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html) module.

The error I was seeing is like:

```
Depsolve Error occurred: 
 Problem: problem with installed package curl-minimal-7.76.1-29.el9_4.x86_64
  - package curl-minimal-7.76.1-29.el9_4.x86_64 from @System conflicts with curl provided by curl-7.76.1-29.el9_4.x86_64 from baseos
  - package curl-minimal-7.76.1-29.el9_4.x86_64 from baseos conflicts with curl provided by curl-7.76.1-29.el9_4.x86_64 from baseos
  - conflicting requests
```

To fix this problem, I switched my tasks from using `package` to using `dnf`, and set the `allowerasing` parameter to `true`.

Before:

```
- name: Ensure dependencies are installed.
  package:
    name: curl
    state: present
```

After:

```
- name: Ensure dependencies are installed.
  dnf:
    name: curl
    allowerasing: true
    state: present
```

If your task is meant to run cross-platform, DNF certainly won't run out of the box on Debian-based installs (or other flavors of Linux), so you will also need to split the one task into two—add a `when` condition to only run the `dnf` task on RHEL-derivatives, and the `package` task on all others.

This seems to fix the issue, see Ansible core issue [DNF fails to properly resolve and install package based the file it provides](https://github.com/ansible/ansible/issues/82461) and [this comment about `--allowerasing`](https://github.com/amazonlinux/amazon-linux-2023/issues/150#issuecomment-1207233037) for more details.
