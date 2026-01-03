---
nid: 2627
title: "Developing with VirtualBox and Vagrant on Windows"
slug: "developing-virtualbox-and-vagrant-on-windows"
date: 2016-03-14T19:02:14+00:00
drupal:
  nid: 2627
  path: /blog/2019/developing-virtualbox-and-vagrant-on-windows
  body_format: markdown
  redirects:
    - /blog/2016/developing-virtualbox-and-vagrant-on-windows
aliases:
  - /blog/2016/developing-virtualbox-and-vagrant-on-windows
tags:
  - drupal
  - drupal planet
  - drupal vm
  - essay
  - open source
  - vagrant
  - virtualization
  - web development
  - windows
---

I've been supporting [Drupal VM](http://www.drupalvm.com/) (a local Drupal CMS development environment) for Windows, Mac, and Linux for the past couple years, and have been using Vagrant and virtual machines for almost all my development (mostly PHP, but also some Python and Node.js at the moment) for the past four years. One theme that comes up quite frequently when dealing with VMs, open source software stacks (especially Drupal/LAMP), and development, is how much extra effort there is to make things work _well_ on Windows.

## Problem: tool-builders use Linux or macOS

The big problem, I see, is that almost all the tool-builders for OSS web software run either macOS or a flavor of Linux, and many don't even have _access_ to a Windows PC (outside of maybe an odd VM for testing sites in Internet Explorer or Edge, if they're a designer/front-end developer). My evidence is anecdotal, but go to any OSS conference/meetup and you'll likely see the same.

When tool-builders don't use Windows natively, and in many cases don't even have access to a real Windows environment, you can't expect the tools they build to always play nice in that kind of environment. Which is why virtualization is almost an essential component of anyone's Windows development workflow.

However, that's all a bit of an aside leading up to the substance of this post: common issues with Windows-based development using virtual machines (e.g. VirtualBox, Hyper-V, VMware, etc.), and some solutions or tips for minimizing the pain.

> As an aside, I bought a Lenovo T420 and stuck 2 SSDs and an eMMC card in it, then I purchased and installed copies of Windows 7, 8, and 10 on them so I could make sure the tools I build work at least decently well on Windows in multiple different environments. Many open source project maintainers aren't willing to fork over a $500+ outlay just to test in a Windows environment, especially since the Windows bugs often take 2-4x more time and cause many more grey hairs than similar bugs on Linux/macOS.

## Tips for more efficiency on Windows

First: **if there's any way you can use Linux or Mac instead of Windows, you'll be in much less pain**. This is not a philosophical statement, nor is it an anti-Microsoft screed. Almost all the modern web development toolkits are supported primarily (and sometimes _only_) for Linux/POSIX-like environments. Getting _everything_ in a modern stack working together in Windows natively is almost never easy; getting things working within a VM is a viable but sometimes annoying alternative.

Second: **if you can do all development within the VM, you'll be in somewhat less pain**. If you can check out your codebase inside the VM's filesystem (and not use a synced folder), then edit files in the VM, or edit files in Windows through a mounted share (instead of using built-in shared folders), some of the pain will be mitigated.

Here are some of the things I've found that make development on Windows possible; and sometimes even enjoyable:

### Using a POSIX-like environment

> **2019 Update**: The [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) is now the recommended way to have a Linux environment running on your Windows 10 or later machine. Note, however, that it cannot be used in all scenarios and still carries with it some caveats, especially having to do with controlling Windows executables and files from the Linux subsystem (and vice-versa).

I'd recommend using either [Cygwin](https://cygwin.com/install.html) (with openssh) or [Cmder](http://cmder.net/) instead of PowerShell/Git Bash/Git Shell. These solutions emulate the same command line environment you get on Linux/BSD much more closely than PowerShell, Git Bash, or Git Shell, and things like SSH and other commands you'll see in guides/tutorials work much more consistently in these environments.

Also, for many problems (especially permissions or filesystem-related), running your terminal environment as administrator seems to help.

### Working with symbolic links (symlinks)

