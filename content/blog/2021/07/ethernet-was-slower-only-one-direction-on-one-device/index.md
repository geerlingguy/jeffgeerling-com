---
nid: 3116
title: "Ethernet was slower only in one direction on one device"
slug: "ethernet-was-slower-only-one-direction-on-one-device"
date: 2021-07-09T21:03:07+00:00
drupal:
  nid: 3116
  path: /blog/2021/ethernet-was-slower-only-one-direction-on-one-device
  body_format: markdown
  redirects:
    - /blog/2021/ethernet-slower-only-one-direction-on-one-device
aliases:
  - /blog/2021/ethernet-slower-only-one-direction-on-one-device
tags:
  - 10 gbps
  - ethernet
  - mikrotik
  - network
  - networking
  - sfp
  - transceiver
---

{{< figure src="./mikrotik-cloud-router-switch-flypro-fiber-rj45-copper-transceiver.jpeg" alt="MikroTik Cloud Switch Router with FlyPro Fiber Copper RJ-45 10G Transceiver" width="600" height="348" class="insert-image" >}}

There could be a thousand reasons something like this happens, but here's my situation:

A few months ago, when I was testing [10 Gigabit networking on the Raspberry Pi](https://www.youtube.com/watch?v=FTP5h9jnVx0), I noticed something funny when I was doing `iperf3` speed tests between devices connected through my [MikroTik CRS305](https://amzn.to/3hsrYDp) 10G switch.

The switch uses SFP+ jacks, and so I was testing a variety of connections—SFP+ to duplex fiber, SFP+ to RJ-45 copper, and SFP+ DAC (Direct Attach Cable) cables. One thing I found very strange was that _sometimes_, I would get in a situation where a particular device (Pi, my Mac, a Windows PC, or even my NAS) would get the full expected speed in _one_ direction (e.g. my Mac to the NAS), but then if I tested it in reverse (NAS to my Mac), I would get horrible speeds—but only if I was using a 2.5 Gbps NIC on one end.

In the case of the NAS, which has 2.5G Ethernet, I was getting between 50 and 500 Mbps to it, with no consistency in the throughput.

I tested with multiple NICs, I tested both ports of my NAS, and I tested with multiple known-working-to-10G Cat6 patch cables.

And in every case, I was getting this asymmetric speed.

Eventually I bought a [QNAP QSW-M2108-2C](https://amzn.to/3qXS7gy) switch instead, which has 8 built-in 2.5G RJ-45 jacks, and 2 dual-mode SFP+/Copper 10G interfaces.

I plugged everything into it, forgoing fiber or DACs, and the problem went away.

So I shelved the MikroTik switch for the time being.

## More MikroTik, More Problems?

Then a few weeks ago, a viewer of my YouTube channel offered me a [MikroTik CRS309](https://amzn.to/3xyaivI) switch for a song, so I had to take him up on the offer. I swapped it into my rack, and... exact same issue!

Thinking there's no possible way _both_ MikroTik units could make one port work poorly at random, I finally ordered a new batch of RJ-45 transceivers, and started swapping _them_ out (after going through the whack-a-mole with cables and devices to no avail).

And I found, after all that testing, that the [FLYPROFiber SFP-10G-T-30M](https://amzn.to/3wzB2ut) transceivers—at least _some_ revisions—had trouble when a device negotiated 2.5G speeds through it.

{{< figure src="./flypro-fiber-transceiver-fixed.png" alt="FLYPRO Fiber copper transceiver shows as multi-mode fiber" width="721" height="96" class="insert-image" >}}

As can be seen above, the FLYPRO transceivers were being identified as "multi-mode fiber", which also seemed suspect, since they are, indeed, copper RJ45 transceivers!

When connected through one of these, I'd get 2.3 Gbps one way, but the other direction would bottleneck at less than 500 Mbps, which was really horrible for editing video and backups to my NAS.

## It was the Transceiver, dummy!

So yeah, when you're diagnosing network problems, don't leave any stone unturned. In my case, I was using a transceiver that I'd tested and had working with 2.5 and 10G devices, but in some cases, for some reason, it would only work one way.

Switching to MikroTik's own [S+RJ10 transceiver](https://amzn.to/3hqzAXc) resulted in full 2.3 Gbps bidirectional throughput.

I'm reminded of a time earlier this year when one of my Macs was getting 100 Mbps sometimes, and 10 Gbps others, seemingly depending on the direction the wind was blowing. In that case, it turns out one of the 8 wires in one keystone jack was rubbing against the shielded keystone casing, and causing the entire cable run to downrate to 100 Mbps... but only sometimes.

Always start with the patch cables. Then look at your equipment. Then check your drivers and device CPU/statistics. Then check transceivers, then jacks, terminations, and finally cabling. Networking can be... fun.

While this may not have been the _direct_ cause, [engrpiman2's post on Ars Technica](https://arstechnica.com/civis/viewtopic.php?p=38769733#p38769733) was what finally jostled my brain to think to swap transceivers. Not everything that's 10G will also work well with 2.5G and 5GBASE-T devices. Lesson learned.
