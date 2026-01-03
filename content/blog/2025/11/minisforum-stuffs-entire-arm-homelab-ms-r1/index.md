---
nid: 3511
title: "Minisforum stuffs an entire Arm Homelab in the MS-R1"
slug: "minisforum-stuffs-entire-arm-homelab-ms-r1"
date: 2025-11-10T16:01:10+00:00
drupal:
  nid: 3511
  path: /blog/2025/minisforum-stuffs-entire-arm-homelab-ms-r1
  body_format: markdown
  redirects:
    - /blog/2025/minisforum-stuffs-entire-homelab-its-new-ms-r1-arm-box
aliases:
  - /blog/2025/minisforum-stuffs-entire-homelab-its-new-ms-r1-arm-box
tags:
  - arm
  - homelab
  - linux
  - minisforum
  - ms-r1
  - reviews
  - video
  - youtube
---

{{< figure src="./minisforum-ms-r1-front.jpg" alt="Minisforum MS-R1 front" width="700" height="394" class="insert-image" >}}

The [Minisforum MS-R1](https://s.minisforum.com/4hRFZbj) uses the same Cix CD8180 Arm SoC as the [Orion O6 I reviewed earlier this year](/blog/2025/radxa-orion-o6-brings-arm-midrange-pc). But everything else about this thing is different.

What this thing _should_ be, is a box that runs Linux and can compete with at least an Apple M1 Mac mini, or a mid-range Mini PC. But what we _got_... is something different.

## Video

Hate reading? I also published a video on the MS-R1 on my YouTube channel. Watch it here, or scroll on past.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/WXfd0rOOtkg" frameborder='0' allowfullscreen></iframe></div>
</div>

## Hardware overview

Let's get started with the hardware. At first glance, it looks great!

{{< figure src="./minisforum-ms-r1-open-rear.jpg" alt="Minisforum MS-R1 open chassis rear ports" width="700" height="394" class="insert-image" >}}

You have a 12 core Arm CPU with a Mali G720 iGPU. There's a full-size PCIe slot, NVMe storage, WiFi 6E, and a ton of ports on the front and back.

You have a grand total of _9_ USB ports, with 2 of them Type C with DisplayPort 1.4.

There's HDMI, _dual_ 10 Gbps NICs (Realtek RTL8127), and even an old fashioned audio combo jack, so you can plug in a headset.

It looks great on my desk, it's quiet, it uses a 19V 180W power adapter (which is a bit chunky, but par for the course with Minisforum PCs), and overall, the hardware is some of the nicest of any Arm system, outside Apple's walled garden.

And the way you get inside is simple: press a little button and slide the chassis out of the shell (see photo above).

{{< figure src="./minisforum-ms-r1-u2-adapter-wifi-e-key-slot.jpg" alt="Minisforum MS-R1 U.2 adapter in WiFi card slot" width="700" height="394" class="insert-image" >}}

It came with adapters for a U.2 drive (see above) or a second M.2 drive, which replace the built-in Mediatek WiFi card.

And yes, the unit I'm testing is a review unit sent by Minisforum. They did not pay me to test the machine, write this blog post, nor did they have any input into its contents.

## Cix SoC - iGPU and a Big/Medium/Little Arm CPU

Now, let's dive into why this machine puzzles me, starting with the iGPU. Using Minisforum's default Debian 12 install, I could run `glmark2`, and it performed well, scoring 6322, far above something like a Raspberry Pi 5 (which got 1935).

But Vulkan support was iffy. `vulkaninfo` Segfaulted, and `vkmark` wouldn't run at all.

But GravityMark did. And while the [G720 won't bring home any awards](https://gravitymark.tellusim.com/report/?id=b47bb5b8bad5c54937dc475f1cdd7cf2607a37da), it's about on par [with the Adreno 750](https://gravitymark.tellusim.com/leaderboard/?api=vk&mode=one&offset=76) in Qualcomm's [Snapdragon 8 cx Gen 3](https://www.notebookcheck.net/Qualcomm-Adreno-750-GPU-Benchmarks-and-Specs.762136.0.html).

That's the chip Microsoft used in their 'Project Volterra' 2023 Windows Arm Dev Kit.

And that's not the only similarity between the two.

[Geekbench 6 scores were also pretty close](https://browser.geekbench.com/v6/cpu/compare/14893385?baseline=2570071), coming in at 1336 single core, and 6773 multicore.

{{< figure src="./minisforum-ms-r1-benchmark-geekbench-6.jpg" alt="Minisforum Geekbench 6 Arm benchmark MS-R1" width="700" height="394" class="insert-image" >}}

That soundly beats SBCs like the Pi 5 or a Rockchip. But it's still _well_ under Apple's four-year-old M1.

In other benchmarks, this thing is all over the place. I have two theories about that, which I'll get to.

But in real-world use, it does _feel_ fast. At least, faster than any Arm SBC. You can actually watch 4K video on YouTube while you do other things, which is kind-of a novelty on anything that's not Qualcomm or Apple.

More testing revealed some oddities, though.

Consider my [Top500 High Performance Linpack benchmark](https://github.com/geerlingguy/top500-benchmark). This is a massive CPU stress test, great for testing memory access, too.

I [played around with 4 cores, 8 cores, all 12 cores](https://github.com/geerlingguy/top500-benchmark/issues/82), and even limited the amount of RAM I was testing, because the results I was getting were confusing.

In the end, after some help from GitHub user [@volyrique](https://github.com/geerlingguy/top500-benchmark/issues/54#issuecomment-3413122598), we found the Cix P1 SoC is affected by the same BLIS issue other chips like the Nvidia GB10 'Superchip' and cloud chips using Neoverse N2 CPU cores run into: [Poor DGEMM performance for armsve build on Neoverse N2](https://github.com/flame/blis/issues/641).

We're diving a bit deep here, but with newer [SVE](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions) technology (vs. Arm's more traditional [NEON 128 bit SIMD](https://www.arm.com/technologies/neon)), chips can use arbitrary vector lengths. The BLIS library optimizes newer chips with an `armsve` configuration, which assumes 256+ bit vector lengths, and is not optimized at all for 128-bit vector lengths (used by the Cix P1 in the Orion O6 and Minisforum MS-R1).

_All that out of the way_, I have deleted the section of the video embedded above covering HPL entirely, and have updated my benchmark graphs below:

{{< figure src="./minisforum-ms-r1-benchmark-hpl-glflops-revised.png" alt="Minisforum HPL graph with other Arm systems" width="700" height="394" class="insert-image" >}}

The MS-R1 with it's 64 GB of RAM edged out my Orion O6 (I have the 16 GB model...), though it is less than half as performant as the M4 Mac mini.

Not a bad showing, overall, and after adjusting the HPL configuration to account for the instruction set mismatch, I was able to get a score almost triple that of the fastest small Arm SBCs'.

Energy efficiency is a step down, though—it's not the worst, and certainly, _under load_, it is better than most Intel/AMD systems:

{{< figure src="./minisforum-ms-r1-benchmark-hpl-efficiency-revised.png" alt="Minisforum HPL graph - efficiency" width="700" height="394" class="insert-image" >}}

But the efficiency story is _much_ worse considering the idle power draw:

{{< figure src="./minisforum-ms-r1-benchmark-power-idle-arm_0.jpg" alt="Minisforum MS-R1 - Idle power draw" width="700" height="394" class="insert-image" >}}

Unless you are running large workloads constantly, this machine will end up using far more energy than other Arm solutions (especially Apple's M-series Macs), due to the high idle power.

But _why is it so high_? This is a graph of core to core memory latency, showing how fast it is for different CPU cores to share memory on the system. Honestly, this isn't _horrible_, especially when I pair it with raw memory access speed:

{{< figure src="./minisforum-ms-r1-cix-c2clat.jpg" alt="Minisforum c2clat Cix SoC Arm" width="700" height="394" class="insert-image" >}}

{{< figure src="./minisforum-ms-r1-benchmark-memory-access_0.jpg" alt="Minisforum MS-R1 Memory Access benchmark" width="700" height="394" class="insert-image" >}}

The MS-R1's RAM is pretty fast (though notably slower than the O6, which directly impacts performance with tasks like AI inference).

But I think the strange CPU core layout is causing power problems; Radxa and Minisforum both told me Cix is working on power draw, and enabling features like [ASPM](https://en.wikipedia.org/wiki/Active_State_Power_Management).

It seems like for stability, and to keep memory access working core to core, with the big.medium.little CPU core layout, Cix wants to keep the chip powered up pretty high. 14 to 17 watts idle is beyond even modern Intel and AMD!

For networking, the onboard NICs provide a full 10 gigs, and the built-in WiFi 6E was good for a gigabit on my network.

And with 64 gigs of RAM, one thing this box could excel at compared to an SBC is local AI, even if it's just on the CPU.

I ran a bunch of different models that would fit in the memory, and here are those results:

{{< figure src="./minisforum-ms-r1-ai-cpu-benchmarks-llama.jpg" alt="Minisforum MS-R1 AI CPU benchmarks vs Arm systems" width="700" height="394" class="insert-image" >}}

This is one place where it actually _underperforms_ the older Orion O6 with the same CPU, which is directly related to the slower RAM speeds.

## Efficiency

The performance inconsistency is puzzling, but the power consumption is really what hurts the most—that's an area Arm is supposed to shine in. But it goes to show you, CPU core architecture and even process nodes aren't everything when it comes to effiency. Design matters.

Apple's M-series puts everything to shame, but even taking that out of the mix, it's not quite what I'd expect from 2025 Arm CPU design.

_Despite_ all that, it's quiet and the fans keep it cool. The performance profile ramps up the fans to 100%, but that didn't make much difference in real-world performance except making it about 50 dBa from a foot away instead of 40 dBa in the normal profile.

## Dedicated GPU Upgrade

If you're thinking about loading up AI models, or even modest gaming, a dedicated GPU will get you a lot further than the iGPU.

Minisforum added ventilation holes across the entire top, so a modded GPU like the [Abovetop RTX A2000](https://www.newegg.com/abovetop-Model-A2000laptop/p/1DW-00MF-00001?Item=9SIC0RRKGN4387&_gl=1*16zz3l2*_gcl_au*ODQ2NDM4NDA2LjE3NTg5MTE3MjM.*_ga*NDAwNjEzMzAzLjE3NTg5MTE3MjM.*_ga_TR46GG8HLR*czE3NTg5MTE3MjIkbzEkZzEkdDE3NTg5MTE4NzgkajQ1JGwwJGgxNTA0OTI0ODU2), with 8 gigs of VRAM, will fit and get adequate cooling. Similar to older MS-** Minisforum workstations, this machine only fits half-height single-slot PCI Express cards, and ones that are not too long at that.

Installation is easy, though finicky due to the tight spaces. You unscrew and pull a small retention clip out, remove the slot cover, and fit the new card. It rests on a small foam spacer to isolate the card from the motherboard.

{{< figure src="./minisforum-ms-r1-gpu-installed-pcie-rear.jpg" alt="Minisforum MS-R1 rear with Nvidia RTX A2000 installed" width="700" height="394" class="insert-image" >}}

Booting the computer back up, I saw the card using `lspci`, so Linux can see it. But I wasn't able to install the drivers on the Debian 12 OS image shipped with the machine. I also tried an [Intel Arc A310 ECO](https://amzn.to/3LSnuYl), a lower-specced and smaller single-slot card, but that wasn't even recognized when I ran `lspci`.

For the Intel card, it's probably just a signaling issue, though—I'm not going to hold it against the MS-R1 since I've had issues with the A310 ECO on other systems.

## BIOS detour

I'll get back to A2000 testing, but these experiments took me on a detour into the BIOS.

{{< figure src="./minisforum-ms-r1-cix-bios.jpg" alt="Minisforum MS-R1 Cix BIOS screen" width="700" height="394" class="insert-image" >}}

There are settings for USB, RAM, power on behavior, and a lot more. It's pretty complete, but I still see a lot of things labeled 'Beta', so keep that in mind if you buy one of these things.

One thing I tested that didn't work is the AC Power Loss setting. You're supposed to be able to tell it to turn on when power is restored—that's great for something like a homelab. But the BIOS setting didn't do anything. I remembered seeing a hardware switch on the board, though, and sure enough! That's how you _actually_ control the AC power loss setting.

## Switching to Ubuntu

Getting back to the A2000, I decided to switch gears and try Ubuntu from an Arm ISO install via USB flash drive. The process was easy enough (I didn't have to change anything in the BIOS), and Ubuntu installed without a hitch.

The A2000's drivers were automatically installed, and I was off to the races.

AI is obviously faster on the GPU (total system power draw was around 94W):

{{< figure src="./minisforum-ms-r1-benchmark-ai-a2000.jpg" alt="Minisforum MS-R1 AI benchmark on RTX A2000" width="700" height="394" class="insert-image" >}}

And GravityMark, a good proxy for how games will run on a given GPU, ran fine too, increasing the score over the iGPU from [3,037](https://gravitymark.tellusim.com/report/?id=b47bb5b8bad5c54937dc475f1cdd7cf2607a37da) to [16,679](https://gravitymark.tellusim.com/report/?id=5aae292da4c60d69a518a594071903141244fb18).

## Conclusion

Having a full PCI Express slot in here _is_ nice. Coupled with the extra included U.2 and M.2 adapters, it's clear Minisforum thinks of this thing as a good homelab box. They even published guides for installing [Proxmox](https://github.com/minisforum-docs/MS-R1-Docs/blob/main/PlayBook/MS-R1-How-To-Install-PVE.md) (a community maintained version) and [Jellyfin](https://github.com/minisforum-docs/MS-R1-Docs/blob/main/PlayBook/MS-R1-Jellyfin-Docker-Compose.md) with iGPU acceleration. Considering expansion-options-per-cubic meter, this has all other Arm machines beat, including the Mac mini.

Honestly, this works fine as an Arm desktop, certainly better than any SBC. But Intel and AMD exist, and so does Apple, for that matter, and that makes this a bad value where it stands _today_, in the $500-600 range. Unless you're an Arm enthusiast, you should save some money and get a different mini PC—even one of [Minisforum's other MS-series desktops](https://store.minisforum.com/collections/mini-pc). _Or_ if you can afford _$600_ bucks, buy the best value Arm desktop on the market, the [M4 Mac mini](https://www.apple.com/mac-mini/). Of course, that thing [can't run bare metal Linux](https://asahilinux.org/docs/platform/feature-support/m4/#soc-blocks), so take that into account.

I like that it exists. And I like that Cix and Minisforum are trying to shake up the Arm desktop market a bit. But it's still half-baked:

  - Can performance and power issues be fixed in firmware?
  - Will they get all the drivers mainlined so all features work in every Linux distro?
  - Windows can run on here, but will Nvidia ever release GPU drivers for Windows on Arm?

I'm not sure. But I will try gaming in Linux on here soon, and some other tests. So make sure you [follow this blog's RSS feed](https://www.jeffgeerling.com/blog.xml) or [subscribe over on YouTube](https://www.youtube.com/c/JeffGeerling), if you want to follow along!

You can buy the [Minisforum MS-R1](https://s.minisforum.com/4hRFZbj) from Minisforum's online store, starting around $500 at the time of this writing.
