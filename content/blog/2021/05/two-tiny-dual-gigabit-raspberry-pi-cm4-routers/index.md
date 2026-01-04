---
nid: 3102
title: "Two Tiny Dual-Gigabit Raspberry Pi CM4 Routers"
slug: "two-tiny-dual-gigabit-raspberry-pi-cm4-routers"
date: 2021-05-28T14:41:36+00:00
drupal:
  nid: 3102
  path: /blog/2021/two-tiny-dual-gigabit-raspberry-pi-cm4-routers
  body_format: markdown
  redirects:
    - /blog/2021/two-tiny-new-dual-gigabit-raspberry-pi-cm4-routers
aliases:
  - /blog/2021/two-tiny-new-dual-gigabit-raspberry-pi-cm4-routers
  - /comment/17679
tags:
  - cm4
  - compute module
  - dfrobot
  - networking
  - raspberry pi
  - router
  - seeed
  - video
  - youtube
---

Since I started testing various [PCI Express cards on the Raspberry Pi Compute Module 4](https://pipci.jeffgeerling.com), I've been excited to see what new kinds of custom networking devices people would come up with.

Well, after months of delays due to part shortages, both DFRobot and Seeed Studios have come out with their 2-port Gigabit router board designs, and I was happy to receive a sample of each for testing:

{{< figure src="./dfrobot-seeed-router-board-iot-mini-carrier-dual-gigabit-ethernet-boards.jpeg" alt="DFRobot and Seeed Studios Router Boards with Dual Gigabit Ethernet" width="600" height="400" class="insert-image" >}}

The boards are tiny, and even with the Compute Module 4 installed, they are incredibly small—take a look at the entire assembled DFRobot unit, complete with a Raspberry Pi attached:

{{< figure src="./dfrobot-tiny-router-raspberry-pi-cm4-quarter-size-comparison.jpeg" alt="DFRobot CM4 IoT Router Board with Raspberry Pi CM4 and Quarter" width="600" height="400" class="insert-image" >}}

These boards are a huge upgrade from any typical Pi 4 model B multi-port router solution, since you not only have half the required device footprint, you also get two ports side-by-side and don't need an extra USB Gigabit network dongle hanging off a USB 3.0 port!

Plus, with the freedom to access the Pi's x1 PCI Express lane directly, DFRobot's board attaches the second Gigabit NIC _directly_ to the bus, instead of through a USB 3.0 controller, like Seeed Studios did. Look at the benchmarks further down this post to see what kind of difference that architecture shift made.

I have an [entire video dedicated to reviewing these two tiny router boards](https://www.youtube.com/watch?v=w7teLVwi408) on my YouTube channel, but I'll provide a top-level summary and the benchmarks in this post.

<p style="text-align: center;">
<a href="https://www.youtube.com/watch?v=w7teLVwi408">{{< figure src="./jeff-holding-dfrobot-dual-gigabit-router-board-cm4.jpeg" alt="Jeff Geerling holding Raspberry Pi Compute Module 4 based DFRobot router board mini" width="500" height="334" class="insert-image" >}}</a><br>
<em>It really is a tiny router! Click the image to see the full video review of these boards.</em></p>

## OpenWRT on the tiny CM4

OpenWRT is about to release a new version compatible with the Pi 4—but that doesn't mean everything will work perfectly on the _Compute Module 4_ out of the box.

DFRobot offers a [customized OpenWRT image download](https://wiki.dfrobot.com/Compute_Module_4_IoT_Router_Board_Mini_SKU_DFR0767#target_3) on their Wiki, but Seeed does not. Currently, for the Seeed board, you have to manually compile a version of OpenWRT to work with the LAN7800 USB to Ethernet bridge chip on the board. That is, unless [this pull request](https://github.com/openwrt/openwrt/pull/4191) gets merged in someday.

With Pi OS, both boards will work out of the box with both ports, but then you'd have to set up all the routing functionality by hand.

I was able to get all OpenWRT's functionality working well, though to get WiFi working, I had to employ a few [hacky workarounds](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/137#issuecomment-847276278). WiFi Access Point performance using the built-in 802.11ac chip over SPI is not amazing, though—I could only route around 60 Mbps through the Pi under ideal conditions.

I'm hoping to build a better Pi WiFi 6E router [using Intel's AX210 chip](https://pipci.jeffgeerling.com/cards_network/intel-ax210-wifi-6e.html), but that's a project for later this year!

## Benchmarks

I ran three simple benchmarks to get a feel for the performance of the two boards—and the main thing I wanted to test was whether either would bottleneck a gigabit network connection. The major difference was the architecture of the second Gigabit adapter. The first adapter on each board is supplied by the built-in Broadcom gigabit NIC on the Compute Module itself, but the second one is routed through the Pi's PCI Express bus.

  - For the Seeed board, there is a USB 3.0 chip on the PCI Express bus, and a Microchip LAN7800 USB to Gigabit Ethernet NIC on that bus.
  - For the DFRobot board, there is a Realtek 8111h Gigabit NIC _directly_ attached to the PCIe lane.

How much of a difference does that make? Well, it's pretty noticeable:

{{< figure src="./bandwidth-and-throughput-dfrobot-seeed-router-boards.jpeg" alt="Bandwidth and throughput graphs showing DFRobot and Seeed Raspberry Pi Compute Module 4 Router Boards" width="672" height="378" class="insert-image" >}}

_Testing method and full results in these GitHub issues: [DFRobot board](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/114), [Seeed board](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/137)._

On the Seeed board, the overhead of the USB 3.0 bus and hardware and driver limitations cause interrupts to stall on one CPU core (as measured by `atop`), and the router can't put through more than around 700 Mbps.

On the DFRobot board, I didn't see any indication the CPU was getting overloaded even under longer stress tests with a full gigabit of data going through.

And that overhead is most apparent when sending through small packets—using `hping`, the Seeed board could only handle _half_ the packets per second of the DFRobot board.

Power consumption offers a similar story: the DFRobot board (which, admittedly, has many fewer features and I/O to support!) uses half the power as the Seeed board:

{{< figure src="./power-consumption-seeed-dfrobot-router-boards.jpeg" alt="Power consumption of Seeed and DFRobot CM4 router boards" width="672" height="378" class="insert-image" >}}

Under 2W at idle is pretty respectable for a full gigabit router!

## Conclusion

These little routers aren't for everyone. If you're passionate about networking and are familiar with the basics, they're a fun way to build a reasonably-performant network router without breaking the bank.

You can buy them from their respective stores:

  - [DFRobot CM4 IoT Router Carrier Board Mini](https://www.dfrobot.com/product-2242.html)
  - [Seeed Dual Gigabit Ethernet Carrier Board for CM4](https://www.seeedstudio.com/Rapberry-Pi-CM4-Dual-GbE-Carrier-Board-p-4874.html)

They each have their own limitations, and I'm also looking forward to testing out a more full-featured (and full-priced!) Compute Module 4-based router I'm building with Dual-2.5 Gbps router _with_ WiFi 6E as I mentioned earlier. Stay tuned and [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) or [this blog's RSS feed](/blog.xml) if you don't want to miss it!
