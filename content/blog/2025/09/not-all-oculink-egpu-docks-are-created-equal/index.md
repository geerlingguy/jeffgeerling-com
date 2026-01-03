---
nid: 3500
title: "Not all OCuLink eGPU docks are created equal"
slug: "not-all-oculink-egpu-docks-are-created-equal"
date: 2025-09-29T14:39:02+00:00
drupal:
  nid: 3500
  path: /blog/2025/not-all-oculink-egpu-docks-are-created-equal
  body_format: markdown
  redirects:
    - /blog/2025/using-minisforum-deg1-gpu-dock-on-non-minisforum-systems
    - /blog/2025/not-all-oculink-cables-are-created-equal-minisforum-egpu-on-pi
    - /blog/2025/not-all-oculink-cables-are-created-equal
aliases:
  - /blog/2025/using-minisforum-deg1-gpu-dock-on-non-minisforum-systems
  - /blog/2025/not-all-oculink-cables-are-created-equal-minisforum-egpu-on-pi
  - /blog/2025/not-all-oculink-cables-are-created-equal
tags:
  - amd
  - cable
  - egpu
  - gpu
  - minisforum
  - oculink
  - pcie
  - raspberry pi
---

I recently tried using the [Minisforum DEG1 GPU Dock](https://amzn.to/46Y65Wo) with a Raspberry Pi 500+, using an M.2 to OCuLink adapter, and [this chenyang SFF-8611 Cable](https://amzn.to/48CZlyl).

After figuring out there's a power button on the DEG1 (which needs to be turned on), and after fiddling around with the switches on the PCB (hidden under the large metal plate on the bottom; TGX to OFF was the most important setting), I was able to get the Raspberry Pi's PCIe bus to at least tell the graphics card installed in the eGPU dock to spin up its fans and initialize.

But I wasn't able to get any output from the card (using [this Linux kernel patch](https://github.com/geerlingguy/raspberry-pi-pcie-devices/discussions/756)), and `lspci` did not show it. (Nor were there any logs showing errors in `dmesg`).

{{< figure src="./pi-500-plus-egpu-jmt-dock.jpeg" alt="Pi 500+ JMT eGPU Dock Setup" width="700" height="394" class="insert-image" >}}

I switched back to my [JMT eGPU OCuLink dock](https://amzn.to/3IBI3XY) for the rest of my testing, and uploaded a [video detailing some of my struggles](https://youtu.be/Dv3RRAx7G6E?t=321), and a [blog post detailing the Pi 500+ eGPU testing](https://www.jeffgeerling.com/blog/2025/full-egpu-acceleration-on-pi-500-15-line-patch).

A few commenters mentioned they _too_ had issues with the Minisforum DEG1. But a few of them looked closely at the _OCuLink cable_ Minisforum included, and noted there were a couple extra colored wires going through the cable sleeve that _didn't_ seem to be present on other cables—like the chenyang I was using! They suggested I try swapping cables.

So I did... and testing it with an RX 6500 XT worked!

{{< figure src="./minisforum-dock-working-with-pi-500-plus.jpeg" alt="Minisforum dock working with AMD RX 6500 XT eGPU on Raspberry Pi 500+" width="700" height="467" class="insert-image" >}}

Looking closely at the cables side by side, I can confirm what some of the commenters said: the cable that came with the DEG1 looks like it has additional colored wires going between the connectors.

{{< figure src="./oculink-cable-difference-minisforum-colored-wires.jpeg" alt="OCuLink cable that came with Minisforum DEG1" width="700" height="467" class="insert-image" >}}

Moral of the _this_ portion of the story: not all OCuLink cables are created equal.

## Going Deeper

But then I swapped back to my RX 7900 XT, the one that was previously unrecognized in the Miniforum dock... and it still wouldn't work.

```
$ lspci
0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 30)
0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
```

I tried all three switches in different settings, I tried swapping OCuLink cables back and forth again... nothing. The RX 6500 XT was happy as can be, but the 7900? Nope.

I even popped in an Intel B580 card, and _it_ worked too...

```
$ lspci
0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 30)
0001:01:00.0 PCI bridge: Intel Corporation Device e2ff (rev 01)
0001:02:01.0 PCI bridge: Intel Corporation Device e2f0
0001:02:02.0 PCI bridge: Intel Corporation Device e2f1
0001:03:00.0 VGA compatible controller: Intel Corporation Battlemage G21 [Arc B580]
0001:04:00.0 Audio device: Intel Corporation Device e2f7
0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 30)
0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
```

So now I'm left scratching my head: _what's different about the RX 7900 XT?_ And _why does my cheaper $50 eGPU dock seem to work with everything, but the $99 Minisforum DEG1 doesn't?_

Searching through forum posts, I even found [someone running a 7900 XT in the DEG1 on a Pi](https://forums.raspberrypi.com/viewtopic.php?t=387794), so maybe it's just a strange fluke with my setup?

Inconsistencies like these really bother me. And they usually eat up an entire afternoon, because I'm always _certain_ it's a PEBKAC, and I usually exhaust every route debugging before I'd waste a vendor or a maintainer's time with a bug report!

{{< figure src="./oculink-amphenol-cable-info.jpg" alt="OCuLink cable dimensions and pinout from Amphenol" width="700" height="495" class="insert-image" >}}

I haven't yet torn down one of these cables to try to figure out which pins are perhaps missing on the chenyang cable (see [OCuLink Pinouts here](https://jpc-pt.com/wp-content/uploads/2017/10/AMPH-OCUL4X-A-RA-XXX-Sent-Out_01.jpg). The bigger issue there is, I can't find a source for the cable Minisforum includes separate from the DEG1 dock, and most online listings don't clearly show which kind of cable you'll get—with or without the extra wires!

## Update - Oct 2025

After publishing this blog post, X user [@changeforabuttn](https://x.com/changeforabuttn/status/1907058254527566209) pointed out a successful test of the RX 7900 XT with a PCIe ReDriver built into the [Micro SATA M.2 to OCuLink adapter](https://amzn.to/47yPrwP):

<blockquote class="twitter-tweet" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">The <a href="https://twitter.com/Hi_MINISFORUM?ref_src=twsrc%5Etfw">@Hi_MINISFORUM</a> DEG1 works great with my <a href="https://twitter.com/Raspberry_Pi?ref_src=twsrc%5Etfw">@Raspberry_Pi</a> CM5 and M.2 M-Key w/ ReDriver to OCulink 4i Adapter from <a href="https://twitter.com/MicroSATA?ref_src=twsrc%5Etfw">@MicroSATA</a>! I&#39;ve tested many other adapters, which may correctly power the dock on/off, but the GPU is never detected. FWIW, my llama-bench scores remain unchanged <a href="https://t.co/P5xc7pTJwx">pic.twitter.com/P5xc7pTJwx</a></p>&mdash; Nicholas A (@changeforabuttn) <a href="https://twitter.com/changeforabuttn/status/1907058254527566209?ref_src=twsrc%5Etfw">April 1, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

@changeforabutton graciously sent me an adapter to test (apparently the thing's out of stock _everywhere_ right now), and I can confirm it gets all the troublesome cards working on the DEG1. So I guess... with the right PCIe adapter setup, a DEG1 is still a valid choice.

I think for critical work, I'll stick with my JMT dock, but for convenience and large-card physical stability, I'll start using the DEG1 with the ReDriver adapter. Hopefully I can find another option, because most of the M.2 adapters are just straight pin-to-pin without active electronics (which degrades the PCIe link quality).
