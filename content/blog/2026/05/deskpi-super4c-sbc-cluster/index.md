---
date: '2026-05-01T09:00:00-05:00'
tags: ['deskpi', 'super4c', 'raspberry pi', 'cluster', 'cm5', 'youtube', 'video', 'waveshare', 'mini rack', 'homelab', 'sbc', 'hpc']
title: "SBC Clusters are a terrible value, but they're fun anyway"
slug: 'deskpi-super4c-sbc-cluster'
---
{{< figure
  src="./deskpi-super4c-in-waveshare-homerack-mini-rack.jpg"
  alt="DeskPi Super4C SBC Cluster Board in Waveshare HomeRack Mini Rack"
  width="700"
  height="auto"
  class="insert-image"
>}}

Pictured above is the new [DeskPi Super4C](https://amzn.to/4w4rUOq) installed in an 8U mini rack. The Super4C is a 4-node Raspberry Pi CM5 cluster board that solves two pain points I had with the older [Super6C](https://www.jeffgeerling.com/blog/2022/6-raspberry-pis-6-ssds-on-mini-itx-motherboard/).

I was testing this board around the same time I helped kick off the [SBCC 2026](https://sbcc.sdsc.edu/main-page.html), the Single Board Cluster Competition for students. A dozen or so university teams squared off to run the best mini HPC cluster with a budget of $6,000, and a couple days to benchmark [six HPC workloads](https://single-board-cluster-competition.github.io/sbcc26-competition-site/grading.html).

I decided to populate the Super4C DeskPi sent me to test with four 16GB CM5s I got _last year_, back when they were $125 each. They're about _$300_ today, after the [latest round of price increases](/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/).

I made a video reviewing the Super4C and a new mini rack from Waveshare, the [HomeRack](https://amzn.to/3P9T8CR), and I posted it on YouTube:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/AjmKpDNsTa8' frameborder='0' allowfullscreen></iframe></div>
</div>

In that rack build, I also tested Waveshare's [HomeRack Pi 7" Touch Panel mount](https://amzn.to/4t7nlQU), as well as a [Tripp-Lite mini UPS](https://amzn.to/4n3hfzH) that slots nicely into the bottom. If you're interested in the hardware, go watch the video.

## The Goldilocks Cluster

The main thing I wanted to point out in this blog post are the two annoyances DeskPi fixed in the Super4C—which I think they fixed by reducing the number of Compute Modules from 6 to 4 (thus gaining valuable board space):

  - **Remote Management**: There's now an ESP32 you can access over WiFi (or, soon, Ethernet) for 'lights out' management of the cluster—at least for power control and monitoring[^lightsout].
  - **Redundant Ethernet and Power**: This board has two Ethernet connections to each CM5 slot (one 2.5 Gbps NIC off the USB 3.0 bus, and one 1 Gbps connection through the CM5's own Broadcom NIC). It also has dual 19V DC barrel jack power inputs, and will switch between them to whichever one has the higher voltage.

The video has more detail about other board features, but I mention that it's kind of a 'Goldilocks' board for the SBC Cluster enthusiast; it has just enough features to solve the pain points I had with the Super6C, but not so much complexity the price is pushed beyond a hobbyist's budget.

{{< figure
  src="./deskpi-super4c-esp32.jpeg"
  alt="DeskPi Super4C with ESP32 for remote management"
  width="700"
  height="auto"
  class="insert-image"
>}}

I don't recommend a cluster like this for _value_. The reason you'd buy something like this is for HPC tinkering, on a tiny scale, at your desk, without a bunch of power-hungry used mini PCs or old servers heating up your room.

It could also be useful in some other niche use cases:

  - A multi-camera / multi-node vision processing system, with one or two cameras per CM5 (up to 8 cameras total, with an AI accelerator for each Pi)
  - A tiny 4-computer board that has an HDMI display on each node
  - A small build farm for Arm projects or CI
  - A tiny redundant edge cluster for lightweight applications

If you just want to build a little homelab, though, and you don't care about learning networking or multi-node deployment/coordination: buy a mini PC. You can get a decent one nowadays for $500-600 with 32 GB of RAM, even with inflated memory pricing.

{{< figure
  src="./deskpi-super4c-4x-raspberry-pi-cm5.jpeg"
  alt="DeskPi Super4C with 16GB CM5s"
  width="700"
  height="auto"
  class="insert-image"
>}}

As it is, a minimum cluster build with four Pi CM5s with eMMC and 2 GB of RAM will cost nearly $600. And the cluster as pictured above is closer to $1,400! Like I said, it's not about value, versus a single beefy machine.

## The Competition

It's fun to see how this cluster running on four CM5s with a total of 16 A76 CPU cores and 64 GB of LPDDR5 RAM compares to the SBCC student clusters.

Here's how it stacks up running HPL:

{{< figure
  src="./hpl-graphs.002.performance-with-super4c.jpg"
  alt="DeskPi Super4C compared to SBCC 2026 HPL results"
  width="700"
  height="auto"
  class="insert-image"
>}}

Not a bad showing, overall! In my kickoff speech, I told the students I suspected the team with a cluster of Orange Pi 5 Max boards would have a good shot at the title—and running HPL at least, they were second!

Looking at efficiency, my Super4C cluster was also in the middle of the pack:

{{< figure
  src="./hpl-graphs.003.efficiency.jpg"
  alt="DeskPi Super4C HPL Efficiency compared to SBCC 2026 results"
  width="700"
  height="auto"
  class="insert-image"
>}}

The other cluster (PlumJuice) that's neck-in-neck is also running on Raspberry Pi 5s (9 of them), so it's nice to see that consistency in efficiency from cluster to cluster.

The outlier in _both_ cases was a cluster of four [Minisforum X1 Pro-370](https://store.minisforum.com/products/minisforum-ai-x1-pro-370-mini-pc) mini PCs—with their boards ripped out of them so they were more in the spirit of 'Single Board' computers :)

Here's a look at all the specs for the clusters in the top of the HPL results:

{{< figure
  src="./hpl-graphs.004.nodes.jpg"
  alt="DeskPi Super4C compared to other HPL SBCC result node types"
  width="700"
  height="auto"
  class="insert-image"
>}}

The NTHU team's AMD nodes were underclocked for better efficiency (AMD and Intel seem to push default clocks way beyond what's necessary, I guess to one-up each other), and they also [compiled HPL with ROCm against the iGPU](https://single-board-cluster-competition.github.io/sbcc26-competition-site/teams/nthu.html#benchmarks) for a bit of a speedup, too.

You can call that cheating, since most people don't look at Minisforum PCs and think "SBC", but I call it a creative interpretation of the rules.

Besides, the NTHU team _didn't_ win the overall competition. Team Kent Ridge did, with a cluster of 16 Orange Pi 5 Max's.

I wish the SBCC existed back when I was in college. Since it didn't, I'm glad I can at least [Cosplay as a Sysadmin](https://www.redshirtjeff.com/shop/p/cosplaying-as-a-sysadmin-shirt) and build my own little clusters to compare today.

These cluster projects don't make sense anymore if you just need to run a homelab. But they're quite fun if you want to learn HPC with a cluster that sits on your desk.

[^lightsout]: It doesn't seem to provide a way to mount USB volumes on the Pis, or flash eMMC modules through the network—a headline feature of the Turing Pi 2 for _complete_ lights-out management.
