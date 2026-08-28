---
date: '2026-08-28T09:00:00-05:00'
tags: ['tag_here']
title: 'Building a mini Homelab that fits in my carry-on'
slug: 'mini-homelab-network-fits-in-carry-on'
---
I'm traveling to Chicago for [VCF Midwest](https://vcfmw.org) next month. I'll be demoing NTP time history on vintage Macs, with my own GPS-derived NTP service hosted on an Xserve G5, synced via NTP or a strange [AppleTalk timing extension from the 1990s](https://netatalk.io/manual/en/timelord.8).

{{< figure
  src="./ubiquiti-mini-rack-network-with-ups.jpg"
  alt="Ubiquiti mini rack network with UPS"
  width="700"
  height="auto"
  class="insert-image"
>}}

So I built a little 'portable homelab' (pictured above) that supports 1-10 Gbps networking, can run off a small battery for at least an hour, switches between multiple WANs (so I can get my own 5G Internet connection, in case I need it), and gives me 12 wired Ethernet connections.

Is it overkill for this particular scenario? _Absolutely_. Would it look different if Micro Center hadn't sponsored the build as part of their [Columbus OH grand re-opening event](https://www.youtube.com/@Level2Jeff)? _You bet_.

That said, it's not far off some of the other networking mini-rack builds I've seen in the [Project MINI RACK Build Showcase](https://mini-rack.jeffgeerling.com/#build-showcase). And I'm happy to have more flexibility when I'm on the road trying to keep _other_ weird stuff (like vintage computers) running. It's better to go overkill on the network stack since I don't want to debug _that_ alongside the Macs.

## Ubiqiti

This is my first experience with UniFi. I've run routers on bare Debian Linux installs, consumer routers with OpenWRT/AsusWRT (my home router is still running that!), and my studio router is currently a mini fanless PC running OPNsense.

I figured it was time to see if the UniFi kool-aid is as good as all the influencers say it is.

First impressions? It's a nice walled garden.

There are plenty of pitfalls to the UniFi's proprietary ecosystem, but if you want to play in their sandbox, it's easy to pick up.

The things I like after messing with this particular Ubiquiti setup:

  - Everything is local-first, and doesn't need any account tie-in
  - Optional cloud integration adds on functionality like remote management and easier site-to-site VPN setup
  - There's no licensing fees for core functionality
  - Most of the hardware is plug-and-play, and easy to manage in one web UI

There are two sides to every coin, and the big sore point I have is the lack of control over the hardware I bought. I don't see any way to unlock the bootloader, so even though the Gateway is running an Arm SoC, there's no way to load my own OS on it.

Not that I'd want to, _today_... but in 10, 20, or however many years, when Ubiquiti drops support for the Gateway I bought, it looks like it'll go straight to e-waste.

But my main goal was to test if I set up everything from scratch without connecting the Cloud Gateway to the Internet, and never connect any sort of Ubiquiti account to the hardware at all. And I could!

## The Build

For a detailed look at this build (and more reasoning behind the components), watch this video:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/qclCCQeg-RQ' frameborder='0' allowfullscreen></iframe></div>
</div>

Mini rack parts (from Micro Center):

  - UniFi Cloud Gateway Fiber: https://www.microcenter.com/product/695361/ubiquiti-cloud-gateway-fiber
  - 2x Ubiquiti 1ft Etherlighting Patch Cable: https://www.microcenter.com/product/709787/ubiquiti-unifi-etherlighting-patch-cable-1-ft
  - 2x Ubiquiti 3.3ft Etherlighting Patch Cable: https://www.microcenter.com/product/698549/ubiquiti-33-ft-unifi-premium-etherlighting-braided-patch-ethernet-cable-white
  - UniFi Flex 2.5G PoE: https://www.microcenter.com/product/695379/ubiquiti-flex-25g-poe-8-port-poe-compliant-managed-network-switch-(psu-not-included)
  - Ubiquiti 210 Watt AC Power Adapter for PoE Switch: https://www.microcenter.com/product/697310/ubiquiti-210-watt-ac-power-adapter-for-poe-switch
  - UniFi 5G Backup: https://www.microcenter.com/product/712077/ubiquiti-unifi-5g-backup
  - U7 Lite: https://www.microcenter.com/product/692982/ubiquiti-unifi-u7-lite-compact-ceiling-mounted-wifi-7-access-point
  - APC UPS BE600M1: https://www.microcenter.com/product/647002/apc-battery-backup-and-surge-protector-ups-(be600m1)

Parts I bought elsewhere (these links are affiliate links):

  - DeskPi RackMate TT: https://amzn.to/4cgPkrL
  - 2' Twinax DAC (for 10Gbps Uplink): https://amzn.to/4y6Y9Nn

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

3D Printed Parts I used in the rack:

  - Cloud Gateway Fiber 10" Rackmount: https://www.printables.com/model/1235928-unifi-ucg-fiber-10-inch-rack-mount
  - Cloud Gateway Fiber M.2 SSD Tray: https://www.printables.com/model/1365302-m2-ssd-tray-for-unifi-cloud-gateway-fiber
  - Flex 2.5G 8 PoE 10" Rackmount: https://makerworld.com/en/models/2037862-unifi-flex-2-5g-8-poe-10-inch-rack-mount
  - U7 Lite 10" Rackmount: https://cults3d.com/en/3d-model/gadget/unifi-u7-lite-10-rack-mount-oounnameoo
  - Ubiquiti 210W Power Supply Rackmount: https://www.printables.com/model/1816999-unifi-210w-ac-power-adapter-mini-rackmount
  - ServeTheHome UniFi Cloud Gateway Fiber Review: https://www.servethehome.com/ubiquiti-unifi-cloud-gateway-fiber-ucg-fiber-review/

Blog post on UniFi 5G Backup debugging: https://www.jeffgeerling.com/blog/2026/unifi-u5g-backup-debugging/

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

## A mini network rack

TODO Explain the rack itself and 3D printed mounts...

## Software and Setup

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO.

## Conclusion

TODO.
