---
nid: 3041
title: "Raspberry Pi USB Boot - UASP, TRIM, and performance"
slug: "raspberry-pi-usb-boot-uasp-trim-and-performance"
date: 2020-09-17T14:35:12+00:00
drupal:
  nid: 3041
  path: /blog/2020/raspberry-pi-usb-boot-uasp-trim-and-performance
  body_format: markdown
  redirects:
    - /blog/2020/raspberry-pi-usb-ssds-uasp-trim-and-boot-performance
    - /blog/2020/raspberry-pi-usb-boot-uasp-trim-and-boot-performance
aliases:
  - /blog/2020/raspberry-pi-usb-ssds-uasp-trim-and-boot-performance
  - /blog/2020/raspberry-pi-usb-boot-uasp-trim-and-boot-performance
tags:
  - performance
  - raspberry pi
  - ssd
  - trim
  - uasp
  - usb
  - video
  - youtube
---

In the past few weeks, I reviewed [USB drive performance on the Raspberry Pi 4](/blog/2020/fastest-usb-storage-options-raspberry-pi), and the [importance of UASP support](/blog/2020/uasp-makes-raspberry-pi-4-disk-io-50-faster) for USB drive performance.

Both posts generated great discussion, and there were three things I wanted to cover in this follow-up, namely:

  1. Which drives support UASP
  2. Real-world performance benchmarks
  3. TRIM support

For reference, here are all the products I'm testing in this post (product links are to their Amazon product page, starting from top middle, clockwise):

