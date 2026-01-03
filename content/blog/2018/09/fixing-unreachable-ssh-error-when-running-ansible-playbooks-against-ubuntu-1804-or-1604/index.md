---
nid: 2871
title: "Fixing 'UNREACHABLE' SSH error when running Ansible playbooks against Ubuntu 18.04 or 16.04"
slug: "fixing-unreachable-ssh-error-when-running-ansible-playbooks-against-ubuntu-1804-or-1604"
date: 2018-09-16T03:36:42+00:00
drupal:
  nid: 2871
  path: /blog/2018/fixing-unreachable-ssh-error-when-running-ansible-playbooks-against-ubuntu-1804-or-1604
  body_format: markdown
  redirects: []
tags:
  - ansible
  - playbook
  - python
  - tutorial
  - ubuntu
---

Ubuntu 16.04 and 18.04 (and likely future versions) often don't have Python 2 installed by default. Sometimes Python 3 is installed, available at `/usr/bin/python3`, but for many minimal images I've used, there's _no_ preinstalled Python at all.

Therefore, when you run Ansible playbooks against new VMs running Ubuntu, you might be greeted with the following error:

```
TASK [Gathering Facts] *************************************************************************************************
fatal: [example.com]: UNREACHABLE! => {"changed": false, "msg": "SSH Error: data could not be sent to remote host \"example.com\". Make sure this host can be reached over ssh", "unreachable": true}
```

It's easy enough to work around this problem, though! If you have the ability to build your own base images (e.g. AMIs on AWS), you can just make sure `/usr/bin/python` is already installed on the image. And if only `python3` is present, you can set `ansible_python_interpreter=/usr/bin/python3` in your inventory for the affected hosts. If you can't do either of these things, the best way is to:

  1. Skip `gather_facts` initially.
  2. Use the `raw` module to make sure Python is installed.
  3. Use the `setup` module to gather facts after Python is definitely installed.

Here's a scaffold playbook I usually use on any Ubuntu 16 or 18 hosts:

```
---
- hosts: all
  gather_facts: no

  pre_tasks:
    - name: Install Python if not already present.
      raw: test -e /usr/bin/python || (apt -y update && apt install -y python-minimal)
      changed_when: False

    - name: Gather facts after Python is definitely present.
      setup:

  roles:
    ...
```

This way, you'll still have access to host facts, and you won't get cryptic errors about Ansible not being able to connect to the host via SSH.
