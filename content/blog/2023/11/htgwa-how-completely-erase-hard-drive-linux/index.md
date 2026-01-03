---
nid: 3329
title: "HTGWA: How to completely erase a hard drive in Linux"
slug: "htgwa-how-completely-erase-hard-drive-linux"
date: 2023-11-22T19:27:39+00:00
drupal:
  nid: 3329
  path: /blog/2023/htgwa-how-completely-erase-hard-drive-linux
  body_format: markdown
  redirects: []
tags:
  - erase
  - format
  - hard drive
  - hdd
  - htgwa
  - linux
  - ssd
---

This is a simple guide, part of a series I'll call 'How-To Guide Without Ads'. In it, I'll show you how I completely initialize a hard drive so I can re-use it somewhere else (like Ceph) that doesn't like drives with partition information!

First, a warning: this blog post does not show how to _zero_ a hard drive, or _secure erase_. That's a slightly different process.

But as someone with way too many storage devices (from testing, mostly), I find myself in the position of trying to use a spare drive in some place where it expects a brand new drive, but winds up failing because the drive had a partition, or had valid boot files from an SBC or something.

I wanted to document the easiest way in Linux to completely reset a hard drive—at least from Linux's perspective.

The impetus was when I was trying to get some hard drives added to a Ceph OSD, and the process that tried adding them ran into an error stating `RuntimeError: Device /dev/sda has partitions.`

I tried quickly formatting the drive using 'Erase' in Disk Utility on my Mac... but that also creates a partition. Which is not the same as getting the drive to look brand new! And in Ceph's case, having a partition [is one of the failure criteria](https://docs.ceph.com/en/quincy/cephadm/services/osd/#deploy-osds) when creating OSDs.

So I plugged the drive into my Raspberry Pi using my [USB to SATA adapter](https://amzn.to/46qJhuU), and ran the following commands:

```
# 1. Confirm the current disk layout:
lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1   7.3T  0 disk 
├─sda1        8:1    1   200M  0 part 
└─sda2        8:2    1   7.3T  0 part /media/pi/Untitled

# 2. Unmount the drive if it's mounted, like above:
sudo umount /dev/sda2

# 3. Wipe all partition data:
sudo wipefs -a /dev/sda*
...
/dev/sda1: 2 bytes were erased at offset 0x000001fe (vfat): 55 aa
/dev/sda2: 8 bytes were erased at offset 0x00000003 (exfat): 45 58 46 41 54 20 20 20
/dev/sda: calling ioctl to re-read partition table: Success

# 4. Verify that worked:
lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1   7.3T  0 disk 

# Fourth, spin down the hard drive with hdparm
sudo hdparm -Y /dev/sda
```

Then disconnect the drive and you're good to go!

Now, if you _do_ want to do a secure erase, writing random bytes to every block on the drive, you can run something like:

```
sudo dd if=/dev/urandom of=/dev/sda bs=1M status=progress
```

But that takes a long time and I generally don't do that unless I'm selling off the storage device or passing it along to a friend or family member. `hdparm` also has a secure erase function, but it's pretty rare I actually do a secure erase... so just noting it here.
