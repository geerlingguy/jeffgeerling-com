---
nid: 3133
title: "Getting a Raspberry Pi to boot after cutting it in half"
slug: "getting-raspberry-pi-boot-after-cutting-it-half"
date: 2021-10-20T14:00:26+00:00
drupal:
  nid: 3133
  path: /blog/2021/getting-raspberry-pi-boot-after-cutting-it-half
  body_format: markdown
  redirects: []
tags:
  - boot
  - debugging
  - raspberry pi
  - serial
  - uart
  - video
  - videocore
  - youtube
---

This blog post starts with the question: _If I cut the ports off a Raspberry Pi 4 model B, will it still work?_

{{< figure src="./cut-raspberry-pi-4-model-b.jpeg" alt="Cut Raspberry Pi 4 model B" width="600" height="400" class="insert-image" >}}

My early conclusion? _Sorta_.

With most Raspberry Pi generations, there is a full-featured model B, and a smaller, trimmed-down model A. The Pi 4 never had a model A, so I thought it would be interesting to see if I could make one. I looked at the Pi 4 with [this really cool X-ray tool](https://al.zerostem.io/~al/dzi/xray.html), as well as using [this album of X-ray images](https://www.reddit.com/r/raspberry_pi/comments/c6l0qa/i_took_some_highresolution_xray_radiographs_of_my/) from reddit user u/xCP23x:

{{< figure src="./raspberry-pi-4-model-b-xray.jpg" alt="Xray image of Raspberry Pi 4 model B" width="455" height="301" class="insert-image" >}}

The cut was calculated to try to avoid anything important, though as we'll find later it may not have been measured carefully enough.

{{< figure src="./cutting-raspberry-pi-4-with-angle-grinder.jpg" alt="Cutting a Raspberry Pi 4 model B with an angle grinder - Red Shirt Jeff" width="500" height="319" class="insert-image" >}}

After the cut, I cleaned up the edge with fine-grit sandpaper, some tweezers to grab off a few ICs and capacitors that were clinging by one edge, and then a bit of rubbing alcohol. I wanted to make sure no internal traces or ground planes were shorted, and I was satisfied with the edge:

{{< figure src="./edge-of-pi-4-model-b-cleaned-cut.jpeg" alt="Edge of Raspberry Pi 4 model B PCB cleaned up after cut" width="600" height="400" class="insert-image" >}}

I took the Pi over to my desk, half expecting something to catch fire. But I plugged it into a switched outlet, turned it on... and the LEDs seemed to light up as if _something_ was working!

{{< figure src="./act-led-flash-pi.gif" alt="ACT LED flashing during boot on Raspberry Pi 4 model B cut" width="400" height="225" class="insert-image" >}}

But there wasn't any HDMI output. No rainbow screen, nothing. So something wasn't quite right. I tried sanding the edge a little more, and put a fresh copy of Raspberry Pi OS on a microSD card, but to no avail. The green activity LED would blink a couple times, then go really dim. And if I waited a while, it would start getting brighter.

So at this point it seemed like some sort of power issue. But _something_ was working—otherwise that series of activity blinks at the beginning wouldn't happen.

## Why won't it boot?

It seemed like the Pi must be dying somewhere in the middle of the bootloader—the one little piece of the Pi puzzle that's unfortunately _closed source_. So I asked for help in [this thread](https://forums.raspberrypi.com/viewtopic.php?f=63&t=320462) in the Raspberry Pi Forums.

The first thing I learned was that the circuit next to the audio jack—which I had cut right through—was apparently part of the Pi's switching power supply. Forum user trejan pointed out that this part of the power circuit was actually moved over next to the USB-C port on newer 8 GB Pi revisions.

{{< figure src="./power-circuit-moved-pi-4-8gb.jpg" alt="Power Circuit moved over by USB-C port on 8GB Raspberry Pi 4 model B" width="599" height="337" class="insert-image" >}}

I was going to throw in the towel, but forum user cleverca22 said the first few blinks of the ACT LED meant SPI flash was being read properly, and he thought we could get UART through the Pi's serial port.

For a good explanation of UART, serial ports, and getting console access to the Pi, please check out my blog post [Attaching to a Raspberry Pi's Serial Console (UART) for debugging](https://www.jeffgeerling.com/blog/2021/attaching-raspberry-pis-serial-console-uart-debugging).

In the course of working on this now-undead-Pi, I learned a LOT about what it _actually_ takes to boot a Raspberry Pi. And I'll explain parts of it here, but if you want the _full_ story, check out my YouTube video on the topic:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/DHwL1_afSn8" frameborder='0' allowfullscreen></iframe></div>
</div>

## The Raspberry Pi boot process

Using a custom `recovery.bin` file from cleverca22, I was able to get the Pi to boot into the VideoCore VPU, and could access that part of the System on a Chip via UART on the Pi. But trying anything else would result in a lockup.

To try to figure out the next steps in debugging, it was important to understand the boot flow on the Pi:

{{< figure src="./raspberry-pi-b-boot-flow.jpg" alt="Raspberry Pi 4 model B cut up boot flow - EEPROM, VideoCore, CPU, SDRAM" width="600" height="400" class="insert-image" >}}

When the Raspberry Pi boots up, the first thing that fires off is the tiny little EEPROM chip (1), using a protocol called SPI, or Serial Peripheral Interface. It contains 'bootloader' code that fires off everything else on the Pi, starting with the VideoCore graphics core (2) inside the Pi's System on a Chip.

For every byte that's read from the EEPROM, the green activity LED flashes once. So when we I was seeing it blink a couple times, there were actually _tons_ of bytes getting sent through the SPI interface to get the Pi booting up.

From that point, the VideoCore GPU takes over and executes a bootloader, and from there things like the CPU, SDRAM, and other subsystems start coming on line (3).

So something between when the VideoCore takes over and when the CPU comes online is breaking.

At this point, cleverca22 suggested I try re-flashing the Raspberry Pi's EEPROM.

I grabbed [a copy of the bootloader firmware from the rpi-eeprom repo](https://github.com/raspberrypi/rpi-eeprom), enabled UART in it [following cleverca22's instructions](https://forums.raspberrypi.com/viewtopic.php?p=1919044#p1919044), and copied it off to a microSD card.

{{< figure src="./steady-led-green-pi.gif" alt="Raspberry Pi 4 model B cut booting to steady green LED" width="480" height="270" class="insert-image" >}}

Unfortunately... when I booted the Pi with that card, the activity LED just stayed green, and it didn't seem like the Pi would do anything. It must be trying to initialize some bit of hardware that's broken.

So right now, the furthest I can get is running a custom `recovery.bin` file that boots me up inside the VPU, or Video processor. I can't get access to the ARM CPU or the system memory.

## Next Steps

But there are still some other things I _might_ be able to try, like desoldering the USB and network chips, rebuilding part of the power circuit by hand, or debugging even further through some test pads on the bottom of the Pi.

In any case, that'll be for a future post. I just ordered a [Quick 861DW](https://amzn.to/3lDq9Wn) hot air rework station... and once that arrives, no circuit board will be safe!
