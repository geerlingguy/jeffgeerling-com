---
nid: 3226
title: "Microsoft is still far behind: Windows on ARM"
slug: "microsoft-still-far-behind-windows-on-arm"
date: 2022-08-03T14:03:57+00:00
drupal:
  nid: 3226
  path: /blog/2022/microsoft-still-far-behind-windows-on-arm
  body_format: markdown
  redirects: []
tags:
  - apple
  - arm
  - m1
  - m2
  - microsoft
  - qualcomm
  - soc
  - video
  - youtube
---

In spite of Microsoft's cryptic announcement of [Project Volterra](https://www.windowscentral.com/hardware/laptops/surface/project-volterra-everything-you-need-to-know), and Qualcomm's continuous lineup of 'flagship' ARM SoCs for Windows, Microsoft is still behind the 8-ball when it comes to ARM.

Apparently, in 2016, Microsoft [entered into an exclusivity deal with Qualcomm](https://www.xda-developers.com/qualcomm-exclusivity-deal-microsoft-windows-on-arm/). That's why all official 'Windows on ARM' devices use Qualcomm SoCs. At the time, Apple hadn't yet pulled off its [_third_ major architecture shift for macOS](https://appleinsider.com/articles/20/06/12/ten-years-of-apple-technology-shifts-made-the-arm-mac-possible), from Intel X86 to ARM.

Looking back, products like the Surface Pro X and the myriad ARM for Windows laptops, were basically built to a budget and for portability above all else. They were never competitive with Intel/AMD-based computers. Microsoft seemed to think ARM would always remain in a niche, only used for light, mobility-first devices.

## Apcsilmic's Dot 1 Mini PC

The prompt for this blog post was the receipt of the [Dot 1 Mini PC](https://www.apcsilmic.com/products/dot-mini-pc?variant=42469270552825) from Apcsilmic (they sent me the unit for review), which contains a Qualcomm Snapdragon 7c SoC, seen here exposed on Qualcomm's System-on-Module board that has additional pads for an optional 4G modem:

{{< figure src="./qualcomm-soc-snapdragon-7c.jpeg" alt="Qualcomm Snapdragon 7c SoC on SoM board" width="700" height="467" class="insert-image" >}}

This is _not_ a 'flagship' SoC—it's a mobile-oriented chip. But though it benchmarks 2-4x faster than a Raspberry Pi 4 model B, the experience running Windows 11 Pro on it is substantially the same as running it on a Pi 4. And slower than it is _virtualized_ on a base-model Apple M1. Heck, even the SQ2-powered [Surface Pro X gets _trounced_ by the base-model two-year old M1](https://browser.geekbench.com/v5/cpu/compare/16333212?baseline=15737715).

Most things run on the Dot 1—some things passably well—but there's no reason a terminal application like Powershell should take 5-9 seconds to load and get me to the prompt. I expect instantaneous response on my power-hungry AMD 5600x desktop, and I'm willing to forgive a low-power device like the Dot 1 for taking a second or two... but when one of the simpler applications on a system takes as long to launch as Firefox, that's a bit odd.

I'm fairly certain Microsoft execs who put resources towards ARM aren't dogfooding these Qualcomm devices, or if they _are_, they aren't using them for much besides light web browsing and email.

I have a full review of the Dot 1 Mini PC in my video on this topic, embedded below—it includes storage, networking, and CPU benchmarks, which I won't rehash here:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/9WgG2sGEhzo" frameborder='0' allowfullscreen></iframe></div>
</div>

Looking back at Linus Tech Tips' [Surface Pro X vs Apple M1 comparison video](https://www.youtube.com/watch?v=OhESSZIXvCA), I'm surprised that in 1.5 years, little has changed. Apple's proven ARM can run productivity workloads just fine, whereas Microsoft's proven they can make Windows run on ARM—barely.

And I know the Snapdragon 7c isn't a flagship SoC—but it's not like it's a 20 year old chip, either! It just seems like software is not optimized for ARM (even if it's compiled natively), at least not first-party software.

## Future Possibilities

I don't think Microsoft can end their Qualcomm exclusivity deal soon enough—Qualcomm announced [they would have a chip to rival Apple's M1 in 2023](https://www.phonearena.com/news/qualcomm-2023-pc-chip-will-be-apple-m1-competitor_id136499)... except that Apple's already moved on to M2, so Qualcomm's targeting performance metrics already three years out of date!

Competing ARM chips from vendors like MediaTek and Samsung (heck, even Apple Silicon if Microsoft puts in the effort) could offer more competitive performance (or price, or efficiency...), but only after Microsoft gets out of their raw deal.

Developers don't want to develop for ARM on Windows because there are no great Windows machines that run ARM CPUs. And users don't want to use slower ARM-powered Windows devices because they can't run the games and apps they want to.

Right now efficiency and compactness are the two things going for tiny PCs like the Dot 1—but at least outside of Apple's world, everyone seems to still think you can't have your cake and eat it too.
