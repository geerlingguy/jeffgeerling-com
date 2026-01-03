---
nid: 3439
title: "Orion O6 ITX Arm V9 board - temper your expectations"
slug: "orion-o6-itx-arm-v9-board-temper-your-expectations"
date: 2025-02-03T18:47:03+00:00
drupal:
  nid: 3439
  path: /blog/2025/orion-o6-itx-arm-v9-board-temper-your-expectations
  body_format: markdown
  redirects:
    - /blog/2025/dont-get-your-hopes-over-oryon-o6-itx-arm-board
    - /blog/2025/oryon-o6-itx-arm-v9-board-temper-your-expectations
aliases:
  - /blog/2025/dont-get-your-hopes-over-oryon-o6-itx-arm-board
  - /blog/2025/oryon-o6-itx-arm-v9-board-temper-your-expectations
tags:
  - apple
  - arm
  - hardware
  - mini itx
  - motherboard
  - radxa
  - silicon
---

{{< figure src="./radxa-oryon-o6.jpg" alt="Radxa Orion O6 Mini ITX Arm V9 Motherboard" width="700" height="394" class="insert-image" >}}

When I first heard about [Radxa's Orion O6](https://radxa.com/products/orion/o6/), it was being compared to Apple's M1 silicon, and the product page has extraordinary claims:

  - World's First **Open Source** Arm V9 Motherboard
  - Higher Performance, **Lower Power Consumption**, Better Security
  - The following performance graph:

{{< figure src="./cix-cd8180-radxa-orion-o6.jpeg" alt="Radxa Orion O6 CIX CD8180 SoC" width="700" height="255" class="insert-image" >}}

As always, when I see a graph like that without any axis labels, alarm bells start going off. It's a marketing tactic used by Apple, Nvidia, and well, most players who want to make hardware seem even more impressive than it is, and generate early buzz.

_Extraordinary claims require extraordinary evidence._

Developers have been receiving sample boards—myself included—and it seems there will be a ways to go before those claims could hold water.

> **IMPORTANT NOTE**: These are my opinions based on a so far [limited testing run](https://github.com/geerlingguy/sbc-reviews/issues/62#issuecomment-2558090456) with a production board running pre-production software. Some of the results in this blog post will likely differ from final production numbers (which is why I will mostly refrain from specific benchmarks in this post). But the points I make will likely still stand, more or less.

**My primary motivation for this post**: early marketing for this board started a hype train that will not deliver the results people expect.

**This board is very cool.** I like seeing a new SoC to compete on low-end-to-midrange Arm PC builds, and I've been asking for something like this for a _long_ time. But if you're interested in this board, you should temper your expectations somewhat, and hold off impulse-buying it until we get further along in its development.

## Open Source Motherboard

The claim of **open source hardware** seems dubious—I have not seen any indication <s>the board or</s> the board or SoC design will be fully released under an OSHW license (update: [board schematics are available at least!](https://docs.radxa.com/en/orion/o6/download)). I'm guessing what Radxa means is "it runs open source software", but that's a lot different than the label that's currently topmost on their product page:

{{< figure src="./radxa-open-source-motherboard.jpg" alt="Radxa Open Source Motherboard Orion O6" width="700" height="414" class="insert-image" >}}

I would be happy to see full schematics and an official stamp of approval from [OSHWA](https://www.oshwa.org), but I don't believe that is coming. I'd love to be proven wrong.

And the board firmware itself (built on EDKII) doesn't seem to be open source... though there are still a few weeks for that to be released. I hope Radxa will release it!

## CIX CD8180: Higher Performance, Lower Power Consumption

After seeing [Apple's extraordinary improvements in efficiency](/blog/2024/m4-mac-minis-efficiency-incredible), anyone who makes claims about efficiency while marketing a new Arm CPU has an uphill battle to fight in proving those claims.

Qualcomm built some pretty good Snapdragon cores in recent generations, but even their cores pale in comparison to Apple's latest, and are only barely surpassing the M1 in performance per watt and idle power draw.

So far, while the CIX CD8180, a 12-core CPU with a big/medium/LITTLE core layout, has performed well, the results from my varied benchmarks are _mixed_.

Here's an early [Geekbench 6 result](https://browser.geekbench.com/v6/cpu/10222859), with single core of 1314, and multi-core of 6273.

That beats the Intel N100/N150, the BCM2712, and the RK3588, popular in tiny PCs and SBCs. But it doesn't beat the two-year-old Microsoft Windows Dev Kit 2023, with a Qualcomm Snapdragon 8cx Gen 3 SoC.

That's just one benchmark, but other benchmarks, from LLMs to HPL, show similarly-mixed results. And using the default OS image Radxa provides—which _currently_ boots with a device tree instead of the more universal ACPI device layout (which would allow booting from any standard arm64 Linux distro)—has very strange default behavior distributing load among all the bit/medium/LITTLE Arm CPU cores.

If you want to get deep into the nitty-gritty, have a look through the [O6 Debug Party thread on Radxa's forum](https://forum.radxa.com/t/orion-o6-debug-party-invitation/25054) (but please don't go into that thread if you're not actively helping with debugging... that's not the proper place for general O6 feedback!).

## Conclusion

All this to say, like many Radxa hardware products, the hardware seems to be in a pretty good place. The _software_? Not so much, less than a month out from the supposed public launch.

I've harped on this numerous times: one reason I prefer Raspberry Pi, despite the lower value hardware per dollar spent, is I can buy the same model at launch, or 10 years later, and expect all the functionality advertised by Raspberry Pi to work. It might require me to adapt a few libraries in my software, but at least it worked day one, and can still be made to work on day 3,650.

I really wish Radxa and CIX would spend the time to refine their bringup process to the point where the first pre-orders will arrive with a fully-supported feature set, and hardware that punches above its price in a good way.

Right now, there are some worrying signs that the efficiency and performance claims are a bit radical, and some important parts of the hardware are still only supported in specific vendor-provided packages, weeks away from the public launch, like hardware acceleration provided by the Immortalis G720 MC10 GPU.

I really want to love this board, because it is almost exactly what I've been asking for since building my first Ampere Altra-based custom PC: something with more grunt and IO than an SBC like a Raspberry Pi, but priced more like low-end PC hardware, which can fit in standard SFF PC enclosures.

**I'm still excited to receive my pre-order**, and I will likely be doing a _lot_ more with this board. And Radxa has a lot of room for improvement in things like the CPU scheduler. But if you saw the initial posts about the O6 and got your hopes up this would be, basically, Apple M1-class performance in an open source motherboard design... you should temper your expectations.
