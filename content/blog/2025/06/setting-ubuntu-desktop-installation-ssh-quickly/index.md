---
nid: 3472
title: "Setting up an Ubuntu Desktop installation for SSH, quickly"
slug: "setting-ubuntu-desktop-installation-ssh-quickly"
date: 2025-06-24T22:02:33+00:00
drupal:
  nid: 3472
  path: /blog/2025/setting-ubuntu-desktop-installation-ssh-quickly
  body_format: markdown
  redirects: []
tags:
  - linux
  - remote access
  - ssh
  - sudoers
  - ubuntu
  - visudo
---

I've enjoyed using Ubuntu Server's GitHub SSH pubkey importer for a long time, it's a quick and easy way when doing an interactive server installation to get the built-in OpenSSH server configured for remote SSH access.

However, many computers I work on have Ubuntu Desktop installed instead, and it doesn't even include OpenSSH Server in the default packages!

So I thought I'd write up a quick guide for how to set up SSH on Ubuntu Desktop pulling in my GitHub SSH public keys quickly, since I haven't found a similar guide elsewhere:

## Install OpenSSH

Open Terminal and enter the commands:

```
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh
```

OpenSSH is running with Ubuntu's default configuration. You can edit the configuration inside `/etc/ssh/sshd_config` if you want (make sure to `systemctl restart ssh` after doing so).

## Import your GitHub public keys

Ubuntu includes a handy utility that does this for you:

```
ssh-import-id gh:username
```

For example, I could enter `gh:geerlingguy` for my own keys. Don't use my username on your own server, though, unless you want me to access it ;)

You can read more about [ssh-import-id](https://manpages.ubuntu.com/manpages/bionic/man1/ssh-import-id.1.html) on the Ubuntu manpages.

## Configuring passwordless sudo

Usually, if I'm going to be using a new Ubuntu Desktop install for quick testing or benchmarking, I just want to set `sudo` to be able to run passwordless under my user account.

The easiest way to do that (note there are security implications to doing this, so don't do it unless you know what you're doing!) is to use `visudo` to configure the `sudo` group to not require a password:

```
sudo visudo
```

Then change the `%sudo` line to the following, and save the file:

```
%sudo  ALL=(ALL) NOPASSWD: ALL
```
