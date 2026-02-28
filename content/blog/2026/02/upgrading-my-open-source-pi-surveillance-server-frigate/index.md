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

I've wanted to downsize the setup while keeping ~~cheap~~ large hard drives[^hdds], and an AI accelerator.

Luckily, Exaviz sent me their new [Cruiser](https://exa-pedia.com/docs/cruiser/) board to test, and DeskPi sent me a prototype mini rack enclosure for it (the [DeskPi 2U Mini Rack Mount Case for Cruiser](https://deskpi.com/products/deskpi-2u-mini-rack-mount-case-pre-order-for-the-exaviz-cruiser-carrier-board)).

I bought a couple Dell R720 drive sleds, plugged in a Compute Module 5, and tested it. I made a video on the upgrade here:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/2LayXUxMjPU' frameborder='0' allowfullscreen></iframe></div>
</div>

If you'd rather read through a more condensed version, scroll on!

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

  - The M.2 M-key NVMe slot is connected directly to the Pi's PCIe Gen 2 x1 lane (technically [you can run it at Gen 3, but that's not the official spec](/blog/2023/forcing-pci-express-gen-30-speeds-on-pi-5/)).
  - The 2.5 Gbps WAN port (RTL8156BG) is routed through USB 3.0
  - The 2x SATA connections (JMS561) are routed through USB 3.0
  - The (up to) 8 10/100/1000 Mbps PoE+ ports (RTL8367RB) are connected to the CM5's built-in 1 Gbps Ethernet.

