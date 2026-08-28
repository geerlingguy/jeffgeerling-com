---
date: '2026-08-28T10:00:00-05:00'
tags: ['homelab', 'ubiquiti', 'unifi', 'youtube', 'video', 'portable', 'battery', 'mini rack']
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

## Ubiquiti

This is my first experience with UniFi. I've run routers on bare Debian Linux installs, consumer routers with OpenWRT/AsusWRT (my home router is still running that!), and my studio router is currently a mini fanless PC running OPNsense.

I figured it was time to see if the UniFi kool-aid is as good as all the influencers say it is.

First impressions? It's a nice walled garden.

There are plenty of pitfalls to the UniFi's proprietary ecosystem, but if you want to play in their sandbox, it's easy to pick up.

The things I like after messing with this particular Ubiquiti setup:

  - Everything is local-first, and doesn't need any account tie-in
  - Optional cloud integration adds on functionality like remote management and easier site-to-site VPN setup
  - There are no licensing fees for core functionality
  - Most of the hardware is plug-and-play, and easy to manage in one web UI

There are two sides to every coin, and the big sore point I have is the lack of control over the hardware I bought. I don't see any way to unlock the bootloader, so even though the Gateway is running an Arm SoC, there's no way to load my own OS on it.

Not that I'd want to, _today_... but in 10, 20, or however many years, when Ubiquiti drops support for the Gateway I bought, it looks like it'll go straight to e-waste.

But my main goal was to test if I set up everything from scratch without connecting the Cloud Gateway to the Internet, and never connect any sort of Ubiquiti account to the hardware at all. And I could!

## The Build

For a detailed look at this build (and more reasoning behind the components), watch this video:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/qclCCQeg-RQ' frameborder='0' allowfullscreen></iframe></div>
</div>

