---
nid: 3419
title: "M4 Mac mini's efficiency is incredible"
slug: "m4-mac-minis-efficiency-incredible"
date: 2024-11-12T21:44:07+00:00
drupal:
  nid: 3419
  path: /blog/2024/m4-mac-minis-efficiency-incredible
  body_format: markdown
  redirects: []
tags:
  - apple
  - benchmarks
  - energy efficiency
  - m4
  - mac
  - mac mini
  - performance
  - top500
---

I had to pause some of my work getting [a current-gen AMD graphics card running on the Pi 5](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/680) and [testing a 192-core AmpereOne server](https://github.com/geerlingguy/sbc-reviews/issues/52) to quickly post on the M4's efficiency.

{{< figure src="./m4-mac-mini-on-desk.jpg" alt="M4 Mac mini on desk" width="700" height="auto" class="insert-image" >}}

I expected M4 to be better than M1/M2 (I haven't personally tested M3), and I hoped it would at least match the previous total-system-power efficiency king, a tiny arm SBC with an RK3588 SoC... but I didn't expect it to jump forward _32%_. Efficiency gains on the Arm systems I test typically look like 2-5% year over year.

The M4 mini I just bought reaches **6.74 Gflops/W** on the HPL benchmark.

<blockquote>
<p><strong>UPDATE 2024-11-20</strong>: I re-ran all my tests without my 10 Gbps Ethernet plugged in, and the efficiency is even better. I also re-tested LLM performance, and made this quick video:</p>
<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/3FICjyf-e8k" frameborder='0' allowfullscreen></iframe></div>
</div>
<p>For the latest benchmark results, <a href="https://github.com/geerlingguy/sbc-reviews/issues/57">check my sbc-reviews M4 Mac mini issue</a>.</p>
</blockquote>

I can get 283 Gflops at 42W, versus 264 at 66W on my M1 Max Mac Studio (for a round 4.00 Gflops/W).

The chip isn't the _fastest_ at everything, but it's certainly the most _efficient_ CPU I've ever tested. And that scales down to idle power, too—it hovers between 3-4W at idle—which is about the same as a _Raspberry Pi_.

This is total system power draw, too—not just the CPU.

And the system I bought includes 10 Gigabit Ethernet and 32 GB of RAM; most systems I've used consume 4-6W just _running the 10 GbE controller_!

In [1.25U of rack space](https://www.myelectronics.nl/us/19-inch-125u-rack-mount-for-3x-mac-mini-2024.html), you could run three Mac minis, idling around 10W, giving almost a teraflop of CPU performance. (Not to mention there's a fast GPU/NPU, 10 GbE, and tons of high speed Thunderbolt IO in the back.)

_If only they didn't put the power button on the bottom._

You can check out all my [top500-benchmark results](https://github.com/geerlingguy/top500-benchmark) on GitHub, and follow my progress [testing out the M4 mini here](https://github.com/geerlingguy/sbc-reviews/issues/57).

I haven't tested an M4 Pro Mac mini yet, so I'm not sure if the efficiency is any better or worse.
