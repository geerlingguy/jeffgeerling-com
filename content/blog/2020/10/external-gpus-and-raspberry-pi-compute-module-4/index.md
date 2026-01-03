---
nid: 3046
title: "External GPUs and the Raspberry Pi Compute Module 4"
slug: "external-gpus-and-raspberry-pi-compute-module-4"
date: 2020-10-27T20:13:28+00:00
drupal:
  nid: 3046
  path: /blog/2020/external-gpus-and-raspberry-pi-compute-module-4
  body_format: markdown
  redirects: []
tags:
  - amd
  - cm4
  - compute module
  - gpu
  - nvidia
  - pcie
  - raspberry pi
---

The [Raspberry Pi Compute Module 4](https://www.raspberrypi.org/products/compute-module-4/) eschews a built-in USB 3.0 controller and exposes a 1x PCI Express lane.

The slightly older Raspberry Pi 4 model B could be [hacked](http://labs.domipheus.com/blog/raspberry-pi-4-pci-express-it-actually-works-usb-sata-gpu/) to get access to the PCIe lane (sacrificing the VL805 USB 3.0 controller chip in the process), but it was a bit of a delicate operation and only a few daring souls tried it.

{{< figure src="./raspberry-pi-cm4-zotac-nvidia-gpu.jpg" alt="Raspberry Pi Compute Module 4 with Zotac Nvidia GeForce GT 710 GPU" width="600" height="336" class="insert-image" >}}

> Watch this video for more detail about my experience using these GPUs on the CM4:  
> [GPUs on a Raspberry Pi Compute Module 4!](https://www.youtube.com/watch?v=ikpgZu6kLKE)

Now that the CM4's IO Board has a 1x slot, it's trivial to plug in any PCI Express card, and test out its functionality with the Raspberry Pi. And test I have! I am detailing all the cards I've tested and the results on my [Raspberry Pi PCIe device compatibility database](https://pipci.jeffgeerling.com), and you can look at the linked issues to learn more about each card.

## GPUs and the Raspberry Pi

The Pi's BCM2711 SoC includes a VideoCore 6 GPU capable of features like H.265 4Kp60 decode, H.264 1080p60 decode, and 1080p30 encode. It also supports OpenGL ES 3.0, and it's not a terrible little GPU for what it costs.

But there are many people who have wanted to know whether you could use an Nvidia or AMD GPU with a Pi, and I have tried answering that question.

{{< figure src="./nvidia-amd-gpus-raspberry-pi-cm4.jpeg" alt="Nvidia and AMD PCIe GPU with Raspberry Pi Compute Module 4 IO Board" width="1200" height="802" class="insert-image" >}}

And so far, the answer seems to be 'no.'

Partly it's due to lack of support for I/O BAR space on the BCM2711 ARM SoC, and partly it _may_ be due to driver bugs or features that are only supported on X86 or certain ARM architectures.

I have tried the following drivers, and all of them failed to initialize the card fully in one way or another:

For the [Zotac Nvidia GeForce GT 710](https://amzn.to/3mqdvrp):

  - [Nouveau](https://nouveau.freedesktop.org) open source driver (you have to recompile the Raspberry Pi OS kernel to enable it)
  - Nvidia [32-bit ARM driver](https://www.nvidia.com/en-us/drivers/unix/linux-arm-display-archive/)
  - Nvidia [64-bit ARM driver](https://www.nvidia.com/en-us/drivers/unix/linux-aarch64-archive/)

For the [VisionTek AMD Radeon 5450](https://amzn.to/37HYcGx):

  - [Radeon open source driver](https://help.ubuntu.com/community/RadeonDriver) (you have to recompile the Raspberry Pi OS kernel to enable it)
  - AMDGPU open source driver... which I found after trying to use it does not work with as old a video card as the one I tried!

Just getting the hardware to plug in might be your first challenge, as many (in fact, almost _all_) GPUs have physical slots that won't fit in the IO Board's x1 PCIe slot. You _could_ hack off the bit in the middle to make the card physically fit, and it would work, but luckily there are [x1 to x16 adapters](https://amzn.to/31Nrobi) that allow larger cards to plug into the x1 slot (though without the added lanes of bandwidth).

Most cards work fine with fewer lanes available; they just don't get as much bandwidth between the GPU and the CPU.

Both cards were recognized appropriately when I ran `lspci`, so at least there was a glimmer of hope:

```
# Nvidia GeForce GT 710
01:00.0 VGA compatible controller: NVIDIA Corporation GK208 [GeForce GT 710B] (rev a1) (prog-if 00 [VGA controller])
	Subsystem: ZOTAC International (MCO) Ltd. GK208B [GeForce GT 710]
	Flags: fast devsel
	Memory at 600000000 (32-bit, non-prefetchable) [disabled] [size=16M]
	Memory at <unassigned> (64-bit, prefetchable) [disabled]
	Memory at <unassigned> (64-bit, prefetchable) [disabled]
	I/O ports at <unassigned> [disabled]
	[virtual] Expansion ROM at 601000000 [disabled] [size=512K]
	Capabilities: [60] Power Management version 3
	Capabilities: [68] MSI: Enable- Count=1/1 Maskable- 64bit+
	Capabilities: [78] Express Legacy Endpoint, MSI 00
	Capabilities: [100] Virtual Channel
	Capabilities: [128] Power Budgeting <?>
	Capabilities: [600] Vendor Specific Information: ID=0001 Rev=1 Len=024 <?>

# AMD Radeon 5450
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Cedar [Radeon HD 5000/6000/7350/8350 Series] (prog-if 00 [VGA controller])
	Subsystem: VISIONTEK Cedar [Radeon HD 5000/6000/7350/8350 Series]
	Flags: fast devsel, IRQ 255
	Memory at <unassigned> (64-bit, prefetchable) [disabled]
	Memory at 600000000 (64-bit, non-prefetchable) [disabled] [size=128K]
	I/O ports at <unassigned> [disabled]
	[virtual] Expansion ROM at 600020000 [disabled] [size=128K]
	Capabilities: [50] Power Management version 3
	Capabilities: [58] Express Legacy Endpoint, MSI 00
	Capabilities: [a0] MSI: Enable- Count=1/1 Maskable- 64bit+
	Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
	Capabilities: [150] Advanced Error Reporting
```

## BAR space woes

PCI express devices require BAR ('Base Address Register') space to be able to initialize and map memory to the computer's own memory space, and the Pi [currently gives devices 64 MB of RAM](https://github.com/raspberrypi/linux/blob/rpi-5.4.y/drivers/pci/controller/pcie-brcmstb.c) for this purpose.

That's fine for a simple device like the VL805 USB 3.0 controller used in the regular Pi 4, and for things like NVMe drives and SATA adapters. But GPUs require a lot more BAR space, so after a bit of research, I [documented the process for expanding the BAR space on the Pi to 1 GB](https://gist.github.com/geerlingguy/9d78ea34cab8e18d71ee5954417429df) after some help from a couple engineers on the Pi Forums.

The Nvidia GPU was happy with just 256 MB of RAM available, but the AMD Radeon wanted 1 GB. This also means that the lowest-end 1 GB Compute Module 4 might not be adequate for certain applications when you want to pair them with PCIe devices.

## Driver woes

Once I got through the BAR space issue, and `dmesg` was showing all the MEM space was allocated correctly (though IO space was not, since the BCM2711 doesn't have any IO registers for PCIe devices), I started trying out all the drivers I could find:

  - **The Nouveau open source driver** for Nvidia cards had to be compiled into a custom Pi kernel—neither Pi OS nor Ubuntu for Pi has it available by default (to save space in their images). Once I got it compiled, the Pi completely locked up during boot if I had the card inserted. No serial output, nothing.
  - **The Nvidia ARM32 driver** would fail to compile the kernel module due to a ton of errors; I'm not sure if this driver would install on any ARM device currently.
  - **The Nvidia ARM64 driver** compiled and loaded, but during card initialization it output `RmInitAdapter failed!` and I couldn't get past that.
  - ** The Radeon open source driver** also needs to be compiled, and almost initialized the card, but [complained](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4#issuecomment-715613166) that it was `Unable to find PCI I/O BA`. Oh well.

You can follow my entire journey with these cards in these two issues:

  - [Test GPU (VisionTek Radeon 5450 1GB)](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4)
  - [Test GPU (Zotac Nvidia GeForce GT 710)](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/2)

## What about CUDA?

I thought that maybe I could still use [CUDA](https://developer.nvidia.com/cuda-toolkit) on the Nvidia card even though the GPU wouldn't initialize and output a signal over HDMI, nor work with Xorg... but alas, it seems the CUDA tools require the card to initialize in the same way as the graphics bits, so I got that same `RmInitAdapter failed!` message in `dmesg`.

It also turns out the 710 _might_ not be compatible with CUDA 11, as it wasn't listed on the [GPU compatibility page](https://developer.nvidia.com/cuda-gpus) (even though the 705, 720, 730, and 720 were), even though it is advertised as having 192 CUDA cores. Ah well.

## Other ARM attempts

{{< figure src="./96boards-oxalis.jpg" alt="96Boards Oxalis board" width="600" height="454" class="insert-image" >}}

It looks like the closest anyone's gotten to using a GPU with a readily-available ARM board is [@sahajsarup](https://www.geektillithertz.com), and in [this livestream with 96Boards](https://www.youtube.com/watch?v=rPHahahbheo), he demoed getting console output over HDMI through the 96Boards [Oxalis](https://www.96boards.org/product/oxalis/) hardware. That board costs over $400, though, so it's hardly in the same price range as a Raspberry Pi!

And before the Compute Module 4 was released, a couple people hacked out the VL805 chip and routed the PCIe bus through an external riser, most notably [@domipheus](https://twitter.com/domipheus/status/1175340360060612608), who got about as far along as I did and seemed to also hit a wall.

Besides that, it looks like there were similar troubles in the land of the [ROCKPro64](https://www.pine64.org/rockpro64/), as [tllim mentions](https://forum.pine64.org/showthread.php?tid=6205&pid=42832#pid42832):

> I don't think NVidia card can work on ROCKPro64, this due to graphic card needs large IO Memory range.

As TL Lim is the founder of Pine64, I'd say his opinion is pretty solid.

## Next Steps

Every time I post a story of failure or conjecture, there are immediately a number of suggestions for follow-up, and if I tried them all... well I'd never be able to get anything else done.

But a few things did stand out, and when I get time I may try them:

  - Using an externally-powered riser to see if getting more power to the GPU that is not coming through the Pi's own PCIe circuit could help at all. (I have a riser, but don't have the power adapter to get it going yet).
  - Trying out [Windows on Raspberry](https://www.worproject.ml)—I don't have high hopes for it to work, but this would be a good excuse to at least take it for a spin.
  - Trying to see if there's another way to work around the IO BAR space limitations. According to some people I've spoken with, they have gotten these cards working on other ARM devices, but they're always mum about which devices specifically (I'm guessing maybe things like Graviton at AWS, which they probably can't discuss in detail?).
  - Testing a slightly newer card, like the [AMD Radeon RX 550](https://amzn.to/35IS26a), which doesn't have BIOS (uses UEFI) and has overall newer architecture, supported by the amdgpu driver.

Anyways, this was quite an adventure, and in the end, even though I didn't get a GPU to output a video signal from the Pi, I did learn a _lot_ about PCIe, the Linux kernel, and the Raspberry Pi Compute Module 4.

Be sure to check out my video [GPUs on a Raspberry Pi Compute Module 4!](https://www.youtube.com/watch?v=ikpgZu6kLKE), and my website where I'm documenting all the PCIe cards I'm testing with the CM4: [Raspberry Pi PCIe device compatibility database](https://pipci.jeffgeerling.com).
