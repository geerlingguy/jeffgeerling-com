---
date: '2026-07-31T09:00:00-05:00'
tags: ['thunderbolt', '25g', 'ethernet', 'mac', 'macos', 'noctua', 'youtube', 'video', 'tutorial', '3d printing']
title: 'Getting 25 Gbps Thunderbolt Ethernet on my Mac Studio'
slug: 'getting-25g-ethernet-mac-thunderbolt'
---
{{< figure
  src="./mac-studio-ports-full-back-ethernet.jpg"
  alt="Mac Studio with all ports plugged in Ethernet 10G"
  width="700"
  height="auto"
  class="insert-image"
>}}

I've been using the built-in 10 Gigabit Ethernet on my Mac Studio for a few years. It works fine: I can edit 4K video straight off my NAS over the network, and run backups at around 1 GB/sec.

But... I want _more_. I upgraded my rack and my NAS to 25 GbE a couple years ago, and wanted to upgrade my main workstation, too.

I looked up 25G networking options for the Mac, and they're all _crazy_ expensive:

  - [Sonnet's Twin25G Adapter](https://amzn.to/4tVqlAM) is $999
  - [Atto's ThunderLink](https://amzn.to/48Tj0cG) is $1,099
  - [Raiden Digit's LightOne 25GbE Docking Station](https://store.raidendigit.com/products/lightone-25gbe-thunderbolt-docking-station) is $399 (which honestly, isn't bad)

The problem is Macs all require Thunderbolt adapters; you can't just plug an inexpensive(ish) PCIe card into a Mac (RIP Mac Pro).

I stopped looking until I saw [this blog post](https://kohlschuetter.github.io/blog/posts/2026/01/27/tb25/). Christian Kohlschütter found a [cheap 25G Thunderbolt adapter](https://amzn.to/4vGLjDG) that uses a server-pulled OCP 2 NIC with a little Thunderbolt 3 adapter board. And it works on any computer with Thunderbolt.

{{< figure
  src="./166.71-price-paid-25g-january.jpg"
  alt="I paid $166.71 in January for the 25G Thunderbolt NIC"
  width="700"
  height="auto"
  class="insert-image"
>}}

Back in January, it was only $160, which was insta-buy territory for me. Since that time, the Amazon listing jumped to **$299**, which still might be good compared to the Sonnet... but you might have to go digging through some Chinese sites to find a non-marked-up version now.

_This blog post is a companion to the following YouTube video:_

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/_--JjauL19A' frameborder='0' allowfullscreen></iframe></div>
</div>

## First Test - Two Problems to Solve

Once I had pulled some new fiber to my desk (where I only had Cat6A cabling before), I tested the bandwidth using `iperf3` between my Mac and my NAS. That's when I ran into two problems:

  1. The version of `iperf3` I was running on the NAS was too old. Without multi-threading, it maxed out at 15 Gbps.

  2. The 25G NIC enclosure was getting _hot_. Painful to the touch.

I could solve the first problem easily: I compiled the latest version of `iperf3`. That got me to 20 gigabits, since more than one CPU core could hand the transfers on my NAS. As Christian mentioned in his blog post, 20 Gpbs single direction and 25 Gbps bidirectional is about the limit for the Thunderbolt 3 chipset being used (even if you plug into a Thunderbolt 5 port).

{{< figure
  src="./thunderbolt3-to-25g-ethernet-pcie-board.jpg"
  alt="Thunderbolt 3 to PCIe NIC OCP 2 adapter board"
  width="700"
  height="auto"
  class="insert-image"
>}}

But the second problem was more tricky.

The burning-hot enclosure wasn't thermally bonded to the OCP 2 network card, meaning the NIC chips were _cooking_.

They had tiny heatsinks on them, but OCP 2 NICs are meant to be inside servers with high pressure fans, not in a little passively-cooled enclosure.

It was acting like a little oven.

## Fixing the NIC's cooling problem

Christian mentioned he slapped a couple giant heatsinks on the enclosure. That brought the chip down to a temperature that wouldn't cause NIC dropouts, but it was still getting pretty hot.

I wanted to make sure things were stable, and that meant active cooling.

My first idea was to stick on [these low-profile heatsinks](https://amzn.to/48DSiVn) and set [this speed-controlled USB fan](https://amzn.to/4cCM6OS) in front. I had to remove the enclosure's barely-ventilated front plate to get more airflow inside, but the back plate also created a ton of resistance.

It would still get hot, and the fan was just loud enough to be distracting, even on its lowest setting.

A Prusa rep had reached out around this time asking if I had any use for their new [Prusament PLA in Noctua Brown and Beige](https://www.noctua.at/en/news/noctua-and-prusa-research-introduce-3d-printing-filaments-in-signature-noctua-colours)... and I decided to switch tracks once they offered to send a spool of each. I purchased a [Noctua NF-A8 80mm 5V fan](https://amzn.to/4gUpZqK), and an [NA-FC1 Speed Controller](https://amzn.to/4vQq8iB) to silence it.

I designed a [fan duct for the 25G Thunderbolt NIC enclosure](https://www.printables.com/model/1789472-80mm-fan-mod-for-25g-thunderbolt-nic), and printed it in Noctua beige PLA.

Then I printed this [airflow-optimized 80mm fan grill](https://www.printables.com/model/1098017-high-efficiency-noctua-80mm-fan-grill), and screwed that on the front of the 80mm fan.

I was able to use the screws from the 25G NIC enclosure (I removed the front plate entirely), and the fan screws and extra cable that came with the Noctua 80mm fan, to secure everything together.

I chose to splice the braided fan extension cable Noctua includes, and taped it down inside the enclosure with kapton tape for some strain relief.

I soldered the cut end of the fan cable into these through-holes on the Thunderbolt-to-OCP adapter PCB to get the needed 5V power (well, 4.8V, but it's close enough):

{{< figure
  src="./noctua-fan-mod-25g-nic-solder-fan-header.jpeg"
  alt="Soldering the fan connector on the NIC adapter board for 5V power"
  width="700"
  height="auto"
  class="insert-image"
>}}

The fan only used about 0.5W of power, so I don't think it'll cause any brownout conditions on the NIC itself (which uses 4-5W total at idle).

After final assembly, this is what it looks like:

{{< figure
  src="./noctua-fan-mod-25g-nic-handheld.jpeg"
  alt="Holding the finished NIC with a Noctua 80mm fan and grill cover"
  width="700"
  height="auto"
  class="insert-image"
>}}

I plugged it in, re-tested with `iperf3`, and checked the temperature. It was sitting at less than 36°C after 10 minutes, with the fan on low. And this being a Noctua fan, I couldn't hear it at all under the desk.

## How does 25 Gbps perform on the Mac?

Like earlier, it maxes out around 20-25 Gbps, because of the slower Thunderbolt 3 connection.

{{< figure
  src="./mac-activity-monitor-1.43gb-per-second.jpg"
  alt="Activity Monitor showing 1.43 GB/sec on macOS with 25G NIC"
  width="700"
  height="auto"
  class="insert-image"
>}}

Testing Samba file copies between my NAS and my Mac, I got around 1.4 GB/sec read, and 1 GB/sec write[^samba].

That's only marginally better than the built-in 10G Ethernet. It's an improvement, sure... but was all the work pulling fiber, designing a fan cowling, paying $200 for all the parts, and assembling everything worth it?

Maybe. At least I got this blog post out of it.

[^samba]: I have SMB multichannel enabled, but this real-world speed limitation could also be related to my use of my lower-power Arm NAS (running on Ampere Altra, with 32 fairly-slow CPU cores). I was testing writing to an array of fast enterprise NVMe SSDs, so they _shouldn't_ be the bottleneck here.
