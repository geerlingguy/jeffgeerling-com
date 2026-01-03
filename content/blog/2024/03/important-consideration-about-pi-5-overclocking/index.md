---
nid: 3357
title: "An important consideration about Pi 5 overclocking"
slug: "important-consideration-about-pi-5-overclocking"
date: 2024-03-13T14:54:15+00:00
drupal:
  nid: 3357
  path: /blog/2024/important-consideration-about-pi-5-overclocking
  body_format: markdown
  redirects: []
tags:
  - lottery
  - overclock
  - performance
  - pi 5
  - raspberry pi
  - silicon
  - wafer
---

_Silicon lottery_.

Now that the Raspberry Pi 5s been readily available (at least in _most_ regions) for a few months, more people started messing with clocks, trying to get the most speed possible out of their Pi 5s.

{{< figure src="./raspberry-pi-5-argon-thrml-tower-cooler.jpg" alt="Argon THRML Tower Cooler installed on Raspberry Pi 5 for Overclocking test" width="700" height="auto" class="insert-image" >}}

Unlike the Pi 4, the Pi 5 is typically comfortable at 2.6 or even 2.8 GHz, and some Pi 5s can hit 3.0 GHz (<s>but no higher—more on why tomorrow</s> well... [this limit may be able to be lifted](https://github.com/raspberrypi/firmware/issues/1876)).

After some testing, I found the [default 2.4 GHz clock on the Pi 5 is pretty much the efficiency sweet spot](/blog/2023/overclocking-and-underclocking-raspberry-pi-5), and after a _lot_ more testing recently, I can confirm that's still the case, testing a number of Pi 5 samples.

Also unlike the Pi 4, the Pi 5's not very picky about cooling. While the chip runs a little hotter, it doesn't need exotic cooling like spraying ice, water cooling, or LN2, to run at its highest possible clock speeds. It does need _some_ cooling, but I've found the biggest factor affecting how fast your Pi 5 will go is the chip itself.

{{< figure src="./silicon-wafer-80s.jpeg" alt="A silicon wafer from the 1980s" width="700" height="auto" class="insert-image" >}}

The _silicon lottery_ basically states that among samples of the exact same silicon chip—in this case the BCM2712 at the heart of the Pi 5—there are variations affecting performance, thermals, etc.

These variations are almost imperceptible at the 2.4 GHz default clock Raspberry Pi chose for the board, but they can affect how fast your Pi 5 can go, no matter what cooling solution you use.

To prove that, over the past 5 months, I've slowly acquired 10 Pi 5s from vendors around the world (1 at a time), to make sure they come from different batches, and I've been testing overclocking performance on each. I also had another project slated for a number of these Pis (which I'll reveal tomorrow), but one thing I wanted to quantify is how many of the Pi 5s would hit 3.0 GHz.

And the answer? Out of the ten _I_ bought, only one! It was an 8GB model (I did buy a few 4GB Pi 5s as well, since [the performance characteristics can be slightly different](https://github.com/raspberrypi/firmware/issues/1854), and it runs at 3 GHz reliably with _any_ form of active cooling.

I've tested it with:

  - Raspberry Pi's own Active Cooler
  - Argon THRML (a giant tower cooler for the Pi 5)
  - Argon Neo (a case with a larger heatsink and PWM fan for the Pi 5)
  - EDATEC Pi 5 Fanless Case (a top + bottom heatsink cover for the Pi 5)

And in all cases, it worked fine.

I tested my other Pis with all those cooling solutions, and even tried a couple on my [massively-overkill water cooling setup](/blog/2024/water-cooling-overkill-pi-5), and no matter what, none of them reached 3.0 GHz. The closest I got was 2.9 GHz on a couple of them. The rest maxed out at 2.8 GHz.

The result of that 3.0 GHz overclock? A marginally-improved [Geekbench 6 score of 1662](https://browser.geekbench.com/v6/cpu/5297916), versus [1507](https://browser.geekbench.com/v6/cpu/2808487) with no OC. To achieve that 10% speedup, it ate up about 20% more power, so efficiency-wise, it's not worth it.

Also, if you're _only_ concerned about raw performance and efficiency, an RK3588-based SBC might be the better option regardless—it gives almost double the maximum performance, using about the same power! (notwithstanding software issues and vendor / community support.)

Bottom line: not every Pi 5 can achieve a 3.0 GHz overclock—in fact, in my testing, _most can't_. 2.4 GHz is the most efficient clock for the C0 BCM2712 silicon running on the Pi 5, at least based on my testing.

More on the Pi 5's silicon coming tomorrow—which happens to be Pi Day :)
