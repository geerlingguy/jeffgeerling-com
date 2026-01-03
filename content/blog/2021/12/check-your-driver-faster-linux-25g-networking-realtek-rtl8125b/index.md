---
nid: 3160
title: "Check your driver! Faster Linux 2.5G Networking with Realtek RTL8125B"
slug: "check-your-driver-faster-linux-25g-networking-realtek-rtl8125b"
date: 2021-12-21T20:45:10+00:00
drupal:
  nid: 3160
  path: /blog/2021/check-your-driver-faster-linux-25g-networking-realtek-rtl8125b
  body_format: markdown
  redirects:
    - /blog/2021/check-your-driver-faster-25g-networking-realtek-rtl8125b
aliases:
  - /blog/2021/check-your-driver-faster-25g-networking-realtek-rtl8125b
tags:
  - asustor
  - benchmarking
  - drivers
  - drivestor
  - ethernet
  - iperf3
  - linux
  - network
  - nic
  - performance
  - raspberry pi
  - realtek
---

Since the Raspberry Pi Compute Module 4 was introduced last year, I've been testing a [variety of PCI Express NICs](https://pipci.jeffgeerling.com/#network-cards-nics-and-wifi-adapters) with it. One of the main types of NIC I'm interested in is cheap 2.5 Gigabit Ethernet adapters.

2.5 Gigabits is about the highest reasonable bandwidth you can get through the PCI Express Gen 2.0 x1 lane on the Raspberry Pi, and it's also a lot more accessible than 10 Gigabit networking, especially for home users who might already have Cat5e runs that they are loathe to swap out for Cat6 or better cabling.

In my testing, [besides discovering that not all 10 Gbps SFP+ transceivers are created equal](/blog/2021/ethernet-was-slower-only-one-direction-on-one-device), I found out that when it comes to performance, the Linux driver you're using matters—a _lot_.

And as a stark illustration of this point, I recently pitted an [ASUSTOR Drivestor 4 Pro NAS against a Raspberry Pi 'Taco' NAS](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/268). Both of these devices use the popular [Realtek RTL8125B](https://www.realtek.com/en/component/zoo/category/network-interface-controllers-10-100-1000m-gigabit-ethernet-pci-express-software) chip, and _both_ of them were reporting underwhelming `iperf3` bandwidth results:

{{< figure src="./iperf3-bandwidth-kernel-driver.jpg" alt="iperf3 bandwidth - kernel driver" width="700" height="394" class="insert-image" >}}

The maximum throughput was eerily similar, just under 1.9 Gbps. And worse, I noticed when using devices through a PCI Express switch on the Pi, like a SATA RAID array, the network throughput took a hit, down to 1.51 Gbps on the Pi.

I wondered if the driver might've seen some improvements in later revisions of the Linux kernel, so I recompiled the kernel using the 5.15.x source:

{{< figure src="./realtek-ethernet-driver-menuconfig.png" alt="menuconfig - Realtek 2.5G network driver in Linux kernel source tree" width="600" height="316" class="insert-image" >}}

That made no difference—in fact, the results started to have more jitter in them, so I decided that avenue wasn't worth pursuing further.

So next, I downloaded the driver directly from Realtek's website, and installed version `9.007.01`:

```
$ sudo apt-get install -y raspberrypi-kernel-headers
$ tar vjxf r8125-9.007.01.tar.bz2
$ cd r8125-9.007.01/
$ sudo ./autorun.sh
```

I re-ran my benchmarks, and wouldn't you know? I'm able to get the full 2.35 Gbps of real-world throughput through the card—regardless of other traffic on the PCIe bus!

{{< figure src="./iperf3-bandwidth-realtek-driver.jpg" alt="iperf3 bandwidth - realtek driver" width="700" height="394" class="insert-image" >}}

So the moral of the story seems to be: if you're not seeing the performance you expect, see if the vendor's driver is better than what's in the kernel tree.

_Many_ vendors take an upstream-first approach, where they make sure any driver optimizations make their way to the kernel quickly... but not all. I'm not sure how the discrepancy is so big, though, in this case. It looks like [`8125B` support was only added a year and a half ago](https://github.com/torvalds/linux/commit/0439297be95111cf9ef5ece2091af16d140ce2ef#diff-3a9fe109aabf89a54957b2b641cfc3b5604150bfd486a04cc1aee43b0b3da5e1), and only a few chip-specific commits have been added since.

I have to wonder if maybe since far fewer Linux users have 2.5G-capable networks, these kinds of performance issues aren't discussed as much?

I confirmed with ASUSTOR that their current Drivestor 4 Pro software is running the driver from the kernel, and not the Realtek vendor driver. No word yet on if that could change—but if so, it may be able to unlock more performance from their value-lineup of 2.5G NASes!

For all my debugging details, check out my GitHub issue [NAS Comparison - ASUSTOR Drivestor 4 Pro vs Pi CM4](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/162).
