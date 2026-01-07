---
nid: 2507
title: "Tips for a better Vagrant-based development workflow"
slug: "better-vagrant-development-workflow"
date: 2015-07-20T17:07:29+00:00
drupal:
  nid: 2507
  path: /blogs/jeff-geerling/better-vagrant-development-workflow
  body_format: full_html
  redirects:
    - /blogs/jeff-geerling/modify-etcsudoers-better
aliases:
  - /blogs/jeff-geerling/modify-etcsudoers-better
  - /blogs/jeff-geerling/better-vagrant-development-workflow
tags:
  - drupal
  - drupal planet
  - drupal vm
  - sudoers
  - vagrant
---

I build and destroy a <em>lot</em> of VMs using Vagrant in the course of the day. Between developing <a href="http://www.drupalvm.com/">Drupal VM</a>, writing <a href="http://ansiblefordevops.com/">Ansible for DevOps</a>, and testing <a href="https://galaxy.ansible.com/list#/users/219">dozens of Ansible Galaxy roles</a>, I probably run <code>vagrant up</code> and <code>vagrant destroy -f</code> at least a dozen times a day.

Building all these VMs would be a pain, and require much more user intervention, if it weren't for a few things I've done on my local workstation to help with the process. I thought I'd share these tips so you can enjoy a much more streamlined Vagrant workflow as well!

<h2>Extremely helpful Vagrant plugins</h2>

None of my projects require particular Vagrant plugins—but many, like Drupal VM, will benefit from adding at least one venerable plugin, <a href="https://github.com/cogitatio/vagrant-hostsupdater">vagrant-hostsupdater</a>. Every time you start or shut down a VM with Vagrant, the relevant hosts entries will be placed in your system's hosts file, without requiring you to do anything manually. Great time-saver, and highly recommended! To install: <code>vagrant plugin install vagrant-hostsupdater</code>

Another plugin that many people have used to provide the fastest filesystem synchronization support is <a href="https://github.com/smerrill/vagrant-gatling-rsync">vagrant-gatling-rsync</a>, which uses an rsync-based sync mechanism similar to the one built into Vagrant, but much faster and less resource-intense on your host machine.

<h2>Helpful modifications to /etc/sudoers</h2>

One major downside to using the vagrant-hostsupdater plugin, or to using NFS mounts (which are much faster than native shares in either VirtualBox or VMWare Fusion), is that you have to enter your sudo password when you build and destroy VMs. You can avoid this gotcha by adding the following lines to your <code>/etc/sudoers</code> configuration (then quit and restart your Terminal session so the new settings are picked up):

```
# Vagrant configuration.
# Allow Vagrant to manage NFS exports.
Cmnd_Alias VAGRANT_EXPORTS_ADD = /usr/bin/tee -a /etc/exports
Cmnd_Alias VAGRANT_NFSD = /sbin/nfsd restart
Cmnd_Alias VAGRANT_EXPORTS_REMOVE = /usr/bin/sed -E -e /*/ d -ibak /etc/exports
# Allow Vagant to manage hosts file.
Cmnd_Alias VAGRANT_HOSTS_ADD = /bin/sh -c echo "*" >> /etc/hosts
Cmnd_Alias VAGRANT_HOSTS_REMOVE = /usr/bin/sed -i -e /*/ d /etc/hosts
%admin ALL=(root) NOPASSWD: VAGRANT_EXPORTS_ADD, VAGRANT_NFSD, VAGRANT_EXPORTS_REMOVE, VAGRANT_HOSTS_ADD, VAGRANT_HOSTS_REMOVE
```

<strong>Important note</strong>: If you're editing sudoers by hand, make sure you edit the file with <code>sudo visudo</code> instead of just editing it in your favorite editor. This ensures the file is valid when you save it, so you don't get locked out from sudo on your system!

This configuration works out of the box on Mac OS X, and only needs slight modifications to make sure it works on Linux distributions (make sure the 'admin' group is changed to whatever group your user account is in).

I've even wrapped up the configuration of /etc/sudoers into my <a href="https://github.com/geerlingguy/mac-dev-playbook">Mac Development Ansible Playbook</a>, so I can automatically ensure all my Macs are configured for an optimal Vagrant experience!

<h2>SSH keys inside your VM</h2>

If you want to use your SSH credentials inside a Vagrant-powered VM, you can turn on <a href="http://www.unixwiz.net/techtips/ssh-agent-forwarding.html">SSH agent forwarding</a> on by adding the following line inside your Vagrantfile:

```
  config.ssh.forward_agent = true
```

Drupal VM includes agent forwarding by default, so you can build your VM, log in, and work on Git projects, log into remote servers, use drush, etc., just as you would on your host computer.

Note that I usually <em>don't</em> have fowarding enabled in my own environments, as I treat Vagrant VMs strictly as sandboxed development environments—if I install some software for testing inside the VM as the <code>vagrant</code> user, I don't want it to be able to use my SSH credentials to do anything nefarious! Generally that won't happen, but I like erring on the side of caution.

<h2>Summary</h2>

What are some of your favorite tips and tricks for Vagrant-based workflows? Any other tricks you know of to solve common pain points (e.g. using the <code>vagrant-vbguest</code> if you have issues with native shares or guest additions)?
