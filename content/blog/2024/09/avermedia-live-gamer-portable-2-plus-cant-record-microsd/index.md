---
nid: 3407
title: "AVerMedia Live Gamer Portable 2 Plus - Can't record to microSD"
slug: "avermedia-live-gamer-portable-2-plus-cant-record-microsd"
date: 2024-09-27T14:36:42+00:00
drupal:
  nid: 3407
  path: /blog/2024/avermedia-live-gamer-portable-2-plus-cant-record-microsd
  body_format: markdown
  redirects: []
tags:
  - 4k
  - avermedia
  - hdmi
  - microsd
  - recording
  - screen
---

I recently purchased an [AVerMedia Live Gamer Portable 2 Plus](https://amzn.to/3TMeYv8) to help record screens on devices I test at my desk.

It's claim to fame is being able to record to a microSD card standalone (at resolutions up to 1080p60), without having a separate computer attached.

For my 4K cameras, I typically use an [Atomos Ninja V](https://amzn.to/4elL8pA), since it can record in full 4K resolution, but that thing is $700—the Live Gamer Portable is $120, and runs a lot cooler (and quieter).

I don't enjoy dealing with microSD cards, but it's more convenient than having to use OBS or some other recording software on my main computer just to capture the HDMI output of another device. Especially since I can't pass through the HD or 4K signal through my little Elgato USB capture card (they do make a few models that do this, but I digress).

_Anyway_, what brings me to this post is the fact I spent way too long trying to figure out the magical microSD card format required to be able to record on the device.

**tl;dr**: Format a 128 GB or less Class 10 or greater microSD card as **exFAT**, with the **Master Boot Record** scheme (if formatting in Disk Utility on a Mac).

I had tested a few other formats and finally found that to be the magic combo. FAT32 / MS-DOS is supported, but the device will split your recordings up into 4 GB chunks.

AVerMedia's website is organized pretty poorly, but here's at least one support doc I found that was somewhat useful: [Unable to start recording in PC-Free mode, LGP2 / LGP2 Plus LED displays a red LED. How to resolve this error?"](https://www.avermedia.com/support/faq/PC-FreeLGP2-LGP2-Plus-LEDLED).

Note that the problem I was having was the LED was blinking red; this apparently meant there was low space on the microSD card, but what I guess it also can mean is the device can't write to it.
