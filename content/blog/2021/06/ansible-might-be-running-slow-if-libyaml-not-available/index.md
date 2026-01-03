---
nid: 3113
title: "Ansible might be running slow if libyaml is not available"
slug: "ansible-might-be-running-slow-if-libyaml-not-available"
date: 2021-06-30T17:43:47+00:00
drupal:
  nid: 3113
  path: /blog/2021/ansible-might-be-running-slow-if-libyaml-not-available
  body_format: markdown
  redirects: []
tags:
  - ansible
  - libyaml
  - m1
  - mac
  - python
  - raspberry pi
---

Recently I upgraded from an Intel-based MacBook Pro to two M1 Macs. As part of the upgrade, I also made sure to refine my Mac setup automation with Ansible and my [Mac Development Ansible Playbook](https://github.com/geerlingguy/mac-dev-playbook).

But one weird thing I noticed was no matter how I installed Ansible on my new Macs, I couldn't get `libyaml` support to work:

```
$ ansible --version
ansible [core 2.11.1] 
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/Users/jgeerling/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /Users/jgeerling/Library/Python/3.8/lib/python/site-packages/ansible
  ansible collection location = /Users/jgeerling/.ansible/collections:/usr/share/ansible/collections
  executable location = /Users/jgeerling/Library/Python/3.8/bin/ansible
  python version = 3.8.2 (default, Apr  8 2021, 23:19:18) [Clang 12.0.5 (clang-1205.0.22.9)]
  jinja version = 3.0.1
  libyaml = False
```

If you run `ansible -v` and see `libyaml = False`, then Ansible can't find the `libyaml` bindings (which are very fast) and it will resort to a slower Python-based YAML interpreter.

What's `libyaml`, you ask? It's described as a _YAML parser and emitter library_, and it helps PyYAML (the library Ansible uses for YAML parsing _much_ faster.

I first found out _just how much_ slower Ansible can be without `libyaml` support when I was testing out Ansible 2.10 on a Raspberry Pi—which has a very slow microSD card as a boot volume. I opened the following GitHub issue to investigate: [On systems with slow disks, Ansible 2.10 runs generally much slower than 2.9](https://github.com/ansible/ansible/issues/72030).

The speedup is dramatic: _just running the `ansible` command_ took **6 seconds** without libyaml, but only **1.5 seconds** _with_ libyaml.

The GitHub issue has a lot of good discussion in it, but since there aren't a whole lot of helpful docs on how to properly get Ansible working with `libyaml` support out there, I thought I'd write up this blog post.

## Checking if `libyaml` is present

The simplest test to see if `libyaml` is present in your Python installation is to run the following command:

```
$ python3 -c 'import _yaml'
```

If successful, you'll see no output. If it isn't present, you'll see `ImportError: No module named _yaml`.

## Getting `libyaml` support working on macOS

On my Mac, I first made sure I was using the Python 3 version I installed via Homebrew, and then made sure to install `libyaml` with `brew install libyaml`.

Then I made sure Ansible was completely _uninstalled_ using `pip3 uninstall ansible ansible-core`.

Then I re-installed Ansible with:

```
$ pip3 install ansible
```

And finally, I can see `libyaml` support is working:

```
$ ansible --version
ansible [core 2.11.2] 
  ...
  libyaml = True
```

## Getting `libyaml` support working on Raspberry Pi OS (Debian aarch64)

I had to uninstall Ansible and any installed `pyyaml` version:

```
pip3 uninstall pyyaml ansible ansible-base
```

Then I explicitly installed libyaml, pyyaml, and ansible, making sure when installing the latter two that Pip's local cache was not used:

```
sudo apt install -y libyaml-dev
pip3 install --no-cache-dir --no-binary pyyaml ansible
```

Why the `--no-binary` option? Well, currently the pyyaml wheel for Pi OS / ARM64 is not built correctly to detect libyaml support, so you have to skip the pre-built wheel and basically compile the library yourself. See [this issue](https://github.com/piwheels/packages/issues/130) for more details.

Hopefully if you encounter the same issue—which you might not have even known you had!—Ansible will be a bit faster after fixing this annoying problem.
