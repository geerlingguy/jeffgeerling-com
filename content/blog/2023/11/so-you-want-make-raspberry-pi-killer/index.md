---
nid: 3328
title: "So you want to make a Raspberry Pi killer..."
slug: "so-you-want-make-raspberry-pi-killer"
date: 2023-11-22T15:02:59+00:00
drupal:
  nid: 3328
  path: /blog/2023/so-you-want-make-raspberry-pi-killer
  body_format: markdown
  redirects: []
tags:
  - clones
  - cm4
  - compute module
  - raspberry pi
  - sbc
---

{{< figure src="./raspberry-pi-cm4-clone.jpg" alt="Raspberry Pi CM4 Clones stacked up" width="700" height="auto" class="insert-image" >}}

I'm in the unique position of owning a collection of Raspberry Pi Compute Modules 4 (CM4).

I also own at least one of every production CM4 clone in existence.

This sets up a quandary: if I have _the real thing_, what motivation do I have to care about the clones?

There are [_hundreds_ of CM4 carrier boards](https://pipci.jeffgeerling.com/boards_cm) that do everything from restoring retro game consoles to monitoring remote oil rigs in highly-explosive environments.

Since launch, the CM4 has been difficult—and since early 2021, _impossible_—to acquire. The supply constraints are well documented, and I'm sure a few comments will lament the situation. But the CM4 is [trickling back to 'in stock'](https://rpilocator.com/?cat=CM4) at many suppliers (about how the Pi 4 was a couple months ago).

This lines up with the [timeline Eben Upton gave](https://www.tomshardware.com/news/raspberry-pi-ceo-million-unit-months-are-ahead) when I [interviewed him](https://www.youtube.com/watch?v=-_aL9V0JsQQ) in May.

But because of the lengthy shortage, other companies built their own CM4-compatible SoMs (System-on-Modules). For many, those clones were the _only_ way to participate in the SoM revolution brought about by the CM4.

So I've been testing them, methodically. All my results are posted on my [sbc-reviews](https://github.com/geerlingguy/sbc-reviews) GitHub repo. In many of the linked issues, other SBC (Single Board Computer) users offered valuable insights regarding performance, design, and stability.

But I haven't given a broad overview in one cohesive piece, so I posted a video where I do just that:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/KghZIgkKZcs" frameborder='0' allowfullscreen></iframe></div>
</div>

In _this_ blog post, however, I take a different tack: after experimenting with dozens of Pi 4 and CM4 clones, what would it take to make a _true_ Raspberry Pi killer?

For every commenter who says "Raspberry Pi abandoned the maker community during the shortage, I'll never buy one again," there are a thousand Pi sales to other makers. What would it take to turn that on its head?

What would an SBC maker need to do to truly unseat the Raspberry Pi from the throne?

## Hardware

This is deceptively easy. Build hardware that's better (faster, more efficient, and more feature-packed) than what's on the Raspberry Pi. It's been done, many times over.

The Pi's hardware shortcomings are well-known—and often highlighted by alternative SBC advocates:

  - The locked-down proprietary Broadcom firmware
  - The quirky VideoCore GPU-based boot process (see first point)
  - The slower-than-Rockchip-flagship 4-core Broadcom CPUs
  - The dearth of hardware encoders and decoders
  - The lack of AI coprocessors (no built-in NPU)
  - The integrated Broadcom WiFi with it's notoriously annoying drivers
  - (For Pi 5, not CM4) The decision to recommend an oddball 5V 5A power supply
  - Only one lane of PCIe Gen 2 for high-speed expansion
  - (Except Pi 5) no built-in RTC, and no onboard M.2 expansion slot

There's also only one RAM chip on a Pi, so you could gap the Pi on memory bandwidth, using two RAM chips like the Rock 5 B does.

But the devil's in the details. It's really _peripherals_ where Raspberry Pi hardware shines. Even through multiple BCM generations, and a transition to a custom RP1 chip, most interfaces on the Pi _just work_, whether that's GPIO, I2C, SPI, USB, Ethernet, Bluetooth, MIPI CSI/DSI, UART, or whatever.

There are small exceptions, but hardware interfaces that have good drivers, well-known quirks, and thorough documentation—that might just be Raspberry Pi's greatest hardware moat.

And despite the quirky GPU, the Raspberry Pi will output a picture on nearly anything you plug it into, even older DVI monitors, CRTs, and other oddball displays.

So on the hardware front: beat Raspberry Pi in speed, efficiency, and features. But focus on a _long-term_ strategy of consistency in hardware interaction. Sometimes that means devoting hard engineering hours to patching things in Linux, or rewriting drivers. And that brings me to...

## Software (specifically, Linux)

Raspberry Pi devotes engineering resources to Linux kernel development. They have device trees (detailed descriptions of their hardware so Linux can support it) ready to go even during _alpha_ testing of the boards. Some SBC makers don't have complete, working device trees even months _after_ public launch!

They maintain multiple forked versions of the Linux kernel, and track upstream development. When the Pi 5 launched, Pi OS was already running the 6.1.x LTS kernel. The 6.6.x LTS—which was _just_ announced—is already being explored in [Raspberry Pi's fork](https://github.com/raspberrypi/linux/tree/rpi-6.6.y).

Raspberry Pi has a first party OS _that's actually good_, and they devote a ton of time and effort into making their hardware run with the latest Linux kernel versions.

Many alternative SBCs run older kernels like 5.10 (or in one case, ancient 4.19!), and that can cause it's own problems. SBC makers don't take full ownership of their OS, or don't have the resources to maintain a broad set of compatibility, so they lean on community distributions like [Armbian](https://www.armbian.com) to do the work for them.

In some cases, a decent Android release may be given, and maybe an old, unmaintained Linux image, and that's it. Crickets on follow-up releases even as the board is still sold brand new at retailers!

Armbian is amazing, and is a lifeline for many of these boards. But to beat the Raspberry Pi, community distros are not enough. (Though I am happy to see [many manufacturers directly support the distro](https://www.armbian.com/partners/).)

The other main software problem that must be matched or beat is drivers and third-party compatibility. Raspberry Pi has momentum due to their existing base, but their engineers [go out of their way to enable third party accessories](https://forums.raspberrypi.com/viewtopic.php?p=2128089#p2128089) even when the third party manufacturers abandon support. That's customer-centric software support!

It is hard to match the level of active Linux involvement Raspberry Pi maintains at this point, especially for smaller, hardware-focused companies. (Some do a worthy job of upstreaming things into 'mainline' Linux, though that is a _very_ lengthy process!)

One area where you could sidestep Raspberry Pi's advantages is in standardization, especially around boot and platform enablement.

Build an SBC with full UEFI/u-boot/SystemReady certification, without some of the [quirks](https://www.cnx-software.com/2021/10/16/raspberry-pi-4-rockchip-rk3399-sbcs-get-arm-systemready-ir-certification/) of the Pi's boot sequence. Leverage chipmakers to better support Linux, and work together with them to make all their hardware interfaces work _reliably_.

And hire great technical writers. Even if the primary language is not English, work on having good translations in the markets where you want to compete. Raspberry Pi's documentation sometimes takes a little time to be fully fleshed out after a new board release—but it is a joy to work with, and extremely thorough, compared to most SBC docs I've read.

Having useful illustrations where needed is also helpful—not just block diagrams and image captures from your SoC vendor's documentation!

## Community

There's no magic here. And the Raspberry Pi community isn't perfect—spend some time on the [official forums](https://forums.raspberrypi.com) and you'll be greeted by snippy responses from time to time.

But at least you _will_ get a response. Many other SBC makers toss up a Discourse instance, and a few pesky users will register and post a question... then crickets.

The few SBC makers who have a decent community tend to focus more on Discord and other real-time resources rather than Forums and thorough Wikis/Docsites.

The trouble is, Discord is ephemeral, and utterly useless for stored knowledge. Discourse forums are actually quite nice (I much prefer them to the ancient phpbb style of the Pi Forums!), but useless without first-party presence.

Having engineers (and ideally a moderator or two who gets community a bit better than the average engineer) browse the forum and respond here and there is a huge shot in the arm, and brings people back to the forum as a first-rate first-party resource.

It is _hard_ to offer that level of support, but it is necessary if you want to target Raspberry Pi. It can turn an interested first-time user into a lifelong devotee, just through assisting them with some small issue they had the courage to post in your official forum!

## Price

But we get to the last thing in this list (I could write more... but I think there's enough already), and I know some people are already yelling "BUT JEFF, a Pi costs like $200!"

Alternatively, someone will mention "You can't get a fully functional Pi with power supply, etc. for less than $100 MSRP!"

But here's the rub: the Raspberry Pi (if you consider the entire lineup, including the Zero 2W, Pi 4, Pi 5, etc.), has a model at almost any sub-$100 price point, and for a huge quantity of use cases and users, you _don't_ need to outfit the Pi with a whole assortment of accessories.

It's not 2021-early 2023 anymore. You can buy a Pi 4 at list MSRP almost anywhere (even in retail stores—my local Micro Center has over 100 boards in stock right now).

Pi 5 stock comes and goes, so check [rpilocator.com](https://rpilocator.com)—and don't ever buy a Pi from an unauthorized reseller.

But in terms of price to performance,—assuming you buy at MSRP—the Pi compares favorably to any of it's competition. Some of the boards that crush it in performance... have truly eye-watering prices, north of $150!

It's not like a Porsche or Lamborghini, where you're paying a bit more for the name. Raspberry Pi hardware is actually a good value (again, assuming MSRP), compared to other SBCs—_if you need an SBC_.

If your needs are better served with a Tiny PC, by all means go that route—I'm just talking SBCs.

If you can undercut the Pi on price, match its software support, and exceed it in performance and features, you can kill the Raspberry Pi.

I still have not seen that happen (outside of particular niche use cases).

Despite the naysayers, I still spend much of my hobby computing time with Raspberry Pis because they work, they're supported, and... well, finally they can be _bought_ again.
