---
nid: 3155
title: "Install Python 3.9 on Raspberry Pi OS or Debian 10 (for Ansible or other uses)"
slug: "install-python-39-on-raspberry-pi-os-or-debian-10-ansible-or-other-uses"
date: 2021-12-05T02:52:45+00:00
drupal:
  nid: 3155
  path: /blog/2021/install-python-39-on-raspberry-pi-os-or-debian-10-ansible-or-other-uses
  body_format: markdown
  redirects:
    - /blog/2021/install-python-39-on-raspberry-pi-os-or-debian-11-ansible-or-other-uses
aliases:
  - /blog/2021/install-python-39-on-raspberry-pi-os-or-debian-11-ansible-or-other-uses
tags:
  - ansible
  - centos
  - debian
  - python
  - raspberry pi
  - redhat
---

I've started getting a lot of bug reports on my repos to the effect of "Ansible won't install on my Raspberry Pi anymore". Accompanying it is a debug message like one of the following:

```
$ python3 -m pip install ansible
...
No matching distribution found for ansible-core<2.13,>=2.12.0 (from ansible)

# Alternatively:
ERROR: No matching distribution found for ansible-core<2.13,>=2.12.0
```

The problem is [`ansible-core` 2.12 has a new hard requirement for Python 3.8 or newer](https://github.com/ansible/ansible/issues/72668). And `ansible-core` 2.12 is included in Ansible 5.0.0, which was recently released. Raspberry Pi OS, which was based on Debian 10 ("Buster") until recently, includes Python 3.7, which is too old to satisfy Ansible's installation requirements.

There was recently a fix that makes it so Ansible 5.x won't get installed on these older systems, but who wants to get stuck on old unsupported Ansible versions?

There are three options:

  - Stick with Ansible 4.x or earlier
  - Switch to Debian 11 "Bullseye" (download the latest version of Pi OS) or another newer OS that has Python 3.8 or later by default.
  - Install at least Python 3.8

## Workaround: Stay on Ansible 4.x

The easiest workaround for now is to install the latest version of Ansible 4, which uses `ansible-core` 2.11, which is compatible with the version of Python (3.7) that ships with Debian 10 Buster. To do that, run:

```
$ python -m pip install --user ansible==4.9.0
```

That _should_ work, and as long as you don't try upgrading to Ansible 5, you'd have a stable (if no longer supported) version of Ansible running.

## Best fix: Install Python 3.9

It's best to upgrade Python so you can install the latest version of Ansible cleanly. Unfortunately for those with older OSes that don't have a pre-packaged version of Python available, you will need to either deal with the complexity of [`pyenv`](https://github.com/pyenv/pyenv), or [build a newer version of Python from source](https://bobcares.com/blog/how-to-install-python-3-9-on-debian-10/).

If you're running Debian 10 or the slightly-older version of Raspberry Pi OS based on it, you can still install Python 3.9 using apt, but you'll need to update your 'apt sources' to pull down a newer version of Python.

Edit `/etc/apt/sources.list`:

```
$ sudo nano /etc/apt/sources.list
```

Then add the following line to the bottom of the file and save it:

```
deb http://http.us.debian.org/debian/ testing non-free contrib main
```

Now, to install Python 3.9, run:

```
$ sudo apt update
$ sudo apt install -y python3.9
```

Now you should start seeing a Python 3.9 version installed:

```
$ python3 --version
Python 3.9.9
```

And you can now install the latest version of Ansible without an issue:

```
$ python3 -m pip install ansible
```

> Note: If you get an error like `AttributeError: 'HTMLParser' object has no attribute 'unescape'`, try running `python3 -m pip install --upgrade setuptools` and then try installing Ansible again (thanks to [this answer](https://stackoverflow.com/a/65640477) for the solution). You may also get an error like `can't find Rust compiler'—if so, also run `python3 -m pip install --upgrade pip` and then try installing Ansible again.

> Note 2: Please read through the first few comments below for suggestions on how to do this while also pinning the change to just Python—if you don't do that, you could end up upgrading a lot of other packages unintentionally, leading to system breakage!

Now verify that Ansible's installed:

```
$ python3 -m pip freeze
ansible==5.0.1
ansible-core==2.12.0
cffi==1.15.0
```
