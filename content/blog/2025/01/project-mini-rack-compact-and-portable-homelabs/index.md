---
nid: 3434
title: "Project Mini Rack - compact and portable homelabs"
slug: "project-mini-rack-compact-and-portable-homelabs"
date: 2025-01-17T14:59:20+00:00
drupal:
  nid: 3434
  path: /blog/2025/project-mini-rack-compact-and-portable-homelabs
  body_format: markdown
  redirects:
    - /blog/2025/project-mini-rack
    - /blog/2025/project-mini-rack-compact-and-portable-racks
aliases:
  - /blog/2025/project-mini-rack
  - /blog/2025/project-mini-rack-compact-and-portable-racks
tags:
  - community
  - github
  - homelab
  - mini
  - open source
  - rack
  - video
  - youtube
---

{{< figure src="./mini-rack-jeff-geerling-pointing.jpeg" alt="Jeff Geerling Project Mini Rack" width="700" height="394" class="insert-image" >}}

Today I'm announcing [Project MINI RACK](https://mini-rack.jeffgeerling.com), an open source project to help those building homelabs, RF/wireless rigs, and other electronics projects into mini 10" racks.

{{< figure src="./mini-racks-001-002.jpeg" alt="Mini Rack 001 and 002 by Jeff Geerling" width="700" height="394" class="insert-image" >}}

Not everyone can afford (either due to budget or space constraints) to have a full 19" rack in their home. Besides that, people may want to deploy small, easily-composable equipment racks to remote sites, or have one in the car that they can take anywhere! And with the flood of Mini PCs in the market (in addition to SBCs and small PoE-powered network devices), and the move to solid state storage, a mini rack can hold a formidable amount of resources.

