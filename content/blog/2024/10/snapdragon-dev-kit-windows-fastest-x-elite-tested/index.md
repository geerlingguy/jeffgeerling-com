---
nid: 3408
title: "Snapdragon Dev Kit for Windows - the fastest X Elite, tested"
slug: "snapdragon-dev-kit-windows-fastest-x-elite-tested"
date: 2024-10-02T14:02:17+00:00
drupal:
  nid: 3408
  path: /blog/2024/snapdragon-dev-kit-windows-fastest-x-elite-tested
  body_format: markdown
  redirects:
    - /blog/2024/snapdragon-x-elite-dev-kit-windows-tested
    - /blog/2024/snapdragon-dev-kit-windows-fastest-x-elite-arm-system-tested
aliases:
  - /blog/2024/snapdragon-x-elite-dev-kit-windows-tested
  - /blog/2024/snapdragon-dev-kit-windows-fastest-x-elite-arm-system-tested
tags:
  - arm
  - qualcomm
  - snapdragon
  - video
  - windows
  - youtube
---

{{< figure src="./snapdragon-x-elite-dev-kit-for-windows-hero.jpeg" alt="Snapdragon Dev Kit for Windows - Snapdragon X Elite" width="700" height="auto" class="insert-image" >}}

> **Update - October 17**: Today [Qualcomm cancelled all remaining orders, and will no longer support the Dev Kit](/blog/2024/qualcomm-cancels-snapdragon-dev-kit-refunds-all-orders).

I have mixed feelings publishing this post: many developers who are _actively trying to port their Windows software to Arm_ are [still awaiting shipment](https://www.reddit.com/r/snapdragon/comments/1ftrsp4/additional_delivery_update_on_snapdragon/) of their own Snapdragon Dev Kits, and I seem to be one of the first few people to receive one.

Everyone I've been in contact with _also_ ordered the Dev Kit on July 16, but [we've all been waiting for it to ship—for months](/blog/2024/where-qualcomms-snapdragon-x-elite-dev-kit).