But here are all the components of the build (I've linked to Micro Center since they were all in stock, but you could purchase direct from Ubiquiti if you're not near a Micro Center):

  - [UniFi Cloud Gateway Fiber](https://www.microcenter.com/product/695361/ubiquiti-cloud-gateway-fiber)
  - [UniFi Flex 2.5G PoE](https://www.microcenter.com/product/695379/ubiquiti-flex-25g-poe-8-port-poe-compliant-managed-network-switch-(psu-not-included))
  - [Ubiquiti 210 Watt AC Power Adapter for PoE Switch](https://www.microcenter.com/product/697310/ubiquiti-210-watt-ac-power-adapter-for-poe-switch)
  - [UniFi 5G Backup](https://www.microcenter.com/product/712077/ubiquiti-unifi-5g-backup)
  - [U7 Lite](https://www.microcenter.com/product/692982/ubiquiti-unifi-u7-lite-compact-ceiling-mounted-wifi-7-access-point)
  - [APC UPS BE600M1](https://www.microcenter.com/product/647002/apc-battery-backup-and-surge-protector-ups-(be600m1))

I used some extra patch cables I had laying around for the Ethernet connections, but did add on an extra DAC cable since the Ubiquiti DACs are either too short or much too long for this particular setup. Here's the DAC I'm using, and it's all getting mounted inside a RackMate TT:

  - [DeskPi RackMate TT](https://amzn.to/4cgPkrL)
  - [2' Twinax DAC (for 10Gbps Uplink)](https://amzn.to/4y6Y9Nn)

Ubiquiti doesn't make any 10" / mini rack mounting hardware, so most people resort to 3D printing as an upgrade over placing components on rack shelves. It's a hard requirement for my setup, because portability means rigid mounts for everything. I don't want a switch sliding out while I'm lugging the mini rack!

To make the prints as durable and sag-resistant as possible—and also self-extinguishing for a little extra safety—I tried printing them out of [Prusament PETG V0](https://www.prusa3d.com/product/prusament-petg-v0-jet-black-1kg-nfc/)... that turned out okay with a lot of filament drying and tuning for two of the mounts... but I had failure after failure printing the switch enclosure:

{{< figure
  src="./prusament-petg-v0-spaghetti-minirack-print.jpg"
  alt="Prusament PETG V0 Spaghetti Print"
  width="700"
  height="auto"
  class="insert-image"
>}}

V0 is notoriously stringy, and no matter how I tuned things, it would glob up on the nozzle and eventually start touching the printed part. As it got taller and on one side, only narrowly supported, the glob would knock off part of the print... and then spaghetti was the result. I think I would design this print to have a little more cross-bracing on the long sides, as even my Bambu P1S had trouble with regular ol' PLA on this print!

Anyway, here are links to all the other 3D printed rackmounts:

  - [Cloud Gateway Fiber 10" Rackmount](https://www.printables.com/model/1235928-unifi-ucg-fiber-10-inch-rack-mount)
  - [Cloud Gateway Fiber M.2 SSD Tray:](https://www.printables.com/model/1365302-m2-ssd-tray-for-unifi-cloud-gateway-fiber)
  - [Flex 2.5G 8 PoE 10" Rackmount](https://makerworld.com/en/models/2037862-unifi-flex-2-5g-8-poe-10-inch-rack-mount)
  - [U7 Lite 10" Rackmount](https://cults3d.com/en/3d-model/gadget/unifi-u7-lite-10-rack-mount-oounnameoo)
  - [Ubiquiti 210W Power Supply Rackmount](https://www.printables.com/model/1816999-unifi-210w-ac-power-adapter-mini-rackmount)

The Ubiquiti 210W power supply is rather large, and I couldn't find a way to origami it inside the 3U RackMate TT, so I designed a blanking panel that hard-mounts it on the rear, using the wall mount bracket that comes with the power supply.

## A mini network rack

With all the 3D prints sorted, everything is hard-mounted and ready for travel. I cut a few blocks of foam to support everything inside during travel, and as long as I unplug the cables and remove the top handles, it fits nicely in my standard carry-on luggage bag:

{{< figure
  src="./ubiquiti-mini-rack-in-carry-on-luggage.jpeg"
  alt="Ubiquiti Mini Rack inside Carry-on luggage"
  width="700"
  height="auto"
  class="insert-image"
>}}

I brought the rack with me to and from Columbus, OH, and used it along with the 5G Backup stick in lieu of hotel WiFi.

And after spending [far too long debugging why I only got 4G LTE speeds with the U5G-Backup on my AT&T SIM](https://www.jeffgeerling.com/blog/2026/unifi-u5g-backup-debugging/), I realized the hotel had a wired Ethernet jack with 500 Mbps symmetric bandwidth available!

The hotel's WiFi would only give me 30-40 Mbps, but the wired connection seemed to give me the full connection. So I plugged that into WAN1 on the back of the Cloud Gateway Fiber, and switched to that for primary Internet.

The flexibility of the little setup was working exactly as intended, but I still wanted to see how _true_ 5G connectivity would perform.

So I tested the [UniFi 5G Max](https://www.microcenter.com/product/705381/ubiquiti-unifi-5g-max), which is a more full-featured 5G modem (with dual-SIM, better antennas, a touchscreen status display, etc.), and was getting speeds in excess of 500 Mbps down _inside_ the Columbus, OH Micro Center:

{{< figure
  src="./unifi-5g-max-500mbps-in-mc.jpg"
  alt="UniFi 5G Max with over 500 Mbps bandwidth in Micro Center"
  width="700"
  height="auto"
  class="insert-image"
>}}

When I got back to St. Louis, I did a little more digging on the UniFi 5G modems. Apparently they only work with UniFi's networking, you can't plug one into a generic router and use it as a separate WAN.

That was a bit disappointing, especially for the 5G Max which costs over $400. Since I'd like a redundant 5G connection at the studio (where I run OPNsense, not Ubiquiti), I'm now looking at a [Pepwave 5G Adapter](https://crosstalkmobile.com/collections/routers/products/pepwave-5g-adapter), since it _looks_ like it works with anything.

## Conclusion

Before getting into this build, I knew the meme of people buying one UniFi switch or gateway since it meets their needs... then a few years later their entire homelab is laden in [hues of UniFi grey and white](https://www.reddit.com/r/Ubiquiti/comments/1oqk7m4/accidentally_built_a_home_lab_instead_of_a_simple/).

I don't blame anyone for going that way; Ubiquiti has a complete ecosystem at this point with anything from physical security, environment monitoring, routing, data storage, etc., and all the equipment I've tried is at least competent.

Personally, I'm not migrating from OPNsense and my hodge-podge studio network. But I will get some use out of the mobile carry-on-sized UniFi mini rack.

{{< figure
  src="./unifi-mini-rack-with-xserve-g5.jpeg"
  alt="UniFi mini rack on workbench with Xserve G5"
  width="700"
  height="auto"
  class="insert-image"
>}}

Right now it's running on my workbench next to an old Xserve G5 and a TrueTime XL GPS time server, which I'm prepping for VCF Midwest!
