---
nid: 3524
title: "Dell's version of the DGX Spark fixes pain points"
slug: "dells-version-dgx-spark-fixes-pain-points"
date: 2025-12-26T15:00:41+00:00
drupal:
  nid: 3524
  path: /blog/2025/dells-version-dgx-spark-fixes-pain-points
  body_format: markdown
  redirects:
    - /blog/2025/dells-version-dgx-spark-fixes-few-pain-points
aliases:
  - /blog/2025/dells-version-dgx-spark-fixes-few-pain-points
tags:
  - ai
  - arm
  - dell
  - dgx spark
  - linux
  - llm
  - nvidia
  - reviews
  - video
  - youtube
---

Dell sent me two of their GB10 mini workstations to test:

{{< figure src="./dell-pro-max-gb10-two.jpeg" alt="Dell Pro Max with GB10" width="700" height="394" class="insert-image" >}}

In this blog post, I'll cover the base system, just one of the two nodes. Cluster testing is ongoing, and I'll cover things like AI model training and networking more in depth next year, likely with comparisons to the [Framework Desktop cluster](/blog/2025/i-clustered-four-framework-mainboards-test-huge-llms) and [Mac Studio cluster](/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5) I've also been testing.

But many of the same caveats of the DGX Spark (namely, price to performance is not great if you just want to run LLMs on a small desktop) apply to Dell's GB10 box as well.

It costs a little _more_ than the DGX Spark, but does solve a couple pain points people experienced on the DGX Spark:

  - It has a power LED (seriously, why does the DGX Spark _not_ have one?!)
  - The included power supply is 280W instead of 240W for a little more headroom
  - The thermal design (front-to-back airflow) seems less restricted, so is quieter and capable of keeping the GB10 'AI Superchip' from thermal throttling

But if this isn't a mini PC to compete with a Mac mini, nor a good value for huge LLMs like a Mac Studio, or AMD's Ryzen AI Max+ 395 machines, what is it and who is it for?

