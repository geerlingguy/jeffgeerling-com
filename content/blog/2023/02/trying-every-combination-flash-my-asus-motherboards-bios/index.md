---
nid: 3272
title: "Trying every combination to flash my ASUS motherboard's BIOS"
slug: "trying-every-combination-flash-my-asus-motherboards-bios"
date: 2023-02-15T01:57:03+00:00
drupal:
  nid: 3272
  path: /blog/2023/trying-every-combination-flash-my-asus-motherboards-bios
  body_format: markdown
  redirects:
    - /blog/2023/trying-every-possible-combination-update-my-motherboards-bios
aliases:
  - /blog/2023/trying-every-possible-combination-update-my-motherboards-bios
tags:
  - amd
  - asus
  - bios
  - build
  - flash
  - motherboard
  - pc
  - usb
---

> **tl;dr**: Use an [old-fashioned USB 2.0 flash drive](https://amzn.to/3E4IAwc), format it FAT32, download the firmware, make sure it's named correctly, and use the motherboard's 'BIOS Flashback' option after powering off the computer.

This past week, I devoted far too much time to the task of updating my brand new motherboard's BIOS.

It started with a combo deal from Micro Center: a [ASUS ROG Strix B650E-F Gaming WiFi motherboard](https://amzn.to/3lrwLti), a [Ryzen 9 7900x](https://amzn.to/3YMsNKg) CPU, and a [G.Skill Flare X5 Series 32GB DDR5-6000 memory kit](https://amzn.to/3YDkr8g), all for $599. Quite a beefy upgrade for the main PC I use to compile code and do random Linux-y tasks.

{{< figure src="./4090-amd-7900x-motherboard-build-on-desk-open-benchtable-bc1.jpeg" alt="Nvidia RTX 4090 on AMD 7900x platform" width="700" height="394" class="insert-image" >}}

So I popped everything together, made sure it benchmarked as expected, tested an Intel Arc A750 in preparation for testing on a Raspberry Pi, and then decided the 7900x's egregious power consumption wasn't to my liking—the thing **idled over 90W**, and would eat up over 285W while compiling Linux!

I wanted to enable [AMD's 'Eco' mode](https://community.amd.com/t5/gaming/ryzen-7000-series-processors-let-s-talk-about-power-temperature/ba-p/554629), which limits the TDP from the stock 170W to either 105W or 65W. And in my own benchmarking (which happened later on, but I'm including the data here because it's kinda insane), **the CPU got about 96% of its 170W performance when I limited it to 105W**. And at that level, it idled at 45W and maxed out at 206W. Much better.

## Updating the BIOS - Not so EZ

Knowing from past experience how BIOS Flashback can be flaky, I decided to try ASUS' 'EZ Flash' UI.

First I downloaded the [latest BIOS file for the B650E-F](https://rog.asus.com/motherboards/rog-strix/rog-strix-b650e-f-gaming-wifi-model/helpdesk_bios/) from ASUS' website, and expanded the zip file.

Then I ran the included file renamer tool, and copied the renamed BIOS file over to my flash drive.

I then rebooted the PC, entered the BIOS settings, went to Advanced settings, went to the Tools, and entered ASUS's EZ Flash 3 menu.

From there, I could see the BIOS and select it, but when I did, the screen would go to 'Processing', a status bar would start filling, then every time, the PC would just shut down, then try rebooting, and when it did, after the orange DRAM LED lit for a bit, the red CPU LED would light up and stay lit until I removed power from the motherboard.

I tried this with three different flash drives (two SanDisk USB 3.0 models, and one generic [Alihelan USB 2.0 drive](https://amzn.to/3YJ7VUo)), and none of them worked with EZ Flash—all had the same weird 'immediate shutdown' issue.

So next I tried each one with BIOS Flashback, where you make sure the USB drive is attached to a specific port on the motherboard, shut down the computer, and press and hold a 'BIOS Flashback' button nearby until the process begins.

Well, with the two USB 3.0 drives I was testing (both formatted as FAT32), I got three blinks, then the LED stayed lit—an indication the process did not succeed.

So I finally tried again with the USB 2.0 drive, and lo and behold, the thing finally worked—and now in BIOS I have options for setting the AMD Eco modes for lower TDP/energy consumption at basically the same performance.

I don't know how motherboard BIOS updates are still so flaky after all these years, but I guess it's better than requiring a USB-to-TTL device and some terminal hacking to flash it like you do on many ARM SBCs!

Regardless, I'm finally confident I can upgrade my Ryzen 5 5600x system to this new Ryzen 7 7900x, and I won't have to take out a second mortgage just to afford my electric bill.
