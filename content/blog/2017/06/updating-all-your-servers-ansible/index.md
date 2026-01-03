---
nid: 2786
title: "Updating all your servers with Ansible"
slug: "updating-all-your-servers-ansible"
date: 2017-06-22T13:23:25+00:00
drupal:
  nid: 2786
  path: /blog/2018/updating-all-your-servers-ansible
  body_format: markdown
  redirects:
    - /blog/2017/updating-all-your-servers-ansible
aliases:
  - /blog/2017/updating-all-your-servers-ansible
tags:
  - ansible
  - apt
  - automation
  - centos
  - debian
  - dnf
  - fedora
  - redhat
  - ubuntu
  - update
  - upgrade
  - yum
---

From time to time, there's a security patch or other update that's critical to apply ASAP to all your servers. If you use Ansible to automate infrastructure work, then updates are painless—even across dozens, hundreds, or thousands of instances! I've written about this a little bit in the past, in relation to [protecting against the shellshock vulnerability](https://www.jeffgeerling.com/blog/secure-your-servers-shellshock-bash-vulnerability), but that was specific to one package.

I have an inventory script that pulls together all the servers I manage for personal projects (including the server running this website), and organizes them by OS, so I can run commands like `ansible [os] command`. Then that enables me to run commands like:

```
# Upgrade all the Ubuntu servers.
ansible ubuntu -m apt -a "upgrade=yes update_cache=yes" -b

# Upgrade all the Debian servers.
ansible debian -m apt -a "upgrade=yes update_cache=yes" -b

# Upgrade all the CentOS servers.
ansible centos -m yum -a "name=* state=latest" -b

# Upgrade all the Fedora servers.
ansible fedora -m dnf -a "name=* state=latest" -b
```

Then I can reboot all servers with `ansible all -a "reboot" -b`.

I've also built more intelligent playbooks for this purpose, allowing me to do rolling updates (e.g. don't reboot all servers at once—just do half, then the other half), monitor the progress with `wait_for` and `connection: local`... but I'll leave that exercise to the reader, since these kind of playbooks are usually more specific to your infrastructure (hint: [google it](https://www.google.com/search?client=safari&rls=en&q=rolling+update+reboot+ansible&ie=UTF-8&oe=UTF-8)).
