---
nid: 3238
title: "BliKVM PCIe puts a computer in your computer"
slug: "blikvm-pcie-puts-computer-your-computer"
date: 2022-09-15T15:45:37+00:00
drupal:
  nid: 3238
  path: /blog/2022/blikvm-pcie-puts-computer-your-computer
  body_format: markdown
  redirects: []
tags:
  - blikvm
  - cm4
  - compute module
  - homelab
  - ipmi
  - kvm
  - pcie
  - pi-kvm
  - raspberry pi
  - servers
---

{{< figure src="./blikvm-pcie-with-raspberry-pi-cm4-pikvm.jpeg" alt="BliKVM PCIe with Raspberry Pi CM4 running PiKVM" width="700" height="467" class="insert-image" >}}

This is the [BliKVM PCIe](https://www.aliexpress.com/item/3256804386522898.html), a full computer on a PCI Express card. This is an IP KVM (Internet Protocol Keyboard-Video-Mouse) that can be put inside another computer or server.

Most _server_ motherboards already have remote 'lights-out' management functionality built in. Most frequently this is referred to as IPMI (Intelligent Platform Management Interface, but Dell calls it iDRAC, and HPE calls it ILO.

But not all servers have it. And even if they do, sometimes you have to pay extra money to use it, or the version you have goes unmaintained and it would be a security risk to keep it running on your network.

So that's where the BliKVM PCIe comes in.

It runs open source software called [Pi-KVM](https://pikvm.org), and once it's installed, it can control _everything_, _even if the computer's powered off_!

You can boot up the computer and force shut it down. You can remote control it anywhere along the boot process, so you could even manage BIOS settings or install an operating system.

## Setup

But how does it work? I mean, it's a PCI Express card. Won't it shut off when you shut down the computer?

Well that's where it gets a little weird.

{{< figure src="./blikvm-pcie-pins-closeup.jpeg" alt="BliKVM PCIe card pins closeup" width="700" height="467" class="insert-image" >}}

See these pins? The only ones connected to anything are actually the ground pins. All the data pins are disconnected.

So this card is a PCI Express card... but not really. It uses the slot as a convenient place to mount itself inside a PC or server, so you don't have a Raspberry Pi dangling off the back.

Exposed to the back of the computer is an HDMI and USB input, some activity lights, a USB-C power input, and a Gigabit Ethernet port, capable of using Power over Ethernet to power the device. So technically you could skip the USB-C power plug if you have PoE.

{{< figure src="./blikvm-pcie-with-cm4.jpeg" alt="BliKVM PCIe with Raspberry Pi Compute Module 4" width="700" height="467" class="insert-image" >}}

But the heart of this card goes on top—a Raspberry Pi Compute Module 4, a whole computer on a tiny system-on-module board.

blicube (makers of BliKVM PCIe) supplies a lot of accessories in the box, including a heatsink and fan, so if your case has poor airflow, you can get more air to the Pi so it still stays cool.

{{< figure src="./blikvm-pcie-oled-display-pi-cm4.jpg" alt="BliKVM PCIe with OLED external IP display for Raspberry Pi CM4" width="700" height="394" class="insert-image" >}}

There's also an OLED display that will tell you the IP address of PiKVM, and other stats like CPU and memory usage.

The front of the board has two headers: one for an internal USB 2.0 connection, and another for front panel ATX IO connections (power, reset, and LEDs).

You can see how I installed it in my desktop tower PC, and how PiKVM's UI works, in my latest YouTube video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/cVWF3u-y-Zg" frameborder='0' allowfullscreen></iframe></div>
</div>

## Conclusion

This thing isn't for everyone. Remote Desktop or VNC is adequate for simple remote access. And dedicated apps like Parsec are better if you need low-latency remote access. But if you need _full_ remote access with lights-out management, and you don't have IPMI/iDRAC/ILO already, this is a great option. It's a little expensive, but a lot cheaper than most external IP KVMs.

And _with a base model CM4_ it's cheaper than [ASRock Rack's PAUL card](https://www.newegg.com/asrock-rack-paul-interface-module/p/N82E16816775027). The BliKVM PCIe can be powered over Ethernet and has a few more external IO options, but the PAUL has a few more internal options for full-fledged servers, like internal sensors and SMBus monitoring for server power supplies.

These types of cards aren't the only reason you might put a computer in your computer, either. [Sir Neggles on twitter got this Mikrotik DPU](https://twitter.com/geerlingguy/status/1564628617002422274), which is basically a dual 25 Gigabit router-on-a-board, running on a Raspberry Pi too! Granted, it only got 3 Gbps of throughput on the Pi.

A few other things I didn't mention earlier: the BliKVM also comes with a bundle of helpful accessories like a VGA to HDMI adapter, an HDMI Sink for locking in an HDMI resolution, and a low profile bracket, for smaller PC cases and shorter 2U servers.

It uses about 2-3 Watts at idle, and 4-6 watts when you're remoted in controlling the screen. The latency is in the 100-300 millisecond range, so this isn't great for remote gaming, but it's fine for most other use cases. You can get up to 1080p at 60Hz with it.

You can [buy the BliKVM PCIe from AliExpress](https://www.aliexpress.com/item/3256804386522898.html) for a little over $100 without a Pi, or they even sell a kit with a marked-up CM4 for a little over $200. BliKVM sent me the card I reviewed in this post, but they didn't pay me anything and had no say about the content in this review.

For the best value, I would recommend getting the version _without_ a Pi, then watch [rpilocator](https://rpilocator.com) until you find one at list price.

I also should mention Pi-powered IP KVM competition like the [TinyPilot Voyager 2](https://tinypilotkvm.com/product/tinypilot-voyager2) and the [Pi-KVM v3](https://pikvm.org/buy/). I reviewed older versions of those last year, in my video [Control ANY COMPUTER with these Pi KVMs!](https://www.youtube.com/watch?v=TIrkEr2AeDY). Also my Dad and I reviewed the original BliKVM that was based on a Raspberry Pi 4 [over on Geerling Engineering](https://www.youtube.com/watch?v=3OPd7svT3bE).
