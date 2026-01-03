---
nid: 3277
title: "RISC-V Business: Testing StarFive's VisionFive 2 SBC"
slug: "risc-v-business-testing-starfives-visionfive-2-sbc"
date: 2023-03-03T16:00:55+00:00
drupal:
  nid: 3277
  path: /blog/2023/risc-v-business-testing-starfives-visionfive-2-sbc
  body_format: markdown
  redirects: []
tags:
  - amd
  - arm
  - hardware
  - intel
  - isa
  - jh7110
  - linux
  - open source
  - reviews
  - risc-v
  - soc
  - youtube
---

It's risky business fighting Intel, AMD, and Arm, and that's _exactly_ what Star Five is trying to do with this:

{{< figure src="./visionfive-2-black-background.jpeg" alt="StarFive VisionFive 2 Black Background" width="700" height="394" class="insert-image" >}}

The chip on this new single board computer could be the start of a computing _revolution_—at least that's what some people think!

The VisionFive 2 has a JH7110 SoC on it, sporting a new Instruction Set Architecture (ISA) called RISC-V.

{{< figure src="./StarFive-VisionFive-2-Focus-Stacked.jpeg" alt="StarFive VisionFive 2 - Focus Stacked" width="700" height="463" class="insert-image" >}}

On board are four 1.5 GHz CPU cores, so it's no slouch. And the one I'm testing is the high-end configuration, with 8 gigs of RAM, an M.2 slot, USB 3.0, and _two_ Gigabit Ethernet ports.

_On paper_, this board looks like it can compete with something like a Raspberry Pi. Can it?

Yes and no.

RISC-V is the new kid on the block. It's so new software isn't really optimized for it yet. And some software won't run at _all_.

But a lot will. Especially if we're talking about Linux.

## Video

This blog post is a lightly-edited transcript of the following video—feel free to either watch the video or read the rest of the blog post:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/aFze0XVhHZA" frameborder='0' allowfullscreen></iframe></div>
</div>

StarFive sent me the board I tested in this review, but I also have an order in for another one. I welcome another competitor in the chip space, especially when there's a more open community around it.

Intel's X86 architecture and ARM's instruction sets are tightly controlled and licensed. RISC-V has an 'open' architecture—though individual designs (like the cores used in the JH7110) are often proprietary and licensed, since that's how chip manufacturers make money.

{{< figure src="./visionfive-2-jh7110-riscv.jpeg" alt="StarFive JH7110 SoC Closeup" width="700" height="467" class="insert-image" >}}

A few years ago I would've said RISC-V had a huge hurdle for adoption. But now, with a new geopolitical landscape, trade wars, and the [lawsuit between Qualcomm and Arm](https://www.theregister.com/2023/01/04/arm_qualcomm_lawsuit/)... eh... maybe it's not so risky after all!

But back to this board. This is the first mass market RISC-V board with compelling hardware specs. So what should you expect if you pick one up?

Initially, not much.

## Bringup

Like many other boards that I've tested from Chinese manufacturers, the initial experience is a bit jarring, especially if you're new to SBCs.

But considering the entire architecture's new, I'm willing to cut it some slack. It's still better than most of the Pi clones—but that's not saying much.

