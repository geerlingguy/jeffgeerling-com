---
nid: 3410
title: "3rd Party PoE HATs for Pi 5 add NVMe, fit inside case"
slug: "3rd-party-poe-hats-pi-5-add-nvme-fit-inside-case"
date: 2024-10-10T14:01:22+00:00
drupal:
  nid: 3410
  path: /blog/2024/3rd-party-poe-hats-pi-5-add-nvme-fit-inside-case
  body_format: markdown
  redirects: []
tags:
  - hat
  - nvme
  - poe
  - power over ethernet
  - raspberry pi
  - reviews
  - ssd
  - video
---

Today I published a video detailing my testing of three new Raspberry Pi HATs—these HATs all add on PoE+ power _and_ an NVMe SSD slot, though the three go about it in different ways.

You can watch the video for the full story (embedded below), but in this post I'll go through my brief thoughts on all three, and link to a few other options coming on the market as well.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/x9ceI0_r_Kg" frameborder='0' allowfullscreen></iframe></div>
</div>

## GeeekPi P33 M.2 NVMe M-Key PoE+ HAT

{{< figure src="./52pi-p33-geeekpi-poe-nvme-hat.jpg" alt="52Pi P33 GeeekPi PoE+ NVMe HAT for Pi 5" width="700" height="auto" class="insert-image" >}}

This HAT is compatible with all standard NVMe sizes up to 2280, and has holes cut into the PCB to allow airflow through, under the NVMe, into the Raspberry Pi Active Cooler fan—which is included in the box (a nice touch)!

It provides 5.1V at 4.5A power output to the Pi, and comes with a passthrough GPIO header, so you can stack another HAT on top. There are also a few convenient pins on top for additional 3.3V, 5V, and 12V power outputs, though I didn't test these.

The board fits within the Pi 5's own PCB footprint, but because of how the 2280 slot is positioned, the FFC connector placement is a little strange (it's under the NVMe drive, and results in a slightly awkward experience plugging it in).

When running it on the Pi, I heard no coil whine at all (a problem that plagues some PoE devices), and the hottest IC never went beyond about 50°C.

There are a few downsides:

  - The way the transformer is mounted on top makes this solution a bit tall
  - There are only power and activity LEDs; there's no separate indication of PoE power being present.
  - When I shut down the Pi in software, the PoE HAT seemed to reset its power line, causing the Pi to immediately power back on—the same thing happens if I press the power button on the Pi. 52Pi support said there are some EEPROM settings you can change to make the power behavior work, but I thought I'd call this out since none of the other HATs I tested had this issue.

You can buy it here: [52Pi/GeeekPi P33 NVMe + PoE+ 2280 HAT](https://amzn.to/3BETcmP) (affiliate link)

## HackerGadgets PoE + NVMe HAT

{{< figure src="./hackergadgets-poe-nvme-hat-inside-pi-5-case.jpg" alt="HackerGadgets PoE+ NVMe HAT inside Pi 5 case" width="700" height="auto" class="insert-image" >}}

This HAT has a few unique features. It includes a separate USB-C PD circuit that allows powering the Pi at full 25W power using more standard USB-C power supplies like those that come with laptops—it will bring 9V and 12V supplies down to the 5V the Pi 5 needs.

It's compatible with 2230 and 2242-size SSDs, and has a cutout in the PCB that's the right size for the Raspberry Pi case fan—it even includes two screws to mount the case fan directly onto the HAT PCB.

Why does it do that? Because this is the first (and only, so far) PoE + NVMe HAT to support mounting directly inside the official Raspberry Pi 5 Case.

The fan cutout is also nearly aligned with the Active Cooler's fan, so you could use it with that instead, if you want (it's fan is a bit quieter than the Case fan).

A further downside to the Case fan is one of its screws touches the tiny heatsink that comes with the Pi 5 Case, so you can't really use that heatsink along with this HAT and the fan included with the Case.

_Outside_ of the Pi Case, it provides a solid 5V at 4.8A, with temperatures well-controlled (I tested mainly with the Active Cooler). The hottest IC (which is around 50°C) is right next to the fan cutout, which should help with cooling if it does get even hotter.

There is a very faint coil whine audible from a foot or two away. Not annoying, but noticeable if your ears can hear that range of frequencies.

The LED's on the board are a nice touch, indicating Pi power and activity, as well as whether there is power supplied by either USB-C PD or PoE. The included FFC cable is impedance-matched, so it handles Gen 3 speeds well, but the mounting is ever-so-slightly misaligned, which made plugging it in a tiny bit more difficult than it should be.

### (Pi 5) Case Closed

{{< figure src="./hackergadgets-inside-pi-5-case-temperature-graph.jpg" alt="HackerGadgets PoE+ NVMe HAT running inside Pi 5 case temperatures" width="700" height="auto" class="insert-image" >}}

When you enclose this thing inside the Pi 5 case, though, it's not amazing. I wouldn't recommend this configuration as it basically turns into an easy-bake oven, as displayed in the temperature graph above, where I ran `stress-ng` for 10 minutes to see how well cooling worked.

It _looks_ great, but the Pi 5 case itself is terrible for airflow, and that's really highlighted in my testing. And it's made even worse by the fact you can't stick the tiny heatsink on top of the Pi's SoC to help it dump heat a little better.

