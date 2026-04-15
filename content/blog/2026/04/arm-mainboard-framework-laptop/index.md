---
date: '2026-04-15T09:00:00-05:00'
tags: ['arm', 'framework', 'laptop', 'linux', 'right to repair', 'video', 'youtube', 'metacomputing']
title: 'An Arm Mainboard for the Framework Laptop'
slug: 'arm-mainboard-for-framework-laptop'
---
Using the repair-friendly Framework 13 laptop chassis, I've tested the low-end x86 option (a [Ryzen AI 5 340 Mainboard](https://github.com/geerlingguy/sbc-reviews/issues/90)), the fastest RISC-V option ([DC-ROMA II](https://github.com/geerlingguy/sbc-reviews/issues/82)), and today I'm publishing results from the only Arm Mainboard, the [MetaComputing AI PC](https://github.com/geerlingguy/sbc-reviews/issues/103), which has a 12-core Arm SoC and up to 32 GB of soldered-on RAM.

{{< figure
  src="./metacomputing-arm-framework-hero.jpg"
  alt="MetaComputing AI PC Mainboard next to Framework 13 laptop"
  width="700"
  height="auto"
  class="insert-image"
>}}

My Framework 13 has run on x86, RISC-V, and now Arm, making it something of a 'Ship of Theseus'.

The AI PC Mainboard uses Cix's P1 SoC, an odd duck in the Arm world. There are 12 CPU cores, but they're structured in a way that necessitates disabling four of them to run Windows 11—and yes, this board _should_ be able to do that.

I have a video going over my experience swapping out the Framework 13's guts and testing everything (including setting up FEX and playing some x86 games through Steam):

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/CIb87SJ4xwo' frameborder='0' allowfullscreen></iframe></div>
</div>

If you'd rather read than watch a video, scroll on!

## Hardware

The AI PC Mainboard features the Cix P1 CP8180, a chip that's also found in Radxa's [Orion O6](https://github.com/geerlingguy/sbc-reviews/issues/62), [Minisforum's MS-R1](https://github.com/geerlingguy/sbc-reviews/issues/89), and the [Orange Pi 6 Plus](https://amzn.to/4tIDr43).

RAM chips are soldered to the mainboard (16GB of LPDDR5 in the review sample I was provided), and all the typical I/O for a Framework Mainboard is present (a M.2 NVMe slot, a WiFi module slot, display, keyboard, sound, and battery connections, and four USB-C ports for high-speed peripherals, power input, and display out).

{{< figure
  src="./metacomputing-arm-framework-hero.jpg"
  alt="MetaComputing AI PC Mainboard installed inside Framework 13"
  width="700"
  height="auto"
  class="insert-image"
>}}

It was easy to swap out mainboards so I could test this build in a chassis. And my first question was whether this mainboard fixes the major drawback of the Cix P1 chip: idle power consumption.

And it does... a little. Compared to the other Cix P1 systems I've tested:

TODO Graph idle power 1

But we're still far from ideal—here's a comparison to the MacBook Neo, and Framework's lowest-spec AMD Mainboard (which is also faster and about as efficient as the Cix CPU in heavy workloads):

{{< figure
  src="./metacomputing-ai-pc-mainboard-idle-power-compared-others.jpg"
  alt="MetaComputing AI PC Mainboard compared to MacBook Neo and AMD Ryzen AI 5 340 Idle Power Draw"
  width="700"
  height="auto"
  class="insert-image"
>}}

## Software

MetaComputing currently provides an 'official' Ubuntu 25.04 ISO you can flash to an NVMe drive to boot with full hardware support, but this laptop has a full BIOS, with UEFI support. _However_, not all distros are supported yet... I didn't test any other distros yet, but [Windows for Arm at least partially installed](https://github.com/geerlingguy/sbc-reviews/issues/103#issuecomment-4226472014), which is a good start.

But running their official Linux build, I was able to run Vulkan and OpenGL on the chip's Arm Mali G720 Immortalis iGPU. I had some trouble with `vkmark`, but [GravityMark scored 7,627](https://gravitymark.tellusim.com/report/?id=8ed048387ccca9a89ba294aed959523bd64bd534), comparable to the graphics in Apple's A14 SoC, and a little faster than Intel's low-end graphics in chips like the N150.

{{< figure
  src="./metacomputing-ai-pc-mainboard-gravitymark.jpg"
  alt="MetaComputing AI PC Mainboard running GravityMark Benchmark"
  width="700"
  height="auto"
  class="insert-image"
>}}

[Geekbench scores](https://browser.geekbench.com/v6/cpu/17448233) are right in line with the other Cix P1 systems I've tested, though [High Performance Linpack scores](https://github.com/geerlingguy/top500-benchmark/issues/94) are not. I'm not sure if it's the slightly slower memory, or what, but this system scored about half as well as the MS-R1 and Orion O6 when running the memory-intensive FP64 HPL benchmark.

But rather than compare the chip against itself, let's put the numbers in context, using Geekbench, as it's a good proxy for general perceived performance for smaller systems:

{{< figure
  src="./metacomputing-ai-pc-mainboard-geekbench-compared-others.jpg"
  alt="MetaComputing AI PC Mainboard Geekbench comparison to MacBook Neo and AMD Ryzen AI 5 340"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO... Neo throttling and stuff. But in price class of Air

## Fex for Steam Games on Arm

TODO: Quickly summarize, maybe have embed of slideshowness

## Conclusion

TODO, copy from video conclusion?

You can find all my test data and any further updates in the [MetaComputing AI PC issue](https://github.com/geerlingguy/sbc-reviews/issues/103) in my SBC Reviews project.

And you can buy the MetaComputing AI PC Mainboard (either standalone, or as part of a Framework 13 build) direct from MetaComputing: [AI PC Arm Mainboard](https://metacomputing.io/products/metacomputing-aipc?variant=50604798574898).
