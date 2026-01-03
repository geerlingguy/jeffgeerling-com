---
nid: 3346
title: "Waveshare's PoE HAT is the first for Raspberry Pi 5"
slug: "waveshares-poe-hat-first-raspberry-pi-5"
date: 2024-02-06T15:00:27+00:00
drupal:
  nid: 3346
  path: /blog/2024/waveshares-poe-hat-first-raspberry-pi-5
  body_format: markdown
  redirects: []
tags:
  - pi 5
  - poe
  - power over ethernet
  - raspberry pi
  - reviews
  - video
  - waveshare
---

{{< figure src="./pi-5-poe-hat-waveshare.jpeg" alt="Pi 5 PoE HAT Waveshare F" width="700" height="auto" class="insert-image" >}}

Power over Ethernet lets you run both power and networking to certain devices through one Ethernet cable. It's extremely convenient, especially if you have a managed PoE switch, because you get the following benefits:

  - A single cable for power + Ethernet (no need for separate power adapters)
  - No need to have electrical service near every device
  - Simple remote power on/off capability (assuming you have a managed switch)
  - Centralized power management (e.g. one UPS in a rack room covering all powered devices)

I have used the Raspberry Pi PoE and PoE+ HATs for years now, allowing me to have 4 or 5 Raspberry Pi per 1U of rack space, with all wiring on the front side. I also use PoE for cameras around my house, though there are dozens of use cases where PoE makes sense.

The Raspberry Pi, since it only requires 3-10W of power, is an ideal candidate for PoE, assuming you can find a HAT for it.

The Pi 5, however, doesn't have a PoE HAT available, since Raspberry Pi moved the PoE power header down near the moved Ethernet jack (it was right next to the GPIO header for the Pi 3 and 4 generations).

That is, until now—Waveshare introduced the [PoE HAT (F)](https://amzn.to/3OwjZWd), which is their 6th iteration on a Pi PoE HAT.

This HAT comes with a thin but large heatsink (complete with three thermal pads for SoC, PMIC, and memory chip), a built-in always-on fan, and even an auxiliary 12v header supplying up to 2A of power for accessories.

The built-in GPIO 5v connections provide up to 4.5A of power to the Raspberry Pi, which is enough to power the Pi (even overclocked), a PCIe device up to 5W or so, plus one or two USB devices at full current.

{{< figure src="./waveshare-poe-hat-stress-ssd-power-test.jpg" alt="Waveshare PoE HAT Stress and SSD power test" width="700" height="auto" class="insert-image" >}}

To test it, I ran `stress-ng` while copying a 10 GB file between an external USB 3.0 NVMe SSD and an internal PCIe NVMe SSD (using the [Pimoroni NVMe BASE](https://shop.pimoroni.com/products/nvme-base)), and as you can see above, the Waveshare PoE HAT averaged around 5.10V of power to the Pi's 5V power rail throughout.

The lowest I ever saw the 5V rail go was around 5.04V, and there were no voltage warnings from the Pi, nor did it throttle (confirmed using the command `vcgencmd get_throttled`).

## Maximum USB Current

Out of the box, the board did not supply full USB current—it was limited by Pi OS to 600 mA, which is enough for keyboards and other similar low-power peripherals, but not nearly enough to initialize a bus-powered SSD.

I had to edit `/boot/firmware/config.txt` and add the following line to override the Pi's USB current limiter:

```
usb_max_current_enable=1
```

Doing so allows the Pi to pass through up to 1.6A of current to the USB ports.

## Other observations

For other thoughts on this HAT, please check out [this GitHub issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/597) as well as today's video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/OEctB0HOpZ8" frameborder='0' allowfullscreen></iframe></div>
</div>
