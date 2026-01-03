---
nid: 3139
title: "CutiePi - a Raspberry Pi CM4 Linux Tablet"
slug: "cutiepi-raspberry-pi-cm4-linux-tablet"
date: 2021-11-10T15:00:12+00:00
drupal:
  nid: 3139
  path: /blog/2021/cutiepi-raspberry-pi-cm4-linux-tablet
  body_format: markdown
  redirects: []
tags:
  - cutiepi
  - linux
  - portable
  - raspberry pi
  - reviews
  - tablet
  - video
  - youtube
---

A few weeks ago, I got my hands on an early prototype of the [CutiePi](https://cutiepi.io).

{{< figure src="./cutiepi-pi-mug.jpeg" alt="CutiePi Tablet with Raspberry Pi mug" width="640" height="360" class="insert-image" >}}

Unlike many other Pi 'tablet' projects, this one is actually more of a, well, _tablet_, since it is based on the diminutive Compute Module 4. And because of that, and a custom main board, the CutiePi is less than half as thick as the other decent modern Raspberry Pi tablet on the market, the RasPad—plus it has a cute handle:

{{< figure src="./cutiepi-back.jpeg" alt="CutiePi Back" width="640" height="360" class="insert-image" >}}

It has an 8" 1280x800 multi-touch display, a 5000 mAh battery, USB 2.0, USB-C power (you can use the tablet while charging), micro HDMI for an external monitor or TV, and a microphone, speaker, and 5MP 1080p rear-facing camera.

But my favorite thing? The rear case pops off after removing eight #2 phillips-head screws! No pentalobe here. The entire design is made to be repairable (to a certain extent), and is also [open source](https://github.com/cutiepi-io), including the custom [CutiePi Shell](https://github.com/cutiepi-io/cutiepi-shell) UI, which is so far the best custom tablet UI I've played with on a Raspberry Pi (though... that's not saying much!).

{{< figure src="./cutiepi-shell.jpg" alt="CutiePi Shell" width="552" height="372" class="insert-image" >}}

Being based on a Raspberry Pi means you can also run other OSes, for example Ubuntu 21.04, with its own touch-based UI. Support for that, and for some other interesting use cases like being an external keyboard and touchpad in 'convergence mode', is still in the works.

In addition to some shipping woes, the pre-release software I'm using still has some bugs that are being ironed out. In fact, in the course of making my video on the CutiePi, I found an MCU bug that prevented a hard reset in some conditions, and that bug was fixed the next day!

{{< figure src="./cutiepi-insides.jpeg" alt="CutiePi Insides - Custom motherboard" width="640" height="418" class="insert-image" >}}

I wasn't expecting too much from the CutiePi, after all, 99% of the Raspberry Pi-based tablets are a touchscreen mounted to a bulky Raspberry Pi 4. This tablet sells for $229, includes a Compute Module, and is built with a custom-molded plastic enclosure.

The enclosure is fairly durable and has a nice grippy texture, but the screen can scratch pretty easily, so if using it for remote access or tossing it in a bag with other things, I'd consider a screen protector.

{{< figure src="./cutiepi-dissembled.jpeg" alt="CutiePi Dissembled" width="640" height="427" class="insert-image" >}}

Besides the fact that the experience isn't buttery smooth like even a low-end iPad, one other disappointment that I don't think is solvable with this particular design is the thermals are pretty constrained. Only a few minutes into a `stress-ng` run results in throttling, from 1.5 GHz to 1.2 GHz. The heat from the Compute Module just has nowhere to go after the thin heat sink is hot—plastic is a pretty good insulator, and there aren't any vents to speak of:

{{< figure src="./Throttle-Temp-CutiePi.png" alt="CutiePi temperature graph showing throttling after stress test" width="700" height="394" class="insert-image" >}}

I have a _full_ review of the board in the following YouTube video—please have a watch and see how it handles YouTube, general browsing, and RetroPie, then keep watching for a full teardown!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/t-ZQ9LRdXSk" frameborder='0' allowfullscreen></iframe></div>
</div>
