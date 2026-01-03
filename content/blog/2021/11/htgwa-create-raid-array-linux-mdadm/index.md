---
nid: 3141
title: "HTGWA: Create a RAID array in Linux with mdadm"
slug: "htgwa-create-raid-array-linux-mdadm"
date: 2021-11-11T03:03:22+00:00
drupal:
  nid: 3141
  path: /blog/2021/htgwa-create-raid-array-linux-mdadm
  body_format: markdown
  redirects:
    - /blog/2021/htgwa-create-raid-0-array-mdadm
    - /blog/2021/htgwa-create-raid-0-array-linux-mdadm
aliases:
  - /blog/2021/htgwa-create-raid-0-array-mdadm
  - /blog/2021/htgwa-create-raid-0-array-linux-mdadm
tags:
  - htgwa
  - linux
  - mdadm
  - partition
  - raid
  - tutorial
---

This is a simple guide, part of a series I'll call 'How-To Guide Without Ads'. In it, I'm going to document how I create and mount a RAID array in Linux with `mdadm`.

In the guide, I'll create a RAID 0 array, but other types can be created by specifying the proper `--level` in the `mdadm create` command.

## Prepare the disks

You should have at least two drives set up and ready to go. And make sure you don't care about anything on them. They're gonna get erased. And make sure you don't care about the integrity of the data you're going to store on the RAID 0 volume. RAID 0 is good for speed... and that's about it. Any drive fails, all your data's gone.

