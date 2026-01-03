---
nid: 3376
title: "microSD cards' SBC days are numbered"
slug: "microsd-cards-sbc-days-are-numbered"
date: 2024-05-15T02:46:16+00:00
drupal:
  nid: 3376
  path: /blog/2024/microsd-cards-sbc-days-are-numbered
  body_format: markdown
  redirects: []
tags:
  - m2
  - nvme
  - raspberry pi
  - sbc
  - ssd
  - video
  - youtube
---

{{< figure src="./raspberry-pi-m2-hat-plus.png" alt="Raspberry Pi M.2 HAT+" width="500" height="auto" class="insert-image" >}}

For years, SBCs that aren't Raspberry Pis experimented with eMMC and M.2 storage interfaces. While the Raspberry Pi went from full-size SD card in the first generation to microSD in every generation following (Compute Modules excluded), other vendors like Radxa, Orange Pi, Banana Pi, etc. have been all over the place.

Still, _most_ of the time a fallback microSD card slot remains.

But microSD cards—even the fastest UHS-II/A2/V90/etc. ones that advertise hundreds of MB/sec—are laggards when it comes to any kind of SBC workflow.

The two main reasons they're used are cost and size. They're tiny, and they don't cost much, especially if you don't shell out for industrial-rated microSD cards.

{{< figure src="./microsd-card-slot.jpeg" alt="microSD card slot on Raspberry Pi" width="500" height="auto" class="insert-image" >}}

They're so small, in fact, that it can be hard to pick one up off a desk. In many cases, a small tweezers are required to extract them once inserted. My GoPro's slot is so poorly placed I've damaged both my fingernail and a microSD card trying to use the infernal push-push mechanism in the tiny battery compartment.

With SBCs, the _rest_ of the world (outside Raspberry Pi) settled on either a space for an eMMC module, built-in eMMC, or an M.2 M-key slot for primary storage. Almost all the main boards have them either on top or bottom.

But the Pi—even the latest Pi 5 variant—stubbornly avoided this, opting for external USB storage for those wanting more speed or reliability.

Today, Raspberry Pi introduced a first-party [M.2 HAT+](https://www.raspberrypi.com/news/m-2-hat-on-sale-now-for-12/). They've even [released the schematics](https://datasheets.raspberrypi.com/m2-hat-plus/raspberry-pi-m2-hat-plus-schematics.pdf), so people can build off their reference design more easily.

In fact, there are already [dozens of other NVMe and M.2 HATs](https://pipci.jeffgeerling.com/hats) for the Pi 5, but it's nice to have a [more finalized HAT+ specification](https://datasheets.raspberrypi.com/hat/hat-plus-specification.pdf) vendors can work from. Some creative adaptations include Radxa's use of their existing [Penta SATA HAT](/blog/2024/radxas-sata-hat-makes-compact-pi-5-nas) for the Pi 5 with a special PCIe adapter cable.

{{< figure src="./pineberry-pi-dual-nvme-board.jpeg" alt="Pineboards dual NVMe HAT" width="700" height="auto" class="insert-image" >}}

But back to the topic of this post: despite what many commenters on my YouTube videos think, Raspberry Pi still holds the lion's share of the entire SBC market. As goes Raspberry Pi, so goes the rest of the SBC market.

And their new M.2 HAT (along with the inclusion of PCIe accessible to the end user) signals what I think will be a transition to faster primary storage. Maybe a revision to the Pi 400 will include an internal M.2 slot?

I remember when desktop computers transitioned from primarily spinning hard drives for boot volumes to SSDs. It was a life-changing difference, as random access was especially fast on solid state storage. The immense performance gains all but ended the hard disk's reign as the _de facto_ standard for desktop PC storage.

Hard drives still have a ton of utility—I have a bunch in my NAS, and they're great for value, beating out most other storage media for cost per TB.

Similarly, microSD cards are great for recording and transferring files like photos and videos for mobile devices—whether phones, drones, or small cameras.

But I know for me, except in cases where I use a Pi in a more 'embedded' style use case (which is honestly better suited for microcontrollers like the ESP32 or Pico these days), I've deployed Pi 5s with a cheap 128 or 256 GB $25 NVMe SSD and a $12 HAT, giving a nice, well-supported Linux device sipping 4-5W of power for $100 or so. The NVMe drives are generally 10-100x faster than microSD (especially at IOPS/random access), though they cost about 2x per GB, and use about 1W vs 0.1W at idle—YMMV.

Sure, mini PCs in the $150-200 range are faster, and in many cases better for desktop use. But a Pi is great, too (especially if you do need to add on some embedded integration using GPIO or cameras or displays). Now that the shortages are over, Pi's are also available, which is nice :D

I'm especially excited Raspberry Pi finally has [NVMe boot behind a PCIe switch working](https://github.com/raspberrypi/firmware/issues/1833). Even though current multi-drive HATs take a hit on PCIe speeds, they add to the Pi's potential utility, especially with HAT's like Pineboards' [HatDrive! AI Coral bundle](https://pineboards.io/products/hatdrive-ai-coral-edge-tpu-bundle-nvme-2230-2242-gen-2-for-raspberry-pi-5), which matches up a Coral TPU (included) with an NVMe slot, for a tidy little 5W setup for something like Frigate with object detection.

I made a video where I did some more testing of the Pi M.2 HAT+ and other HATs, which you can watch below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/GYN3ub8Qb_I" frameborder='0' allowfullscreen></iframe></div>
</div>
