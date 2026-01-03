---
nid: 3378
title: "LattePanda Mu crams x86 PC into SoM form factor"
slug: "lattepanda-mu-crams-x86-pc-som-form-factor"
date: 2024-05-24T14:00:46+00:00
drupal:
  nid: 3378
  path: /blog/2024/lattepanda-mu-crams-x86-pc-som-form-factor
  body_format: markdown
  redirects: []
tags:
  - compute module
  - lattepanda
  - linux
  - mu
  - raspberry pi
  - sbc
  - video
  - youtube
---

{{< figure src="./lattepanda-mu-raspberry-pi-5.jpeg" alt="LattePanda Mu with Raspberry Pi 5 in background" width="700" height="auto" class="insert-image" >}}

LattePanda's been building Intel-based SBCs for almost a decade, but until now, they've never attempted to unite an Intel x86 chip with the popular SoM-style form factor Raspberry Pi's dominated with their Compute Module boards.

This year they've introduced the [LattePanda Mu](https://www.lattepanda.com/lattepanda-mu), a SoM that marries an Intel N100 SoC with a new edge connector standard they've designed, using a DDR4 SODIMM form factor.

Right now they offer two carrier boards: a [lite version](https://www.dfrobot.com/product-2822.html) with basic interfaces and a couple 2230-size M.2 slots for SSDs and wireless, and a [full evaluation carrier](https://www.dfrobot.com/product-2821.html) that breaks out _every_ hardware interface in a Mini ITX-sized motherboard.

The module itself costs $139, and comes with an N100, 8GB of LPDDR5 RAM, and 64GB of eMMC storage. The Lite carrier board is $39, and the full Mini ITX board is $89. There's a $189 [kit](https://www.dfrobot.com/product-2844.html) available with all you need to get started—and that's the version I received for review.

{{< figure src="./lattepanda-carrier-lite-mu.jpeg" alt="LattePanda Mu Carrier Board Lite with full kit and heatsink fan" width="700" height="auto" class="insert-image" >}}

The fan heatsink allows the N100 to boost to full 35W mode, giving maximum performance (the fan is spinning and audible at all times), and there's a fanless heatsink that allows the N100 to perform at the lower 6W TDP for lighter usage.

My kit had Windows 11 Home pre-installed (unlicensed), and I was able to install Ubuntu 24.04 directly to the eMMC using a USB flash drive.

I had a little trouble getting the on-board M.2 2230 M-key slot to work with any of my NVMe SSDs, and after asking LattePanda about this, it sounds like they shipped the board with slightly-incomplete firmware—a fact also mentioned on their [Dev Status](http://docs.lattepanda.com/content/mu_edition/dev_status/) page:

> But sorry, the firmware engineers couldn't keep up with the hardware engineers. Some of the features that have hardware pins reserved for them don't have firmware adaptations yet, and they don't work at the moment.

Luckily, a firmware update _should_ fix the NVMe SSD support in the M-key slot, but there are a few other interfaces yet to be implemented.

I compared the Mu to a Raspberry Pi 5 and Radxa Rock 5C in my latest video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/GKGtRrElu30" frameborder='0' allowfullscreen></iframe></div>
</div>

You can watch that video for more, but if you want the raw performance numbers that led to my conclusions, read through the [LattePanda Mu issue](https://github.com/geerlingguy/sbc-reviews/issues/42) in my `sbc-reviews` repo.

My basic conclusion: The Mu certainly performs well. And efficiency is nearly the same as the Pi 5 (with more than double the performance on tap). It's not as efficient as the best Arm chips, like the Rockchip RK3588S2, but it's a welcome change from Intel's tradition of burning watts in favor of higher clocks.

{{< figure src="./lattepanda-mu-turing-rk1-radxa-cm5.jpg" alt="LattePanda Mu Turing RK1 and Radxa CM5 SoMs" width="700" height="auto" class="insert-image" >}}

But LattePanda Mu has an uphill battle—the SoM form factor of the Compute Module 4 (and upcoming CM5) has been widely adopted in the Arm ecosystem, and there are hundreds if not _thousands_ of carrier boards in production using that form factor.

The Turing RK1 (pictured above, top right) has a similar problem, as it's chosen the Nvidia Jetson Nano edge connector pinout, but at least there is an ecosystem of Jetson boards that could be used with the RK1. The Mu needs developers to adopt the standard for the Mu to become a compelling CM. Until then, it's slightly cheaper to buy an N100-based tiny PC if you just need a compact Intel PC for Windows or Linux.

It is exciting to see someone take a stab at another edge form factor, especially with an efficient x86 chip, and I'm happy to see LattePanda [releasing the BIOS, drivers, and schematics in the open](https://github.com/LattePandaTeam/LattePanda-Mu).

If someone were to build a carrier board for 4-6 of these, with an external 10 Gbps network connection and NVMe slots under each board, it would make a fairly robust edge clusterboard!

And being Intel/x86, PCIe support for things like graphics cards is much simpler than on Arm. ETA PRIME [installed an RTX 3050](https://youtu.be/z3XHWwfqXJg?t=567) and it worked right away, boosting gaming performance and opening up the possibility of easy GPU AI/compute acceleration.