If you have to support symbolic links inside the VM, you can't use Git Bash, Git Shell, or Powershell when managing the Vagrant environment (there is a way, but it's excruciating). It's highly recommended to use either [Cygwin](https://cygwin.com/install.html) (with openssh) or [Cmder](http://cmder.net/) instead (see above). There are additional caveats when you require symlink support:

  - You need to run Cygwin or Cmder as administrator (otherwise you can't create symlinks).
  - You have to do everything inside the VM (you can do git stuff outside, and edit code outside, but anything you need to do dealing with creating/changing/deleting symlinks should be done inside the VM).
  - If you touch the symlinks outside the VM, bad things will happen.
  - Symlinks only work with SMB or native shares (possibly rsync, too, but that's a bit harder to work with in my experience.
  - If you switch from native to SMB, or vice-versa, you have to rebuild all symlinks (symlinks between the two synced folder types are incompatible).
  - If you use SMB, you have to set custom mount options for Vagrant in the synced folder configuration, e.g.: `mount_options: ["mfsymlinks,dir_mode=0755,file_mode=0755"]`

### VirtualBox Guest Additions

Probably half the problems I've seen are due to outdated (or not-installed) VirtualBox Guest Additions. Many Vagrant box maintainers don't update their boxes regularly, and if this is the case, and you have a newer version of VirtualBox, all kinds of strange issues (ssh errors, synced folder errors, etc.) ensue.

I highly recommend (for Mac, Linux, _and_ Windows) you install the `vagrant-vbguest` plugin: `vagrant plugin install vagrant-vbguest`

### Delete a deep folder hierarchy (nested directories)

For many of the projects I've worked on, folder hierarchies can get quite deep, e.g. `C:/Users/jgeerling/Documents/GitHub/myproject/docroot/sites/all/themes/mytheme/node_modules/dist/modulename/etc.` Windows _hates_ deep folder hierarchy, and if you try deleting a folder with such a structure either in Explorer or using `rmdir` in PowerShell, you'll likely end up with an error message (e.g. `File name too long...`).

To delete a folder with a deep hierarchy (many nested directories), you need to install [robocopy](https://www.microsoft.com/en-us/download/details.aspx?id=17657) (part of the Windows Server set of tools), then [follow these directions to delete the directory](/blog/2016/deleting-directory-windows-10-source-path-too-long-using-robocopy).

### Node.js and npm problems

There are myriad issues running Node.js, NPM, and the ecosystem of associated build tools. It's hard enough keeping things straight with multiple Node versions and `nvm` on Mac/Linux... but toss in a Windows environment and most corporate networks/group policies, and you will also need to deal with:

  - If you have certain flavors of antivirus running, you might have trouble with Node.js and NPM.
  - If you are behind a corporate proxy, you will need to run a few extra commands to make sure things like `apt` work inside the VM.

If you attempt to use Node/NPM within Windows, you should run Cygwin or Cmder as administrator, and possibly disable AntiVirus software. If working behind a proxy, you will also need to configure NPM to work with the proxy (_in addition to_ configuring the VM/Linux in general to work behind the proxy):

```
$ npm config set proxy http://username:password@host:port/
$ npm config set https-proxy http://username:password@host:port/
```

### Intel VT-x virtualization

Many PC laptops (especially those from Lenovo, HP, and Dell) have Intel's VT-x virtualization turned off by default, which can cause issues with many Vagrant boxes. Check your computer manufacturer's knowledge base for instructions for enabling VT-x in your system BIOS/UEFI settings.

I have a Lenovo T420, and had to follow these [instructions for enabling virtualization](http://amiduos.com/support/knowledge-base/article/enabling-virtualization-in-lenovo-systems) from Lenovo's support site.

### Other Notes

I've also compiled a list of Windows tips and tricks in the Drupal VM project documentation: [Drupal VM Docs - Windows Notes](http://docs.drupalvm.com/en/latest/getting-started/installation-windows/).

## Summary

Developing for Drupal with Vagrant and VMs on Windows is possible—I've used Drupal VM and related projects with Windows 7, 8, and 10, with and without proxies, on a variety of hardware—but not optimal for all cases. If you keep running into issues like those listed above (or others), you might want to investigate switching your development environment to Linux or macOS instead.
