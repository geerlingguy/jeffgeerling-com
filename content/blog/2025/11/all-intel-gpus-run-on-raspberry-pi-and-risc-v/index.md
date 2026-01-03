---
nid: 3510
title: "All Intel GPUs run on Raspberry Pi and RISC-V"
slug: "all-intel-gpus-run-on-raspberry-pi-and-risc-v"
date: 2025-11-13T15:06:28+00:00
drupal:
  nid: 3510
  path: /blog/2025/all-intel-gpus-run-on-raspberry-pi-and-risc-v
  body_format: markdown
  redirects:
    - /blog/2025/all-intel-gpus-run-on-raspberry-pi-now
    - /blog/2025/all-intel-gpus-run-on-raspberry-pi-risc-v
aliases:
  - /blog/2025/all-intel-gpus-run-on-raspberry-pi-now
  - /blog/2025/all-intel-gpus-run-on-raspberry-pi-risc-v
tags:
  - arc
  - egpu
  - gpu
  - intel
  - linux
  - pcie
  - raspberry pi
  - tutorial
  - video
  - xe
  - youtube
---

{{< figure src="./intel-arc-pi-gpu-b580-ai-llama-cpp-llm.jpeg" alt="Intel Arc Pi GPU B580 AI Llama.cpp LLM" width="700" height="394" class="insert-image" >}}

