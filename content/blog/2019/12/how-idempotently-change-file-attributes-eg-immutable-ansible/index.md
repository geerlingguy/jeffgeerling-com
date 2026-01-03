---
nid: 2956
title: "How to idempotently change file attributes (e.g. immutable) with Ansible"
slug: "how-idempotently-change-file-attributes-eg-immutable-ansible"
date: 2019-12-03T22:44:41+00:00
drupal:
  nid: 2956
  path: /blog/2019/how-idempotently-change-file-attributes-eg-immutable-ansible
  body_format: markdown
  redirects: []
tags:
  - ansible
  - attributes
  - file
  - modules
---

I recently needed to force the `/etc/resolv.conf` file to be immutable on a set of CentOS servers, since the upstream provider's DHCP server was giving me a poorly-running set of default DNS servers, which was getting written to the `resolv.conf` file on every reboot.

There are a few different ways to force your own DNS servers (and override DHCP), but one of the simplest, at least for my use case, is to change the file attributes on `/etc/resolv.conf` to make the file _immutable_ (unable to be overwritten, e.g. by the network service's DHCP on reboot).

Typically you would do this on the command line with:

    chattr +i /etc/resolv.conf

And Ansible's [file module](https://docs.ansible.com/ansible/latest/modules/file_module.html) has an `attributes` (alias: `attr`) parameter which allows the setting of attributes. For example, to set the attributes to `i`, you would use a task like:

```
- name: Ensure resolv.conf is immutable.
  file:
    path: /etc/resolv.conf
    attr: i
```

The problem is, this fails (at least on CentOS), because it's trying to override _all_ the file's attributes, and CentOS also needs the `e` attribute. You _could_ say `attr: ie`, but then you're being pretty strict about the attributes. Instead, you can use the value `+i`:

```
- name: Ensure resolv.conf is immutable.
  file:
    path: /etc/resolv.conf
    attr: +i
```

But here's the rub: when you do this, Ansible will _always_ report 'changed' for this task, because it is always going to run `lsattr +i` on the file, even if it's already immutable. To make it so Ansible only reports a change if the file wasn't _already_ immutable, you can register a variable and then set `changed_when` for the task, like so:

```
- name: Ensure resolv.conf is immutable.
  file:
    path: /etc/resolv.conf
    attr: +i
  register: resolv_file
  changed_when: "'i' not in resolv_file.diff.before.attributes"
```

Now, when you run the playbook, it will report a change on the first run, but not after that (unless someone is surreptitiously running a `-i` on your server and not using automation!).
