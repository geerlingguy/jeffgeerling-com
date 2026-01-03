---
nid: 3205
title: "External graphics cards work on the Raspberry Pi"
slug: "external-graphics-cards-work-on-raspberry-pi"
date: 2022-04-27T14:02:36+00:00
drupal:
  nid: 3205
  path: /blog/2022/external-graphics-cards-work-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - amd
  - arm64
  - drivers
  - gpu
  - graphics
  - linux
  - nvidia
  - radeon
  - raspberry pi
---

{{< figure src="./amd-radeon-gpu-with-raspberry-pi-compute-module-4.jpeg" alt="AMD Radeon HD 7450 Graphics card with Raspberry Pi Compute Module 4" width="700" height="467" class="insert-image" >}}

In October 2020, after Raspberry Pi introduced the Compute Module 4, I started out on a journey to [get an external graphics card working on the Pi](/blog/2020/external-gpus-and-raspberry-pi-compute-module-4).

At the time, it'd been over a decade since the last time I'd built a PC, and I had a lot to learn about PCI Express, the state of graphics card drivers in Linux, and PCI Express support on various ARM SoCs.

After failing to get the Nvidia GT710 or AMD 5450 running, I started testing the [GTX 750 Ti, RX 550, and SM750](/blog/2021/three-more-graphics-cards-on-raspberry-pi-cm4), all with wildly different architectures and driver support. After failing to get those cards working, I [tested a newer GTX 1080](/blog/2021/tried-nvidias-gtx-1080-still-no-external-gpu-on-pi), and even splurged on an [AMD Radeon RX 6700 XT on the Pi](https://www.youtube.com/watch?v=LO7Ip9VbOLY)—which also didn't work.

Along the way, dozens of people (from AMD engineers, to ARM enthusiasts, to fellow hobbyists like me) helped explore the dark, dusty corners of the BCM2711—Broadcom's ARM SoC that powers the Raspberry Pi Compute Module 4.

What we found is the BCM2711's PCIe root complex is fundamentally broken, at least when it comes to some memory operations on 64-bit Linux. Some speculated the brokenness couldn't be worked around, but as Winston Churchill once said:

> Success is stumbling from failure to failure with no loss of enthusiasm.

[This issue in particular](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4), with over 490 comments as of this writing, documents dozens of failures in one central location, to the point where they could be categorized and [worked around in a set of patches](https://github.com/Coreforge/linux/pull/1) to the open source `radeon` driver.

## Video for this Blog post

I've also made the video embedded below, to help illustrate the journey, and to show more about how the graphics cards are—and aren't—working on the Pi:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/crnEygp4C6g" frameborder='0' allowfullscreen></iframe></div>
</div>

## How to get an AMD GPU working

{{< figure src="./memcpy-functions-patch-linux.jpeg" alt="memcpy function patch in Linux" width="700" height="467" class="insert-image" >}}

Before you get started, you'll need to have on hand:

  1. Raspberry Pi Compute Module 4 (hard to find currently, check [rpilocator](https://rpilocator.com) for stock).
  2. Raspberry Pi Compute Module 4 IO Board (or another IO board with a PCI Express slot).
  3. [PCIe x1 to x16 riser/adapter](https://amzn.to/3LmfNVc) (if the IO board you have only has a x1 slot).
  4. An AMD Radeon graphics card in the 5000/6000/7000 line (We've confirmed at least the 5450, 6450, and 7470 work).

### Prepare the OS

The current working patch is based off the previous 5.10.y Linux fork Raspberry Pi maintained, so you need to flash a copy of Raspberry Pi OS from earlier this year (not the latest). I downloaded `2022-01-28-raspios-bullseye-arm64-full.zip` from [here](http://downloads.raspberrypi.org/raspios_full_arm64/images/raspios_full_arm64-2022-01-28/) and expanded it, then used Raspberry Pi Imager to flash it to a microSD card.

I put that card in my Raspberry Pi, and installed AMD's firmware with `sudo apt install -y firmware-amd-graphics`.

Then I went to my main workstation and cross-compiled the Raspberry Pi kernel. The exact environment and process I follow is thoroughly documented here: [Raspberry Pi Linux Cross-compilation Environment](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile). That setup _should_ work on any Mac or Linux workstation. I haven't tested it on Windows.

> Why cross-compile? Well, a fresh compilation takes between 6-10 minutes on my main workstation. On a Compute Module 4, the process takes almost an _hour_.

Before compiling Linux, you need to make sure the branch that's checked out is [this branch, from Coreforge's Pi OS Linux fork](https://github.com/Coreforge/linux/pull/1). Alternatively, you can clone the [`raspberrypi/linux` source at `rpi-5.10.y`](https://github.com/raspberrypi/linux/tree/rpi-5.10.y), and apply Coreforge's branch [as a patch file](https://patch-diff.githubusercontent.com/raw/Coreforge/linux/pull/1.patch).

I've been working on a [5.15.y update to that branch](https://github.com/geerlingguy/linux/pull/3), but that version isn't quite working yet, since some of the overridden AMD driver flags we modified were removed between Linux 5.10 and 5.15.

To make things easier on yourself, blacklist the radeon driver before copying the cross-compiled kernel to the Pi. Create a file named `/etc/modprobe.d/blacklist-radeon.conf`, with the contents:

```
blacklist radeon
```

Then copy the cross-compiled kernel to the Pi. We're _almost_ done, but to make Xorg and other compositors like Weston run, you also need to override the `memcpy` library:

```
# Download Coreforge's modified memcpy library.
wget https://gist.githubusercontent.com/Coreforge/91da3d410ec7eb0ef5bc8dee24b91359/raw/1b72d428b2fe1cba459d5ae7f73663483743ff55/memcpy_unaligned.c

# Compile the library and move it into place.
gcc -shared -fPIC -o memcpy.so memcpy_unaligned.c
sudo mv memcpy.so /usr/local/lib/memcpy.so

# Create an `ld.so.preload` file to instruct Linux to use our version of `memcpy`.
sudo nano /etc/ld.so.preload

# Put the following line inside ld.so.preload:
/usr/local/lib/memcpy.so
```

### Load the driver

Now, reboot the Raspberry Pi. After it reboots, you can open up a terminal session and run `dmesg --follow` to see what's going on (you don't have to, though).

To load the `radeon` driver, run:

```
sudo modprobe radeon
```

After 10 or 20 seconds, if you have a monitor plugged into the Radeon card, it should come up as the driver loads. Typically I set Pi OS to boot to console (CLI) instead of to the graphical system, since that is more stable.

For better stability running Xorg (`startx` to launch) or Weston (`weston-launch` to launch), you should also add the following options to your `/boot/cmdline.txt` (in the same line as the other options) and reboot:

```
radeon.uvd=0 pci=noaer,nomsi radeon.msi=0 radeon.pcie_gen2=0 pcie_aspm=off radeon.aspm=0 radeon.runpm=0 radeon.dpm=0
```

The patches and cmdline options are still actively being investigated. Follow this issue for further progress: [Test GPU (VisionTek Radeon 5450 1GB)](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4).

> We've also gotten the SiliconMotion SM750 graphics working with [this patch](https://github.com/geerlingguy/linux/pull/2), but as it's an older `fb` driver, it only reliably works for a text console, as there are issues getting Xorg running with it. The driver in the Linux kernel isn't really maintained, and wasn't the highest-quality to begin with.

## What works

{{< figure src="./pi-desktop-janky-amd-radeon.jpg" alt="Pi OS Xorg desktop janky glitches with neofetch stats" width="700" height="394" class="insert-image" >}}

In summary: DisplayPort, VGA, HDMI, and DVI ports. The command line (console), Xorg, and Weston (a reference implementation of Wayland), as well as some 3D benchmarks and applications that use OpenGL.

But Xorg especially shows a lot of 'glitches' in its output (see above), especially when interacting with different screen elements.

{{< figure src="./weston-smoother-amd-radeon-pi.jpg" alt="Weston running more smoothly on Radeon on Raspberry Pi" width="700" height="394" class="insert-image" >}}

Weston (pictured above) didn't have the same glitchy behavior, but ran a bit sluggish and would often lock up after a while (necessitating a soft reboot).

{{< figure src="./jellyfish-glmark2-drm-raspberrypi-amd-radeon.jpg" alt="GLMark2 DRM jellyfish example" width="700" height="394" class="insert-image" >}}

`glmark2-drm` (see [how I installed GLMark2 on the Pi](https://www.jeffgeerling.com/blog/2022/how-run-glmark2-drm-benchmark-external-gpu-on-raspberry-pi)) and `glxgears` usually ran all the way through, but sometimes would lock up in the middle of a run.

The driver is _far_ from optimal in its current state—there's a lot of debug code currently, and the memory copy implementations err on the side of caution, slowing down some operations significantly (GLMark2 gives a score of about 50, and `glxgears` was rendering at 25-35 fps—slower than the VC4 GPU built into the Pi!

## What doesn't work

A lot of things still don't work, since each specific feature of a given line of cards would need more work combing through code, finding memory issues.

As one example, H.264 acceleration is currently disabled, so [using the card as an `ffmpeg` video transcoding accelerator](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4#issuecomment-1101653278) isn't going to work. Also, assuming we could get Nvidia's drivers working (or more realistically, `nouveau`, since Nvidia doesn't open source their driver), things like CUDA cores would still be inaccessible.

And even after more work, it's unlikely you'd be able to do something like play a AAA game on a Pi with an external GPU. Many things are working against this possibility right now:

  1. The x1 Gen 2.0 lane doesn't provide a ton of bandwidth.
  2. Most (all?) AAA games are compiled for X86 platforms, not for ARM/ARM64. Box86/Box64 would struggle, especially with a hacked-together graphics driver.
  3. Trying to sort through layers of incompatibilities with (a) ARM64, (b) Linux, and (c) a modified driver for an older unsupported GPU is a pretty crazy task.

I won't say _never_, but it's highly unlikely a Compute Module 4 will do anything outside of highly specialized external-GPU-related tasks—and that's assuming we haven't hit a dead end already.

## What's next?

First, I'm sure many people reading this post had the following thoughts pop in their heads:

  - What about running [Windows on Raspberry](https://www.worproject.ml)? After all, Windows is much better for gaming!
  - You should try powering the card differently; the CM4 IO Board can only supply up to 25W!
  - What about Rockchip or Allwinner SoCs? Or Apple's M1?

Well, in all three of the above cases, these avenues have been discussed and explored quite a bit, and let me assure you they are _usually_ dead ends:

**Windows**: Windows on Raspberry runs Windows for ARM, which does _not_ support ARM GPU drivers in any way I've seen so far. And Windows GPU drivers are also more obtuse than Linux drivers, meaning it would be harder for a random guy like me to debug them, anyways. And finally, it's unlikely Microsoft will patch around _hardware PCIe bugs_ on the BCM2711 since they don't even support Windows on Raspberry Pi hardware _anyways_!

**Power**: The issues we're running into are _not_ power-related, and I have also tested all the graphics cards in powered risers with beefy 650W and 750W PSUs.

**Other SoCs**: There _are_ some ARM platforms that _do_ support external GPUs, like some of Solid-Run's boards. But most ARM SoCs—especially ones that are targeted at mobile/embedded use—have a broken PCIe root complex (just like the Broadcom BCM2711) and run into very similar (if not identical) issues with things like graphics cards.

[pgwipeout has been exploring some Rockchip SoCs' PCIe bus](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/336#issuecomment-1070922599), and had this to say:

> We already know BRCM doesn't care about complying with the spec, and their implementation is severely broken.
> 
> It seems the rk35xx series also doesn't comply, but not nearly as bad.
> 
> I'm trying to narrow down exactly how bad, so that I can document it as we finalize the PCIe support for mainline.

So far it seems like we're hitting similar dead ends with MMIO and PCIe memory management on all the SoCs on lower-cost SBCs—at least of the current generation.

My hope is future chips from Broadcom _et all_ may have a better implementation, that could at least work with the latest generation of PCIe devices, and not require workarounds like [avoiding `writeq` on 64-bit OSes](https://github.com/raspberrypi/linux/issues/4158).

As it stands, some devices (like [newer LSI HBAs](https://pipci.jeffgeerling.com/#sata-cards-and-storage)) can work around the issues with minimal performance penalties, while other devices (like graphics cards and Google's Coral TPU) seem to be crippled.

If you want to follow along on our journey (work continues! Coreforge is experimenting with Minecraft on the GPU currently...), please follow these issues on GitHub:

  - [Radeon 5450/6450/7470 testing on the Pi](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4)
  - [Radeon RX 6700 XT testing on the Pi](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/222)
  - [ASRock Rack M2_VGA SM750 on the Pi](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/62)
  - [Radeon RX 550 testing on the Pi](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/6)
  - [Pine64 SOQuartz Testing - Rockchip RK3566](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/336)
