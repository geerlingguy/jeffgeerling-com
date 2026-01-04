---
nid: 3091
title: "Three more graphics cards on the Raspberry Pi CM4"
slug: "three-more-graphics-cards-on-raspberry-pi-cm4"
date: 2021-04-23T14:17:39+00:00
drupal:
  nid: 3091
  path: /blog/2021/three-more-graphics-cards-on-raspberry-pi-cm4
  body_format: markdown
  redirects: []
tags:
  - amd
  - asrock rack
  - cm4
  - compute module
  - gpu
  - graphics
  - m2
  - nvidia
  - pi os
  - raspberry pi
  - vga
  - video
  - youtube
aliases:
  - /comment/16889
---

Last year I tested two older graphics cards—a [Radeon 5450](https://pipci.jeffgeerling.com/cards_gpu/visiontek-radeon-5450-1gb.html) and a [GeForce GT710](https://pipci.jeffgeerling.com/cards_gpu/zotac-geforce-gt710-1gb.html)—on a Raspberry Pi Compute Module 4.

{{< figure src="./jeff-holding-graphics-cards-raspberry-pi-cm4.jpeg" alt="Jeff Geerling holds NVidia and ASRock Rack GPU and Raspberry Pi Compute Module 4 with quizzical look" width="600" height="400" class="insert-image" >}}

This year, I've been testing three more graphics cards—a [GeForce GTX 750 Ti](https://pipci.jeffgeerling.com/cards_gpu/evga-geforce-gtx-750ti.html), a [Radeon RX 550](https://pipci.jeffgeerling.com/cards_gpu/sapphire-radeon-rx550-2gb.html), and the diminutive [ASRock Rack M2_VGA](https://pipci.jeffgeerling.com/cards_gpu/asrock-rack-m2-vga.html).

The Compute Module 4, if you didn't know already, exposes the BCM2711's single PCI express lane, and the official IO Board has a nice, standard, 1x PCIe slot into which you can plug any PCI express device.

## Video version of this post

I also published a YouTube video on this topic, with even more detail: [Will ANY GPUs work on the Raspberry Pi?](https://www.youtube.com/watch?v=MxcafwjWw24).

## Difficulties with PCIe on the Pi

But physical connection is one thing—getting a card to work on the Pi is a different problem, and it is compounded because:

  - Until the CM4, no Pi exposed a PCI express interface (the Pi 4 model B internally uses the bus for a VL805 USB 3.0 chip). So Pi OS and other distributions easy to run on the Pi have never really optimized their PCI express support, or even included standard drivers for things you'd plug into a typical PC.
  - Until late last year, the default BAR (Base Address Register) allocation on the Pi was _256 MB_, and many cards require much more than this. The default allocation [was raised to 1 GB](https://github.com/raspberrypi/linux/commit/52ded9e4f07b7b608344c5bbef59e31f7b39cb79) in newer Pi OS kernels, and you can even raise it further (to 4 or 8 GB) following [these instructions](https://gist.github.com/geerlingguy/9d78ea34cab8e18d71ee5954417429df).
  - The PCI express interface on the BCM2711 system on a chip was never optimized for general purpose 'desktop' use, and there are some quirks in its implementation (one of which was [patched around](https://github.com/raspberrypi/linux/issues/4158) to [get a MegaRAID card working for SAS RAID storage on the Pi](/blog/2021/hardware-raid-on-raspberry-pi-cm4)).
  - Features like MSI-X were not originally supported and [now are](https://www.raspberrypi.org/forums/viewtopic.php?t=293248#p1772216)... mostly—and some PCI express cards rely on these features and expect them to behave a certain way in their driver.
  - The Raspberry Pi uses an ARM processor. Many drivers are written for and tested on X86 but not ARM. Luckily, this is changing a bit over time, as ARM is slowly entering data center usage, and is finally gaining a foothold on end-user workstations.
  - The CM4 IO Board is powered through either a 4-pin floppy connector or a 12v barrel plug. If you don't supply enough juice, PCI express cards can exhibit weird behavior. I spend a _ton_ of time testing various scenarios and making sure the power supply was not the issue when I am testing cards.

I've tested a large variety of PCI express cards, and have been compiling the results of my testing on my [Raspberry Pi PCI Express device compatibility database](https://pipci.jeffgeerling.com).

Some cards, like USB 3.0 controllers and NVMe drives, 'just work,' while others require a driver download and install (like Intel's AX200 WiFi 6 chip), or a kernel recompile (like Rosewill's 2.5 Gigabit NIC).

## GPUs in Linux

Graphics cards on Linux have traditionally had... interesting levels of support, even on the most widely-used hardware.

For example, Nvidia supplies proprietary closed-source drivers for most of their modern cards, but loading them taints the kernel and if you have a problem, there's no real way to fix it short of begging Nvidia to deliver a new driver. Because of this, an open source, but inferior (performance-wise) reverse-engineered 'nouveau' driver exists in the Linux kernel source tree.

AMD actually submits its driver code straight into the Linux kernel source, so it can be inspected and patched if need be.

So against that backdrop, there are many challenges to overcome if one wants to get a graphics card working (for any purpose, whether gaming, AI/ML, mining, or just to add another display) on a Raspberry Pi.

But I like a good challenge, so I keep plunging forward:

## Nvidia GeForce GTX 750 Ti

{{< figure src="./evga-geforce-gtx-750-ti.jpeg" alt="EVGA Geforce GTX 750 Ti graphics card" width="600" height="401" class="insert-image" >}}

Like with the GT710, I tried installing the [proprietary Nvidia ARM 64-bit driver](https://www.nvidia.com/en-us/drivers/unix/linux-aarch64-archive/). Doing so requires the installation of the `raspberrypi-kernel-headers` on the 64-bit Pi OS beta. The driver installed, but upon restart, when X server started up, the Nvidia driver errored out with `Internal error: Oops: 96000005 [#1] PREEMPT SMP`.

Since the driver is closed-source, I had no hope of debugging it, so I switched to [recompiling the kernel](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile) with the `nouveau` driver.

After doing so, and rebooting the Pi, it would lock up in the middle of initialization—and not a gentle lockup, a full hard lockup that required power cycling the Pi to get it to reboot.

I tried debugging the lockup over a serial connection, but was not getting very far, so I shelved the card and moved on.

## AMD Radeon RX 550

{{< figure src="./sapphire-radeon-rx-550.jpeg" alt="Sapphire Radeon RX 550 graphics card" width="600" height="389" class="insert-image" >}}

The Radeon RX 550 uses the `amdgpu` driver in the kernel source, so debugging it is a lot easier than with the proprietary Nvidia driver. I recompiled the kernel with that driver, rebooted the Pi and... lockup, just like every other card I've tested.

In this case, it locked up seemingly at the same point each time, so I dropped some debug `printk()`s in the source in various places, eventually narrowing down the problem to something inside `amdgpu_ring_init()`. I patched an errant call to `memset()` with some help from GitHub user elFarto, but eventually after a ton more debugging I kind of petered out on the card and shelved it too.

## ASRock Rack M2_VGA

{{< figure src="./asrock_rack_m2_vga.jpeg" alt="ASRock Rack M2_VGA graphics card for M.2 PCIe" width="600" height="401" class="insert-image" >}}

Around that time, I recieved ASRock Rack's M2_VGA in the mail. I had emailed them after seeing it mentioned in a forum post about low-power graphics cards, and they graciously sent me one for testing.

It's an M.2 graphics card that sips 2W of power, supports one VGA port (though the SM750 GPU supports multiple displays and even video inputs!), and is almost as tiny as the Compute Module itself!

How did it fare on the Pi? Well, I recompiled the kernel with the built-in `sm750fb` driver (which happens to be in the staging drivers still, after five years in the kernel source), and the Pi locked up when it tried starting the X window server. Just like all the other cards.

I was digging around in the SM750 driver source, found there was a fork that seems to have been started to 'get it into shape' and migrate it to the `drm` subsystem, and tried that, but to no avail. That fork was actually more out of date than the in-tree fb driver, probably because the in-tree one, despite being hardly maintained, was at least updated to compile with the rest of the Linux kernel.

Maybe Phoronix's article [Silicon Motion Has Open-Source Driver, But Fails](https://www.phoronix.com/scan.php?page=news_item&px=MTA2OTk) was prescient. I tried reaching out to a few of the people who were listed as maintainers for the driver, but didn't get anywhere.

## A reason for hope

After five fails (well, a couple were more "I give up after hours of testing"), all hope is not lost, though! GitHub user Coreforge [is testing with a Radeon 6450](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4#issuecomment-751307934), and was able to get a blinking cursor to be output through the card (albeit in a very noisy image):

{{< figure src="./cursor-blinking-screen-coreforge.jpg" alt="Coreforge cursor blinking on screen Radeon 6450" width="700" height="395" class="insert-image" >}}

This means that it _is_ likely possible to get a graphics card working with the Pi CM4... but it's going to take a bit of driver debugging to get there.

## Conclusion

I'm definitely getting out of my element in terms of driver work. Hopefully someone can make a breakthrough and figure out what's holding back all these drivers. Likely memory access issues or maybe even some yet-uncovered bug with how PCIe addressing works on the Pi's BCM2711 SoC.

Check out the companion video that goes into more depth: [Will ANY GPUs work on the Raspberry Pi?](https://www.youtube.com/watch?v=MxcafwjWw24).

Also check out the [Pi PCI Express card database site](https://pipci.jeffgeerling.com) for more details on my experience with each of the cards, along with links to the full discussion on GitHub.