It's October, and the Snapdragon Dev Kit meant to propel CoPilot+ PCs into a new era of Generative AI computing was expected in June, but finally opened up for orders on July 16. At that time, Arrow's website proclaimed 'ships tomorrow'... [until you paid for it and saw your order status](https://x.com/geerlingguy/status/1813957760155058654). But it's _finally_ trickling out to Windows developers who put down almost $900 (including shipping).

At least _some_ hardware is making it out the door, though—some of us feared after all the delays and the poor communication, there might never _be_ shipping hardware.

## Video

This blog post is loosely tied into the video I published on the Dev Kit today, on my YouTube channel. You can watch that video below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/gpFSCACqDqQ" frameborder='0' allowfullscreen></iframe></div>
</div>

## The Hardware

{{< figure src="./snapdragon-dev-kit-open.jpeg" alt="Snapdragon Dev Kit hardware" width="700" height="auto" class="insert-image" >}}

The Dev Kit shipped in a large box with foam padding, a warranty and welcome postcard, and a separate box containing a 180W power supply and a USB-C to HDMI dongle.

Initially, they advertised the Dev Kit as including an internal HDMI port, but recently pulled that feature, and dropped the dongle in the box. Richard Campbell [speculated on a recent TWiT episode](https://www.youtube.com/watch?v=NlEV38cO8Gs) the HDMI port may have caused the production delays, if it blocked FCC compliance testing.

{{< figure src="./snapdragon-devkit-running-hdmi-board.jpeg" alt="Snapdragon Dev Kit - ghost HDMI port" width="700" height="auto" class="insert-image" >}}

And after [tearing it down](/blog/2024/qualcomm-snapdragon-dev-kit-windows-teardown-2024), I think he's on to something. All the chips are in place for an internal DisplayPort to HDMI conversion, with pads on an HDMI + Ethernet daughtercard for an HDMI port, but it is unpopulated (and there are remnants of flux on a few of the pads on mine... see above photo).

{{< figure src="./snapdragon-dev-kit-copper-heatsink.jpeg" alt="Copper Heatsink" width="700" height="auto" class="insert-image" >}}

One surprise was the _massive_ copper heat sink and heat pipes taking heat off the Snapdragon X Elite SoC, 4x8GB LPDDR5x RAM chips, and a large array of PMICs to deliver power to it all. (There was also a little unpopulated spot for eMMC near the RAM.)

For an overview of the hardware features, Qualcomm has an [updated Snapdragon Dev Kit Product Brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Dev-Kit-for-Windows-Product-Brief.pdf); a few headline features are three full-fledged USB 4 ports (one on front, two on back), two 10 Gbps USB-A ports on the back, 2.5 Gbps Ethernet, and a microSD card slot.

Internally, there's a 2280-size NVMe SSD—with an unconventional 2230 mounting post poking right into the bottom of it. Then there's a WiFi 7 / Bluetooth 5.4 card in another M.2 slot, and the Ethernet goes in a mini PCIe slot.

{{< figure src="./snapdragon-18-mystery-boar.jpeg" alt="Snapdragon Dev Kit - mystery board Running ECB" width="700" height="auto" class="insert-image" >}}

Towards the front of the unit, there's a strange 'Running ECB' board that covers up a hidden (and empty) SIM card slot, and the jury's still out on what that is, exactly (I've asked in the official Qualcomm Developer Discord, but haven't gotten a response).

For a deeper dive into the hardware, check out my [teardown post](/blog/2024/qualcomm-snapdragon-dev-kit-windows-teardown-2024), or the video linked earlier in this post.

## Windows 11 Home

{{< figure src="./snapdragon-dev-kit-windows-11.jpg" alt="Windows 11 Home" width="700" height="auto" class="insert-image" >}}

Easily the most baffling decision is Qualcomm's choice of Windows 11 _Home_ to ship with these units. Microsoft can't be charging OEM's _that_ much more per unit for a device meant to assist developers building their next-gen computing platform, right?

Especially when developer-centric features like Active Directory support and Remote Desktop server are tied to a Pro license?

You _can_ upgrade the included Home installation to a Pro license, but it seems rather silly to have to do it. Even the $599 [Windows Dev Kit 2023](https://learn.microsoft.com/en-us/windows/arm/dev-kit/) shipped with Windows 11 Pro!

And Microsoft _still_ doesn't have any official way of downloading an arm64 version of the Windows 11 installation media ISO... though _that could change, finally_. As [noted by @_sumitdh](https://x.com/_sumitdh/status/1841124915392430098), this line recently appeared on the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11):

> Windows 11 ISOs for Arm64 devices will be made available in the coming weeks.

Even with that, the partition layout for the Snapdragon Dev Kit is a little odd, and takes up more space on the included 512 GB SSD than some developers would prefer.

And since the warranty states "Can not replace components.", it may be risky trying to swap out the NVMe SSD for a larger one (or replacing it if it breaks).

Currently, there's no restore image available from Qualcomm, and multiple developers have been asking about this (myself included). So far the answer continues to be "we are asking internally", but a lot of questions are bounced around like that, and don't get a timely answer.

## Linux on Snapdragon X Elite

And before I get to some preliminary performance testing, I wanted to mention _you should not buy a Dev Kit if you're just interested in running Linux on Snapdragon_. At least not yet.

I am still hopeful Linux support will come. Linaro's been working on Linux on Snapdragon for years, and there's an enthusiastic community of Arm Linux devs who have been slowly enabling various Snapdragon laptops this year.

To assist in that effort, I dumped the ACPI tables on my own unit, and [submitted them to the aarch64-linux/build repo](https://github.com/aarch64-laptops/build/pull/110).

For more on where that leads, and for _all_ my test data and observations, please head over to my [GitHub issue on the Snapdragon Dev Kit](https://github.com/geerlingguy/sbc-reviews/issues/51) in my sbc-reviews repo.

## Performance

{{< figure src="./snapdragon-dev-kit-open-x-elite-soc.jpeg" alt="Snapdragon X Elite SoC with 32 GB of RAM" width="700" height="auto" class="insert-image" >}}

The Dev Kit includes a Snapdragon X Elite SoC with:

  - 12-core Oryon CPU (all-core boost to 3.8 GHz, dual-core boost to 4.3 GHz)
  - Adreno GPU ('up to 4.6 TFLOPS')
  - Hexagon NPU ('Up to 45 TOPS')

I did not perform comprehensive performance testing. I won't do that until I can get a real OS running on the Dev Kit and run my full benchmark suite. I was primarily interested in system stability and running a few tests I can rely on for comparison, especially cross-platform.

To that end, I ran Geekbench 6 and Cinebench 2024, both of which have Arm-native versions for Windows, macOS, and Linux. No, they are not perfect, but they are decent proxies for comparison. Like I said, when I have a more serious OS installed, I'll run my full suite; follow [the GitHub issue](https://github.com/geerlingguy/sbc-reviews/issues/51) if you want to see that when it happens.

| Benchmark | Single core score | Multicore score |
| --- | --- | --- |
| Geekbench 6.3.0 | 3020 (28W) | 15969 (80W) |
| Cinebench 2024 | 131 (28W) | 1227 (99W) |

In the table above, the power draw was the maximum sustained power draw during the test. Geekbench is not wonderful at consistency, so I measure power draw at the outlet, and take a period of stable readings during one of the benchmark tests, and average that value. (Cinebench is thankfully more consistent in how it saturates the CPU.)

Idle power draw was around 8W, and during sleep, the system sipped 4.4W.

One thing that surprised me—mostly because Qualcomm's marketing focused a lot on how much better Snapdragon X would be than Apple's M3-class CPU—was how loud the fan on this unit is.

It's not _horrible_. But it's quite noticeable.

My Mac Studio is barely above a whisper when it's running full tilt transcoding HEVC video content. The Dev Kit's fan ramps up when you do almost anything—even sometimes when you're doing nothing, because Windows likes to do random stuff quite frequently.

| Fan state | dBa measurement at 50 cm |
| --- | --- |
| Idle (20%?) | 32 dBa |
| 50% | 51 dBa |
| 100% | 59 dBa |

These measurements were taken in a room with a 30 dBa noise floor. The fan was at least at 50% speed most of the time I was using windows (e.g. browsing the web, opening apps, watching videos). It was certainly one of the louder mini PC boxes I've had on my desk, and when running Cinebench, I could feel the warm air (all 100W of it) blowing with some force a foot or two away.

Generally, the performance was underwhelming _compared to my expectations_. I know from my work [overclocking Raspberry Pis](https://www.youtube.com/watch?v=OXXKi-J0gs4) there are diminishing returns when you force-feed more power into a chip that's optimized for a certain level of performance.

There's a lot more power, a lot more heat, and only marginal performance gains. It looks like the Snapdragon X Elite on a laptop at 20-30W is [only 15-30% less performant](https://www.tomshardware.com/pc-components/cpus/snapdragon-x-elite-pushed-past-100w-shows-us-what-the-cpu-can-offer-on-the-desktop-almost-4x-more-power-for-10-to-30-more-performance) than the X Elite on the Dev Kit running at 80-100W!

And it's downright embarrassing, efficiency-wise, compared to Apple's M3 and M4 chips (M2 is close to comparable, at least).

## Conclusion

The Snapdragon Dev Kit is a missed opportunity.

For the performance and features you get, it isn't a bad price (a hypothetical M3 Pro Mac mini with similar specs would be in the $1200-1400 range).

It's got similar performance to an M3 Pro—which doesn't exist in any Apple desktop, mind you. It's quite upgradable and repairable (there's even empty pads for a full length PCIe slot inside!). And despite the noise, it's a compact, fast mini PC with three full 40 Gbps USB 4 ports.

But it's not approved for resale, so some of the value proposition (outside of development purposes, for a business that can justify throwing away $900) is lost. And there's little documentation or support (so far, at least), so developers aren't eager to ditch lucrative work on x86 versions of their software for a new architecture that's not getting the full, enthusiastic support of either Microsoft or Qualcomm. And [the consumer launch of the CoPilot+ PC has been underwhelming](https://www.digitimes.com/news/a20240916PD211/qualcomm-market-ai-pc-mediatek-2024.html?mod=3&q=qualcomm%27s+early+struggles), meaning Windows developers are likely to be even _less_ enthusiastic about devoting time to arm64.

My main suggestion to Qualcomm would be: support Linux as a first-class citizen. It'd be nice to get the thing approved for resale too, and maybe even get that HDMI port back. But Linux users in particular are hungry for a decent platform that's faster than SBC-level performance, not as expensive as an Ampere workstation, and... 'not a Mac'.

Otherwise, until Microsoft and Qualcomm really throw their full might into Windows on Arm as a platform, these Dev Kits are going to keep landing with a thud on developer's doorsteps—or not at all.
