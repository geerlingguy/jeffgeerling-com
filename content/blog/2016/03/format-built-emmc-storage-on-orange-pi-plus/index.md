---
nid: 2628
title: "Format eMMC storage on an Orange Pi, Radxa, etc."
slug: "format-built-emmc-storage-on-orange-pi-plus"
date: 2016-03-08T03:13:06+00:00
drupal:
  nid: 2628
  path: /blog/2016/format-built-emmc-storage-on-orange-pi-plus
  body_format: markdown
  redirects: []
tags:
  - debian
  - emmc
  - fdisk
  - format
  - linux
  - mount
  - orange pi
  - partition
---

To use eMMC modules on the Orange Pi, Radxa, Milk-V, etc. as a writable volume in Linux, you need to delete the existing partitions (on my old Orange Pi, it was formatted as FAT/WIN32), create a new partition, format the partition, then mount it:

  1. Delete the existing partitions, and create a new partition:
    1. `sudo fdisk /dev/mmcblk1`
    2. `p` to list all partitions, then `d` and a number, once for each of the existing partitions.
    2. `n` to create a new partition, then use all the defaults, then `w` to write the changes.
  3. Format the partition: `sudo mkfs.ext4 -L "emmc" /dev/mmcblk1p1`
  4. Create a mount point: `sudo mkdir -p /mnt/emmc`
  5. Mount the disk: `sudo mount /dev/mmcblk1p1 /mnt/emmc`

Note your eMMC device may be a different ID, e.g. `mmcblk2` or `mmcblk0`, depending on the order the board firmware loads multiple devices in. Check with `lsblk` to see which device you would like to modify.
