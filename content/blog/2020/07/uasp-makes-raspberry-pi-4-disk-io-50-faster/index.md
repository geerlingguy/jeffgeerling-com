---
nid: 3025
title: "UASP makes Raspberry Pi 4 disk IO 50% faster"
slug: "uasp-makes-raspberry-pi-4-disk-io-50-faster"
date: 2020-07-03T16:36:04+00:00
drupal:
  nid: 3025
  path: /blog/2020/uasp-makes-raspberry-pi-4-disk-io-50-faster
  body_format: markdown
  redirects: []
tags:
  - benchmarks
  - inateck
  - performance
  - ssd
  - uasp
  - usb
---

> You can view a video related to this blog post here: [Does UASP make the Raspberry Pi faster?](https://www.youtube.com/watch?v=t0kYcM1E5fY).

A couple weeks ago, I [did some testing](/blog/2020/im-booting-my-raspberry-pi-4-usb-ssd) with my Raspberry Pi 4 and external USB SSD drives. I found a USB 3.0 SSD was ten times faster than the fastest microSD card I tested.

In the comments on the video associated with that post, [Brad Manske](https://www.youtube.com/watch?v=B1aRGkH3bgw&lc=Ugyub9T7QYjgC3WgLEh4AaABAg) mentioned something I never even thought about. He noticed that I had linked to an [Inateck USB  3.0 SATA case](https://www.amazon.com/gp/product/B00DW374W4/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=0f464952d9710ca38c33ca2433062a4f&language=en_US) that didn't have UASP.

What's UASP, you might ask?

Without UASP, a drive is mounted as a Mass Storage Device using Bulk Only Transport (or BOT), a protocol that was designed for transferring files way back in the USB 'Full speed' days, when the fastest speed you could get was a whopping 12 Mbps!

With USB 3.0, the BOT protocol cripples throughput. USB 3.0 has 5 Gbps of bandwidth, which is _400x more_ than USB 1.1. The old BOT protocol would transfer data in large chunks, and each chunk of data had to be delivered in order, without regard for buffering or multiple bits of data being able to transfer in parallel.

So a new protocol was created, called 'USB Attached SCSI Protocol', or 'UASP'.

I won't get too technical here, but the [SCSI protocol](https://en.wikipedia.org/wiki/SCSI) has been around for a very long time—long enough that [it was part of a joke in this 1994 Dilbert comic](https://dilbert.com/strip/1994-05-26). It has features like allowing parallel bits of data to be copied and out of order data transfer so the drive can use buffering and caching mechanisms for better performance.

Around the time USB 3.0 was introduced, most USB storage devices and adapters for hard drives started adopting the standard. And some computers with only USB 2.0 ports could have their firmware updated to use UASP for newer drives, so some USB 2.0 connections got a speed boost.

## What does this have to do with the Pi?

Let's not get too far ahead of ourselves. Going back to Brad's comment on my Pi SSD video, I replied to Brad that I didn't even realize I had the non-UASP version of the Inateck case.

So I ordered the [UASP version](https://www.amazon.com/dp/B00FCLG65U/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=1ba205ee2d7b9d0f6b53c76989ff85c9&language=en_US), and waited for it to arrive.

{{< figure src="./inateck-usb-sata-case-top.jpeg" alt="Inateck USB 3.0 SATA case - top side" width="600" height="338" class="insert-image" >}}

And when it did arrive, I tried to see what was different about it. The top, sides, and back are completely identical.

{{< figure src="./inateck-usb-sata-case-bottom-uasp.jpeg" alt="Inateck USB 3.0 SATA case with and without UASP - bottom side" width="600" height="338" class="insert-image" >}}

On the bottom, the only difference is one additional letter in the model number.

{{< figure src="./uasp-ssd-sata-usb-inateck-circuit-boards.jpeg" alt="Inateck USB 3.0 SSD SATA adapter circuit boards - UASP" width="600" height="338" class="insert-image" >}}

The differences are only really apparent if you take the thing apart and look at the actual circuit board. The older non-UASP version is on the top left in the picture above, and the UASP version on the bottom right. The UASP version has a completely different layout, and uses a different controller chip.

If you have a USB drive and don't want to take it apart and look up the specs of the controller chip, the only reliable way to tell if it's being mounted with UASP support or not is to plug it into your Pi, then run the command `lsusb -t`:

```
$ lsusb -t
/:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M
    |__ Port 1: Dev 2, If 0, Class=Mass Storage, Driver=uas, 5000M
```

This command lists all the USB devices in a tree, and for each of the hard drives, you should see a `Driver` listed. If it's `uas` (like in the above example), then your drive supports UASP and you'll get the best speed. If it's `usb-storage`, then it's using the older BOT protocol and you won't see the full potential.

I also had two other old SATA adapters that I've used over the years when doing computer repairs, when I would clone an old hard drive to a new one, or try to recover data from a hard drive in a broken computer.

I checked this [inland adapter](https://www.microcenter.com/product/485230/inland-usb-30-sata-hard-drive-adapter) I bought from Micro Center, and it also supports UASP, which was a surprise since the specs on Micro Center's website showed the data transfer rate as "Up to 480Mbps", ha!

Then I checked this [StarTech SATA adapter](https://www.amazon.com/StarTech-com-SATA-USB-Cable-USB3S2SAT3CB/dp/B00HJZJI84/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=82a41645218c9db04cf8fded0ef9e87a&language=en_US) I bought in 2015 and it also supports UASP. So it looks like most newer USB 3.0 adapters _do_ support it, but it's not always easy to see in the specs on Amazon or other retailers' websites.

> Update: I also bought a cheap [Sabrent](https://www.amazon.com/gp/product/B011M8YACM/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=13600d94b94d1769b129ffe9fb3a41a0&language=en_US) adapter when it was on sale last week, and it also works with UASP on my Pi 4.

### What about the Pi 3 B+ and older Pis?

Even though Raspberry Pis older than the Pi 4 only have USB 2.0 ports, I wanted to check if they might support UASP, because as we'll see in a minute, just having UASP versus the older BOT protocol makes a large difference in performance, which would help even on older USB 2.0 ports.

Alas, after testing with all my adapters, I found they all mounted the drive using the `usb-storage` driver. I was trying to find any official confirmation as to whether the Pi 3 B+ firmware could support UASP, but all I could find was a reference in [this Pi Forum post](https://www.raspberrypi.org/forums/viewtopic.php?t=236357#p1445475) to the Pi's `dwc_otg` driver not having support for a feature the UAS driver requires.

So if you have an older Raspberry Pi, your options for fast external storage are very limited. I'd stick with the Pi 4 if you want to do anything that requires data transfer like building a NAS, setting up Nextcloud, using it for backups, or media streaming.

## Benchmarks with and without UASP

These benchmarks show just how big a difference UASP makes when you use it with a drive on a Raspberry Pi 4.

{{< figure src="./benchmark-uasp.png" alt="Raspberry Pi 4 USB 3.0 UASP performance difference" width="600" height="294" class="insert-image" >}}

Across the board, UASP makes a huge difference. At the top there are benchmarks for hdparm and dd tests, which test large file transfers. These show 50% and 40% speedups, respectively.

At the bottom there are 4K random access benchmarks, which are a better measure of how the drive will perform doing typical computing tasks. And UASP still makes a big impact. Random reads are 35% faster, and random writes are 20% faster.

But I wanted to check something else, too. With more efficient data transfer possible, would there be any measurable difference in how much power is required?

For many Raspberry Pi projects, efficient power usage is an important consideration, especially if you're running the Pi off a battery or solar energy.

{{< figure src="./benchmark-power-consumption.png" alt="UASP power consumption benchmark on Pi 4" width="600" height="176" class="insert-image" >}}

I used a [Satechi USB-C power tester](https://www.amazon.com/gp/product/B01MT8MC3N/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=f122bbbbcbc6c985b9632c67b00d42b2&language=en_US) and measured an 8% peak power savings using UASP. That means you'd get 8% more runtime on a battery if you do a lot of file transfers.

As with all my benchmarks, I ran every benchmark four times, discarding the first result. I talked a lot about my benchmarking process in [my previous Raspberry Pi Cluster video](https://www.youtube.com/watch?v=IoMxpndlDWI).

You can also see all the raw data and my methodology in [this benchmarking issue on the turing-pi-cluster repository](https://github.com/geerlingguy/turing-pi-cluster/issues/11). If you run the same benchmarks, you may get slightly different results if you use a different SSD or enclosure.

## Summary

My advice is always use UASP with USB 3.0 devices on the Pi 4, otherwise you're missing out on a pretty substantial performance gain. Also, remember to plug USB 3.0 devices into the blue USB 3.0 ports, not into the black USB 2.0 ports, otherwise you won't see any of the performance difference.
