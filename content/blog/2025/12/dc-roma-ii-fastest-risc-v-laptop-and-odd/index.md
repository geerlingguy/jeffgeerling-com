---
nid: 3517
title: "The DC-ROMA II is the fastest RISC-V laptop and is odd"
slug: "dc-roma-ii-fastest-risc-v-laptop-and-odd"
date: 2025-12-08T15:40:07+00:00
drupal:
  nid: 3517
  path: /blog/2025/dc-roma-ii-fastest-risc-v-laptop-and-odd
  body_format: markdown
  redirects:
    - /blog/2025/dc-roma-ii-has-fastest-risc-v-chip-ive-tested-and-odd
aliases:
  - /blog/2025/dc-roma-ii-has-fastest-risc-v-chip-ive-tested-and-odd
tags:
  - computer
  - dc-roma
  - framework
  - laptops
  - p550
  - reviews
  - risc-v
  - video
  - youtube
---

{{< figure src="./dc-roma-ii-framework-external-display.jpeg" alt="Framework 13 DC-ROMA II DeepComputing Laptop with external HDMI display" width="700" height="394" class="insert-image" >}}

Inside this [Framework 13](https://frame.work/laptop13) laptop is a special mainboard developed by DeepComputing in collaboration with Framework. It has an 8-core RISC-V processor, the ESWIN 7702X—not your typical AMD, Intel, or even _Arm_ SoC. The full laptop version I tested [costs $1119](https://store.deepcomputing.io/products/dc-roma-ai-pc-risc-v-mainboard-ii-for-framework-laptop-13?variant=50950609895588) and gets you about the performance of a Raspberry Pi.

A Pi 4—the one that came out in 2019.

But unlike the Pi 4, this eats up 25 watts of power at idle, meaning the poor battery only lasts 2-3 hours.

And it uses a bit of tech I don't remember seeing since, like... well...

{{< figure src="./dell-optiplex-780.jpeg" alt="Dell Optiplex 780" width="700" height="394" class="insert-image" >}}

_This_ thing. From 2009.

But before we get to that, no, I'm _not_ recommending most of you reading this even _consider_ buying the DC-ROMA II. It's is a very niche product, meant for RISC-V developers and enthusiasts.

But I'm still excited to see it, for two reasons:

  1. DeepComputing decided to build a Framework Mainboard instead of a custom laptop. Meaning after the system is unsupported in two years, you can upgrade the mainboard to a modern AMD or Intel version, and get a lot more life out of the rest of the chassis.
  2. It has the fastest RISC-V chip I've ever tested, with 8 SiFive P550 CPU cores, which increases my hope we might get three viable CPU architectures: x86, Arm, and RISC-V. (Yes I know there are others, but x86 and Arm are ruling over the rest right now).

But no, _objectively_ this is not a good laptop.

And if it isn't obvious, DeepComputing, who sent me this laptop, are not paying me for this post. They did provide the laptop, but have no say in my review.

## Video

I have a full video of this review, if you'd like to watch. Otherwise, scroll past for the rest of the written version!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/OkFfTK8S00c" frameborder='0' allowfullscreen></iframe></div>
</div>

## Hardware

If you've never heard of Framework, they make repairable and upgradable laptops. The Framework 13 seems to be a midrange option, and the build quality is good. It's not quite Apple-premium—especially the keyboard, which is a little mushy—but overall it's a solid laptop.

{{< figure src="./dc-roma-ii-framework-expansion-slots.jpeg" alt="DC ROMA II Framework 13 Expansion Slots" width="700" height="394" class="insert-image" >}}

It has four expansion slots (two on each side) that you can stick in a number of modules, from USB-C ports to HDMI, SD card readers, or even Ethernet. It also has an audio headset jack (separate from the modules).

I tested USB-C modules, and got about 100 Megabytes per second for file copies, so not quite the full USB3 speed I expected, but at least it's better than USB2. I also tested an HDMI module in the top right slot, and was able to run a full external display without any issues (see photo at top of post).

The Framework's built-in display is 2.2K, with a nice 3x2 aspect ratio. Inside it has a 56 watt-hour battery, which for _normal_ Framework 13 builds, would get you 8 or 9 hours of use.

But this isn't a review of the Framework 13—the laptop hardware itself is fine, and I'd say overall midrange.

I'll focus more on the _RISC-V mainboard inside_, which DeepComputing custom-built for the 8-core P550 RISC-V CPU.

If you haven't heard of RISC-V, it is an [open ISA](https://riscv.org/blog/a-complete-overview-of-risc-v-open-isa-for-your-quick-reference/), meaning the overall chip architecture isn't tied to one or two companies' whims. RISC-V CPUs are already popular in hard drive controllers and microcontrollers, but they've had a harder time in things like SBCs, laptops, and desktops. We'll see why later.

But with the Framework, getting to the mainboard is easy, compared to most laptops. You flip over the laptop, unscrew 5 screws, flip it _back_ over, and pull off the top cover.

{{< figure src="./dc-roma-ii-open-desk-framework-13.jpeg" alt="Framework 13 DeepComputing DC-ROMA II Open inside" width="700" height="394" class="insert-image" >}}

(Framework even includes the only tool you need for all repairs in the box.)

The CPU resides under the cooling module, and once removed, we reveal the odd CPU:

{{< figure src="./dc-roma-ii-eswin-7702x-soc-dual-die-risc-v-chip.jpeg" alt="ESWIN EIC7702X dual die CPU in DC-ROMA II Mainboard" width="700" height="467" class="insert-image" >}}

It looks like there are two identical ESWIN EIC7702 CPU dies—the same die that's used in the single-chip [HiFive Premiere P550 I tested earlier this year](/blog/2025/sifives-hifive-premier-p550-strange-powerful-risc-v-board).

Looking at the RAM layout on the mainboard, two 8 GB chips go to one CPU, and the other chips go to the other one.

A strange architecture, but not unprecedented—I mentioned the Dell Optiplex earlier in the video. It has an Intel Core 2 Quad CPU, and it has the exact same weird architecture: Intel took two Core 2 _Duo_ CPU dies and [slapped them together on an interposer](https://www.reddit.com/r/overclocking/comments/1bdusa6/delidding_intel_core2_quad_6600/).

Those Core 2 Quad chips would burn a lot of power, and had issues with cross-die memory access being slower than accesses on the same die.

Did ESWIN solve those problems on this new RISC-V chip? Short answer: no. Before we get to benchmarks, I'll talk a little bit about Linux support.

## Software

The DC-ROMA II ships with Ubuntu 24.10. Newer Ubuntu releases like 25.10 won't run on it.

RISC-V is a newer CPU architecture, and up until the past year or two, important RISC-V standards for higher-perfoming CPUs were still being formalized. The latest standard, RVA23, is the main target for a lotta Linux distros, [like Ubuntu](https://www.phoronix.com/news/RISC-V-RVA23-Progress-Ubuntu).

The P550 cores inside the ESWIN CPU don't support RVA23, so Ubuntu 24.10 be the _only_ version that'll ever run on it!

There's also a special version of Fedora 42, but this is one of the main reasons I recommend you _don't_ buy these first-generation RISC-V computers, unless you're really into the architecture, or you're developing software that you wanna run on RISC-V.

But assuming you're okay with all that, how is it using this as a laptop?

Well, bringing back another theme from the early 2000s, it's one of those laptops with the fan running pretty much all the time.

And it would ramp up to 100% quite often.

Why is that? Well, the power profile for this complicated dual-die chip is not efficient. The total system power draw is about _25 watts_ while it's sitting there doing nothing.

{{< figure src="./ubuntu-menu-on-dc-roma-ii.jpeg" alt="Ubuntu on DC-ROMA II Laptop" width="700" height="394" class="insert-image" >}}

Other modern laptops I've tested idle between 2-10W, depending on screen brightness.

The DC-ROMA II, even with the screen turned _off_, is burning through the battery like crazy.

I tested battery life through a few charge cycles, and I'd say you can expect 2-3 hours, tops. So, again, this is not a laptop you should buy if you just want a decent Linux laptop. The regular Framework 13, maybe, but not the RISC-V version.

The screen looks great, but running normal applications on the RISC-V chip is sluggish. Just like an older Pi 4, you can only expect to get smooth video playback at lower resolutions, like 720p. And the UI is generally a little choppy.

It's not horrible, and it's actually the best experience I've had running a RISC-V desktop environment—but that's not saying much.

Chromium ran better than Firefox, due to GPU acceleration working in that browser. I could get 40 fps on Chromium running [WebGL Aquarium](http://webglsamples.org/aquarium/aquarium.html) versus 16-17 fps on Firefox.

SuperTuxKart was playable after I turned down all the settings, but it was only getting single-digit FPS at 1080p.

{{< figure src="./crispydoom-dc-roma-ii-laptop.jpg" alt="CrispyDoom running on DC-ROMA II RISC-V Laptop" width="700" height="394" class="insert-image" >}}

At least [Doom](https://github.com/fabiangreffrath/crispy-doom) gave me a full 60 fps at full resolution—but that game's from the 90s, so that's not surprising!

I keep comparing this to the Pi 4 though, because that was the first Arm SBC where I could use it as a desktop and not feel like it was _painful_—just, _slow_.

The biggest let-down besides the power draw was how features on this chip are still not supported.

It includes H.265 encode and decode, and a modest but decent built-in NPU, but using those things requires software support, and that was a little lacking.

They provided a demo of Deepseek R1 7B optimized for the NPU, and it was respectable, running around [5 tokens per second](https://github.com/geerlingguy/ai-benchmarks/issues/28). But trying to get other models to run on it was difficult. If I just ran models on the _CPU_, I would get less than a token per second.

And even though the system comes with _32 GB_ of RAM, half of it is allocated to the NPU, somewhere in the firmware. So unless you use one of the few demos that runs on the NPU, that extra 16 GB is wasted.

DeepComputing _did_ say the RAM might be able to be re-allocated, but I wasn't able to get that to happen in time for this post. So for now I guess think of this machine as having half the RAM that's advertised, if you're not using the NPU.

## Performance

But having only half the RAM is only half the problem. Let me show you a few performance graphs (full testing data is stored in my sbc-reviews project, as always](https://github.com/geerlingguy/sbc-reviews/issues/82)), and we'll talk about the other half.

{{< figure src="./dc-roma-ii-geekbench6.jpg" alt="Geekbench 6 DC-ROMA II" width="700" height="394" class="insert-image" >}}

First up, Geekbench. It's not a perfect benchmark, but it's a good match to the overall 'feel' of a computer's UI performance, at least for these systems.

This _is_ the fastest RISC-V computer I've ever used, but... RISC-V isn't fast. At least not with any of the chips I've tested so far.

The chip even beats the Raspberry Pi 4 (7 years old, remember) on HPL performance, but the efficiency in doing so is pretty rough:

{{< figure src="./dc-roma-ii-hpl-efficiency.jpg" alt="DC-ROMA II HPL Efficiency" width="700" height="394" class="insert-image" >}}

It's less efficient than the same single chip CPU in the HiFive Premiere P550, which isn't too surprising, since you have to use more power to keep the two chips in sync all the time. But even Intel looks amazing here, with their N100 chip in that LattePanda Mu up top.

And these are _far_ from the most efficient Arm and Intel systems I've tested. I just wanted to find some modern systems in the same ballpark, to give RISC-V the best chance possible.

The graph that really destroys this thing for a _laptop_, though, is this one:

{{< figure src="./dc-roma-ii-idle-power.jpg" alt="DC-ROMA II Idle Power Draw" width="700" height="394" class="insert-image" >}}

25 watts at idle is a _lot_.

I think a large part of the reason the performance and efficiency numbers are so rough comes down to _memory access_. This is a measurement of _core to core latency_—how many nanoseconds it takes one CPU core to access memory from another core:

{{< figure src="./c2clat-dc-roma.jpg" alt="c2clat DC-ROMA II" width="700" height="394" class="insert-image" >}}

Cross-die memory access is over 1000 nanoseconds. That's an order of magnitude slower than memory accesses on the same die.

GitHub user [@ganboing speculates](https://github.com/geerlingguy/sbc-reviews/issues/82#issuecomment-3565169651):

> The critical issue here is that the LLC (last-level-cache) on each die is only responsible for the memory connected to the die. It doesn't care about remote memory, and the logic on each Die is probably quite straightforward: if the address belong to myself, use my L3, otherwise, ask the remote L3. This can be further validated by [the patch from ESWIN](https://github.com/DC-DeepComputing/fml13v03_linux/blob/03236c8570be3c9796139dc4efcfece05c672003/drivers/soc/sifive/sifive_ccache.c#L112-L138) where the code checks to see which cache controller a particular cache line belongs to, and then invalidate.
> 
> Thus, you actually get the worst performance for core-to-core latency in the same die if the synchronization variables happen to reside in the remote die memory, because it has to reach out to L3 on remote die, then back. The estimated latency for this scenario is 1029 * 2 - 79 = 1979, which is pretty close to the actual number. To me this is really inefficient. I'd imagine all modern multi-socket/die CPUs to be able to cache remote socket/die memory and snoop for modifications. Here it's more like ESWIN glued together 2 P550 clusters without too much thought.

I think @ganboing is on to something, and it is also somewhat confirmed by [this post on the SiFive forums](https://forums.sifive.com/t/high-core-to-core-latency-from-c2clat-benchmark/7616/2)—where @dconn notes core designs following the P550 should not suffer from the same problem.

## Compared to Dell Optiplex 780

I wanted to see how the Dell Optiplex system with the Core 2 Quad (from 2009) stacks up against this modern ESWIN chip.

{{< figure src="./c2clat-dell-optiplex-780-c2q.jpg" alt="Dell Optiplex 780 Core 2 Quad c2clat" width="700" height="394" class="insert-image" >}}

And... it's a lot better. Granted, this is a _workstation_ CPU. But back in 2009, Intel figured out how to get two dies communicating at just over 100 nanoseconds. Apparently we've forgotten how to do that!

The almost 17-year-old computer [_still_ beats the DC-ROMA II in Geekbench](https://github.com/geerlingguy/sbc-reviews/issues/88). And in raw HPC computing performance. And... well, not in efficiency. At least RISC-V can take a small win here.

## Benefits of Framework

Anyway, I don't want you to think I hate the DC-ROMA II. In fact, it's the opposite. I've been following RISC-V for years now, and the thing I liked most is that it's built into a Framework Mainboard form factor.

Because of that, the entire laptop chassis won't go to ewaste in a couple years once Linux isn't supported on it.

To give a proper comparison in the exact same chassis, I tested Framework's cheapest [AMD Mainboard](https://frame.work/products/mainboard-amd-ai300?v=FRANTE0005) (kindly provided by Framework). It costs around $450, and a full Framework 13 with the AMD AI 340 configuration is actually cheaper than the equivalent DC-ROMA II setup.

I replaced the mainboard, and with the DC-ROMA, I had a choice of either installing it in a [$40 Cooler Master case](https://frame.work/products/cooler-master-mainboard-case?v=FRANHDCM01), or 3D printing my own [Framework Mainboard case](https://www.printables.com/model/1049890-framework-industrial-mainboard-case)—which is what I did:

{{< figure src="./framework-desktop-3d-printed-case-dc-roma-ii.jpg" alt="Framework Laptop 13 3D printed Mainboard case with DC-ROMA II" width="700" height="394" class="insert-image" >}}

I re-ran all my benchmarks on the base model AMD Framework 13 build, and it absolutely slaughtered the ESWIN chip, in every metric.

{{< figure src="./amd340-gb6-dc-roma.jpg" alt="AMD AI 340 vs DC-ROMA Geekbench 6" width="700" height="394" class="insert-image" >}}

In a few benchmarks, the DC-ROMA is somewhat visible on the chart at least, but the one that maybe matters _most_ for laptop users is idle power consumption, and it's rough:

{{< figure src="./amd340-idle-power.jpg" alt="AMD AI 340 vs DC-ROMA Idle Power Draw" width="700" height="394" class="insert-image" >}}

BUT, I should re-iterate, you're not buying the DC-ROMA II if you're looking at the best performance or efficiency. The thing I like is how it's a modular, future-proof chassis, because they partnered with Framework.

## RP2350 GPIO Module

On the theme of modularity, one last thing I got to test on this laptop was a new module with two _more_ RISC-V CPU cores, the [RP2350 GPIO expansion module](https://github.com/semitov/rp2350-gpio-card) from SemiTO-V (I hope I'm pronouncing that right...). It's from a student team at Polytechnic of Turin, in Italy.

{{< figure src="./dc-roma-ii-semitov-rp2350-framework-expansion-module.jpeg" alt="DC-ROMA II Raspberry Pi RP2350 Framework Expansion Module" width="700" height="394" class="insert-image" >}}

They sent over this module, which is part of their curriculum towards learning CPU architecture. This module has a Raspberry Pi RP2350, which has it's own RISC-V cores—two tiny Hazard3 CPU cores.

{{< figure src="./blink-led-from-rp2350-framework-expansion-module.jpeg" alt="Blink LED on breadboard using RP2350 expansion module with Framework 13 laptop" width="700" height="394" class="insert-image" >}}

It doesn't accelerate the DC-ROMA, but it does add on GPIO capabilities, meaning you can do things like... well, I'm just blinking an LED on here, but you get the idea.

It's a neat little open source hardware design that was supported by DeepComputing and Framework, and I love to see these community projects, especially when they help the next generation learn about computing hardware.

The students also built [a Python library, 'MCL'](https://github.com/semitov/SemiTOV-MCL) to make it easier to interact with the RP2350 from Python directly.

## Conclusion

{{< figure src="./dc-roma-ii-framework-13-open-back.jpg" alt="DC-ROMA II Framework 13 laptop open back" width="700" height="394" class="insert-image" >}}

But the [DeepComputing DC-ROMA II](https://store.deepcomputing.io/products/dc-roma-ai-pc-risc-v-mainboard-ii-for-framework-laptop-13?variant=50950610452644)—or the 'AI PC' as it's labeled on the website...

Do I recommend you buy it? No. Not unless you're deeply into RISC-V or you're developing stuff and wanna test it on real RISC-V hardware.

It's not a great laptop, but it's the best RISC-V laptop I've seen. And the fastest RISC-V computer I've ever used. Which isn't saying much right now, but functional and slow is better than fast and broken—which is the state of many Arm boards I test!
