---
nid: 3330
title: "External GPUs working on the Raspberry Pi 5"
slug: "external-gpus-working-on-raspberry-pi-5"
date: 2023-11-29T03:13:59+00:00
drupal:
  nid: 3330
  path: /blog/2023/external-gpus-working-on-raspberry-pi-5
  body_format: markdown
  redirects:
    - /blog/2023/you-can-use-external-gpus-on-raspberry-pi-5
aliases:
  - /blog/2023/you-can-use-external-gpus-on-raspberry-pi-5
tags:
  - amd
  - gpu
  - linux
  - open source
  - pcie
  - pi 5
  - raspberry pi
---

My journey testing various graphics cards on the Raspberry Pi began soon after the Compute Module 4 was launched in 2020. Since then I've [tested](https://pipci.jeffgeerling.com/#gpus-graphics-cards) almost 20 graphics cards—with a [_little_](/blog/2023/i-built-special-pcie-card-test-gpus-on-pi) success.

But there were two roadblocks to getting drivers for even older AMD `radeon` drivers working well:

  1. The maximum PCIe Gen 2.0 bandwidth meant use cases were limited to 'processing on GPU' tasks like GPU-assisted compute. Even in the base case, external cards couldn't necessarily pipe through data quick enough for modest gaming or other real-time tasks.
  2. (And most impactful) The BCM2711 SoC used on the CM4 and Pi 4 had some strange PCI Express bus quirks that caused hard crashes and various faults in drivers attempting to use 64-bit memory addresses. There were strange and exotic workarounds—but these workarounds led to even _more_ limited performance!

{{< figure src="./pi-5-gpu-amd.jpg" alt="Raspberry Pi 5 with AMD XFX RX 460 graphics card" width="700" height="auto" class="insert-image" >}}

The Pi 5, fortunately, seems to have fixed the PCIe bus quirks with its new BCM2712 SoC, and the new chip also introduces unofficial support for PCIe Gen 3.0 speeds (8 GT/sec versus the CM4's 5).

External GPU bringup on the Pi 5 was much faster since we now know many of the driver quirks are due to old code assuming an X86 architecture.

In the video below, I demonstrate the Pi 5 displaying Wayfire through an AMD RX 460, and running at least _much_ of the `glmark2` test:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/BLg-1w2QayU" frameborder='0' allowfullscreen></iframe></div>
</div>

As [chronicled in the RX 460 testing GitHub issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/564) (and related [issue #6](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/6), user Coreforge got a `glmark2` score of `3441` over PCIe Gen 1 speeds, had Steam launching (but sometimes crashing) using [`box86`](https://box86.org) and [`box64`](https://github.com/ptitSeb/box64), ran Portal and Portal 2 with no issues (outside of Steam), and Minecraft 1.14.4 ran but at a reduced framerate due to the lower-speed PCIe Gen 1 connection.

When I have more time (right now I'm in the middle of moving all my gear to a new space...), I will join in more testing, but hopefully [Pineberry Pi](https://pineberrypi.com) can get a PCIe adapter like their prototype uPCity I'm using to market, so more people can test and squash the remaining memory alignment bugs for older cards like the RX 460.

I have also been [testing my RX 6700 XT](https://pipci.jeffgeerling.com/cards_gpu/amd-radeon-rx6700xt-12gb.html), which also uses the `amdgpu` Linux driver, but with some newer extensions. I have gotten through a few roadblocks but am currently [stuck](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/222#issuecomment-1817395974) at the part where the driver attempts initializing Display Core.

Honestly, I'm approaching 'infantile' stages of familiarity with graphics drivers, but I know enough to mess up the driver (a lot) and quite rarely get something working on my own. I hope that with the Pi 5's better PCIe bus (and Gen 3.0 speeds, even if unofficial), more people can work on squashing `arm64` vs `x86`-related memory access bugs in various drivers.

The best thing is on the Pi 5, I've so far _never_ encountered any bugs where the entire system crashes (to the point the kernel can't recover). On the Compute Module 4, I had to hard pull power and re-apply it to get back into a working state! Debugging is immeasurably if you can get an error message or exception, and the entire system doesn't explode every time you test it :)

Many other PCIe cards 'just work' out of the box on the Pi 5, and as always—you can follow _my_ progress testing various devices over on the [Raspberry Pi PCIe database](https://pipci.jeffgeerling.com).
