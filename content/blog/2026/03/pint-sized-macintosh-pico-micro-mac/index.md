---
draft: true
date: '2026-02-20T09:50:09-06:00'
tags: ['mac', 'macintosh', 'youtube', 'video', 'pico', 'raspberry pi', 'open source', 'micro', 'marchintosh']
title: "I built a pint-sized Macintosh"
slug: 'pint-sized-macintosh-pico-micro-mac'
---
To kick off [MARCHintosh](https://marchintosh.com), I built this tiny pint-sized Macintosh with a Raspberry Pi Pico:

{{< figure
  src="./pico-micro-mac-screen-system-folder.jpg"
  alt="Pico Micro Mac running System 5.3"
  width="700"
  height="auto"
  class="insert-image"
>}}

This is not my own doing—I just assembled the parts to run Matt Evans' [Pico Micro Mac](https://github.com/evansm7/pico-mac) firmware on a Raspberry Pi Pico (with an RP2040).

The version I built outputs to a 640x480 VGA display at 60 Hz, and allows you to plug in a USB keyboard and mouse.

Since the original Pico's RAM is fairly constrained, you get a maximum of 208 KB of RAM with this setup—which is 63% more RAM than you got on the original '128K' Macintosh!

## Hardware

I was inspired to try this out after seeing the setup on [Ron's Computer Videos](https://www.youtube.com/watch?v=G3bW4f5Gn4o) and [Action Retro](https://www.youtube.com/watch?v=jYOTAGBqoW0).

{{< figure
  src="./pico-micro-mac-pre-assembly.jpg"
  alt="Pico Micro Mac - Hardware pre-assembly"
  width="700"
  height="auto"
  class="insert-image"
>}}

And almost two years ago now, I bought all the parts for the build:

  - [JCM - PicoMicroMac (v3) hardware](https://jcm-1.com/product/picomicromac/) (I had the now-discontinued v2)
  - PicoMicroMac microSD card adapter (discontinued)
  - [Eyoyo 5" VGA Monitor](https://amzn.to/4cOULz9)
  - [1ft VGA cable](https://amzn.to/4bdaaIq)
  - [Micro USB to USB OTG cable](https://amzn.to/3OGeXt9)

As with most of my projects, the parts have been sitting in a box long enough that a new version exists which makes the build even easier! Ron (of Ron's Computer Videos) designed a ['V3' version](https://jcm-1.com/product/picomicromac/) of the Pico Micro Mac adapter, which makes the setup much easier:

  - It integrates the microSD card adapter right into the main board (no need for a little 'microSD card HAT' soldered precariously on top of some header pins)
  - It has two rows of female headers, so you can just buy a [Pico WH](https://www.adafruit.com/product/5525) ('With Headers') and plug it in—no soldering required!

Since I had purchased the V2 version a couple years ago, I had to do a little soldering before I could flash it with a Macintosh ROM and OS image:

{{< figure
  src="./pico-micro-mac-soldering-sd-hat.jpg"
  alt="Pico Micro Mac - Soldering on the microSD card HAT"
  width="700"
  height="auto"
  class="insert-image"
>}}

If you'd like to see the full setup, along with some video of me trying out games and applications on System 5.3 (pre 'Mac OS' days!), you can watch the video below:

<div class="yt-embed">
  TODO
</div>

If you just want to see how to finish setting up a Pico Micro Mac (any version, including v3), read on!

## Pico setup (Mac OS on a Pi Pico)

You can set up the Pico before or after putting together all the hardware, all you need to do is plug it into a computer with a micro USB cable.

First, you need a `.uf2` file to flash the Pico. This is the firmware based on [pico-mac](https://github.com/evansm7/pico-mac) which runs an early version of Mac OS, and contains all the necessary system files to boot and display VGA.

In my case, since I am using the microSD Card HAT, I downloaded the [Firmware for Pico with SD Card Hat (208K + VGA Resolution)](https://retro.bluescsi.com/pico-umac-208k-sd-vga.uf2) directly from the [PicoMicroMac UF2 Creator](https://picomac.bluescsi.com) page.

{{< figure
  src="./pico-micro-mac-plug-in-usb.jpg"
  alt="Pico Micro Mac - plug Pico into USB port while holding down BOOT"
  width="700"
  height="auto"
  class="insert-image"
>}}

To flash the UF2 to the Pico:

  1. Hold down the 'BOOT' button on the Pico while plugging it into your computer via the micro USB connector
  2. After the drive mounts, copy the downloaded `.uf2` file directly to the root of the drive.
  3. After the copy is complete, the Raspberry Pi Pico will automatically restart itself, and unmount from your computer. You can safely disconnect it now.

If, like me, you're also using the microSD Card HAT, you will also need to copy a `umac0.img` file like the one provided on the [PicoMicroMac UF2 Creator](https://picomac.bluescsi.com) page, in the "PicoMicroMac with SD Hat" section.

Format a microSD card as FAT32 (I used Raspberry Pi Imager to do this), and then copy the `umac0.img` file directly to the root of the drive.

The Pico Micro Mac firmware will mount this disk during startup.

## Plugging it all in

{{< figure
  src="./pico-micro-mac-booted.jpg"
  alt="Pico Micro Mac - booted into Mac OS System 5.3"
  width="700"
  height="auto"
  class="insert-image"
>}}

To boot up the Pico Mac:

  1. Plug a VGA monitor into the VGA port.
  1. Plug a micro USB to USB-A adapter or hub into the Pico's micro USB port, then plug a keyboard (ideally a keyboard with a built-in hub) and mouse into the adapter.
  1. Plug micro USB power into the PicoMicroMac board's micro USB port.

Assuming you put everything together correctly and the Pico is flashed, it should boot up, with a 'Welcome to Macintosh' splash screen, then the Mac OS desktop.

## Usage

{{< figure
  src="./pico-micro-mac-running.jpg"
  alt="Pico Micro Mac - running over VGA monitor"
  width="700"
  height="auto"
  class="insert-image"
>}}

Probably the biggest limitation of this setup is the Pico's SRAM, which only allows up to 208 KB of RAM to be allocated to Mac OS.

> Matt Evans (evansm7 on GitHub) has done some work with RP2350 to [enable more memory—up to 4MB in one test running System 7.5.5!](https://github.com/evansm7/pico-mac/issues/7). But that capability is still in the more experimental stage, as only a few people have been testing on the RP2350 so far.

If you use the sample images provided by the UF2 Creator page, the applications provided should all run within the 208 KB of available RAM.

But if you want to run larger applications, or games that were built specifically to run on later Macs like the 512K or Mac Plus, they'll likely complain about running out of memory.

[Action Retro tried running \\]\\[ in a Mac](https://archive.org/details/2InaMac), but it also complained there wasn't enough RAM to emulate an Apple II.

Sound also doesn't work—see [this issue](https://github.com/evansm7/pico-mac/issues/23), and we probably won't see more specialized features like AppleTalk, SCSI, and printer support any time soon.

## Conclusion

Early Macintosh computers were very limited in what they could do—despite the $2,495 price tag (almost $8,000 today, adjusted for inflation).

The Pico Micro Mac is even _more_ limited... but what do you expect for a setup that cost me around $20 (about $5 in 1984 dollars!)?

In reality, this setup is mostly useful for learning and the novelty.
