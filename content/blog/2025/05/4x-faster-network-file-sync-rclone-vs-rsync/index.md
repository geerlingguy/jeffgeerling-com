---
nid: 3463
title: "4x faster network file sync with rclone (vs rsync)"
slug: "4x-faster-network-file-sync-rclone-vs-rsync"
date: 2025-05-06T17:26:28+00:00
drupal:
  nid: 3463
  path: /blog/2025/4x-faster-network-file-sync-rclone-vs-rsync
  body_format: markdown
  redirects: []
tags:
  - backup
  - file copy
  - nas
  - network
  - rclone
  - rsync
---

For the past couple years, I have transported my 'working set' of video and project data to and from work on an external Thunderbolt NVMe SSD.

But it's always been _slow_ when I do the sync. In a typical day, I may generate a new project folder with 500-1000 individual files, and dozens of them may be 1-10 GB in size.

The Thunderbolt drive I had was capable of well over 5 GB/sec, and my 10 Gbps network connection is capable of 1 GB/sec. I even [upgraded my Thunderbolt drive to Thunderbolt 5 lately](https://www.youtube.com/watch?v=gaV-O6NPWrI)... though that was not the bottleneck.

I used the following rsync command to copy files from a network share mounted on my Mac to the drive (which I call "Shuttle"):

```
rsync -au --progress --stats /Volumes/mercury/* /Volumes/Shuttle/Video_Projects
```

`mercury` is so named because it's a fast NVMe-backed NAS volume on my [Arm NAS](/blog/2024/building-efficient-server-grade-arm-nas) (all my network volumes are named after celestial bodies).

As a test, I deleted one of the dozen or so active projects off my 'Shuttle' drive, and ran my `rsync` copy:

```
$ time rsync -au --progress --stats /Volumes/mercury/* /Volumes/Shuttle/Video_Projects
Radxa Orion O6/
Radxa Orion O6/.DS_Store
           6148 100%    4.80MB/s   00:00:00 (xfer#1, to-check=1582/3564)
Radxa Orion O6/Micro Center Visit Details.pages
         141560 100%    9.83MB/s   00:00:00 (xfer#2, to-check=1583/3564)
Radxa Orion O6/Radxa Orion O6.md
          19817 100%    1.89MB/s   00:00:00 (xfer#3, to-check=1584/3564)
Radxa Orion O6/BIOS and Images/
Radxa Orion O6/BIOS and Images/orion-o6-bios-0.2.2-1.zip
        3916964 100%   83.32MB/s   00:00:00 (xfer#4, to-check=1586/3564)
Radxa Orion O6/BIOS and Images/orion-o6-bios-9.0.0-apr-11.7z
        4341505 100%  112.62MB/s   00:00:00 (xfer#5, to-check=1587/3564)
Radxa Orion O6/Scratch/
Radxa Orion O6/Scratch/bios 9.0.0 - screen acpi and debian 12 attempt.mp4
      254240026 100%  114.11MB/s   00:00:02 (xfer#6, to-check=1589/3564)
...
Number of files: 3564
Number of files transferred: 122
Total file size: 244284287846 B
Total transferred file size: 62947785101 B
Unmatched data: 62947785101 B
Matched data: 0 B
File list size: 444318 B
File list generation time: 9.155 seconds
File list transfer time: 0.078 seconds
Total sent: 62955918871 B
Total received: 2728 B

sent 62955918871 bytes  received 2728 bytes  128990035 bytes/sec
total size is 244284287846  speedup is 3.88

real	8:17.57
user	3:13.14
sys	2:45.45
```

The full copy took over 8 minutes, for a total of about 59 GiB of files copied. There are two problems:

  1. `rsync` performs copies single-threaded, _serially_, meaning only one file is copied at a time
  2. Even for very large files, `rsync` seems to max out on this network share around 350 MB/sec

I had been playing with different compression algorithms, trying to `tar` then pipe that to `rsync`, even experimenting with running the `rsync` daemon instead of SSH... but never could I get a _significant_ speedup! In fact, some compression modes would actually slow things down as my energy-efficient NAS is running on some slower Arm cores, and they bog things down a bit single-threaded...

## `rclone` to the rescue

I've been using `rclone` as part of my [3-2-1 backup plan](/blog/2021/my-backup-plan) for years. It's amazing at copying, moving, and syncing files from and to almost any place (including Cloud storage, local storage, NAS volumes, etc.), but I had somehow pigeonholed it as "for cloud to local or vice-versa", and never considered it for _local_ transfer, like over my own LAN.

But it has an option that allows transfers in parallel, `--multi-thread-streams`, which [Stack Overflow user `dantebarba` suggested](https://stackoverflow.com/a/62460707) someone use in the same scenario.

So I gave it a try.

After fiddling a bit with the exact parameters to match rsync's `-a`, and handling the weird symlinks like `.fcpcache` directories Final Cut Pro spits out inside project files, I came up with:

```
rclone sync \
  --exclude='**/._*' \
  --exclude='.fcpcache/**' \
  --multi-thread-streams=32 \
  -P -L --metadata \
  /Volumes/mercury/ /Volumes/Shuttle/Video_Projects
```

Using this method, I could see my Mac's network connection quickly max out around 1 GB/sec, completing the same directory copy in 2 minutes:

```
$ rclone sync \                                                                       
  --exclude='**/._*' \
  --exclude='.fcpcache/**' \
  --multi-thread-streams=32 \
  --progress --links --metadata \
  /Volumes/mercury/ /Volumes/Shuttle/Video_Projects
2025/05/06 12:03:57 NOTICE: Config file "/Users/jgeerling/.config/rclone/rclone.conf" not found - using defaults
Transferred:   	   58.625 GiB / 58.625 GiB, 100%, 0 B/s, ETA -
Checks:              2503 / 2503, 100%
Transferred:          122 / 122, 100%
Server Side Copies:   122 @ 58.625 GiB
Elapsed time:      2m15.3s
```

<s>I'm not 100% sure why `rclone` says 59 GB were copied, versus `rsync`'s 63 GB. Probably the exclusion of the `.fcpcache` directory?</s> lol units... GiB vs GB ;)

But the conclusion—especially after seeing my 10 Gbps connection _finally_ being fully utilized—is that `rclone` is about 4x faster working in parallel.

I also ran comparisons just changing out a couple files, and `rclone` and `rsync` were almost identical, as the full scan of the directory tree for metadata changes takes about the same time on both (about 18 seconds). It's just the parallel file transfers that help `rclone` pull ahead.
