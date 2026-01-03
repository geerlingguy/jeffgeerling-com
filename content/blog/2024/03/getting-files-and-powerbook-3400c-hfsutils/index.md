---
nid: 3353
title: "Getting files to and from a PowerBook 3400c with hfsutils"
slug: "getting-files-and-powerbook-3400c-hfsutils"
date: 2024-03-01T22:28:23+00:00
drupal:
  nid: 3353
  path: /blog/2024/getting-files-and-powerbook-3400c-hfsutils
  body_format: markdown
  redirects: []
tags:
  - cf
  - homebrew
  - mac
  - mac os
  - marchintosh
  - powerbook
  - restore
  - retro
---

{{< figure src="./powerbook-3400c-booting-macos-8.6.jpg" alt="PowerBook 3400c booting Mac OS 8.6" width="700" height="auto" class="insert-image" >}}

There are about a dozen ways to get files to and from an older Mac like my PowerBook 3400c, but right now (at least until I figure out a good way to get my NAS -> an AppleTalk server -> 3400c working), my preferred method is via a CF card—I pop the CF card into a [CF-to-PCMCIA adapter](https://amzn.to/3IhZDwi), then insert that into one of my PowerBook 3400's PC card slots, and bingo: removable flash storage on a 1990s laptop!

I still have a few CF cards kicking around (I used them with my old Nikon D700 camera), and you can buy a [4GB SanDisk Ultra CF card](https://amzn.to/3SXyljW) new from Amazon still—albeit for the price of $35... Sometimes the smaller/older cards work better with old Macs, and most of the files I deal with are well under a few MB anyways.

But in my case, I had a specific task I wanted to accomplish. I wanted to restore my PowerBook 3400c to its original state using the restore CD it came with (with Mac OS 7.6), then upgrade it to 8.6, which I'm told about the most stable/flexible Mac OS version that runs on the [PowerPC 603e CPU it ships with](https://everymac.com/systems/apple/powerbook/specs/mac_powerbook3400c_200.html). After that, I needed to copy over some files, but without any networking or USB.

## Mac OS 8.6 Upgrade

The first step was upgrading the 7.6 install to 8.6. (And luckily, the 7.6 restore went without a hitch, as the original 12x CD-ROM drive works a treat, and the original restore CD was in mint condition.)

To do that, I popped the CF card in my USB card reader, and plugged that into my modern Mac.

I downloaded the [`Mac_OS_8.6.toast_.zip`](http://macintoshgarden.org/apps/mac-os-85-851-update) CD image from Macintosh Garden, unzipped it, then used Terminal to write the 8.6 CD to the CF card:

  1. Find the CF card with `diskutil list` (in my case, it was `/dev/disk5`, a 4 GB external drive)
  2. Write the toast file to the CF card: `sudo dd if="/path/to/Mac OS 8.6.toast" of=/dev/disk5 bs=1M status=progress`

Note the quotes (`""`) around the file path—if there are spaces in any part of it, make sure you put the whole path in quotes.

After a couple minutes, `dd` completed it's job, and I pulled the CF card.

I booted the PowerBook 3400c into 7.6, and inserted the CF card using my PCMCIA adapter, and it appeared as if it were the original "Mac OS 8.6" CD. I opened that, ran the installer, and waited for it to complete.

## Copying files

To get other files onto the system, I formatted the CF card once the 8.6 upgrade was complete:

  1. Open Utilities > Drive Setup
  2. Select the CF card volume (e.g. 'Mac OS 8.6')
  3. Initialize it

Eject the CF card (by dragging it to the Trash, and waiting for the PCMCIA eject mechanism to pop it out), then plug it back into your newer Mac.

You'll get a 'Disk unreadable' message, just click Ignore.

Now, to copy any other files to/from the HFS-formatted drive, you'll need to install `hfsutils`. I should note the blog post that inspired this post was [How to mount HFS Classic drives on MacOS Catalina and later](https://www.matthewhughes.co.uk/how-to-mount-hfs-classic-drives-on-macos-catalina-and-later/) from Matthew Hughes.

But make sure you have [Homebrew](https://brew.sh) installed, then install `hfsutils`:

```
brew install hfsutils
```

Now, run `diskutil list` again to see which disk is the CF card—hopefully it's the same as before, e.g. `/dev/disk5`. You can mount the drive using `hmount`, like so:

```
sudo hmount /dev/disk5
```

This _won't_ mount it like a typical disk on the Mac, however—it's just mounted in the _ether_... you can only interact with the drive using `hfsutils`. And as a note, classic Mac OS used `:` instead of `/` to indicate directory traversal.

> Note: If your drive has multiple partitions, you might need to just mount one of them—that's outside the purview of this blog post. I've only been testing with one partition!

For example:

  - To get a directory listing: `sudo hls`
  - To copy a folder from the drive to your Mac: `sudo hcopy -r ":Folder Name" ./
  - To copy a file from your Mac to the drive: `sudo hcopy -r ./filename.sit ":"

I found I didn't need to add the `-r` option for 'raw' file copies, as the default 'automatic' file detection worked, but it's fine to be explicit and specify it.

Once you're done copying the files, unmount the drive before disconnecting it:

```
sudo humount
```
