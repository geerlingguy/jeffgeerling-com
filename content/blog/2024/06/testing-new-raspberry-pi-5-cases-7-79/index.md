---
nid: 3387
title: "Testing new Raspberry Pi 5 Cases - $7 to $79"
slug: "testing-new-raspberry-pi-5-cases-7-79"
date: 2024-06-28T21:04:30+00:00
drupal:
  nid: 3387
  path: /blog/2024/testing-new-raspberry-pi-5-cases-7-79
  body_format: markdown
  redirects:
    - /blog/2024/testing-array-raspberry-pi-5-cases-7-79
aliases:
  - /blog/2024/testing-array-raspberry-pi-5-cases-7-79
tags:
  - case
  - enclosure
  - raspberry pi
  - reviews
  - video
  - youtube
---

Since the Pi 5's launch, a number of Pi case redesigns have launched, and there are a few new entrants with something to offer. Like Fractal's 'Baby North'... which, unfortunately, is only a prototype designed for their displays at Computex, and is not being planned for sale. At least not for now! I'll write more about this case later in this post.

{{< figure src="./fractal-baby-north-raspberry-pi-5-case.jpeg" alt="Fractal Baby North - Raspberry Pi 5 Case" width="700" height="auto" class="insert-image" >}}

The Pi 5's thermals are close enough to the Pi 4 that old cooling solutions work okay, but the port layout and inclusion of a power button means at least minimal redesigns are necessary.

Here are a few of the Pi 5 cases I've been testing (most for over a month, in various places), and my thoughts on each.

## Raspberry Pi 5 Case (official)

The [official case for the Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5-case/) is like a saltine cracker.

{{< figure src="./raspberry-pi-official-case_1.jpeg" alt="Raspberry Pi 5 official case" width="700" height="auto" class="insert-image" >}}

It _works_. It holds the Pi like a saltine holds peanut butter. But it's nothing to write home about. It's cheap, the power button works, all the ports are accessible, and a few HATs even work with it, but overall it's not easy to use if you have anything plugged into the top of the Pi, like a camera or any GPIO projects.

The ventilation isn't great, meaning the fan has to run a bit more than you might expect, _but_ the rubber feet hold it nicely on your desk. The best things? It's cheap, quick to put together, and it looks nice.

4/5 stars; it's the saltine of Pi cases.

## Fractal Baby North

Going entirely the _other_ way, form over function (but in the best way), there's Fractal's Baby North (see photo at top of post).

I _want_ to buy this. But I can't. This prototype was made for Computex. The reason they built it was to [so they could have a cute little box for the Pis they were using to play music](https://youtu.be/trKtxmdQO6s?t=498). It was a sparingly beautiful means to an end: promoting their $200 Scape headset. But I want one.

Woodgrain with a Pi 5? Perfect for my office's retro-themed area, or even my home media center!

It has warts like any prototype: the microSD card access door is a little flimsy, and the two front intake fans (little 40mm Noctuas!) are 12V, meaning you'll need to convert from 5V to 12V to run them (or try running them under-volted?).

This is the case we all _want_ for our Pis. I can only hope Fractal gets into the Pi case game... it wouldn't be the first high-end Pi case to exist (see the next section).

🪵/5 stars; I _would_ recommend it, but it's not for sale.

## Sunfounder Pironman 5

