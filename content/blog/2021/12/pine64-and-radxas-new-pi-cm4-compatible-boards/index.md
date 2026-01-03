---
nid: 3158
title: "Pine64 and Radxa's new Pi CM4-compatible boards"
slug: "pine64-and-radxas-new-pi-cm4-compatible-boards"
date: 2021-12-15T15:00:41+00:00
drupal:
  nid: 3158
  path: /blog/2021/pine64-and-radxas-new-pi-cm4-compatible-boards
  body_format: markdown
  redirects:
    - /blog/2021/these-rockchip-pi-cm4-compatible-replacements-cant-replace-pi—yet
    - /blog/2021/these-rockchip-pi-cm4-compatible-replacements-wont-replace-pi—yet
    - /blog/2021/rockchip-cm4-compatible-replacements-wont-replace-pi—yet
    - /blog/2021/pine64-radxa-cm4-compatible-boards-wont-replace-pi—yet
    - /blog/2021/pine64-and-radxas-new-raspberry-pi-cm4-compatible-boards
    - /blog/2021/pine64-and-radxa-have-new-pi-cm4-compatible-boards
aliases:
  - /blog/2021/these-rockchip-pi-cm4-compatible-replacements-cant-replace-pi—yet
  - /blog/2021/these-rockchip-pi-cm4-compatible-replacements-wont-replace-pi—yet
  - /blog/2021/rockchip-cm4-compatible-replacements-wont-replace-pi—yet
  - /blog/2021/pine64-radxa-cm4-compatible-boards-wont-replace-pi—yet
  - /blog/2021/pine64-and-radxas-new-raspberry-pi-cm4-compatible-boards
  - /blog/2021/pine64-and-radxa-have-new-pi-cm4-compatible-boards
tags:
  - cm3
  - cm4
  - compute module
  - pine64
  - radxa
  - rockchip
  - sbc
  - soquartz
  - video
  - youtube
---

Since the Raspberry Pi was introduced, hundreds of clones have adopted the Pi's form factor (from the diminutive Zero to the 'full size' model B). Often they have better hardware specs, and yet they remain a more obscure also-ran in that generation of Single Board Computer (SBC).

{{< figure src="./pine64-soquartz-radxa-cm3.jpg" alt="Pine64 SOQuartz and Radxa CM3 in front of Raspberry Pi Compute Module 4" width="700" height="316" class="insert-image" >}}

