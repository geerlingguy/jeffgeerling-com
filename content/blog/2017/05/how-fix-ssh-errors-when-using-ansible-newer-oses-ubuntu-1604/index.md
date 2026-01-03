---
nid: 2774
title: "How to fix SSH errors when using Ansible with newer OSes like Ubuntu 16.04"
slug: "how-fix-ssh-errors-when-using-ansible-newer-oses-ubuntu-1604"
date: 2017-05-11T16:30:33+00:00
drupal:
  nid: 2774
  path: /blog/2017/how-fix-ssh-errors-when-using-ansible-newer-oses-ubuntu-1604
  body_format: markdown
  redirects: []
tags:
  - ansible
  - python
  - tutorial
  - ubuntu
---

Recently, as I've been building more and more servers running Ubuntu 16.04, I've hit the following errors:

```
PLAY [host] ************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
fatal: [1.2.3.4]: UNREACHABLE! => {"changed": false, "msg": "SSH Error: data could not be sent to remote host \"1.2.3.4\". Make sure this host can be reached over ssh", "unreachable": true}
```

or:

```
/bin/sh: 1: /usr/bin/python: not found
```

The former error seems to happen when you're running a playbook on an Ubuntu 16.04 host (with `gather_facts: yes`), while the latter happens if you're using a minimal distribution that doesn't include Python at all. The problem, in both cases, is that Python 2.x is not installed on the server, and there are two different fixes:

  1. If you already have Python 3 installed on the server (such is the case with Ubuntu 16.04, by default), you can set in your inventory: `ansible_python_interpreter=/usr/bin/python3`. This enables Ansible's ([currently experimental as of 2.3](https://github.com/ansible/ansible/issues/16388#issuecomment-227584967)) Python 3 support, which seems to work well for _most_ Ansible modules.
  2. If you don't have Python installed on the server, you should change the structure of your playbook so it will ensure Python 2 is installed prior to running the rest of the playbook. See the below example, which is [lifted from Drupal VM](https://github.com/geerlingguy/drupal-vm/issues/1245):

```
---
- hosts: drupalvm
  gather_facts: no

  pre_tasks:
    # See: https://github.com/geerlingguy/drupal-vm/issues/1245
    - name: Install Python if it's not available.
      raw: test -e /usr/bin/python || (apt -y update && apt install -y python-minimal)
      register: output
      changed_when: output.stdout != ""

    - action: setup
      tags: ['always']
```

Note that I set `gather_facts: no` (this prevents Ansible from trying to run Python modules before Python is available)—then after ensuring Python is present, I run the task `action: setup` (with the `always` tag so it's always run, even if you're just running a subset of tasks later). This is basically a 'poor man's `gather_facts`' that gathers facts in the middle of a playbook.

Using this, you should be able to overcome the problems caused by not having Python 2 available on the server you're controlling. Hopefully Ansible will be 100% compatible with Python 3 soon, and this problem will not require any additional code to make it work!
