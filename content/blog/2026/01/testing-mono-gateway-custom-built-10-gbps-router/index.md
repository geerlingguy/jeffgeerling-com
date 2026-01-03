---
date: '2026-01-02T09:12:25-06:00'
tags: ['mono','gateway','router','openwrt','linux','servethehome','youtube','video','networking']
title: 'Testing the Mono Gateway, a custom-built 10 Gbps Router'
slug: 'testing-mono-gateway-custom-built-10-gbps-router'
---

{{< figure
  src="./mono-gateway-router-hero.jpeg"
  alt="Mono Gateway"
  width="700"
  height="auto"
  class="insert-image"
>}}

Last month, the stars aligned for me to bring the [Mono Gateway](https://mono.si) (a 10 Gbps router that YouTuber [Tomaž Zaman](https://www.youtube.com/@tomazzaman) and his team at Mono built from scratch) on a trip to Phoenix, and test it with one of the most OP network test boxes I've ever seen, at the [ServeTheHome](https://www.servethehome.com) HQ.

In this video, Patrick (from STH) and I put Gateway through a real-world torture test using CyPerf:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/3D5q3NWEMZY' frameborder='0' allowfullscreen></iframe></div>
</div>

## Mono Gateway

The Gateway is a small (1U/desktop) router with features like a 4-core Arm CPU, 8GB of ECC LPDDR RAM, and decent expansion options for a compact router.

{{< figure
  src="./mono-gateway-ports.jpg"
  alt="Mono Gateway - Network Ports"
  width="700"
  height="auto"
  class="insert-image"
>}}

On the back (or front, depending on your perspective), it has:

  - USB-C PD power input (the unit comes with a 65W GaN power supply)
  - USB 3.0 Type C port
  - USB-C UART
  - 3x 1 Gbps RJ45 ports
  - 10 Gbps SFP+ WAN port
  - 10 Gbps SFP+ LAN port

It comes preconfigured with OpenWRT, and just as of this month, hardware offload on the NXP SoC is supported, so it _should_ be able to hit 10 Gbps speeds on each port. We'll test that later.

Internally there are extra fan headers, an M.2 slot (I believe E-key for WiFi), and some other odds and ends I haven't tested.

The preliminary developer edition is CNC machined out of aluminum, with a nice finish and a clear plastic top. It is solid, and has threaded holes along edges so you could build your own rackmount ears for it (my test unit did not come with any).

There's a blindingly-bright NeoPixel LED for status on the top front, and the first batch of units will include a [mirror so you can see under-mount status LEDs too](https://www.youtube.com/watch?v=P1nH77ieYnU) (my test unit did not come with one).

Finally, when it powers up, the fan on top of the SoC briefly runs at 100% speed (which is audible and would be annoying if left there), but then spins down to the point it is nearly silent.

I should mention, the unit I have been testing was sent by Tomaž and his team at Mono, I did not pay for it. But prior to that, I had also placed a reservation for a dev unit, which I eagerly await for testing at home!

## STH's 1.6 Tbps CyPerf Test Server

Here at the studio, I have a 100 Gbps network switch, but my fastest network device (my NAS) is only running at 25 Gbps. Everything else is 1, 2.5, or 10 Gbps.

I've never done _routing_ tests beyond 2.5 Gbps, and though I could probably whip something together to at least explore the bandwidth limits for raw packets at 10 Gbps, I wasn't confident I could test a real-load workload through the Gateway.

_Luckily_, I was already scheduled to visit Phoenix to visit their new Micro Center... and since Patrick from ServeTheHome was going to be around, I gave him a call. We met up, and I got to test the Gateway on his [$1 million Keysight Cyperf 1.6 Tbps network test server](https://www.servethehome.com/looking-for-feedback-on-next-gen-sth-network-device-testing-keysight-cyperf-ubiquiti/)!

{{< figure
  src="./servethehome-cyperf-test-server.jpg"
  alt="ServeTheHome CyPerf test server - rear"
  width="700"
  height="auto"
  class="insert-image"
>}}

This test server is a dual-Xeon setup with 1.5 TB of RAM, Hundreds of PCIe Gen 5 lanes, and almost everything is dedicated to pumping bits through network IO.

On the rear there are NICs ranging from 10 Gbps (technically, 4x 50 Gbps) to 800 Gbps (courtesy of NVIDIA ConnectX-8 cards), giving the full box a switch/router-testing capacity of 1.6 Tbps!

It runs a (very expensive) real-world network load test application from Keysight called [CyPerf](https://www.cyperf.com), which is leagues beyond basic `iperf` throughput testing, which is exactly why I wanted to test the Gateway on it.

We didn't use this feature, but the dual-400 Gbps ConnectX-8 cards needed 32 PCIe Gen 5 lanes. Apparently few server platforms have the hardware laid out for easy access to _twice_ the normal lane allotment per card, so they had to make custom PCIe cables to steal lanes from NVMe connections on the front of the system to make it all work! It's no wonder Patrick was so excited showing off that system.

## Testing Gateway to the Limit

We plugged the SFP+ WAN and LAN ports directly into the CyPerf machine, and ran through two gauntlets, testing the throughput to the limit. Here's the test setup:

{{< figure
  src="./mono-gateway-on-cyperf-server-dual-10gbps-test.jpeg"
  alt="Mono Gateway on CyPerf Network test server"
  width="700"
  height="auto"
  class="insert-image"
>}}

How did it perform? I'll leave full details to the video embedded earlier in the post, but in a word: _very good_. Some vendors advertise 10 Gbps routing, but only hit half of that (or worse!). The Mono team did a good job ensuring hardware offload works and is supported in their default OpenWRT install.

The box was putting through 17+ Gbps of Layer 4/7 traffic, and 18+ at Layer 2/3, with loads varying between 1-1,000 users and over 15,000 connections. Between two test runs, we measured 850,000 to 1,100,000 packets per second of real-world HTTP throughput:

{{< figure
  src="./mono-gateway-keysight-cyperf-result.jpg"
  alt="Mono Gateway Keysight CyPerf Result - HTTP Gateway Mix"
  width="700"
  height="auto"
  class="insert-image"
>}}

Patrick was impressed, and said it performs admirably for a 10 Gbps router. I agree!

I was able to get that hardware offload support added in _just_ before the test—initially, Tomaž said [they wouldn't be able to pay for the hardware offload support](https://www.youtube.com/watch?v=GpmvINa-xhY) for the initial developer batch. Apparently that feature is a paid addon for NXP's networking SoCs. Luckily, Mono was able to pay for a license and will now enable it out of the box on all the developer units.

{{< figure
  src="./mono-gateway-htop-hardware-offload.jpg"
  alt="Mono Gateway - hardware offload during test run showing CPU usage low"
  width="700"
  height="auto"
  class="insert-image"
>}}

This is a screenshot of `htop` taken on the device (via SSH on my Mac) during one of the CyPerf runs. You can see the only thing taking up CPU cycles is the OpenWRT monitoring side of things; the nearly 20 Gbps of network traffic is not impacting the CPU side barely at all.

## More info on Gateway

It seems like the initial batch of Gateway developer units may be accounted for, but you can still place a preorder on the [Mono website](https://mono.si). It seems like the first 1,000 units are first-come, first-served.

I really hope they'll get the funding (and keep the motivation) to produce a second batch, or to go to full production, after they finish shipping the first 1,000 Gateways. It's more of a niche product, as many homelabbers don't even have _1_ Gbps of Internet bandwidth, much less 2.5, 5, or 10... but as someone who always appreciates a little extra capacity, and already uses OpenWRT in many places, I've enjoyed my time using Mono's Gateway so far.
