---
date: '2026-03-24T11:00:00-05:00'
tags: ['firewire', 'raspberry pi', 'pi 5', 'pcie', 'pci express', 'apple', 'ieee 1394']
title: 'Using FireWire on a Raspberry Pi'
slug: 'firewire-on-a-raspberry-pi'
---
After learning Apple [killed off FireWire (IEEE 1394) support in macOS 26 Tahoe](https://512pixels.net/2025/07/tahoe-no-firewire/), I started looking at alternatives for old FireWire equipment like hard drives, DV cameras, and A/V gear.

{{< figure
  src="./g4-canon-gl1-firewire.jpg"
  alt="Power Mac G4 MDD with Canon GL1 DV Camera importing footage into Final Cut Express"
  width="700"
  height="auto"
  class="insert-image"
>}}

I own an old Canon GL1 camera, with a 'DV' port. I could plug that into an old Mac (like the dual G4 MDD above) with FireWire—or even a modern Mac running macOS < 26, [with some dongles](https://youtu.be/nqCO4Z_VP3c?t=1281)—and transfer digital video footage between the camera and an application like Final Cut Pro.

But with Apple killing off support, and my desire to have a modern, supported hardware solution, I turned to Linux and `dvgrab`.

Linux will likely [drop support for IEEE 1394 in 2029](https://ieee1394.docs.kernel.org/en/latest/#maintenance-schedule), but at least that gives me three more years!

On a Raspberry Pi, I can plug in [this GeeekPi Mini PCIe HAT](https://amzn.to/47U0vFj), and connect a [StarTech Mini PCIe FireWire adapter](https://amzn.to/4lRrQeU). This allows the Pi to recognize the FireWire controller:

```
$ lspci
0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
0001:01:00.0 PCI bridge: Texas Instruments XIO2213A/B/XIO2221 PCI Express to PCI Bridge [Cheetah Express] (rev 01)
0001:02:00.0 FireWire (IEEE 1394): Texas Instruments XIO2213A/B/XIO2221 IEEE-1394b OHCI Controller [Cheetah Express] (rev 01)
0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
```

But to _use_ it, you have to [recompile the Linux kernel](/blog/2025/how-recompile-linux-on-raspberry-pi/) with FireWire support, then configure the Pi's PCIe bus for 32-bit DMA support, since old FireWire controllers like the TI XIO2213A and VIA VT6315N don't support 64-bit access.

## Recompile the Linux Kernel with Firewire support

Recompile the Linux kernel, enabling the following features:

  - `CONFIG_FIREWIRE` (Device Drivers -> IEEE 1394 (FireWire) support -> FireWire driver stack)
  - `CONFIG_FIREWIRE_OHCI` (Device Drivers -> IEEE 1394 (FireWire) support -> FireWire driver stack -> OHCI-1394 controllers)

## Configure Pi Boot options

At the end of `/boot/firmware/config.txt`, under `[all]`, add:

```
dtparam=pciex1
dtoverlay=pcie-32bit-dma
```

At the end of the line in `/boot/firmware/cmdline.txt`, add:

```
pcie_aspm=off
```

Reboot your Pi.

## Using FireWire on the Pi

{{< figure
  src="./canon-gl1-pi-firewire-dvgrab.jpg"
  alt="Canon GL1 connected to Raspberry Pi 5 via FireWire 400 Mini PCIe card"
  width="700"
  height="auto"
  class="insert-image"
>}}

At this point, you should be able to use FireWire devices connected to the FireWire 400 port. If you want to use the FireWire 800 ports, you'll have to find a way to connect auxiliary power to the power header on the Mini PCIe card (StarTech provides an adapter for this).

All my devices are FireWire 400, so this was not a concern for me.

Using `dvgrab` (which can be installed with `sudo apt install -y dvgrab`), you can record clips from the camera in either camera or 'VCR' mode, for example:

```
$ sudo apt install -y dvgrab

$ dvgrab
Found AV/C device with GUID 0x000085000014e35a
libiec61883 error: Failed to get channels available.
Waiting for DV...
Capture Started
^C"dvgrab-002.dv":    45.89 MiB 401 frames timecode 00:00:00.00 date 2067.02.15 22:26:25
Capture Stopped
```

You can use `dvgrab` interactively, too:

```
$ dvgrab -i
Found AV/C device with GUID 0x000085000014e35a
libiec61883 error: Failed to get channels available.
Going interactive. Press '?' for help.
q=quit, p=play, c=capture, Esc=stop, h=reverse, j=backward scan, k=pause        
l=forward scan, a=rewind, z=fast forward, 0-9=trickplay, <space>=play/pause
```

I posted my first [sample video recording](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/752#issuecomment-3993083089) with this setup over on GitHub.

DVgrab is straightforward, and can easily be used in scripts—something which I'll explore later with a prototype [Firehat](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/805), and which would be useful for projects like [Open MRU](https://www.reddit.com/r/tapeless/comments/1n3aqsk/open_mru_raspberry_pi_5_based_mrucapture_device/), both of which I found on the [r/tapeless subreddit](https://www.reddit.com/r/tapeless/)...
