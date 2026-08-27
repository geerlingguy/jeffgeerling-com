---
date: '2026-08-28T09:00:00-05:00'
tags: ['tag_here']
title: 'Building a mini Homelab that fits in my carry-on'
slug: 'mini-homelab-network-fits-in-carry-on'
---
I'm traveling to Chicago for VCF Midwest next month. This year I'll be demoing NTP time through the years on Macs, with my own GPS-derived NTP services hosted on an Xserve G5.

The demo involves some vintage Macs since Apple actually has an interesting history with Internet time (which I'll get into in a future blog post), but underneath the table, I'd like to have a little 'portable homelab' I can preconfigure so I don't have to worry about networking at the show.

This is what I built:

{{< figure
  src="./ubiquiti-mini-rack-network-with-ups.jpg"
  alt="Ubiquiti mini rack network with UPS"
  width="700"
  height="auto"
  class="insert-image"
>}}

Is it overkill for this particular scenario? _Absolutely_. Would it look different if Micro Center hadn't sponsored the build as part of their [Columbus OH grand re-opening event](https://www.youtube.com/@Level2Jeff)? _You bet_.

That said, it's not far off some of the other networking mini-rack builds I've seen in the [Project MINI RACK Build Showcase](https://mini-rack.jeffgeerling.com/#build-showcase). And I'm usually happier to have more flexibility (like having 8 PoE++ ports, a solid WiFi AP, and an independent 5G Internet connection) when I'm on the road and trying to keep _other_ weird stuff (like vintage computers) running. It's better to go overkill on the network stack since I don't want to debug my network setup alongside the Macs.

## Ubiqiti

Until this summer, I'd never used a piece of Ubiquiti hardware. I've run routers built on top of bare Debian Linux installs, consumer routers with OpenWRT or AsusWRT-Merlin (my home router is still running that!), and my studio router is a mini PC running OPNsense.

I figured it was time to see if the UniFi kool-aid is as good as all the influencers say it is.

And overall? It's a nice proprietary ecosystem.

There are plenty of pitfalls to the walled-garden approach with UniFi, but if you want to play in their ecosystem, it's pretty coherent. Everything under one local controller. Optional cloud functionality to manage it remotely or set up site-to-site VPN links. No licensing like some other proprietary vendors...

And the hardware lineup is hard to match—almost everything I tested was plug-and-play.

The main thing I wanted to see: could I set up the entire network from scratch without connecting the Cloud Gateway to the Internet, and never connect any sort of Ubiquiti account to the hardware at all?

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