I am supposed to be receiving a [Pironman 5](https://www.sunfounder.com/products/pironman-5-nvme-m-2-ssd-pcie-mini-pc-case-for-raspberry-pi-5) sometime, but it's stuck in shipping.

{{< figure src="./pironman-5-sunfounder-pi-case.jpg" alt="SunFounder Ironman 5 Pi 5 Case" width="700" height="auto" class="insert-image" >}}

I'll update this section once I receive it, but it promises _everything_: RTC battery, tower cooler, dual RGB exhaust fans, OLED display on front, port breakout board to route all plugs to the back...

But there's one glaring problem: It's $79. A hefty sum for the unicorn of Pi cases.

But there _is_ a market for it. A small one, I mean there are also people crazy enough to buy a [$120 water cooling kit for the Pi 5](https://www.jeffgeerling.com/blog/2024/water-cooling-overkill-pi-5) too!

And of course, [Michael Klements](https://www.youtube.com/watch?v=GE_8MURePbo) has the OG design the Pironman drew inspiration from, and he even sells the [3D print files](https://www.etsy.com/listing/1304654740/raspberry-pi-4b-desktop-split-ssd-case) so you can make one too.

It's fun to see where the high end goes, just because some of the ideas can trickle down to other ones, like integrating an RTC battery into the case (something that's still pretty rare in Pi-land).

?/5 stars; since mine's stuck in the mail.

## EDATEC Fanless Cases

[EDATEC sells two fanless cases](https://edatec.cn/en/ac/pi5-case.html). Both completely surround the Pi with heatsink:

{{< figure src="./edatec-pi-fanless-case-for-pi-5.jpeg" alt="EDATEC Fanless Pi 5 Case" width="700" height="auto" class="insert-image" >}}

This is great for thermals, In fact I've been running their silver case next to my 3D printer for almost a month and it's been perfect. GPIO access is fine, but getting a camera plugged in is a bit of a pain. Same goes for any PCI Express HATs.

There's a tradeoff there. This design is better for compactness than convenience. These cases are best when running a Pi 5 without any extra attachments or if you need to avoid a fan for dust or noise reasons.

The difficulty using the Pi's ports sours things a little, but the price makes up for it: $7 for the open case, or $16 for the box.

4/5 stars; They're not perfect, but the price is good.

## Argon 40 Cases

Argon 40's long made some of the coolest Pi cases, and I still run a Pi 4 in one of their older cases next to my 3D printer at home.

They're durable, they break out all the ports to the back (at least the 'One' version), and they add on handy features like an IR receiver and color-coded GPIO headers. Or at least, well-labeled GPIO headers on the cheaper Neo 5 case.

I've been running a [Neo 5 M.2 case](https://argon40.com/products/argon-neo-5-m-2-nvme-for-raspberry-pi-5) as my retro Mac AppleTalk server (running [netatalk](https://netatalk.io)) for months, and besides setup being a little finicky, it looks and feels great.

{{< figure src="./argon-neo-5-case-open-pi-5.jpeg" alt="Argon 40 Neo 5 Pi 5 Case" width="700" height="auto" class="insert-image" >}}

The [regular Neo 5](https://argon40.com/products/argon-neo-case-for-raspberry-pi-5) is about the same, just without the finicky PCI Express adapter board underneath. The microSD card slot cover is a little flimsy, but otherwise, it's a solid case.

The [Argon One V3 M.2](https://argon40.com/products/argon-one-v3-m-2-nvme-case) takes up more desk space, but turns the Pi into something closer to the high end Rockchip boards—at least in terms of port layout on the back.

{{< figure src="./argon-40-one-v3-m2.jpeg" alt="Argon 40 One V3 M.2 Case for Pi 5" width="700" height="auto" class="insert-image" >}}

There's full-size HDMI, and even a headphone jack!

The NEO 5 M.2 is $38, and the One V3 is $49. Both are premium, but they're pricing's a little more down-to-earth than the Pironman.

5/5 for the Neo 5, I have no issues with that case.

4/5 for the Neo 5 M.2; it's finicky to put together.

But the Argon One V3 M.2? I'm won't rate it today. _Mine_ seems to work, but I've had a few people [mention theirs didn't](https://forum.argon40.com/t/solved-argon-one-v3-died-suddenly-and-wont-power-on/2849).

The One V3 is a more complicated case than the most others I tested. It has a more feature-packed expansion board inside, with it's own RP2040 microcontroller and board firmware. You might have to fiddle with firmware if you get an older board, so I still _like_ it, but I don't want to officially recommend it. At least not yet.

## Other cases

There are tons of other cases. Like there are _hundreds_ of [3D-printable cases](https://www.printables.com/search/models?q=raspberry%20pi%205%20case) on Printables. There are [DIN rail cases](https://www.printables.com/model/744135-raspberry-pi-5-snap-fit-case-for-din-rail), unofficial cases to [house 3rd party PCI Express HATs](https://www.printables.com/model/699129-case-for-raspberry-pi-5-with-pineberry-pi-hatdrive), and even wacky designs like an adapter for a [60mm Noctua fan](https://www.printables.com/model/642174-raspberry-pi-5-fan-case-60mm-fan-adapter) on the official case.

There are many other commercial cases too. Flirc has a [Pi 5 version](https://flirc.tv/products/raspberry-pi-5-case?variant=44801637286120) of _their_ fanless case, and Amazon has [tons of options](https://amzn.to/45GrL7a) for whatever price you want.

But the case I use most often is just a cheap acrylic tray I bought a decade ago. I bought a set of stackable trays, and I stuck some rubber feet on mine, so I can have the Pi 5 on top, with an active cooler and easy access to every port.

And using a tray like this also frees you to try different coolers, like [52Pi's Armor Lite](https://52pi.com/products/armor-lite-v5), or [Argon's THRML coolers](https://argon40.com/products/argon-thrml-30mm-active-cooler).

{{< figure src="./pi-5-ice-tower-cooler.jpeg" alt="Raspberry Pi 5 with Ice Tower 52Pi Cooler" width="700" height="auto" class="insert-image" >}}

You can even go wild with an [Ice Tower](https://52pi.com/products/ice-tower-cpu-cooler-rgb-led-light-cooling-fan-for-raspberry-pi-5), or Argon's [ridiculous 60mm tower cooler](https://argon40.com/products/argon-thrml-50mm-radiator-cooler)—it's the definition of overkill. But it also keeps the Pi's CPU almost ambient temperature... So if you have the space for it and $20 to spare, go for it!

## Video

I have a video covering all these cases, and you can watch it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/rV8v40MKFik" frameborder='0' allowfullscreen></iframe></div>
</div>

Note that I will try to update this blog post as I get new information or more testing done on some of these cases—I can't do that for the video :)
