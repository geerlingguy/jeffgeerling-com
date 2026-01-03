---
nid: 3281
title: "I built a special PCIe card to test GPUs on the Pi"
slug: "i-built-special-pcie-card-test-gpus-on-pi"
date: 2023-04-13T15:00:04+00:00
drupal:
  nid: 3281
  path: /blog/2023/i-built-special-pcie-card-test-gpus-on-pi
  body_format: markdown
  redirects:
    - /blog/2023/we-built-special-pcie-card-test-gpus-on-pi
aliases:
  - /blog/2023/we-built-special-pcie-card-test-gpus-on-pi
tags:
  - cm4
  - compute module
  - mirkopc
  - open source
  - pcie
  - pi4gpu
  - raspberry pi
---

I partnered up with Mirek (of Mirkotronics / [@Mirko_DIY](https://twitter.com/Mirko_DIY) on Twitter) to build the Pi4GPU (or 'PiG' for short):

{{< figure src="./pi4gpu-pig-pci-express-raspberry-pi-card.jpeg" alt="Pi4GPU or PiG card - PCI Express Raspberry Pi CM4 card for GPU testing" width="700" height="467" class="insert-image" >}}

This journey started almost three years ago: almost immediately after the Raspberry Pi Compute Module 4 was launched, I started testing graphics cards on it.

First I tried some low-spec cards like the [Zotac Nvidia GT 710](https://pipci.jeffgeerling.com/cards_gpu/zotac-geforce-gt710-1gb.html) and the [VisionTek AMD Radeon 5450](https://pipci.jeffgeerling.com/cards_gpu/visiontek-radeon-5450-1gb.html). They kept locking up regardless of the driver and Linux versions.

{{< figure src="./DSC01164.jpeg" alt="Pi4GPU with AMD Radeon HD 7450 Graphics Card" width="700" height="467" class="insert-image" >}}

Over the next couple years, I kept testing more and more cards—over 14 at the time of this writing. The reason? Each card (really, each _generation_ of each vendor's cards) had quirks that made it more or less likely to run on the Pi.

Why's that? Well, the Pi has problems with cache coherency on the PCI Express bus beyond 32-bits. And many (well, _all_ nowadays) of the drivers expect that to function. That wasn't the first problem, though—early on, there were issues with the BAR (Base Address Register) space allocated on the Pi's OS. Luckily [this could be worked around by re-compiling a DTB file](https://gist.github.com/geerlingguy/9d78ea34cab8e18d71ee5954417429df).

This whole endeavor is what inspired me to create the [Raspberry Pi PCIe Device Database](https://pipci.jeffgeerling.com), which documents (often in _excruciating_ detail) the travails bringing up various PCI Express devices on a Raspberry Pi—and now, on other ARM SBCs like the Radxa Rock 5 and the Pine64 SOQuartz.

## Making a Custom PCB

Last year I floated the idea of a custom PCB to 'plug a computer into a graphics card' to Mirek. He didn't immediately say 'no', so I started pursuing the idea, coming up with this quite basic post-it note illustration:

{{< figure src="./post-it-note-jeff-design.jpg" alt="Post it note with illustration of Pi4GPU from Jeff Geerling" width="600" height="475" class="insert-image" >}}

Miraculously, through a series of emails, we refined that concept into a working PCB design. Mirek had it printed by JLCPCB, [soldered on a bunch of SMD components](https://twitter.com/Mirko_DIY/status/1610366805859524608), and shipped the PCBs (along with some metal brackets he had his friend Adam fabricate) by February.

In the midst of that journey, I [had another major surgery](https://www.jeffgeerling.com/blog/2022/part-of-the-wrong-1-perecent-ostomy-surgery-part-2), and wound up working on a so-far-still-secret-project that soaked up the entire month of March 2023.

{{< figure src="./3d-printed-base-pcie-pi4gpu-with-card-installed.jpeg" alt="3D printed base with Pi4GPU installed" width="700" height="467" class="insert-image" >}}

So here we are today: between spare hours in March and a few weeks' time finally testing this thing with all the cards this month, I've uncovered one or two minor quirks with the build, designed a 3D-printed base (pictured above) that supports up to a 4090-sized behemoth PCIe card (pictured below), and documented everything in our [open source Pi4GPU repository](https://github.com/geerlingguy/pi4gpu).

{{< figure src="./4090-pi4gpu-raspberry-pi.jpeg" alt="Pi4GPU running an Nvidia RTX 4090 Graphics Card - Gigabyte" width="700" height="467" class="insert-image" >}}

The card has a standard standard PCIe x4 (physical) edge connector, and it plugs into a special PCIe-to-PCIe adapter board, which fits neatly into the recessed part of a 3D printed base.

The graphics card slots into the x16 (physical, only x1 pins are connected) slot on the adapter board, and if needed, you use an external power supply to power beefier GPUs.

The Pi4GPU board itself can be powered via USB-C or 6-pin PCIe (internal edge), or via 12v barrel plug (external edge). It also has 2 USB 2.0 ports, a full-size HDMI port, and a 1 Gbps LAN port (all through the rear PCIe bracket):

{{< figure src="./DSC01145.jpeg" alt="Port side of Pi4GPU PCI Express Raspberry Pi CM4 card" width="700" height="467" class="insert-image" >}}

It can physically slot inside a computer in a motherboard, but that is _not_ recommended, as I haven't tested that configuration...

## External GPUs on a Raspberry Pi (or other Arm SBCs)

So we have this card, and I can plug it into a variety of graphics cards... do any of them work? Or for avid readers of this blog—has anything changed since [last year's update](/blog/2022/external-graphics-cards-work-on-raspberry-pi)?

Well... it's still a bit grim. So far we only have some older AMD cards working with a [kernel patch](https://github.com/geerlingguy/linux/pull/6) for the `radeon` graphics driver, and the SM750 GPU which is used on ASRock Rack's M2_VGA, using [this patch](https://github.com/geerlingguy/linux/pull/2) to the `sm750` driver.

In some positive news, though, Nvidia's proprietary driver no longer hard-locks-up when it hits the memory errors on the Pi. Now it will attempt to load, but then error out. That _would_ make debugging easier... if the driver source were fully open and available.

Unfortunately, it's not.

And on AMD's side (as well as other vendors for _other_ PCI Express cards, like Google's Coral TPU), there's no desire to either maintain a fork of their drivers or spend time hacking their driver to work on the buggy PCIe bus on the Pi.

And the Pi isn't alone—it seems other SBC SoCs like the Rockchip RK3566 and RK3588 have a slightly broken PCIe implementation as well. 'Cache coherency' is the problem—these ARM SoCs that have their heritage in TV boxes and embedded devices don't have fully working PCI Express implementations.

Other ARM chips _do_, however, like this Ampere Altra Development Platform that just arrived courtesy of Ampere:

{{< figure src="./ampere-altra-developer-platform-hero-shot.jpg" alt="Ampere Altra Developer Platform" width="700" height="394" class="insert-image" >}}

It has a fully functional PCI Express implementation, and also has _128 lanes_ of PCI Express Gen 4... which is about a zillion times more bandwidth than the _single_ PCIe Gen 2 lane on the Pi and similar-era SoCs.

Check out my initial review of the Ampere system: [Testing a 96-core Ampere Altra Developer Platform](/blog/2023/testing-96-core-ampere-altra-developer-platform).

Apple's M-series chips might have even more bandwidth (per lane), but there's no easy way to get at the PCI Express expansion on them. Maybe the upcoming Mac Pro will make it happen, but I'm not holding my breath.

## Video

Check out my video with even more detail about the project:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/l9dItRUjQ0k" frameborder="0" allowfullscreen=""></iframe></div>
</div>
