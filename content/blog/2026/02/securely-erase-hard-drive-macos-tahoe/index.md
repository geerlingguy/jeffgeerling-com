---
date: '2026-02-26T14:30:00-06:00'
tags: ['hard drive', 'hdd', 'erase', 'mac', 'macos', 'disk utility', 'guide']
title: 'How to Securely Erase an old Hard Drive on macOS Tahoe'
slug: 'securely-erase-hard-drive-macos-tahoe'
---
Apparently Apple thinks nobody with a modern Mac uses spinning rust (hard drives with platters) anymore.

I plugged in a hard drive from an old iMac into my Mac Studio using my [Sabrent USB to SATA Hard Drive](https://amzn.to/4aP7e3d) enclosure, and opened up Disk Utility, clicked on the top-level disk in the sidebar, and clicked 'Erase'.

{{< figure
  src="./no-secure-erase-sabrent-media-macos-tahoe-disk-utility.png"
  alt="Secure Erase option missing in macOS Tahoe Disk Utility"
  width="700"
  height="auto"
  class="insert-image"
>}}

Lo and behold, there's no 'Security Options' button on there, as there had been since—I believe—the very first version of Disk Utility in Mac OS X!

It seems like [this option may have been dropped in macOS 15 Sequoia](https://discussions.apple.com/thread/256053093), but regardless, if you want to write 1s, 0s, or do a [DOE-compliant 3-pass erase](https://apple.stackexchange.com/a/61272), you have to hop over to Terminal now.

Apple apparently hasn't gotten the memo, as [their macOS 26 Tahoe Disk Utility User Guide](https://support.apple.com/guide/disk-utility/erase-and-reformat-a-storage-device-dskutl14079/mac) currently states[^guidenote]:

> (Optional) If available, click Security Options, use the slider to choose how many times to write over the erased data, then click OK.
> 
> Secure erase options are available only for some types of storage devices. If the Security Options button is not available, Disk Utility cannot perform a secure erase on the storage device.

## Secure Erase with `diskutil` in Terminal

First, find your disk using `diskutil list`:

```
$ diskutil list
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *1.0 TB     disk0
   1:             Apple_APFS_ISC Container disk1         524.3 MB   disk0s1
   2:                 Apple_APFS Container disk3         994.7 GB   disk0s2
   3:        Apple_APFS_Recovery Container disk2         5.4 GB     disk0s3
...
/dev/disk9 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *1.0 TB     disk9
   1:                  Apple_HFS Macintosh HD            1.0 TB     disk9s1
```

Mine is `/dev/disk9`. Run the command `diskutil secureErase` on that disk, providing an integer for the secure option:

```
0 - Single-pass erase resulting in a zero fill.
1 - Single-pass erase resulting in a random-number fill.
2 - Seven-pass "secure" erase.
3 - Gutmann algorithm 35-pass "secure" erase.
4 - Three-pass "secure" erase.
```

For example:

```
$ diskutil secureErase 1 /dev/disk9
Started erase on disk9
[ / 0%..10%.............................................. ] 10.5% 
```

`diskutil`'s docs warn `Level 2, 3, or 4 secure erases can take an extremely long time`, but even a single pass takes a while on older drives, or some of the largest modern drives with 16+ TB. SATA performance has sadly not kept up with the times.

[^guidenote]: As of February 2026.
