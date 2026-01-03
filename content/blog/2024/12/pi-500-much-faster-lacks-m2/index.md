---
nid: 3426
title: "The Pi 500 is much faster, but lacks M.2"
slug: "pi-500-much-faster-lacks-m2"
date: 2024-12-09T08:00:02+00:00
drupal:
  nid: 3426
  path: /blog/2024/pi-500-much-faster-lacks-m2
  body_format: markdown
  redirects: []
tags:
  - linux
  - pi 400
  - pi 500
  - raspberry pi
  - reviews
  - sbc
  - video
  - youtube
---

Raspberry Pi this morning launched the [Pi 500](https://www.raspberrypi.com/products/raspberry-pi-500/) and a new [15.6" Pi Monitor](https://www.raspberrypi.com/products/raspberry-pi-monitor/), for $90 and $100, respectively.

{{< figure src="./pi-500-monitor-hero.jpeg" alt="Pi 500 setup with monitor on desk" width="700" height="auto" class="insert-image" >}}

They're also selling a Pi 500 Kit, complete with a Power Supply, Mouse, and micro HDMI to HDMI cable, for $120. This is the first time Raspberry Pi is selling a complete package, where every part of a desktop computer could be Pi-branded—and makes me wonder if uniting all these parts into one could result in an eventual Pi Laptop...

Before we get too deep, _no_, the Pi 500 does not include a built-in M.2 slot. _Sort-of_.

{{< figure src="./pi-500-pcb-top.jpeg" alt="Pi 500 PCB top side" width="700" height="auto" class="insert-image" >}}

I posted a [full teardown of the Pi 500](https://www.youtube.com/watch?v=omYWRb1dLA4), alongside my [full review of the Pi 500 and Pi Monitor](https://www.youtube.com/watch?v=5YfJWYELA3k). After popping the seam with a spudger, I was greeted by what _looked_ like an M.2 slot... except it was missing an actual _socket_. It had pads for one, and indications for 2230, 2242, 2260, and 2280-sized NVMe SSDs... but the connector isn't present.

I quickly ordered some [M.2 sockets from DigiKey](https://www.digikey.com/en/products/detail/attend-technology/123A-30M00/23626211) and soldered one on—quite poorly, I may add.

{{< figure src="./pi-500-m2-socket-install.jpg" alt="Pi 500 M.2 socket installation" width="700" height="auto" class="insert-image" >}}

But that did not work. I realized after finishing up my work that none of the M.2 power circuit pads on the _underside_ of the board are populated, thus the slot gets no power. There are also a couple missing capacitors on the matched PCIe traces coming from the BCM2712 SoC.

Also, if you peek at the _left_ side of the Pi 500's PCB, there are a bunch of empty pads obviously meant for a PoE (Power over Ethernet) circuit!

It seems obvious this PCB was intended not only for the features delivered on the Pi 500, but maybe something more—a Pi 500 'Pro' (or maybe 'Pro Max', lol) with PoE and NVMe support. But why not populate M.2 circuits on the Pi 500 that's shipping _now_?

I asked, and Raspberry Pi responded:

> Those features [PoE and M.2] are present to give us some flexibility to reuse the PCB in other contexts. We feel the feature set we've picked for the Pi 500 is the right one.

The Pi 500 also increased in price from the Pi 400—$90 versus $70—though it brings 2-3x faster speeds _for nearly every feature_, doubles the RAM to 8GB, and tacks on a 32GB A2 microSD card.

So as I mention in my video, it's not a _bad_ value... but it's not quite the instant-buy it would be (despite the lack of an M.2 slot) if it remained at the $70 price point. The full 'Computer Kit' also had such a round price point of exactly $100.

Why do I care about the missing M.2 slot so much? Because I still believe [microSD cards' SBC days are numbered](/blog/2024/microsd-cards-sbc-days-are-numbered). But as it is not present, I'll move on to reviewing what _is_ present!

In lieu of the missing M.2, Raspberry Pi is including a 32 GB A2-class microSD card (with Pi OS pre-installed). Despite [Raspberry Pi not supporting A2 features in the past](/blog/2019/a2-class-microsd-cards-offer-no-better-performance-raspberry-pi), earlier this year [they added support for A2 Command Queueing](/blog/2024/numa-emulation-speeds-pi-5-and-other-improvements), vastly improving random IO performance.

It pales in comparison to NVMe performance (and high-capacity microSD cards are usually double the price of a much faster NVMe SSD...), but it's not _nothing_, I guess.

{{< figure src="./pi-500-bcm2712-soc.jpeg" alt="Pi 500 SoC BCM2712" width="700" height="auto" class="insert-image" >}}

Glancing at the other parts of the Pi 500's PCB, the whole middle section is nearly identical in layout to a Pi 5, probably saving on design costs, and then for the keyboard input, Raspberry Pi switched to using their own microcontroller, the RP2040. (RP2040 for peripheral support seems to be a trend, lately—I've spotted it on the MNT Reform trackball module, the Positron 3D printer control board, the System76 Launch keyboard, and even inside the System76 Thelio Astra I'm testing, on an IO/Fan controller!

## Pi 500 Overview (and comparison to Pi 400)

{{< figure src="./pi-400-500-ports.jpg" alt="Pi 400 Pi 500 Ports on back" width="700" height="auto" class="insert-image" >}}

Externally, at least on the rear, the ports are identical—save for the USB ports on the Pi 500 having independent USB 3.0 buses (for 2x5 Gbps, instead of a shared 5 Gbps of bandwidth). The layout is changed, but external I/O is the same (the Pi 400 is the red and white model in the picture above).

{{< figure src="./pi-500-keyboard-top.jpeg" alt="Pi 500 plugged in from above" width="700" height="auto" class="insert-image" >}}

Looking at the top, the keyboard layout and printing has changed a bit. The keyboard itself is a different design, with a slightly better feel (though 'feel' is somewhat subjective), but it's still a bit 'Chromebook' feeling (the key action has a midrange laptop feel). It's serviceable, and better than the Pi 400's keyboard, but not amazing.

The bigger improvement is the new dedicated power key, in the top right corner, where it should be. The Pi 400 had a strange setup where the function/power key was a couple over to the left, and I never got used to it.

Now, there's an LED that's green when the Pi 500 is on, and red when off. The power button works the same as the Pi 5 power button, with a long press forcing a shutdown.

After some [exhaustive benchmarking](https://github.com/geerlingguy/sbc-reviews/issues/60), I found the Pi 500's performance to be within a margin of error from the Pi 5, at least for any normal benchmarking. Under extreme load for 30+ minutes, I didn't see any thermal throttling, but performance was slightly lower on the Pi 500 compared to my Pi 5 in that instance.

{{< figure src="./pi-500-vs-400-thermals.jpg" alt="Pi 500 vs Pi 400 - Thermals" width="700" height="auto" class="insert-image" >}}

Thermally, the Pi 500 uses a large heatsink that also provides internal structure to the plastic case. It weighs nearly the same as the Pi 500, and I saw temperatures consistently 6-8°C warmer on the Pi 500's SoC, but the keys were never noticeably warm, even after a lot of benchmark runs:

{{< figure src="./pi-500-thermals.jpg" alt="Pi 500 thermals" width="700" height="auto" class="insert-image" >}}

The heatsink spread the heat out enough it didn't have a burn-your-fingers hot spot, like I remember back in the Intel MacBook days. But the passive heatsink can't keep up with 3.0 GHz overclocking. For that, you'd need to figure out custom active cooling, or a way to get more ventilation inside the plastic case. I was able to overclock to 2.8 GHz with moderate workloads, but 3.0 GHz resulted in severe thermal throttling after just a few minutes of benchmarking.

Compared to the Pi 400, the Pi 500 at its default 2.4 GHz clock is consistently 2-3x faster. The same speedup seen going from the Pi 4 to Pi 5, or CM4 to CM5:

{{< figure src="./hpl-pi500-pi400.jpg" alt="Pi 500 vs Pi 400 HPL and Power Efficiency" width="700" height="auto" class="insert-image" >}}

Raspberry Pi also _just_ released a software update to [tweak SDRAM timings](/blog/2024/raspberry-pi-boosts-pi-5-performance-sdram-tuning), resulting in an additional 6-18% speedup, depending on the workload (multi-core workloads benefit the most, alongside now-default [NUMA emulation](/blog/2024/numa-emulation-speeds-pi-5-and-other-improvements)).

## Pi Monitor

Raspberry Pi also launched a new $100 'Pi Monitor' today. It's a 15.6" IPS LCD, and it can be powered either directly off the Pi's USB port (at 60% brightness and 60% volume), or via an external USB-C charger (for 100%).

I measured the Pi Monitor's power draw (at the wall, using Raspberry Pi's own USB-C power adapter), and it seemed to pull between 5-5.5W while in use at 100% brightness, and 4-5W at 60% brightness. When the Pi 500 was powered off, the monitor didn't draw enough current to register on my ThirdReality Smart Outlet.

{{< figure src="./pi-monitor-buttons-back.jpeg" alt="Pi Monitor buttons and LED on back" width="700" height="auto" class="insert-image" >}}

The hinge mechanism on the back offers a variety of viewing angles, and can even be flipped up to reveal nail mounts, if you want to just pop a couple nails in a wall and hang it on there!

But the back is also the location of all the controls and the power LED—an odd choice in the latter case, because I don't normally turn around my monitor to check if it's on or has power! (See above).

Luckily, the controls are intuitive, and easy to feel without looking—there's a large power button across the bottom, and then separate buttons for volume and brightness up and down.

The tiny built-in speakers are quite tinny, and only audible in a quiet place, but they'd do in a pinch. The better option is to plug headphones or speakers into the headphone jack on the back—it breaks the audio out from the Pi's HDMI output, which is handy for Pi 5 / Pi 400 / Pi 500 users especially, since those models have no analog audio jack!

{{< figure src="./pi-monitors-vesa-mount-setup.jpg" alt="Pi Monitor VESA mount dual setup portrait" width="700" height="auto" class="insert-image" >}}

The biggest gripe I have with the monitor (and it's a small one, in the grand scheme of things) is the VESA mount option. It's okay... but a mounting plate covers up the port area entirely, so if you ever need to change out a cable or plug in headphones, you have to remove the VESA mount entirely. It also makes installation more challenging, especially if your VESA mount stand doesn't have a detachable mounting plate!

## Pi 500 Usage

{{< figure src="./pi-500-coding-workstation-setup-drupal-development-monitor-portrait.jpg" alt="Pi 500 and dual monitor portrait coding session setup" width="700" height="auto" class="insert-image" >}}

But _because_ Raspberry Pi now makes all the hardware someone could conceivably require to build an all-Pi-battlestation, I asked if they'd send a second monitor.

I built a dual-monitor Pi workstation, with one monitor in portrait (it's easy enough using the Screen Configuration tool in Pi OS), and worked on updating the code on my Drupal website (the very one you're reading!).

The Pi 500 is snappy, and all the containers and tools I require for web development (Docker, Sublime Text, Firefox, PHP, MySQL, etc.) worked perfectly.

The 8 GB of RAM is slightly limiting, as running multiple containers and multiple apps can quickly load that up and hit swap—which is unbearably slow on the microSD card.

What I wonder, then, is if Raspberry Pi would be willing to build a "Pro" or "Pro Max" version of the Pi 500. Give us everything: an M.2 slot, easier opening of the case, a nicer keyboard, PoE+ support, and 16 GB of RAM (apparently [a 16GB CM5 will come 'in 2025'](https://www.raspberrypi.com/news/compute-module-5-on-sale-now/)).

If they could keep the price down, that'd be a worthy first computer for a lot of aspiring developers—maybe this generation's [Commodore 64](https://en.wikipedia.org/wiki/Commodore_64). It still won't hold a candle to my Mac Studio, but I wasn't hampered at all, working on my Drupal codebase on the Pi 500. (Media work is different—I still can't do even the basics of my YouTube/photography work with any kind of speed on low-end Arm/Linux computers).

Of course, my Mac Studio doesn't fit inside a keyboard.

## Benchmarks, Teardowns, and More...

As mentioned above, I made a series of videos; the main video with even more benchmarks and test data, is embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/5YfJWYELA3k" frameborder='0' allowfullscreen></iframe></div>
</div>

In addition, you can view my [teardown of the Pi 500](https://www.youtube.com/watch?v=omYWRb1dLA4), or similarly, my [teardown of the Pi Monitor](https://www.youtube.com/watch?v=CnBu1wuoWew).