There are extra USB 3.0 and USB 2.0 ports for accessories and peripherals, a microSD card slot for Lite CM5s, two Qwiic I2C connectors, two HDMI 2.0 ports, fan headers, a molex power connector for HDD power, and even an ESP32-C6 thrown in the mix to give the board [Zigbee](https://exa-pedia.com/docs/cruiser/esp32/#zigbee-coordinator) (or additional WiFi/BT) capabilities.

There's a front panel IO header, a jumper to enable hardware RAID if you want, a connector for adding on even _more_ PoE ports (via addon card), and a 48V DC barrel jack accepting up to 288W of power (48V at 6A, recommended if you buy the maxed-out version).

The board doesn't fit in an ITX-sized chassis, but all the important IO is on one side, at least, meaning you don't wind up with a cable mess.

## DeskPi's mini rack case

Installing the Cruiser in DeskPi's [prototype 2U mini rack enclosure](https://deskpi.com/products/deskpi-2u-mini-rack-mount-case-pre-order-for-the-exaviz-cruiser-carrier-board) was easy enough:

{{< figure
  src="./exaviz-cruiser-front-built.jpg"
  alt="Exaviz Cruiser in DeskPi Rackmount - front"
  width="700"
  height="auto"
  class="insert-image"
>}}

The front side looks polished, with the ports all in a wide IO cutout, and the R720-style drive sleds locked in.

The back... not quite as much:

{{< figure
  src="./exaviz-cruiser-back-built.jpg"
  alt="Exaviz Cruiser in DeskPi Rackmount - back"
  width="700"
  height="auto"
  class="insert-image"
>}}

DeskPi is working on it, though. This prototype just lets the cables dangle, but they may be engineering a PCB that allows the drive sleds to hot swap more easily, without having wires to plug and unplug by hand every time.

They also included a power button with no power LED, which makes it harder to tell if the system is powered on from the front—so hopefully the final version will have an LED on the power button, in addition to a better option for cable managing the two drives.

(I've also mentioned thin ITX motherboard compatibility would make this enclosure even better!)

The two bays at the bottom accept drive sleds like [these Dell R720-compatible sleds](https://www.ebay.com/itm/404293056771) I found on eBay. Into those sleds I installed two $99(!) [4TB IronWolf NAS hard drives](https://amzn.to/46vIPyx). Someday storage will go back down in price again. [Hopefully](https://pcpartpicker.com/trends/price/internal-hard-drive/#storage.hdd350.4000).

The power button and cabling are cosmetic issues, but cooling is something that could be improved in the design that goes to production.

{{< figure
  src="./exaviz-cruiser-deskpi-case-cm5-hot-thermal-camera.jpg"
  alt="Exaviz Cruiser CM5 is hot in prototype case"
  width="700"
  height="auto"
  class="insert-image"
>}}

The fan up top is used for exhaust, but as you can see above, because there are so many vents and openings, air is not directed over the top of the hottest part of the build—the CM5, and thus it can overheat under load (even with a small heatsink, as I had configured it).

For now, I can work around this problem by installing a fan/heatsink combo like the EDAtec's [Active Cooler for CM5](https://www.pishop.us/product/active-cooler-for-raspberry-pi-cm5/?searchid=0&search_query=cm5+cooler). The Cruiser includes multiple case fan (3 pin) headers, so adding a couple fans elsewhere would be another easy fix.

## Software

My goal was to run [Frigate](https://frigate.video), one of the most popular open source NVR apps, and to do that efficiently, you need mass storage (to store video) and a suitable accelerator for object detection (e.g. people, cars, bikes, animals, etc.).

To that end:

  - I [built a RAID 1 array with mdadm](/blog/2021/htgwa-create-raid-array-linux-mdadm/), with the two 4TB drives mirrored, so if one drive dies, I still have all the footage.
  - I [installed the Hailo 8 driver on the Pi](/blog/2026/frigate-with-hailo-for-object-detection-on-a-raspberry-pi/) following Frigate's guide.
  - I installed Frigate (in Docker) using my [pi-nvr Ansible playbook](https://github.com/geerlingguy/pi-nvr).

After sorting out one issue with the Hailo on the Pi's PCIe bus (mentioned in the linked post above), everything was working, and Frigate saw the three cameras I had connected:

{{< figure
  src="./frigate-three-cameras-feed-exaviz-cruiser.jpg"
  alt="Frigate with three camera feeds including a 4K Annke camera"
  width="700"
  height="auto"
  class="insert-image"
>}}

Three cameras barely scratches the surface of what this setup can do—CPU usage was under 5%, the Hailo utilization was below 10%, and object detection was running around 10-11ms. That was with two 1080p cameras and one 4K.

Considering even 4K security cameras run on 100 Mbps networking, and most cameras send low-bandwidth H.264 or H.265 feeds, 8 cameras [should be easy](https://www.cctvcalculator.net/en/calculations/bandwidth-calculator/), even if you're just running one slow hard drive and a Hailo 8L.

## PoE ports and power monitoring and control

The headline feature of this board is the built-in PoE+ switch—which is managed through Linux on the Pi. Exaviz maintains their own OS image, but you can [install their drivers](https://exa-pedia.com/docs/cruiser/software/#drivers-and-software) on Pi OS, like I did.

In addition to configuring all the networking, their packages include a GUI for PoE port management, called PoE Tool:

{{< figure
  src="./exaviz-cruiser-poe-tool.jpg"
  alt="Exaviz Cruiser PoE Tool GUI in Pi OS"
  width="700"
  height="auto"
  class="insert-image"
>}}

You can monitor port status, power consumption, and reset ports (to remotely power cycle powered devices).

The default networking configuration uses the Pi as a bridge (with an uplink to your network through the 2.5 Gbps WAN port). The PoE ports are on their own subnet. All of this can be customized, if you don't like the defaults configured by the `exaviz-netplan` package.

If you'd like to monitor the PoE port status in Home Assistant, [Exaviz maintains a plugin for that](https://exa-pedia.com/docs/home-assistant/). I'd love to see more vendors provide HA integration for devices which will find their way into homelabs.

## Conclusion

Besides the cooling issue, I had no issues with the pre-launch hardware I tested. I was especially impressed by the quality of Exaviz's documentation, even though they hadn't publicly launched the product while I was testing.

If DeskPi can iron out a couple enclosure quirks, this will be a killer setup for network video recording, or even a generic storage server for mini racks.

The Crusier will go on sale for between $99 and $149, and Exaviz even makes their own [deep 1U desktop case (that fits in a mini rack)](https://www.exaviz.com/product-page/cruiser-1u-case).

[^hdds]: Hard drives are still the gold standard for Network Video Recorders (NVRs). They're cheap (at least compared to SSDs—nothing's cheap these days), and plenty fast for low-bandwidth video streams. Not amazing for random access, of course.
