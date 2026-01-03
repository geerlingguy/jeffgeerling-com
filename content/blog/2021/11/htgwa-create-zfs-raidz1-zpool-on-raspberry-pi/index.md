---
nid: 3144
title: "HTGWA: Create a ZFS RAIDZ1 zpool on a Raspberry Pi"
slug: "htgwa-create-zfs-raidz1-zpool-on-raspberry-pi"
date: 2021-11-12T05:15:57+00:00
drupal:
  nid: 3144
  path: /blog/2021/htgwa-create-zfs-raidz1-zpool-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - debian
  - filesystem
  - linux
  - raid
  - raspberry pi
  - tutorial
  - zfs
---

This is a simple guide, part of a series I'll call 'How-To Guide Without Ads'. In it, I'm going to document how I set up a ZFS zpool in RAIDZ1 in Linux on a Raspberry Pi.

## Prequisites

ZFS does not enjoy USB drives, though it can work on them. I wouldn't really recommend ZFS for the Pi 4 model B or other Pi models that can't use native SATA, NVMe, or SAS drives.

For my own testing, I am using a Raspberry Pi Compute Module 4, and there are a [variety of PCI Express storage controller cards](https://pipci.jeffgeerling.com/#sata-cards-and-storage) and [carrier boards](https://pipci.jeffgeerling.com/boards_cm) with integrated storage controllers that make ZFS much happier.

I have also only tested ZFS on 64-bit Raspberry Pi OS, on Compute Modules with 4 or 8 GB of RAM. No guarantees under other configurations.

## Installing ZFS

Since ZFS is not bundled with other Debian 'free' software (because of licensing issues), you need to install the kernel headers, then install two ZFS packages:

```
$ sudo apt install raspberrypi-kernel-headers  # linux-headers-$(uname -r) on Debian/Ubuntu
$ sudo apt install zfs-dkms zfsutils-linux  # don't need zfs-dkms on Ubuntu
```

## Verify ZFS is loaded

```
$ dmesg | grep ZFS
[ 5393.504988] ZFS: Loaded module v2.0.2-1~bpo10+1, ZFS pool version 5000, ZFS filesystem version 5
```

You should see something like the above. If not, it might not have loaded correctly.

## Prepare the disks

You should have at least three drives set up and ready to go. And make sure you don't care about anything on them. They're gonna get erased.

List all the devices on your system:

```
$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    0  7.3T  0 disk 
└─sda1        8:1    0  7.3T  0 part /mnt/mydrive
sdb           8:16   0  7.3T  0 disk 
sdc           8:32   0  7.3T  0 disk 
sdd           8:48   0  7.3T  0 disk 
sde           8:64   0  7.3T  0 disk 
nvme0n1     259:0    0  7.3T  0 disk 
└─nvme0n1p1 259:1    0  7.3T  0 part /
```

I want to put `sda` through `sde` into the RAIDZ1 volume. I noticed `sda` already has a partition and a mount. We should make sure all the drives that will be part of the array are partition-free:

```
$ sudo umount /dev/sda?; sudo wipefs --all --force /dev/sda?; sudo wipefs --all --force /dev/sda
$ sudo umount /dev/sdb?; sudo wipefs --all --force /dev/sdb?; sudo wipefs --all --force /dev/sdb
...
```

Do that for each of the drives. If you didn't realize it yet, this wipes everything. It doesn't zero the data, so _technically_ it could still be recovered at this point!

Check to make sure nothing's mounted (and make sure you have removed any of the drives you'll use in the array from `/etc/fstab` if you had persistent mounts for them in there!):

```
$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    0  7.3T  0 disk 
sdb           8:16   0  7.3T  0 disk 
sdc           8:32   0  7.3T  0 disk 
sdd           8:48   0  7.3T  0 disk 
sde           8:64   0  7.3T  0 disk 
nvme0n1     259:0    0  7.3T  0 disk 
└─nvme0n1p1 259:1    0  7.3T  0 part /
```

Looking good, time to start building the array!

## Create a RAIDZ1 zpool

The following command will create a zpool with all the block devices listed:

```
$ sudo zpool create zfspool raidz1 sda sdb sdc sdd sde -f
```

> For production use, you should really read up on the benefits and drawbacks of different RAID levels in ZFS, and how to structure zpools and vdevs. The specific structure you should use depends on how many and what type of drives you have, as well as your performance and redundancy needs.

Verify the pool is set up correctly:

```
$ zfs list
NAME      USED  AVAIL     REFER  MOUNTPOINT
zfspool   143K  28.1T     35.1K  /zfspool

$ zpool status -v zfspool
  pool: zfspool
 state: ONLINE
config:

	NAME        STATE     READ WRITE CKSUM
	zfspool     ONLINE       0     0     0
	  raidz1-0  ONLINE       0     0     0
	    sda     ONLINE       0     0     0
	    sdb     ONLINE       0     0     0
	    sdc     ONLINE       0     0     0
	    sdd     ONLINE       0     0     0
	    sde     ONLINE       0     0     0

errors: No known data errors
```

And make sure it was mounted so Linux can see it:

```
$ df -h
...
zfspool          29T  128K   29T   1% /zfspool
```

## Destroy a pool

If you no longer like swimming in the waters of ZFS, you can destroy the pool you created with:

```
$ sudo zpool destroy zfspool
```

> Note: This will wipe out the pool and lead to data loss. Make sure you're deleting the right pool and don't have any data inside that you care about.
