---
date: '2026-02-27T09:00:00-06:00'
tags: ['raspberry pi', 'cm5', 'compute module', 'exaviz', 'nvr', 'video', 'youtube', 'frigate', 'cruiser', 'review', 'poe']
title: 'Upgrading my Open Source Pi Surveillance Server with Frigate'
slug: 'upgrading-my-open-source-pi-surveillance-server-frigate'
---
In 2024 I built a [Pi Frigate NVR with Axzez's Interceptor 1U Case](/blog/2024/building-pi-frigate-nvr-axzezs-interceptor-1u-case/), and installed it in my 19" rack. Using a Coral TPU for object detection, it's been dutifully surveilling my property—on _my_ terms (100% local, no cloud integration or account required).

{{< figure
  src="./exaviz-cruiser-mini-rack-enclosure-with-annke-camera.jpeg"
  alt="Exaviz Cruiser CM5 carrier board inside DeskPi mini rack enclosure with Annke 4K camera on top"
  width="700"
  height="auto"
  class="insert-image"
>}}

I've wanted to downsize the setup while keeping cheap, large hard drives (still the gold standard for Network Video Recorders (NVRs)), and an AI accelerator.

Luckily, Exaviz sent me their new [Cruiser](https://exa-pedia.com/docs/cruiser/) board to test, and DeskPi sent me a prototype mini rack enclosure for it.

I bought a couple Dell R720 drive sleds, plugged in one of my Compute Module 5's, and tested it. I made a video on the upgrade here:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/2LayXUxMjPU' frameborder='0' allowfullscreen></iframe></div>
</div>

But if you'd rather read through a more condensed version, scroll on!

## Hardware

The star of the show, is of course the Cruiser CM5 carrier board:

{{< figure
  src="./exaviz-cruiser-top.jpeg"
  alt="Exaviz Cruiser CM5 carrier board top"
  width="700"
  height="auto"
  class="insert-image"
>}}

The architecture works around the Raspberry Pi CM5's main downside: limited PCI Express bandwidth. Instead of adding an expensive PCIe switch, and attaching multiple high-bandwidth devices to the Pi's only PCIe lane, Exaviz went with a mix of PCIe and USB:

  - The M.2 NVMe slot is connected directly to the Pi's PCIe Gen 2 x1 lane (technically [you can run it at Gen 3, but that's not the official spec](/blog/2023/forcing-pci-express-gen-30-speeds-on-pi-5/)).
  - The 2.5 Gbps WAN port (RTL8156BG) is routed through USB 3.0
  - The 2x SATA connections (JMS561) are routed through USB 3.0
  - The (up to) 8 100 Mbps PoE+ ports (RTL8367RB) are connected to the Pi's 1 Gbps Ethernet connection.

There are extra USB 3.0 and USB 2.0 ports for accessories and peripherals, a microSD card slot for Lite CM5s, two Qwiic I2C connectors, two HDMI 2.0 ports, fan headers, a molex power connector for HDD power, and even an ESP32-C6 thrown in the mix to give the board Zigbee (or additional WiFi/BT) capabilities.

There's a front panel IO connector, a jumper to enable hardware RAID if you want (I don't!), a connector for adding on even _more_ PoE ports (via addon card), and a 48V DC barrel jack accepting up to 288W of power (48V at 6A, recommended if you buy the maxed-out version).

The board doesn't fit in an ITX-sized chassis, but all the important IO is on one side, at least, meaning you don't wind up with a cable mess.

## DeskPi's mini rack case

Installing the Cruiser in DeskPi's prototype mini rack enclosure (which is not public yet—I'll try to link to it when available) was easy enough:

TODO: Photo of front enclosed.

The front side looks polished, with the ports all in a wide IO cutout, and the R720-style drive sleds locked in.

The back... not quite as much:

TODO: Photo of back with wires.

DeskPi is working on it, though. This prototype just lets the cables dangle, but they may be engineering a PCB that allows the drive sleds to hot swap more easily, without having wires to plug and unplug by hand every time.

TODO: More notes here.

## Software

TODO: RAID, Hailo, Frigate, PoE control, Exa-pedia, and Home Assistant plugin

## How many cameras can it support?

Considering even 4K security cameras run on 100 Mbps networking, and most bitrates available on commercial units are low, 8 cameras should be easy, even if you store footage on a single hard drive.

12 or 16 cameras may be a little harder, depending on resolution and bitrate, but I imagine the CM5 could handle that too, especially if you put two drives in RAID 0, or use SSDs instead of spinning disks.

## Conclusion

Besides the cooling issue, I had no issues with the pre-launch hardware I tested. I was especially impressed by the quality of Exaviz's documentation, even though they hadn't publicly launched the product while I was testing.

If DeskPi can iron out a couple enclosure quirks, this will be a killer setup for network video recording, or even a generic storage server for mini racks.

The Crusier will go on sale for between $99 and $149, and Exaviz even makes their own [deep 1U desktop case (that fits in a mini rack)](https://www.exaviz.com/product-page/cruiser-1u-case).
