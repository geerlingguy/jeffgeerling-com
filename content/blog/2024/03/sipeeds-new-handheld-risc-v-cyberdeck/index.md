---
nid: 3362
title: "Sipeed's new handheld RISC-V Cyberdeck"
slug: "sipeeds-new-handheld-risc-v-cyberdeck"
date: 2024-03-29T14:00:34+00:00
drupal:
  nid: 3362
  path: /blog/2024/sipeeds-new-handheld-risc-v-cyberdeck
  body_format: markdown
  redirects: []
tags:
  - cyberdeck
  - lichee console 4a
  - netbooks
  - reviews
  - risc-v
  - sbc
  - sipeed
  - video
  - youtube
---

**tl;dr**: Sipeed sent a [Lichee Console 4A](https://sipeed.com/licheepi4a) to test. It has a T-Head TH1520 4-core RISC-V CPU that's on par with 2-3 generations-old Arm SBC CPUs, and is in a fun but impractical netbook/cyberdeck form factor. [Here's my video on the Lichee Console 4A](https://www.youtube.com/watch?v=8qDGV6LTOnk), and [here's all my test data on GitHub](https://github.com/geerlingguy/sbc-reviews/issues/39).

{{< figure src="./sipeed-lichee-console-4a-hero.jpeg" alt="Sipeed Lichee Console 4A" width="700" height="auto" class="insert-image" >}}

Last year I tested the [StarFive VisionFive 2](/blog/2023/risc-v-business-testing-starfives-visionfive-2-sbc) and [Milk-V Mars CM](/blog/2023/getting-risc-v-again-milk-vs-mars-cm)—both machines ran the JH7110, a 4-core RISC-V SoC that was slower than a Pi 3.

Sipeed introduced the [Lichee Pi 4A](https://sipeed.com/licheepi4a) line of computers, offering a slightly newer T-Head TH1520 SoC, which is also 4-core, but uses faster C910 cores than the JH7110.

So how does it compare? Well, overall, it may be a pretty good RISC-V SoC, but in practice, at least underclocked as it is in the Lichee Console 4A, it's underwhelming (see my benchmarks later in the post).

That said, it's not _terrible_, but I'll quote the [Sipeed Wiki](https://wiki.sipeed.com/hardware/en/lichee/th1520/lcon4a/lcon4a.html#简介) when it comes to recommending who should buy this:

> Lichee Console 4A is mainly for RISC-V developers to experience development and use. It requires at least skilled Linux operating experience. Ordinary consumers cannot get started directly. in use. If you are an ordinary user without Linux experience, please do not buy.

The TH1520 can be clocked over 2 GHz, and in _some_ synthetic benchmarks quoted by Sipeed, it can perform even better than the Pi 4. But the Pi 4 is a 5-year-old SBC design based on an 8-year-old Arm SoC (BCM2711), so it's not _that_ impressive.

Especially considering the Lichee Console 4A's price tag: it starts at $375 for 8GB of RAM and 32GB of eMMC storage, and the configuration I was sent is the $429 model with 16GB of RAM and 128GB of eMMC.

As far as the netbook hardware goes, it's quite adequate:

{{< figure src="./sipeed-lichee-console-4a-ports-rear.jpeg" alt="Sipeed Lichee Console 4A - ports on rear" width="700" height="auto" class="insert-image" >}}

The rear has a single USB-A port, 12v DC power, mini HDMI, USB-C, and a Gigabit Ethernet port. Though there are caveats to almost all those ports' functionality:

  - The DC power port will charge the device when powered on or off, and will draw up to 30W from the wall, making the unit quite warm at the initial stages of charging.
  - Some reviewers have noted quirks with mirroring the display via HDMI. Extending the display doesn't seem possible right now.
  - USB-C can accept power input, but only while the device is booted.
  - The Ethernet jack is shallow-depth, and doesn't seem to retain the plug—the little retention clip wouldn't engage on any of the three cables I tested. It worked fine, but if you just tug on the wire, it will unplug.

{{< figure src="./sipeed-lichee-console-4a-ports-side.jpeg" alt="Sipeed Lichee Console 4A - ports on side" width="700" height="auto" class="insert-image" >}}

The side ports are handy: a headphone jack, another USB-A, and a microSD card slot. Nothing too crazy there. It _looks_ like there's a hole for a microphone, but I couldn't find a mic input using Audacity or the built-in pulseaudio mixer.

I also couldn't confirm whether there's a physical microphone inside, because four of the six phillips screws on the bottom were stripped completely from the factory (the screw metal is *very* soft), and I couldn't get inside. I have a tiny screw extraction set on the way to see if I can get inside...

There's also an NVMe slot in the bottom, but when I tried installing an SKHynix 2242 M.2 NVMe SSD, it was bumping slightly against one of the screw posts... to the point it didn't seem to seat perfectly all the way inside—thus `lspci` and `lsblk` showed no drive.

You can order a variant for $519 with a 1TB NVMe SSD pre-installed, so I have to imagine they validated the design... maybe it only works for certain SSDs?

{{< figure src="./sipeed-lichee-console-4a-keyboard-redpoint-trackpoint.jpeg" alt="Sipeed Lichee Console 4A - RedPoint tracking nub and keyboard detail" width="700" height="auto" class="insert-image" >}}

For portability, the keyboard and tracking device need to be reliable. The keyboard and 'RedPoint' (not to be confused with 'TrackPoint') are definitely a keyboard and an input device.

I used an Eee PC in college, so I'm used to a cramped keyboard layout, and the tradeoffs you make for that portability... but some of the key placements—most notably `.` (period) and `'` (apostrophe) are still difficult to hit touch-typing after using it for a couple weeks.

I _can_ type faster than on my iPad's touch keyboard, so that's something... but it's not a great keyboard layout (IMO).

The RedPoint tracking nub required far too much force to use—my finger would get a bit tired after only 5-10 minutes of use. And it's not nearly as precise as the TrackPoint nubs I'm used to on IBM/Lenovo laptops.

The screen is also a touchscreen, but the included Debian 12 environment with Xfce is not designed for touch control, so besides drawing, it's a frustrating experience trying to use the built-in input methods. Luckily I can pop an external mouse onto it using the USB port on the side... but Bluetooth didn't seem to work for me. I would get error messages when trying to enable Bluetooth, and once I started the Bluetooth daemon, the Bluetooth device manager would just crash on launch (with no logged messages).

The included speakers are audible, but quiet and tinny, as to be expected in a tiny device like this. It only got up to maybe 35-40°C on the bottom even while charging and running benchmarks, so thermally, my unit seemed to be okay. They could probably clock the SoC a bit higher, but I'm guessing their thermal solution (a little heat pipe sticking on the SoC, with a fan blowing across the end) is not able to guarantee no throttling at higher clocks.

The fan runs all the time, and there's no lid close switch, so if you close the lid, it won't turn off the display or go to sleep.

There are plenty of quirks, but that's not unexpected, with a dev-oriented machine like this. It's just... a bit hard to swallow at around $400!

## Performance

The bigger question for me was how well the C910 CPU cores perform. Even underclocked at 1.5 GHz, can this thing do better than the painfully-slow JH7110?

{{< figure src="./lichee-console-4a-cpu-performance.png" alt="Lichee Console 4A - CPU Performance" width="700" height="auto" class="insert-image" >}}

Yes, it can! Though it's still not coming even close to the Pi 4—much less the Pi 5 that came out last year. Clocked higher, it would probably come closer, but I don't think it would match the Pi 4 even, in some of these benchmarks.

In normal use (browsing the web, using GIMP and office apps, playing games), the device does feel more on par with a Pi 3 than a Pi 4—which is to say, a little painful for desktop use. Somewhat surprisingly, a _ton_ of software is available and working without any issues on RISC-V, from KiCad to SuperTuxKart to Kdenlive. It's smoother than Arm desktop support was 10 years ago, when it was about as mature, so that's nice. It's just... slow.

But that speed could be worth it, if like Arm, it was slow but more efficient...

{{< figure src="./lichee-console-4a-cpu-efficiency.png" alt="Lichee Console 4A - CPU Efficiency" width="700" height="auto" class="insert-image" >}}

...unfortunately it's not. Just like the JH7110, the measured efficiency is underwhelming.

To test this on the laptop, I ran benchmarks twice, letting the battery fully charge for a period of hours, confirming the power adapter was drawing less than 0.5W by the end of the charge cycle. Then I booted the laptop, ran the test, and averaged the power consumption over the course of the test.

The Imagination PowerVR GPU—a "BXM-4-64" isn't _amazing_, but it's adequate, and hits GLmark2 scores similar to a Pi 4:

{{< figure src="./lichee-console-4a-gpu-performance.png" alt="Lichee Console 4A - GPU Performance" width="700" height="auto" class="insert-image" >}}

I could get 30-40 fps with SuperTuxKart, which was definitely playable (especially since it used the keyboard only, and not the RedPoint tracking nub), and over 100 fps with Doom (dsda-doom), though the experience playing that with RedPoint was painful:

{{< figure src="./lichee-console-4a-dsda-doom.jpg" alt="Lichee Console 4A - dsda-doom gameplay" width="700" height="auto" class="insert-image" >}}

It was much more enjoyable playing with an external mouse.

Overall, the Lichee Console 4A is a novel idea in the RISC-V space, but too expensive for me to recommend, for the hardware you get. I would rather recommend the Lichee Pi 4A if you're just looking into RISC-V support with the C910 cores, and don't need a tiny ultraportable device. There are too many little tradeoffs and quirks for too high a price, even for a dev machine.

You can watch my full video review of the Lichee Console 4A on YouTube:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/8qDGV6LTOnk" frameborder='0' allowfullscreen></iframe></div>
</div>
