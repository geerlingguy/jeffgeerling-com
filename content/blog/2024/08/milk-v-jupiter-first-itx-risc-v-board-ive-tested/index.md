---
nid: 3397
title: "Milk-V Jupiter is the first ITX RISC-V board I've tested"
slug: "milk-v-jupiter-first-itx-risc-v-board-ive-tested"
date: 2024-08-05T14:05:40+00:00
drupal:
  nid: 3397
  path: /blog/2024/milk-v-jupiter-first-itx-risc-v-board-ive-tested
  body_format: markdown
  redirects: []
tags:
  - jupiter
  - milk-v
  - mini itx
  - risc-v
  - video
  - youtube
---

{{< figure src="./milk-v-jupiter-motherboard.jpeg" alt="Milk-V Jupiter Mini ITX Motherboard" width="700" height="auto" class="insert-image" >}}

The latest RISC-V computer I've tested is the Milk-V Jupiter. It's pokey at [Intel Core 2 Duo](https://browser.geekbench.com/v6/cpu/compare/6979805?baseline=6998183) levels of performance—at least according to Geekbench.

But performance is only one aspect that interests me. This is the first RISC-V Mini ITX motherboard I've tested, which means it can be installed in a PC case or rackmount enclosure, and it is much more featureful than a typical credit-card-sized SBC.

It includes niceties like front panel IO, front-panel Audio, USB 3.0, and USB 2.0, 24-pin ATX power input, an M.2 M-key slot for NVMe, _and_ an open ended PCI Express slot!

This blog post follows along roughly with today's video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/YxtFctEsHy0" frameborder='0' allowfullscreen></iframe></div>
</div>

## Hardware

Being ITX means you can deploy it in any PC case, or even [in my 10" rack](https://www.youtube.com/watch?v=c8-cdA50bpU)! Companies like Milk-V are betting it all on a future where RISC-V is neck-in-neck with X86 and Arm for everything from servers to desktops.

Before testing the Jupiter in a Fractal North PC case, I ran it on my test bench and, as always, compiled [every benchmark and bringup note in my sbc-reviews repo](https://github.com/geerlingguy/sbc-reviews/issues/47).

[All the RISC-V SBCs I've tested](https://www.jeffgeerling.com/tags/risc-v) before are based on older chips like the JH7110, designed with older and less-complete RISC-V specs.

{{< figure src="./milk-v-jupiter-spacemit-m1-x60-soc.jpeg" alt="Spacemit M1 RISC-V SoC on Milk-V Jupiter" width="700" height="auto" class="insert-image" >}}

This board is based on the [Spacemit M1](https://www.spacemit.com/en/key-stone-k1/), a newer RISC-V chip with 8 X60 CPU cores running at 1.8 GHz. It won't be blazing fast, but it *is* the fastest RISC-V board I've tested.

Lower spec models of Jupiter are available with a 1.6 GHz-clocked K1, with either 4 or 8 gigs of RAM. The top-end M1 model comes with 16 GB.

Here are the Geekbench 6 results:

{{< figure src="./milk-v-jupiter-geekbench-6.jpg" alt="Milk-V Jupiter - Geekbench 6 Results" width="700" height="auto" class="insert-image" >}}

I know Geekbench doesn't hold much weight, especially comparing across architectures, but I still like it. It gives hard numbers based on code that exists in the wild. Many apps are in the same boat, where they aren't optimized for every platform the same (and are especially weak on RISC-V). So in that sense, if you see some wild results, maybe the code libraries underlying them could use a little love.

All that outta the way, the 8-core M1 _is_ faster than the JH7110 I've seen in all the other boards. But at least for Geekbench, most of that speedup is from having more cores, not necessarily from the cores being faster _individually_. The current Raspberry Pi still trounces them all, and RISC-V SBCs are about on par with a Pi 3 now, at least for CPU.

{{< figure src="./milk-v-jupiter-hpl-efficiency.jpg" alt="Milk-V Jupiter - HPL and Efficiency Results" width="700" height="auto" class="insert-image" >}}

To further illustrate that point, I also ran my HPL benchmarks, and it shows a similar story. Except here, the speedup from the 8 cores is more apparent. It's still nowhere near a modern Pi, and better Arm chips like the RK3588 go off the charts in these graphs.

The efficiency is improving a little, but it's still nowhere near Arm—and not even Intel or AMD yet.

{{< figure src="./milk-v-jupiter-linux-kernel-compile.jpg" alt="Milk-V Jupiter - Linux Kernel Compilation" width="700" height="auto" class="insert-image" >}}

Linux Kernel compilation is a little better, _and_ it's also a more realistic workload. This is also the first time I was able to get one of Milk-V's boards to even _complete_ the Phoronix kernel compile test (it still has trouble on other `pts` benchmarks).

So it's not fast. And compatibility's a work in progress. Why would anyone buy it?

The the biggest difference between this and the older boards is it's the first processor I've seen with [RVA22](https://github.com/riscv/riscv-profiles/blob/main/src/profiles.adoc#rva22-profiles) and [RVV 1.0](https://github.com/riscv/riscv-v-spec/releases/tag/v1.0) support. RISC-V is reaching a maturity level that should let devs optimize things better now, like [when Arm introduced it's NEON architecture](https://peterdn.com/post/2014/01/03/an-introduction-to-arm-neon/).

This year's also the first time I've tried out [Bianbu Linux](https://bianbu-linux.spacemit.com/en/), an Ubuntu derivative Spacemit is pushing.

In the video embedded above, I spoke with Christopher Barnatt from the [ExplainingComputers YouTube channel](https://www.youtube.com/@ExplainingComputers) about the progress RISC-V has made in comparison to Arm for SBCs and general desktop use—you can watch the video to see his thoughts. But as I see very little English-language coverage of Bianbu, I thought I'd write a little on the OS here.

## Bianbu Linux and RISC-V Linux support

With how slowly [Windows on Arm](https://learn.microsoft.com/en-us/windows/arm/overview) has progressed, I don't hold out much hope for Microsoft ever considering RISC-V as a platform worthy of their licensed OS. And I don't think Apple has much interest in moving architectures any time soon, as their M-series Arm cores have been serving them _very_ well.

So Linux it is! And [Canonical seems to have a good relationship with Milk-V](https://canonical.com/blog/canonical-enables-ubuntu-on-milk-v-mars), so Ubuntu seems to be the base distro off which Bianbu Linux is built.

Spacemit maintains their [Linux kernel 6.1 fork](https://gitee.com/bianbu-linux) over on Gitee (a China-backed GitHub/GitLab-style platform), and there are already forks like one from icenowy which [add basic support for the open source AMD graphic card driver stack](https://gitee.com/icenowy/linux-6.1/tree/k1-gpu), at least for the Spacemit K1/M1.

Milk-V maintains [their own Ubuntu and Bianbu builds for the Jupiter](https://github.com/milkv-jupiter) over on GitHub, and they're already maintaining full desktop, NAS (via OpenMediaVault), and minimal images.

The Fedora V-Force initiative is also providing [Fedora 41 RISC-V images](https://image.fedoravforce.com) for tons of boards, including the Jupiter, and I tested 6 different images (minimal + desktop for Ubuntu, Bianbu, and Fedora) and had zero issues booting any of them on my Jupiter.

As with most Arm SBCs, there isn't a standardized UEFI interface or any BIOS that I could find, so you have to use images built for the board—or use [Buildroot to build your own](https://milkv.io/docs/jupiter/build-os/buildroot).

_Unlike_ Arm SBCs—at least those not from Raspberry Pi—the company and devs behind the Jupiter seem active on the forums, eager to expand the docs, and generally helpful. It feels like they want their hardware to succeed, and are going to spend time working on the 'soft' parts: software, support, and community.

## Building my first RISC-V PC

I installed the Jupiter inside a (massively overkill) Fractal North (which pairs nicely with my [3D printed Baby North](https://www.youtube.com/watch?v=ncyl7cTU9k8)), and the board is surprisingly well-rounded.

{{< figure src="./milk-v-jupiter-installed-in-fractal-north.jpeg" alt="Milk-V Jupiter installed in Fractal North PC case" width="700" height="auto" class="insert-image" >}}

The front panel connections all worked out of the box (I tested power + LED, front panel audio, and USB 3.0), and the board powers on automatically when you apply power—either via USB-C PD, an integrated 12V DC barrel jack, or 24-pin ATX from a PC power supply or a Pico PSU.

{{< figure src="./milk-v-jupiter-ports.jpeg" alt="Milk-V Jupiter rear IO ports" width="700" height="auto" class="insert-image" >}}

There are headers for UART inside, and the back exposes dual 1 Gbps LAN ports, HDMI, USB, and audio... a common assortment of ports. I installed an M.2 NVMe SSD and got PCIe Gen 2x1 speed. I tested the included PCIe Gen 2x2 slot (it's open ended, so you can install any type of card), and was able to see a card plugged in. _Working drivers_ for PCIe devices (outside of NVMe and some simpler devices) are another matter, just like Arm.

I was impressed by how the board just... worked. I know there are a couple ITX boards with Intel's N100, and Radxa makes a [Rock 5 ITX](https://radxa.com/products/rock5/5itx/) board, but this already puts RISC-V right on par with the other architectures, at least in terms of the base feature set.

Boost the CPU and improve its efficiency, add more PCIe bandwidth, and this would make a very reasonable desktop or server board!

## Using it as a Linux Workstation

{{< figure src="./milk-v-jupiter-bianbu-youtube-240p.jpg" alt="Milk-V Jupiter playing back YouTube video at 240p" width="700" height="auto" class="insert-image" >}}

I wrote about [Docker and RISC-V](/blog/2024/state-docker-on-popular-risc-v-platforms) and [Ansible and RISC-V](/blog/2024/installing-ansible-on-risc-v-computer) earlier this year.

Software support for RISC-V has improved at a rapid pace, and besides being slow, I was able to run a common set of apps from LibreOffice, to Chromium (YouTube only plays my videos smoothly at 240p!), to SuperTuxKart.

## Conclusion

It all works—a bit better than I expected. And the price for this board, considering it has the CPU, RAM, motherboard, and an IO shield included, is not bad. My M1/16GB model costs $115 (mine was provided as a review sample by Milk-V), but the base model, with 4GB of RAM and a K1 SoC, is only $60—that's a whole RISC-V motherboard for the price of a Raspberry Pi 5.

But RISC-V isn't ready for prime-time yet. It's meant for developers building and testing their software on RISC-V. It's fun to see a 3rd architecture rise to prominence. And we can thank Arm's popularity for making build toolchains and repos like Docker Hub easier to use with multiple architectures.
