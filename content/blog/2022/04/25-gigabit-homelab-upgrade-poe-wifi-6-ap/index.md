---
nid: 3197
title: "2.5 Gigabit homelab upgrade - with a PoE+ WiFi 6 AP"
slug: "25-gigabit-homelab-upgrade-poe-wifi-6-ap"
date: 2022-04-13T14:01:44+00:00
drupal:
  nid: 3197
  path: /blog/2022/25-gigabit-homelab-upgrade-poe-wifi-6-ap
  body_format: markdown
  redirects: []
tags:
  - access point
  - netgear
  - network
  - networking
  - qnap
  - upgrade
  - video
  - wifi
  - wifi 6
  - youtube
---

For the past year, I've slowly upgraded parts of my network to 10 Gigabit. But 10 Gigabit switches, NICs, and even cabling is a bit more expensive and sometimes annoying to deal with than the very-cheap 1 Gbps equipment most homelabbers are used to.

I dipped my toes into the 2.5 Gbps waters once I got a NAS with 2.5G ports—you can use standard USB NICs that cost less than $50, or PCIe cards for even less. And cabling is easier, since 2.5G works fine over Cat5e (which I already have run to most of my house).

So in order to install a new WiFi 6 Access Point upstairs—and get it's full bandwidth—I upgraded my main 1 Gbps PoE+ switch to a 2.5 Gbps PoE+ switch.

Looking around at options, most switches with more than 4 2.5 Gbps ports with PoE+ seem to cost upwards of $300. And knowing that I'd like to expand my network a bit in the future, I finally splurged a bit and bought this 20-port monstrosity:

{{< figure src="./DSC06949.jpeg" alt="QNAP 20-port 2.5G 10G PoE+ Managed Switch" width="700" height="467" class="insert-image" >}}

Meet the [QNAP QSW-M2116P-2T2S-US](https://amzn.to/3LxrqZm). It's a 20-port managed switch, with 16 of those ports being 2.5 Gbps PoE+ (perfect for WiFi 6 and WiFi 6E Access Points!), 2 10 Gbps SFP+, and 2 10 Gbps PoE++.

I didn't _need_ all of that yet, but I do imagine WiFi 7 APs—once they're a thing—will require 10 Gbps networking, and will likely require more power than the standard PoE+-based APs that are out today.

Besides, some of my wildest Raspberry Pi testing involves PoE++ at this point, so having it available straight through my main network rack (no PoE++ injector necessary!) may come in handy.

In tandem with the switch upgrade, I also wanted to install a new WiFi 6 AP upstairs, since my existing AP is actually a combo router+AP, the [ASUS RT-AX86U](https://amzn.to/3Dqajpv), and it's located on my network rack, in the basement:

{{< figure src="./asus-rt-ax86u.jpg" alt="ASUS RT-AX86U in basement rack" width="700" height="394" class="insert-image" >}}

Eventually, I'd like to build my own rackmount router/firewall (possibly using a Raspberry Pi), and keep it separate from any wireless access points.

So I ran a new Cat6A cable (which will be more than adequate for PoE++ and 10 Gbps when the time comes for an upgrade), and installed the [Netgear WAX620 AX3600 WiFi 6 AP](https://amzn.to/3iSM9us), powered over Ethernet:

{{< figure src="./netgear-wax620.jpeg" alt="Netgear WAX620 WiFi 6 AP" width="700" height="467" class="insert-image" >}}

I really wanted to go for WiFi 6E, but none of my computers (besides, ironically, a Raspberry Pi Compute Module system I'm testing) has 6E yet, and the $150 _on top_ of the $200 I was spending on this AP just wasn't worth it.

Both the switch and AP have web management UIs, and I was annoyed by my first experience with both:

  - **QNAP**: The preferred method of finding the switch on the network is to run Qfinder Pro, but when I went to install this _200+ MB app_, the required agreement basically asked me to sign over my social security number. I'm not sure why they need so much analytics data for a little utility that scans the network for a MAC address. I just spelunked a bit until I could find the switch on my own, then I brought it onto my main subnet.
  - **Netgear**: The initial setup process really wanted me to sign up for an 'Insight' cloud management portal for 'all my Netgear devices'. That rubs me the wrong way—many people buying these 'low-end enterprise' APs are probably SMBs or 'advanced homelabbers'—pushing them to buy into a $10/month subscription service is a bad look. Everything is easy enough to manage in the web UI, but it's not immediately obvious that's even an option!

Initial setup aside, everything in the web UI for both QNAP and Netgear was intuitive and worked well in both Firefox and Safari. I especially liked the live power consumption monitoring on the PoE switch:

{{< figure src="./poe-consumption-monitoring-qss.jpg" alt="QNAP QSS PoE monitoring table" width="700" height="394" class="insert-image" >}}

All in all, the network upgrade was a success, as I more than doubled the bandwidth both near the router at my upstairs desk (green bar) and at the furthest point upstairs (blue bar):

{{< figure src="./wifi-6-performance-downstairs-asus-upstairs-netgear.jpg" alt="WiFi 6 performance downstairs and upstairs with APs" width="700" height="394" class="insert-image" >}}

Now that I have a nicer dedicated AP, I'm also planning on segregating more of my network, so devices like the little [ESP8266 DIY Air Quality Monitors](/blog/2021/airgradient-diy-air-quality-monitor-co2-pm25) I have running aren't on the same network as my NAS or main computers.

The upgrade also means _every_ device and port in my house is a minimum of 2.5 Gbps, so as I upgrade the rest of my computers over the next few years, file transfers will hum along at 250+ MB/sec instead of the 119 MB/sec I've been used to.

Not that anyone besides me cares in my household—the only time anyone else notices the network at all is if Berenstain Bears stops streaming off the NAS in the middle of a show—but it's nice to have the upgrade :)

If you want to see the whole upgrade process, check out the video on my YouTube channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/LDflrf85h9Y" frameborder='0' allowfullscreen></iframe></div>
</div>
