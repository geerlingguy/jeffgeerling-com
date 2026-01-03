---
nid: 3384
title: "Newer versions of Ansible don't work with RHEL 8"
slug: "newer-versions-ansible-dont-work-rhel-8"
date: 2024-06-07T15:50:22+00:00
drupal:
  nid: 3384
  path: /blog/2024/newer-versions-ansible-dont-work-rhel-8
  body_format: markdown
  redirects: []
tags:
  - ansible
  - devops
  - infrastructure
  - linux
  - python
---

> **Note**: This problem may occur on other older distros as well, like Ubuntu 18.04.

Red Hat Enterprise Linux 8 is supported until 2029, and that distribution includes Python 3.6 for system python. Ansible's long been stuck between a rock and a hard place supporting certain modules (especially packaging modules like `dnf`/`yum` on RHEL and its derivatives, because the Python bindings for the packaging modules are stuck supporting system Python.

Users are getting errors like:

```
/bin/sh: /usr/bin/python3: No such file or directory
The module failed to execute correctly, you probably need to set the interpreter.\nSee stdout/stderr for the exact error.

...or...

SyntaxError: future feature annotations is not defined
```

As `ansible-core` evolves, they don't want to support old insecure versions of Python forever—[Python 3.6 was out of security support back in 2021!](https://endoflife.date/python).

But that creates a conundrum; if you're a Red Hat customer using Ansible to automate your RHEL 8 infrastructure—or if you're using one of the many derivatives, like AlmaLinux, Rocky Linux, Oracle Linux, etc.—then you will start running into issues automating these older servers if you install the newest version of Ansible.

Luckily, Ansible core 2.16 is slated to be something of an 'LTS' release, [according to one of the core maintainers](https://github.com/ansible/ansible/issues/83357#issuecomment-2148280535)—so if you lock into that version of Ansible core anywhere you run code against RHEL 8 servers, you should be good to go:

```
pip3 install ansible-core<2.17
```

Ideally, any security issues in Ansible itself will be fixed and backported in the 2.16 release branch—but it won't get any new features or any other Ansible 2.17+ goodness.

> NOTE: You _can_ install a newer version of Python on RHEL 8 systems and get at least much of Ansible to work, but many system-level components—most notably `dnf`—won't work because of the older system Python bindings. That makes it functionally useless for _me_, because `dnf`/`package` is probably the module that appears most frequently in my playbooks!

Where this really throws in a wrench is for 'community edition' users (I still don't know what the main `ansible` bundle package should be _technically_ called—I still just call it Ansible hehe). There are two options, one probably better than the other:

  1. Lock in version 9.x: `pip install 'ansible<10.0'`
  2. Switch to installing `ansible-core` and a set of collections you need (which is similar to what the main `ansible` package does, just you do it through a requirements file and lose a few packaging conveniences.

With the first option, you wind up on an [already-unsupported release of Ansible 9.x](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-community-package-release-cycle):

> Starting with version 2.10, the Ansible community team guarantees maintenance for only one major community package release at a time. For example, when Ansible 4.0.0 gets released, the team will stop making new 3.x releases. Community members may maintain older versions if desired.

With the second option, you'll lock in Ansible 2.16, but if you don't also start locking in other collection versions for modules you use, you may run into incompatibilities in the future, as other collections use features only present in Ansible 2.17 or later, or newer versions of Python.

In any case, I've moved my personal infrastructure over to Debian, so these things aren't an issue as I've started upgrading servers on a 5 year cycle instead of 10 years—but even there, Ubuntu 18.04 stragglers (to be fair, it's LTS support ended _last_ year) also have issues since system python is too old for Ansible.

The main takeaway: Ansible's core developers have consistently chosen newer Python version compatibility at the expense of supporting old, unsupported versions. So plan your infrastructure lifecycle accordingly. IMO, if you are an organization that chooses to run servers for 10 years without migrating to newer OS releases... you should figure out how you can use Ansible to make those OS upgrades and system migrations easier :P
