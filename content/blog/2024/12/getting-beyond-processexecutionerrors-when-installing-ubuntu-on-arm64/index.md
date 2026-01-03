---
nid: 3429
title: "Getting beyond ProcessExecutionErrors when installing Ubuntu on arm64"
slug: "getting-beyond-processexecutionerrors-when-installing-ubuntu-on-arm64"
date: 2024-12-16T23:27:18+00:00
drupal:
  nid: 3429
  path: /blog/2024/getting-beyond-processexecutionerrors-when-installing-ubuntu-on-arm64
  body_format: markdown
  redirects: []
tags:
  - ampere
  - arm64
  - install
  - thelio astra
  - ubuntu
---

Currently there are precious few SystemReady Arm computers—computers like the [System76 Thelio Astra](https://system76.com/desktops/thelio-astra-a1-n1/configure) I was sent recently to test.

The level or 'band' of [SystemReady SR](https://developer.arm.com/Architectures/Arm%20SystemReady%20Band) used by modern Ampere-based arm64 workstations and servers means you can install any out-of-the-box Linux distributions, as long as they provide an arm64-compatible installer.

Ubuntu has some of the most complete support for arm64, so I went to download a Live CD ISO I could flash to a USB stick, to install on my test Thelio Astra. For server installs (with no GUI), either 4k or 64k page sizes, there are easily-findable ISOs:

  - [Ubuntu Server for Arm](https://ubuntu.com/download/server/arm)

However, for desktop, you can only get it via daily build downloads:

  - [Ubuntu 24.04 (Noble Numbat) Daily Build](https://cdimage.ubuntu.com/daily-live/20240421/)

Regardless of download, I was having trouble installing Ubuntu on my system. The install would proceed as normal, but eventually it would error out, leaving the installation _kinda_ working.

{{< figure src="./ubuntu-error-message-installer-arm64.jpg" alt="Ubuntu installer on arm64 error with installation" width="700" height="auto" class="insert-image" >}}

```
Conmand: ['unshare', '--fork', '--pid', '--option=Dpkg::options::=--force-unsafe-io', '--option=Dpkg::options::=--force-confold', 'install', '--download-only', 'linux-generic-hwe-24.04']
```

I would have to manually mount the Ubuntu data partition, use `sudo chroot /mnt/partition_here`, and add a user account manually. But some other stuff in the install was broken too, and that's just no fun!

After posting about this in my [testing thread for the Thelio Astra](https://github.com/geerlingguy/sbc-reviews/issues/53), GitHub user bexcran mentioned:

> I'd guess it's getting confused about existing partitions.

And even though I was choosing the "Erase and install" option in the Ubuntu installers (both on Server and Desktop), for some reason (I guess just 'user misunderstanding'?), that was not wiping the disk enough that it would install successfully.

So to counter that, before completing the Ubuntu installation, I opened a Terminal window when booted from the Live Install CD, and ran these commands:

```
sudo wipefs /dev/nvme0n1 --all
sudo parted /dev/nvme0n1 print  # to confirm the partition table is wiped
```

After that, the installation completed without a hitch.

I'm not certain, but I don't remember having this issue on my x86 machines, when installing Ubuntu on them... though last time I tried a new Ubuntu install on one of those was probably a year or so ago!

I'm mostly posting this for my own future reference, because I can _guarantee_ I'll have the same problem again, and my silly brain won't remember that I just had to wipe the partitions prior to installing Ubuntu.
