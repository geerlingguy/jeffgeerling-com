---
nid: 3522
title: "1.5 TB of VRAM on Mac Studio - RDMA over Thunderbolt 5"
slug: "15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5"
date: 2025-12-18T14:00:33+00:00
drupal:
  nid: 3522
  path: /blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5
  body_format: markdown
  redirects:
    - /blog/2025/15-tb-vram-40k-rdma-over-thunderbolt
aliases:
  - /blog/2025/15-tb-vram-40k-rdma-over-thunderbolt
tags:
  - apple
  - arm
  - exo
  - hpc
  - mac
  - mac studio
  - networking
  - rdma
  - thunderbolt
  - video
  - youtube
---

{{< figure src="./mac-studio-cluster-1-hero.jpg" alt="Mac Studio Cluster" width="700" height="394" class="insert-image" >}}

Apple gave me access to this Mac Studio cluster to test RDMA over Thunderbolt, a [new feature in macOS 26.2](https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes#RDMA-over-Thunderbolt). The easiest way to test it is with [Exo 1.0](https://exolabs.net), an open source private AI clustering tool. RDMA lets the Macs all act like they have one giant pool of RAM, which speeds up things like massive AI models.

The stack of Macs I tested, with 1.5 TB of unified memory, costs just shy of $40,000, and if you're wondering, no I cannot justify spending that much money for this. Apple loaned the Mac Studios for testing. I also have to thank DeskPi for sending over the 4-post mini rack containing the cluster.

The last time I remember hearing anything interesting about Apple and HPC (High Performance Computing), was back in the early 2000s, when they still made the [Xserve](https://support.apple.com/en-us/112625).

{{< figure src="./apple-xgrid-icon.png" alt="Apple Xgrid icon" width="128" height="128" class="insert-image" >}}

They had a proprietary clustering solution called Xgrid... that [landed with a thud](https://forums.macrumors.com/threads/xgrid-officially-dead.1412900/). A few universities built some clusters, but it never really caught on, and now Xserve is a distant memory.

I'm not sure if its by accident or Apple's playing the long game, but the M3 Ultra Mac Studio hit a sweet spot for running local AI models. And with RDMA support [lowering memory access latency from 300μs down to < 50μs](https://github.com/ml-explore/mlx/pull/2808), clustering now adds to the performance, especially running huge models.

They also hold their own for creative apps and at least small-scale scientific computing, all while running under 250 watts and almost whisper-quiet.

The two Macs on the bottom have _512 GB_ of unified memory and 32 CPU cores, and cost $11,699 each. The two on top, with half the RAM, are $8,099 each[^pricing].

They're not cheap.

But with Nvidia releasing their [DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) and AMD with their [AI Max+ 395](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html) systems, both of which have a _fourth_ the memory (128 GB maximum), I thought I'd put this cluster through its paces.

## Video

This blog post is the reformatted text version of my latest YouTube video, which you can watch below.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/x4_RsUxRjKU" frameborder='0' allowfullscreen></iframe></div>
</div>

## A Mini Mac Rack

In a stroke of perfect timing, DeskPi sent over a new 4-post mini rack called the [TL1](https://deskpi.com/products/deskpi-rackmate-t1l-rackmount-10u-open-frame-network-rack-for-10-it-network-audio-and-video-device) the day before these Macs showed up.

{{< figure src="./mac-studio-cluster-2-cabling-thunderbolt.jpg" alt="Mac Studio cluster cabling - Thunderbolt 5" width="700" height="394" class="insert-image" >}}

I kicked off [Project MINI RACK](https://mini-rack.jeffgeerling.com) earlier this year, but the idea is you can have the benefits of rackmount gear, but in a form factor that'll fit on your desk, or tucked away in a corner.

Right now, I haven't seen any solutions for mounting Mac Studios in 10" racks besides [this 3D printable enclosure](https://www.printables.com/model/1283153-10-inch-rack-mount-for-mac-studio-m1), so I just put them on some 10" rack shelves.

The most annoying thing about racking _any_ non-Pro Macs is the power button. On a Mac Studio it's located in the back left, on a rounded surface, which means rackmount solutions need to have a way to get to it.

The open sides on the mini rack allow me to reach in and press the power button, but I still have to hold onto the Mac Studio while doing so, to prevent it from sliding out the front!

It _is_ nice to have the front ports on the Studio to plug in a keyboard and monitor:

{{< figure src="./mac-studio-cluster-3-kvm-front.jpg" alt="Mac Studio cluster - KVM keyboard monitor mouse" width="700" height="394" class="insert-image" >}}

For power, I'm glad Apple uses an internal power supply. Too many 'small' PCs are small only because they punt the power supply into a giant brick outside the case. Not so, here, but you _do_ have to deal with Apple's non-C13 power cables (which means it's harder to find cables in the perfect length to reduce cabling to be managed).

{{< figure src="./mac-studio-cluster-4-dgx-spark-qsfp.jpg" alt="DGX Spark mini cluster QSFP ports" width="700" height="394" class="insert-image" >}}

The DGX Spark does better than Apple on networking. They have these big rectangle QSFP ports (pictured above). The plugs hold in better, while still being easy to plug in and pull out.

The Mac Studios have 10 Gbps Ethernet, but the high speed networking (something like 50-60 Gbps real-world throughput) on the Macs comes courtesy of Thunderbolt. Even with [premium Apple cables](https://www.apple.com/us/search/Thunderbolt-5-USB%E2%80%91C-Pro-Cable-1%C2%A0m?tab=accessories) costing $70 each, I don't feel like the mess of plugs would hold up for long in many environments.

There's tech called [ThunderLok-A](https://www.sonnetstore.com/products/thunderlok-a), which adds a little screw to each cable to hold it in, but I wasn't about to drill out and tap the loaner Mac Studios, to see if I could make them work.

Also, AFAICT, Thunderbolt 5 switches don't exist, so you can't plug in multiple Macs to one central switch—you have to plug every Mac into every other Mac, which adds to the cabling mess. Right now, you can only cross-connect up to four Macs, but I think that may not be a hard limit for the current Mac Studio (Apple said all five TB5 ports are RDMA-enabled).

The bigger question is: do you need a full cluster of Mac Studios at all? Because just one is already a beast, matching _four_ maxed-out DGX Sparks or AI Max+ 395 systems. Managing clusters can be painful.

## M3 Ultra Mac Studio - Baseline

To inform that decision, I ran some baseline benchmarks, and posted _all_ my results (much more than I highlight in this blog post) to my [sbc-reviews](https://github.com/geerlingguy/sbc-reviews/issues/95) project.

I'll compare the M3 Ultra Mac Studio to a:

  - Dell Pro Max with GB10 (similar to the Nvidia DGX Spark, but with better thermals)
  - Framework Desktop Mainboard (with AMD's AI Max+ 395 chip)

{{< figure src="./mac-studio-cluster-benchmarks.002.geekbench.jpeg" alt="Mac Studio - M3 Ultra Geekbench 6" width="700" height="394" class="insert-image" >}}

First, Geekbench. The M3 Ultra, running two-generations-old CPU cores, beats the other two in both single and multi-core performance (and even more handily in Geekbench 5, which is more suitable for CPUs with many cores).

{{< figure src="./mac-studio-cluster-benchmarks.003.hpl_.jpeg" alt="Mac Studio - M3 Ultra HPL" width="700" height="394" class="insert-image" >}}

Switching over to a double-precision FP64 test, my classic [top500 HPL benchmark](https://github.com/geerlingguy/top500-benchmark/issues/89), the M3 Ultra is the first small desktop I've tested that breaks 1 Tflop FP64. It's almost double Nvidia's GB10, and the AMD AI Max chip is left in the dust.

{{< figure src="./mac-studio-cluster-benchmarks.004.hpl-efficiency.jpeg" alt="Mac Studio - M3 Ultra HPL Efficiency" width="700" height="394" class="insert-image" >}}

Efficiency on the CPU is also great, though that's been the story with Apple since the A-series, with all their chips. And related to that, idle power draw on here is less than 10 watts:

{{< figure src="./mac-studio-cluster-benchmarks.005.power-draw.jpeg" alt="Mac Studio - M3 Ultra Power Draw at idle" width="700" height="394" class="insert-image" >}}

I mean, I've seen _SBC's_ idle over 10 watts, much less something that could be considered a personal supercomputer.

Regarding AI Inference, the M3 Ultra stands out, both for small and large models:

{{< figure src="./mac-studio-cluster-benchmarks.006.ai-llama-3b.jpeg" alt="Mac Studio - M3 Ultra AI Llama 3B" width="700" height="394" class="insert-image" >}}

{{< figure src="./mac-studio-cluster-benchmarks.007.ai-llama-70b.jpeg" alt="Mac Studio - M3 Ultra AI Llama 70B" width="700" height="394" class="insert-image" >}}

Of course, the _truly_ massive models (like DeepSeek R1 or Kimi K2 Thinking) won't even run on a single node of the other two systems.

{{< figure src="./mac-studio-cluster-benchmarks.009.price_.jpeg" alt="Mac Studio M3 Ultra - Price comparison" width="700" height="394" class="insert-image" >}}

But this _is_ a $10,000 system. You expect more when you pay more.

But consider this: a single M3 Ultra Mac Studio has more horsepower than my _entire_ [Framework Desktop cluster](/blog/2025/i-clustered-four-framework-mainboards-test-huge-llms), using _half_ the power. I also compared it to a tiny 2-node cluster of Dell Pro Max with GB10 systems, and a single M3 Ultra still comes ahead in performance and efficiency, with double the memory.

## Mini Stack, Maxi Mac

But with four Macs, how's clustering and remote management?

The biggest hurdle for _me_ is macOS itself. I automate _everything I can_ on my Macs. I maintain the most popular [Ansible playbook for managing Macs](https://github.com/geerlingguy/mac-dev-playbook), and can say with some authority: managing Linux clusters is easier.

Every cluster has hurdles, but there are a bunch of small struggles when managing a cluster of Macs without additional tooling like MDM. For example: did you know there's no way to run a system upgrade (like to 26.2) via SSH? You _have_ to click buttons in the UI.

Instead of plugging a KVM into each Mac remotely, I used Screen Sharing (built into macOS) to connect to each Mac and complete certain operations via the GUI.

## HPL and Llama.cpp

With everything set up, I tested HPL over 2.5 Gigabit Ethernet, and llama.cpp over that and Thunderbolt 5.

{{< figure src="./mac-studio-cluster-hpl-llama.001.hpl_.jpeg" alt="Mac Studio - Clustered HPL vs HPL on one node" width="700" height="394" class="insert-image" >}}

For HPL, I got 1.3 Teraflops with a single M3 Ultra. With all four put together, I got 3.7, which is less than a 3x speedup. But keep in mind, the top two Studios only have half the RAM of the bottom two, so a 3x speedup is probably around what I'd expect.

I tried running HPL through Thunderbolt (not using RDMA, just TCP), but after a minute or so, both Macs I had configured in a cluster would crash and reboot. I looked into using [Apple's MLX wrapper for `mpirun`](https://ml-explore.github.io/mlx/build/html/usage/distributed.html), but I couldn't get that done in time for this post.

Next I tested llama.cpp running AI models over 2.5 gigabit Ethernet versus Thunderbolt 5:

{{< figure src="./mac-studio-cluster-hpl-llama.002.llama-tb5-eth.jpeg" alt="Mac Studio - llama.cpp TB5 vs Ethernet performance" width="700" height="394" class="insert-image" >}}

Thunderbolt definitely wins for latency, even if you're not using RDMA.

[All my llama.cpp cluster test results are listed here](https://github.com/geerlingguy/beowulf-ai-cluster/issues/17)—I ran many tests that are not included in this blog post, for brevity.

## Enabling RDMA

[Exo 1.0](https://exolabs.net) was launched today (at least, so far as I've been told), and the headline feature is RDMA support for clustering on Macs with Thunderbolt 5.

{{< figure src="./mac-studio-cluster-10-rdma_ctl.jpg" alt="Mac Studio rdma_ctl enable" width="700" height="394" class="insert-image" >}}

To _enable_ RDMA, though, you have to boot into recovery mode and run a command:

  1. Shut down the Mac Studio
  2. Hold down the power button for 10 seconds (you'll see a boot menu appear)
  3. Go into Options, then when the UI appears, open Terminal from the Utilities menu
  4. Type in `rdma_ctl enable`, and press enter
  5. Reboot the Mac Studio

Once that was done, I ran a bunch of HUGE models, including Kimi K2 Thinking, which at 600+ GB, is too big to run on a single Mac.

{{< figure src="./mac-studio-cluster-25-exo-kimi-k2-thinking.jpg" alt="Mac Studio Kimi K2 Thinking on full cluster in Exo" width="700" height="394" class="insert-image" >}}

I can run models like that across multiple Macs using both llama.cpp and Exo, but the latter is so far the only one to support RDMA. Llama.cpp currently uses an [RPC method](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md) that spreads layers of a model across nodes, which scales but is inefficient, causing performance to decrease as you add more nodes.

This benchmark of Qwen3 235B illustrates that well:

{{< figure src="./mac-studio-cluster-ai-full-1-qwen3-235b.jpeg" alt="Mac Studio cluster - Qwen3 235B Result llama.cpp vs Exo" width="700" height="394" class="insert-image" >}}

Exo speeds _up_ as you add more nodes, hitting 32 tokens per second on the full cluster. That's definitely fast enough for vibe coding, if that's your thing, but it's not mine.

So I moved on to testing DeepSeek V3.1, a 671 billion parameter model:

{{< figure src="./mac-studio-cluster-ai-full-2-deepseek-3.1-671b.jpeg" alt="Mac Studio cluster - DeepSeek R1 671B Result llama.cpp vs Exo" width="700" height="394" class="insert-image" >}}

I was a little surprised to see llama.cpp get a little speedup. Maybe the network overhead isn't so bad running on two nodes? I'm not sure.

Let's move to the biggest model I've personally run on anything, Kimi K2 Thinking:

{{< figure src="./mac-studio-cluster-ai-full-3-kimi-k2-thinking.jpeg" alt="Mac Studio cluster - Kimi-K2-Thinking Result llama.cpp vs Exo" width="700" height="394" class="insert-image" >}}

This is a 1 _trillion_ parameter model, though there's only 32 billion 'active' at any given time—that's what the A is for in the A32B there.

But we're still getting around 30 tokens per second.

Working with some of these huge models, I can see how AI has some use, especially if it's under my own local control. But it'll be a long time before I put much trust in what I get out of it—I treat it like I do Wikipedia. Maybe good for a jumping-off point, but don't _ever_ let AI replace your ability to think critically!

But this post isn't about the merits of AI, it's about a Mac Studio Cluster, RDMA, and Exo.

They performed great... _when_ they performed.

## Stability Issues

**First a caveat**: I was working with _prerelease_ software while testing. A lot of bugs were worked out in the course of testing.

But it was obvious RDMA over Thunderbolt is new. When it works, it works great. When it doesn't... well, let's just say I was glad I had Ansible set up so I could shut down and reboot the whole cluster quickly.

{{< figure src="./mac-studio-cluster-15-exo-failed.jpg" alt="Mac Studio Cluster - Exo failed loading model" width="700" height="394" class="insert-image" >}}

I also mentioned HPL crashing when I ran it over Thunderbolt. Even if I do get that working, I've only seen clusters of 4 Macs with RDMA (as of late 2025). Apple says all five Thunderbolt 5 ports are enabled for RDMA, though, so maybe more Macs could be added?

Besides that, I still have some underlying trust issues with Exo, since the developers [went AWOL for a while](https://github.com/exo-explore/exo/issues/819).

They _are_ keeping true to their open source roots, releasing Exo 1.0 under the Apache 2.0 license, but I wish they didn't have to hole up and develop it in secrecy; that's probably a side effect of working so closely with Apple.

I mean, it's their right, but as someone who maybe develops _too_ much in the open, I dislike layers of secrecy around any open source project.

I _am_ excited to see where it goes next. They teased [putting a DGX Spark in front of a Mac Studio cluster](https://blog.exolabs.net/nvidia-dgx-spark/) to speed up prompt processing... maybe they'll get support re-added for Raspberry Pi's, too? Who knows.

## Unanswered Questions / Topics to Explore Further

But I'm left with more questions:

  - Where's the M5 Ultra? If Apple released one, it would be [a lot faster](https://machinelearning.apple.com/research/exploring-llms-mlx-m5) for machine learning.
  - Could Apple revive the Mac Pro to give me all the PCIe bandwidth I desire for faster clustering, without being held back by Thunderbolt?
  - Could Macs get [SMB Direct](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-direct)? Network file shares would behave as if attached directly to the Mac, which'd be amazing for video editing or other latency-sensitive, high-bandwidth applications.

Finally, what about other software? [Llama.cpp](https://github.com/ggml-org/llama.cpp/issues/9493#event-21411249655) and other apps could get a speed boost with RDMA support, too.

## Conclusion

Unlike _most_ AI-related hardware, I'm kinda okay with Apple hyping this up. When the AI bubble goes bust, Mac Studios are still fast, silent, and capable workstations for creative work (I use an M4 Max at my desk!).

But it's not all rainbows and sunshine in Apple-land. Besides being more of a headache to manage Mac clusters, Thunderbolt 5 holds these things back from their true potential. QSFP would be better, but it _would_ make the machine less relevant for people who 'just want a computer'.

Maybe as a consolation prize, they could replace the Ethernet jack and one or two Thunderbolt ports on the back with QSFP? That way we could use network switches, and cluster more than four of these things at a time...

[^pricing]: As configured. Apple put in 8 TB of SSD storage on the 512GB models, and 4TB on the 256GB models.
