---
nid: 2542
title: "Orange Pi Plus Setup, Benchmarks, and Initial Impressions"
slug: "orange-pi-plus-setup-benchmarks-and-initial-impressions"
date: 2016-03-08T21:22:58+00:00
drupal:
  nid: 2542
  path: /blog/2016/orange-pi-plus-setup-benchmarks-and-initial-impressions
  body_format: markdown
  redirects: []
tags:
  - benchmarks
  - computer
  - dramble
  - linux
  - networking
  - orange pi
  - raspberry pi
  - reviews
---

> **tl;dr**: The Orange Pi Plus offers much better specs, and much better performance, than a similarly-priced Raspberry Pi. Unfortunately—and this is the case with most RPi competitors at this time—setup, hardware support, and the smaller repository of documentation and community knowledge narrow this board's appeal to enthusiasts willing to debug annoying setup and configuration issues on their own.

<p style="text-align: center;">{{< figure src="./orange-pi-plus-front.jpg" alt="Orange Pi Plus - Front" width="500" height="303" class="insert-image" >}}</p>

<p style="text-align: center;">{{< figure src="./orange-pi-plus-back.jpg" alt="Orange Pi Plus - Back" width="500" height="308" class="insert-image" >}}</p>

A few months ago, I bought an [Orange Pi Plus](http://www.aliexpress.com/store/product/NEW-orange-pi-plus-Allwinner-A31s-Dual-Core-1GB-RAM-Open-source-development-board/1553371_32248189300.html) from AliExpress. It's a single-board Linux computer very similar to the Raspberry Pi, with a few key differences:

  - Higher hardware specs at lower price points than the Raspberry Pi
  - An Allwinner H3 processor instead of a Broadcom ARM CPU
  - Features not found on any Raspberry Pi, like SATA, Gigabit Ethernet, IR, and even a built-in mic!

It looks amazing on paper, but my real-world experience with one has been disappointing. Between waiting for the very slow [Orange Pi](http://orangepi.com/) website and forums to load, to spending a few hours just trying to get one of the 'official' Linux distro images to boot correctly, to then debugging hardware issues (like USB keyboard detection, HDMI-to-DVI connections, etc.), there were obstacles every step of the way.

This very blog post was started a few months ago when I received the Pi, but I burned out trying to get everything working then, and I've only now finished the post so others might not spend so much time getting started. That's not high praise for the Orange Pi. It can work, and it does perform respectably, but the end-to-end experience of purchasing and setting up the board leaves a very bitter taste. Many of the issues I encountered with the Orange Pi have long been solved for the Raspberry Pi as a result of the Raspberry Pi Foundation and it's enormous community, and I'm not sure if the Orange Pi or similar boards will ever gain the critical mass of users to match the RPi experience.

## Choosing a Linux distro for the Orange Pi

The Orange Pi website has a [Downloads](http://www.orangepi.org/downloadresources/) section that includes popular Linux distros, even including a version of Raspbian, but after trying to use both the Raspbian v0.8.0 and Debian Server v0.9 images for the Orange Pi Plus (both downloaded from Google Drive), and having no success (like not recognizing my Apple USB keyboard, allowing non-root SSH login, or detecting my Asus HDMI monitor), I searched around and found out about loboris' unofficial Orange Pi images. See forum topic [Linux Distributions for Orange Pi H3 Boards](http://www.orangepi.org/orangepibbsen/forum.php?mod=viewthread&tid=342).

So, after trying a few of the 'official' images and hitting nothing but failure, I finally settled on loboris' images, but using them involves a few extra setup steps to make it work with the Orange Pi Plus (detailed below).

## Setting up the Orange Pi Plus with loboris' Debian Jessie image

  1. Download `OrangePI_Jessie_Xfce.img.xz` from [loboris' Google Drive](https://drive.google.com/folderview?id=0B1hyW7T0dqn6fndnZTRhRm5BaW4zVDVyTGlGMWJES3Z1eXVDQzI5R1lnV21oRHFsWnVwSEU#list) folder.
  2. Expand the .xz file with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html).
  3. Copy the resulting .img file to the microSD card using `dd` technique (directions for Mac OS X):
    1. Figure out which disk is the microSD card: `diskutil list`
    2. Unmount the disk `diskutil unmountDisk /dev/disk2`
    3. Write the image file to the disk: `sudo dd if=path/to/image.img of=/dev/rdisk2 bs=1m` (or with `pv` so you can monitor progress: `pv path/to/image.img | sudo dd of=/dev/rdisk2 bs=1m`)
  4. Following [these directions](http://vosse.blogspot.hr/2015/10/installing-linux-img-files-on-orange-pi.html), I finished the image setup so it had the right kernel settings for the Orange Pi Plus:
    1. Once the card is written (step 3.3 above is complete), open the BOOT volume and do the following:
      1. From the `scriptbin_kernel` archive, select the appropriate `script.bin.OPI-PLUS_` file for your monitor setup (I chose the `script.bin.OPI-PLUS_1080p60_dvi` file since I have an HDMI-to-DVI cable for my LG monitor), rename it to `script.bin`, and place it inside the BOOT volume.
      2. Rename the existing `uImage` to `uImage.bak` and then copy `uImage_OPI-PLUS` from the `scriptbin_kernel` archive, and copy it to the BOOT volume, renamed to `uImage`.
  5. Eject the card, put it in the Orange Pi, and boot it up. Cross your fingers!
  6. Once booted, log in using username `orangepi` and password `orangepi`—if your USB keyboard doesn't work (my Apple USB keyboard didn't), log in via SSH, e.g. `ssh orangepi@[ip-address]`.
  7. Upon first login, resize the filesystem with `sudo fs_resize`.

It seemed every time I found a way to work through one problem, another one presented itself, so at this point, I've given up on trying to get an external keyboard to work with the Orange Pi, and am only using it via SSH. At least I can see it on my monitor now :)

There's no friendly setup utility like `raspi-config`, and very little documentation on other settings that can be changed, so you're on your own for customizations to busses, overclocking, changing boot settings, etc. Whereas almost any little tweak for a Raspberry Pi is documented in someone's blog post, a forum topic, or even in official documentation, there is very little (comparatively) for the Allwinner-based boards, which is one of the main reasons why these boards haven't wiped out the Raspberry Pi, despite their impressive hardware specs.

## Benchmarking the Orange Pi

After running `sudo apt-get update && sudo apt-get upgrade` to get the latest updates, and changing the `orangepi` password using `passwd`, I decided to run a few quick benchmarks, to see how good the hardware was in comparison to the Raspberry Pi models I've tested exhaustively for my [Raspberry Pi Dramble Drupal cluster](http://www.pidramble.com/wiki/benchmarks) project.

### Networking

One of my main annoyances with the Raspberry Pi is it's abysmally slow network I/O capabilities; even if using a USB 3.0 Gigabit Ethernet adapter, the [maximum throughput I could achieve was about 220 Mbps](http://www.jeffgeerling.com/blogs/jeff-geerling/getting-gigabit-networking), which means using a Pi for things like NAS, load balancing, reverse proxying, etc. was far from ideal. On top of that, all networking was done (until the Pi 3) through the single USB 2.0 bus, so any bandwidth used by networking would be stolen from other I/O!

The Orange Pi fares much better, due to it's built-in support for Gigabit Ethernet:

  - 100 MB file download (via 100 Mbps Internet, onboard Gigabit Ethernet): **10.4 MB/s**
  - 100 MB LAN file copy from Pi to Mac (onboard Gigabit Ethernet): **17.66 MB/s**
  - 100 MB LAN file copy from Mac to Pi (onboard Gigabit Ethernet): **17.31 MB/s**
  - `iperf` raw throughput (onboard Gigabit Ethernet): **545 Mbps**

Compare these results to those from [various Raspberry Pi configurations](http://www.pidramble.com/wiki/benchmarks/networking), and the Orange Pi is the winner by a large margin, at least for wired networking. One caveat: All the tests had relatively large margins of error—the `iperf` benchmark was run 10 times, and it ranged from 400 Mbps to 700 Mbps, meaning raw throughput is pretty decent... but not extremely consistent. As a comparison, using a USB 3.0 Gigabit adapter on my MacBook Air (connected to another Air/USB 3 adapter), I averaged 920 Mbps, and the tests ranged from 910 to 940 Mbps—_much_ more consistent speeds.

Unfortunately for those wanting fast I/O and networking, chips like Broadcom's (used in the Raspberry Pi) and Allwinner's (used in the Orange Pi) were originally designed for smartphones, most of which don't worry too much about saturating 1 Gbps networks! They deal with and are optimized for much lower (and more spotty) bandwidth.

### Storage / MicroSD / eMMC Flash

The Orange Pi includes a microSD card slot (like the Raspberry Pi), but also offers 8GB of onboard eMMC storage and an SATA port, so storage has the potential to be much faster on the Orange Pi than a Raspberry Pi!

I did some basic benchmarks, only testing on the internal eMMC and a SanDisk Extreme microSD card, to compare the Orange Pi's I/O performance against the Raspberry Pi (see my [Raspberry Pi microSD Card Benchmarks](http://www.pidramble.com/wiki/benchmarks/microsd-cards)). Here are the results for the microSD card (shows as `/dev/mmcblk0`):

  - `hdparm` buffered: **20.32 MB/s** (18.51 MB/s on RPi)
  - `dd` write: **21.8 MB/s** (18.3 MB/s on RPi)
  - `iozone` 4K random read: **8.30 MB/s** (8.10 MB/s on RPi)
  - `iozone` 4K random write: **2.27 MB/s** (2.30 MB/s on RPi)

For microSD cards, it's pretty much a wash. But that's to be expected. Where things get more interesting is when using the internal eMMC storage (shows as `/dev/mmcblk1`), which promises to be a bit faster:

  - `hdparm` buffered: **58.20 MB/s** (3x faster than microSD)
  - `dd` write: **26.6 MB/s** (similar to microSD)
  - `iozone` 4K random read: **15.26 MB/s** (2x faster than microSD)
  - `iozone` 4K random write: **6.00 MB/s** (3x faster than microSD)

Two caveats for eMMC usage:

  1. You have to [format and mount the Orange Pi Plus's eMMC drive](http://www.jeffgeerling.com/blog/2016/format-built-emmc-storage-on-orange-pi-plus) before you can use it.
  2. It's a bit more difficult than a typical drive to use for things like booting the Orange Pi, so for now, I would recommend just using the onboard storage for faster supplemental storage, as it's simple (and great!) for that purpose, and won't put you in a bind when you try reflashing the Orange Pi or changing boot configurations.

### Drupal 8 (LEMP server)

Drupal is a fairly intense PHP-based CMS that hits CPU and I/O fairly hard when running completely uncached, and I like seeing how different servers handle a simple Drupal site under load. The Raspberry Pi's 4-core ARM CPU and the Allwinner H3 are both fairly slow in comparison to any modern desktop or laptop CPU, but they're quite a bit snappier than the older single-core CPU in older Raspberry Pis! Let's see how the Orange Pi stacks up when serving Drupal requests (using some of the same [Drupal Benchmarks](http://www.pidramble.com/wiki/benchmarks/drupal) I used for the Pi Dramble):

  - Anonymous (cached) requests (Drupal 8.0.5, PHP 7): **110 req/s** (100 req/s on Pi)
  - Authenticated (uncached) requests (Drupal 8.0.5, PHP 7): **19.7 req/s** (8.4 req/s on Pi)
  - Cached requests (Nginx as reverse proxy): **15,908 req/s** (2,220 req/s on Pi)

The Orange Pi's higher CPU frequency and overall system architecture (especially related to network and microSD I/O) give a very good boost to a heavy application like Drupal; so despite it's usage/setup warts, the Orange Pi has excellent performance characteristics, with consistent results that were 2-6x faster than the Pi 2 B even after 5-10 minutes of heavy load.

When I receive the Pi 3 B that I ordered last week, I'll be running these tests against it as well, to see how much of an improvement it provides based on just the CPU architecture improvements. Sadly, networking and general I/O is still the main bottleneck for the Pi 3 in many applications.

## Some other observations

  - On the board, SW4 is a power switch, but it didn't seem to do anything in my use.
  - The official "Raspbian v0.8.0" image didn't recognize my USB keyboard, nor allow non-root SSH login (even after tons of debugging—my USB mouse _did_ work, and root SSH password or key-based login worked fine).
  - The official "Debian Server v0.9" image also had some weird issues (like the non-root SSH login not working).
  - If you use an HDMI-to-DVI cable, make sure you use the right profile in the BOOT volume (as described using loboris' images above).
  - The forums are the only place where useful information can be found at this time. There are a few blog posts on the Orange Pi scattered around, but they're of varying quality and harder to find/digest than the official (and slow-loading) forums.

## Recommendation

I likely spent ten or twelve hours getting the Orange Pi Plus to do all the things I wanted it to do (run some benchmarks, work with a couple external devices, etc.), and I had to give up trying to get my external USB keyboard working with it, so I was never able to evaluate its use as a lightweight desktop replacement.

The performance—especially for I/O and networking—is extremely appealing. For $40, this computer can be made into a very respectable NAS, load balancer, router, or reverse proxy. However, unless the setup process and ongoing support of the Orange Pi developers and community improves dramatically, I don't think the Orange Pi will be a viable alternative to the Raspberry Pi for most people.
