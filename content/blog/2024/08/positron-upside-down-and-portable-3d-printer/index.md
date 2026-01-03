---
nid: 3400
title: "Positron - an upside-down and portable 3D printer"
slug: "positron-upside-down-and-portable-3d-printer"
date: 2024-08-26T16:44:51+00:00
drupal:
  nid: 3400
  path: /blog/2024/positron-upside-down-and-portable-3d-printer
  body_format: markdown
  redirects: []
tags:
  - 3d printing
  - portable
  - positron
  - raspberry pi
  - video
  - youtube
---

I've been getting into 3D printing lately. I have an older Ender 3 V2 at home I bought during COVID. And in the past year I've acquired an Ender 3 S1, Bambu Labs P1S, and Prusa MK4.

I also [dove head-first into 3D CAD](https://www.jeffgeerling.com/blog/2024/giving-away-480-raspberry-pis-was-harder-i-expected), and designed a number of small SBC cases or parts to help with things around the house.

But I'd never built my own 3D printer from a kit—all the printers I've had were pre-built and at most, required assembling the prebuilt gantry or toolhead. That finally changed with the Positron V3.2:

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" preload autoplay loop playsinline muted>
  <source src="./positron-benchy-timelapse-resized.m4v" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

The Positron V3.2 has its origins in [this design by K R A L Y N 3D](https://www.youtube.com/watch?v=X_QLxTVtyng), and the V3.2 version was turned into a kit by LDO Motors and Positron3D. There's also a reprap-style alternative that's slightly taller and a bit cheaper called [Positron LT](https://github.com/Audiotronix/Positron_LT).

The Positron V3.2 is _not cheap_, with [the kit](https://positron3d.com/pages/kits) (consisting of a hard carry case, the CNC machined parts, the PCBs, a touchscreen controller with Raspberry Pi CM4, belts, motors, screws, etc) priced at $699. If you don't have a 3D printer capable of printing the various 3D printed parts, you can buy a set of pre-printed parts for [an additional $99](https://west3d.com/products/positron-printed-parts-in-stock-ready-to-ship).

> **Disclaimer**: The Positron V3.2 kit I built was sent from Positron3D/LDO Motors. They don't have any input into this blog post or the video I published, but it's important to note I did not pay for this with my own money, and I would have a hard time justifying the price to my wife if I did, since I already am spoiled for choice with the 3D printers I _have_ paid for :)

The first question most people ask is _why upside-down?_ Many have already [tested upside-down printing](https://www.youtube.com/watch?v=n4nIM60UUZc), and found it doesn't offer much improvement in terms of bridging and general print quality. [Emily the Engineer](https://www.youtube.com/watch?v=FYuqLsvRXhU) even _spun her Ender_ while printing, and found it was still quite happy to print out a decent benchy.

{{< figure src="./positron-motion-system.jpeg" alt="Positron Motion System - belts and pulleys" width="700" height="auto" class="insert-image" >}}

For the Positron, the advantage is keeping almost all the parts in the base. The X, Y, and Z motors are all contained within the base, and the toolhead is mounted directly above the base, keeping a low center of gravity, allowing the Z-axis to be the only vertical protrusion.

{{< figure src="./positron-upside-down-benchy.jpeg" alt="Upside-down benchy on Positron V3.2 bed" width="700" height="auto" class="insert-image" >}}

Seeing the image above, you may wonder about the bed—it's transparent glass, so I first wondered how they could advertise it as 'heated'?

They use [borosilicate glass](https://en.wikipedia.org/wiki/Borosilicate_glass) capable of handling higher temperatures than normal glass, and they coated the top with a 3-micron layer of ITO, or [Indium Tin Oxide](https://en.wikipedia.org/wiki/Indium_tin_oxide), the same stuff that's used for defrosting airplane cockpit windows.

Two leads on either edge of the glass heat up the bed _very_ evenly, and it's great for PLA, and can reach beyond 100°C—but I was told it's not as useful for higher temperature materials like ASA, ABS, or Nylon. And the hot end isn't suited for those materials either, as the unique 90°-angled print head probably can't keep up at any reasonable flow rate past 250°C.

The biggest downside to upside-down printing is that the nozzle likes to turn into a little filament fountain—which requires a little vigilance picking errant filament goo off before starting a print:

{{< figure src="./positron-filament-goo-nozzle.jpg" alt="Positron filament goo on nozzle" width="700" height="auto" class="insert-image" >}}

Some updates to the Klipper macros may help with this, though—I'm told it's _supposed_ to dock the nozzle on a silicon pad on the bed while heating, but right now it's a bit hard to get that to work correctly.

As a final test of this printer's portability, I set it up on my trunk in a local park, and printed a frisbee while plugged into my little 256 Watt-hour portable battery:

{{< figure src="./positron-on-car-trunk.jpeg" alt="Positron on car trunk" width="700" height="auto" class="insert-image" >}}

The Positron consumed between 50-150W while printing (spiking highest while the bed and toolhead heaters were going full blast), and idled around 20W with just Klipper and the fans running. I was going to test how long I could run a solar-powered print with a backpack-size foldable solar panel as well, but that didn't arrive in time for my testing.

I have a full video going through my build experience, some of the other quirks I encountered, and how it worked on my trunk in a local park. You can watch it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/mTIwNMhFvOU" frameborder='0' allowfullscreen></iframe></div>
</div>

If you have the budget and would like to pick up a kit, [Positron3D partnered with LDO Motoros](https://positron3d.com) and they have some kits linked from their website. All the designs and software are open source, you can find them on [Positron3D's GitHub](https://github.com/Positron3D/Positron).
