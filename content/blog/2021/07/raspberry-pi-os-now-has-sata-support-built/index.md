---
nid: 3119
title: "Raspberry Pi OS now has SATA support built-in"
slug: "raspberry-pi-os-now-has-sata-support-built"
date: 2021-07-30T21:11:39+00:00
drupal:
  nid: 3119
  path: /blog/2021/raspberry-pi-os-now-has-sata-support-built
  body_format: markdown
  redirects: []
tags:
  - hard drive
  - linux
  - nas
  - open source
  - raspberry pi
  - sata
  - ssd
  - video
  - youtube
---

After months of [testing various SATA cards](https://pipci.jeffgeerling.com/#sata-cards-and-storage) on the Raspberry Pi Compute Module 4, the default Raspberry Pi OS kernel [now includes SATA support out of the box](https://github.com/raspberrypi/linux/pull/4256).

{{< figure src="./sata-ssd-raspberry-pi-cm4.jpeg" alt="SATA card and Samsung SSD with Raspberry Pi Compute Module 4 IO Board" width="661" height="372" class="insert-image" >}}

In the past, if you wanted to use SATA hard drives or SSDs and get native SATA speeds, and be able to RAID them together for redundancy or performance, you'd have to recompile the Linux kernel with SATA and AHCI.

Sure you could always use hard drives and SSDs with SATA to USB adapters, but you sacrifice 10-20% of the performance, and can't RAID them together, at least not without some hacks.

> There's a video version of this post: [SATA support is now built into Raspberry Pi OS!](https://www.youtube.com/watch?v=ZSx1BRwz1bs)

Recompiling the kernel isn't rocket science, and I even built a [cross-compile environment to make it easy](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile). But it _is_ annoying, and takes some time, and you have to keep compiling the kernel if you want to keep your Pi up to date.

But this month, Raspberry Pi OS finally has built-in support for almost all PCI Express SATA adapters. All you have to do is run `sudo apt upgrade` and you'll have it.

That means anyone with a Compute Module 4 can plug in a SATA card, and plug in hard drives or SSDs, and they should just work, assuming you have power to the drives.

I'm especially excited about this because one of the big motivations for adding support came out of my testing efforts for the [Pi PCI Express card website](https://pipci.jeffgeerling.com), and the code that added support was in [my first ever PR to the Raspberry Pi Linux kernel](https://github.com/raspberrypi/linux/pull/4256).

And to think, _less than a year ago I had never compiled a Linux kernel before_!

Native SATA support means we can use things like [OpenMediaVault](https://www.openmediavault.org) to build RAID NASes with Raspberry Pis, without having to maintain a custom kernel or do any special setup work.

And my main takeaway is it's not as daunting as I thought to write a patch for the Linux kernel (though to be fair I didn't have to go through the kernel mailing list, since my patch went into the Pi OS forked kernel tree).

And I have to credit the humble Raspberry Pi for getting me to this point—because Pis are cheap and re-imaging them is easy, it's less daunting because I know a mistake won't cost me much.

I think a lot of people used to big hulking desktops and servers don't understand how liberating it is to use a tiny hobby computer like a Pi.

One thing you _can't_ do yet is boot the Pi from a SATA drive (see [this issue](https://github.com/raspberrypi/firmware/issues/1653)). You can boot from USB, microSD, eMMC, or [even NVMe on the latest Pi OS](/blog/2021/raspberry-pi-can-boot-nvme-ssds-now), but currently the Raspberry Pi bootloader doesn't scan SATA devices for booting. At least not yet.