{{< figure src="./usb-performance-devices-tested.jpg" alt="USB Performance testing - SATA SSD, NVMe, and Flash drives" width="600" height="398" class="insert-image" >}}

  - [Inatech enclosure](https://amzn.to/2Zqan5S) with [Kingston 120GB SSD](https://amzn.to/32iltvB)
  - [TDBT M.2 enclosure](https://amzn.to/3ihOkFW) with [XPG SX6000 128GB NVMe](https://amzn.to/2RdFhd1)
  - [Corsair Flash Voyager GTX 128GB](https://amzn.to/2RbqcJ2)
  - [Arcanite 128GB USB 3.1 flash drive](https://amzn.to/32jDuJT)
  - [SanDisk Ultra Flair 16GB USB 3.0 flash drive](https://amzn.to/2DLRNgK)
  - [SanDisk Ultra Fit 128GB USB 3.0 flash drive](https://amzn.to/2Fljg9P)
  - [Samsung Evo+ 32GB microSD](https://amzn.to/32fmRz1) (not pictured - in Raspberry Pi)

## Video Version

There is also a video version of this blog post: [view video on YouTube](https://www.youtube.com/watch?v=oufXAysaywk).

## UASP support

First, in the last post, I completely forgot to discuss which of the USB drives I tested supported UASP, and which ones didn't.

For a refresher, UASP lets the Raspberry Pi communicate with the drive using the SCSI protocol, which is up to twice as fast for file copies and disk performance as the older 'USB mass storage' protocol.

You can check if your own drive supports UASP with the command `lsusb -t`. If the output shows 'uas', it supports it out of the box. If it shows 'usb-storage', it doesn't.

So here's a quick graph showing which drives support UASP.

| UASP | Device |
| ---: | --- |
| ✅ | Inatech enclosure with Kingston 120GB SSD |
| ✅ | TDBT M.2 enclosure with XPG SX6000 128GB NVMe |
| ✅ | Corsair Flash Voyager GTX 128GB |
| ❌ | Arcanite 128GB USB 3.1 flash drive |
| ❌ | SanDisk Ultra Flair 16GB USB 3.0 flash drive |
| ❌ | SanDisk Ultra Fit 128GB USB 3.0 flash drive |
| ❌ | Samsung Evo+ 32GB microSD |

It looks like all the fastest drives I benchmarked support it, while all the slowest ones don't. No huge surprise there; the faster drives use better chipsets that are built for SSD performance.

The Arcanite is an outlier, though. It doesn't support UASP, but it does perform very well for its price. And it sometimes behaves a little like an SSD—I'll talk about that in a bit.

## Performance

For the second thing I wanted to cover, I was prompted by none other than Gordon Hollingworth, the Director of Engineering at Raspberry Pi, in his Twitter post. He said:

<blockquote class="twitter-tweet" data-conversation="none"><p lang="en" dir="ltr">What would be really interesting is how the different SD card, usb flash and nvme storage compare in terms of booting time and time to start a web page from the command line...</p>&mdash; Gordon Hollingworth (@gsholling) <a href="https://twitter.com/gsholling/status/1291648954854146050?ref_src=twsrc%5Etfw">August 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

First, I'll test boot time performance.

### Boot Performance

The most important thing when measuring boot time is to find a way to compare different devices using an objective measure. That is, you don't want to sit around with a stopwatch and try to time 'from plug-in to desktop appearing' boot times. That could be helpful sometimes, but it's not very objective.

Instead, I use a built-in tool in Raspberry Pi OS, called `systemd-analyze`. It's a tool that helps you analyze the system manager, and by default, if you just run that command, it will output the boot time. How easy is that?!

So I did that, three times for each drive, and averaged the results:

{{< figure src="./graph-usb-boot-performance.png" alt="USB boot performance for Raspberry Pi 4" width="672" height="378" class="insert-image" >}}

All the drives performed pretty well, though the non-UASP drives did tend to be slower, with the strange exception of the SanDisk Ultra Flair, which punched above its weight class. The slowest by far was the SanDisk Ultra Fit, which I mentioned in the previous post has a tendency to overheat and slow way down.

But there are two important caveats to these boot time numbers:

First, I booted with the August 2020 version of Rasbperry Pi OS, and followed the [directions in this blog post](/blog/2020/im-booting-my-raspberry-pi-4-usb-ssd) to configure the USB drive to be able to boot the Pi.

Second, it seems like the Pi already optimized its boot performance really well. The first boot was always a bit slower, but subsequent boots took around 15-17 seconds, on all the USB drives I tested.

The biggest difference was that first boot was much faster on the faster SSDs and NVMe drive, and a bit slower on the cheap flash drives and the microSD card.

### Browser launch time

The other thing Gordon mentioned in his tweet was testing the web browser launch time from the command line.

It actually took a bit of doing, figuring out a way to launch Chromium from the command line, load a web page, and then quit it, and get an accurate time measurement of the process. Just using `chromium-browser [URL here]` didn't cut it, because that launched the browser, and the process wouldn't exit until I manually quit the browser.

After [asking on Twitter](https://twitter.com/geerlingguy/status/1303779579228717057) about what others might do, I found a neat Node.js utility called ['puppeteer'](https://github.com/puppeteer/puppeteer/), which I could use to do it all automatically, and then I used the `time` utility in Linux to benchmark the process three times for each drive. I described how I did this benchmark in detail in this post: [Testing how long it takes Chromium to open, load a web page, and quit on Debian](/blog/2020/testing-how-long-it-takes-chromium-open-load-web-page-and-quit-on-debian).

Here are the results:

{{< figure src="./usb-web-browser-performance.png" alt="USB drive web browser performance for Raspberry Pi 4" width="672" height="378" class="insert-image" >}}

The difference really isn't that big. Definitely not as big as I thought it would be. The faster drives still open Chromium a tiny bit faster—especially on first launch—but only a tiny bit!

I tested all of these Pis over a VNC connection, with the resolution set in `raspi-config` to 1280x720. And just like the boot times, the first launch of the browser after a reboot would take a bit longer than the 2nd, 3rd, 4th, or 5th launches.

I think this just means the caching mechanisms in Linux are good at normalizing performance for even very slow boot volumes, as long as you have enough system memory.

Once booted for the second time and after quitting and restarting Chrome, the difference in common UI tasks between the slowest drive and the NVMe drive was almost imperceptible.

There are some things, especially when you're doing upgrades, installing software, writing files, or working on large projects (like Drupal websites I maintain) where the difference is more apparent.

To test that, I installed `php7.3-cli` on each of the drives, and checked how long that took:

{{< figure src="./usb-php-install-performance.png" alt="USB drive PHP installation performance on Raspberry Pi 4" width="672" height="378" class="insert-image" >}}

And... as with the other performance tests, this one is not the most consistent. I ran it a couple times on some of the drives, re-flashing the entire drive between runs, and the standard deviation—the variance between runs—was usually around 20%, so take these results with a grain of salt.

Generally speaking, the faster drives _did_ do better, but it was hard to get exact numbers when benchmarking real-world workloads.

## TRIM support

So finally, in a Hacker News thread, user Legogris [asked about TRIM](https://news.ycombinator.com/item?id=24075035), saying:

> Are you aware if the GTX and Arcanite support TRIM? That definitely makes a difference when considering OS storage.

And why would Legogris be interested in TRIM support? Well, the short answer is with SSDs, when little bits of data are deleted, and new data needs to be written to where those old deleted bits were, the drive can slow down and also do more work than it should have to.

{{< figure src="./win95-defragment.gif" alt="Defragmenting a Windows 95 Hard Drive" width="480" height="360" class="insert-image" >}}

This is a really simple answer, but basically think of it like 'automatic defragmentation' for an SSD. I don't know if you've ever had the honor of sitting in front of an old Windows computer watching it defragment your 80 MB IDE drive for hours on end, but it's kind of like that, at warp speed. TRIM doesn't do defragmentation, technically, but it's similar in that it lets your SSD perform its best through some automatic cleanup processes.

The hard thing is, you have to have TRIM support in both your operating system—in our case, Raspberry Pi OS (which does support TRIM)—and in the drive controller's firmware.

There are a few ways to check for TRIM support, like running the `fstrim` command:

    sudo fstrim -v /

If it says `the discard operation is not supported`, then TRIM isn't currently working for your drive.

You can also run the `lsblk` command:

    lsblk -D

If the `DISC-MAX` value is `0B`, then, again, TRIM isn't currently working for your drive.

Many adapters will work with TRIM after you follow a special process to change their 'provisioning mode'.

I have a separate blog post with details on how to enable TRIM support if your firmware supports it but it's not enabled by default: [Enabling TRIM on an external SSD on a Raspberry Pi](/blog/2020/enabling-trim-on-external-ssd-on-raspberry-pi).

Some drive controllers may also need a firmware update to enable TRIM support, so check on your drive manufacturer's website.

Here are the results for all the drives I tested:

| Device | TRIM OOTB | TRIM support in Firmware |
| --- | --- |
| Inatech enclosure with Kingston 120GB SSD | ❌ | ❌ |
| TDBT M.2 enclosure with XPG SX6000 128GB NVMe | ❌ | ✅ |
| Corsair Flash Voyager GTX 128GB | ❌ | ✅ |
| Arcanite 128GB USB 3.1 flash drive | ❌ | ⁉️ |
| SanDisk Ultra Flair 16GB USB 3.0 flash drive | ❌ | ❌ |
| SanDisk Ultra Fit 128GB USB 3.0 flash drive | ❌ | ❌ |
| Samsung Evo+ 32GB microSD | ✅ | ✅ |

Surprisingly, the Inatech enclosure didn't seem to have any TRIM support, while the TDBT NVMe enclosure and the Corsair did.

Also, and this is something I never thought about—the Raspberry Pi actually supports TRIM out of the box for internal microSD cards!

But the most _alarming_ result is that the Arcanite firmware indicated TRIM support, but when I followed the process to change the provisioning mode and ran `fstrim`, the drive failed spectacularly, and now I can't even mount or initialize the thing on any computer!

So... the Arcanite firmware may be from an SSD, but the flash memory itself seemed to not take well to the `fstrim` command. Either that, or I had one defective unit!

## Summary

In the end, I found there are a lot of different traits, positive and negative, on all the drives I tested. If you just need a drive to store large files, I still think the Arcanite is the best overall value, even though it doesn't support UASP, and it kind of explodes if you try enabling TRIM.

And if you're after raw performance, an NVMe inside an enclosure is going to give the best bang for your buck, as well as—at least in the case of the TDBT enclosure I tested—full TRIM and UASP support.

In the end, if you have any USB 3.0 drive, outside of cheap flash drives, it's probably going to perform as well as or better than a microSD card in a Raspberry Pi 4.