We finally have Intel Arc GPUs working on the Pi _somewhat_ stably—it required overcoming many small hurdles, but it looks like support could land in Raspberry Pi OS if we can get [a simple patch upstreamed](https://lore.kernel.org/lkml/20250715061837.2144388-1-zhangzhijie@bosc.ac.cn/)[^patchnote]. If that happens, all you'd need to do to use an Intel card on a Pi is install a firmware package.

The cards I've spent the most time with so far are:

  - [Intel Arc A750](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/510) ([$249 on Amazon](https://amzn.to/3IeEQKL))
  - [Intel Arc B580](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/695) ([$249 on Amazon](https://amzn.to/4gAKYeK))
  - [Intel Arc B50](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/779) ([$349 on NewEgg](https://www.newegg.com/Intel-Arc-Pro-B50-16GB-Workstation-SFF-Graphics-Card/p/N82E16814883007))
  - [Intel Arc A310 ECO](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/778) ([$109 on Amazon](https://amzn.to/4mWEDgm))

I've also heard good reports on the A350 and A770, though I haven't personally tested those cards. Also, the low end A310 can be especially picky about PCIe link signal integrity, so it pays to use a robust eGPU dock and PCIe adapters/cabling!

{{< figure src="./intel-arc-b310-eco-minisforum-egpu-dock.jpeg" alt="Intel Arc A310 ECO in Minisforum DEG1 Dock for Raspberry Pi" width="700" height="394" class="insert-image" >}}

Since publishing my blog post about how [some eGPU docks are less reliable than others](https://www.jeffgeerling.com/blog/2025/not-all-oculink-egpu-docks-are-created-equal), someone reached out and asked if I had tried an M.2 to OcuLink adapter with a built-in PCI Express ReDriver ([this one](https://amzn.to/48UCnTQ)). This helps with link quality, especially when adapting from full size PCIe to OcuLink to M.2 and ultimately to the Pi's PCIe bus. And... what do you know, that helps! I can now use _all_ my graphics cards with the Minisforum DEG1 dock, which is good—because it's a little more stable holding giant cards like the AMD RX 7900 XT!

As a quick refresher, to _physically_ connect a graphics card to the Pi, you need an eGPU dock, like the [Minisforum DEG1](https://amzn.to/4nHteSa), or this one from JMT. Then you plug that into the Pi using a PCI express adapter, like on the Pi 500 I have this [M.2 to Oculink adapter](https://amzn.to/48ZW10B), with an [Oculink cable](https://amzn.to/3LrAd4a) that goes from there into the dock. Most graphics cards also need a separate power source, so you'll need a [PC power supply](https://amzn.to/3WJzA8B) to power both the dock, and in some cases, the card too.

But what follows is all the steps needed to make a Pi 5/500/CM5 running Pi OS Trixie work with any current Intel graphics card (for AMD, it's even easier, but I'll talk about that later ;). After that, I'll highlight quirks with each of the Intel cards I've been testing.

And if you don't like reading (then why are you on this blog?), here's a video covering Intel cards on the Pi:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/ewDJpxQEGo4" frameborder='0' allowfullscreen></iframe></div>
</div>

## A quick word on cost and value

Since I know some people may be interested in how the value of a Pi setup with an Intel Arc GPU compares to buying a desktop PC and adding in a graphics card, here are the base numbers for my setup you can play with:

| Part | Price |
| :-- | :-- |
| [Raspberry Pi CM5 8GB](https://www.pishop.us/product/raspberry-pi-compute-module-5-8gb-ram-lite-cm5008000/) | $85 |
| [CM5 IO Board (includes M.2 slot)](https://www.pishop.us/product/raspberry-pi-compute-module-5-io-board-rev-2/) | $25 |
| [JMT M.2 M-key eGPU dock](https://amzn.to/490b7TP) | $86 |
| [Thermaltake 500W Power Supply](https://amzn.to/3Jppoz8) | $40 |
| [Intel Arc B50 16GB GPU](https://www.newegg.com/Intel-Arc-Pro-B50-16GB-Workstation-SFF-Graphics-Card/p/N82E16814883007) | $350 |

**TOTAL**: $586

Note the B50 is currently out of stock everywhere as of this writing (it seems to have hit a value sweet spot for Intel...), but the B580 is about the same price and faster, though requires more power, and has less VRAM. Also, you might need to buy a USB-C power adapter, and microSD card... in other words, the value and what you'd need vary depending on what things you may already have on hand.

But you could also buy a minitower PC (especially used) and get similar performance, with slightly worse total power draw, but with **fully-supported drivers**. So no, I don't recommend you build a Pi eGPU setup unless you have a very specific need, or want to learn and play with GPUs on small Arm systems.

## Configuring the Pi Kernel (without recompiling!)

Make sure you're on a fresh Pi OS Trixie install, updated to the latest packages (run `sudo apt upgrade -y` and reboot).

  1. Install 6by9's custom Pi kernel from the Raspberry Pi Linux repository: `sudo rpi-update pulls/7113`
  1. This PR is configured for the `bcm2711_defconfig` (technically meant for Pi 4), so edit `/boot/firmware/config.txt` and add the following to the bottom:

        kernel=kernel8.img  # to use bcm2711 config from PR 7072
        dtparam=pciex1_gen=3  # for faster PCIe Gen 3 speeds
        auto_initramfs=0  # to avoid 'weird boot mechanisms or file systems'

  1. Older Intel cards might not be identified by the Xe driver automatically, so tell it to force probe all connected cards by adding the following in `/boot/firmware/cmdline.txt`:

        xe.force_probe=*

  1. Reboot: `sudo reboot`

At this point, you need to install the firmware for the card you're using.

## Installing non-free firmware

Ideally, all the current firmware is in one of three packages (installed with `sudo apt install -y [package name]`:

  - `firmware-intel-graphics` for Intel
  - `firmware-amd-graphics` for AMD
  - `firmware-misc-nonfree` for Nvidia

After installing that, reboot. If the card is still not outputting anything, it may be too new for the firmware included in the system package. Check for this with `dmesg`.

For example, with my B580, I got the messages:

```
[    5.063645] xe 0001:03:00.0: [drm] GT1: Using GuC firmware from xe/bmg_guc_70.bin version 70.36.0
[    5.063657] xe 0001:03:00.0: [drm] GuC firmware (70.45.2) is recommended, but only (70.36.0) was found in xe/bmg_guc_70.bin
[    5.063667] xe 0001:03:00.0: [drm] Consider updating your linux-firmware pkg or downloading from https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
[    5.067926] xe 0001:03:00.0: [drm] GT1: Using HuC firmware from xe/bmg_huc.bin version 8.2.10
```

And I could manually download the newer firmware file with:

```
cd /usr/lib/firmware/xe && \
sudo wget -O bmg_guc_70.bin -q https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/xe/bmg_guc_70.bin
```

Then reboot.

> For Alchemist-series cards (e.g. A380, A750, etc.), you might need to download the firmware files into `/usr/lib/firmware/i915`.

## Getting a working desktop environment

With my B580, I noticed the desktop environment (`labwc-pi`) was still not starting automatically. I was stuck in the 'blinking cursor' mode, and had to press Alt+F2 to get to the console.

To get the desktop environment working, I also needed to [manually compile Mesa](https://gist.github.com/geerlingguy/fbdc2c52fcf8ba3b87f04323f3dc517c), because the one baked into Pi OS
_currently_ doesn't include `iris` support (Iris is the Gallium and Vulkan driver name for Intel Arc in Mesa...).

## Enabling Resizeable BAR

If you look deeper into the logs, you'll also see an entry like:

```
[    4.742322] xe 0001:03:00.0: [drm] Failed to resize BAR2 to 16384M (-ENOSPC). Consider enabling 'Resizable BAR' support in your BIOS
```

This means the Xe driver _tried_ resizing the Pi's BAR (Base Address Register) allocation for the GPU, but failed. This _should_ work, but currently doesn't, at least not for the Intel GPU drivers; see [Resizable BAR support on Pi 5](https://github.com/raspberrypi/linux/issues/6621).

To fix that, you can manually resize the BAR on your Pi, prior to the Xe driver initialization.

I wrote a guide for that here: [Resizeable BAR support on the Raspberry Pi](https://www.jeffgeerling.com/blog/2025/resizeable-bar-support-on-raspberry-pi)

## Intel card quirks

{{< figure src="./intel-arc-pi-gpu-artifacts-desktop.jpeg" alt="Intel Arc Pi GPU artifacts on desktop" width="700" height="394" class="insert-image" >}}

Each of the Intel cards I've tested has a quirk or two worth mentioning:

  - [**Intel Arc A750**](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/510): The A750 has some rendering artifacts, generally at the top of drawn objects, like windows, menubars, and pictures displayed in the web browser. Sometimes textures on a 3D object don't load when using Vulkan, but OpenGL seems to render just fine, with full 3D acceleration.
  - [**Intel Arc B580**](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/695): Similar to the A750, there are artifacts, but it seemed to be slightly less prevalent. The memory seemed fine for smaller AI model acceleration, but I could not get a stable run with larger models that took up more than 4 or 5 GB of VRAM.
  - [**Intel Arc B50**](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/779): Similar to the B580, larger AI models would not run correctly, and would start repeating themselves at a certain point. It was a bit slower than even the A750 for pure GPU-accelerated tasks, but with the smaller footprint, quiet fan, and low power requirements, it may be suitable for workstations, SFF builds, or more energy-efficient setups.
  - [**Intel Arc A310 ECO**](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/778): This card was difficult to get recognized on the PCIe bus; I had to purchase an M.2 to Oculink adapter with a built-in ReDriver, to boost the PCIe link signal, otherwise it would try negotiating a link and fail after a couple minutes, no matter what eGPU dock I tried. It's very slow, but also fits in a 1-slot half-height footprint. It doesn't have enough VRAM to do much, but it is only around $100, so if you just want a little GPU accelerator, you could do worse.

## Intel card performance

I've been benchmarking _all_ my GPUs on the Pi in [this issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/764) on my Pi PCI Express database website, but I wanted to highlight the GravityMark benchmark in particular. GravityMark is almost entirely GPU-bound, so it's a good way of seeing the relative performance between each of these cards.

{{< figure src="./intel-arc-pi-gravitymark-benchmark.jpg" alt="Intel Arc GPU GravityMark Benchmarks on Raspberry Pi" width="700" height="394" class="insert-image" >}}

And the Intel cards, well, they're not going to take home any crowns, especially since Nvidia doesn't even show up on this list yet. But they're not slouches, either, especially considering the price.

I also ran AI models on them, and at least for smaller models, they performed decent, too. The B50 Pro, in particular, has enough RAM and sips power better than other cards, so it _might_ be a viable option for an efficient, small LLM machine.

But those quirks I mentioned earlier seem to impact 3D rendering and AI, especially when more memory is involved. So while the performance is decent, until we get the memory issues sorted, working with these cards on a Pi is more for the fun of it.

## Where do we go next?

Right now [the PR for AMD and Intel graphics card support](https://github.com/raspberrypi/linux/pull/7113) works great—and I also maintain [a separate PR](https://github.com/geerlingguy/linux/pull/10) with just the 23 line patch currently required.

But before these changes will make it into Raspberry Pi Linux, we need to break them down and get them into upstream Linux—which is possible! I'm currently talking to a few other people in the Pi community to see how we want to move forward.

The Intel changes in particular affect not only Arm but RISC-V as well. Therefore some members of the RISC-V community have been working on a patch in parallel, and it's already been submitted to the mailing list. In fact, my first ever [LKML reply](https://lore.kernel.org/lkml/C67D4EC2-649C-4E46-A55D-8B48A31E8928@jeffgeerling.com/) is on that patch series!

The main thing is making sure any changes we make are architecturally sound, and work well for _all_ non-x86 systems, not just the Pi.

So stay tuned, and make sure you follow any of the issues you're interested in over on my [Raspberry Pi PCIe project](https://pipci.jeffgeerling.com) website!

[^patchnote]: The patch enables Intel Arc cards on _all non-x86 systems_, not just Arm. So RISC-V users would benefit as well. If merged into the Linux kernel, Raspberry Pi will likely backport the patch into their current OS version; so there are a couple steps involved in making this happen!
