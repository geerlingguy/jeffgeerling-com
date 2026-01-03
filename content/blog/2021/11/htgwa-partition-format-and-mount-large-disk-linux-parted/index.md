---
nid: 3140
title: "HTGWA: Partition, format, and mount a large disk in Linux with parted"
slug: "htgwa-partition-format-and-mount-large-disk-linux-parted"
date: 2021-11-10T22:40:37+00:00
drupal:
  nid: 3140
  path: /blog/2021/htgwa-partition-format-and-mount-large-disk-linux-parted
  body_format: markdown
  redirects: []
tags:
  - disk
  - ext4
  - fdisk
  - format
  - gparted
  - htgwa
  - linux
  - tutorial
---

This is a simple guide, part of a series I'll call 'How-To Guide Without Ads'. In it, I'm going to document how I partition, format, and mount a large disk (2TB+) in Linux with `parted`.

Note that newer `fdisk` versions may work better with giant drives... but since I'm now used to `parted` I'm sticking with it for the foreseeable future.

## List all available drives

```
$ sudo parted -l
...
Error: /dev/sda: unrecognised disk label
Model: ATA Samsung SSD 870 (scsi)                                         
Disk /dev/sda: 8002GB
Sector size (logical/physical): 512B/512B
Partition Table: unknown
Disk Flags:
```

Good, I had plugged in that SSD just now, and it's brand new, so it doesn't have a partition table, label, or anything. It's the one I want to operate on. It's located at `/dev/sda`. I could also find that info with `lsblk`.

## Partition your drive with `parted`

```
$ sudo parted /dev/sda
(parted) mklabel gpt             # to create a partition table
(parted) print                   # to verify parition info
(parted) mkpart primary 0% 100%  # create primary partition filling entire disk
(parted) quit
```

## Verify you see the partition with `fdisk`

```
$ sudo fdisk -l /dev/sda                                        
Disk /dev/sda: 7.3 TiB, 8001563222016 bytes, 15628053168 sectors
Disk model: Samsung SSD 870 
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 44C96693-5B5E-4ABB-AEEC-A60C613E7EC6

Device     Start         End     Sectors  Size Type
/dev/sda1   2048 15628052479 15628050432  7.3T Linux filesystem
```

Now we know the partition ID, `/dev/sda1`.

## Format the partition

I almost always use EXT4, because it's nice and reliable:

```
$ sudo mkfs.ext4 /dev/sda1
mke2fs 1.44.5 (15-Dec-2018)
Discarding device blocks: done                            
Creating filesystem with 1953506304 4k blocks and 244191232 inodes
Filesystem UUID: c597dcb4-83b2-4a93-a8a0-34d17af17729
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
	4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968, 
	102400000, 214990848, 512000000, 550731776, 644972544, 1934917632

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (262144 blocks): done
Writing superblocks and filesystem accounting information: done 
```

## Mount the partition

```
$ sudo mkdir /mnt/mydrive
$ sudo mount /dev/sda1 /mnt/mydrive
```

## Verify the mount shows up with `df`

```
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/sda1       7.3T   93M  6.9T   1% /mnt/mydrive
```

Bingo! It's mounted.

## Make the mount persist

If you don't add the mount to `/etc/fstab`, it won't be mounted after you reboot!

First, get the `UUID` of the drive (the value inside the quotations in the output below—and _not_ the `PARTUUID`):

```
$ sudo blkid
...
/dev/sda1: UUID="c597dcb4-83b2-4a93-a8a0-34d17af17729" TYPE="ext4" PARTLABEL="primary" PARTUUID="99457865-24e2-4e2a-becd-1d6498de2369"
```

Then, edit `/etc/fstab` (e.g. `sudo nano /etc/fstab`) and add a line like the following to the end:

```
UUID=c597dcb4-83b2-4a93-a8a0-34d17af17729 /mnt/mydrive ext4 defaults 0 0
```

Save that file and reboot.

> Note: If `genfstab` is available on your system, use it instead. Much less likely to asplode things: `genfstab -U /mnt/mydrive | sudo tee -a /etc/fstab`.
>
> Note 2: You can verify the fstab syntax is correct with `sudo findmnt --verify`

## Verify the mount persisted.

After reboot:

```
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/sda1       7.3T   93M  6.9T   1% /mnt/mydrive
```
