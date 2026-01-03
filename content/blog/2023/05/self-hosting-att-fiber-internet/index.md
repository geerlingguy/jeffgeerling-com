---
nid: 3284
title: "Self-hosting with AT&T Fiber Internet"
slug: "self-hosting-att-fiber-internet"
date: 2023-05-08T20:48:02+00:00
drupal:
  nid: 3284
  path: /blog/2023/self-hosting-att-fiber-internet
  body_format: markdown
  redirects: []
tags:
  - at&t
  - fiber
  - homelab
  - internet access
  - isp
  - router
  - self-hosted
---

Today I got AT&amp;T Fiber Internet installed at my house, and I thought I'd document a few things I observed during and after the install.

They trenched fiber boxes between pairs of houses in my neighborhood. It seems like they have little fiber hubs for 8 houses in a set, and those little hubs connect back to the main neighborhood box with an 8 or 10-strand cable, directly buried in the ground.

Apparently my street's main run was kinked somewhere, and only one of the strands had full signal, so I'm the lucky winner who signed up first, and I get that fiber until they run a new cable underground :)

{{< figure src="./bgw320-att-internet-gateway-fiber.jpg" alt="BGW320 AT&amp;amp;T Internet Gateway - Fiber" width="700" height="518" class="insert-image" >}}

The AT&amp;T tech (who was great!) installed an [NBS AT&amp;T BGW-320 500 Fiber Gateway](https://amzn.to/3NM9puv), and on the back I spied an SFP port... which unfortunately is used for the fiber connection, so I couldn't just use a [DAC](https://www.fiber-optic-solutions.com/dac-cable.html) between my router and this box.

Instead, I plugged the blue 5 Gbps port into my router's WAN port, and logged into the BGW320-500's admin UI (which is available at http://192.168.1.254).

I wanted the IP address AT&amp;T assigns (which is dynamic unless you add on [Static IP addresses starting at $15/month](https://www.att.com/support/article/u-verse-high-speed-internet/KM1002300/)) to be passed through to my own router, so I went to Firewall &gt; IP Passthrough, then I set 'Allocation Mode' to 'Passthrough', 'Passthrough Mode' to 'DHCPS-fixed', and then pasted in the MAC address of my existing router WAN interface.

I saved those changes, and immediately had Internet through my existing router, and checked `icanhazip.com`, grabbed the IP, ran it through `traceroute` to confirm there wasn't any extra NAT layer anymore, and then set that IP for all my self-hosted services, like [my self-hosted PiVPN instance](/blog/2023/build-your-own-private-wireguard-vpn-pivpn) and my [Raspberry Pi Dramble](http://pidramble.com) website.

In the future, I may tweak settings a bit more if I find the AT&amp;T Gateway device interfering with performance much (it seems to have its own layers of packet filtering and firewall that may still be touching the packets...).

A few other quick notes:

  - When they do the install, the tech seems to do the 'cable from the box to your house to your gateway location' install, but if you have buried cable, another crew comes later to bury the actual fiber outside the house
  - The whole install for a house that never had fiber took about 2.5 hours (friends in the neighborhood say it varied between 1-3 hours, depending on the complexity of the install).
  - I'm paying $80/month for 1 Gbps symmetric speed now. I was paying $135/month for 1 Gbps down, 40 Mbps up with Spectrum. Good riddance.
  - Currently I'm only measuring 550 Mbps down and 650 Mbps up, tested via 10 Gbps internal LAN and WiFi 6E network right next to my AP. Will continue [monitoring my Internet connection with my Raspberry Pi](/blog/2021/monitor-your-internet-raspberry-pi) to see if that changes over time.
  - My Raspberry Pi running Wireguard / PiVPN now gives me about 300 Mbps up and down (was previously limited to 35 Mbps up and down due to the slow upload speed on Spectrum!).

If you have any additional ideas or experience with self-hosting behind AT&amp;T Fiber, let me know! I'm just happy to be paying _half as much_ as I was for Charter/Spectrum coax, but getting _more than 20x faster upload speeds_ :)

**Update**: After [investigating the slow speeds a bit](https://twitter.com/geerlingguy/status/1655756265551806464), I found out I had enabled QoS for bandwidth limiting on my guest network at some point—that resulted in my poor ASUS RT-AX86U processing so many packets the CPU would overload full-tilt, leading to lower overall performance (even on the main wired Ethernet network). After disabling that, I am [getting a full 936 Mbps up and down](https://www.speedtest.net/result/14711702972)—the limit of what you can expect over 1 Gbps networking:

{{< figure src="./speedtest-gigabit-att-fiber-14711702972.png" alt="Speedtest.net Gigabit AT&amp;amp;T Fiber on ASUS RT-AX86U" width="350" height="187" class="insert-image" >}}

Now I'm sorta hoping I can eke out a little more performance if I upgrade to a dual 2.5G router...
