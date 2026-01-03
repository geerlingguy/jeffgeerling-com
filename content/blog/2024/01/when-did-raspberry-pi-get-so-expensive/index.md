---
nid: 3339
title: "When did Raspberry Pi get so expensive?"
slug: "when-did-raspberry-pi-get-so-expensive"
date: 2024-01-23T15:00:38+00:00
drupal:
  nid: 3339
  path: /blog/2024/when-did-raspberry-pi-get-so-expensive
  body_format: markdown
  redirects: []
tags:
  - computer
  - intel
  - n100
  - nuc
  - pc
  - raspberry pi
  - video
  - youtube
---

{{< figure src="./gmktec-n100-pc-raspberry-pi-5.jpeg" alt="Raspberry Pi 5 and N100 GMKtec Nucbox G3" width="700" height="auto" class="insert-image" >}}

I just bought this N100-based Intel x86 mini PC (_brand new_), and it was cheaper than an almost equivalent—but slower—Raspberry Pi 5.

This GMKtec mini PC is called the [Nucbox G3](https://amzn.to/4brupjC), and it comes with an Intel Alder Lake N100 4-core CPU, 8GB of RAM, a 256 GB M.2 NVMe SSD, and Windows 11 Pro—and mine cost just $131, after a couple coupons.

That's... a lot of computer for a very good price. But the Raspberry Pi—the famous "$35 computer", should be well below that... right?

Well, I bought all the parts required to build a Pi 5 to the same spec—including the adapters and parts to assemble it into one small unit—and it turns out... the Pi is _more expensive_. And _slower_.

The Pi 4 still starts at $35 (for a 1 GB model), but the Pi 5 starts at $60 (for 4 GB) and climbs to $80 for the maximum 8 GB model.

But if you want to use an NVMe SSD, add on $20 for a HAT to adapt the new PCIe jack to an M.2 slot. And to power it, you need a $12 5v 5A power adapter (though the slightly-cheaper 3A adapter works in most circumstances). And throw in a $7 Active Cooler since the fan included with the official Pi case won't fit if you add an M.2 HAT to the top. Plus, you probably need a $5 micro HDMI to HDMI adapter if you want to plug the Pi into a monitor.

| [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) | [GMKtec Nucbox G3](https://amzn.to/4brupjC) |
| --- | --- |
| 4x Arm Cortex A76 CPU cores | 4x Intel Alder Lake CPU cores |
| Broadcom VideoCore VII GPU | Intel UHD Graphics |
| 8 GB LPDDR4x RAM | 8 GB DDR4 RAM |
| 128 GB 2242 M.2 NVMe SSD | 256 GB 2280 M.2 NVMe SSD |
| Pineberry Pi HatDrive! M.2 HAT required | (Additional 2242 slot available) |
| Extra 27W power supply required | Power adapter included in box |
| Extra micro HDMI to HDMI cable required | HDMI cable included in box |
| Extra case + cooling solution required | Prebuilt, fully assembled |
| **$147** | **$131** |

The Pi works fine as a tiny Linux desktop, but add everything together—and in my case, the total runs up to around $140-150! More expensive than the prebuilt N100 PC _with Windows 11 Pro_!

I made a video comparing the entire process of purchasing, setting up, and using the Pi and the N100 tiny PC, and you can view it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/jjzvh-bfV-E" frameborder='0' allowfullscreen></iframe></div>
</div>

The Pi does have some redeeming values, which offset the sticker shock:

  - It exposes 40 GPIO pins for easy interfacing with tons of pre-built HATs or electronics projects
  - It has two CSI/DSI connectors for high speed display and camera interfaces (not just USB for webcams or expensive HDMI transcievers)
  - The volume of the Pi build is less than 1/4th that of the PC
  - The Pi runs on 3-4W idle, or 8-12W maximum, with a measured efficiency of around 130 'geekbenches per watt' (compared to about 95 for the mini PC, burning through 28W of power maximum)
  - The Pi can be adapted to run on PoE+ power, so you can provide networking _and_ power over one cable (though... there are a couple [N100-based mini PCs that have this feature](https://liliputing.com/minisforum-s100-n100-is-a-pocket-sized-alder-lake-n-pc-with-power-over-ethernet-support/) now!)

Besides, Raspberry Pi still includes a 1G and 2G space on the Pi 5 board—if we see variants with less RAM, the Pi 5 may yet push down towards a $40 starting price (I really hope they can release a 2 GB Pi 5 for $40, once they get through their initial production batches).

{{< figure src="./gmktec-n100-pc-raspberry-pi-5-side.jpeg" alt="Raspberry Pi 5 and N100 GMKtec Nucbox G3 - Side" width="700" height="auto" class="insert-image" >}}

But even accounting for all that, you will likely have to pay shipping on at least two or three separate orders, because not _everything_ is available through one retailer right now. So if you really want the best Raspberry Pi 5 desktop setup, realistically you're going to pay over $150.

The Pi 4 is still around, and [in vast quantity now](https://rpilocator.com), starting at $35. And if you don't need much horsepower, it makes a fine little server for small tasks—running Home Assistant, monitoring a garden, setting up a remote sensor. Or you can probably put an ESP32 or Pico W on the task, if you don't need full Linux support.

So the Pi 5—it's in a smaller niche currently. It's faster than a Pi 4, at the expense of a little more power draw, and a lot more money. It's priced out of many 'tiny homelab' or 'mini desktop' scenarios, at least when compute efficiency and total build volume aren't your primary concerns. And it's lack of faster Ethernet means it has more limited networking uses compared to a tiny PC like the Nucbox G3 with it's 2.5 Gbps chipset.

I don't think the Pi 5 will become a smash hit like the Pi 4 was[^1] until they release a lower-cost variant at $40. A potential Compute Module 5 has more legs, as it will make integrating a tiny, energy-efficient computer into more exotic and unique use cases that much easier.

The big question is whether Intel will continue designing better low-end chips like the N100—they've certainly upped their game, but they're still not quite as efficient or easy to cool as Arm SBC equivalents like the RK3588 or BCM2712.

[^1]: Well... besides the fact they've probably sold over half a million units so far!
