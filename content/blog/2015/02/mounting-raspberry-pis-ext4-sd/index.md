---
nid: 2479
title: "Mounting a Raspberry Pi's ext4 SD card on Ubuntu 14.04 inside VirtualBox on Mac OS X"
slug: "mounting-raspberry-pis-ext4-sd"
date: 2015-02-09T14:49:21+00:00
drupal:
  nid: 2479
  path: /blogs/jeff-geerling/mounting-raspberry-pis-ext4-sd
  body_format: full_html
  redirects: []
tags:
  - ext4
  - flash
  - mac
  - microsd
  - raspberry pi
  - raspbian
  - sd
  - usb
  - virtualbox
aliases:
  - /blogs/jeff-geerling/mounting-raspberry-pis-ext4-sd
---

Since I'm running a Mac, and don't have a spare linux-running machine that can mount ext4-formatted partitions (like those used by default for official Raspberry Pi distributions like Raspbian on SD cards), I don't have a simple way to mount the boot partition on my Mac to tweak files on the Pi; this is a necessity if, for example, you break some critical configuration and the Pi no longer boots cleanly.

To mount an ext4-formatted SD or microSD card on a Mac, the easiest option is to use VirtualBox (and, in my case, Vagrant with one of <a href="http://files.jeffgeerling.com/">Midwestern Mac's Ubuntu boxes</a>). Boot a new linux VM (any kind will do, as long as it's modern enough to support ext4), shut it down, go into Settings for the VM inside VirtualBox and enable USB, then reboot.

Follow these steps once the VM is booted, to mount the flash drive:

<ol>
<li>Plug in the flash drive once the VM is booted.</li>
<li>Click on the USB icon in VirtualBox's window, and select the flash drive to 'capture' it inside the VM.</li>
<li>List all visible drives on the system: <code>$ sudo fdisk -l</code>, and it should be one of <code>/dev/sdb1</code> or <code>/dev/sdb2</code> (usually, whichever is larger, with 'System' of 'Linux'.</li>
<li>Make a directory into which you'll mount the drive: <code>$ mkdir /media/usb</code>
<li>Mount the drive: <code>$ sudo mount /dev/sdb2 /media/usb</code>
<li>All finished! cd into <code>/media/usb</code> and browse the contents of the drive.</li>
</ol>

This process was tested with Ubuntu 14.04, but should work with most Linux distros.
