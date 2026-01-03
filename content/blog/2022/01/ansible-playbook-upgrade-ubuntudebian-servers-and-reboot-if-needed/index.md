---
nid: 3171
title: "Ansible playbook to upgrade Ubuntu/Debian servers and reboot if needed"
slug: "ansible-playbook-upgrade-ubuntudebian-servers-and-reboot-if-needed"
date: 2022-01-26T21:09:58+00:00
drupal:
  nid: 3171
  path: /blog/2022/ansible-playbook-upgrade-ubuntudebian-servers-and-reboot-if-needed
  body_format: markdown
  redirects: []
tags:
  - ansible
  - apt
  - debian
  - playbook
  - reboot
  - ubuntu
  - upgrade
---

I realized I've never posted this playbook to my blog... I needed to grab it for a project I'm working on, so I figured I'd post it here for future reference.

Basically, I need a playbook I can run whenever, that will ensure all packages are upgraded, then checks if a reboot is required, and if so, reboots the server. Afterwards, it removes any dependencies no longer required.

```
---
- hosts: all
  gather_facts: yes
  become: yes

  tasks:
    - name: Perform a dist-upgrade.
      ansible.builtin.apt:
        upgrade: dist
        update_cache: yes

    - name: Check if a reboot is required.
      ansible.builtin.stat:
        path: /var/run/reboot-required
        get_checksum: no
      register: reboot_required_file

    - name: Reboot the server (if required).
      ansible.builtin.reboot:
      when: reboot_required_file.stat.exists == true

    - name: Remove dependencies that are no longer required.
      ansible.builtin.apt:
        autoremove: yes
```
