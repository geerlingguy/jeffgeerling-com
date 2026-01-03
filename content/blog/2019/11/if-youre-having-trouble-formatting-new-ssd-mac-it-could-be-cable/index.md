---
nid: 2946
title: "If you're having trouble formatting a new SSD in a Mac, it could be the cable"
slug: "if-youre-having-trouble-formatting-new-ssd-mac-it-could-be-cable"
date: 2019-11-09T17:27:34+00:00
drupal:
  nid: 2946
  path: /blog/2019/if-youre-having-trouble-formatting-new-ssd-mac-it-could-be-cable
  body_format: markdown
  redirects: []
tags:
  - disk utility
  - format
  - ifixit
  - mac
  - mac mini
  - partition
  - repair
  - sata
  - ssd
---

> **tl;dr**: If you see weird errors when using or formatting a drive internally on a Mac (especially after upgrading to a newer and/or faster SATA hard drive), it could mean the SATA cable needs to be replaced.

<p style="text-align: center;">{{< figure src="./sata-ribbon-cable-mac-mini-mid-2011-lower.jpeg" alt="Mac mini mid-2011 lower SATA hard drive cable with connector" width="650" height="454" class="insert-image" >}}<br />
<em>Who would've thought such a tiny cable could cause so many problems?</em></p>

I have an older Mac mini (mid-2011 i5 model), and I use it as a general media server and network backup. It handles Time Machine backups for two other Macs, it has about 20 TB of external storage connected, and I also use it as a 'home base' to store all my Dropbox, iCloud, and Photos content locally, and store an extra Time Machine backup of all _that_. I'm a little nutty about backups... but I haven't lost a file in two decades and I don't want to start now ;-).

Anyways, my digital cruft has grown to the point it wouldn't fit on a 1 TB main drive anymore, so I decided to upgrade the Mac mini's internal drive to a 2 TB SSD, hopefully giving me another 2-4 years of life out of that computer before I have to find a new backup solution with more than 2 TB of storage.

I've replaced the drive a couple times before, and never had any issues. I'd plug the new SATA drive into my USB-to-SATA adapter, clone the disk using Disk Utility (now using [Carbon Copy Cloner](https://bombich.com) as of macOS 10.12, since Disk Utility won't restore APFS volumes cleanly anymore), and then use the iFixIt guide for [replacing the hard drive in a 2011 Mac mini](https://www.ifixit.com/Guide/Mac+mini+Mid+2011+Hard+Drive+Replacement/6422).

This time, I bought a [2TB SATA III (6 Gb/s) drive from Crucial](https://www.amazon.com/Crucial-MX500-NAND-SATA-Internal/dp/B078C515QL/ref=as_li_ss_tl?keywords=crucial+2tb+ssd&qid=1573319501&s=electronics&sr=1-3&linkCode=ll1&tag=mmjjg-20&linkId=3488aaab6a9498c130d7b0e7ea26239d&language=en_US), to replace an older SATA II Mushkin drive. The drive formatted via the USB-to-SATA adapter, and I cloned the disk successfully using CCC. I replaced the internal drive, and booted the Mini... and it wouldn't boot off the new drive!

So I used system restore (⌘-R while booting the Mac), and opened Disk Utility. It saw the new drive, and could mount and unmount it.

But when I tried to switch the startup disk, and it popped a message saying the disk could not be 'blessed'. I tried opening the terminal and manually blessing the disk with the `bless` command, but that failed.

Since I had two backups of the old drive, I decided to try re-formatting the new drive while it was inside the Mac mini. Many times (erasing and partitioning as both 'APFS' and 'Mac OS Extended (Journaled)'), it would start the process, then run into an error. I actually hit a few different errors, depending on the type of format I was attempting, including:

```
# While restoring in Disk Utility... at the very end.
The volume on device dev disk0(source volume) is not of type Apple_HFS or Apple_UFS

# When trying to partition the drive while it was in the Mac.
An internal error occurred while preflighting your volume for APFS conversion

# When trying to erase the disk in Terminal with `diskutil eraseDisk`.
Error: 12: POSIX reports: Cannot allocate memory
```

There were a few other errors, too... but eventually in all my Google searches, I found [this incredibly helpful answer from iFixIt's forums](https://www.ifixit.com/Answers/View/447882/Samsung+850+Evo+SSD+not+recognized+in+Mac+Mini+2011#answer448123). User Dan/@danj said:

> I'm thinking the drive cable has degraded so the faster data flows with the SSD is having problems. I've had a few that needed replacing.

I realized that I've now replaced the hard drive in this Mac mini 3 times... and the tiny flex cable and connector on the cable _is_ very fragile. It would probably last forever if you never touched it, but having to pull it and put it back in 3 times could definitely make it less-than-reliable.

So I went on Amazon and found a [Mac mini hard drive cable upgrade kit with part number 821-1500-A](https://www.amazon.com/gp/product/B07Q5GCHYG/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=e143d29c4861f19780c8a28a42dd34e4&language=en_US) for a little over $10. I ordered it, it arrived the next day, I swapped the cable, and now I'm having no trouble at all with the new SATA III Crucial drive.

Moral of the story? If you are upgrading your hard drive in a Mac (Mini, MacBook Pro, etc.), and the new drive has mysterious problems that don't happen when it's plugged in elsewhere, consider replacing the SATA cable!

(Unfortunately, newer Macs don't have replaceable hard drives anymore... so this might be a moot point in the future. I hope not.)