The [r/minilab](https://www.reddit.com/r/minilab/) subreddit is probably the largest nexus of mini rack enthusiasts—and Project MINI RACK doesn't aim to supplant that. But I would like to have a central resource for 10" rack mount equipment, racks, and compatibility testing.

{{< figure src="./mini-rack-in-big-rack.jpeg" alt="Mini Rack in big rack" width="700" height="394" class="insert-image" >}}

Not all equipment that fits within the 10" rack dimensions makes sense in a mini rack. And some equipment that _shouldn't_ make sense works great! But discovering what works and what doesn't can be a long and expensive journey. One of the great benefits of a mini rack is you can _save_ money not having to buy 'full size' rackmount equipment, which is often sold at a premium compared to standard desktop equipment. But you have to know the right equipment to buy.

Besides listing [mini racks](https://mini-rack.jeffgeerling.com/#racks), [PDUs](https://mini-rack.jeffgeerling.com/#pdus), [UPSes](https://mini-rack.jeffgeerling.com/#upses), [drive trays](https://mini-rack.jeffgeerling.com/#disk-shelves), [SBC mounts](https://mini-rack.jeffgeerling.com/#sbc-shelves), [mini PC mounts](https://mini-rack.jeffgeerling.com/#mini-pc-server-shelves), [mini network switches](https://mini-rack.jeffgeerling.com/#network-gear), etc., I am adding a [Build Showcase](https://mini-rack.jeffgeerling.com/#build-showcase), and to kick things off, I built three unique mini racks, and documented them in detail:

## Mini Rack 001

{{< figure src="./mini-rack-001.jpeg" alt="Mini Rack 001" width="700" height="394" class="insert-image" >}}

I wanted to build a mini rack that could be picked up and transported with zero downtime. It has a UPS on the bottom that provides 3-4 hours of battery backup, can be recharged in 2 hours, and even has a DC solar input, so you can keep it running off a portable solar panel! (Though in my late-winter-day testing I could only get 11W through USB-C on my 45W foldable solar panel... I need to re-test in the spring.)

All the devices are powered via PoE, and I will eventually have everything hard-mounted for rugged durability (right now the Sherpa UPS is loose in the bottom, so if you shake it around like in a moving vehicle, it will likely fall out).

Full parts list (I earn for qualifying purchases—some links are Amazon affiliate links):

  - [DeskPi RackMate T0](https://amzn.to/4gNGT7t): $110
  - [LabStack Mini 2U Rackmount Kit (metal plate + 3D modules)](https://github.com/JaredC01/LabStack): $100 (approx)
  - [2x Raspberry Pi 5 8GB](https://www.raspberrypi.com/products/raspberry-pi-5/): $160
  - [1x Raspberry Pi 4 8GB](https://www.raspberrypi.com/products/raspberry-pi-4/): $75
  - [WisdPi PoE+ 5G HAT](https://www.wisdpi.com/products/wp-nh5000p): $50
  - [HackerGadgets PoE+ NVMe HAT](https://pipci.jeffgeerling.com/hats/hackergadgets-poe-nvme-hat.html): $42
  - [Raspberry Pi PoE+ HAT](https://www.raspberrypi.com/products/poe-plus-hat/): $20
  - [JetKVM](https://jetkvm.com): $69
  - [USB Keystone Passthrough](https://amzn.to/3We8zdy): $8
  - [Cat6A Keystone Passthrough](https://amzn.to/40sSNhl): $14
  - [USB-A to USB-A Jumper Cable](https://amzn.to/40qx3mn): $9
  - [GigaPlus 10-port 2.5G PoE+ Switch](https://amzn.to/4hdznTr): $99
  - [Pelopy Universal Rack Mount Brackets](https://amzn.to/4gQh4Ul): $15
  - [Goal Zero Sherpa 100AC Power Bank](https://amzn.to/40eaccs): $187
  - [60W GaN USB-C PD Charger](https://amzn.to/42soB7J): $28
  - [Monoprice Slimline Ethernet 6" 10 pack](https://amzn.to/4fSqqO3): $22

Total cost (brand new, not including tax/shipping): $1,008

## Mini Rack 002

**NOTE**: Thanks to DeskPi's generosity, I'm giving away this rack, sans the PDU! Details for entering to win are at the end of this blog post.

{{< figure src="./mini-rack-002.jpeg" alt="Mini Rack 002" width="700" height="394" class="insert-image" >}}

My goal for my second rack build was to run a basic mini Pi cluster, targeting a lower price with 1 Gbps networking and USB-C power. Using DeskPi's Pi 5 NVMe 2U mounting bracket, I can have a 4-node Pi cluster with NVMe SSD storage, and USB-C power delivery. I added on a 10" rack PDU on the back, to keep power organized.

Plug in a network jack, and an AC power plug, and away you go!

{{< figure src="./mini-rack-002-tupavco-pdu.jpeg" alt="Tupavco PDU in mini rack 002" width="700" height="394" class="insert-image" >}}

There's a PDU on the back of this rack, but it's just a glorified (and very expensive) power strip. It would be great to see more PDU and UPS options for mini racks—right now the few options that exist are very expensive.

Full parts list:

  - [DeskPi RackMate T0](https://amzn.to/4gNGT7t): $110
  - [DeskPi 2U 4x Raspberry Pi PCIe NVMe Mount](https://amzn.to/427GPee): $100
  - [4x Raspberry Pi 5 8GB](https://www.raspberrypi.com/products/raspberry-pi-5/): $320
  - [260W GaN USB-C Charging Station](https://amzn.to/40tn0wQ): $25
  - [Tupavco 10" Mini Rack PDU](https://amzn.to/425nLxr): $45
  - [1 ft 3 pack USB-C cables (x2)](https://amzn.to/4264tb1): $20
  - [Mikrotik CSS610-8G-2S+in Switch](https://amzn.to/427nOZu): $110
  - [Mikrotik RMK-2/10 Rack Mount Kit](https://amzn.to/3C4yU6T): $15
  - [Monoprice Slimline Ethernet 6" 10 pack](https://amzn.to/4fSqqO3): $22

Total cost (brand new, not including tax/shipping): $767

## Mini Rack 003

{{< figure src="./mini-rack-003.jpeg" alt="Mini Rack 003" width="700" height="394" class="insert-image" >}}

For this rack, I wanted to see how much compute I could cram into 8U. I would likely add on a better network switch, but the idea is to use an external UPS so every rack space can be taken up with compute, while still allowing adequate airflow/cooling.

The two base units are Mini ITX cases from MyElectronics, which don't have room for a full PSU, so you'd likely use a PicoPSU or use boards that take direct 12V power input.

Above that is a mini ITX tray from DeskPi, holding a Raspberry Pi Compute Module 5 ITX board. And above that is another DeskPi tray, this time for dual SBC, which can also mount two 2.5" SSDs or HDDs below for storage.

{{< figure src="./mini-rack-003-itx-case-stick-out-back.jpeg" alt="Mini Rack 003 ITX case sticking out the back" width="700" height="394" class="insert-image" >}}

The Mini ITX cases do stick out in the back a little. If you want to stack multiple racks (or an 8U and 4U), DeskPi actually makes a kit to join them securely. But you'll have to worry about stability, the higher you go! There are some racks from other vendors (notably, NavePoint) that are deeper and/or wall-mountable, which can help with the depth problems.

Full parts list:

  - [DeskPi RackMate T1](https://amzn.to/4jfAaVK): $150
  - [MyElectronics 10" 2U Mini ITX Case x2](https://www.myelectronics.nl/us/10-inch-2u-mini-itx-case.html): $230 ($115 x2)
  - [DeskPi Super6C Clusterboard x2](https://amzn.to/4gRy7pc): $440 ($220 x2)
  - [Raspberry Pi Compute Module 5 8GB x12](https://www.pishop.us/product/raspberry-pi-compute-module-5-wireless-8gb-ram-lite-cm5108000/): $960 ($80 x12)
  - [DeskPi 10" Mini ITX Shelf](https://amzn.to/4fWEYMw): $24
  - [Seaberry Mini ITX board for CM](https://pipci.jeffgeerling.com/boards_cm/seaberry.html): N/A
  - [Nvidia Jetson Nano Developer Kit](https://amzn.to/3CfgG2A): $200
  - [Raspberry Pi 5 - 8GB](https://www.raspberrypi.com/products/raspberry-pi-5/): $80
  - [Netgear GS305P 5-port PoE+ Switch](https://amzn.to/4ajf4BO): $70
  - [DeskPi 12-port Keystone RJ45 0.5U Patch Panel](https://amzn.to/427xXFC): $23
  - [Monoprice Cat6A 10 pack Snagless RJ45 Cables](https://amzn.to/42g9Mor): $17
  - [ECOFLOW River 2 Power Station](https://amzn.to/3Wk0oMH): $220

Total cost (brand new, not including tax/shipping): $2,414

## Other Mini Racks

{{< figure src="./mini-rack-cariboulite-sdr-ham.jpeg" alt="Mini Rack 001 with CaribouLite for SDR Radio" width="700" height="394" class="insert-image" >}}

Pictured above is the closer-to-final form of my Mini Rack 001—my intention is to build a radio-centric mini rack, which I can use for SDR, ADS-B, Meshtastic, that sort of thing. A mini rack is ideal _for me_ because the space limits me to projects I can contain inside the rack. Limitations often lead me to _actually finish a project_ instead of letting it sprawl out over every horizontal surface :)

It's also cool having a rack-mounted, PoE/Battery-powered CaribouLite SDR Pi (that's what the dipole antenna's plugged into), which allows me to transmit and receive anywhere from 30 MHz to 6 _GHz_!

{{< figure src="./jaredc01-mini-rack-front_1.jpg" alt="JaredC01 mini rack front" width="700" height="394" class="insert-image" >}}

JaredC01 (who made the LabStack) has a mini rack (pictured above) with a couple party tricks: the whole thing is powered via PoE++ (using Unify's 65W PoE Injector, or any PoE++ switch). This allows him to place it far from any power outlet, and for Internet access, he can either use Ethernet through the PoE++ cable, or via WiFi or a tethered phone, as he built-in a PoE-powered [GL-iNet GL-A1300](https://www.gl-inet.com/products/gl-a1300/) mini router!

{{< figure src="./jaredc01-mini-rack-back_1.jpg" alt="JaredC01 mini rack back" width="700" height="394" class="insert-image" >}}

On the back, he breaks out two antenna connections from the Radxa X4's u.fl connectors to SMA, so he can mount external WiFi and Bluetooth antennas. Next to it is the PoE++ power and (optional) Ethernet keystone jack, and a USB jack connected to the GL-iNet router, for phone tethering or network storage!

He also adapted [Noctua's 3D printable 120mm quiet fan grill](https://www.printables.com/model/1096961-high-efficiency-noctua-120mm-fan-grill) to two 80mm Arctic fans, and plugged them into USB 5V power on the Radxa so they can move a lot of air while remaining almost silent.

Techno Tim [posted](https://github.com/geerlingguy/mini-rack/issues/11) one of his mini rack builds to Project Mini Rack's [build showcase](https://mini-rack.jeffgeerling.com/#build-showcase). His rack is a self-contained Homelab, complete with two mini monitors and tiny wireless keyboard!

## Video

I published a video going over my first three mini racks, and the project overall—and I also talked to even _more_ makers and homelab enthusiasts about _their_ builds:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/y1GCIwLm3is" frameborder='0' allowfullscreen></iframe></div>
</div>

## Giveaway and Conclusion

Thanks go DeskPi's generosity, I was able to give away 'Mini Rack 002'. The contest is over, so the [entry form](https://docs.google.com/forms/d/e/1FAIpQLSd1548v4R3JmSpoW6BQ-E3WGEUMlxRI_TSCaauL2dR6dOOJiA/viewform) is closed. **Congratulations to Sam J on winning the mini rack**; happy homelabbing! ([Official contest rules](https://www.jeffgeerling.com/2025-sweepstakes-rules))

Check out [Project MINI RACK](https://mini-rack.jeffgeerling.com) and consider building a smaller, more space-efficient homelab today :)