The board was hard to bring up. I had to dig into some forum threads and eventually [this blog post](https://jamesachambers.com/starfive-visionfive-2-firmware-update-guide/) to figure out how to upgrade the firmware, just so I could install the latest OS.

Upgrading the firmware involved running a special buildroot image and logging in with SSH, so already, just to start using the board, it's not simple.

And then I had trouble with HDMI! The GPU supposedly handles 4K, but I couldn't even get it working with my old HD monitor. I tried debugging it with modesed and tried different cables, but I just couldn't get it working. Eventually I was able to get my Atomos Ninja V working, at least, but it seems like HDMI is a little buggy right now.

To add insult to injury, when I went to log in over SSH I tried following the [getting started guide](https://doc-en.rvspace.org/VisionFive2/PDF/VisionFive2_QSG.pdf). But I [found out](https://github.com/geerlingguy/sbc-reviews/issues/10#issuecomment-1421465432) it had the wrong login user. It should be 'user' but the guide said 'root.' (Note: Default SSH behavior has changed in the most recent image.)

Knowing it's not a true plug-and-play experience, how does this thing _perform_?

Well, right now, not that well.

## Benchmarking

Before I show you any test results, I have to warn to you take them with a grain of salt. My results today might be different than someone re-testing everything in a month, or even a year from now.

And that's because RISC-V and the processor on this board are so new that there are thousands of little optimizations that aren't even made yet. Most developers who could _make_ those optimizations don't even have RISC-V hardware to test 'em.

Especially for things like basic math operations or cryptography, this chip looks glacial. In some ways it isn't, but it's not always clear if that's a _hardware_ issue or _software_.

I want compare the VisionFive 2 to two boards you might be more familiar with: the Raspberry Pi 3 B+, and the Raspberry Pi 4.

{{< figure src="./visionfive-2-raspberry-pis.jpg" alt="VisionFive 2 Raspberry Pi 3 and 4" width="700" height="394" class="insert-image" >}}

Putting aside [availability](https://rpilocator.com), the VisionFive 2 is _marketed_ as something between those two boards, but not quite as good as a Pi 4.

So how is it?

Well, just running a basic benchmark like Geekbench, the VisionFive 2 scored 78 single core and 276 multicore.

{{< figure src="./visionfive-2-geekbench-5-benchmark.png" alt="VisionFive 2 Geekbench benchmarks" width="700" height="394" class="insert-image" >}}

It's a LOT slower than a Pi 4. And it's even [noticeably slower than a Pi 3 B+](https://browser.geekbench.com/v5/cpu/compare/20730472?baseline=20776700).

But looking deeper at the [individual test results](https://browser.geekbench.com/v5/cpu/compare/20730472?baseline=20776700), it seems the VisionFive 2 scores especially bad in image-related tests (like Camera, Gaussian Blur, and Structure from Motion). And for Machine Learning, it's only getting 2-4% of the performance of the Pi. What gives?

Reading Geekbench's [documentation](https://www.geekbench.com/doc/geekbench5-cpu-workloads.pdf), it says the Machine Learning workload "performs an image classification task" with a small image. So, another image-based test.

It uses MobileNet v1, an older machine learning model that's _probably_ not optimized for the chip on this board. But it's not like Geekbench's results are useless—if you buy this board today, then for some things it really is that much slower.

Like when I logged in over SSH, the initial login is noticeably slower than the Pi. And image processing and cryptography will be a lot slower on this board.

The lag is bad enough it feels like I'm working on an original Raspberry Pi sometimes.

I also wanted to run linpack to test floating point performance, but I had trouble compiling the Python cryptography library, so I put that on hold.

Before the RISC-V apologists crucify me, I'll add that the JH7110 isn't the only RISC-V chip on the market. And this year other chips which will do better on image processing, neural nets, and encryption are coming.

This is a review of one particular board that happens to be RISC-V. Not the entire RISC-V ecosystem—keep that in mind.

## IO Performance

Moving on to IO performance, I tested both gigabit Ethernet ports, and they both pumped through a full gigabit on their little Motorcomm NICs, so no complaints there.

But what I really wanted to test is the M.2 slot on the bottom. It's got one lane of PCI express Gen 2, just like the Pi 4. On a Compute Module 4, I can get 350-400 MB/sec with a good NVMe SSD.

{{< figure src="./visionfive-2-bottom-nvme-ssd-kioxia-xg6.jpg" alt="Kioxia XG6 NVMe SSD on bottom of VisionFive 2" width="700" height="394" class="insert-image" >}}

Testing the VisionFive 2 I only get about 250 MB/sec. The drive showed up at the correct speed but the board just couldn't put through as much data.

And the built in microSD card slot isn't that fast, either—I only got about 24 MB/sec. The [Pi 4 gets double that](https://pibenchmarks.com/benchmark/56575/), so again, this board is more in line with a Pi 3. More of my test results can be found [here](https://github.com/geerlingguy/sbc-reviews/issues/10).

## Integrated GPU

Next, what about the GPU? One big marketing point is the VisionFive 2 [is the world's first high-performance RISC-V computer with an integrated GPU](https://www.starfivetech.com/en/site/boards)!

The hardware supports HDMI 2, with H.264 and 265 decoding at 4K courtesy of an Imagination BXE GPU.

But can we even _use_ it? One of the curses of Single Board Computers is how hard it is to get the GPU to do anything in Linux. Watching 1080p video on YouTube is a typical use case, and on this board, it's excruciating.

Just _opening_ YouTube is painful enough—it took 30 seconds just to get to the home page! And once you get a video to load, playback is glacial. At HD resolution, almost all the frames were dropped.

It's early days, so the experience should get better. A lot is being worked on right now, like [this pull request that gets hardware acceleration off the ground](https://github.com/riscv/meta-riscv/pull/382).

But forget all that. This thing has an M.2 slot, which means I can take my [M.2 to PCIe x16 adapter](https://amzn.to/3KTtX2H) and plug in anything I want!

## PCI Express Shenanigans

I found [this forum post](http://forum.rvspace.org/t/how-to-use-external-gpu-on-visionfive-v2/1302/4) about someone else already having some success getting an AMD graphics card working, so I pulled out my old Radeon HD 7470, grabbed a copy of Linux, and compiled my own custom kernel.

Surprisingly, compiling Linux for RISC-V using [StarFive's Linux fork](https://github.com/starfive-tech/linux) was easy. I enabled the `radeon` kernel module, then compiled it on the board. It took about an hour.

Once I copied the new kernel in place and rebooted, the GPU worked!

{{< figure src="./visionfive-2-amd-radeon-hd-7470.jpeg" alt="AMD Radeon HD 7470 on VisionFive 2 SBC" width="700" height="467" class="insert-image" >}}

On the Raspberry Pi, I ran into memory access bugs, and we had to write a bunch of ugly hacky patches. I was expecting it to be even worse on an entirely new architecture, but it wasn't!

{{< figure src="./visionfive-2-amd-radeon-console-output.jpeg" alt="VisionFive 2 Console Output from AMD Radeon HD 7470" width="700" height="467" class="insert-image" >}}

I did run into this weird issue where the screen flashes for a while and all these "PVR_K" errors popped up on the screen. So it's not entirely usable yet, but I think there's definitely more fun to be had here.

Trying an Nvidia GTX 750 Ti, the open source nouveau driver made the system freeze up, so I put that on hold—it's likely I ran into a power issue and I'll have to revisit it later.

René Rebe also [get a newer AMD card working on another RISC-V board](https://riscv.org/news/2021/07/rene-rebe-patches-the-linux-kernel-for-worlds-first-look-at-a-radeon-rx-6700xt-on-a-risc-v-pc-gareth-halfacree-hackster-io/), so maybe RISC-V has a leg up on Arm—at least for these tiny SBCs. Getting graphics cards running on low end Arm is painful.

I also checked into hardware video transcoding, but like I said earlier, that's still being worked on. The VisionFive 2 could be useful for things like Plex or Jellyfin—someday.

## Power Consumption / Efficiency

All that would be for naught, though, if this thing isn't also _efficient_. And it's not gonna take the crown, but it's decent, using 3W at idle, and a little over 5W fully stressed.

{{< figure src="./visionfive-2-power-benchmark.png" alt="Power Consumption VisionFive 2 SBC" width="700" height="394" class="insert-image" >}}

This board could be an efficient homelab companion, as long as the software you need can run on it. I haven't had a chance to test other things like Home Assistant or Docker, but I know for many things, just getting the software running right now can be painful.

## Conclusion

But Arm boards—even the darling child Raspberry Pi—were in a similar state a decade ago. StarFive is coming into an already-crowded market and already creating a lotta buzz.

Right now between the Raspberry Pi shortage and the clone manufacturers dropping the ball on software and support, RISC-V SBCs have a prime opportunity.

My biggest question—and I'm not sure if this is praise of the RISC-V community or condemnation of the Arm status quo—is this: How is it that this fledgling RISC-V board, barely off the ground, _already_ has documentation and support that's miles ahead of most other SBCs?

Besides a few small warts in the getting started guide, the [documentation](https://rvspace.org) is pretty good. The [forums](https://forum.rvspace.org) are active, and I didn't have to lurk on Discord just to get help.

And compared to the Raspberry Pi, well, the Pi isn't unimpeachable, but the VisionFive 2 definitely isn't the board to take away _its_ crown.

What it _is_, is an early warning shot across Arm's bow. If each RISC-V board improves at the pace the Pi has over the years, we could see a more competitive landscape, when it comes to energy efficient Linux SoCs.

The JH7110 isn't amazing. But it's not bad, either.

I still wouldn't recommend most people buy this board, unless you already know a lot about Linux and SBCs in general. That may change a year from now, but right now, this board isn't targeted at the same market as a Raspberry Pi.

At [around $100](https://ameridroid.com/products/visionfive-2?variant=40845950779426), and not being quite production-ready, I'm only recommending this board to people interested in exploring RISC-V for now.

But that's the 'risky' business StarFive finds themselves in today.
