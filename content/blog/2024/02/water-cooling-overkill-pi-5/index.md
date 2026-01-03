---
nid: 3351
title: "Water cooling is overkill for Pi 5"
slug: "water-cooling-overkill-pi-5"
date: 2024-02-21T16:16:42+00:00
drupal:
  nid: 3351
  path: /blog/2024/water-cooling-overkill-pi-5
  body_format: markdown
  redirects:
    - /blog/2024/ice-pump-water-cooling-overkill-pi-5
aliases:
  - /blog/2024/ice-pump-water-cooling-overkill-pi-5
tags:
  - 52pi
  - cooling
  - overclock
  - performance
  - raspberry pi
  - seeed
  - water
---

**tl;dr**: 52Pi and Seeed Studio's water cooling solution for the Raspberry Pi 5 can be fun, and works better than any other solution—but at a _steep_ price, and with a number of annoying quirks.

{{< figure src="./ice-pump-installed-pi-5-hero.jpg" alt="Ice Pump water cooling block installed on Raspberry Pi 5" width="700" height="auto" class="insert-image" >}}

A few months ago, 52Pi reached out and asked if they could send a new water cooling kit they were working on for the Raspberry Pi 5. At the time, the hope was we could figure out a way to get very high overclock with adequate cooling.

Unfortunately—for reasons I'll explore more soon—the Pi 5 can't overclock beyond 3.0 GHz (it's not physically possible). Some of why is explained in my blog post [Overclocking and *Underclocking* the Raspberry Pi 5](/blog/2023/overclocking-and-underclocking-raspberry-pi-5).

But water cooling is still fun, and the product is in production now, so I figured I'd still give it a fair shot, and see if I thought it might be worth buying for certain niche use cases.

The [full water cooling kit is $120](https://www.seeedstudio.com/High-Performance-Liquid-Cooler-for-Raspberry-Pi-5-p-5854.html), and the [copper/acrylic water cooling block for the Pi 5 is available separately for $20](https://www.seeedstudio.com/High-Performance-Liquid-Cooler-for-Raspberry-Pi-5-p-5854.html). (The website calls the block a radiator... but that's not quite right.)

There are a few issues out of the gate:

  - The type of metal used in the radiator is not specified, but seems to be aluminum. Mixing metals in a cooling loop can lead to corrosion issues, especially if you mix copper and aluminum. The aluminum will likely corrode over time unless you use [special anti-corrosion cooling fluids](https://amzn.to/3SJfiK1), and even then...
  - The 120mm fan and pump both have RGB LEDs enabled that can't be turned off. This consumes a tiny bit more power, but the more annoying aspect is they're in a perpetual 'demo mode' loop where colors cycle in different patterns, and besides looking neat for a minute or so, they contribute nothing to the performance.
  - The fan + pump + LEDs consume 15W of power continuously—that's more than I've been able to get any Raspberry Pi 5 to consume by itself. If you're cooling a cluster of 10 Raspberry Pis, maybe that could make a tiny bit of sense, but for cooling one, two, even four Raspberry Pis... having the cooling solution consume more power than the Pis themselves seems a tad bit wasteful.

{{< figure src="./ice-pump-15w.jpg" alt="Cooling 15W Kill-A-Watt" width="700" height="auto" class="insert-image" >}}

The cooling performance is outstanding—I expected no less, with a setup so extremely overkill. It comes with a bunch of small thermal pads you apply to the top _and bottom_ of the Pi:

{{< figure src="./ice-pump-thermal-pads.jpg" alt="Ice Pump thermal pads on top and bottom" width="700" height="auto" class="insert-image" >}}

However, the full metal enclosure means it is impossible to get at the PCIe expansion slot, and nearly impossible to use the cooling solution with any [PCIe-based HATs or bottom boards](https://pipci.jeffgeerling.com/hats) (at least none that I'm aware of, yet).

The microSD card slot and other ports and slots are fine, however, and the overall Z-height is not bad, so using a GPIO extender, you could still use many HATs with this cooling solution.

All that said, noise is another concern—you'd think with a giant 120mm fan, and a relatively quiet pump, the overall solution could be whisper quiet... but there again, the flow adds a little noise (even with air out of the lines), and the fan is louder than any other fan solution I've used with Pi 5 so far:

{{< figure src="./ice-pump-44-dba.jpg" alt="Ice Pump 44 dBa sound level" width="700" height="auto" class="insert-image" >}}

Contrast that to the Active Cooler, which costs $7, still keeps the Pi 5 from thermal throttling at any overclock and load, and is quiet enough to be around the 32 dBa noise floor of my studio at 5000 rpm:

{{< figure src="./pi-5-active-cooler-33-dba.jpg" alt="Raspberry Pi active cooler 33 dBa" width="700" height="auto" class="insert-image" >}}

The kit is the purest expression of the phrase "a solution in search of a problem"—though, sadly, I don't blame Seeed Studio or 52Pi here. I know when they started the design process for this cooling kit, nobody had confirmed the Pi 5's 3.0 GHz overclock ceiling.

Outside of some insane hardware hacking, there will not be any way to get beyond that hard limit, and that means a product like the Water Cooling Kit for Raspberry Pi 5 is somewhat DOA, except for possibly one or two _extremely_ niche use cases, for example:

  - Deploying a Raspberry Pi 5 in a very hot environment, while placing the radiator somewhere cooler, using water cooling to its full potential.
  - Cooling a large-ish cluster of Raspberry Pi 5's (though there are other more economical, quieter ways of cooling a cluster)

In the end, after spending a couple days tinkering with this Kit, my main takeaway is: Raspberry Pi's own Active Cooler is a bit of a gem. In my opinion, one of the best little bits of hardware Raspberry Pi's introduced in the past couple years.

{{< figure src="./ice-pump-overclocked-42c.jpg" alt="Pi 5 overclocked to 2800 MHz 42C" width="700" height="auto" class="insert-image" >}}

The Water Cooling Kit does knock the temperature of a Pi 5 overclocked to 2.8 GHz down into the 40's in a room that's 22°C (compared to the 60's for the Active Cooler), so that's nice.

But it is not a product I would recommend to anyone but a very tiny minority of Pi 5 users. I do hope they sell enough of these to continue building out the line (even if not only for Pi). If Raspberry Pi introduces a 'B' revision of the Pi 5, maybe we could have more fun playing with thermal limits...
