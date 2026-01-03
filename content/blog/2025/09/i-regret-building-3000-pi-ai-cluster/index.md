---
nid: 3496
title: "I regret building this $3000 Pi AI cluster"
slug: "i-regret-building-3000-pi-ai-cluster"
date: 2025-09-19T14:12:36+00:00
drupal:
  nid: 3496
  path: /blog/2025/i-regret-building-3000-pi-ai-cluster
  body_format: markdown
  redirects:
    - /blog/2025/compute-blades
aliases:
  - /blog/2025/compute-blades
tags:
  - ai
  - benchmarking
  - blade
  - compute module
  - hpc
  - raspberry pi
  - video
  - youtube
---

{{< figure src="./raspberry-pi-compute-blade-10-node-ai-server.jpeg" alt="Raspberry Pi AI 10 node compute blade server" width="700" height="394" class="insert-image" >}}

I ordered a set of 10 Compute Blades in April 2023 (two years ago), and they just arrived a few weeks ago. In that time Raspberry Pi upgraded the CM4 to a CM5, so I ordered a set of 10 16GB CM5 Lite modules for my blade cluster. That should give me 160 GB of total RAM to play with.

This was the biggest Pi cluster I've built, and it set me back around $3,000, shipping included:

{{< figure src="./framework-vs-pi-cluster-pricing.png" alt="10 Node Pi Cluster Pricing" width="700" height="394" class="insert-image" >}}

There's another Pi-powered blade computer, the [Xerxes Pi](https://www.kickstarter.com/projects/1907647187/small-board-big-possibilities-xerxes-pi). It's smaller and cheaper, but it just wrapped up _its own_ Kickstarter. Will it ship in less than two years? Who knows, but I'm a sucker for crowdfunded blade computers, so of course I backed it!

But my main question, after sinking in a substantial amount of money: are Pi clusters even _worth_ it anymore? I There's no way this cluster could beat the $8,000, 4-node Framework Desktop cluster in performance. But what about in _price per gigaflop_, or in efficiency or compute density?

There's only one way to find out.

## Compute Blade Cluster Build

I made a video going over everything in this blog post—and the entire cluster build (and rebuild, and rebuild again) process. You can watch it here, or on YouTube:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/8SiB-bNyP5E" frameborder='0' allowfullscreen></iframe></div>
</div>

But if you're on the blog, you're probably not the type to sit through a video anyway. So moving on...

## Clustering means doing everything over _n_ times

{{< figure src="./compute-blade-cluster-nvme-install.jpeg" alt="Installing M.2 NVMe SSDs in Compute Blades" width="700" height="394" class="insert-image" >}}

