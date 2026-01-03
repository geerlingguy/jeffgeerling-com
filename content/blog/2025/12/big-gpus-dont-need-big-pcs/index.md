---
nid: 3521
title: "Big GPUs don't need big PCs"
slug: "big-gpus-dont-need-big-pcs"
date: 2025-12-20T15:04:54+00:00
drupal:
  nid: 3521
  path: /blog/2025/big-gpus-dont-need-big-pcs
  body_format: markdown
  redirects:
    - /blog/2025/beefy-gpus-dont-always-need-beefy-pcs
    - /blog/2025/big-gpus-dont-always-need-big-pcs
    - /blog/2025/big-gpus-dont-need-big-pcs-when-pi-will-do
aliases:
  - /blog/2025/beefy-gpus-dont-always-need-beefy-pcs
  - /blog/2025/big-gpus-dont-always-need-big-pcs
  - /blog/2025/big-gpus-dont-need-big-pcs-when-pi-will-do
tags:
  - amd
  - arm
  - gpu
  - intel
  - nvidia
  - pc
  - raspberry pi
  - video
---

{{< figure src="./raspberry-pi-egpu-vs-pc-gpu-setup.jpeg" alt="Raspberry Pi eGPU vs PC GPU" width="700" height="394" class="insert-image" >}}

Ever since I got [AMD](/blog/2025/using-amd-gpus-on-raspberry-pi-without-recompiling-linux), [Intel](/blog/2025/all-intel-gpus-run-on-raspberry-pi-and-risc-v), and [Nvidia](/blog/2025/nvidia-graphics-cards-work-on-pi-5-and-rockchip) graphics cards to run on a Raspberry Pi, I had a nagging question:

_What's the point?_

The Raspberry Pi only has 1 lane of PCIe Gen 3 bandwidth available for a connection to an eGPU. That's not much. Especially considering a modern desktop has at least one slot with 16 lanes of PCIe Gen 5 bandwidth. That's 8 GT/s versus 512 GT/s. Not a fair fight.

But I wondered if bandwidth isn't everything, all the time.

