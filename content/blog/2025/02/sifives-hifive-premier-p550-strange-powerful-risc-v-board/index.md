---
nid: 3445
title: "SiFive's HiFive Premier P550 is a strange, powerful RISC-V board"
slug: "sifives-hifive-premier-p550-strange-powerful-risc-v-board"
date: 2025-02-21T15:01:47+00:00
drupal:
  nid: 3445
  path: /blog/2025/sifives-hifive-premier-p550-strange-powerful-risc-v-board
  body_format: markdown
  redirects: []
tags:
  - computer
  - eswin
  - hifive
  - linux
  - p550
  - risc-v
  - sbc
  - sifive
  - video
  - youtube
---

{{< figure src="./sifive-hifive-premier-p550-case.jpg" alt="SiFive HiFive Premier P550 leaning on case" width="700" height="394" class="insert-image" >}}

SiFive's [HiFive Premier P550](https://www.sifive.com/boards/hifive-premier-p550) is a strange board. It's the fastest RISC-V development board I've tested—though I haven't tested a [Milk-V Megrez](https://milkv.io/megrez). It's also [Mini DTX](https://en.wikipedia.org/wiki/DTX_%28form_factor%29), which is an ATX-adjacent standard board size that won't fit in many Mini ITX SFF PC cases, which might be why SiFive and ESWIN are releasing a custom case for it (pictured above, which they sent along with the board for my review).

The board has tons of hardware features, like a 20 TOPS NPU for AI. And an Imagination GPU for video acceleration. _And_ a full 40 pin GPIO header like a Raspberry Pi. Except some of those things aren't supported yet. The hardware's there, but the software, not so much.

Even though it's barely faster than a Pi 3 B+—which I can still buy new for [$35](https://www.pishop.us/product/raspberry-pi-3-model-b-plus/)—the P550 costs [$400](https://www.arrow.com/en/products/hf106/sifive-inc).

This is not a board I think most of you reading this should buy.

But it's _very much_ a board I think you should be interested in.

Why? Because more than twice as fast as the first RISC-V SBC I tested, the [VisionFive 2](/blog/2023/risc-v-business-testing-starfives-visionfive-2-sbc). And the new [Framework RISC-V Mainboard](https://frame.work/blog/risc-v-mainboard-for-framework-laptop-13-is-now-available)? It uses the same JH7110 SoC as the VisionFive 2, so it's also left in the dust. It's even faster than the [Milk-V Jupiter](/blog/2024/milk-v-jupiter-first-itx-risc-v-board-ive-tested) with it's 8-core Spacemit M1 I tested last year, using half the CPU cores at a lower clock speed (1.4 vs 1.8 GHz)!

So even if the P550's not fast in comparison to modern SBCs, it's at least not _painfully slow_ like the older RISC-V boards. It also fits in most standard PC cases, has a full-size PCIe Gen 3 x4 slot (x16 physical), and it has enough bandwidth and IO to do... just about anything a normal computer does!

Just, a lot slower.

{{< figure src="./P550-Benchmarks-llm.png" alt="P550 vs other SBCs LLM performance" width="700" height="394" class="insert-image" >}}

Take AI. I ran Llama on my Raspberry Pi 5, and it's slow but not horrible, giving me answers around 5 tokens per second.

The P550's .24 tokens per second is _glacial_—at least running on the CPU. There's a way you can [get at the on-chip NPU to accelerate it a little more](https://forums.sifive.com/t/eic7700x-memory-bandwidth-ram-timings/7002/2?u=geerlingguy), but right now that's not supported out of the box. See all my test data here: [LLM Benchmarks - HiFive Premier P550](https://github.com/geerlingguy/ollama-benchmark/issues/17).

{{< figure src="./P550-Benchmarks-hpl-efficiency.png" alt="HPL Efficiency benchmarks with RISC-V Arm and X86 boards" width="700" height="394" class="insert-image" >}}

Efficiency's pretty bad too. High Performance Linpack benchmark gives me almost 3 Gflops/W on the Pi 5, but on here, _0.8_. Ouch. It _is_ [the most efficient RISC-V board I've tested](https://github.com/geerlingguy/top500-benchmark?tab=readme-ov-file#results), but that's a bit of a pyrrhic victory.

Despite the speed—or lack thereof—I've had a blast testing this thing.

The main reason is software support for RISC-V is getting better.

Arm had growing pains for _years_, but it seems like RISC-V is riding Arm's coattails and already has native builds for practically all the tools I use day to day. It won't run Zoom or play Netflix yet, but most developer tools just work now.

For the Linux kernel, SiFive maintains [around 100 patches](https://forums.sifive.com/t/how-to-compile-and-install-kernel/6836/8?u=geerlingguy) over mainline. That may sound like a lot, but other RISC-V boards are stuck on older kernels, because they're maintaining _hundreds_. RISC-V might skip the awkward teenage years Arm's going through, where every single SBC requires hacky Linux kernels with minimal vendor support. I'd love to see that!

For a complete overview of the _hardware_, please check out this [Explaining Computers video on the P550](https://youtu.be/9KTbi8dJjzQ?t=327). He does a great job walking through every feature, and I wouldn't want to deprive you of an exciting Explaining Computers unboxing!

## Video

Speaking of video, this blog post based on my script for today's video over on YouTube, which is embedded below (scroll right on past if you'd rather read the information instead!):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/1565YYsFmd4" frameborder='0' allowfullscreen></iframe></div>
</div>

## Bringup Notes and Benchmarks

The default setup with this custom case was _loud_. This Flex ATX power supply isn't quiet, and the main fan was also pretty loud, since it was running at full speed by default.

I was pleasantly surprised, though, once it booted up. I could install Ansible without having to compile any extra Python dependencies. In the past, I had to [compile the Python cryptography library](/2024/installing-ansible-on-risc-v-computer), but it looks like that has a native RISC-V build now.

Ollama didn't install right away, but [I could at least compile it without _too_ much hassle](https://github.com/ollama/ollama/issues/8857).

But while I was doing all this, I was a little puzzled by the power consumption.

At idle the board was pulling like 12-13 Watts, and it only went up to like 14 Watts under load. Now that _was_ using the included ATX power supply, which is probably not ideal for a low-power SBC.

{{< figure src="./p550-power-consumption.jpg" alt="P550 Power Consumption on different supplies" width="700" height="394" class="insert-image" >}}

But even if I switched to a 12 volt power adapter, and skipped the PSU, it was burning 8 watts at idle, which is still pretty high. (In the graph above, the three measurement periods are when I was running it with an RX 480 GPU installed, then without it on the Flex ATX PSU, then without it on a 12V DC adapter, respectively).

It looks like the chip is set to run at 1.4 gigahertz no matter what, and there's no idle power governor that slows down the chip when it doesn't need to go full blast.

The heatsink fan ran at full blast by default, but even after I [turned it down a bit](https://forums.sifive.com/t/pwm-fan-control/7003), the SoC was well under 50°C, so I'm not sure why they don't have any fan control enabled by default (hopefully it's added soon!).

General computing under Ubuntu 24.04's desktop environment wasn't _horrible_, but I had to get YouTube down to 480p for smooth playback, or 720p with a few stutters. Other applications were a little sluggish compared to a modern Arm SBC, but bearable. Certainly faster than other RISC-V boards I've tested.

As [Chips and Cheese pointed out recently](https://chipsandcheese.com/p/a-risc-v-progress-check-benchmarking), most software is optimized for x86 and Arm, but not at all for RISC-V's special extensions.

Even if it _were_ optimized, some of the specs on this board are ambitious.

{{< figure src="./sifive-hifive-premier-p550-board-alone.jpeg" alt="SiFive HiFive Premier P550 board alone" width="700" height="467" class="insert-image" >}}

Like it has LPDDR5 RAM that _could_ get _40+ GB/s_ of memory bandwidth. But in my testing, I only see like... 10. Apparently the P550 cores just [don't have the capacity](https://forums.sifive.com/t/eic7700x-memory-bandwidth-ram-timings/7002/2?u=geerlingguy) to use all the memory bandwidth, and it doesn't help that these early boards are run at 1.4 Gigahertz.

> See [all my P550 benchmark data in my sbc-reviews repository](https://github.com/geerlingguy/sbc-reviews/issues/65).

ESWIN support mentioned their [Debian OS version called 'RockOS'](https://github.com/eswincomputing/eic7x-images/releases/tag/Debian-v1.0.0-p550-20241230) (see [rockos-riscv](https://github.com/rockos-riscv)) runs at 1.8 GHz, and it also has extensions for the NPU. But I haven't been able to test that yet. My tests were running their latest Ubuntu image.

To be complete, Fedora also offers a testing [Fedora 41 image](https://fedoraproject.org/wiki/Architectures/RISC-V/SiFive/HiFivePremierP550) for the P550.

## Hardware and PCIe

The main thing I wanted to test was the P550's PCI Express bus. There are 4 PCIe Gen 3 lanes exposed in a x16 slot. There's also an M.2 E-key slot on the other side of the board, but it's actually exposing SDIO for a custom WiFi module, which [ESWIN says is under development](https://forums.sifive.com/t/sdio-wifi-for-the-p550/6964/4).

For the x16 slot, the maximum throughput is 32 GT/s (Gigatransfers per second), or about 8 GB/sec. But the ESWIN EIC7700X just can't handle that much throughput, it seems.

I tested a Kioxia XG8 SSD, which I would expect to get around 2 GB/sec of throughput at PCIe Gen 3x4 (or at least well over 1 GB/sec). It only got about 800 MB/sec—only a slight improvement over x1 speeds:

| Benchmark                  | Result (x1) | Result (x4) |
| -------------------------- | ------ | --------- |
| iozone 4K random read      | 45.00 MB/s | 47.50 MB/s |
| iozone 4K random write     | 82.66 MB/s | 87.84 MB/s |
| iozone 1M random read      | 585.13 MB/s | 703.95 MB/s |
| iozone 1M random write     | 614.41 MB/s | 796.03 MB/s |
| iozone 1M sequential read  | 591.46 MB/s | 712.22 MB/s |
| iozone 1M sequential write | 616.79 MB/s | 798.01 MB/s |

Switching gears to something a little less bandwidth-constrained, I tested a number of AMD GPUs:

  - R5 230 (old, but half-height single slot, meaning it fit inside ESWIN's custom case
  - RX 460 (cheap but limited to 4 GB of VRAM)
  - RX 580 (cheap still, but with 8 GB of VRAM, so it can be useful in some contexts)
  - RX 6700 XT (more expensive, and maybe a little too beefy for the CPU)

All but the RX 6700 XT worked out of the box, but there were some quirks:

  1. I had to fiddle with a file to switch between the iGPU's HDMI output and the dGPU's outputs (with a reboot between each switch).
  2. OpenGL support required an environment variable to be set to use [Zink](https://www.collabora.com/news-and-blog/blog/2018/10/31/introducing-zink-opengl-implementation-vulkan/).
  3. Some monitoring software like `nvtop` resulted in a segmentation fault, while others (e.g. `radeontop` worked, but with some data missing.
  4. Like on Arm, early boot screens are only rendered through the iGPU—so you can't observe u-boot screens or change BIOS-related settings while you're plugged into the dGPU's display outputs.

As a quick test of 3D rendering performance in native Linux, I ran SuperTuxKart:

{{< figure src="./sifive-hifive-premier-p550-supertuxkart-dgpu.jpeg" alt="SuperTuxKart on RX 460 on SiFive HiFive Premier P550" width="700" height="394" class="insert-image" >}}

At 1080p maximum graphics settings, I got around 10-15 fps on the internal Imagination AXM-8-256 GPU, and 50+ fps on an AMD RX 460.

What about triple-A _Windows_ games, though? Or, at least, triple-A Windows games from _a decade ago_?

## The State of (10 year old) Triple-A gaming on RISC-V

I heard [ptitSeb and ksco had gotten The Witcher 3 running on RISC-V](https://box86.org/2024/08/box64-and-risc-v-in-2024/), though they tested on a Milk-V Pioneer board, with _64_ CPU cores (16x more than I had available). How will the P550 handle it?

Well, to install it, I ran through the process of compiling Box64 with Box32 and RISC-V extensions. Then I compiled Wine, then DXVK, to translate Windows to RISC-V, and DirectX to Vulkan. I documented everything in this blog post: [Build Box64 with Box32 for X86 emulation on RISC-V Linux](/blog/2025/build-box64-box32-x86-emulation-on-risc-v-linux).

Then I installed The Witcher 3, downloaded from Gog.com. That process took _over 7 hours_, but eventually after working through a few quirks, I got it running... slowly. _Very_ slowly:

{{< figure src="./p550-witcher-3-fps-low.jpeg" alt="P550 playing The Witcher 3 on an AMD RX 460 GPU" width="700" height="394" class="insert-image" >}}

> [Watch the video](https://www.youtube.com/watch?v=1565YYsFmd4) to see examples of gameplay.

This isn't quite seconds-per-frame, but it is more like experiencing an interactive PowerPoint slideshow than playing a game. After an hour, I was able to make it out of the first room to a cutscene.

It wasn't playable, but it _worked_, which is huge: this processor is able to coordinate everything to render pixels on the screen. That can be the most challenging part sometimes. And that means as RISC-V gets faster, the experience will only get better—at least with older games!

The game was heavily CPU-bound, as all four cores were going 100%, and the GPU was almost idling between 8-12%.

## A more reasonable option - World of Goo

I also tried out a simpler game that still used 3D rendering: World of Goo.

It only took an hour to install, and I was able to get right into the menu and start playing—a welcome improvement over The Witcher 3.

The game was still CPU-bound and couldn't hit a smooth 60 fps, but it was quite playable, with brief stutters now and then. There's a native Linux version available too, though I haven't tested it.

## GPU-Accelerated LLMs

Since the [Linux drivers for the ESWIN's NPU](https://github.com/eswincomputing/linux-stable/commit/3297212953ffa6d2306823710cd8ce47059e1c5f) are pretty bleeding edge, I haven't gotten any LLMs to run on it yet.

But I was able to [compile Ollama on RISC-V](/blog/2025/how-build-ollama-run-llms-on-risc-v-linux), and since [Ollama doesn't support Vulkan yet](https://github.com/ollama/ollama/pull/5059), I also [compiled `llama.cpp` with Vulkan support](/blog/2024/llms-accelerated-egpu-on-raspberry-pi-5) and ran it on the AMD GPUs.

{{< figure src="./p550-llm-radeontop.jpeg" alt="P550 radeontop showing LLM performance" width="700" height="394" class="insert-image" >}}

I got between 15 to 30 tokens per second on llama3.2 3B, and a few more tokens on an RX 580.

These older GPUs are only like $40-50, so if you _wanted_ to try out some small AI models, I mean... there are _worse_ ways to do it!

The setup burned between 100-150W of power, so again, for AI—at least until that NPU works—it's not very efficient.

## Conclusion

After _all that testing_, I'm confident saying this board isn't for the mainstream. It's a well-supported hardware platform for RISC-V, and software enablement is currently underway (there are probably already fixes for a few of the things I pointed out in this post!).

It's the fastest and most efficient RISC-V board I've tested, it has tons of standard interfaces to work with, and as a bonus, it fits inside a PC case!

Would I recommend you go buy one? No. But does it excite me, seeing RISC-V _hardware_ compatibility already closing the gap with Arm? Yes.

It'd be great to see three thriving ecosystems, with software supporting them all. Because the [AMD and Intel duopoly](https://finance.yahoo.com/news/intel-amd-duopoly-pc-processor-160640925.html) was doing the industry no favors, and with [Arm's licensing shenanigans](https://www.theregister.com/2025/02/06/arm_qualcomm_nuvia/), it'd be great to have another player on the low end.
