---
nid: 2712
title: "Figuring out why an external USB hard drive won't spin down on my Mac"
slug: "figuring-out-why-external-usb-hard-drive-wont-spin-down-on-my-mac"
date: 2016-11-07T17:11:13+00:00
drupal:
  nid: 2712
  path: /blog/2016/figuring-out-why-external-usb-hard-drive-wont-spin-down-on-my-mac
  body_format: markdown
  redirects: []
tags:
  - energy efficiency
  - external
  - fs_usage
  - hard drive
  - hdd
  - mac
  - macos
  - terminal
  - usb
---

I am using a 2011 Mac mini as a [backup server for all the data I store on iCloud](http://www.jeffgeerling.com/blog/2016/i-made-switch-aperture-photos#backup), and for the first few days while I was setting up the Mac, I noticed the 4 TB and 2 TB external USB drives I had plugged in would spin down after a few minutes, and I would have blissful silence as long as there wasn't an active operation on that Mac (which should be fairly rare; just hourly Time Machine backups and periodic SSD activity since the iCloud libraries are all on SSD).

However, after a few weeks, I noticed that at least one of the two hard drives runs continuously, 24x7. Something on the Mac mini must keep hitting the drive and preventing it from spinning down.

To see what was happening, I used `sudo fs_usage | grep VOLUME` (in my case, `VOLUME` is `4\ TB\ Utility`) to monitor what processes were accessing the drive, and what files they were accessing. After a few minutes watching (and doing nothing else on the computer, to make sure I wasn't causing any extra filesystem seeks), there were a couple regular culprits:

```
10:52:13  getattrlist       /Volumes/4 TB Utility                                                            0.000005   lsd         
10:52:13  getattrlist       /Volumes/4 TB Utility                                                            0.000004   lsd         
10:52:37  getattrlist       /Volumes/4 TB Utility                                                            0.000006   lsd

10:55:32  stat64            es/4 TB Utility/.Spotlight-V100/Store-V2/069E7AE9-4CA8-4342-AF0A-EE472A279FC4    0.000007   mds_stores  
10:55:33  stat64            es/4 TB Utility/.Spotlight-V100/Store-V2/069E7AE9-4CA8-4342-AF0A-EE472A279FC4    0.000019   mds_stores

10:56:21  statfs64          /Volumes/4 TB Utility                                                            0.000009   Spotlight   
10:56:21  getattrlist       /Volumes/4 TB Utility                                                            0.000009   Spotlight   
10:56:22  fsgetpath         /Volumes/4 TB Utility                                                            0.000017   mds         
10:56:22  fsgetpath         /Volumes/4 TB Utility                                                            0.000011   mds         
10:56:22  stat64            /Volumes/4 TB Utility//Applications                                              0.000030   mds

10:58:15  getattrlist       /Volumes/4 TB Utility                                                            0.000010   mtmd        
10:58:15  lstat64           /Volumes/4 TB Utility/.MobileBackups                                             0.000004   mtmd        
10:58:15  getattrlist       /Volumes/4 TB Utility                                                            0.000010   mtmd        
10:58:15  getattrlist       /Volumes/4 TB Utility/.MobileBackups.trash                                       0.000005   mtmd        
10:58:15  lstat64           /Volumes/4 TB Utility/.MobileBackups.trash                                       0.000003   mtmd
```

It looks like the following processes were causing disk accesses:

  1. `mds`/Spotlight/`mds_stores` - related to Spotlight. Since I don't need to search data on this volume, I went into System Preferences > Spotlight > Privacy, and dragged the volume into the list of locations Spotlight will be prevented from searching.
  2. `mtmd` - related to Time Machine. It looks like, by default, Time Machine keeps some deleted files on the disk, just moved into a hidden `.MobileBackups` directory, to speed up recovery or make it possible to keep snapshot data available even when you're disconnected from your Time Machine volume (see [OS X's MobileBackups. What is It?](http://archive.ec/1NENQ)). But you can run `sudo tmutil disablelocal` to disable this functionality.

See also [this post](http://www.jackenhack.com/disk-that-refuses-to-sleep-in-mac-os-x-how-to-fix-it/), which I found when researching usage of fs_usage.

Someday, when all drives (even giant ones) are SSDs, this will be a non-issue. But I still have a bunch of 2, 3, and 4 TB spinning rust drives kicking around, and I like the energy (and noise) savings that comes from letting the drive spin down for inactivity.