So when I saw [Radxa's CM3](https://www.cnx-software.com/2021/11/07/radxa-cm3-raspberry-pi-cm4-alternative/) and [Pine64's SOQuartz](https://www.pine64.org/2021/10/29/october-update-follow-up/), I wanted to see if either would be—as they advertised—'drop in, pin-compatible replacements' for the Raspberry Pi Compute Module 4.

> **tl;dr**: They're not. At least not yet.

## Hardware and Specs

Both boards _are_ technically pin-compatible. And both will boot and run (to some extent) on pre-existing Compute Module 4 carrier boards, including Raspberry Pi's official IO Board:

{{< figure src="./pine64-soquartz-on-cm4-io-board.jpeg" alt="Pine64 SOQuartz on Raspberry Pi Compute Module 4 IO Board" width="600" height="329" class="insert-image" >}}

Because the boards are pin-compatible, you can use them on almost every pre-existing carrier board designed for the CM4—I'm tracking [almost 100 on my Pi PCIe site](https://pipci.jeffgeerling.com/boards_cm)!

That's great, because while many of the CM4 _carrier boards_ are available, the CM4 itself is _not_. It's nearly impossible to snag the model you want, and for most flavors there won't be any in stock for _months_!

And just because the boards are Pi clones, they don't have to stick to all the limitations of the CM4's layout—the Radxa CM3 sports a third IO board-to-board connector along the top edge that's not present on the CM4 or SOQuartz:

{{< figure src="./radxa-cm3-bottom-3rd-connector.jpeg" alt="Radxa CM3 3rd connector on bottom for IO" width="600" height="400" class="insert-image" >}}

This connector breaks out two SATA ports (split between the PCIe bus and USB 3.0 port), an extra USB 3.0 port, and extra GPIO pins above and beyond what the Pi offers. _But_ it requires a board that supports the third connector, and none that are available do, yet ([Radxa's own](https://wiki.radxa.com/Rock3/CM3/radxacm3io) is still not available for testing or purchase).

The RK3566 (used by both the CM3 and the SOQuartz) also includes ARMv8 crypto extensions, and a 0.8 TOPS AI accelerator, so there are some other hardware niceties on offer, even though the 4x Cortex A55 cores are slightly slower (even at a higher clock) than the A72 cores in the CM4.

But if you just want to drool over specs, go read them at the source:

  - [Radxa CM3](https://wiki.radxa.com/Rock3/CM3)
  - [Pine64 SOQuartz](https://wiki.pine64.org/wiki/SOQuartz)

## The Promise

After months of [testing dozens of PCI Express devices](https://pipci.jeffgeerling.com) with the Compute Module 4—which exposes the BCM2711 PCIe Gen 2.0 x1 lane directly—I've encountered issues with some drivers, notably any GPU / graphics card, some storage controllers, and the Coral TPU.

The Pi's chip doesn't have a fully-baked PCIe bus. It's perfectly adequate for USB 3.0 chips (like the VL805 used in the Pi 4 model B and Pi 400), most NVMe SSDs, and a number of other devices, but the Pi locks up in strange ways when you try something crazy like [plugging in an AMD Radeon RX 6700 XT](https://www.youtube.com/watch?v=LO7Ip9VbOLY).

{{< figure src="./Rockchip-RK3566-SoC.jpeg" alt="Rockchip RK3566 SoC on Pine64 SOQuartz" width="600" height="386" class="insert-image" >}}

So I am hoping the Rockchip RK3566 used in these other boards _might_ have a better PCIe implementation. Good enough to be able to load drivers for more devices without hacky patches to work around the PCIe bus limitations on the Pi.

And supposedly the bootloader and firmware surrounding Rockchip-based boards is more open than that on the Raspberry Pi. This isn't a huge issue for _most_ users, but it is a thorn in the otherwise stellar reputation Raspberry Pi has for working with open source hardware and software.

## The Problem

But here's the problem: as I've encountered with nearly every non-Pi clone in the past, the hardware and specs are great, but the software, documentation, and community fall short.

I had a lot of trouble getting both boards to a state where I could start using them (e.g. with Debian or Ubuntu running and accessible over SSH, at least), and I detailed my journey in this video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/aXlcNVKK-7Q" frameborder='0' allowfullscreen></iframe></div>
</div>

But having to spend hours just trying to get the boards to boot—for someone who isn't completely new to the world of single-board computers—highlights the lack of polish on the software and documentation side.

The Pi, despite its warts, has two things going for it: a company that devotes a lot of time to testing, documentation, and bug fixes, and an active and broad community—one that isn't comprised _mostly_ of devoted 'hacker' types who know the meaning of u-boot, buildroot, and UART!

And I'm not alone in my misery—earlier this month [there was a post on CNX Software](https://www.cnx-software.com/2021/12/02/tribulations-with-linux-on-zidoo-m6-rockchip-rk3566-mini-pc/) about issues getting Linux working on a mini PC with the same RK3566 chip.

Even though many of these boards use the exact same chip, OS images still have to be built custom for every board. So you're relying on each board vendor—Pine64, Radxa, or whomever else—to maintain up to date and working Linux builds.

And sure, there's [Armbian](https://www.armbian.com) and custom distro maintainers out there, but those often require even more technical knowledge, and aren't 'officially' supported by vendors.

Pine64 at least states the software for the SOQuartz is in early development... but even when it _is_ ready, will the documentation, community, and support be up to par with the Pi? I'm doubtful (but ever-hopeful, even after years of disappointment).

I think for either of these Compute Module replacements, Radxa and Pine64 need to devote time and resources to polishing their software and documentation, especially targeting the first-time out-of-the-box experience.

## Conclusion

{{< figure src="./cm4-cm3-soquartz.jpeg" alt="Raspberry Pi Compute Module 4, Radxa CM3, and Pine64 SOQuartz SBCs" width="660" height="438" class="insert-image" >}}

In the end, I see a lot of potential. Having three compatible products available for the breadth of Compute Module 4 carrier boards should provide a lot of relief for those who want to power some new IoT or edge project with a tiny ARM board, but the CM4 alternatives just aren't there yet.

I hope they will be—and I'm still struggling forward with both the CM3 and SOQuartz; you can follow my progress in these GitHub issues:

  - [Test Radxa CM3 on CM4 Boards](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/327)
  - [Test Pine64 SOQuartz on CM4 boards](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/336)
