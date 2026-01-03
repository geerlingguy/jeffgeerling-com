---
nid: 3297
title: "Ampere Altra Max - Windows, GPUs, and Gaming"
slug: "ampere-altra-max-windows-gpus-and-gaming"
date: 2023-07-03T13:59:24+00:00
drupal:
  nid: 3297
  path: /blog/2023/ampere-altra-max-windows-gpus-and-gaming
  body_format: markdown
  redirects: []
tags:
  - altra
  - ampere
  - arm
  - gaming
  - nvidia
  - video
  - windows
  - youtube
---

{{< figure src="./ampere-altra-dev-workstation-platform.jpg" alt="Ampere Altra Developer Platform Workstation" width="700" height="394" class="insert-image" >}}

I'm testing [Adlink's Ampere Altra Developer Platform](https://www.ipi.wiki/pages/ampere-altra-developer-platform). This machine has a 96-core Arm CPU, but now they sell a 128-core version. Apple also recently released the [M2 Ultra Mac Pro](https://www.apple.com/mac-pro/), so the model I'm testing isn't the "fastest in the world" like I could boast a couple months ago... but it's close, and I actually _doubled_ my performance from last time—I'll show how later.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/ydGdHjIncbk" frameborder='0' allowfullscreen></iframe></div>
</div>

Disclaimer: I was not sponsored by Adlink or Ampere, and they had no input into this article or the above video. However, they did supply the system used for testing.

## Windows Support

Let's start with Windows. It works now! A [firmware upgrade](https://www.ipi.wiki/pages/download-ava-developer-platform) was all it took to get Windows 11 Pro installed: and this isn't some janky hacked-together version, this is the standard Windows on Arm installer you download from Microsoft directly—well, sorta... I'll get to that.

But I installed Windows, ran Cinebench, installed a driver for the built-in GPU, and I know what some people are already asking:

_Can it run Crysis?_

Of _course_! It runs Steam just fine, and I got Crysis and a few other games installed. And Crysis runs, just it runs a bit slow.

{{< figure src="./crysis-on-ampere-altra-max.jpg" alt="Crysis Remastered running on Ampere Altra Max" width="700" height="394" class="insert-image" >}}

...well, maybe that's an understatement. "Runs" is being generous, as it got only a frame per second. But the fact this non-X86 hardware even loads it at all playable—with no GPU under Windows on Arm—is a significant achievement.

I tried out other stuff, too.

I downloaded Adobe Creative Cloud, signed in, installed Photoshop, and did some of my normal RAW editing workflow, and... it was actually _fast_. Fast enough I didn't feel hampered by it.

I tried running [PugetBench](https://www.pugetsystems.com/labs/articles/PugetBench-for-Adobe-Creative-Cloud-1642/), but this is where you start seeing the cracks in Microsoft's approach to Arm. Creative Cloud, which admittedly isn't what I'd call _good_ software, seems to have bugs with managing plugins under Windows on Arm.

Their translation layer isn't perfect. Unlike Apple's Rosetta 2, it's a bit slower, has no hardware-assist, and can't achieve the same compatibility Apple does on M-series CPUs.

And drivers? Well, drivers for Arm on _Linux_ are in a good place—we'll get to that shortly.

But drivers for Arm on Windows? That's a different story.

Let's start with installing Windows.

## Windows 11 Installation

At this point, there are a few other Arm Windows desktops—Microsoft even _makes_ one, the Windows Dev Kit 2023, their 'Project Volterra' [I previously covered](/blog/2022/testing-microsofts-windows-dev-kit-2023). There's also the Surface and a few Windows on Arm laptops.

So why doesn't Microsoft have an easily downloadable Arm image for Windows? Not sure.

{{< figure src="./uupdump-image-arm64.jpg" alt="UUPDump AARCH64" width="700" height="394" class="insert-image" >}}

I had to go to [UUPdump.net](https://uupdump.net), download an arm64 Windows 11 Insider Preview build, use a Windows PC to flash that to a USB drive using Rufus, and _then_ I had my installer ready.

Ampere [has their own guide](https://github.com/AmpereComputing/Windows-11-On-Ampere) for this process, because you can't find Arm64 Windows at all on Microsoft's website. The Windows Installation Media tool doesn't support Arm, and the [Windows 11 Download Page](https://www.microsoft.com/en-us/software-download/windows11/) only shows x64 ISOs (as of July 2023).

Anyway, I created an installer and plugged it in. Last video it would just crash during boot, but since then, Adlink released version 10 of the firmware with a UEFI bugfix, and now Windows can install just like any other PC.

And just like on any other install, I had to jump through Microsoft's hoops to [set up Windows with a local account](https://www.windowscentral.com/how-set-windows-11-without-microsoft-account).

But now I have a Windows 11 install running native on this thing! The graphics were a bit wonky, but I got in contact with the Adlink team, and they passed along an early ASPEED driver, which got me going at 1080p at 60 Hz. ASPEED is working on getting their driver certified, so hopefully it will be public soon!

{{< figure src="./aspeed-chip-on-motherboard.jpg" alt="ASPEED AST2500 in Ampere Altra Dev Platform" width="700" height="394" class="insert-image" >}}

This little ASPEED chip isn't gonna burn rubber in the latest racing game, but it can render Windows at 60 Hertz just fine.

Running apps like Firefox is a pleasure on the Ampere Altra Max—it has a completely native Arm build for Windows, so it's quite snappy. Unlike the desktop experience on Single Board Computers, this thing can play YouTube in 4K all day, with no dropped frames. (If you use SBCs a lot, you'll know that is somewhat of an accomplishment.)

But how about other software?

One problem that's not specific to this hardware is there are _very few_ things optimized for Arm on Windows. It's a chicken and egg problem.

But even something that's not well optimized can be passable if you just throw a hundred CPU cores at it!

Like Cinebench—it's actually one of the worst scenarios, because the code in Cinebench is optimized completely for X86, not Arm. But even with emulation, the 96 cores gave a Cinebench score just over 6000.

{{< figure src="./cinebench-r23-ampere-altra-max.jpg" alt="Cinebench R23 Ampere Altra Max Windows on Arm" width="700" height="394" class="insert-image" >}}

That's... about on par with a 10th gen Intel CPU, but it's running under emulation. While running these tests, I ran into a strange issue you'll only see with high-end workstation or server CPUs on Windows.

## Windows and Multicore

Windows apps—and even Windows itself—traditionally didn't know what to do with more than, say, 32 cores. In fact, [until recently in Windows 10](https://www.anandtech.com/show/15483/amd-threadripper-3990x-review/3), you had to buy special Enterprise Windows editions just to _address_ more than 60 cores on your CPU!

But that assumption in Windows means many apps don't scale beyond a few dozen cores. By default, Cinebench only used 60 cores. I had to go into the BIOS and change the CPU core `ANC` mode from `Monolithic` to `Quadrant` to get all 96 cores in use.

The default Monolithic mode worked great in Linux, but Windows would only ever show apps 60 CPU cores.

But when changing to Quadrant, even though Windows started allocating tasks to all 96 cores, I could sometimes get _higher_ scores on Monolithic only hitting 60 cores than with Quadrant running on all 96!

Why's that? Well, this is party speculation, but the different modes make CPU caches work a little differently. With so many little CPU cores, the processor's built-in L2 and L3 caches are routed differently. With hyper-focused software like Cinebench... my best guess is some routines that are optimized for X86 kinda blow up on Arm. So the problem could get worse if you go full steam on all the cores!

## Steam on Windows

Steam must've updated recently, because the first time I was testing it in April, I had some UI issues, but those are gone now. It loads and lets me install and run games just fine.

But not all games work. In fact, most of the older games I tried had issues, like Star Wars Pod Racer tried installing 32-bit DirectX, but then it would just die and not start.

{{< figure src="./steam-quake-3-arena-windows.jpg" alt="Steam Quake III Arena on Windows on Arm OpenGL issue" width="700" height="394" class="insert-image" >}}

Quake 3 Arena would open, but then the console would pop up warning OpenGL couldn't load.

Some of this might be down to running on Arm, other things because Arm graphics drivers in Windows barely exist, but in either case, many apps and games won't work yet—or might never.

But one app that _should_ work, but I've had trouble, with is Geekbench.

Geekbench 6 actually [gave a result](https://browser.geekbench.com/v6/cpu/1590435), but while I was monitoring CPU cores, it seemed like most of the multicore tests would only hit 60 cores at a time.

I could even see that just by power usage. During Geekbench runs, I never saw more than about 170W of power use, even though during Linux benchmarking it would get up past 220W.

On the Linux side, all 96 cores worked, so it might be just Windows libraries that aren't expecting so many cores. Again, not sure.

I [opened a support request](http://support.primatelabs.com/discussions/geekbench/82502-geekbench-6-doesnt-install-correctly-under-windows-on-arm-on-ampere) with Geekbench to try to figure out the problem.

Jumping over from games to general 3D graphics, the Heaven benchmark won't run at all because DirectX 11 couldn't find a GPU. Which is fair, since the little ASPEED chip doesn't do 3D graphics at all.

But anything that relies on 3D rendering won't work until graphics cards are supported for Windows on Arm. And I don't see any timeline for that yet.

Qualcomm probably likes it that way, because right now the only way to really get 3D acceleration on Windows on Arm is with _their_ chips.

For general Windows productivity, like web browsing and even photo editing in Photoshop, this thing could be my daily driver, no problem.

I just hope Microsoft keeps investing in Windows on Arm, and convinces the rest of the world it actually _matters_. There are a lot of device drivers that just won't work in Windows, including the basic Intel gigabit Ethernet driver. I had to use [an external USB adapter](https://amzn.to/44uIU26) because that's actually supported for Windows on Arm laptops and tablets.

But let's switch back to Linux.

## RAM Upgrade from 64 GB to 96 GB (4 to 6 sticks)

For this round of testing, I upgraded the system from four sticks of 16 GB ECC RAM to 6 sticks, meaning I went from 64 to 96 GB of RAM.

You wouldn't think it, but that actually made a _huge_ difference in performance. I got about 400 Gigaflops with 64 gigs, and _600_ with 96. And Geekbench went from [30,000](https://browser.geekbench.com/v5/cpu/21070727) to almost [_36,000_](https://browser.geekbench.com/v5/cpu/21323770)!

Power usage jumped up a bit too. I actually did a double-take, and had to test out both my Kill-A-Watt and this Sonoff S31 adapter, but both were within 1W of each other. With four sticks of RAM, I was seeing about 200W of power draw under load.

{{< figure src="./235w-power-usage-ampere-altra-max-6-sticks-ram.jpg" alt="Ampere Altra Max Developer Platform using 235W of power" width="700" height="394" class="insert-image" >}}

Putting in two more sticks and changing _nothing else_, the system used 235W.

That's a 35-watt difference! A stick of DDR ECC RAM uses maybe 5 or 6 watts, so two should just add 10-15W max. Where's the other 15W coming from?

Well, the Ampere Altra Max CPU has 8 memory channels. And the COM-HPC carrier where the CPU _sits_ has 6 memory slots. Each memory slot goes to a single channel.

{{< figure src="./ampere-altra-max-com-hpc-6-ram.jpg" alt="Ampere Altra Max COM-HPC with 6 sticks of DDR4 ECC RAM" width="700" height="394" class="insert-image" >}}

The more channels you fill, the faster the CPU can access memory across all cores. And what I'm guessing is happening is the CPU is activating more memory channels, thus consuming more power. With great power comes... a lot more performance in this case.

And in this case, I could even eke out _more_ gigaflops—in my case 985 of them—by using an Ampere-optimized math library instead of compiling a more generic one.

I followed [these directions](https://github.com/geerlingguy/top500-benchmark/issues/10#issuecomment-1593386630) to install a special library to use with Linpack, and doing that, I could get [985 Gigaflops using 270W of wall power](https://github.com/geerlingguy/top500-benchmark/issues/10#issuecomment-1593386630).

That means the performance _efficiency_ for this machine went from 2 to 3.64 Gflops per watt, which is nearly as efficient as my Apple M1 Max Mac Studio. Not bad.

Idle power consumption is a lot higher, though; 3.1W when powered off (due to the IPMI functionality), and 70-90W running idle, depending on whether I had a graphics card installed.

## Nvidia Graphics Card support

Windows on Arm has zero support for graphics cards yet, but in Linux, support is already good and getting better.

{{< figure src="./nvidia-3080-ti-graphics-card-installed.jpg" alt="Nvidia 3080 Ti graphics card installed inside Ampere Altra Dev Platform" width="700" height="394" class="insert-image" >}}

I tested my 3080 Ti extensively under Ubuntu, and I can also confirm a 4090 _just barely_ fits in this system, but because the power supply isn't quite a thousand watts, I didn't wanna risk overloading it. So 3080 it is.

Just like installing Windows, [Ampere has a whole guide](https://github.com/AmpereComputing/NVIDIA-GPU-Accelerated-Linux-Desktop-on-Ampere) for how to install Nvidia's graphics card drivers on Linux, and it worked well for me.

I didn't even have to recompile the Linux kernel! I just installed the Arm drivers from Nvidia's website.

And with a graphics card speeding things up, now I can get over 100 fps in SuperTuxCart on max settings. I also ran glmark2, and I could get a score of just under 10,000.

{{< figure src="./dhewm-3-ampere-altra-max.jpg" alt="Dhewm 3 Doom 3 running on Ampere Altra Max Developer Platform" width="700" height="394" class="insert-image" >}}

Then I followed Ampere's instructions to install Doom 3—or, well, [Dhewm 3](https://dhewm3.org), the open source version. And running _that_, I was getting a perfect 60 fps the whole time. I could probably get a lot more, but for some reason it was locked to the monitor refresh rate. And when I tried running the built-in benchmark, it segfaulted and crashed.

So then I installed Openarena, which is a little older, but based on a similar engine. On an overclocked Raspberry Pi 4, I could get 90 fps. On this machine, it maxed out the engine at 1000 fps! But it's more stable locked at a lower framerate, something more reasonable like 500 fps.

It's a silly example, but it just shows how modern GPUs can run even older games just fine, as long as you have the driver support (which is missing in Windows).

But speaking of Windows, Steam ran just fine there. In Ubuntu, I couldn't get it to launch at all. I got an 'exec format error', which means Linux tried launching Steam but kinda blew up because Steam is only compiled for X86 on Linux.

And since Linux doesn't have an X86 translation layer like Rosetta 2 or Microsoft's WOW64 engine, Steam won't launch at all.

I tried launching the Heaven benchmark too, but the same thing happened.

I won't hold my breath for Valve or other 3D graphics companies to support Arm natively, but that doesn't mean a fast GPU isn't useful on Arm already.

Machine learning apps like Stable Diffusion and LLaMA run just fine on here, though I completely screwed up my CUDA install, to the point I had to reinstall Ubuntu just to get my drivers working again.

## Other GPU Topics

There's a lot to look forward to here, though. Microsoft showed off the [Unity engine running natively](https://twitter.com/windowsdev/status/1661542171156127753) on Windows on Arm recently, and Arm showed off a bunch of game-related developments [at Mobile World Congress 23](https://twitter.com/GioKinto/status/1630143845353545728?s=20).

And what about AMD GPUs? It looks like they'll actually work too, but right now it does require a [kernel patch](https://community.amperecomputing.com/t/amd-gpus-on-the-altra-devkit-and-other-altras-patches-available-now/336/3), since the AMD drivers still run into cache coherency issues on Arm.

That's one of the problems I ran into on the Raspberry Pi as well, though the Ampere's PCI Express bus—all 128 lanes of PCIe Gen 4—is a lot more robust than the single Gen 2 lane on the Pi!

## Conclusion

{{< figure src="./ampere-altra-max-m128-28.jpeg" alt="Ampere Altra Max M128-28 CPU" width="700" height="394" class="insert-image" >}}

So where do we go from here? _Obviously_ we go faster!

[Subscribe over on YouTube](https://www.youtube.com/c/JeffGeerling), because on a livestream I'll be upgrading my machine from 96 to 128 cores, and I'll see if I can surpass 1 Tflop on the CPU!
