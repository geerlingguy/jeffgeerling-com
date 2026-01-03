---
nid: 3358
title: "Raspberry Pi 5 *can* overclock to 3.14 GHz"
slug: "raspberry-pi-5-can-overclock-314-ghz"
date: 2024-03-14T22:20:38+00:00
drupal:
  nid: 3358
  path: /blog/2024/raspberry-pi-5-can-overclock-314-ghz
  body_format: markdown
  redirects: []
tags:
  - cooling
  - cpu
  - overclock
  - performance
  - pi 5
  - raspberry pi
  - video
  - youtube
---

...and it's not just for Pi Day.

{{< figure src="./pi-5-with-tower-cooler-thrml.jpg" alt="Raspberry Pi 5 with THRML tower cooler" width="700" height="auto" class="insert-image" >}}

After posting [my deep-dive into the Pi 5's new BCM2712 and RP1 silicon](https://www.youtube.com/watch?v=WKrt1E5fxLg) this morning, someone linked me to this GitHub issue: [Raspberry Pi 5 cannot overclock beyond 3.0GHz due to firmware limit(?)](https://github.com/raspberrypi/firmware/issues/1876).

For the past few weeks, a few blog readers (most notably, tkaiser—thanks!) commented on PLLs, OPP tables, and DVFS and how something seemed a little off with the 3.0 GHz CPU limit—which was apparently recommended by Broadcom, according to that GitHub issue.

But today, [@popcornmix generated a test firmware revision _without_ the 3.0 GHz limit](https://github.com/raspberrypi/firmware/issues/1876#issuecomment-1997785709), and zealous overclockers can get to pushing the clocks higher.

I started things rolling with a stable 3.14 GHz overclock, able to complete a Geekbench 6 test run, and posted a video with my process and results:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/TTIkZBsVJyA" frameborder='0' allowfullscreen></iframe></div>
</div>

I tried 3.2 and 3.3 GHz as well, but 3.2 was unstable during benchmarking, and 3.3 wouldn't boot.

I was using an [Argon THRML 60mm tower cooler](https://amzn.to/3TBCBXI) for my testing (pictured at the top of this post). It is _quite_ overkill (it actually keeps the Pi cooler than the [Pi 5 water cooling setup I tested earlier](/blog/2024/water-cooling-overkill-pi-5)!). But I would rather not have thermals be an issue when pushing the clocks higher.

> Note: I've also been told, at least with the 16nm process node used for the BCM2712, the chip may be more stable at higher temperatures, versus lower (at least in relative terms). I may re-test trying to maintain the chip at 50°C or 70°C and see if it's more stable at another temperature. It seems unintuitive... but I've seen stranger things. I may also try chilling the chip to see how it does at lower-than-ambient temperatures.

My Geekbench 6 result improved a bit (but was still slightly less efficient than the base clock at 2.4 GHz):

| Pi 5 clock | Single Core | Multi Core |
| --- | --- | --- |
| [2.40 GHz](https://browser.geekbench.com/v6/cpu/2808487) | 748 | 1507 |
| [3.00 GHz](https://browser.geekbench.com/v6/cpu/5297916) | 907 | 1662 |
| [3.14 GHz](https://browser.geekbench.com/v6/cpu/5314274) | 967 | 1793 |

In the end, I will remind you that [most Pi 5's won't even reach a 3.0 GHz overclock](/blog/2024/important-consideration-about-pi-5-overclocking) because of the _silicon lottery_, and performing more extreme overclocks (especially involving firmware you download from a GitHub issue) may void your warranty or at minimum cause permanent damage to your Raspberry Pi 5. _You've been warned._

Now, go forth, and please beat my Geekbench scores!
