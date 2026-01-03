---
nid: 3507
title: "The Arduino Uno Q is a weird hybrid SBC"
slug: "arduino-uno-q-weird-hybrid-sbc"
date: 2025-10-31T14:01:28+00:00
drupal:
  nid: 3507
  path: /blog/2025/arduino-uno-q-weird-hybrid-sbc
  body_format: markdown
  redirects:
    - /blog/2025/arduino-uno-q-weird-sbc
aliases:
  - /blog/2025/arduino-uno-q-weird-sbc
tags:
  - arduino
  - arm
  - linux
  - microcontroller
  - qualcomm
  - reviews
  - sbc
  - uno
  - video
---

{{< figure src="./arduino-uno-1-in-hand.jpg" alt="Arduino Uno Q" width="700" height="394" class="insert-image" >}}

The [Arduino Uno Q](https://www.arduino.cc/product-uno-q) is... a weird board. It's the first product born out of [Qualcomm's buyout of Arduino](/blog/2025/qualcomms-buying-arduino-–-what-it-means-makers).

It's like if you married an Intel CPU, and a Raspberry Pi RP2040 microcontroller—oh wait, [Radxa's X4 did that](/blog/2024/radxa-x4-sbc-unites-intel-n100-and-raspberry-pi-rp2040).

Arduino even tried it before with their old [Yún](https://docs.arduino.cc/retired/boards/arduino-yun/) board, which had Linux running on a MIPS CPU, married to an ATmega microcontroller.

The Uno Q isn't quite a Raspberry Pi, but it looks like one when you squint at it. And it's not quite an Uno, but it does a pretty good job masquerading as that, too.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Vz3pD3_CDUE" frameborder='0' allowfullscreen></iframe></div>
</div>

Really, it's a tiny computer in the shape of an Arduino Uno, with a bunch more IO than you might be used to.

What is it _best_ for? That's a good question. Maybe robotics, where you need to run a lightweight machine vision model while you control a bunch of servos in real-time?

Maybe light industrial controls, where you could almost get by with just a microcontroller, but you wanna run some remote control through Linux?

Whatever the case, I ran this thing through my gauntlet of SBC benchmarks (see my [full results here](https://github.com/geerlingguy/sbc-reviews/issues/83)), then I also tried it out as a hybrid computer-plus-microcontroller, and I have to say, if there's one word to describe it, it's... _weird_.

## Hardware

Starting on the computer side, it runs a Qualcomm Dragonwing SoC. It has some older Arm A53 CPU cores, a tiny little Adreno iGPU, and has 2 gigs of RAM and a 16 gig eMMC storage chip.

{{< figure src="./qualcomm-qrb2210-arduino-uno-q.jpg" alt="Arduino Uno Q Dragonwing Qualcomm QRB2210 SoC" width="700" height="394" class="insert-image" >}}

In practice, those specs are pretty limiting, but it's still enough for many applications. Also, a 4GB RAM model should be coming later.

But on the Linux side, you get Debian, and right now _only_ Debian, and the OS it comes with launches you straight into Arduino's new [App Lab](https://docs.arduino.cc/software/app-lab/).

The App Lab gives you a unified IDE. Apps can run _Python_ for the Linux side, and Arduino's flavor of C++ for the MCU side. This means you can have your custom code and what Arduino is calling 'Bricks', that unify the two sides of the board.

The MCU has access to all the pins on the top, but on the SBC-side, you get everything but wireless out of a single USB-C plug. And that includes power, HDMI, USB, everything.

{{< figure src="./arduino-uno-q-back-high-speed-connectors.jpg" alt="Arduino Uno Q high speed connectors on bottom" width="700" height="394" class="insert-image" >}}

There are also some high speed connectors on the bottom (pictured above), but so far I haven't seen any boards that use them, for like camera connections or extra GPIO.

The lone USB-C port being the only connection right now is a blessing and a curse.

One intention is for the Q to be an educational board: students plug one in at a table and work on robotics. Except if you don't have a display with a built-in USB-C hub, now you need a:

  - USB-C power supply
  - USB-C hub with HDMI
  - A monitor and a keyboard

Compared to a Raspberry Pi, it _is_ nice to have one USB-C cable with display, power, and IO, if you want that—and I really hope a future Raspberry Pi 6 could do it. But it's also nice to have physical ports for display and USB devices onboard as well. Even a Pi gets to be a bit of a mess, with ports along two edges—but the Uno Q sprawls even further with a mandatory USB-C hub.

And on the software side, it's nice on the Pi to be able to use GPIO in Python, instead of having App Lab run hybrid Python/C++ apps.

But we're getting a little ahead of ourselves.

{{< figure src="./arduino-uno-q-benchmark-1-geekbench-6.jpg" alt="Arduino Uno Q - Benchmark - Geekbench 6" width="700" height="394" class="insert-image" >}}

Getting back to the hardware, I ran tests like Linpack, Geekbench, and more. And besides the limited 2 gigs of RAM being a bit of a pain, the Linux performance was about on par with a Pi 3 B+ or Pi 4.

This won't be a daily driver for browsing the web or watching YouTube.

{{< figure src="./arduino-uno-q-benchmark-2-hpl.jpg" alt="Arduino Uno Q - Benchmark - HPL" width="700" height="394" class="insert-image" >}}

Most things are a bit slow, like they are on older Arm SBCs, and even downloading and starting the Docker containers App Lab sets up to run the apps you build, is a bit sluggish.

{{< figure src="./arduino-uno-q-benchmark-3-hpl-efficiency.jpg" alt="Arduino Uno Q - Benchmark - HPL Efficiency" width="700" height="394" class="insert-image" >}}

Energy efficiency is decent, with the board pulling .5 watts at idle, up to 2-3 watts at full power. _However_, if you're just using the MCU portion, it doesn't seem like you can just power that without the full Linux stack running.

I even tried shutting down in Linux, multiple ways, like through the GUI or via SSH, and every time it'll just power back on again... so I can't find a way to just run the MCU and not Linux.

I could get my older Uno running at a few dozen _milliwatts_, but because I have to run the full Linux stack too, the Q needs at least 10-100x the power. So battery use will be limited, like with a full Raspberry Pi.

I keep comparing it to a Raspberry Pi, too, because the board costs $44 for the 2GB version. That gets you a decent little board, but the Pi _five_, which is _2-4x faster_, at the expense of another couple watts of power draw, is also $45 (also for 2GB).

And then you have the Radxa X4 I mentioned earlier, which is _faster still_, and it starts at _$60_. (Although the price for those of us living in the US has increased due to tariffs.)

So _just taking the Uno Q as an SBC_, it's not a good value. It's not horrible, and I was happy to see most things in Debian working out of the box. But it's definitely not the best SBC you can buy in the 40-50 dollar price range.

## Software

But this _isn't_ just an SBC. Or at least that's the message Arduino and Qualcomm are pushing.

This is a device that gives you "[modern AI at the edge](https://docs.arduino.cc/hardware/uno-q/)," according to the documentation.

But even there, it can only run the [tiniest of models](https://github.com/geerlingguy/sbc-reviews/issues/83#issuecomment-3446866713), especially if you're talking LLMs, and it runs them slower than most other SBCs in the same price range. And managing apps between Python and C++ is still kind-of annoying.

{{< figure src="./arduino-app-lab-blink-led.jpg" alt="Arduino App Lab - Blink LED python example" width="700" height="394" class="insert-image" >}}

It still feels like you're managing two separate things, though App Lab _is_ an improvement over just doing it all on your own like you have to do on the Radxa. But it's not as easy as on the Pi, where you can just tap into GPIO from anywhere.

> While I was finishing up this post, I saw [this video from Gary Explains](https://www.youtube.com/watch?v=ngdz6xvYiuU), where he details some of the annoyances I also encountered, with programming the Uno from both the Uno Q itself, or through a connected computer. I didn't get _too_ deep with the Uno Q, but I was having trouble with serial console output, having a stable board connection, etc... and I thought it was a PEBKAC, but apparently it might just be the beta-ish nature of App Lab as it currently exists.

I haven't been able to test things like CSI camera and DSI display functionality, because so far I haven't seen any boards that tie into the high speed connectors on the bottom. Supposedly those are coming, but like with most Shields, you'll end up paying another $20, $40, or $50 just to have some of the features you might get out of the box on other SBCs, like USB, Ethernet, camera and display connectors, or built-in HDMI.

I guess I just don't see this thing lighting the world on fire.

It's nice that it exists, especially if you have an Arduino-centric course or robotics pipeline already, and you want the convenience of Linux for remote access or running a tiny ML model. But after using it for a couple weeks, I just don't see the value for _my own_ work. And I can't find many reasons to recommend it unless you're already in the Arduino ecosystem.

## Open Source

I think the immediate reaction from many in the maker community to Qualcomm's buyout was, "Arduino is dead to me." And I get that. I feel the same way, since so many buyouts result in the long-term decay of what made an acquired company beloved.

A lot people wondered if boards would still be open source, and I'm happy to report that _that_, at least, hasn't changed. The [board schematics and step files were up](https://docs.arduino.cc/hardware/uno-q/) on launch day[^designfiles].

{{< figure src="./arduino-uno-q-box-open-source-is-love.jpg" alt="Arduino Uno Q box - Open Source is Love resistors" width="700" height="394" class="insert-image" >}}

Arduino doesn't just stamp their box with 'Open Source is Love' as a platitude. But the bigger question is: can they convince Qualcomm to be the same? I'm doubtful.

Having the schematics is great, but only so far as you could build your _own_ board from scratch. To do that, you need all the main chips. Is the Dragonwing SoC available to buy?

Well... it looks like it _might be_, at least at some point. So that's good. Over on Digikey, I found this listing for the [QRB2210](https://www.digikey.com/en/products/detail/qualcomm/QRB-2210-0-NSP752-TR-00-0/27904331?s=N4IgTCBcDaIIoCUBCYwEYAMIC6BfIA), and it even has a full [datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/7554/QRB2210.pdf) which is... more than I can say for the Broadcom chip on the Raspberry Pi.

So who knows?

Arduino's strengths are software, community, and support, just like with the Raspberry Pi. So could they make this thing work in the long run? Maybe. The biggest question I have is whether Qualcomm will keep putting resources into it, or if they see some faltering first steps and just drop it [like Intel did with Edison](https://www.theregister.com/2017/06/20/intel_joules_edison_galileo/).

## Conclusion

In conclusion, this board is _weird_. I have a lot more about my experience using it, using App Lab, and benchmarks [over on my SBC Reviews website](https://sbc-reviews.jeffgeerling.com).

I do hope this isn't a one-and-done, because it's good to have more players in the SBC game, especially with the support and open source push Arduino is known for.

[^designfiles]: Though as [@aurimasniekis points out on X](https://x.com/aurimasniekis/status/1983541675176886351), the full PCB _design_ files aren't included currently.
