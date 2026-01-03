---
nid: 2728
title: "How to securely erase free space on a hard drive (Mac)"
slug: "how-securely-erase-free-space-on-hard-drive-mac"
date: 2017-01-09T20:51:15+00:00
drupal:
  nid: 2728
  path: /blog/2017/how-securely-erase-free-space-on-hard-drive-mac
  body_format: markdown
  redirects: []
tags:
  - mac
  - security
  - tutorial
---

From time to time, I need to clean off the contents of a hard drive on one of my Macs—most often this is the case prior to selling the mac or giving it to someone else. Instead of just formatting the drive, installing macOS, then handing it off, I want to make sure all the contents I had stored on it are irrecoverably erased (I sometimes work on projects under NDA, and I also like having some semblance of privacy in general).

Disk Utility _used_ to expose this functionality in the UI, which made this a very simple operation. But it seems to have gone missing in recent macOS versions. Luckily, it's still available on the command line (via Terminal.app):

    diskutil secureErase freespace 0 "/Volumes/Macintosh HD"

This command would write zeroes on the entire 'Macintosh HD' drive. You can see a list of all the drives connected to your Mac with `ls /Volumes`. There are a few other common options available (instead of `0`) if you run `man diskutil` and scroll down to the `secureErase` section. I most commonly use:

  - `0` - Zero fill (good for quickly writing over all the free space).
  - `1` - Random fill (slightly better than all zeroes in most cases, but takes a little longer).
  - `4` - 3-pass 'DoE algorithm' erase (way slower, but better if I'm transferring the computer to someone I don't trust (e.g. not a close relation).

The other options are even more secure, according to brainy hardware people... but unless you're often targeted for hacking by multi-billion dollar nation states, it seems useless to me... especially in light of Apple's own warning (and likely the reason Apple removed it from the UI):

    NOTE: This kind of secure erase is no longer considered safe because modern devices have
    wear-leveling, block-sparing, and possibly-persistent cache hardware. The modern solution
    for quickly and securely erasing your data is strong encryption, with which mere destruction
    of the key more or less instantly renders your data irretrievable in practical terms.

I also encrypt my entire drive, as well as my Time Machine backups, so I feel fairly secure regardless of what kind of erasure mode I choose. I figure if a government wants to hack my personal info, there are a zillion other avenues they would be more successful in hacking than a 3-pass-erasure of a secondhand SSD or hard drive that had encrypted personal data.
