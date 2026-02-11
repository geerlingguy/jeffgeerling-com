---
draft: true
date: '2026-02-20T09:50:09-06:00'
tags: ['mac', 'macintosh', 'youtube', 'video', 'pico', 'raspberry pi', 'open source', 'micro', '3d printing']
title: "For Apple's 50th, a pint-sized Macintosh"
slug: 'pint-sized-macintosh'
---
TODO: Hero photo

TODO: Intro

## Hardware

{{< figure
  src="./pico-micro-mac-pre-assembly.jpg"
  alt="Pico Micro Mac - Hardware pre-assembly"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO: Mention all the parts, including SD card header

TODO: Mention assembly

{{< figure
  src="./pico-micro-mac-soldering-sd-hat.jpg"
  alt="Pico Micro Mac - Soldering on the microSD card HAT"
  width="700"
  height="auto"
  class="insert-image"
>}}

> The [V3 edition of the Pico Micro Mac](https://jcm-1.com/product/picomicromac/) allows you to plug a Pi Pico directly into the headers on top, _and_ includes a built-in microSD card slot. Very fancy! My PCBs were purchased a bit earlier, when you still had to stack things a bit odd and add on your own headers to the Pico. So if you get the V3 board and a [Pico with Headers](https://www.adafruit.com/product/5525), you don't have to solder at all!

## Pico setup (Mac OS on a Pi Pico)

You can set up the Pico before or after putting together all the hardware, all you need to do is plug it into a computer with a micro USB cable.

First, you need a `.uf2` file to flash the Pico. This is the firmware based on [pico-mac](https://github.com/evansm7/pico-mac) which runs an early version of Mac OS, and contains all the necessary system files to boot and display VGA.

In my case, since I am using the [microSD Card HAT](TODO), I downloaded the [Firmware for Pico with SD Card Hat (208K + VGA Resolution)](https://retro.bluescsi.com/pico-umac-208k-sd-vga.uf2) directly from the [PicoMicroMac UF2 Creator](https://picomac.bluescsi.com) page.

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
  src="./pico-micro-mac-plugged-in.jpg"
  alt="Pico Micro Mac - everything plugged in"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO: SWAP OUT THIS PICTURE FOR ONE OF IT ACTUALLY DOING THE THING

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

## Building it into a pint-sized enclosure

TODO: This is the challenge.

## Conclusion

Early Macintosh computers were very limited in what they could do—despite the $2,495 price tag (almost $8,000 today, adjusted for inflation).

The Pico Micro Mac is even _more_ limited... but what do you expect for a setup that costs around $20 (re-inflated, would be about $5!)?

In reality, this setup is mostly useful for learning and the novelty.
