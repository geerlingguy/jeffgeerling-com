---
nid: 3120
title: "Uptime Lab's CM4 Blade adds NVMe, TPM 2.0 to Raspberry Pi"
slug: "uptime-labs-cm4-blade-adds-nvme-tpm-20-raspberry-pi"
date: 2021-08-04T14:01:28+00:00
drupal:
  nid: 3120
  path: /blog/2021/uptime-labs-cm4-blade-adds-nvme-tpm-20-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - blade
  - cm4
  - compute module
  - raspberry pi
  - uptime lab
  - video
  - youtube
---

A few weeks ago, I received two early copies of [Uptime.Lab](https://www.instagram.com/uptime.lab/)'s CM4 Blade.

{{< figure src="./uptime-lab-cm4-blade.jpg" alt="Uptime Lab's Raspberry Pi CM4 Blade Computer with NVMe SSD" width="700" height="223" class="insert-image" >}}

The Blade is built for the [Raspberry Pi Compute Module 4](https://www.raspberrypi.org/products/compute-module-4/), which has the same processor as the Pi 4 and Pi 400, but without any of the built-in IO ports. You plug the CM4 into the Blade, then the Blade breaks out the connections to add some interesting features.

A 1U rackmount enclosure is in the works, and 16<sup>1</sup> of these boards would deliver:

  - 64 ARM CPU cores
  - up to 128 GB of RAM
  - 16 TB+ of NVMe SSD storage

That's assuming you can find 8 GB Compute Modules—they've been out of stock since launch almost a year ago, and even smaller models are hard to come by. More realistically, with 4 GB models, you could cram in 64 GB of total RAM.

Having the capacity spread across multiple nodes means you'd need to use something like Kubernetes to coordinate workloads, but this is an interesting alternative to something like an [Ampere Altra](https://amperecomputing.com), if you have parallelizable workloads and need as many 64-bit ARM compute cores as possible.

Each blade has the following features:

  - M.2 M-key slot for NVMe SSDs
  - TPM 2.0 module
  - Integrated PoE+ with Gigabit Ethernet
  - A PWM fan header
  - UART debug header and partial GPIO header for RTC or Zymkey 4i
  - 1x HDMI, USB 2.0, and USB-C for eMMC flashing
  - microSD card slot for Lite CM4 modules
  - GPIO-controlled ID LED and SSD activity LED

I have a full video walkthrough of the board on my YouTube channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/zH9GwYZu_aE" frameborder='0' allowfullscreen></iframe></div>
</div>

I tested the onboard NVMe drive, and was able to get up to **415 MB/sec** sequential reads, which is right at the limit of the Pi's single PCIe Gen 2.0 lane.

I was also able to communicate with the TPM 2.0 chip after enabling it in `/boot/config.txt` with the following configuration line:

```
# Enable TPM module
dtoverlay=tpm-slb9670
```

I used Infineon's [Embedded Linux TPM Toolbox 2](https://github.com/infineon/eltt2) with the command `sudo ./eltt2 -g` to confirm I could communicate with the module, and it returned valid data.

{{< figure src="./infineon-tpm.jpg" alt="Infineon TPM 2.0 embedded chip" width="599" height="345" class="insert-image" >}}

But don't get your hopes up for secure boot on the Pi—it would need support in the Pi's bootloader... right now it's not supported. Since the bootloader is closed source, I wouldn't count on TPM support being added anytime soon, especially since this is the first Pi device I've seen with a TPM 2.0 chip! You can still use it for other secure computing features and cryptography storage, though.

The board gets fairly warm, likely due to the overhead of the PoE+ power conversion (which consumes 6-7W on its own!), so active cooling is probably a good idea—the plan is to have an official 1U rackmount case with integrated Noctua 40mm fans at the rear, plugged into the Blade's 4-pin fan header.

Ivan ([@Merocle](https://twitter.com/Merocle), who posts to [@Uptime.Lab](https://www.instagram.com/uptime.lab/)) already has a short 10" rack case design, which holds 8 boards, and is working on the full 19" version:

{{< figure src="./uptime-lab-blade-rackmount-full-portrait.jpg" alt="Uptime Lab's blade servers in 1U 10 inch mini desktop rack" width="600" height="450" class="insert-image" >}}

His plan is to launch a Kickstarter for the board, but until then, the best way to follow along is to [subscribe to the Uptime.Lab mailing list for a Kickstarter launch notification](https://uplab.us6.list-manage.com/subscribe?u=fdbd31aa8fdf802b1edc668f9&id=2de992b8de), and [follow @Uptime.Lab on Instagram](https://www.instagram.com/uptime.lab/).

<hr>

<sup>1</sup> Ivan [stated](https://twitter.com/Merocle/status/1422931604855566339) the final 1U rack enclosure could support up to 20 or even 22 blades!
