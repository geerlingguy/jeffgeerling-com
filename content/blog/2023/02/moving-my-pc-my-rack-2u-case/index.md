---
nid: 3274
title: "Moving my PC into my rack in a 2U case"
slug: "moving-my-pc-my-rack-2u-case"
date: 2023-02-16T17:00:44+00:00
drupal:
  nid: 3274
  path: /blog/2023/moving-my-pc-my-rack-2u-case
  body_format: markdown
  redirects: []
tags:
  - 2u
  - build
  - homelab
  - intel
  - nvidia
  - pc
  - rack
  - sponsored
  - upgrade
  - video
  - youtube
---

This week I finally moved my gaming/Linux PC into my little office rack—it's that 2U box above the UPS at the bottom:

{{< figure src="./2U-gaming-rackmount-server-installed-in-rack.jpeg" alt="2U Gaming and Linux PC in small studio rack" width="700" height="394" class="insert-image" >}}

I remembered seeing [Linus Tech Tips' 4U build](https://youtu.be/TgRXE9mUHJc?t=812) in a video a couple years ago—but he has a full 42U rack in his basement. I don't have that much space—just 2U (technically 3U if I wanted) in my little under-desk studio rack.

So after working with them last year on a similar build (but with a prototype case), I got in touch with [MyElectronics](https://www.myelectronics.nl/us/) and they sent over their new production Mini ITX short-depth 2U PC case.

Moving from a minitower to SFF forced a major downgrade for my graphics card, going from a 3080 Ti to an RTX A2000, but otherwise, I was able to build a system with slightly _faster_ specs than my original PC. Of course, it's one generation newer, so that makes sense... but it also is more energy efficient to boot!

The build used the following parts, courtesy of Micro Center (who sponsored this project for [this YouTube video](https://www.youtube.com/watch?v=lJDmKYEfVek)):

  - [MyElectronics' 2U Mini ITX case](https://www.myelectronics.nl/us/19-inch-2u-mini-itx-case-short-depth.html)
  - [Intel i5-13400 CPU](https://amzn.to/3K5bgJ1)
  - [ASRock Z790M-ITX WiFi Motherboard](https://amzn.to/3YOnLwF)
  - [CORSAIR Vengeance DDR5-5200 RAM with XMP](https://amzn.to/3lDqzi3)
  - [LIAN LI SP 750 SFX PSU](https://amzn.to/3lGtUg4)
  - [PNY Nvidia RTX A2000 12GB graphics card](https://amzn.to/3YobvmV)
  - [be quiet! Pure Wings 80mm BL044 Case fans](https://amzn.to/3S23mCd)
  - [Noctua NH-L9i-17xx Low-Profile CPU cooler](https://amzn.to/3EaWKMi)
  - [3.5mm Keystone Audio Jack](https://amzn.to/3YRPIUA)
  - [Nanxudyj 3.5mm 1ft Audio Cable](https://amzn.to/3Ea26HD)
  - [KIOXIA XG8 NVMe SSD](https://americas.kioxia.com/en-us/business/ssd/client-ssd/xg8.html)

The CPU was the biggest question mark for me on this build. After seeing both [Hardware Unboxed](https://www.youtube.com/watch?v=OsA52DkP8WU) and [Gamers Nexus](https://www.youtube.com/watch?v=AdvWGEzYqg4) give the i5-13400 a solid 'meh', I was nervous it wouldn't keep up with my Linux workloads, like recompiling Linux.

{{< figure src="./geekbench-cinebench-5600x-i5-13400-m1-max-mac.png" alt="Performance comparison of AMD Ryzen 5 5600x Intel i5-13400 and Mac Studio M1 Max" width="700" height="394" class="insert-image" >}}

For most purposes, it is basically a rebadged 12600K, with similar performance, but a reduced TDP (meaning it consumes a little less energy). But I found that to be to my liking.

It's been a few years since I thought to myself "you know, I'd rather burn 50% more energy to get 5% more performance!" To be honest, even my old system's 5600x is still quite adequate for my needs. Plus, I tend to run a lot on my Mac Studio, which is _way_ more power efficient than either system:

{{< figure src="./power-efficiency-2u-intel-i5-13400-m1-max-mac.png" alt="Power efficiency of Intel i5-13400 vs M1 Max Mac Studio" width="700" height="394" class="insert-image" >}}

So while I think this CPU could be a better value under $200, I'm happy with it.

{{< figure src="./Nvidia-RTX-A2000-Quadro-PNY-Graphics-Card-in-2U-rackmount-gaming-PC.jpeg" alt="Nvidia RTX A2000 Quadro PNY Graphics card in 2U rackmount gaming PC" width="700" height="394" class="insert-image" >}}

The A2000 is no slouch, either—at least for my needs. I still run on a boring old 60 Hz 1080p monitor, so the RTX 3080 Ti I was running before was complete overkill for tasks like gaming.

I did have to turn down some settings from 'ultra' to get more than 60 fps in a few modern games (like Red Dead Redemption 2 and Halo Infinite), but they all played well on the new 2U system.

I haven't had as much time to test machine learning tasks on the A2000, but if [my Geekbench 5 compute results](https://browser.geekbench.com/user/446940) are anything to go by, it will be quite a bit slower than the 3080 Ti—though still faster than my M1 Max Mac Studio.

But it also consumes about 1/4 of the power. One other motivation for _downsizing_ was the fact my UPS (a 1000VA unit) would start beeping and showing 'overload' any time I ran things like [Whisper AI](/blog/2023/transcribing-recorded-audio-and-video-text-using-whisper-ai-on-mac) or [Stable Diffusion](/blog/2022/jeff-geerling-stably-diffused) on it.

The MyElectronics case itself is laid out pretty well, though I had a couple gripes with the completed build:

{{< figure src="./2u-rackmount-gaming-PC-build-interior-front.jpeg" alt="2U Rackmount gaming PC build interior in MyElectronics 2U case" width="700" height="394" class="insert-image" >}}

There are two 80mm case fans in the front, but the one on the left blows into a zone that's designed for up to 5 2.5" SSDs or HDDs. And this thermal zone is also where the sole exhaust fan is located. Since the A2000 graphics card basically cuts that section of the case off from the rest, the poor CPU and motherboard are fighting for air on the other side, and there's just an intake blowing into that area—there's not as much pressure pulling the air out the back of the case on that side.

That didn't hurt the performance of _this_ build, but if you wanted to use a CPU with a higher TDP, like 100+ Watts, you might have some throttling issues.

In the end, I'm quite pleased with how this build turned out—though my kids are a little disappointed the rainbow spectrum of RGB is gone. The back of this new case is a bit more humdrum:

{{< figure src="./2u-rackmount-gaming-server-next-to-asus-custom-gaming-pc.jpeg" alt="2U Rackmount gaming PC next to old ASUS Tuf GT501 gaming PC build" width="700" height="394" class="insert-image" >}}

I made a video covering the whole build below, with a bit more detail:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/lJDmKYEfVek" frameborder='0' allowfullscreen></iframe></div>
</div>
