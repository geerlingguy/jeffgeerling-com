---
nid: 3399
title: "Radxa X4 SBC Unites Intel N100 and Raspberry Pi RP2040"
slug: "radxa-x4-sbc-unites-intel-n100-and-raspberry-pi-rp2040"
date: 2024-08-17T15:22:30+00:00
drupal:
  nid: 3399
  path: /blog/2024/radxa-x4-sbc-unites-intel-n100-and-raspberry-pi-rp2040
  body_format: markdown
  redirects: []
tags:
  - intel
  - linux
  - n100
  - radxa
  - raspberry pi
  - sbc
  - video
  - youtube
---

At first glance, especially from the top, the [Radxa X4](https://radxa.com/products/x/x4/) is your typical Arm SBC:

{{< figure src="./radxa-x4-top.jpeg" alt="Radxa X4 Top" width="700" height="auto" class="insert-image" >}}

But you'll quickly notice the lack of an SoC—that's on the bottom. Looking more closely, what's a Raspberry Pi chip doing on top?! First, let's flip over the board to investigate. There's the SoC: definitely not Arm inside, this thing's an Intel N100:

{{< figure src="./radxa-x4-bottom.jpeg" alt="Radxa X4 Bottom - Intel N100 SoC" width="700" height="auto" class="insert-image" >}}

I have all my benchmarks and notes bringing up this board stored in my sbc-reviews GitHub repository: [Radxa X4 - geerlingguy's sbc-reviews](https://github.com/geerlingguy/sbc-reviews/issues/48), and I also summarized everything in a [video on YouTube](https://www.youtube.com/watch?v=F2atAHDOaIA), which you can watch inline (or skip past and read this blog post instead):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/F2atAHDOaIA" frameborder='0' allowfullscreen></iframe></div>
</div>

## x86 with a side of Arm

This is a gutsy design, and to be honest, I love it. It's not just another Arm board, it's trying something new.

But when I tweeted about it, some people were skeptical. Like [Libre Computers replied](https://twitter.com/librecomputer/status/1818696296040907210):

> "ARM SoCs are usually designed to idle at 1W. N100 idles at 5W. N100 should not be put on a small form factor board like the Pi series."

So to figure out if the X4 is a Pi killer, I have to test it in all the ways I test a Pi or other Arm SBC.

## Thermals and Cooling

First: is the Intel CPU too hot for a board this small? After running my SBC benchmarks, the answer is 'yes'.

{{< figure src="./radxa-x4-heatsink.jpg" alt="Radxa X4 Heatsink" width="700" height="auto" class="insert-image" >}}

There's almost no way you could run this thing without active cooling, and Radxa's own heatsink enclosure is just not adequate. In fact, at least in the first production batch, the thermal pad was crumbly and didn't make great contact for most testers.

Even if you go all out with some thick thermal paste, the heatsink can't pull enough heat off to keep the CPU from throttling, even with a reduced power limit.

On top of that, the integrated fan cable is laughably short, and the wires have to be stretched pretty tightly to plug into the 2-pin fan header under the USB ports.

I tried fixing it by re-screwing the fan with the wires closer to the fan connector, but the fan blades started rubbing against one of the wires, so this really needs to be fixed with a longer cable.

But the fan still just runs full blast all the time, [there's no way to control fan speed](https://forum.radxa.com/t/x4-fan-speed-control/22262/7?u=geerlingguy), and it's not quiet. (It's not horribly loud, but it's annoying if it's on my desk 2' away.)

Assuming you're fine with that, how does the X4 stack up against other SBCs? It's still _fast_, but it's not giving the same leap in performance I measured on the LattePanda Mu, with the same chip.

{{< figure src="./radxa-x4-hpl-efficiency.jpg" alt="Radxa X4 HPL Efficiency" width="700" height="auto" class="insert-image" >}}

The Radxa Rock 5C, which uses an Arm chip (RK3588S), is even faster than the X4 at nearly everything, _and_ it's much more efficient. The 5C running _without a heatsink_ and would still be faster, at least for a while.

{{< figure src="./radxa-x4-linux-recompile-benchmark.jpg" alt="Radxa X4 Linux Recompile Benchmark" width="700" height="auto" class="insert-image" >}}

The LattePanda Mu has the same N100 chip, but it's noticeably faster, especially on the Linux recompile, where it's more than _twice_ as fast. Any time the CPU needs power for a long time, the X4 starts throttling.

> See _all_ my benchmarking and test results in the [sbc-reviews: Radxa X4 GitHub issue](https://github.com/geerlingguy/sbc-reviews/issues/48).

There's just not enough board space to handle the power requirements for an Intel CPU.

And board space also means the LPDDR5 RAM runs slower. There isn't enough space on the PCB to put in dual-channel, 64-bit-wide address support. So not only is the CPU throttling from heat, it isn't getting as good of performance because the memory's slower.

{{< figure src="./radxa-x4-tinymembench.jpg" alt="Radxa X4 - Tinymembench vs N100 on LattePanda Mu" width="700" height="auto" class="insert-image" >}}

Tinymembench really shows those differences, you're getting like 50 to 60% better performance on the Mu.

## Usage

The compromises from a bigger chip and more power don't end with performance.

Because of the size of the N100, it had to go on the bottom. The official heatsink case flips the board upside-down, so it's hard to use for tinkering. In fact, some of the GPIO pins are nearly inaccessible, unless you take off the bottom part of the heatsink case.

Then, you can't really use it upside-down, because the fan has nowhere to pull in fresh air, so you can either try running it on its side, or just give up on tinkering with HATs.

{{< figure src="./radxa-x4-hat-gpio.jpg" alt="Radxa X4 HAT with GPIO" width="700" height="auto" class="insert-image" >}}

One thing I did love is the built-in audio jack, but the flipped design also means you have some antennas and a CMOS battery just flapping in the breeze.

I used some VHB tape for the battery, and stuck the antennas onto the base, but the enclosure overall is full of compromises; I hope they can design a better case.

There are other things SBC users get used to that are missing, like [HDMI-CEC support](https://forum.radxa.com/t/new-n100-intel-board-x4/21928/72). That makes it a little more annoying if you want to use for a media center.

I also used one of my NVMe SSDs in the tiny 2230-size M.2 slot, and it works great, except it's also burning hot, idling above 70°C!

The NVMe did get over 1.5 GB/sec read and write speeds, and networking was solid too, with wired giving me 2.35 Gbps, and wireless over 600 Mbps on my WiFi 6 network.

The integrated GPU is a highlight, though; it's not only faster than any of the Arm SBC GPUs I've tested, it can run games natively in Windows (at least casual games).

In general, the _PC_ parts of this thing are good. They're not _great_, but good, especially considering the price and size of the X4.

## GPIO and RP2040

GPIO makes a Pi a Pi, and there's a huge ecosystem of Pi HATs to add on anything from audio devices to AI accelerators.

{{< figure src="./radxa-x4-and-pi-hats.jpg" alt="Radxa X4 with Pi HATs" width="700" height="auto" class="insert-image" >}}

Do those work with the X4? No. Well, at least a lot of them won't, without a decent amount of effort porting things into MicroPython, and building your own bridge between Linux or Windows and the RP2040.

The way Radxa set it up is neat, though. You just press the unmarked button near the GPIO header, and it mounts the RP2040 as a USB device. Copy firmware over to it, and the 2040 reboots and runs the firmware.

You can drop MicroPython on it, and run any 2040 code on it. I tested temperature measurements with the built-in ADC, and had no issues. Pinouts for popular devices and libraries will [differ from standard Pi GPIO](https://forum.radxa.com/t/using-gpio-through-the-rp2040/22169/8?u=geerlingguy), though.

But it is a neat implementation. It's certainly more fun having the RP2040 integrated instead of dangling a Pico off the side. And you _can_ do real-world projects with this, it'll just take more effort since you can't rely on the hundreds of HATs and libraries are already in existence.

## BIOS and Windows

But let's be honest, most people who run Raspberry Pi's don't use the GPIO. And if you're running a Pi in your homelab, a lot of software is still easier to run on x86, like [old-school software that doesn't support Arm yet](https://forums.truenas.com/t/truenas-scale-on-arm-2024-thread/2706).

An SBC with full-fledged BIOS and the ability to run Windows without patching an Insider build is useful.

And to that end, I installed Windows 11. I created a USB installer, popped it in the X4, and installed Windows, just like that.

{{< figure src="./radxa-x4-windows-11-device-manager.jpg" alt="Radxa X4 - Windows 11 Device Manager" width="700" height="auto" class="insert-image" >}}

Windows didn't automatically recognize the Ethernet or WiFi, though, so I had to use a USB Ethernet adapter to get Internet access. Once I did that, I downloaded the [_800 megabyte_ Ethernet driver package](https://docs.radxa.com/en/x/x4/driver#25gbe-driver-installation) from Radxa's site, installed it, and now I could use onboard Ethernet. The [WiFi driver](https://docs.radxa.com/en/x/x4/driver#wi-fi-installation) was thankfully a lot smaller, and after installing it, I could use WiFi too.

Then I tried installing the [Intel GPU driver](https://docs.radxa.com/en/x/x4/driver#gpu-driver-installation), and after I downloaded it from Radxa, Windows told me the compressed folder was empty!

I [posted an issue on Radxa's community forum](https://forum.radxa.com/t/windows-intel-gpu-driver-the-compressed-folder-is-empty/22344?u=geerlingguy), and it looks like Radxa will fix the download. But having to download a driver from Radxa for an Intel device, and having the zip file look corrupt, makes the experience running Windows a little annoying.

Luckily, the GPU driver eventually installed in the background, and like I mentioned earlier, the iGPU on here is pretty decent.

{{< figure src="./radxa-x4-youtube-4k-playback.jpg" alt="Radxa X4 - Windows YouTube 4K playback" width="700" height="auto" class="insert-image" >}}

At least, it'll run casual games okay on low settings. And it accelerates video playback well enough for 4K on YouTube. I can't say the same for most Arm SBCs.

Outside my driver speedbumps, BIOS releases need more QA. This is an area I've dinged Radxa on in the past. Hardware is usually pretty amazing, but the software experience kinda spoils it. They've already had one BIOS slip-up, they released an update that [magically gave everyone 12 Gigs of RAM earlier this month](https://x.com/bretweber/status/1820566228630716661?s=43), except it didn't.

[Bret Weber](https://x.com/bretweber/status/1820727607651901622) installed it, and when he tried using the extra RAM the BIOS gave him, the X4 crashed.

And you could just skip BIOS updates, right? Well, the reason Bret probably upgraded was to [get GPIO support working](https://forum.radxa.com/t/x4-gpioinfo-gipiodetect-cant-find-gpio/22227?u=geerlingguy); that wasn't something that worked on the firmware the board launched with.

So Radxa still has some work to do on the software and support side, especially for early adopters.

## Conclusion

Which brings me to my recommendation. Do I think this is the Pi killer, finally here after all these years?

No.

The hardware is very cool. And unlike many of the other Arm SBCs I own, this one might _not_ end up in a box on my shelf. But do I think anyone buying a Pi, or one of the other Arm SBCs that's faster and more efficient, should drop Arm and switch to this Intel board? No.

It has its uses, and for the price, despite its flaws, I think it's a great value. But it's not quite the Pi killer we expected.
