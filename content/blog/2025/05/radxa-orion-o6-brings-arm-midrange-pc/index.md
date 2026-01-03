---
nid: 3464
title: "Radxa Orion O6 brings Arm to the midrange PC"
slug: "radxa-orion-o6-brings-arm-midrange-pc"
date: 2025-05-09T14:02:00+00:00
drupal:
  nid: 3464
  path: /blog/2025/radxa-orion-o6-brings-arm-midrange-pc
  body_format: markdown
  redirects:
    - /blog/2025/radxa-orion-o6-brings-arm-midrange
aliases:
  - /blog/2025/radxa-orion-o6-brings-arm-midrange
tags:
  - arm
  - arm64
  - build
  - mini itx
  - motherboard
  - pc
  - reviews
  - video
  - youtube
---

{{< figure src="./radxa-orion-o6-motherboard-hero.jpeg" alt="Radxa Orion O6 Motherboard bare CPU Cix" width="700" height="467" class="insert-image" >}}

...with caveats.

## TL;DR

  - The [Radxa Orion O6](https://radxa.com/products/orion/o6/) is an Arm ITX motherboard with up to 12 cores, 64 GB of RAM, and Armv9.2 support, starting just over $200 USD
  - The board has a [SystemReady SR-certified BIOS](https://dl.radxa.com/orion/o6/images/bios/SystemReady/latest/), which allows running Windows on Arm and many Linux arm64 ISOs unaltered
  - The firmware still has many quirks, enough that I wouldn't recommend it if you don't enjoy tinkering with drivers (remember how I said to [temper your expectations](/blog/2025/orion-o6-itx-arm-v9-board-temper-your-expectations) in February?)
  - Prices for those in the US (like me) just tripled due to import tariffs (ordering the 32 GB model went from $400 to $1500).

The rest of this post is a version of today's video, modified to suit the blog. You can watch the video version below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/OMnCqmM-WKo" frameborder='0' allowfullscreen></iframe></div>
</div>

## Radxa Orion O6

I _pre-ordered_ the $300 32GB 'AI kit' the day the Orion O6 was [announced](https://github.com/JammyZhou/radxa-orion-o6-info-hub/tree/main). And... it never arrived. I'll discuss why at the end of the post, but you may wonder: if it never arrived, how did you review it?

Well, Radxa sent me a [_16 gig_ version of board](https://arace.tech/products/radxa-orion-o6?variant=43770715308212) for testing and review. I always disclose when something is provided, so I'm disclosing that here. See [all my sponsorship and review policies on GitHub](https://github.com/geerlingguy/youtube?tab=readme-ov-file#sponsorships).

They sent a 16 GB kit to many hardware testers and reviewers, and for _months_, we've had what Radxa calls a [debug party](https://forum.radxa.com/t/orion-o6-debug-party-invitation/25054). People post their issues, and hopefully Radxa fixes some of those things before the public launch.

Except, the public launch _already happened_, and there are still _fundamental_ problems with the board. I'll talk about those after I walk through the hardware.

## Hardware

{{< figure src="./orion-o6-in-acrylic-case.jpg" alt="Orion O6 in acrylic case on desk" width="700" height="394" class="insert-image" >}}

In the box, you get the O6 board itself, with a heatsink/cooler combo. It also has an acrylic case that looks nice and provides adequate ventilation, though it gets in the way of PCIe card brackets, if you don't remove them.

It's powered by a soldered-on CIX CD8180 SoC, with the following specs:

  - Armv9.2
  - 12 CPU cores (4x 'big' A720 at 2.6 GHz, 4x 'medium' A720 at 2.4 GHz, 4x 'little' A520 at 1.8 GHz)
  - 12MB L3 shared cache
  - Arm Immortals G720 MC10 GPU
  - Cix 30 TOPS NPU

The CPU is backed by up to 64GB of LPDDR5 RAM, with a 128 bit bus. This means memory bandwidth can get 'up to 96 GB/s' (though in reality, for _CPU_ tasks, I measured up to 40-50 GB/s).

{{< figure src="./orion-o6-rear-io_0.jpg" alt="Orion O6 Rear IO" width="700" height="394" class="insert-image" >}}

For IO, though, this is the most fully-featured Arm board outside of server-class boards from Ampere:

  - 2x USB-C ports for both PD and even DisplayPort. The first port can do 4K60 output.
  - 2x USB 2.0 Type A / 2x USB 3.2 Type A
  - HDMI (up to 4K60)
  - DisplayPort (up to 4K120)
  - Dual 5 Gbps Ethernet (RTL8126)
  - Headset jack

On the surface of the board, there are front panel IO and audio headers, power input via either USB-C PD (65W recommended) or 24-pin ATX header.

There's also a lot of PCIe Gen 4 lanes exposed:

  - M.2 M-key (up to 2280 size) Gen 4 with 4 lanes
  - M.2 E-key (2230 size) Gen 4 with 2 lanes
  - PCIe x16 slot, Gen 4 with 8 lanes

My _favorite_ part is the full-size PCI Express slot, which Radxa forum user [willy pushed to its limit with 100 Gbps networking](https://forum.radxa.com/t/orion-o6-debug-party-invitation/25054/178?u=geerlingguy). He was able to get 70 gigabits of traffic through HAproxy, meaning this board _could_ be a quiet networking beast.

_Could_ be, because as I've found, there's also a _lot_ of weirdness around how the CPU works, that prevents most multi-core apps from running as fast as they _should_.

## Bringup

And anyone who's bought Radxa hardware early on knows this, but it bears mentioning: this board needs a little more time in the oven.

Radxa has a [docs site with a lot of helpful information](https://docs.radxa.com/en/orion/o6). The board runs a lot of things well already. But if you already ordered one of these things, don't expect all the features on their website to run day-one.

Some things, don't expect them to _ever_ run. In fact, when I pre-ordered my 32 GB board, the website said there were [12 cores at up to 2.8 Gigahertz](https://github.com/geerlingguy/sbc-reviews/issues/62#issuecomment-2754731323). As of today, the specs were updated to showing 12 cores, but 'up to 2.6 gigahertz'.

And in reality, with the latest firmware, depending on how you're running the board, you might only get _8_ cores. And only 2.4 or 2.5 gigahertz.

But in positive news, the firmware that limits the board to 8 cores is SystemReady SR certified, meaning it has full UEFI support and can run Windows or Linux arm64 natively.

That _doesn't_ mean everything works out of the box though. If you want run Windows, there are still _precious few drivers_ for Windows on Arm. And on Linux, depending on what version and what distro you install, you might or might not get support for features like the iGPU, or the 5 Gbps Ethernet. Each of the major distros I tested was lacking one feature or another.

In a year or two, the Orion O6 will be in a better place. I probably spent a dozen hours just working on different driver issues to test everything. That's not something I'd want you to have to do, too.

## Benchmarking

After not one but _two_ full cycles of testing, first on a 0.2.x firmware, then again on the SystemReady firmware at version 9, [I have test data](https://github.com/geerlingguy/sbc-reviews/issues/62). [A lot of it](https://github.com/geerlingguy/sbc-reviews/issues/62#issuecomment-2832658093).

I've said before, what I'm looking for is basically Apple's M-series performance and efficiency, but in a more open platform.

{{< figure src="./orion-o6-geekbench-results_0.jpg" alt="Orion O6 Geekbench Results" width="700" height="394" class="insert-image" >}}

And... we get a _little_ bit of that. This thing is at least in the same _ballpark_. Well, the same ballpark as Apple's M1, which is five years old now. But it's _way_ off [on efficiency](https://github.com/geerlingguy/top500-benchmark/issues/54).

There's something weird with the CPU, because even after multiple firmware updates, benchmarks are all over the board, though _on average_, the O6 is more snappy and responsive than a Raspberry Pi.

But at $200 and with _12 cores_, I don't want to compare it to a Raspberry Pi. I want to compare it to an M2 or Snapdragon X. Compared to those chips, this thing is almost half the speed.

And in terms of efficiency, for some reason I barely broke 1 Gflop/W of FP64 performance on the O6. My Raspberry Pi 5 gets nearly 3 Gflops/W, while my M4 Mac mini gets _7_.

And some benchmarking software reports 2.5 GHz, others report 2.4 GHz. And all that, despite me setting the BIOS to _2.6_ GHz!

As mobile SoCs (the A720/A520 cores are targeted at mobile) grow more complex, with Arm's big.LITTLE or Intel's E/P-core architecture, the firmware has to lay out the core clusters in a logical way so the OS can utilize them. And [so far, that's not the case on the O6](https://forum.radxa.com/t/orion-o6-debug-party-invitation/25054/452?u=geerlingguy). The board firmware [doesn't currently](https://forum.radxa.com/t/orion-o6-debug-party-invitation/25054/32?u=geerlingguy) lay out three core clusters, instead it presents 8 cores in two clusters in the SystemReady (9.0.0+) firmware, or 12 cores in _five_ clusters in the Radxa BSP (0.2.x/0.3.x) firmware.

In both situations, the silver lining is the LPDDR5 RAM is pretty performant, giving me speeds into the 40-50 GB/sec range (as measured by `tinymembench`). That's a lot faster than most SBCs, but slower than the latest Arm systems from Apple and Qualcomm.

For $200 to $300, I can accept 'slower than Apple but faster than an SBC'. But I wish there were more consistency in the benchmarks...

{{< figure src="./orion-o6-14w-idle-power-consumption.jpg" alt="14W idle power draw Home Assistant graph Orion O6" width="700" height="394" class="insert-image" >}}

It would also be great if the board could idle at less than 15W (as measured at the wall with an efficient 65W GaN USB-C adapter). That's a lot higher than I expect for mobile-class hardware with LPDDR5 RAM and nothing except a low-power NVMe drive attached!

## A Custom PC

But the one thing the _O6_ can do that Apple, Qualcomm, and Raspberry Pi can't: install directly into a custom PC.

{{< figure src="./radxa-orion-o6-installed-inside-meshroom-itx-case.jpg" alt="Radxa Orion O6 installed inside Meshroom Mini ITX Case" width="700" height="394" class="insert-image" >}}

I installed the board into a mini ITX case, though chose a graphics card (AMD RX 7900 XT) that was a bit too long. Nothing removing one corner of the case—and the front IO assembly—can't fix!

I wanted to see how LLMs would run with a full 20 GB of VRAM, but alas, all the AMD graphics cards I tested in Ubuntu 25.04, from the 7900 to a 7700 and even my older 6700 XT, errored out. For example:

{{< figure src="./orion-o6-pcie-bus-errors-amd-gpu.jpg" alt="AMD GPU errors on Orion O6" width="700" height="394" class="insert-image" >}}

For the time being, I switched tracks and started testing Windows. After all, there's a [full Windows 11 Arm release ISO](https://www.microsoft.com/en-gb/software-download/windows11arm64) available for download now—no more Insider Previews and hacky scripts!

## Windows 11

I just downloaded the arm64 ISO from Microsoft, flashed it to a USB stick with [Rufus](https://rufus.ie/en/), and... for a nice surprise, it just installed with no issues whatsoever (besides the typical 5 or so restarts it takes to get Windows 11 installed...).

There are a few quirks:

  - I had to use a USB Ethernet adapter, since there are very few drivers for Windows on Arm
  - Video output would freeze when I tried using my JetKVM for remote control (this didn't happen under Linux)
  - The system would sometimes get into a weird state where the HDMI output went to 480p, even though Windows was running at 1080p internally. This led to a bit of a 'blurry' user experience! A full power off and unplug/replug cycle was required to get this to reset. Likely the result of some bug between the Cix SoC and the custom DisplayPort to HDMI chip Radxa put on the board.
  - There aren't drivers for... almost _anything_. (See below.)

{{< figure src="./orion-o6-windows-11-device-manager-unknown-device.jpg" alt="Windows Unknown Device Manager Orion O6 Arm" width="700" height="394" class="insert-image" >}}

Outside those quirks (which honestly apply to almost all hardware that runs Windows on Arm currently, like the [Thelio Astra](/blog/2025/system76-built-fastest-windows-arm-pc)), Windows 11 ran surprisingly well. 4K YouTube playback was pretty smooth, even while 30% of the CPU was burned while recording the screen with the Snipping Tool (since my external recorder only got blurred 480p output!).

To round out my Windows experience, I ran Geekbench and Cinebench, and here are those results:

  - Geekbench: [1085 single / 5671 multi](https://browser.geekbench.com/v6/cpu/117273810) (5-10% slower than [Linux](https://browser.geekbench.com/v6/cpu/compare/11703943?baseline=11727381))
  - Cinebench 2024: 52 single / 387 multi

The performance isn't incredible, but it _is_ between a Raspberry Pi 5 and the Qualcomm Snapdragon X. But unlike the _Pi_, this has a full BIOS, so I can install Windows without any hacks. And unlike the _Snapdragon_, I can install _Linux_ without any hacks.[^snapdragon]

{{< figure src="./orion-o6-rtx-a400-gpu.jpg" alt="Nvidia A400 GPU on Orion O6" width="700" height="394" class="insert-image" >}}

I also tested a graphics card in Windows on Arm. I plugged it into the PCIe slot, powered it up, and Windows _does_ recognize the PCIe card. But it does _not_ route any display output through it, nor know what to do with it.

As I said earlier, there are precious few device drivers for Windows on Arm, and while I'm _99% certain_ Nvidia GPU drivers exist for Windows 11 arm64... they definitely aren't public.

## GPUs under Ubuntu 25.04

But you know where GPUs actually _do_ work on Arm? Linux!

I plugged the same Nvidia A400 card in, plugged my monitor into one of it's DisplayPort outputs, and—at least after Ubuntu started loading—I got output!

There were some errors, and the Nouveau driver seemed a little flaky, but once I installed the Nvidia proprietary driver with `sudo ubuntu-drivers install nvidia:570`, it was quite stable.

Gnome and `glmark2` used the card for acceleration, and CUDA support seemed to work fine, but some apps like Firefox didn't seem to pick up on the GPU's presence. Not all applications that run on Arm Linux understand that, like x86, you can have _real PCIe hardware_ like graphics cards on Arm!

But how does AMD do?

The 7900 XT kept giving me errors, so I tried a Pro W7700... which hard-locked the system sometime after displaying the error message `amdgpu 000:c3:00.0: Failed to enable PASID`.

I tried my older RX 6700 XT, and it got much further past that message, but _also_ hard locked the system (killing SSH sessions, freezing my Gnome session), with the messages:

```
...
[   64.943893] [drm] Not enough PCI address space for a large BAR.
[   64.943900] amdgpu 0000:c3:00.0: BAR 0 [mem 0x1800000000-0x180fffffff 64bit pref]: assigned
[   64.943913] amdgpu 0000:c3:00.0: BAR 2 [mem 0x1810000000-0x18101fffff 64bit pref]: assigned
[   64.943927] amdgpu 0000:c3:00.0: amdgpu: VRAM: 12272M 0x0000008000000000 - 0x00000082FEFFFFFF (12272M used)
[   64.943934] amdgpu 0000:c3:00.0: amdgpu: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[   64.943946] [drm] Detected VRAM RAM=12272M, BAR=256M
[   64.943950] [drm] RAM width 192bits GDDR6
[   64.944282] [drm] amdgpu: 12272M of VRAM memory ready
[   64.944290] [drm] amdgpu: 7614M of GTT memory ready.
[   64.944375] [drm] GART: num cpu pages 131072, num gpu pages 131072
[   64.944542] SError Interrupt on CPU0, code 0x00000000be000011 -- SError
[   64.944549] CPU: 0 UID: 0 PID: 2586 Comm: modprobe Kdump: loaded Not tainted 6.14.0-15-generic #15-Ubuntu
[   64.944556] Hardware name: Radxa Computer (Shenzhen) Co., Ltd. Radxa Orion O6/Radxa Orion O6, BIOS 9.0.0 Apr 11 2025
[   64.944560] pstate: 83400009 (Nzcv daif +PAN -UAO +TCO +DIT -SSBS BTYPE=--)
```

Reading through the Radxa forums, it looks like [newer RDNA cards from AMD can have issues](https://forum.radxa.com/t/recommended-external-gpu-for-o6/26898/2?u=geerlingguy), depending on what firmware/BIOS and OS you're running.

Back to Nvidia, I tested my 3080 Ti, and... it actually worked great, with [just a few `arm-smmu-v3`-related errors](https://github.com/geerlingguy/sbc-reviews/issues/62#issuecomment-2852490521).

Before I got to benchmarking LLMs, I noticed one alarming thing: when I shut down the system, the fans on the card went full blast. Apparently there's a bug in the BIOS that doesn't fully power off cards in the slot. Luckily my EVGA card goes into a failsafe mode where the fans ramp up so it doesn't overheat. But some cards [might not](https://forum.radxa.com/t/warning-nearly-cooked-my-amd-pro-while-the-orion-was-turned-off/25948/13?u=geerlingguy). Hopefully that gets fixed soon.

But after booting it back up, I tried out some Large Language Models, like Llama and DeepSeek. All the results are available in [this GitHub issue](https://github.com/geerlingguy/ollama-benchmark/issues/13). But just comparing running a model on the 12-core CPU versus a 3080 Ti, there's an obvious winner:

{{< figure src="./orion-o6-deepseek-r1-14b.jpg" alt="CIX CPU SoC vs Nvidia 3080 Ti Deepseek Inference" width="700" height="394" class="insert-image" >}}

Never mind the fact the SoC burned 32W, while the 3080 Ti burned _465W_!

If you're just doing AI stuff or GPU compute, this board might actually be a decent option, all things considered. It's definitely easier to get going than my [Raspberry Pi GPU-accelerated LLM setup](/blog/2024/llms-accelerated-egpu-on-raspberry-pi-5)—though in a funny reversal, the Pi works with AMD but _not_ Nvidia!

But outside of running LLMs, there are still quirks:

Like other Arm systems, most graphics cards don't display the BIOS screen; you have to be plugged into the motherboard HDMI connector for that.

And for gaming, I got the open source Doom 3 demo running _very_ smoothly thanks to [Pi-Apps](https://pi-apps.io). I couldn't uncap the frame limit, but it was definitely using the GPU, and running a little smoother than I could get it on my Pi, especially with loading times. And, bonus: the sound output works through HDMI! That's not always guaranteed with drivers on Arm.

I haven't had time to run other games yet; since [Steam doesn't install on a 64-bit-only board](https://steamcommunity.com/discussions/forum/10/4030223299341307854/#c601892123632008898) like this, it's a little more annoying getting my full gaming stack set up.

## Conclusion

The bottom line, a couple months post launch: it feels like everyone who's bought one of these boards is part of some extended beta. And that stinks, because this hardware at just over $200 for the base model is a _pretty decent_ value.

It's not perfect, and I'd love to have at least socketed RAM. But it's the best Arm ITX motherboard on the market today. But let's be honest, it's almost the _only_ Arm ITX board on the market today.

Apparently [Cix is working on upstream Linux support](https://patchwork.kernel.org/project/linux-arm-kernel/cover/20250220084020.628704-1-peter.chen@cixtech.com/), [OpenBSD already added support](https://www.openbsd.org/arm64.html), and there's a lot of effort around stabilizing the firmware issues.

But Radxa's played this game before. They're a hardware company first. Their firmware is often a day late and a dollar short. They're better than some other SBC makers, sure. But I've said often: _software_ and _user experience_ are what attracts mainstream buyers.

Right now the firmware that runs this board—it's just not there. I think it _could_ be, and maybe for a few use cases it already is... But for _most_ people, while it's fun building your own little Arm desktop PC, especially with a board that's only a few hundred bucks... I have to say, hold off for now.

If there's another new firmware that fixes all the problems I've encountered, I'll re-test it. But I've already done two full test cycles: and you know what they say: fool me once, shame on you. Fool me twice...

## Tariffs at the 11th hour

Literally _yesterday_, after months spent testing the 16GB board I was provided, and many _more_ months waiting on my AI kit to ship, I received an email from ARACE about my order:

> Due to high customs duties, our DHL and Fedex service providers have suspended shipping services to the US. 
> 
> Currently, we can only offer shipping to the U.S. through the 4PX logistics channel, but prepayment of taxes is required. 

Welp. I went to re-order the board, and realized instead of paying around $330 plus $85 shipping, I'd have to pay around $330 **plus _$1,100_ shipping**, because of the tariffs that took effect this month!

{{< figure src="./orion-o6-arace-shop-1500-tariff.jpg" alt="Orion O6 1500 USD after tariff applied" width="700" height="394" class="insert-image" >}}

That's a bit too much. At $200-300, the board is not a steal, but it's a decent value if the functionality that you need works already. At $500+ (much less _$1,500_), it's just not going to happen. So if you're in the US, definitely hold off buying this board. It's certainly not worth the same price as a fully-featured _enterprise-grade_ [64-core Ampere motherboard + CPU combo](https://www.newegg.com/asrock-rack-altrad8ud-1l2t-q64-22-ampere-altra-max-ampere-altra-processors/p/N82E16813140134?Item=N82E16813140134).

[^snapdragon]: Yes I know some Snapdragon laptops have the ability to install Linux _kind-of_ easily... but it's not universal, and I'd still call that setup a 'hack' as it's not directly supported by Qualcomm. It's annoying, because Linaro's done a ton of work on Linux support for Snapdragon!