I wanted to put the question of utility to rest, by testing four things on a _variety_ of GPUs, comparing performance on a Raspberry Pi 5 to a modern desktop PC:

  - Jellyfin and media transcoding
  - Graphics performance for purely GPU-bound rendering (via GravityMark)
  - LLM/AI performance (both prefill and inference)
  - Multi-GPU applications (specifically, LLMs, since they're the easiest to run)

Yes, that's right, we're going beyond just _one_ graphics card today. Thanks to [Dolphin ICS](https://dolphinics.com), who I met at Supercomputing 25, I have a PCIe Gen 4 external switch and 3-slot backplane, so I can easily run two cards at the same time:

{{< figure src="./two-gpus-dolphin-pcie-interconnect-board.jpg" alt="Two GPUs in Dolphin PCIe Interconnect board - Nvidia RTX A400 and A4000" width="700" height="394" class="insert-image" >}}

**The tl;dr**: The Pi can hold its own in many cases—it even wins on efficiency (often by a large margin) if you're okay with sacrificing just 2-5% of peak performance!

## Four GPUs, One Pi

The craziest part was, while I was finishing up this testing, GitHub user mpsparrow plugged [_four_ Nvidia RTX A5000 GPUs](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/791) into a single Raspberry Pi. Running Llama 3 70b, the setup generated performance within 2% of his reference Intel server:

{{< figure src="./pi-4x-nvidia-rtx-a5000-gpu-llm-benchmark.png" alt="Raspberry Pi 5 with 4x Nvidia RTX A5000 GPUs - LLM benchmark" width="700" height="394" class="insert-image" >}}

On the Pi, it was generating responses at 11.83 tokens per second. On a modern server, using the exact same GPU setup, he got 12. That's less than a _2 percent difference_.

How is this possible? Because—at least when using multiple Nvidia GPUs that are able to share memory access over the PCIe bus—the Pi doesn't have to be in the way. An external PCIe switch may allow cards to share memory over the bus at Gen 4 or Gen 5 speeds, instead of requiring trips 'north-south' through the Pi's PCIe Gen 3 lane.

But even without multiple GPUs and PCIe tricks, a Pi can still match—and in a few cases, _beat_—the performance of a modern PC.

## Cost and efficiency

Besides efficiency, cost might factor in (both setups not including a graphics card in the price):

| Raspberry Pi eGPU setup | Intel PC |
| --- | --- |
| **TOTAL**: $350-400 | **TOTAL**: $1500-2000 |
| 16GB Pi CM5 + IO Board<br>Minisforum eGPU Dock<br>M.2 to Oculink adapter<br>USB SSD[^usbssd]<br>850W PSU | Intel Core Ultra 265K<br>ASUS ProArt Motherboard<br>Noctua Redux cooler<br>850W PSU<br>Benchtable/case<br>M.2 NVMe SSD<br>64GB of DDR5 RAM[^pcram] |

If peak efficiency and performance aren't your thing, consider that the Pi alone burns 4-5W at idle. The PC? 30W. That's _without_ running a graphics card, and in both cases the only thing plugged in during my measurements was a cheap Raspberry Pi USB keyboard and mouse.

So let's get to the hardware.

## Video

For more background, and to see more details on the actual hardware setups used, check out the video that accompanies this blog post (otherwise, keep on scrolling!):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/8X2Y62JGDCo" frameborder='0' allowfullscreen></iframe></div>
</div>

## Single GPU Comparisons - Pi vs Intel Core Ultra

Before we get to the benchmarks I _did_ run, first I'll mention the ones I _didn't_, namely **gaming**. On previous iterations of my Pi + GPU setups, I was able to get [Steam and Proton running Windows games on Arm through box64](/blog/2024/amd-radeon-pro-w7700-running-on-raspberry-pi).

This time around, with Pi OS 13 (Debian Trixie), I had trouble with both FeX and box64 installing Steam, so I put that on hold for the time being. I'll be testing more gaming on Arm for a video next year surrounding Valve's development of the Steam Frame.

The focus today is raw GPU power.

And I have three tests to stress out each system: Jellyfin, GravityMark, and LLMs.

## Benchmark results - Jellyfin

Let's start with the most practical thing: using a Pi as a media transcoding server.

Since Nvidia's encoder's more polished, I tested it first. Even an older budget card should be adequate for a stream or two, but I had a 4070 Ti available, so I tested it.

Using [encoder-benchmark](https://github.com/Proryanator/encoder-benchmark), [the PC kinda slaughters the Pi](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/792#issuecomment-3643156658):

{{< figure src="./encoder-benchmark-pi-vs-pc-nvidia-rtx-4070-ti.png" alt="Encoder benchmark - Pi vs Intel PC" width="700" height="394" class="insert-image" >}}

Observing `nvtop`, I found the culprit: the Raspberry Pi's anemic IO.

Encoder Benchmark uses raw video streams, which are fairly large (e.g. over 10 GB for a 4K file). This means you have to load all that data in from disk, then copy it over the PCIe bus to the GPU, then the GPU spits back a compressed video stream, which is written back to the disk.

On the Pi, the PCIe bus tops out at 850 MB/sec or so, and because there's only one lane, and I was using a USB 3.0 SSD for my boot disk, it really only got up to 300 MB/sec or so, sustained.

The PC could pump through 2 GB/sec from the PCIe Gen 4 x4 SSD I had installed.

In terms of raw throughput, the PC is hands-down the winner.

But the way Jellyfin works, at least for my own media library, where I store lightly-compressed H.264 and H.265 files, transcoding doesn't need quite that much bandwidth.

I installed Jellyfin and [set it to use NVENC hardware encoding](https://jellyfin.org/docs/general/post-install/transcoding/hardware-acceleration/nvidia/). That worked out of the box.

I could skip around in my 1080p encode of Sneakers without any lag during transcoding. I could switch bitrates to emulate playback through my home VPN playing back Galaxy Quest, and Jellyfin didn't miss a beat. A 4K H.265 file for Apollo 11 was also perfectly smooth at all bitrates on this setup.

{{< figure src="./jellyfin-two-transcodes-nvidia-4070-ti-pi-5.jpg" alt="Jellyfin transcoding two videos on the fly with nvtop showing Pi 5 in foreground" width="700" height="394" class="insert-image" >}}

Even with _two_ transcodes going on at the same time, like here for Dune in 4K and Sneakers in 1080p, it's running just as smooth. It does seem to max out the decode engine, at that point, but it wasn't causing any stuttering.

The Intel PC wins in raw throughput, which is great if you're building a full-blown video transcoding server, but the Pi is fine for most other transcoding use-cases (like OBS, Plex, or Jellyfin).

Historically, AMD isn't quite as good at transcoding, but their cards are adequate. Transcoding _worked_ on the AI Pro I tested, but I had some [stability issues](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/785#issuecomment-3643862116).

## Benchmark results - GravityMark

I wanted to see how raw 3D rendering performed, so I ran the GravityMark benchmark—for now, only on AMD cards, because I haven't gotten a display to run on Nvidia's driver on the Pi yet.

{{< figure src="./benchmarks.001.r9700-gravitymark.jpg" alt="GravityMark Pi vs PC - AMD Ryzen AI Pro R9700" width="700" height="394" class="insert-image" >}}

No surprise, [the Intel PC was faster](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/785#issuecomment-3573234057)... but only by a little.

The rendering is all done on the GPU side, and it doesn't really rely on the Pi's CPU or PCIe lane, so it can go pretty fast.

What _did_ surprise me was what happened when I ran it again on an older AMD card, my [RX _460_](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/564#issuecomment-3590148777).

{{< figure src="./benchmarks.002.rx480-gravitymark.jpg" alt="GravityMark RX460 - Pi vs PC" width="700" height="394" class="insert-image" >}}

This GPU is ancient, in computer years, but I think that gives a leg up for the Pi. The RX 460 runs at PCIe Gen 3, which is exactly as fast as the Pi'll go—and the Pi actually edged out the PC. But the thing that gave me a bigger shock was the score per _watt_.

{{< figure src="./benchmarks.003.rx480-gravitymark-efficiency.jpg" alt="GravityMark performance per watt RX 460 - Pi vs PC" width="700" height="394" class="insert-image" >}}

This is measuring the overall efficiency of the system, and while Intel's not amazing for efficiency right now, it's not like the Pi's the best Arm has to offer.

I got benchmark results for an Nvidia [3060](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/790#issuecomment-3619597869), [3080 Ti](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/549#issuecomment-3590318899), and [A4000](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/692#issuecomment-3589873399), but only on the PC side. I still don't have a desktop environment or display output working on the Pi yet.

## Benchmark results - AI

The AMD Radeon AI Pro R9700 has 32 gigs of VRAM, and should be perfect for a large array of LLMs, up to Qwen3's 30 billion parameter model that takes up 20 GB of VRAM.

And here are the results, Pi versus PC:

{{< figure src="./benchmarks.005.r9700-ai-comparison.jpg" alt="AMD Ryzen AI Pro R9700 Pi vs PC LLMs" width="700" height="394" class="insert-image" >}}

Ouch. This is _not_ what I was expecting to see.

I was a little discouraged, so I went back to my trusty RX 460:

{{< figure src="./benchmarks.007.rx460-ai-comparison.jpg" alt="AMD RX 460 GPU LLM performance" width="700" height="394" class="insert-image" >}}

That's more in line with what I was expecting. Maybe that R9700's lackluster performance is from driver quirks or the lack of a [large BAR](/blog/2025/resizeable-bar-support-on-raspberry-pi)?

I can't blame AMD's engineers for not testing their AI GPUs on Raspberry Pis.

That made me wonder if Nvidia's any better, since they've been [optimizing their Arm drivers](https://www.nvidia.com/en-us/drivers/unix/linux-arm-display-archive/) for _years_.

Here's the [RTX 3060 12 gig](https://github.com/geerlingguy/ai-benchmarks/issues/40), it's a popular card for cheap at-home inference since it has just enough VRAM to be useful:

{{< figure src="./benchmarks.008.rtx3060-ai-performance.jpg" alt="Nvidia RTX 3060 AI LLM Performance Pi vs PC" width="700" height="394" class="insert-image" >}}

The Pi's holding its own. Some models seem to do a little better on the PC like tinyllama and llama 3.2 3B, but for medium-size models, the Pi's within spitting distance. The Pi even _beat the PC_ at Llama 2 13B.

What _really_ surprised me was this next graph:

{{< figure src="./benchmarks.009.rtx3060-ai-efficiency.jpg" alt="Nvidia RTX 3060 AI LLM Efficiency Pi vs PC" width="700" height="394" class="insert-image" >}}

This measures how _efficient_ each system is. Accounting for the power supply, CPU, RAM, GPU, and everything, the Pi is actually pumping through tokens more efficiently than the PC, while nearly matching its performance.

Okay... well, that's just the 3060. That card's also _five_ years old. Maybe bigger and newer cards won't fare so well?

I ran my AI gauntlet against all the Nvidia cards I could get my hands on, including an [RTX 3080 Ti](https://github.com/geerlingguy/ai-benchmarks/issues/39), [RTX 4070 Ti](https://github.com/geerlingguy/ai-benchmarks/issues/45), [RTX A4000](https://github.com/geerlingguy/ai-benchmarks/issues/36), and [RTX 4090](https://github.com/geerlingguy/ai-benchmarks/issues/43). I'll let you watch the video to see _all_ the results, but here I'll skip right to the end, showing the RTX 4090's performance on the Pi (it's the fastest GPU I own currently):

{{< figure src="./nvidia-rtx-4090-on-raspberry-pi-cm5.jpg" alt="Nvidia RTX 4090 on Raspberry Pi CM5" width="700" height="394" class="insert-image" >}}

It's comical how much more volume the graphics card takes up, compared to the Pi—it even dwarfs many of the PC builds into which it may be installed!

{{< figure src="./benchmarks.016.rtx4090-performance.jpg" alt="Nvidia RTX 4090 AI LLM Performance Pi vs PC" width="700" height="394" class="insert-image" >}}

And it looks like tinyllama just completely nukes the Pi from orbit here. But surprisingly, the Pi still holds its own for most of the models—Qwen3 30B is less than 5% slower on the Pi.

With a card that can eat up hundreds of watts of power on its own, how's the efficiency?

{{< figure src="./benchmarks.017.rtx4090-efficiency.jpg" alt="Nvidia RTX 4090 AI LLM Efficiency Pi vs PC" width="700" height="394" class="insert-image" >}}

I thought that since the rest of the system would be a smaller percentage of power draw, the PC would fare better—and it does, actually, for a few models. But the Pi's still edging out the bigger PC in the majority of these tests (the larger models).

Which... is weird.

I honestly didn't expect that. I was expecting the Pi just to get trounced, and maybe pull off one or two little miracle wins.

One caveat: I'm using llama.cpp's Vulkan backend, to keep things consistent across vendors. CUDA could change absolute numbers a little, but _not much_ actually, based on some [CUDA testing with the RTX 2080 Ti](https://github.com/geerlingguy/ai-benchmarks/issues/46#issuecomment-3672239842)—and CUDA works fine on the Pi, surprisingly.

And for the [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) folks reading this post already commenting about prompt processing speeds and context, I linked each result above to a GitHub issue with _all_ the test data, so before you post that comment, please check those issues.

## Dual GPUs

So far we've just been running on _one_ GPU. What if we try _two_?

I used a [Dolphin PCIe interconnect board](https://dolphinics.com/products/IBP-G4X16-3.html), with [Dolphin's MXH932 PCIe HBA](https://dolphinics.com/products/MXH932.html), and connected that to my Pi CM5 using an [M.2 to SFF-8643 adapter](https://amzn.to/4pyqSqt), along with an [SFF-8643 to SFF-8644 cable](https://amzn.to/3MKNbup), which goes from the Pi to the Dolphin card.

Before I ran any LLMs, I wanted to see if I could share memory between the two cards. PCI Express has a feature that lets devices talk straight to each other, instead of having to go 'north-south' through the CPU. That would remove the Pi's Gen 3 x1 bottleneck, and give the cards a full Gen 4 x16 link for tons more bandwidth.

For that to work, you have to disable ACS, or the [Access Control Service](https://www.rambus.com/interface-ip/pci-express-glossary/#acs). And Dolphin apparently set that up for me already, on their switch card.

mpsparrow was running four of the same Nvidia RTX A5000 cards. But I only had different model cards. It looks like the Nvidia driver [doesn't support VRAM pooling](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/791#issuecomment-3638735843) the same way if you have different cards, like my 4070 and A4000, or my A4000 and A400.

But that's okay, there's still things I can do with [llama.cpp and multiple GPUs](https://github.com/geerlingguy/ai-benchmarks/issues/44), going 'north south' through the CPU.

{{< figure src="./benchmarks.018.dual-gpu-nvidia.jpg" alt="Nvidia Dual GPU setup on Pi 5" width="700" height="394" class="insert-image" >}}

This is the performance of the 4070 and A4000, compared to just running the same models on the A4000 directly.

I'm guessing because of that extra traffic between the Pi and the cards, there are tons of little delays while llama.cpp is pushing data through the two GPUs. It's not better for performance, but this setup _does_ let you scale up to larger models that won't fit on one GPU.

Like Qwen 3 30B is around 18 GB, which is too big for either of these two cards alone. It would be faster and more efficient to use a GPU with enough VRAM to fit the entire model. But if you have two graphics cards already, and you want to run them together, at least it's possible.

I also ran the two biggest AMD cards I have, the RX 7900 XT (20 GB) and Radeon AI Pro R9700 (32GB), and that gives me a whopping 52 GB of VRAM. But there, again, maybe due to AMD's drivers, I couldn't get some models to finish a run—and when they did, they were not very fast:

{{< figure src="./benchmarks.019.dual-gpu-amd.jpg" alt="AMD RX 7900 XT and Radeon AI Pro R9700 Dual GPU on Pi 5" width="700" height="394" class="insert-image" >}}

To close out my dual GPU testing, I also ran all the tests on the Intel PC, and it shouldn't be too surprising, it was faster:

{{< figure src="./benchmarks.020.dual-gpu-pi-vs-pc.jpg" alt="Dual GPU setup performance for AI LLMs Pi vs PC" width="700" height="394" class="insert-image" >}}

But at least with Qwen3 30B, the Pi holds its own again.

Takeaway: If you have multiple of the same card, and maybe even try other tools like vLLM—which [I couldn't get to install on Pi](https://github.com/geerlingguy/ai-benchmarks/issues/44#issuecomment-3638978231)—you might get better numbers than I did here.

But the main lesson still applies: more GPUs can give you more capacity, but they'll definitely be slower than one bigger GPU—and less efficient.

## Conclusion

After all that, which one is the winner?

{{< figure src="./pi-vs-pc-ai-llm-power-usage.jpg" alt="Raspberry Pi vs PC power usage measured by Home Assistant ThirdReality Zigbee Smart Outlets" width="700" height="394" class="insert-image" >}}

Well, the PC obviously, if you care about raw performance and easy setup. But for a very specific niche of users, the Pi is better, like if you're not maxed out all the time and have almost entirely GPU-driven workloads. The idle power on the Pi setup was always 20-30W lower. And other Arm SBCs using Rockchip or Qualcomm SoCs are even _more_ efficient, and often have more I/O bandwidth.

Ultimately, I didn't do this because it made sense, I did it because it's fun to learn about the Pi's limitations, GPU computing, and PCI Express. And that goal was achieved.

I'd like to thank [Micro Center](https://www.microcenter.com) for sponsoring the video that led to writing this blog post (they provided the AMD Ryzen AI Pro R9700 for testing, as well as one of the 850W power supplies), and [Dolphin ICS](https://dolphinics.com) for letting me borrow two of their PCI Express boards after I spoke with them at their booth at Supercomputing 25.

[^usbssd]: The price calculation has some flexibility for boot storage. If you are willing to give up half the read/write performance, you could get a fast microSD card to save some money, but I don't recommend it.

[^pcram]: I paid $209 for 64GB of DDR5 memory in April 2025. Lucky for me I purchased that set when I did, because the same set was over $600 in late 2025. The PC setup would be impossible to replicate at the same price currently :(
