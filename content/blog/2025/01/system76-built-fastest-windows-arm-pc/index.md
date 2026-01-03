---
nid: 3431
title: "System76 built the fastest Windows Arm PC"
slug: "system76-built-fastest-windows-arm-pc"
date: 2025-01-03T15:02:15+00:00
drupal:
  nid: 3431
  path: /blog/2025/system76-built-fastest-windows-arm-pc
  body_format: markdown
  redirects:
    - /blog/2025/system76-accidentally-built-worlds-fastest-windows-arm-pc
    - /blog/2025/system76-built-worlds-fastest-windows-arm-pc
aliases:
  - /blog/2025/system76-accidentally-built-worlds-fastest-windows-arm-pc
  - /blog/2025/system76-built-worlds-fastest-windows-arm-pc
tags:
  - altra
  - ampere
  - arm
  - cpu
  - reviews
  - system76
  - video
  - youtube
---

System76 built their first workstation-class Arm PC, the [Thelio Astra](https://system76.com/desktops/thelio-astra-a1-n1/configure), and it's marketed for [streamlined autonomous vehicle development](https://system76.com/autonomous-vehicles).

{{< figure src="./system76-thelio-astra-hero.jpeg" alt="System76 Thelio Astra - Hero with Launch Keyboard" width="700" height="auto" class="insert-image" >}}

But I'm not an automotive developer, just someone who enjoys Linux, Arm, and computing. So I was excited to spend a few weeks (which turned into a few _months_) testing the latest Ampere-based computer to come to market.

I initially ran my [gauntlet of tests](https://github.com/geerlingguy/sbc-reviews/issues/53) under Ubuntu 24.04 (the OS this workstation ships with), but after discovering System76 dropped in ASRock Rack's [TPM 2.0 module](https://www.newegg.com/asrock-rack-tpm-spi/p/N82E16816775069), I switched tracks and installed Windows 11—which went without a hitch!

With that, I spent some time comparing this workstation to the current 'best of breed' Windows on Arm PC, the models based on Snapdragon's X Elite chips. And this thing _wipes the floor_.

## Hardware - Ampere Altra (Max)

But before we get into Linux, Windows, benchmark results, and why I'm not running Pop!_OS, we should discuss the hardware.

{{< figure src="./system76-thelio-astra-rear.jpg" alt="System76 Thelio Astra - Rear" width="700" height="auto" class="insert-image" >}}

The base model costs $3,299—which is in line with most x86 workstation-class PCs, at least in the Threadripper and Xeon W range. That'll get you a 64-core CPU, 64GB of ECC RAM, 500 GB of NVMe storage, an Nvidia RTX A400 Workstation GPU, and dual 10 GbE Ethernet.

But the configuration System76 sent me for review had some upgrades:

  - Ampere Altra Max M128-30 CPU (128 Neoverse N1 CPU cores at 3.00 GHz)
  - 512 GB ECC DDR4 RAM
  - 1TB NVMe SSD
  - Dual 25 GbE Ethernet (on-motherboard, Broadcom NIC)
  - ASRock Rack TPM 2.0 module

This upgraded configuration costs around $7,000—which is the _starting price_ of an M2 Ultra Mac Pro workstation.

Note that you can buy every part of this system—aside from System76's case and support—from a retailer like NewEgg (e.g. [the motherboard + CPU combo](https://www.newegg.com/asrock-rack-altrad8ud-1l2t-q64-22-ampere-altra-max-ampere-altra-processors/p/N82E16813140135) for $2349) should you wish to build a custom arm64 workstation PC.

Everything is built into System76's Thelio case, which is very solid sheet metal with a design similar to the Mac Pro, where the entire shell slides over the top, revealing the chassis within:

{{< figure src="./system76-thelio-astra-inside-cooling.jpg" alt="System76 Thelio Astra - Open Inside Cooling Zones" width="700" height="auto" class="insert-image" >}}

There are three distinct cooling zones—and despite having no mesh or holes in the front (it's a solid facade), there is enough airflow for HEDT-class performance. The top contains a custom metal shroud to guide airflow through the [Arctic Freezer 4U-M CPU cooler](https://amzn.to/3WrVQ7l), directing it's airflow over the RAM and motherboard power regulators to an exhaust fan in the back.

The middle section has a wide metal fan bracket which provides a ton of intake for GPUs and other PCIe devices.

The bottom has an additional 140mm intake fan to pull air up to the GPU area and motherboard, as well as the power supply, drawing air from the bottom.

The result is an elegant, if heavy, case, that maximizes airflow while keeping the system _very_ quiet. During long HPL and Cinebench runs, the noise only rose to a low 40 dB range, and with 140mm and 120mm fans, the sound was not unpleasant.

The default fan curve keeps the CPU down to around 60°C fully loaded, so there's even wiggle room if you wanted to adjust it. It should be noted my initial review unit had a bug in the BIOS which resulted in the fan curve not being applied—so my first tests were literally cooking the CPU to thermal limits!

I saw it hit 99°C a few times, with the CPU pulling 250W, and entire system power draw at 450W, then the system would hard lock up until I pulled power!

Luckily, a firmware update fixed that issue universally, and the proper installation of a `system76` background daemon allowed me to tweak things further.

There are three aspects of the case design I do _not_ like, however:

  1. The custom case design includes screwless PCIe slot covers—however, these covers are a bit loose, and besides rattling when transporting the computer, they are prone to popping out whenever you loosen the retention bracket that holds PCIe cards in place. Which is highly annoying when adding or replacing cards in the 4 x16 card slots!
  2. There is no front IO with the current Astra design—and only four USB 3.2 Gen 1 Type-A ports on the rear. So in my use, I needed a USB hub (the first time I've had to use one in a while!). It would be nice to have some front panel IO, even if only one or two USB-C ports.
  3. Unlike the Mac Pro, this case has no handles, and the front edge is flush with the surface it's resting on. This can make picking it up, moving it around, and removing the top case a little awkward. It's not a huge deal, but I _do_ love Apple's case design in that regard, considering you might want to put one of these on wheels and move it around a bit.

## Linux (and no Pop!_OS... yet)

The primary reason someone would buy this thing is for automotive development. Since most cars and infotainment systems run on Arm chips, building software with an Arm workstation makes sense—it's a lot faster compiling Arm software and running tests on it natively on a monster Arm CPU than even the fastest AMD or Intel CPU with emulation.

The nice thing about System76 selling this machine is you get their excellent support (you can choose from 1-3 years of support at purchase). This is a huge boon to businesses who elect to run open source software, because they get a fully-supported hardware configuration instead of having to figure out compatibility themselves.

And System76 builds Pop!_OS (and a new COSMIC desktop environment), which is meant to ease the adoption of Linux for desktop use... unfortunately, Pop!_OS is not yet fully supported on arm64.

In lieu of that, System76 is shipping Ubuntu 24.04 (or 22.04, your choice), which has great support for Ampere CPUs already, and in my experience, is the easiest Linux distribution to run when working on various hardware configurations. Arm64 driver compatibility is excellent with most anything made in the last 5-10 years, including graphics cards from AMD and Nvidia!

## Performance

To see _all_ my benchmark data, see my [GitHub issue on the Thelio Astra](https://github.com/geerlingguy/sbc-reviews/issues/53). But here are a few selected benchmarks I'd like to highlight:

{{< figure src="./system76-thelio-astra-benchmark-hpl.png" alt="System76 Thelio Astra - HPL Benchmark Results" width="700" height="auto" class="insert-image" >}}

Besides the 192-core AmpereOne, which [I reviewed late last year](/blog/2024/ampereone-cores-are-new-mhz), no other Arm machine comes close to the overall performance of Ampere's Altra Max—at least as far as multi-core is concerned.

Single-core, the Neoverse N1 cores are getting long in the tooth, but still faster than any of the common SBC cores (like the A76 and A78).

But multi-core, the Thelio Astra takes advantage of all eight DDR4 memory channels available on an Ampere Altra Max CPU, and propels it past the previous champ, the [Adlink Dev Workstation](/blog/2023/testing-96-core-ampere-altra-developer-platform). That machine was limited to 6 memory channels, though it _did_ have a bit more panache, courtesy of built-in RGB fans :)

{{< figure src="./system76-thelio-astra-benchmark-linux.png" alt="System76 Thelio Astra - Linux Timed Compile Benchmark Results" width="700" height="auto" class="insert-image" >}}

I benchmarked a number of things with Phoronix Test Suite, and above are some results for the timed Linux compilation benchmark. This machine obviously scores worse than the AmpereOne, but I left in the fastest current Arm SBC I own (an Orange Pi 5 Max), to show the massive difference you get with 128 cores and enough high-speed memory to feed them.

Eagle-eyed readers will note I have not shown any Threadripper or EPYC results, nor anything x86 at all! That's because core-for-core, x86 dominates on many, if not most, benchmarks, especially current-generation core designs like Zen 5. The Ampere Altra is now 5 years old, and though it still has some fight in it, it can't keep up with 'the big boys'.

That is, unless we _change the rules of the game_...

## Windows on Arm and a Cinebench 2024 WR

{{< figure src="./system76-thelio-astra-benchmark-cinebench.png" alt="System76 Thelio Astra - Cinebench 2024 Benchmark Results" width="700" height="auto" class="insert-image" >}}

Being the fastest Arm PC means it _of course_ obliterates the fastest Mac Pro money can buy—to say nothing of the puny Snapdragon X Elite I tested in the very-short-lived Dev Kit last year.

But this system is _also_ unofficially the fastest 128-core system on the planet, running Cinebench 2024. At least [according to HWBot.org](https://hwbot.org/benchmark/cinebench_-_2024/rankings?cores=128&hardwareType=cpu).

I've been [attempting to submit a result of `5003 cb`](https://community.hwbot.org/topic/40155-please-add-other-hardware-thread/page/40/#findComment-684073), but am stymied by a technicality: The Ampere Altra Max is apparently too exotic to exist in most Windows PC hardware databases, so submissions aren't able to be made!

I've been in contact with the authors of CPU-Z, and am hopeful we can get more results for high-end Arm chips into HWBot soon. We'll see!

It is a bit difficult to overclock these chips, but I _can_ coax a little more performance out of them by cooling them better. I was able to increase the score consistently by 2-3% running the fans at 100%... one wonders if more gains could be had!

But I'm burying the lede—full Windows 11 is running on this machine. And not like "spend 6 hours patching things together to get Windows running", but _download ISO, plug in USB stick, and install_.

It's been possible to install Windows on Arm to earlier Ampere Altra systems, but a [rather annoying process involving UUP Dump was required](https://github.com/AmpereComputing/Windows-11-On-Ampere). Now that Microsoft is _finally_ publishing a [Windows 11 arm64 ISO](https://www.microsoft.com/en-us/software-download/windows11arm64), [the process has become much easier](https://github.com/AmpereComputing/Windows-11-On-Ampere/issues/6).

And x86 software that runs in Windows' emulation mode is still limited to using only 64 CPU cores, but native arm64 versions can address all 128 cores on the Ampere Altra Max. Cinebench 2024 had a bug where it would still only address 64 cores on the Arm version, but that has since been fixed:

{{< figure src="./system76-thelio-astra-cinebench-all-core.jpg" alt="System76 Thelio Astra - Cinebench 2024 multi 128 core task manager" width="700" height="auto" class="insert-image" >}}

## Productivity

If Windows can run, what about the vast library of software Microsoft's been touting as native on Arm, like on their new AI Copilot+ PCs?

Well, I loaded up a number of apps, and Photoshop worked great right away:

{{< figure src="./system76-thelio-astra-windows-photoshop.jpg" alt="System76 Thelio Astra - Photoshop running on Windows" width="700" height="auto" class="insert-image" >}}

Everything ran well, including new AI features like generative AI fill, AI-assisted remove and background isolation tools, etc. It was smooth enough I couldn't really tell a difference from working on my M1 Max Mac Studio (where I normally do work on YouTube thumbnails and graphics for videos).

But I quickly ran into issues launching other applications...

{{< figure src="./system76-thelio-astra-windows-arm-davinci-opengl.jpg" alt="System76 Thelio Astra - OpenGL not found in Davinci Resolve" width="700" height="auto" class="insert-image" >}}

The problem is, any app that requires GPU support or OpenGL has trouble, because even though _from what I've heard_ Nvidia has working Arm drivers for Windows... none have been released publicly. So no matter what GPU you try, you can't get any kind of graphics acceleration working in Windows.

ASPEED's little BMC chip has a built-in VGA controller, and they even have a Windows Arm driver for it... but despite its best effort, it has no 3D graphics rendering capabilities or GPU compute!

In the video embedded later, I also demonstrated running Minecraft and Crysis Remastered in Windows, but both rely on CPU rendering, which is... just not ideal at all. You could play both games if you enjoy powerpoint-presentation-style gameplay.

## Linux Gaming with Steam, Proton, and Box86

Luckily, switching back to Linux solves that issue. Games not only run with 3D acceleration, they run _smoothly_.

Crysis Remastered rendered out smoothly in 'Can It Run Crysis?' mode, Halo 3 ran just as smooth as an Xbox 360, and Doom Eternal—with Ray Tracing enabled—ran well enough to be playable, though the older workstation A4000 GPU I was testing it with is _not_ meant for gaming by any stretch.

{{< figure src="./system76-thelio-astra-doom-eternal-gpu-steam.jpg" alt="System76 Thelio Astra - Doom Eternal on Steam with Proton and Box86" width="700" height="auto" class="insert-image" >}}

This is _not_ a gaming machine. But I was able to install Box86/Box64 and Steam using [Pi-Apps](https://pi-apps.io) (it's literally one click to get Steam installed!), and then I could play a number of games; almost anything that runs through Proton can play on arm64 nowadays, and [Box32 is now trying to fill the gap](https://box86.org/2024/12/new-version-of-box64-v0-3-2-and-box86-v0-3-8/) with more modern Linux distros which are dropping support for 32-bit packages!

## Quirks and Downsides

To paint a complete picture of the experience running System76's first arm64 desktop, I also have to run through some of the quirks inherent to the hardware design, and to running Ampere's silicon:

  - Video card support for arm64 is still not perfect; `nouveau` _really_ has issues, depending on kernel version and card, and even Nvidia's proprietary drivers can cause weird issues, like a blank screen with just a mouse cursor, or an invisible second display, and debugging these problems can become challenging, since the ASPEED BMC also supplies a built-in VGA display... which can sometimes confuse both Windows and Linux when you're sorting out driver issues!
  - AMD GPUs have a text artifacting bug that requires a patch to the `amdgpu` driver to fix. It didn't seem to break my experience using the machine, but it's just another quirk to deal with on arm64.
  - There are still very few people running arm64 in a 'professional' manner like through this workstation. So you often have to convince people that _yes_, you're using arm64, but _no_, you're not dealing with a puny SBC like a Raspberry Pi. It leads to some interesting support tickets, though, especially for Windows devs who were led to believe Snapdragon is the penultimate Windows on Arm processor :)

## Video and more

If this blog post wasn't enough, I have a full video where I go even more in depth, and give a better idea of how well games and applications run under both Linux and Windows. I also go into more detail on my GPU upgrades and some of the random bugs I ran into (and how I resolved them with System76's help). You can watch it here:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/AshDjtlV6go" frameborder='0' allowfullscreen></iframe></div>
</div>

Thank you to System76 and Ampere for providing the hardware and supporting my three months of testing, leading up to this review. And thank you to Micro Center for providing two workstation graphics cards for more testing.

System76 also recently sent over an Nvidia RTX 4080 Super, and I will be installing that and trying to resolve some lingering issues with Blender and Steam.

My biggest takeaway: _Microsoft is missing out on a lotta fun._ They need to convince their hardware partners to start supporting Arm64, if they want any chance at catching up to Linux for arm64.

If you're interested in the Thelio Astra, you can [configure and buy one on System76's website](https://system76.com/desktops/thelio-astra-a1-n1/configure).

## If you made it this far...

If you like the idea of me writing these ad, cookie, and tracking-free blog posts... would you consider sponsoring my work on [Patreon](https://www.patreon.com/geerlingguy) or [GitHub](https://github.com/sponsors/geerlingguy)?
