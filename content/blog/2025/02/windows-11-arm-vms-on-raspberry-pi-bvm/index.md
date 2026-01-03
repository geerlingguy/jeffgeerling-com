---
nid: 3449
title: "Windows 11 Arm VMs on a Raspberry Pi, with BVM"
slug: "windows-11-arm-vms-on-raspberry-pi-bvm"
date: 2025-02-28T20:45:29+00:00
drupal:
  nid: 3449
  path: /blog/2025/windows-11-arm-vms-on-raspberry-pi-bvm
  body_format: markdown
  redirects: []
tags:
  - kvm
  - linux
  - microsoft
  - open source
  - qemu
  - raspberry pi
  - virtualization
  - windows
---

With the release of a [Windows 11 for Arm ISO](https://www.microsoft.com/en-gb/software-download/windows11arm64), it's easier than ever to get an officially-supported install of Windows on many different Arm PCs—now including a Raspberry Pi.

The [Windows on R](https://worproject.com/) seems like it has run out of steam, as many open source initiatives do, after years of being bludgeoned with support requests being the only way to really get Windows going on a Pi.

But GitHub user (and _high-schooler_) Botspot just emailed me his [BVM](https://github.com/Botspot/bvm) project, short for 'Botspot Virtual Machine'.

{{< figure src="./bvm-install-windows-11-raspberry-pi.jpg" alt="BVM installing Windows 11 on a Raspberry Pi" width="700" height="394" class="insert-image" >}}

This project includes a handy CLI and GUI utility to configure a Windows 11 VM using QEMU/KVM. I'll let you [peruse the README](https://github.com/Botspot/bvm) for full specs, but the most important bits for most people:

  - Setup is streamlined (and I've tested it successfully on a 4GB and 8GB Pi 5)
  - It passes through network (WiFi and wired) and audio so that should all work out of the box
  - `connect` mode allows filesystem passthrough, so you can share files between Linux and the VM
  - USB passthrough is coming soon (hopefully!)
  - GPU passthrough is not working—but that's on Microsoft and Raspberry Pi/Broadcom, right now you can't use any GPUs without drivers, and there are precious few drivers for GPUs in Windows on Arm!

To that last point, Raspberry Pi actually maintains a [Board Support Package for Windows 10](https://github.com/raspberrypi/windows-drivers) with certain drivers included. Could they someday include a driver for the VideoCore GPU? Not sure, but it'd be quite awesome if they had full hardware-accelerated Windows 11 support.

I ran through the entire setup process on a Pi—two times in fact—and it's as easy as it says in the README. The GUI could probably be streamlined a little further, but right now it breaks out each step into its own operation. That's probably useful in case anything goes wrong, for support you can just say "Step 3 failed with this message" and that narrows it down a lot more, resulting in fewer GitHub issues with 1,000s of lines of log output!

Here's a video of the entire process on a Pi 5, end-to-end:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/mkfILjKJ8nc" frameborder='0' allowfullscreen></iframe></div>
</div>

I ran Geekbench for arm64 within Windows and compared it to a couple runs on the Raspberry Pi running Linux natively, and the results surprised me:

| Scenario | Single Core | Multicore |
| --- | --- | --- |
| [Windows 11 VM](https://browser.geekbench.com/v6/cpu/10797191) | 782 | 1736 |
| [Pi 5 - Launch Day Firmware](https://browser.geekbench.com/v6/cpu/2808487) | 748 | 1507 |
| [Pi 5 - Latest Firmware](https://browser.geekbench.com/v6/cpu/9202663) | 899 | 2169 |

If you want to give it a try, it apparently runs on Pi 4 as well, and it's recommended you have a Pi model with at least 4 GB of RAM.