Well, it's a $4,000+ box built specifically for developers in Nvidia's ecosystem, deploying code to Nvidia servers that cost [half a million dollars](https://wccftech.com/nvidia-blackwell-dgx-b200-price-half-a-million-dollars-top-of-the-line-ai-hardware/) _each_. A major part of the selling point are these built-in 200 gigabit QSFP ports, which would cost $1,500 or so to add on to another system, assuming you have the available PCIe bandwidth:

{{< figure src="./dell-pro-max-gb10-qsfp-200gbps.jpeg" alt="Dell Pro Max with GB10 Cluster - QSFP cables" width="700" height="394" class="insert-image" >}}

Those ports can't achieve 400 Gbps, but they _do_ hit over 200 Gbps in the right conditions, configured for Infiniband / RDMA. And they hit over 100 Gbps for Ethernet (though only when running multiple TCP streams).

So it may seem a little bit of an odd duck for me, since I'm not an 'Nvidia developer' and I don't deploy code to Nvidia's 'AI factories'.

If I'm being honest, I'm _more_ interested in the 'Grace' part of the GB10 (or 'Grace Blackwell 10') 'AI Superchip. It's a big.LITTLE Arm CPU co-designed by Mediatek, with 10 Cortex-X925 cores and 10 Cortex-A725 cores.

{{< figure src="./grace-blackwell-gb10-ai-superchip-nvidia.jpg" alt="Nvidia GB10 Grace CPU diagram 20 cores" width="700" height="436" class="insert-image" >}}

The chip is united to the Blackwell GPU, and shares the same 128 GB pool of LPDDR5X memory. And it's a pretty snappy Arm CPU—just stuck in a $4,000+ system.

But like I said, Dell sent me these boxes to test. They aren't paying for this blog post and have no control over what I say.

In fact, one of the main things they said was "this is isn't a gaming machine, so don't focus on that."

But that got me thinking. What if... I _did_.

## Gaming on Arm Linux

Valve just announced the Steam Frame, and it [runs on Arm](https://www.windowscentral.com/hardware/virtual-reality/valve-announce-steam-frame-snapdragon-xr-headset-steam-os-arm-support).

Steam Frame will use [FEX](https://fex-emu.com) for its x86-Arm translation layer, and [CodeWeavers' Crossover Preview for Arm64](https://www.codeweavers.com/blog/mjohnson/2025/11/6/twist-our-arm64-heres-the-latest-crossover-preview) was just released, so I thought I'd give that a try on DGX OS (Nvidia's Linux OS, currently based on Ubuntu 24.04).

I was able to quickly install Steam, and through that, games like Cyberpunk 2077, Doom Eternal, and Ultimate Epic Battle Simulator II.

I'll leave the full experience and test results for you to see in this video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/FjRKvKC4ntw" frameborder='0' allowfullscreen></iframe></div>
</div>

But bottom line, the Windows games I typically test on Arm systems through Steam/Proton played very well here, with no stuttering, and decent frame rates (100 fps in Cyberpunk 2077 at 1080p with low settings).

{{< figure src="./dell-pro-max-gb10-gaming-doom-eternal.jpeg" alt="Doom Eternal 200 fps Dell Pro Max GB10" width="700" height="394" class="insert-image" >}}

But no, I agree with Dell, this box should _not_ be evaluated as a gaming machine. While it performs admirably for an Arm linux box, you could do a lot better with half the budget if you just wanted to build a dedicated gaming rig. Even with RAM prices as they are today.

## General Purpose Arm Workstation (with tons of VRAM)

This machine is built for AI development, but it just so happens to have a very good Arm CPU and tons of RAM, so I wanted to test it for both running LLMs, and as a general Arm Linux workstation.

The video above has more depth, and you can find [all my benchmark data here](https://github.com/geerlingguy/sbc-reviews/issues/92), but I wanted to focus on a few things in particular.

## Software

Before we get to benchmarks, I wanted to mention Nvidia's [DGX OS](https://docs.nvidia.com/dgx/dgx-spark/dgx-os.html#release-cadence). Based on Ubuntu Linux, it's the only supported Linux distribution for GB10 systems. Regular Ubuntu LTS versions are supported for 5 years, with optional Pro support extending that out to 10 or even 15 years. But [DGX OS only guarantees updates for two years](https://docs.nvidia.com/dgx/dgx-spark/dgx-os.html#release-cadence), though Nvidia doesn't really offer guarantees for its hardware support.

Their track record for ongoing support for their hardware is [decidedly mixed](https://developer.nvidia.com/embedded/jetson-linux-archive), and in the absence of any guarantees, I wouldn't expect them to continue supporting the Spark or other GB10 systems beyond a few years.

[Some people have had luck getting other distros running](https://forums.developer.nvidia.com/t/has-anyone-tried-an-alternative-linux-distro/349124), but they're still running [Nvidia's kernel](https://github.com/NVIDIA/NV-Kernels). So if you buy one of these, know there's no guarantees for ongoing support.

Running things on DGX OS, I've found most server/headless software runs great, but there are still desktop tools that are more of a hassle. Like Blender doesn't have a stable release that uses GPU acceleration on Arm. But if you [compile it from source](https://github.com/CoconutMacaroon/blender-arm64/)like GitHub user CoconutMacaroon did, you can get full acceleration.

Just using this box as a little workstation, it is plenty fast for all the things I do, from coding, to browsing the web, to media editing. (Though media workflows are still rough on Linux in general, even on x86.)

## CPU benchmarks

The Grace CPU is a 20-core Arm chip [co-designed by Mediatek](https://www.mediatek.com/press-room/newly-launched-nvidia-dgx-spark-features-gb10-superchip-co-designed-by-mediatek), fused together with the Blackwell GPU.

There must be some inefficiency there, though, because the system's idle power draw is a bit higher than I'm used to for Arm, coming in around 30 watts. A lot higher than Apple's M3 Ultra with 512GB of RAM, or even AMD's Ryzen AI Max+ 395 (these names just roll right off the tongue, don't they?).

{{< figure src="./gb10-benchmark-power-idle.jpeg" alt="Dell Pro Max with GB10 - Idle power draw comparison" width="700" height="394" class="insert-image" >}}

In my testing, it seems the CPU itself maxes out around 140 watts, leaving another 140 watts of headroom for the GPU, network, and USB-C ports with PD.

Geekbench 6 was a little unstable, which was weird, but when I did get it to run, it was about on par with the AMD Ryzen AI Max+ 395 system I tested earlier this year, the Framework Desktop.

{{< figure src="./gb10-benchmark-geekbench6.jpeg" alt="Dell Pro Max with GB10 - Geekbench 6 comparison" width="700" height="394" class="insert-image" >}}

Apple's 2-generation-old M3 Ultra Mac studio beats both, but it does cost quite a bit more, so that's to be expected.

And testing with High Performance Linpack, the Dell Pro Max gets about 675 Gflops:

{{< figure src="./gb10-benchmark-hpl.jpeg" alt="Dell Pro Max with GB10 - HPL comparison" width="700" height="394" class="insert-image" >}}

NVIDIA's marketing said the GB10 ["offers a petaflop of AI computing performance"](https://nvidianews.nvidia.com/news/nvidia-puts-grace-blackwell-on-every-desk-and-at-every-ai-developers-fingertips)—a _thousand_ teraflops! This thing can't even hit _one_...

But in the fine print, NVIDIA says it's a petaflop at _FP4 precision_. HPL tests FP64, aka double precision, which is more used in scientific computing. [A FLOP is not always a FLOP](https://bsky.app/profile/fclc.bsky.social/post/3lc4qpte3ys2o), and even the 'petaflop' claim seems disputed, at least if I'm reading [John Carmack's tweets correctly](https://x.com/ID_AA_Carmack/status/1982831774850748825).

But at least for FP64 on the CPU, the GB10 is fairly efficient, at least compared to x86 systems I've tested:

{{< figure src="./gb10-benchmark-hpl-efficiency.jpeg" alt="Dell Pro Max with GB10 - HPL efficiency comparison" width="700" height="394" class="insert-image" >}}

## Networking Performance

A huge part of the value is the built-in ConnectX-7 networking. I tested that, and it's fast. But also a bit odd. Here's the maximum TCP performance I was able to get through the fastest interface on each of the three systems I've been comparing:

{{< figure src="./gb10-benchmark-network.jpeg" alt="Dell Pro Max with GB10 - Ethernet bandwidth" width="700" height="394" class="insert-image" >}}

But 106 Gigabits isn't 200, is NVIDIA lying?

Well, no... it's a little complicated. For full details, I'll refer you to the ServeTheHome article [The NVIDIA GB10 ConnectX-7 200GbE Networking is Really Different](https://www.servethehome.com/the-nvidia-gb10-connectx-7-200gbe-networking-is-really-different/).

Because the ports are each connected to a x4 PCIe Gen 5 link—which isn't enough bandwidth for 200 Gbps per port. To get a full 200 Gbps, you have to use Infiniband/RDMA and carefully configure the network topology. You won't get more than about 206 Gbps, maximum, in real world throughput, no matter how you set it up.

That's still honestly pretty good, but it's not the same as getting 400 Gbps of networking for AI clustering, like I think some of us expected reading the initial press releases in early 2025...

From the perspective of someone replicating NVIDIA's networking stack locally, though, having ConnectX ports built in is a boon. If you want replicate this kind of developer setup on AMD, you'd have to spend around the same amount of money, for the Max+ 395 plus a Connect-X 7 card.

Many people don't care about clustering use cases, or RDMA or Infiniband, but that doesn't mean it's not extremely useful for the people who _do_. This stuff's expensive, but to some people, it's not a bad value.

## AI Performance

For now I'm just running two models, both of them with llama.cpp, optimized for each architecture.

And for a small model that requires a decent amount of CPU to keep up with the GPU, the GB10 does pretty well, almost hitting 100 tokens/s for inference, which is second to the M3 Ultra:

{{< figure src="./gb10-benchmark-ai-llama32-3b.jpeg" alt="Dell Pro Max with GB10 - AI llama small" width="700" height="394" class="insert-image" >}}

But for prompt processing, which is important for how quickly you start seeing a response from AI models, the GB10 chip is the winner, despite costing less than half the M3 Ultra.

And it's a similar story for a huge 'dense' model, Llama 3.1 70B, except here, it gets beat just a little by AMD's Strix Halo in the Framework Desktop:

{{< figure src="./gb10-benchmark-ai-llama31-70b.jpeg" alt="Dell Pro Max with GB10 - AI llama large" width="700" height="394" class="insert-image" >}}

Prompt processing is a strong selling point for these boxes. That's the reason Exo teased [running a DGX Spark as the compute node](https://blog.exolabs.net/nvidia-dgx-spark/) for a Mac Studio cluster.

You can have the Spark, or one of these Dell's, handle the thing _it's_ best at, prompt processing, while the Mac Studios handle the thing _they're_ best at, memory bandwidth for token generation.

Anyway, these are just two quick AI benchmarks, and I have [a lot more in the Dell Pro Max with GB10 issue in my ai-benchmarks repository](https://github.com/geerlingguy/ai-benchmarks/issues/34). I'm doing a lot more testing, including model training and how I clustered two of these things in a tiny mini rack, but you'll have to wait until next year for that.

{{< figure src="./dell-pro-max-gb10-cluster-display.jpeg" alt="Dell Pro Max with GB10 mini cluster" width="700" height="394" class="insert-image" >}}
