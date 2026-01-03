---
nid: 3394
title: "Hacking Pi firmware to get the fastest overclock"
slug: "hacking-pi-firmware-get-fastest-overclock"
date: 2024-07-30T14:02:57+00:00
drupal:
  nid: 3394
  path: /blog/2024/hacking-pi-firmware-get-fastest-overclock
  body_format: markdown
  redirects:
    - /blog/2024/fastest-overclock-–-on-raspberry-pi
    - /blog/2024/fastest-overclock-on-raspberry-pi
aliases:
  - /blog/2024/fastest-overclock-–-on-raspberry-pi
  - /blog/2024/fastest-overclock-on-raspberry-pi
tags:
  - cooling
  - cpu
  - linux
  - overclock
  - peltier
  - performance
  - raspberry pi
  - video
---

{{< figure src="./raspberry-pi-5-smoky-overclock.jpeg" alt="Raspberry Pi 5 with dry ice smoke surrounding it" width="700" height="auto" class="insert-image" >}}

Since boosting my Pi 5 from the default 2.4 GHz clock to [3.14 GHz on Pi Day](/blog/2024/raspberry-pi-5-can-overclock-314-ghz), I've wanted to go faster. Especially since many other users have topped my Geekbench scores since then :)

In March, Raspberry Pi introduced new firmware that unlocked frequencies above 3,000 MHz for overclocking. This summer, [NUMA Emulation patches](/blog/2024/numa-emulation-speeds-pi-5-and-other-improvements) boosted performance another 5-10% through memory access optimizations.

But even with a [golden sample](https://www.reddit.com/r/overclocking/comments/3d1y4j/comment/ct1sk4e/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) Pi 5, I haven't seen anybody go much beyond 3.1 or 3.2 GHz. The problem seemed to be power supply—the Pi's firmware limits the SoC to a maximum of 1.000V.

There is [an `over_voltage_delta` option](/blog/2023/overclocking-and-underclocking-raspberry-pi-5) which works with [DVFS](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#using-dvfs) to boost voltages a bit—but that is also capped at 1.000V.

After emailing back and forth a bit, GitHub user jonatron [beat my 3.14 GHz overclock](https://jonatron.github.io/randomstuff/pivolt/) quite handily, pushing his Pi up to 3.3 GHz, but without attempting a full Geekbench 6 run.

{{< figure src="./pi-overclock-overvolt-cooling-setup.jpg" alt="Pi Overclock - Overvolt cooling setup" width="700" height="auto" class="insert-image" >}}

His blog post (linked above) explains some of the process, but after talking a bunch, he agreed to let me release a bit of code that enables the overvolt hack. It is now available in my [pi-overvolt](https://github.com/geerlingguy/pi-overvolt) repository, along with a description of how to use it—and **copious warnings**.

The problem is, **if you hack the firmware's voltage limits, you void your Pi's warranty**. I'm not sure if it's detectable, especially the way it's being done here... but there's a good chance you'll burn up your Pi's SoC even if you know what you're doing.

I didn't burn up my Pi (luckily), and I made this video documenting my journey to a stable-ish 3.4 GHz overclock, resulting in the [current world record Geekbench 6 score on a Pi 5](https://browser.geekbench.com/v6/cpu/search?dir=desc&q=Raspberry+Pi+5+Model+B&sort=score).

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/OXXKi-J0gs4" frameborder='0' allowfullscreen></iframe></div>
</div>

If you want to replicate my setup, here are all the parts I used:

  - Raspberry Pi 5 'golden sample' (the one that was most stable out of the 10 Pi 5's I own)
  - [USB Fan Heatsink Peltier Cooling Module](https://amzn.to/3WmTJ3H) (Amazon affiliate link)
  - Bottom heatsink plate from [EDATEC Fanless Heatsink Case](https://www.digikey.com/en/products/detail/edatec/ED-PI5CASE-OB/21769666)
  - [Noctua 5V 140mm Fan](https://amzn.to/4dmYAbX) (Amazon affiliate link) inside [this 3D printed stand](https://www.printables.com/model/511959-adjustable-perfect-desktop-fan-stand-for-120-and-1)
  - [Argon PWR GaN 27W USB-C power supply](https://amzn.to/3Yse5Lt) (Amazon affiliate link)
  - [Extra thermal pads](https://amzn.to/3SxpTs3) (Amazon affiliate link) to conduct heat from PMIC to Peltier cooler

For the [world-record 3.4 GHz Geekbench run](https://browser.geekbench.com/v6/cpu/7058700), I ran my custom kernel with the NUMA Emulation patch (linked earlier in this post) applied, and followed the instructions to set a higher voltage in my [pi-overvolt repo](https://github.com/geerlingguy/pi-overvolt).

> **Update**: Since posting this information, I also found out about another great guide to overclocking and the PMIC's limitations on the Pi 5—see [SkatterBencher #77: Raspberry Pi 5 Overclocked to 3000 MHz](https://skatterbencher.com/2024/07/18/skatterbencher-77-raspberry-pi-5-overclocked-to-3000-mhz/#OC_Strategy_X_PMIC_Further_Discussion).
