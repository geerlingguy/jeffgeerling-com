---
nid: 2840
title: "Re-partitioning and reinstalling a newer version of Fedora on my laptop"
slug: "re-partitioning-and-reinstalling-newer-version-fedora-on-my-laptop"
date: 2018-04-13T16:24:59+00:00
drupal:
  nid: 2840
  path: /blog/2018/re-partitioning-and-reinstalling-newer-version-fedora-on-my-laptop
  body_format: markdown
  redirects: []
tags:
  - fedora
  - fedora 26
  - install
  - linux
  - partition
  - pc
  - ssd
  - tutorial
  - upgrade
---

{{< figure src="./fedora-26-installing-software.jpg" alt="Fedora 26 Installer - Installing software progress bar" width="650" height="399" class="insert-image" >}}

I wanted to document this process on my blog, since it's the second time I've had to do it, and it always takes me way longer to figure it out than it should... basically, here's how you can take a laptop with a hard disk that's running an older version of Fedora (in my case, Fedora 23), use the Fedora install media to re-partition the drive, then install a newer version of Fedora (in my case, Fedora 26):

  1. Boot to the Fedora install media (I used a USB flash drive that I prepared on my Mac).
  1. In the installer, choose the install disk, and pick the one where you currently have Fedora installed (I have one separate physical SSD in my laptop for Windows 10, another for Fedora, and a third for Ubuntu, just to make it easier to manage partitions without blowing out other OSes).
  1. If you want to be brave and attempt to re-partition the disk manually, choose "Advanced Custom (Blivet-GUI)" under 'Storage Configuration', then follow the advice in the Fedora [Recommended Partitioning Scheme](https://docs-old.fedoraproject.org/en-US/Fedora/html/Installation_Guide/sect-installation-gui-manual-partitioning-recommended.html) documentation to create new partitions.
  1. If you're like me, and want to just wipe out all the old stuff and let the installer repartition the drive, choose 'Automatic' under Storage Configuration, then click 'Done'.
  1. At this point, the installer will mention there's not enough free space—click 'Reclaim space'.
  1. On the 'Reclaim disk space' screen, click 'Delete all' to delete all the partitions and get back all the free space on the drive, then click 'Reclaim space'.
    1. Note: If you have a mount that has data you'd like to preserve, you can leave it of course... but I automate everything and store all my important data in the cloud, so I like to blow away everything then restore it all using Ansible and automation afterwards. It's a good test of your backup and recovery strategy for sure :)
  1. Customize any other installation options (Timezone, Network connection details, etc.), then click 'Begin Installation'.
  1. While Fedora is installing, set a root password and add a new admin user account if desired, then wait for install to complete!

One nice thing about the whole process: until you begin the actual Fedora installation, the physical partitions are not touched... so if you accidentally click the wrong button, or try a custom partitioning scheme but totally screw it up, you can back out of the installation and start over, no harm, no foul!
