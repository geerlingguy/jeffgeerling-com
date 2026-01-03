---
nid: 3159
title: "HTGWA: Use bcache for SSD caching on a Raspberry Pi"
slug: "htgwa-use-bcache-ssd-caching-on-raspberry-pi"
date: 2021-12-16T21:50:48+00:00
drupal:
  nid: 3159
  path: /blog/2021/htgwa-use-bcache-ssd-caching-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - bcache
  - htgwa
  - linux
  - nvme
  - performance
  - raid
  - ssd
  - tutorial
---

This is a simple guide, part of a series I'll call 'How-To Guide Without Ads'. In it, I'm going to document how I set up `bcache` on a Raspberry Pi, so I could use an SSD as a cache in front of a RAID array.

## Getting bcache

`bcache` is sometimes used on Linux devices to allow a more efficient SSD cache to run in front of a single or multiple slower hard drives—typically in a storage array.

In my case, I have three SATA hard drives: `/dev/sda`, `/dev/sdb`, and `/dev/sdc`. And I have one NVMe SSD: `/dev/nvme0n1`.

I [created a RAID5 array with `mdadm`](/blog/2021/htgwa-create-raid-array-linux-mdadm) for the three hard drives, and had the raid device `/dev/md0`.

I then installed `bcache-tools`:

```
$ sudo apt-get install bcache-tools
```

And used `make-bcache` to create the backing and cache devices:

```
$ sudo make-bcache -B /dev/md0
UUID:			eb360a2d-4c62-451d-8549-a68621c633e5
Set UUID:		c8b5c63c-0a44-49f3-bb65-cd4df9b751a0
version:		1
block_size:		1
data_offset:		16

$ sudo make-bcache -C /dev/nvme0n1
UUID:			15bf54e9-be21-4478-b676-a08dad937963
Set UUID:		dea419ba-d795-4566-b01f-bb57fa96eb21
version:		0
nbuckets:		15261770
block_size:		1
bucket_size:		1024
nr_in_set:		1
nr_this_dev:		0
first_bucket:		1
```

Then I tried to look in `/sys/block/md0/bcache/` so I could attach the cache to the backing device, but I realized `bcache` isn't loaded into the default Raspberry Pi OS kernel... so I'll have to compile that in.

## Getting `bcache` on Raspberry Pi OS

I [cross-compiled](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile) the Raspberry Pi Linux kernel, and when I did it, during the `menuconfig` portion, I selected the following option:

```
> Device Drivers
  > Multiple devices driver support (RAID and LVM)
    > Block device as cache (BCACHE)
```

I recompiled the kernel and copied my updated kernel to the Pi, then rebooted.

At this point, I could see the `bcache0` device was working:

```
pi@omv:~ $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda           8:0    0  3.6T  0 disk  
└─md0         9:0    0  7.3T  0 raid5 
  └─bcache0 254:0    0  7.3T  0 disk  /mnt
sdb           8:16   0  3.6T  0 disk  
└─md0         9:0    0  7.3T  0 raid5 
  └─bcache0 254:0    0  7.3T  0 disk  /mnt
sdc           8:32   0  3.6T  0 disk  
└─md0         9:0    0  7.3T  0 raid5 
  └─bcache0 254:0    0  7.3T  0 disk  /mnt
mmcblk0     179:0    0 14.8G  0 disk  
├─mmcblk0p1 179:1    0  256M  0 part  /boot
└─mmcblk0p2 179:2    0 14.6G  0 part  /
nvme0n1     259:0    0  7.3T  0 disk  
```

But if I checked on the status of the cache, it said there was no cache:

```
pi@omv:~ $ cat /sys/block/bcache0/bcache/state
no cache
```

## Attaching the SSD cache to the backing device

Finally, it's time to attach the SSD cache to the backing device:

```
$ sudo su  # switch to the root user
# cd /sys/block/md0/bcache/
# echo dea419ba-d795-4566-b01f-bb57fa96eb21 > attach
# cat state 
clean
```

The UUID in the `echo` command above comes from the 'Set UUID' output from the `make-bcache -C` command earlier.

## Creating a filesystem and mounting

To actually _use_ the device, I formatted it and mounted it to `/mnt`:

```
$ sudo mkfs.ext4 -E lazy_itable_init=0,lazy_journal_init=0 /dev/bcache0
$ sudo mount /dev/bcache0 /mnt
```

To avoid the initialization when making the filesystem, you can omit the `-E` option entirely. But for RAID arrays I typically let it go full blast on first initialization, because I don't like relying on `ext4lazyinit` on a RAID array—it can take days at its reduced rate, and affect RAID performance that whole time!

## Getting stats

You can check the stats from `bcache` with:

```
$ tail /sys/block/bcache0/bcache/stats_total/*
==> /sys/block/bcache0/bcache/stats_total/bypassed <==
563.1M

==> /sys/block/bcache0/bcache/stats_total/cache_bypass_hits <==
0

==> /sys/block/bcache0/bcache/stats_total/cache_bypass_misses <==
0

==> /sys/block/bcache0/bcache/stats_total/cache_hit_ratio <==
13

==> /sys/block/bcache0/bcache/stats_total/cache_hits <==
132

==> /sys/block/bcache0/bcache/stats_total/cache_miss_collisions <==
0

==> /sys/block/bcache0/bcache/stats_total/cache_misses <==
849

==> /sys/block/bcache0/bcache/stats_total/cache_readaheads <==
0
```

## Switching the caching mode

There are [multiple caching modes](https://wiki.ubuntu.com/ServerTeam/Bcache#Bcache_caching_modes), including `writeback`, `writethrough`, `writearound`, and `none`. The most performant (but most dangerous, especially if you're using a _single_ SSD and not a set of SSDs in RAID 1 for safety) is `writeback`, which caches reads, and writes data to the SSD first (considering a write 'complete' once written to the SSD), then asynchronously copies that data to the backing device.

Check the current caching mode with:

```
$ sudo cat /sys/block/bcache0/bcache/cache_mode
[writethrough] writeback writearound none
```

To change it, for example, to `writeback`:

```
$ sudo su - -c 'echo writeback > /sys/block/bcache0/bcache/cache_mode'
```

## Dropping the cache

If you want to pop the SSD off of the backing device, and use it again for other purposes, you have to first de-register it (otherwise you'll get errors like `probing initialization failed: Device or resource busy`):

```
$ sudo su
# cd /sys/block/md0/bcache
# echo 1 > detach  # Prints a 'cached_dev_detach_finish' message in `dmesg` log
# cd /sys/fs/bcache/dea419ba-d795-4566-b01f-bb57fa96eb21
# echo 1 > stop  # Prints a 'cache_set_free ' message in `dmesg` log
```

Then if you want to use the device for something else, wipe it with `wipefs`:

```
# wipefs -a /dev/nvme0n1
```

See the [kernel documentation for bcache](https://www.kernel.org/doc/Documentation/bcache.txt) for more detail and usage examples.
