---
date: '2026-05-28T09:00:00-05:00'
tags: ['geerling engineering', 'radio', 'sdr', 'nanovna', '3d printing', 'video', 'youtube']
title: 'Tuning in FM Radio on a 3D Printer Heatbed'
slug: 'tuning-in-fm-radio-on-a-3d-printer-heatbed'
---
[Pooch](https://linktr.ee/repkord) from Repkord dropped by my studio while he was in St. Louis, and asked a simple question:

_Can a 3D printer's heatbed act as an antenna?_

A fair question, as many an antenna is embedded in a PCB these days... and the traces on a [PCB heatbed](https://www.prusa3d.com/product/heatbed-set/) like the one used in Prusa's Core One look kinda like an antenna, if you squint the right way.

{{< figure
  src="./nanovna-3d-printer-heatbed.jpg"
  alt="NanoVNA hooked up to 3D Printer Heatbed"
  width="500"
  height="auto"
  class="insert-image"
>}}

Really, anything (or anyone) can be an antenna, given enough power.

But to stick to the scientific method, I had my Dad come over and show me the ropes with a [NanoVNA](https://amzn.to/4u3eYX7)—a useful tool radio engineers and amateur radio operators use to measure the performance of antenna systems (among other things).

There's a video detailing the whole journey over on Geerling Engineering, and I've embedded it below:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/BA3_jCstp3o' frameborder='0' allowfullscreen></iframe></div>
</div>

## Too long, didn't watch

If you'd rather get to the punchline, here it is:

  - When plugged into the NanoVNA, there were many notches on the SWR chart, like around 1 GHz, 130 MHz, and 43 MHz. They weren't well-defined, but there were definitely frequecies that seemed to be okay candidates for radio reception!
  - A 3D printer heatbed is designed for low resistance DC power for heating, so the traces and design are not at all optimized for RF use (either transmit or receive)
  - _However_... if you're within a mile of a high-power FM transmitting tower (like KYKY-FM in St. Louis, which broadcasts at 30+ kW), you can pick up the signal; clear enough for stereo reception!

Now I'm wondering whether Prusa should include a headphone jack in their next printer design...
