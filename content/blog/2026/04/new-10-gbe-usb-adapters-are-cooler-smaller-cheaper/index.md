---
date: '2026-04-18T09:00:00-05:00'
tags: ['youtube', 'video', '10g', '10gbe', 'ethernet', 'networking', 'homelab', 'wisdpi', 'usb', 'reviews']
title: 'New 10 GbE USB adapters are cooler, smaller, cheaper'
slug: 'new-10-gbe-usb-adapters-cooler-smaller-cheaper'
---
For years, the best way to get 10 gigabit networking on laptops was to buy an expensive, large, and hot 10 GbE Thunderbolt adapter. With new RTL8159-based 10G USB 3.2 adapters coming onto the market, the bulky adapters might be a thing of the past. Just look at the size of the thing in comparison to my Thunderbolt adapters.

{{< figure
  src="./thunderbolt-and-usb-c-10g-ethernet-adapters.jpg"
  alt="10 Gbps Ethernet adapters for Thunderbolt and USB"
  width="700"
  height="auto"
  class="insert-image"
>}}

[2.5G](https://amzn.to/3QIkfFm) and even [5G USB adapters](https://amzn.to/4mytCmZ) have been out for a while, but sometimes you need more bandwidth, and most computers have at least one high-speed USB port.

The 10G adapter I'm testing is [this $80 model from WisdPi](https://www.wisdpi.com/products/usb-c-to-10gb-ethernet-adapter). That's double the price of most 5G/2.5G adapters, but less than half what I paid for my Thunderbolt 10G adapters.

If you _need_ 10 gigs, this might be the best option now. At least if you're using RJ45 and not SFP+. But if you _don't_ need 10 gigs, a 2.5 or 5 gig adapter's still gonna be the best value.

Also, you might not even _get_ 10 gigs with these new adapters, depending on your computer. Why? Well, I'll demonstrate that using my _own_ computers.

This blog post is a companion to today's video, which is embedded below if you'd like to watch instead of read:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/zYZbZJZfCFI' frameborder='0' allowfullscreen></iframe></div>
</div>

## USB is something special

{{< figure
  src="./framework-13-amd-ryzen-ai-5-340-10g-usb-ethernet-test.jpg"
  alt="Framework 13 with AMD Ryzen AI 5 340 running 10G USB Ethernet Test over USB 3.2 Gen 2x1"
  width="700"
  height="auto"
  class="insert-image"
>}}

I tested this adapter on four computers:

  - Framework 13 with AMD Ryzen AI 5 340 (includes USB 4 / USB 3.2 Gen 2)
  - MacBook Neo (USB 3.1 and USB 2.0)
  - M4 MacBook Air (USB 4 / USB 3.1 Gen 2)
  - Desktop with AMD Ryzen 7900x with B650 motherboard (USB 3.2 Gen 2x2)

Getting those specific USB port specs is a bit of a chore (some websites don't even tell you if it's '3.2 Gen 2' or '3.0', and Windows itself only says "USB 3.0" when you plug in a USB 3.2 Gen 2x2 device like the 10 Gbps NIC!)

I was only able to get _full_ 10 Gbps speed (minus a little overhead) on the AMD Desktop, which has a single USB 3.2 Gen 2x2 port good for 20 Gbps of throughput. The other machines got around 6-7 Gbps:

{{< figure
  src="./iperf3-speed-wisdpi-10gbps-send.jpeg"
  alt="10 Gbps iperf3 bandwidth test results for Macs and PCs"
  width="700"
  height="auto"
  class="insert-image"
>}}

The Macs have the same per-port bandwidth (USB 3.1 Gen 2x1, for 10 Gbps), but the performance is consistently worse than the Framework.

On the Macs, the adapter was correctly identified when I plugged it in, and worked straightaway, with no extra driver installation. The 'Hardware' tab in the Network settings incorrectly reported a connection speed of `2500Base-T`.

On Windows, the adapter was recognized when plugged in, but wouldn't connect to the network until I installed the latest Realtek driver, downloaded from their website.

{{< figure
  src="./iperf3-speed-wisdpi-10gbps-bidir.jpg"
  alt="10 Gbps iperf3 bidirectional bandwidth test results for Macs and PCs"
  width="700"
  height="auto"
  class="insert-image"
>}}

Bidirectional bandwidth testing offered an interesting contrast; the Macs both handled traffic symmetrically, while the Framework was wildly disparate. The desktop PC gave a full 9.5 Gbps down, and around 5 Gbps up.

The main takeaway is this adapter only reaches its full potential if you have a USB 3.2 Gen 2 2x2 20 Gbps port.

And considering the mess of USB naming over the past decade—and the fact Microsoft reports _all_ USB 3.x connections as "3.0" in their Device Settings pane, good luck figuring out your own computer's support without glancing at spec sheets!

A few computers I've seen actually label the USB port speed (e.g. '10' or '20'), but that seems fairly rare. Most manufacturers seem to follow Apple in eschewing labeling entirely!

{{< figure
  src="./macbook-air-10g-usb-only-7-gbps-bandwidth-iperf3.jpg"
  alt="Mac USB bandwidth displayed in System Information"
  width="700"
  height="auto"
  class="insert-image"
>}}

At least Apple has the negotiated port speed visible in the 'System Information' app—I couldn't find that detail anywhere on Windows.

## 5G and 2.5G a better value?

With reduced speed due to inadequate USB port bandwidth, would a 2.5 Gbps or 5 Gbps adapter be a better value?

{{< figure
  src="./10g-5g-usb-wisdpi-ethernet-adapters.jpg"
  alt="10 Gbps and 5 Gbps WisdPi Ethernet USB adapters"
  width="700"
  height="auto"
  class="insert-image"
>}}

Testing the [WisdPi 5 Gbps adapter](https://www.wisdpi.com/products/wisdpi-usb-3-2-5g-ethernet-adapter-wp-ut5-wired-lan-network-connection-for-mac-os-linux-windows-backward-compatible-on-5g-2-5g-1g-100mbps-ideal-for-gaming) pictured above on my M4 Air, it got 4.6 Gbps. The [10 Gbps adapter](https://www.wisdpi.com/products/usb-c-to-10gb-ethernet-adapter) is 1.4x faster, but for more than 2x the price ($30 vs $80).

I think, if you already _have_ a 10 Gbps network, you use RJ45 and not SFP+ connections, and you want a more compact adapter (compared to the bulky, hot Thunderbolt adapters), it's a good deal. But if you _need_ that full 10 Gbps or SFP+ support, Thunderbolt adapters are still the best if you have Thunderbolt ports that don't support USB 3.2 Gen 2 2x2.

If you don't need 10 Gbps, though, stick to 2.5 or 5 Gbps adapters—they are still the best value right now.

## Thermals and Power Draw

I also checked thermals and power draw—though my tests are not comprehensive. Measuring the absolute power draw is difficult because my USB-C power measurement devices downgrade the connection speed to USB 2, which means I'm not testing at full performance.

{{< figure
  src="./TODO POWER"
  alt="Power Draw for WisdPi 10 Gbps USB-C Ethernet Adapter"
  width="700"
  height="auto"
  class="insert-image"
>}}

At the slower USB 2 speed, the adapter uses about 0.86 Watts of power.

TODO HERE.

And it doesn't get that hot, which was surprising to me. All my Aquantia-based 10 gig adapters turn into little ovens, and that's a big reason they're so... big. The enclosures are giant heatsinks.

{{< figure
  src="./TODO THERMALS"
  alt="Thermals for WisdPi 10 Gbps USB-C Ethernet Adapter"
  width="700"
  height="auto"
  class="insert-image"
>}}

But this one only got up to like 42 degrees celsius after I was running a bidirectional test for a few minutes.

That's warm, for sure, but not so hot that I'd burn myself touching it like I have with some of my other 10 gig adapters.

## Conclusion

If $80 is too rich, this isn't the only option that uses the new chip; AliExpress is [littered with alternatives](https://www.aliexpress.us/w/wholesale-realtek-10gbps-usb-nic.html). And you can get it on PCI Express cards, which bypasses the USB port requirement on desktop PCs.

In the midst of all the price inflation in personal computing, it's nice to find a new device that's cheaper, faster, and (depending on your USB port) better.
