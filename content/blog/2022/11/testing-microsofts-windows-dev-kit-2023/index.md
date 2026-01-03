---
nid: 3252
title: "Testing Microsoft's Windows Dev Kit 2023"
slug: "testing-microsofts-windows-dev-kit-2023"
date: 2022-11-03T14:00:11+00:00
drupal:
  nid: 3252
  path: /blog/2022/testing-microsofts-windows-dev-kit-2023
  body_format: markdown
  redirects:
    - /blog/2022/windows-on-arm-dead-microsoft-says-not-so-fast
    - /blog/2022/testing-microsofts-windows-dev-kit-2023-project-volterra
aliases:
  - /blog/2022/windows-on-arm-dead-microsoft-says-not-so-fast
  - /blog/2022/testing-microsofts-windows-dev-kit-2023-project-volterra
tags:
  - arm
  - arm64
  - computer
  - microsoft
  - reviews
  - video
  - windows
  - youtube
---

Last week Microsoft started selling their $599 [Windows Dev Kit 2023](https://www.microsoft.com/en-us/d/windows-dev-kit-2023/94k0p67w7581), formerly known as 'Project Volterra'.

{{< figure src="./microsoft-windows-developer-kit-2023-arm-desktop.jpg" alt="Microsoft Windows Developer Kit 2023 ARM Desktop - Project Volterra" width="700" height="394" class="insert-image" >}}

I got my hands on one after a little bit of a shipping delay, and promptly started tearing it down to see what's inside. You can [click here](https://twitter.com/geerlingguy/status/1587175367306977280) to browse the entire Twitter thread where I posted pictures of the box contents and teardown, or view it below:

<blockquote class="twitter-tweet" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">Windows Dev Kit 2023 (aka "Project Volterra") has arrived. Box is fine, just includes large power adapter and regulatory papers.<br><br>A thread 🧵(1/??) <a href="https://t.co/QTtD6NPC9c">pic.twitter.com/QTtD6NPC9c</a></p>— Jeff Geerling (@geerlingguy) <a href="https://twitter.com/geerlingguy/status/1587175367306977280?ref_src=twsrc%5Etfw">October 31, 2022</a></blockquote> <script async="" src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Eventually I'd like to have this box replace my 10th-gen Intel i3 Windows 10 desktop I use for some light Windows testing, and also perhaps use it as a faster-than-an-SBC Linux ARM workstation.

But for that to happen, it needs to perform. Apple's M1 chips proved ARM can be a serious contender in the desktop space, while also remaining energy efficient. Can Qualcomm's latest stab, the Snapdragon 8cx Gen 3, do the same for Windows on ARM?

Unfortunately, the answer is still no:

{{< figure src="./geekbench-scores-dot-1-dev-kit-m1-mini.jpg" alt="Geekbench scores - Apple M1 Mac mini vs Microsoft Windows Dev Kit 2023 vs Dot 1 Mini PC" width="700" height="394" class="insert-image" >}}

That first entry is the $250 [Dot 1 Mini PC](https://www.apcsilmic.com/products/dot-mini-pc?variant=42469270552825) I reviewed earlier this year. It's a little faster than a Raspberry Pi 4, but the Snapdragon 7c inside is really showing its age.

The second is the Dev Kit, with the 8cx Gen 3 (the same silicon, I believe, used in Microsoft's SQ3 chip). It's noticeably faster—and in many tasks it makes using Windows feel more snappy and x86 applications usable—but it's still not what I'd call 'speedy'.

The M1 blows away the Dev Kit's performance numbers.

And it gets worse—at idle, the mini runs at about 4 watts compared to 5 watts on the Dev Kit. Full blast, the M1 Mac mini is even _more_ efficient, with it's two-year-old Apple Silicon:

{{< figure src="./geekbench-per-watt-power-efficiency.jpg" alt="Geekbench score per watt - M1 Mac mini vs Microsoft Dev Kit 2023" width="700" height="394" class="insert-image" >}}

All is not lost, though. The Dev Kit is $599, a full hundred bucks less than the entry level M1 Mac mini. And for that price, you get 32 GB of RAM (a Mac mini starts at a paltry _8 GB_!), and a 512 GB SSD (Apple tacks on an additional _$200_ for that).

Oh, and the SSD inside the Dev Kit is upgradeable:

{{< figure src="./512gb-ssd-dev-kit-2023-m2-2230.jpg" alt="512 GB SSD inside Microsoft Windows Dev Kit 2023" width="700" height="394" class="insert-image" >}}

Strangely, only a 2230-sized M.2 mounting standoff is included in the case, and there's no built-in 2280-sized standoff or hole to mount one. So if you want to upgrade to a more standard-sized 2280 SSD—like the one that was [shown in the Project Volterra launch video](https://youtu.be/yICVNta8jMU?t=43)—you'll have to improvise.

The rest of the innards are a bit of a mess. It seems obvious the guts were basically a Surface Pro X-style main board rearranged to fit inside a desktop case. And Microsoft missed out on a few golden opportunities, like adding in a 2.5 Gbps network port instead of a stodgy old 1 Gbps port. But the box does have WiFi 6E and _triple_ display support built in (one via mini DisplayPort, two via USB-C).

This box is a solid device for Windows ARM development. But it's not as useful for Linux. You can run ARM Linux inside WSL (Windows Subsystem for Linux), but you can't yet natively boot into a Linux distro—[many have tried and failed already](https://blog.alexellis.io/linux-on-microsoft-dev-kit-2023/).

I made a video about hte Dev Kit 2023 where I dive a bit deeper into a teardown and benchmarking, and I'll embed that video below:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/I3wmp9mstFM" frameborder='0' allowfullscreen></iframe></div>

Overall, it's a decent box. It's quiet, _relatively_ power efficient, and Microsoft's done a great job getting Windows 11 and their own software up and running on ARM. The big question is—will this $599 desktop be enough to push more developers towards cross-compiling for native ARM64 software on Windows?

If not, Windows' own x86 emulation layer still struggles to keep up on ARM. And in an embarrassing turn of events, right now at least, you can [eke out more performance](https://twitter.com/bendycatus/status/1585751395189276673) running x86 code _inside Apple's Rosetta 2 in a Linux VM_ under Windows than you can using Windows' native emulation layer!

I'm hopeful for Microsoft's future on ARM, but either Qualcomm needs to get their act together, or Microsoft needs to pour money into some other chipmaker to optimize for Windows. Otherwise, the vast gulf between ARM SBCs on the low end and Apple's custom Silicon on the high end will persist.

There's plenty of space for a middle ground, especially if it brings features like all-day battery life and snappy performance to cheap and mid-range Windows laptops, like it has for Apple's MacBook lineup.
