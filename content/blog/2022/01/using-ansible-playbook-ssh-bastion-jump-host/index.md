---
nid: 3172
title: "Using an Ansible playbook with an SSH bastion / jump host"
slug: "using-ansible-playbook-ssh-bastion-jump-host"
date: 2022-01-27T15:31:23+00:00
drupal:
  nid: 3172
  path: /blog/2022/using-ansible-playbook-ssh-bastion-jump-host
  body_format: markdown
  redirects: []
tags:
  - ansible
  - bastion
  - jump server
  - private network
  - proxy
  - security
  - ssh
---

Since I've set this up a number of times, but I just realized I've never documented it on my blog, I thought I'd finally do that.

I have a set of servers that are running on a private network. That network is connected to the Internet through a single reverse proxy / 'bastion' host.

But I still want to be able to manage the servers on the private network _behind_ the bastion from outside.

## Method 1 - Inventory vars

The first way to do it with Ansible is to describe how to connect through the proxy server in Ansible's inventory. This is helpful for a project that might be run from various workstations or servers without the same SSH configuration (the configuration is stored alongside the playbook, in the inventory).

In my Ansible project, I had an inventory file like the following:

```
[proxy]
bastion.example.com

[nodes]
private-server-1.example.com
private-server-2.example.com
private-server-3.example.com
```

If I am connected to the private network directly, I can just run `ansible` commands and playbooks, and Ansible can see all the servers and connect to them (assuming my SSH config is otherwise correct).

From the outside, though, I need to modify my inventory to look like the following:

```
[proxy]
bastion.example.com

[nodes]
private-server-1.example.com
private-server-2.example.com
private-server-3.example.com

[nodes:vars]
ansible_ssh_common_args='-o ProxyCommand="ssh -p 2222 -W %h:%p -q username@bastion.example.com"'
```

This sets up an SSH proxy through bastion.example.com on port 2222 (if using the default port, 22, you can drop the port argument). The `-W` argument tells SSH it can forward stdin and stdout through the host and port, effectively allowing Ansible to manage the node _behind_ the bastion/jump server.

## Method 2 - SSH config

The alternative, which would apply the proxy configuration to all SSH connections on a given workstation, is to add the following configuration inside your `~/.ssh/config` file:

```
Host bastion
   User username
   Hostname bastion.example.com

Host private-server-*.example.com
   ProxyJump bastion
```

Ansible will automatically use whatever SSH options are defined in the user or global SSH config, so it should pick these settings up even if you don't modify your inventory.

This method is most helpful if you know your playbook will always be run from a server or workstation where the SSH config is present.
