---
nid: 2621
title: "Drupal VM - Quick Introduction Video"
slug: "drupal-vm-quick-introduction-video"
date: 2016-02-25T16:17:05+00:00
drupal:
  nid: 2621
  path: /blog/2016/drupal-vm-quick-introduction-video
  body_format: markdown
  redirects: []
tags:
  - ansible
  - drupal
  - drupal planet
  - drupal vm
  - tutorial
  - vagrant
  - video
---

After months of having this on my todo list, I've finally had the time to record a quick introduction video for [Drupal VM](http://www.drupalvm.com/). Watch the video below, then a transcript below the video:

<p style="text-align: center;"><iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/PR9uh_GGZhI?rel=0" frameborder="0" allowfullscreen></iframe></p>

Drupal VM is a local development environment for Drupal that's built with Vagrant and Ansible. It helps you build and maintain Drupal sites using best practices and the best tools. In this quick overview, I'll show you where you can learn more about Drupal VM, then show you a simple Drupal VM setup.

The [Drupal VM website](http://www.drupalvm.com/) gives a general overview of the project and links to:

  - [Documentation](http://docs.drupalvm.com/)
  - [Drupal VM's source code on GitHub](https://github.com/geerlingguy/drupal-vm)
  - [A link to download Drupal VM](https://github.com/geerlingguy/drupal-vm/archive/master.zip).

I'm going to build Drupal VM on my Mac using the [Quick Start Guide](https://github.com/geerlingguy/drupal-vm#quick-start-guide).

First, download [Vagrant](https://www.vagrantup.com/downloads.html) using the link in the Quick Start Guide and install it on your computer. Vagrant will install the only other required application, VirtualBox, the first time you run it. (If you're on a Mac or Linux PC, you should also install Ansible for the best experience.)

Next, go back to the Drupal VM website, then download Drupal VM using the download link.

  - Copy the `example.drupal.make.yml` file to `drupal.make.yml`.
  - Then copy `example.config.yml` to `config.yml`, and make changes to suit your environment.

I removed some of the tools inside the `installed_extras` section since I don't need them for this demonstration.

Open your Terminal, and change directories into the Drupal VM directory using the `cd` command.

```
cd ~/Downloads/drupal-vm-master
```

Type in `vagrant up`, and after a few minutes, Drupal VM will be set up and ready for you to use.

Once the VM is built, visit [http://dashboard.drupalvm.dev/](http://dashboard.drupalvm.dev/) to see an overview of all the sites and software on your VM. Visit [http://drupalvm.dev/](http://drupalvm.dev/) to see the Drupal 8 site that was automatically created.

At this point, after I'm finished working on my project, I can shut down the VM using `vagrant halt`, restart it with `vagrant reload`, or delete it and start over from scratch with `vagrant destroy`.

I'll be posting other videos demonstrating Drupal VM on Windows, Drupal VM with PHP 7, and how to use Drupal VM with existing Drupal sites, or multisite Drupal installs!

For more information about Drupal VM, visit the Drupal VM website at [http://www.drupalvm.com/](http://www.drupalvm.com/).
