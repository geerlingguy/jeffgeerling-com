---
date: '2026-10-09T15:00:00-05:00'
tags: ['radxa', 'q8b', 'raspberry pi', 'pi 5', 'youtube', 'video', 'linux', 'sbc', 'reviews']
title: "Radxa's Q8B has 2x the performance and expansion of the Pi 5"
slug: 'radxa-q8b-double-pi-5'
---
{{< figure
  src="radxa-dragon-q8b-with-raspberry-pi-5.jpg"
  alt="Radxa Dragon Q8B with Raspberry Pi 5"
  width="700"
  height="auto"
  class="insert-image"
>}}

There was a time I'd look at a board like the [Radxa Dragon Q8B](https://radxa.com/products/dragon/q8b/) (at left, above) and be like, "there's no way I'd spend $209 on an SBC with 8 gigs of RAM". But we're in 2026, and seeing the 8 gig Raspberry Pi 5 going for almost the same amount, I figured I'd give it a shot.

On _paper_, the Q8B beats the Pi 5 in pretty much every way. A lot of that is thanks to this Snapdragon 8cx Gen 3 chip, which is the same chip [I tested on Microsoft's Windows Dev Kit 2023](/blog/2022/testing-microsofts-windows-dev-kit-2023/).

{{< figure
  src="radxa-dragon-q8b-top-qualcomm-snapdragon-8cx.jpeg"
  alt="Radxa Dragon Q8B with Qualcomm Snapdragon 8cx Gen 3"
  width="700"
  height="auto"
  class="insert-image"
>}}

It has twice the CPU cores, a way faster GPU, a built in NPU, a newer process node for better efficiency, way more PCI Express lanes to play with, multiple built-in M.2 slots, dual 2.5G networking...

I mean, I could go on, and yes it's a slightly larger board. But once we're in the $200 price range, we're talking the realm of mini PCs. But instead of Intel or AMD, Qualcomm promises better efficiency.

And the Windows Dev Kit only ran Windows officially, but this board _should_ be able to run any arm64 flavor of Linux, too (including Radxa's own OS). This strange love-child between Qualcomm and Radxa might prove to be the start of an interesting new era in SBCs. No longer is it mainly Broadcom, Rockchip, and Allwinner. Qualcomm might be finally breaking into the hobbyist market, though it's not without hiccups.

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/KUUuxkICOLw' frameborder='0' allowfullscreen></iframe></div>
</div>

> This blog post is a condensed version of the information in the video above; I left out some of the experiential aspects of using the Q8B in this blog post, since they're more easily conveyed on YouTube. But please continue reading for more notes on performance and usability, compared to the Raspberry Pi 5.

## Getting Started - Choosing an OS

The first hiccup is selecting an operating system to run. Like other Radxa boards, instead of just pointing you to one download, the [System Installation Guide](https://docs.radxa.com/en/dragon/q8b/getting-started/install-system) is more like a choose-your-own-adventure. And you get to decide what storage medium you'll use (some require different techniques), whether to use the link in the Wiki or one on a GitHub release page, and whether to run Debian or two flavors of official Ubuntu-derived OSes.

And that's before I tried installing a generic arm64 OS via USB. I've detailed that process in my [Dragon Q8B benchmark issue](https://github.com/geerlingguy/sbc-reviews/issues/108), and spoiler: I still haven't been able to boot a generic arm64 ISO to install to NVMe storage. Follow [this thread on the Radxa Community forum](https://forum.radxa.com/t/usb-issues-in-bios-on-q8b/31582) for more.

I'm not saying all this to harp on Radxa. They're certainly a lot better than some _other_ SBC vendors. But I keep saying this, year after year. One reason I stick with Raspberry Pi when I need to get a project done is—despite weaker hardware and fewer options—_it's easy to get started_. And I don't have to spend time in the forums just to figure out the best way to turn it on.

## Usage

Overall, at least running Radxa OS, the board feels like an N150 mini PC, maybe even a bit faster. Firefox is the default browser, and YouTube plays back in 4K just fine, and the UI is snappy (which I can't always say for Pi 5-era SBCs).

There are two 2.5 Gbps Ethernet ports, an M.2 2230 slot on the topside for WiFi, dual M.2 2280 slots on the bottom for NVMe or other expansion, a PCIe FPC like on the Raspberry Pi 5, full GPIO, and even another PCIe flat connector on the bottom that doesn't seem to be documented in the Wiki.

{{< figure
  src="radxa-dragon-q8b-bottom-pcie.jpeg"
  alt="Radxa Dragon Q8B bottom side PCIe and connectors"
  width="700"
  height="auto"
  class="insert-image"
>}}

I haven't gotten in a ton of testing with the I/O on this board, but if Qualcomm doesn't run into the same PCIe compatibility quirks as other arm64 platforms, you could do a _lot_ with this board.

I was about to run `apt upgrade` so I'd be on the latest versions of everything for benchmarks, but I'm glad I kept reading through the [Getting Started Guide](https://docs.radxa.com/en/dragon/q8b/system-config/system-update).

{{< figure
  src="system-update-tooltip-radxa.png"
  alt="Radxa Dragon Q8B Rsetup tool warning for upgrades"
  width="600"
  height="auto"
  class="insert-image"
>}}

_Apparently_ you're not supposed to use apt to upgrade things on here. You're supposed to use Radxa's 'Rsetup' tool. I have to ding Radxa on this: If you're maintaining a custom distro, the least you can do is make sure things like system updates work using the standard tools (in this case `apt upgrade`).

If that doesn't work, and it breaks someone's install... that just shouldn't happen. Rsetup is useful for hardware configuration, but I hate that in 2026 we still have custom tools for standard operations like this—at least using Radxa OS.

## Performance

Besides some odd behavior with network download speeds (and not always, but in some instances like downloading Geekbench or some video files), the performance of this board was excellent, especially compared to SBCs in the same class as the Pi 5.

{{< figure
  src="geekbench-6-single-core.png"
  alt="Radxa Dragon Q8B Geekbench Single Core"
  width="700"
  height="auto"
  class="insert-image"
>}}

Just looking at Geekbench, it's not the best benchmark in the world, but it's good for a relative comparison. The Q8B's not quite double the speed of the Pi 5, but it's a major improvement. Radxa's slightly cheaper Q6A holds up well with _its_ 8 cores, but the Q8B _really_ trounces these two in multicore.

{{< figure
  src="geekbench-6-multi-core.png"
  alt="Radxa Dragon Q8B Geekbench Multi Core"
  width="700"
  height="auto"
  class="insert-image"
>}}

It's more than twice as fast as the Pi. It's not quite like an Apple M1, but to have this type of performance on a tiny SBC is huge.

{{< figure
  src="hpl.png"
  alt="Radxa Dragon Q8B HPL"
  width="700"
  height="auto"
  class="insert-image"
>}}

HPL, which really crushes the CPU and RAM, is also showing a huge jump from Pi 5 performance.

{{< figure
  src="hpl-efficiency.png"
  alt="Radxa Dragon Q8B HPL Efficiency"
  width="700"
  height="auto"
  class="insert-image"
>}}

And even using more power, the overall efficiency is better. It's not quite as good as the more efficiency-focused ARM SoCs, but it's pretty good.

{{< figure
  src="power-idle.png"
  alt="Radxa Dragon Q8B Idle Power Draw"
  width="700"
  height="auto"
  class="insert-image"
>}}

But idle power was interesting. I noticed Radxa has this thing set in performance mode by default, so it'll always be burning a little more power when it's doing nothing.

I don't know if it's for stability, to juice benchmark numbers, or what, but that is something I noticed. The chip also pulls 20+W under full load, so having a 65W power adapter is important, especially if you have NVMe, WiFi cards, that sort of stuff.

{{< figure
  src="network.png"
  alt="Radxa Dragon Q8B Network Performance"
  width="700"
  height="auto"
  class="insert-image"
>}}

And of course this thing's 2.5 gig port blows away the 1 gig network that was standard on most of the previous generation SBCs.

3D performance was also way better, but we _are_ talking about a chip that's built for this stuff. The Pi's SoC just doesn't have the same grunt.

{{< figure
  src="memory-memcpy.png"
  alt="Radxa Dragon Q8B Memcopy performance"
  width="700"
  height="auto"
  class="insert-image"
>}}

Memory speed's also up, which helps a lot if you're doing something like running a local LLM or doing image processing.

But the overall picture is that for around the same price, you're getting a lot more performance. And Qualcomm _seems_ committed to Linux support, in a way that Rockchip never was. They've actually put some resources into it, and it seems like Radxa's taking advantage of that.

For _all_ my benchmark data and more comparisons, visit my [SBC Reviews website](https://sbc-reviews.jeffgeerling.com).

## Conclusion

There's one big problem, though: _getting_ a Q8B. It doesn't matter how good it is if you can't buy one. Here in the US, they're in short supply. I bought mine from ARACE, but I ordered it in June, and it showed up in September.

A three month lead time isn't great if you're building something important with your SBC. With Raspberry Pi, at least, I can drive 10 minutes to Micro Center and pick one up right now. Or I could order one from PiShop and have it here in a week or two. At least... some models.

It seems like SBCs might be nearing shortage-level supplies again, if [this PiShop page](https://www.pishop.us/product-category/raspberry-pi/raspberry-pi-5/raspberry-pi-5-boards/) is any indication.

It's a tough time for the SBC market. I said it before, [the SBC hobby is dying](https://www.youtube.com/watch?v=HeX22LnKdFY). And if it's not prices that'll put you off, it's just... getting them in the first place.

I really hope we can get past this, like we just barely did with the component shortages. But what will things be like on the other side? Your guess is as good as mine.