In the course of going from 'everything's in the box' to 'running AI and HPC benchmarks reliably', I rebuilt the cluster basically three times:

  1. First, my hodgepodge of random NVMe SSDs laying around the office was unreliable. Some drives wouldn't work with the Pi 5's PCIe bus, it seems, other ones were a little flaky (there's a reason these were spares sitting around the place, and not in use!)
  2. After replacing all the SSDs with [Patriot P300s](https://amzn.to/4lPJ0JC), they were more reliable, but the CM5s would throttle under load
  3. I put [these CM heatsinks](https://amzn.to/45YACBV) on without screwing them in... then realized they would pop off sometimes, so I took all the blades out _again_ and screwed them into the CM5s/Blades so they were more secure for the long term.

## Compute Blade Cluster HPL Top500 Test

The first benchmark I ran was my [top500 High Performance Linpack cluster benchmark](https://github.com/geerlingguy/top500-benchmark). This is my favorite cluster benchmark, because it's the traditional benchmark they'd run on massive supercomputers to get on the [top500 supercomputer list](https://www.top500.org).

Before I installed heatsinks, the cluster got 275 Gflops, which is an 8.5x speedup over a single 8 GB CM5. Not bad, but I noticed the cluster was only using 105 Watts of power during the run. Definitely more headroom available.

After fixing the thermals, the cluster did not throttle, and used around 130W. At full power, I got 325 Gflops, which is a 10x performance improvement (for 10x 16GB CM5s) over a single 8 GB CM5.

Compared to the $8,000 [Framework Cluster I benchmarked last month](/blog/2025/i-clustered-four-framework-mainboards-test-huge-llms), this cluster is about 4 times slower:

{{< figure src="./framework-vs-pi-cluster-hpl-cluster.png" alt="Pi vs Framework Cluster HPL performance" width="700" height="394" class="insert-image" >}}

But the Pi cluster is _slightly_ more energy efficient, on a Gflops/W basis:

{{< figure src="./framework-vs-pi-cluster-hpl-efficiency.png" alt="Pi vs Framework Cluster HPL Efficiency" width="700" height="394" class="insert-image" >}}

But what about price?

{{< figure src="./framework-vs-pi-cluster-hpl-cost.png" alt="Pi vs Framework Cluster Cost" width="700" height="394" class="insert-image" >}}

The Pi is a little less cost-effective for HPC applications than a Framework Desktop running a AMD's fastest APU. So discounting the fact we're only talking CPUs, I don't think any hyperscalers are looking to swap out a few thousand AMD EPYC systems for 10,000+ Raspberry Pis :)

But what about AI use cases?

## Compute Blade Cluster AI Test

With 160 GB of total RAM, shared by the CPU and iGPU, this could be a small, efficient AI Cluster, right? Well, you'd think.

But no: [currently llama.cpp can't speed up AI using Vulkan on the Pi 5 iGPU](https://github.com/ggml-org/llama.cpp/issues/9801). That means we have 160 GB of RAM, but only CPU-powered inference. On pokey Arm Cortex A76 CPU cores with 10 GB/sec or so of memory bandwidth.

A small model (Llama 3.2:3B), running on a single Pi, isn't horrible; you get about 6 tokens per second. But that is pretty weak compared to even an Intel N100 (much less a single Framework Desktop):

{{< figure src="./framework-vs-pi-cluster-ai-llama-32-3b.png" alt="AI model Llama 3.2 3B on Pi vs Framework vs N150" width="700" height="394" class="insert-image" >}}

You could have 10 nodes running 10 models, and that might be a very niche use case, but the real test would be running a _larger_ AI model across all nodes. So I switched tracks to Llama 3.3:70B, which is a 40 GB model. It _has_ to run across multiple Pis, since no single Pi has more than 16 GB of RAM.

Just as with the Framework cluster, llama.cpp RPC was _very_ slow, since it splits up the model layers on all the cluster members, then goes round-robin style asking each node to perform its prompt processing, then token generation.

The Pi cluster couldn't even make it to token generation (tg) on my default settings, so I had to dial things back and only generate 16 tokens at a time to allow it to complete.

And after all that? Only 0.28 tokens per second, which is _25x slower_ than the Framework Cluster, running the same model (except on AI Max iGPUs with Vulkan).

{{< figure src="./framework-vs-pi-cluster-ai-llama-33-70b-tg.png" alt="Pi vs Framework Cluster AI token generation" width="700" height="394" class="insert-image" >}}

I also tried [Exo](https://github.com/exo-explore/exo) and [distributed-llama](https://github.com/b4rtaz/distributed-llama). Exo was having trouble even running a small 3B model on even a 2 or 3 node Pi cluster configuration, so I stopped trying to get that working.

Distributed llama worked, but only with up to 8 nodes for the 70B model. Doing that, I got a more useful 0.85 tokens/s, but that's still 5x slower than the Framework cluster (and it was a bit more fragile than llama.cpp RPC—the tokens were sometimes gibberish):

{{< figure src="./framework-vs-pi-cluster-ai-llama-33-70b-tg-dllama.png" alt="Pi vs Framework Cluster AI token generation - dllama" width="700" height="394" class="insert-image" >}}

You can find _all_ my AI cluster benchmarking results in the issue [Test various AI clustering setups on 10 node Pi 5 cluster](https://github.com/geerlingguy/beowulf-ai-cluster/issues/6) over on GitHub.

## Gatesworks and Conclusion

Bottom line: this cluster's not a powerhouse. And dollar for dollar, if you're spending over $3k on a compute cluster, it's not the best value.

It _is_ efficient, quiet, and compact. So if _density_ is important, and if you need lots of small, physically separate nodes, this could actually make sense.

Like the only real world use case besides learning is for CI jobs or high security edge deployments, where you're not allowed to run multiple things on one server.

That's what [Unredacted Labs](https://unredacted.org/blog/2025/05/unredacted-labs/) is building Pi clusters for: they're building Tor exit relays on blades, after they found the Pi was the most efficient way to run massive amounts of nodes. If your goal is efficiency and node density, this does win, ever so slightly.

But for 99% of you reading this: this is not the cluster you're looking for.

{{< figure src="./gateworks-gblade-server.jpg" alt="Gateworks Gblade server" width="700" height="394" class="insert-image" >}}

Two years ago, when I originally ordered the Blades, [Gateworks](https://www.gateworks.com) reached out. They were selling a souped up version of the Compute Blade, made to an industrial spec. The [GBlade](https://www.gateworks.com/products/arm-server-blades/gblade-arm-server-blade/) is around Pi 4 levels of performance, but with _10_ gig networking, along with a 1 gig management interface.

But... it's discontinued. It doesn't look like any type of compute blade really lit the world on fire, and like the Blade movie series, the Compute Blade is more of a cult classic than a mainstream hit.

{{< figure src="./compute-blade-cluster-front.jpeg" alt="Compute Blade 10 node Raspberry Pi Cluster mini rack 1" width="700" height="394" class="insert-image" >}}

This is a _bad_ cluster. Except for maybe blade 9, which dies every time I run a benchmark. But I will keep it going, knowing it's _definitely_ easier to maintain than the [1,050 node Pi cluster at UC Santa Barbera](https://www.independent.com/2025/04/29/worlds-biggest-raspberry-pi-cluster-is-now-at-uc-santa-barbara/), which to my knowledge is still the world's largest!

Before I go, I just wanted to give a special thanks to everyone who supports my on [Patreon](https://www.patreon.com/geerlingguy), [GitHub](https://github.com/sponsors/geerlingguy), [YouTube Memberships](https://www.youtube.com/c/JeffGeerling), and [Floatplane](https://www.floatplane.com/channel/JeffGeerling). It really helps when I take on these months- (or years!) long projects.

## Parts Used

You might not want to replicate my cluster setup — but I always get asked what parts I used (especially the slim Ethernet cables... everyone asks about those!), so here's the parts list:

  - [Compute Blade DEV](https://www.pishop.us/product/compute-blade-dev/)
  - [Compute Blade Standard Fan Unit](https://www.pishop.us/product/fansta-1v1-0/)
  - [Compute Blade 10" 3D Print Rackmount](https://github.com/Uptime-Lab/compute-blade/tree/main/models/bladerunner)
  - [Raspberry Pi CM5 16GB (CM5016000)](https://www.pishop.us/product/raspberry-pi-compute-module-5-16gb-ram-lite-cm5016000/)
  - [GLOTRENDS Aluminum CM5 Heatsink](https://amzn.to/45YACBV)
  - [Patriot P300 256GB NVMe SSD 10-pack](https://amzn.to/4lPJ0JC)
  - [GigaPlus 2.5 Gbps 10 port PoE+ switch](https://amzn.to/3UNOwSd)
  - [GigaPlus 10" Rack Mount 3D Print ears](https://www.printables.com/model/1215585-unified-10-rack-gigaplus-switch-mounting-ears)
  - [Monoprice Cat6A SlimRun 6" Cat6 patch cables (10 pack)](https://amzn.to/4fX1gzr)
  - [ioplex SFP+ Twinax DAC patch cable](https://amzn.to/47UlPKX)
  - [DeskPi RackMate TT](https://amzn.to/3UUjCHP)
