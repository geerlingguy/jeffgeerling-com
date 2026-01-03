---
nid: 2342
title: "Problems copying a huge Aperture library from one drive to another"
slug: "problems-copying-huge-aperture"
date: 2011-11-05T19:14:07+00:00
drupal:
  nid: 2342
  path: /blogs/jeff-geerling/problems-copying-huge-aperture
  body_format: markdown
  redirects: []
tags:
  - copy
  - file copy
  - files
  - finder
  - linux
  - rsync
  - sync
  - terminal
  - tricks
  - unix
aliases:
  - /blogs/jeff-geerling/problems-copying-huge-aperture
---

I've often had trouble copying files with Mac OS X's Finder. From back in the Mac OS X Beta days (when it was based on NeXT's UI), hard drive to hard drive copies, network copies, and backups have often had strange quirks, and one of the strangest I've yet found happened yesterday when I tried copying a ~170GB Aperture library from one external USB drive to another.

I tried copying the library three times, and each time the copy would get to about 24GB, the hard drive (from which the library was being copied) would make a loud CLICK, and then it would unmount and remount, stopping the library file copy. This particular drive has never had troubles in the past, and the fact that it kept doing the CLICK-die thing at 24GB meant that there may have been a file problem or a Finder bug causing the problem.

I verified the drive using Disk Utility (could've gone deeper and used other utilities too), but only found one or two small errors (a file count one file off, or a few improper permissions). After repairing the disk, the drive still clicked off at 24GB.

So, finally, after having copied about 14GB of data from one of my web servers to another, I decided to use a rather old-fashioned technique to try to copy the two librarys—the trusty UNIX utility rsync. This little utility basically takes a look at a 'source' directory, compares it to the 'destination' directory, and makes the directory structure and file structure identical. I won't explain much more about it, other than it's rock solid as a file copy/sync tool, and has been in use for many years.

Using the command below, I simply let rsync run for a couple hours (USB 2 is sloooow compared to FW 800, which I would usually use for larger libraries), and all the files were copied successfully:

```
$ rsync -avz --stats /Volumes/Utility/Photo\ Libraries/Aperture\ Library.aplibrary /Volumes/New\ Drive/Photo\ Libraries/
```

Looks to me like Finder should just use rsync or cp for file/folder copies rather than whatever it uses currently :-)
