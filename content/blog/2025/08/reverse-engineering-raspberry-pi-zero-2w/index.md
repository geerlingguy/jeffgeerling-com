---
nid: 3484
title: "Reverse Engineering the Raspberry Pi Zero 2W"
slug: "reverse-engineering-raspberry-pi-zero-2w"
date: 2025-08-12T21:00:29+00:00
drupal:
  nid: 3484
  path: /blog/2025/reverse-engineering-raspberry-pi-zero-2w
  body_format: markdown
  redirects: []
tags:
  - level2jeff
  - pcb
  - raspberry pi
  - reverse engineering
  - rp3a0
  - video
  - zero 2 w
---

{{< figure src="./jonathan-clark-pico-zero-2w-full.jpeg" alt="Raspberry Pi not Pico by Jonathan Clark" width="700" height="467" class="insert-image" >}}

This is not a Raspberry Pi Pico. Despite it's tiny size and castellated edges, this is _actually_ a full Raspberry Pi Zero 2W.

Well, sorta. At Open Sauce, probably the most interesting encounter I had was with [Jonathan Clark](http://jonathanclark.dev/).

You see, I was on a Reverse Engineering panel at Open Sauce, but [I mentioned on Twitter](https://x.com/geerlingguy/status/1945207387914178562), I wouldn't call myself a reverse engineer, more like a 'guy who breaks things sometimes taking them apart, and learns many ways to not break things, sometimes.'

One thing I _do_ have sometimes, is access to other people and companies who I know can do amazing things I _can't_, like Lumafield, who I worked with to CT scan the Raspberry Pi Zero 2W:

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" autoplay loop muted>
  <source src="./pi-zero-2w-lumafield-spin.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

They've been gracious enough to let me share the scan in their webapp, Voyager, so if you want to take it for a spin, check it out here: [Lumafield Raspberry Pi Zero 2W reconstruction](https://voyager.lumafield.com/project/fcbc8145-2873-4432-bfcc-29896cd440c9).

_Jonathan_, on the other hand, _desoldered every chip on a Pi Zero 2W_, then sat there sanding down the circuit board by hand, layer by layer, to [take pictures, layer by layer](https://github.com/jonny12375/rp3a0/tree/main/docs#results).

He reverse-engineered the entire PCB design, with help from the [reduced schematics Raspberry Pi provides](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-reduced-schematics.pdf). Then he built his _own_ version, that just so happens to sit in the same form factor as a Raspberry Pi Pico, just a little taller to account for a micro HDMI and USB-C port (thus solving two of my I/O gripes with the Pi Zero 2W!).

{{< figure src="./jonathan-clark-pico-zero-2w-bare-pcb-pico.jpeg" alt="Raspberry Pi Pico and RP3A0 board next to each other" width="700" height="467" class="insert-image" >}}

The biggest achievement was reverse engineering the [entire pinout of the custom Raspberry Pi RP3A0 chip](https://docs.google.com/spreadsheets/d/1cQo1mM0g4L-HjAe8-86Zw-xbBoLv0I49Cb5mO69Yzt8/edit?usp=sharing).

Not everything works:

  - The HDMI port is a bit off, so you can't get output. Plus the spacing on the board makes it hard to use in tandem with most USB-C plugs I've tried.
  - There's no WiFi (no current space on the board to put something like Raspberry Pi's new [Radio Module 2](https://www.raspberrypi.com/news/raspberry-pi-radio-module-2-available-now-at-4/)
  - The board is small enough the RP3A0 chip can't dissipate heat as effectively as on the Zero 2W, meaning it gets a little toasty
  - I had trouble getting it to run stably, as it would reboot every 34 seconds, while I watched over UART with a Debug Probe.

But... _why?_

Jonathan said he's trying to take an old Blackberry and replace its guts with modern hardware. And he already had it going on a microcontroller, but he wanted to see if he could get the full Linux experience going and still fit inside a standard Blackberry case.

It reminds me of Ahmad Byagowi's years-long, painstaking project to [reverse engineer the entire IBM PC110](https://github.com/ahmadexp/Open-Source-PC110).

I spoke with him about it at NAB earlier this year, and he said he literally _wore away his fingerprints_ sanding down PCBs to find all the traces. And he's also working with John McMaster, who I also visited this year, to de-lid and reverse engineer a bunch of the proprietary chips that make it run.

They're not doing it for money or to build some product off it, they're doing it for _curiosity_. And _preservation_.

Without efforts like these, the hardware designs we use every day will just get lost to history. And so I'm contributing my little part, too. Check out my video on this little Pi Zero 2W-in-a-Pico board below, and the links beyond that for all the things I've mentioned in this post:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/p7IvioiveOo" frameborder='0' allowfullscreen></iframe></div>
</div>

Links:

  - [Jonathan's Pi Zero 2W RP3A0 reverse engineering project](https://jonathanclark.dev/rp3a0)
  - [Lumafield's Pi Zero 2W reconstruction](https://voyager.lumafield.com/project/fcbc8145-2873-4432-bfcc-29896cd440c9)
  - [My original video on the Zero 2W with some x-ray images](https://www.youtube.com/watch?v=lKS2ElWQizA)
  - [Ahmad's PC110 Reverse Engineering project](https://github.com/ahmadexp/Open-Source-PC110)