With this HAT and the case closed up, the fan has to run almost continuously, whereas running outside a case, or in a case with more open airflow, it will only run the fan under load in most environments.

The case problems aren't really caused by the HackerGadget's HAT, though. And this mounting capability does make it more flexible in use, so I'm still happiest with this design overall, of the three I tested. I just won't run mine inside a Pi 5 Case!

You can buy it here: [HackerGadgets PoE + NVMe HAT](https://hackergadgets.com/products/nvme-and-poe-hat-for-raspberry-pi-5)

## n-fuse PoE HAT with mini PCIe and M.2

{{< figure src="./n-fuse-poe-hat-nvme-pi-5-front.jpg" alt="n-fuse PoE + NVMe HAT on Pi 5" width="700" height="auto" class="insert-image" >}}

n|fuse has a series of PoE HATs that support M.2 B/E/M-key, or even mini PCIe, for all kinds of different add-ons.

It is the lowest-profile design—so low-profile it necessitates breaking a few fins off the Active Cooler! (A procedure recommended in the install guide.)

It has cutouts for the Active Cooler fan airflow, and for the CSI/DSI connectors on the Pi. It supplies 5A or 25W of power delivery, as long as you have active cooling, but the PCIe FFC it ships with is the white non-impedance-matched variety, so you may have trouble at PCIe Gen 3 speeds with some devices. Better to stick to the default Gen 2 if you need stability with this HAT.

My favorite feature is a set of three debug LEDs, "Type 1", "Type 2", and "BT", indicating [what type of PoE power your Pi is getting](https://planetechusa.com/what-you-need-to-know-about-the-design-of-an-ieee-802-3bt-powered-device/). My Aruba PoE+ injector supplies Type 2 BT, meaning I'm getting the full 25.5 Watts of power to the Powered Device (the Pi).

But those LEDs were part of the feature I was most confused by: _thermals_. The main inductor reached 60°C, and the LEDs were about the same! There weren't any ICs on the other side of the board, so it seems maybe there's a lot of current running through the little LED resistors? It was a strange thing to see on the thermal camera; definitely don't touch the LEDs while in use. When I asked, n|fuse said the temperatures were within spec.

Shutdown behavior worked as expected, and there was no coil whine at all—but that leads me to two other issues I have with this board.

First, a couple of the little circuits touch the top of one of the Active Cooler fan screws, though not on any solder joints. It's just a bit annoying since vibration could cause issues over time.

But there was a bigger issue...

### Feeling isolated

{{< figure src="./n-fuse-poe-hat-nvme-pi-5-back.jpg" alt="n-fuse PoE + NVMe HAT lacking an isolation transformer" width="700" height="auto" class="insert-image" >}}

There's no isolation transformer on this board. I asked n|fuse about it and they said "The design is not isolated. The advantage of our design is certainly that is supports PoE .bt and is pretty efficient."

Now in general, removing the isolation transformer won't cause an issue. But it _can_ cause problems in some cases, probably even blowing up your Pi in strange fault conditions or with wiring running through high-EMI environments, so I generally don't trust a PoE device without any isolation.

[There's a reason the PoE standard requires isolation](https://electronics.stackexchange.com/q/488550), and that's to prevent things like frying the CPU in the powered device. Aside: while research PoE isolation requirements, I was nerd-sniped into reading [this entire paper on the topic](http://www.embeddedpowerlabs.com/Downloads/APEC_2006_PoE_Electrical_Isolation_Requirements.pdf).

n|fuse mentioned better efficiency, and comparing it to the HackerGadgets board, the Pi did use 0.9W less power at idle. That's close to the margin of error for my smart outlet, so I can't say anything definitive, but it does seem that removing the isolation transformer may have helped them achieve a little better power efficiency.

You can buy it here: [n-fuse Power over Ethernet HAT with M.2 Slot](https://n-fuse.co/devices/SBCPoE-RPi-Power-over-Ethernet-Hat-for-Raspberry-Pi-5-with-mPCIe-Slot-m2-slot.html)

## Other PoE+ HATs

There are a bunch of other HATs coming out too. Mcuzone makes [two different size HATs](https://www.aliexpress.us/item/3256806343314127.html) for both size drives.

And Waveshare added two _more_ PoE HAT's to _their_ lineup. One [has an M.2 slot](https://www.waveshare.com/poe-m.2-hat-plus.htm), and the other one is [a tiny model G](https://www.waveshare.com/PoE-HAT-G.htm). This one looks like it also lacks an isolation transformer, so I'm not that excited about it.

But more will come. Maybe Raspberry Pi'll launch their own, someday! But I'm not gonna hold my breath for that.

I didn't see what happens when backfeeding USB-C power. Some of these designs might behave better or worse in that condition. What I typically recommend is you _don't_ try plugging in USB-C power when you one of these installed. Some HATs like the P33 from 52Pi [explicitly tells you _not_ to](https://52pi.com/products/p33-m-2-nvme-2280-poe-hat-extension-board-for-raspberry-pi-5).

I also didn't push each of these to their maximum current ratings. I typically would just run an NVMe SSD on these HATs, and maybe a medium power USB device like an SDR.

But bottom line, even if Raspberry Pi never releases their own design, I think we're pretty well covered at this point.
