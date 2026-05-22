---
date: '2026-05-22T15:15:00-05:00'
tags: ['raspberry pi', 'rp2040', 'rp2350', 'microcontroller', 'sbc']
title: 'News about Raspberry Pi 6 and Microcontroller Development'
slug: 'news-about-raspberry-pi-6-and-microcontroller-development'
---
On Thursday, three of the [lead Raspberry Pi engineers](https://investors.raspberrypi.com/leadership) hosted an [AMA on the r/engineering subreddit](https://www.reddit.com/r/engineering/comments/1tcyfvk/hello_rengineering_were_eben_upton_ceo_james/).

{{< figure
  src="./pi-reddit-ama.jpg"
  alt="Raspberry Pi Reddit AMA with Eben Upton, Gordon Hollingworth, and James Adams"
  width="500"
  height="auto"
  class="insert-image"
>}}

## Raspberry Pi 6

One of the most interesting tidbits was on the Pi 6.

Looking back at previous launches:

  - 2012: Raspberry Pi
  - 2015: Raspberry Pi 2 (+3 years)
  - 2016: Raspberry Pi 3 (+1 year)
  - 2019: Raspberry Pi 4 (+3 years)
  - 2023: Raspberry Pi 5 (+4 years)

Following that cycle, one would expect a Pi 6 3-4 years after the Pi 5, which would put it in 2026 or 2027.

My _guess_ is Pi 6 development is already pretty far along... but there's that pesky global DRAM shortage that makes this a bad time to launch a new computer. There's no sense in releasing an SBC that costs twice as much as the [$50 Pi 5](https://www.adafruit.com/product/6447).

Eben stretched the timeline a bit to 4-4.5 years, and indicated a Pi 6 wouldn't come before early 2028... which means the Pi 5 will remain Pi's flagship for a while.

And if you're expecting a built-in M.2 slot or more ports, I'd temper your expectations: It sounds like the key feature will be 'more': a faster CPU and faster IO, rather than new features.

And instead of wasting precious silicon with an NPU, Eben said they see the "CPU as a venue for AI compute." So I don't expect any specific AI chip on the Pi 6.

## Pi Zero 2W and 3

When asked about the Pi Zero 2W, Eben said the substrate supply is constrained—basically, so many AI chips are being made that even older chips using older process nodes have to fight for the actual silicon wafers to use to _make_ the chips.

They're bringing up a new vendor to help with capacity, so the current Pi Zero 2 W shortage _should_ be temporary.

{{< figure
  src="./pi-zero-zero-2-w.jpg"
  alt="Raspberry Pi Zero and Zero 2 W have flat bottoms"
  width="700"
  height="auto"
  class="insert-image"
>}}

It doesn't sound like a Pi Zero 3 is on the horizon yet, for two reasons:

  1. They need to give up on the single-sided PCB, which adds a little cost, because the chips they have that stack a RAM die on top of the CPU to save board space might not work with faster CPUs.
  2. Newer LPDDR RAM is way too expensive for the $15 Zero price point right now.

The reason the Pi Zero 2 W can still hit its price point—at least when it's in stock—is its use of old LPDDR2 RAM, of which Raspberry Pi apparently has a stockpile.

When someone mentioned the Pi 3B as a lower-cost alternative to the Pi 4 and Pi 5, Eben said it's still a popular model, "selling nearly a million units a year." That, despite being released over a decade ago.

## Microcontrollers (MCUs)

James Adams said power and security were more challenging than expected, developing the RP2350 microcontroller. But their efforts seemed to have paid off, especially after a new 'stepping', or silicon revision, which [fixed a current leakage bug](https://hackaday.com/2025/07/31/raspberry-pi-rp2350-a4-stepping-addresses-e9-current-leakage-bug/).

When asked about why Picos use micro USB and not USB-C, he said it's a cost issue. USB-C connectors are more expensive than micro USB, while also taking a tiny bit more board space. That said, USB-C will probably happen someday.

Eben also mentioned microcontroller shipments finally surpassed Pi SBC sales in 2025. The gap is probably widening this year, as Pi prices continue going up.

## Software and Firmware

A few times in the thread, Pi engineers mentioned the software side being integral to having a good hardware experience, and Gordon Hollingworth—Pi's CTO of Software Engineering—vowed to spend 95% of software engineering time supporting and developing libraries, drivers, kernels, and OSes.

If there's one thing where Raspberry Pi excels versus other embedded companies, it's software support. That's the reason people might still pay more for a Pi product, despite the lack of new hardware.
