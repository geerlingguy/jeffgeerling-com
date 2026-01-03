---
nid: 3136
title: "Look inside the Raspberry Pi Zero 2 W and the RP3A0-AU"
slug: "look-inside-raspberry-pi-zero-2-w-and-rp3a0-au"
date: 2021-10-28T06:00:25+00:00
drupal:
  nid: 3136
  path: /blog/2021/look-inside-raspberry-pi-zero-2-w-and-rp3a0-au
  body_format: markdown
  redirects:
    - /blog/2021/look-inside-raspberry-pi-zero-2-w-and-new-rp3a0-au-chip
aliases:
  - /blog/2021/look-inside-raspberry-pi-zero-2-w-and-new-rp3a0-au-chip
tags:
  - bga
  - design
  - electronics
  - raspberry pi
  - reviews
  - soc
  - video
  - xray
  - youtube
  - zero
  - zero 2 w
---

Today, Raspberry Pi released their new [Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/), and it includes a new Raspberry Pi-branded chip, labeled `RP3A0-AU`.

I was able to get early access to the Zero 2, and I have a [full review of the device on my YouTube channel](https://www.youtube.com/watch?v=lKS2ElWQizA), but I wanted to share more of the X-ray images I took of the device to reveal its inner workings, and because I just think they look cool. Also, I paid a bit of money to get these pictures, so might as well share!

First, here's what the Zero 2 W looks like in person:

{{< figure src="./pi-zero-2-w-hero.jpeg" alt="Raspberry Pi Zero 2 W" width="640" height="427" class="insert-image" >}}

And here's what it looks like via X-ray:

{{< figure src="./pi-zero-2-w-xray-inverted.jpeg" alt="Raspberry Pi Zero 2 W - X-ray vision" width="640" height="427" class="insert-image" >}}

You might already see a few of the easter eggs hidden inside, but let's first get the basics out of the way. This board has the exact same _physical_ layout as the earlier Pi Zero W, with the same I/O, meaning it will fit in almost every accessory and project designed for earlier Pi Zero models.

For I/O, it features:

  - 1x mini CSI connector on edge for Pi Camera modules
  - 1x microSD card reader for boot volumes
  - 1x micro USB power input
  - 1x micro USB data port
  - 1x mini HDMI display port
  - 40-pin GPIO (following standard Pi layout)

But looking more closely at the X-ray image reveals what's inside the new Pi chip:

{{< figure src="./raspberry-pi-zero-2-w-chip-xray-side.jpg" alt="Xray picture of side of Pi Zero 2 W SoC chip with RAM package on top RP3A0-AU" width="700" height="276" class="insert-image" >}}

You can distinctly see two sets of bond wires—in this case, _gold_ bond wires, as indicated by the `-AU` chip suffix—with one leading to the 512MB LPDDR2 RAM on top, and the other leading to the BCM2710A1 clocked at 1 GHz on the bottom.

So this is not custom _silicon_, but it _is_ a custom 'package'. Older Pi Zero models (and some of the older Pi A/B models) used a [package-on-package](https://en.wikipedia.org/wiki/Package_on_a_package) layout, but the BCM2710 used here didn't come in a variety that was stackable. So Raspberry Pi decided to make their own, and put it all inside one easier-to-mass-produce chip.

But I was looking through more angles via digital X-ray when something else caught my eye:

{{< figure src="./pi-zero-2-chip-bga-ballout-pi-logo.jpg" alt="Raspberry Pi Zero 2 W BGA Xray pattern with mini Raspberry Pi Logo" width="600" height="600" class="insert-image" >}}

Do you see that little pattern in the middle of the BGA ('Ball Grid Array') on the main chip? Does it remind you of anything? How about we zoom and enhance:

{{< figure src="./raspberry-pi-logo-zero-2-w-bga-fun.jpg" alt="Raspberry Pi Logo in BGA ballout on Pi Zero 2 W" width="600" height="600" class="insert-image" >}}

And there it is! I stuck a transparent Pi logo on there in case it's still hard to see. I love seeing little design details like this, since it reminds me of the [signatures inside the Macintosh case](https://www.folklore.org/StoryView.py?project=Macintosh&story=Signing_Party.txt&topic=Apple%20Spirit&sortOrder=Sort%20by%20Date&detail=medium)—a little mark of pride from the hardware designer that also shows a spirit of playfulness... and in a place where vanishingly few people will ever notice!

I had to know more, so I asked Gordon Hollingworth about the design, and he referred me to Simon Martin, who was principle designer of this chip. He was happy to see someone noticed, and had a bit to say:

> The BGA ballout is just a bit of fun. The balls on the outside of the package contain the I/O signals and have to be carefully placed. The balls in the middle are just power and ground (and help with cooling) so can be placed in any arrangement.

I also asked a bit more about the chip design since, well, he designed it! And he mentioned that the SoC and DRAM have a silicon spacer to make sure the bond wires aren't crushed during manufacturing. And he also mentioned why they chose gold bond wires:

> It's a busy looking thing if viewed under X-Ray. Over 800 gold bond wires [...] We got a bit scared of using cheaper copper wires in the package and decided on the gold version to ensure a long life.

So there you have it! I also wanted to take a peek under the WiFi/Bluetooth module cover, to see what's inside, and it's very similar to the older board, just encased inside a metal shield:

{{< figure src="./raspberry-pi-zero-2-wh-wifi-undercover.jpg" alt="Raspberry Pi Zero 2 W WiFi Bluetooth undercover X-ray shot" width="600" height="600" class="insert-image" >}}

I'll get more into this next week, but the _actual chip_ used here is the `SYN43436`, made by Synaptics. It's very close to the `BCM43438` used in the 3 model B and Zero W, but it does require [dedicated firmware](https://github.com/raspberrypi/linux/commit/c52581ffa49b9c0e5de3349436c283fe20128073#diff-ffce630590e253b5f402e964a1085c5709e56a2ba5e060579fe68cfd87988fe7), and that threw me for a loop while working on a RetroPie build for the Zero 2 W!

Anyways, that about sums up the 'inside look' at the Zero 2 W—please check out [my YouTube review of the Raspberry Pi Zero 2 W](https://www.youtube.com/watch?v=lKS2ElWQizA) for more juicy design details.

## Performance

To help those who _don't_ enjoy sitting through videos, I'm also posting the performance benchmarks here:

{{< figure src="./pi-zero-2-w-benchmark.001.png" alt="x264 Encode phoronix benchmark results on Pi Zero 2 W" width="700" height="394" class="insert-image" >}}

I ran all these benchmarks using my [pi-general-benchmark](https://gist.github.com/geerlingguy/570e13f4f81a40a5395688667b1f79af) script, and this first one was interesting—due to the fact the Pi Zero W and Zero 2 W have 512 MB of RAM, it was hard to even get the benchmark to complete. The OOM (Out Of Memory) Killer was ruthless in killing the runs until I gave the Pi at least 512 MB of swap space on the slow microSD storage.

It's not showing a ton of speed, but another thing to note is the Pi Zero 2 can take an overclock of 1.2 or even 1.4 GHz with adequate cooling. I get more into thermals and efficiency in my video, but moving on to the next benchmark, the following become apparent:

  - The Pi Zero 2 W is 2x faster at base clock on 32-bit Pi OS.
  - The Pi Zero 2 W can finally run 64-bit Pi OS.
  - The Pi Zero 2 W can be 3-4x faster (or more!) running 64-bit Pi OS with a slight overclock.

Here's the result of an MP3 encode test:

{{< figure src="./pi-zero-2-w-benchmark.002.png" alt="MP3 Encoding Phoronix test benchmark results for Pi Zero 2 W" width="700" height="394" class="insert-image" >}}

And finally, `phpbench`:

{{< figure src="./pi-zero-2-w-benchmark.003.png" alt="phpbench phoronix benchmark results on Pi Zero 2 W" width="700" height="394" class="insert-image" >}}

You can expect everything to run at least twice as fast, sometimes 3-4x faster, on the Pi Zero 2 W with it's quad-core A53 chip. But RAM is definitely a limiting factor for many uses.

Two other things I tested were networking performance—since the upgraded CPU can make a difference there—and power consumption:

{{< figure src="./pi-zero-2-w-benchmark.004.png" alt="WiFi and Wired LAN networking performance on Pi Zero 2 W" width="700" height="394" class="insert-image" >}}

WiFi is about twice as fast, and Wired LAN performance with a Gigabit USB Ethernet adapter is about 25% faster. I should note that it still pales in comparison to the Pi 4, which doubles WiFi performance again, and has built-in 1 Gbps Ethernet!

Finally, here's power consumption as measured by a [PowerJive USB power meter](https://www.amazon.com/gp/product/B013FANC9W?ie=UTF8&psc=1&linkCode=sl1&tag=mmjjg-20&linkId=de369957687f9ac1089973da78a85e0d&language=en_US&ref_=as_li_ss_tl).

{{< figure src="./pi-zero-2-w-benchmark.005.png" alt="Pi Zero 2 W Power Consumption Benchmarks" width="700" height="394" class="insert-image" >}}

If you [turn off almost everything on the Pi Zero to reduce power consumption](https://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy), you can get the Zero 2 W down to about 100 mA, or 0.52W. The original Zero W could get down to about 80 mA, or 0.42W.

## Back side pads

On the back of the Pi Zero 2 W, there are a number of unlabeled pads that can be tapped into for things like composite video output or USB via pogo pins. Unlike the rest of the board's physical layout, the layout of these pads _has_ changed a bit, so some gear that relied on those pads being in a specific location will need to be changed.

Here's a simple image showing the pad locations with the Zero 2 W on top, and the Zero W on bottom:

{{< figure src="./pads-pins-bottom-pi-zero-2-w-differences.jpeg" alt="Pins and pads on bottom of Pi Zero 2 W in different locations than the pads on the Pi Zero W at bottom" width="640" height="618" class="insert-image" >}}

## Conclusion

The Zero 2 W is a nice upgrade over the Zero W, and makes some uses—like retro gaming or light duty tasks—a lot less painful. It's still no performance champ compared to the Pi 4, but it comes in with good features for a still-low price, and I can imagine it'll be hard to find one in stock for some time!

I'll be back next week with details on how I integrated the Pi Zero 2 W in a [Null 2](https://www.null2.co.uk) RetroPie gaming handheld build, so be sure to [subscribe on YouTube](https://www.youtube.com/c/JeffGeerling) and subscribe to this blog's RSS feed!

And if you haven't yet, go watch [the full YouTube review of the Raspberry Pi Zero 2 W](https://www.youtube.com/watch?v=lKS2ElWQizA).
