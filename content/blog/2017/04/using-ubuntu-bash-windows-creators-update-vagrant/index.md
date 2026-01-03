---
nid: 2763
title: "Using Ubuntu Bash in Windows Creators' Update with Vagrant"
slug: "using-ubuntu-bash-windows-creators-update-vagrant"
date: 2017-04-10T21:58:41+00:00
drupal:
  nid: 2763
  path: /blog/2017/using-ubuntu-bash-windows-creators-update-vagrant
  body_format: markdown
  redirects: []
tags:
  - bash
  - drupal
  - drupal planet
  - drupal vm
  - linux
  - tutorial
  - ubuntu
  - vagrant
  - windows
  - windows 10
---

When Microsoft announced the Windows Subsystem for Linux, now seemingly rebranded as [Bash on ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about), I was excited at the possibility of having Drupal VM (and other similarly command-line-friendly open source projects) work better in a Windows environment. But unfortunately, the Anniversary update's version of WSL/Ubuntu Bash was half-baked, and there were a lot of little issues trying to get anything cohesive done between the Windows and Ubuntu Bash environments (even with [cbwin](https://github.com/xilun/cbwin)).

Then, a year or so later, Microsoft finally announced that tons of improvements (including upgrading Ubuntu in the WSL from 14.04 to 16.04!) would be included in the 'Creators Update' to Windows 10, dropping tomorrow, April 11.

One of the major improvements would be the ability to [call out to Windows executables from within Ubuntu Bash](https://msdn.microsoft.com/en-us/commandline/wsl/release_notes#build-14951), which was added in October 2016, but only available to those willing to run Microsoft's bleeding-edge 'Insider' builds. This feature is going to be included with the rest of the improvements in the Creator's update, so I thought I'd update early and explore whether this is the panacea I dreamt of when I first heard about WSL/Ubuntu Bash.

> **tl;dr**: It's not a panacea. But it _is_ something. And things are improved significantly from where we were one year ago, as far as open source devs who develop in Windows (by choice or by dictum).

## How to update to Windows 10 'Creators Update'

If it's April 11 or later, you can just use Windows Auto Update mechanism to upgrade to the Creators Update version of Windows 10. It seems the ISO images are already on microsoft.com, and it's only April 10 where I live, so I'm not sure when your particular computer will see the update become available for install.

## How to Install WSL/Ubuntu Bash

> Note: If you've previously installed Ubuntu Bash on an older version of Windows, and want to get the new version running Ubuntu 16.04 instead of 14.04, you need to run Powershell as administrator, and enter the command `lxrun /uninstall /full`.

  1. Run `lxrun /install /y`
  2. After installation is finished, enter 'Ubuntu' in Cortana/search and open "Bash on Ubuntu on Windows"
  3. Confirm you're on Ubuntu 16.04 by running `lsb_release -a`

## Use Vagrant with Ubuntu Bash

  1. Add Windows executables to your Ubuntu `$PATH`: `export PATH=$PATH:/mnt/c/Windows/System32/
  2. Test that Vagrant is callable by running `vagrant.exe status`
  3. Change directories to a location that's accessible to Windows (e.g. `cd /mnt/c/Users/yourusername`).
  4. Clone a Vagrant-based project locally: `git clone https://github.com/geerlingguy/drupal-vm.git`
  5. Change directories into the project dir: `cd drupal-vm`
  6. Run `vagrant.exe up`.

Note that, currently, you can't run `vagrant.exe ssh` from within Ubuntu Bash. You have to either use Cmder or a similar CLI for that, or run `vagrant.exe ssh-config`, then run a manual SSH command (`ssh -p [port] vagrant@127.0.0.1`) to connect to your VM from within Ubuntu Bash.

## Necessary improvements

I'm hopeful that Microsoft may be able to find ways to allow Windows executables (like Vagrant) see and use binaries in the WSL environment (e.g. Vagrant.exe can call out to Ubuntu's `ssh`). In lieu of that, I wonder if Vagrant itself may be able to make some improvements to make it easier for Windows users to do things like `vagrant ssh` and other esoteric commands without resorting to Cygwin.

I'm still working through some of these issues and trying to find the best path forward (especially for beginners) in the Drupal VM issue queue: [Update docs for Windows with WSL Windows Interoperability improvements](https://github.com/geerlingguy/drupal-vm/issues/1012).

I've also [left feedback](https://github.com/mitchellh/vagrant/issues/7731#issuecomment-292998033) in the Vagrant project's issue dealing with the WSL ([Use Linux Subsystem on Windows](https://github.com/mitchellh/vagrant/issues/7731)), but I think as more developers start using Vagrant and WSL together, we may find clever ways of working around the current limitations.

You could also just run Linux or macOS as your desktop OS, and avoid these issues entirely ;-)