> Note: Other guides, like [this excellent one on the Unix StackExchange site](https://unix.stackexchange.com/a/320330/16194), have a lot more detail. This is just a quick and dirty guide.

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

I want to RAID together `sda` through `sde` (crazy, I know). I noticed that `sda` already has a partition and a mount. We should make sure all the drives that will be part of the array are partition-free:

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

## Partition the disks with `sgdisk`

You could interactively do this with `gdisk`, but I like more automation, so I use `sgdisk`. If it's not installed, and you're on a Debian-like distro, install it: `sudo apt install -y gdisk`.

```
sudo sgdisk -n 1:0:0 /dev/sda
sudo sgdisk -n 1:0:0 /dev/sdb
...
```

Do that for each of the drives.

> **WARNING**: Entering the wrong commands here will wipe data on your precious drives. You've been warned. Again.

Verify there's now a partition for each drive:

```
pi@taco:~ $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    0  7.3T  0 disk 
└─sda1        8:1    0  7.3T  0 part 
sdb           8:16   0  7.3T  0 disk 
└─sdb1        8:17   0  7.3T  0 part 
sdc           8:32   0  7.3T  0 disk 
└─sdc1        8:33   0  7.3T  0 part 
sdd           8:48   0  7.3T  0 disk 
└─sdd1        8:49   0  7.3T  0 part 
sde           8:64   0  7.3T  0 disk 
└─sde1        8:65   0  7.3T  0 part 
...
```

## Create a RAID 0 array with `mdadm`

If you don't have `mdadm` installed, and you're on a Debian-like system, run `sudo apt install -y mdadm`.

```
$ sudo mdadm --create --verbose /dev/md0 --level=0 --raid-devices=5 /dev/sd[a-e]1
mdadm: chunk size defaults to 512K
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.
```

> You can specify different RAID levels with the `--level` option above. Certain levels require certain numbers of drives to work correctly!

## Verify the array is working

For RAID 0, it should immediately show `State : clean` when running the command below. For other RAID levels, it may take a while to initially `resync` or do other operations.

```
$ sudo mdadm --detail /dev/md0
/dev/md0:
           Version : 1.2
     Creation Time : Wed Nov 10 18:05:57 2021
        Raid Level : raid0
        Array Size : 39069465600 (37259.55 GiB 40007.13 GB)
      Raid Devices : 5
     Total Devices : 5
       Persistence : Superblock is persistent

       Update Time : Wed Nov 10 18:05:57 2021
             State : clean 
    Active Devices : 5
   Working Devices : 5
    Failed Devices : 0
     Spare Devices : 0

        Chunk Size : 512K

Consistency Policy : none

              Name : taco:0  (local to host taco)
              UUID : a5043664:c01dac00:73e5a8fc:2caf5144
            Events : 0

    Number   Major   Minor   RaidDevice State
       0       8        1        0      active sync   /dev/sda1
       1       8       17        1      active sync   /dev/sdb1
       2       8       33        2      active sync   /dev/sdc1
       3       8       49        3      active sync   /dev/sdd1
       4       8       65        4      active sync   /dev/sde1
```

You observe the progress of a rebuild (if choosing a level besides RAID 0, this will take some time) with `watch cat /proc/mdstat`. Ctrl-C to exit.

## Persist the array configuration to `mdadm.conf`

```
$ sudo mdadm --detail --scan --verbose | sudo tee -a /etc/mdadm/mdadm.conf
```

If you don't do this, the RAID array won't come up after a reboot. That would be sad.

## Format the array

```
$ sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0 /dev/md0
mke2fs 1.44.5 (15-Dec-2018)
Discarding device blocks: done                            
Creating filesystem with 9767366400 4k blocks and 610461696 inodes
Filesystem UUID: 5d3b012c-e5f6-49d1-9014-1c61e982594f
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
	4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968, 
	102400000, 214990848, 512000000, 550731776, 644972544, 1934917632, 
	2560000000, 3855122432, 5804752896

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (262144 blocks): done
Writing superblocks and filesystem accounting information: done 
```

In this example, I used `lazy` initialization to avoid the (very) long process of initializing all the inodes. For large arrays, especially with brand new drives that you know aren't full of old files, there's no practical reason to do it the 'normal'/non-lazy way (at least, AFAICT).

## Mount the array

Checking on our array with `lsblk` now, we can see all the members of `md0`:

```
$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda           8:0    0  7.3T  0 disk  
└─sda1        8:1    0  7.3T  0 part  
  └─md0       9:0    0 36.4T  0 raid0 
sdb           8:16   0  7.3T  0 disk  
└─sdb1        8:17   0  7.3T  0 part  
  └─md0       9:0    0 36.4T  0 raid0 
sdc           8:32   0  7.3T  0 disk  
└─sdc1        8:33   0  7.3T  0 part  
  └─md0       9:0    0 36.4T  0 raid0 
sdd           8:48   0  7.3T  0 disk  
└─sdd1        8:49   0  7.3T  0 part  
  └─md0       9:0    0 36.4T  0 raid0 
sde           8:64   0  7.3T  0 disk  
└─sde1        8:65   0  7.3T  0 part  
  └─md0       9:0    0 36.4T  0 raid0 
```

Now make a mount point and mount the volume:

```
$ sudo mkdir /mnt/raid0
$ sudo mount /dev/md0 /mnt/raid0
```

## Verify the mount shows up with `df`

```
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/md0         37T   24K   37T   1% /mnt/raid0
```

## Make the mount persist

If you don't add the mount to `/etc/fstab`, it won't be mounted after you reboot!

First, get the `UUID` of the array (the value inside the quotations in the output below):

```
$ sudo blkid
...
/dev/md0: UUID="5d3b012c-e5f6-49d1-9014-1c61e982594f" TYPE="ext4"
```

Then, edit `/etc/fstab` (e.g. `sudo nano /etc/fstab`) and add a line like the following to the end:

```
UUID=5d3b012c-e5f6-49d1-9014-1c61e982594f /mnt/raid0 ext4 defaults 0 0
```

Save that file and reboot.

> Note: If `genfstab` is available on your system, use it instead. Much less likely to asplode things: `genfstab -U /mnt/mydrive >> /mnt/etc/fstab`.

## Verify the mount persisted.

After reboot:

```
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/md0         37T   24K   37T   1% /mnt/raid0
```

## Drop the array

If you'd like to _drop_ or remove the RAID array and reset all the disk partitions so you could use them in another array, or separately, you need to do the following:

  1. Edit `/etc/fstab` and delete the line for the `/mnt/raid0` mount point.
  2. Edit `/etc/mdadm/mdadm.conf` and delete the lines you added earlier via `mdadm | tee`.
  3. Unmount the volume: `sudo umount /mnt/raid0`
  4. Wipe the ext4 filesystem: `sudo wipefs --all --force /dev/md0`
  5. Stop the RAID volume: `sudo mdadm --stop /dev/md0`
  6. Zero the superblock on all the drives: `sudo mdadm --zero-superblock /dev/sda1 /dev/sdb1 ...`

At this point, you should have back all the drives that were part of the array and can do other things with them.
