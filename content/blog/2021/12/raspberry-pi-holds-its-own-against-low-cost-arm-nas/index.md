---
nid: 3161
title: "Raspberry Pi holds its own against low-cost ARM NAS"
slug: "raspberry-pi-holds-its-own-against-low-cost-arm-nas"
date: 2021-12-22T15:00:05+00:00
drupal:
  nid: 3161
  path: /blog/2021/raspberry-pi-holds-its-own-against-low-cost-arm-nas
  body_format: markdown
  redirects: []
tags:
  - asustor
  - benchmarks
  - cm4
  - compute module
  - drivestor
  - networking
  - radxa
  - raid
  - raspberry pi
  - reviews
  - taco
  - video
  - youtube
---

Earlier this year, I [pitted the $549 ASUSTOR Lockerstor 4 NAS against a homebrew $350 Raspberry Pi CM4 NAS](https://www.youtube.com/watch?v=vBccak8f-VY), and came to the (rather obvious) conclusion that the Lockerstor was better in almost every regard.

{{< figure src="./jeff-holds-both-nases.jpeg" alt="Jeff Geerling holding Raspberry Pi Radxa Taco NAS board and ASUSTOR Drivestor 4 Pro" width="700" height="393" class="insert-image" >}}

Well, ASUSTOR introduced a new lower-cost NAS, the $329 Drivestor 4 Pro (model AS3304T—pictured above), and sent me one to review against the Raspberry Pi, since it make for a better matchup—both have 4-core ARM CPUs and a more limited PCI Express Gen 2 bus at their heart.

Around the same time, Radxa also sent me their new Taco—a less-than-$100 Raspberry Pi Compute Module 4 carrier board with 5x SATA ports, 1 Gbps and 2.5 Gbps Ethernet, an M.2 NVMe slot, and an M.2 A+E key slot. (The Taco will soon be available as part of a kit with a CM4 and case for around $200.)

The specs evenly matched, at least on paper:

{{< figure src="./ASUSTOR-vs-Pi-Taco-specs-comparison.jpeg" alt="Radxa Taco Raspberry Pi NAS vs ASUSTOR Drivestor 4 Pro NAS spec comparison" width="840" height="473" class="insert-image" >}}

But specs are one thing, measurable performance is another.

## Disk performance

I benchmarked the raw disk access performance with `fio` and `iozone` to get a general idea of how fast the SATA drives would perform in RAID 5.

I chose RAID 5 because it taxes all the subsystems that are traditionally weak points on lower-powered ARM boards: the SoC's CPU for parity calculations when writing, the PCIe bus for throughput, and the SATA controller.

> Note: All the details of my test methodology and benchmarks I ran are documented in [this GitHub issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/162).

Here's how raw disk performance looks:

{{< figure src="./ASUSTOR-vs-Pi-Taco-disk-benchmark.jpeg" alt="Disk benchmarks on ASUSTOR Drivestor 4 Pro vs Raspberry Pi Taco" width="700" height="394" class="insert-image" >}}

The Pi is faster for reads, but the ASUSTOR somehow wipes the floor on writes. Seeing that the Pi board also had space for an NVMe drive, I also [set up bcache in Pi OS](/blog/2021/htgwa-use-bcache-ssd-caching-on-raspberry-pi) in `writeback` mode to give the Pi a boost. And that definitely helped:

{{< figure src="./ASUSTOR-vs-Pi-Taco-disk-benchmark-bcache.jpeg" alt="bcache Disk benchmarks on ASUSTOR Drivestor 4 Pro vs Raspberry Pi Taco" width="700" height="394" class="insert-image" >}}

But NASes have to expose raw storage to a network—and that's an area lower-end NASes often fall short, especially when they try saturating more than a 1 Gbps network connection!

## Network and Samba performance

Indeed, both the Taco and the Drivestor seemed to struggle to saturate a 2.5 Gbps network connection in their default configuration—both using the Realtek driver built into the Linux kernel:

{{< figure src="./ASUSTOR-vs-Pi-Taco-network-bandwidth-kernel.jpeg" alt="RTL8125B NIC performance on 2.5G network" width="700" height="394" class="insert-image" >}}

But I noticed if I switched the Pi over to Realtek's own driver, I could fully saturate the connection:

{{< figure src="./ASUSTOR-vs-Pi-Taco-network-bandwidth-realtek.jpeg" alt="RTL8125B NIC performance on 2.5G network - realtek driver" width="700" height="394" class="insert-image" >}}

I wrote up a [blog post about the driver issue](/blog/2021/check-your-driver-faster-linux-25g-networking-realtek-rtl8125b), but it seems like Realtek's driver has some optimizations that offload a lot of the network packet processing from the CPU, or somehow saves on interrupts by a very significant amount.

But that network throughput doesn't automatically translate to network file copy performance, as demonstrated in my next benchmark:

{{< figure src="./ASUSTOR-vs-Pi-Taco-smb-copy.jpeg" alt="Samba file copy on ASUSTOR Drivestor 4 Pro vs Raspberry Pi Taco NAS" width="700" height="394" class="insert-image" >}}

The benchmark above was a large file copy—the best case scenario. And both the Pi and the Drivestor were very consistent across multiple tests. When you tax a low power SoC with RAID 5 and set it up as the traffic cop between SATA and a 2.5G Ethernet port, it's obvious the performance is more limited than more expensive Intel/AMD options.

Overclocking could help, but honestly, if you want to see supercharged network file copy performance, opt for a more expensive and better endowed NAS.

I know you might be curious how bcache (SSD caching) speeds things up on the Pi—and the answer is _not much_:

{{< figure src="./ASUSTOR-vs-Pi-Taco-smb-copy-bcache.jpeg" alt="Samba file copy with bcache on ASUSTOR Drivestor 4 Pro vs Raspberry Pi Taco NAS" width="700" height="394" class="insert-image" >}}

I was surprised, but I think the reason the numbers are low is because the Pi's BCM2711 chip is hitting some sort of queuing and internal limits with the amount of traffic being routed through it. This chip is just not meant for heavy IO, and tests like this really show it.

It's still fast and reliable, though—and in many cases (especially for smaller copies that fit in RAM), the speeds are much better. Using RAID 1 or RAID 10 would also help greatly with write performance.

## Conclusions

I go into more depth and explanation in [my latest video comparing the ASUSTOR and the Taco](https://www.youtube.com/watch?v=V3jwQzb46Zc), but I'll share the conclusion here that I had in that video:

Based on performance alone, the Raspberry Pi is a worthy alternative to a traditional low-end NAS, like the Drivestor 4 Pro—provided you're okay with getting your hands a _little_ dirty.

{{< figure src="./radxa-taco-raspberry-pi-nas-cm4-hard-drives.jpeg" alt="Radxa Taco CM4 Raspberry Pi NAS board with three hard drives" width="700" height="467" class="insert-image" >}}

You can either go fully custom and configure RAID and Samba or NFS by hand, or rely on a tool like [openmediavault](https://www.openmediavault.org) to get the job done. But in either case, expect to spend more time doing anything more advanced like SSD caching or using ZFS or btrfs.

One of the main reasons people opt for pre-built NASes like those from ASUSTOR is the turnkey NAS software that comes with them—operating systems like ADM (ASUSTOR Data Master) are optimized for end users and don't assume you have deeper knowledge of Linux's storage configuration.

But I do love seeing the Taco and the Drivestor 4 Pro both building around Realtek and Broadcom ARM SoCs (and the Taco could be used with CM4-compatible Rockchip boards, too). Seeing multiple solid ARM NAS products come to market this year shows how mature the ARM ecosystem has come for low to mid-range general computing!

You can buy the [Drivestor 4 Pro](https://amzn.to/3pg7p16) from Amazon, and [Radxa's Taco](https://wiki.radxa.com/Taco) will be available at some point in early 2022.

Check out [my video on these two NAS builds](https://www.youtube.com/watch?v=V3jwQzb46Zc) for a deeper dive.
