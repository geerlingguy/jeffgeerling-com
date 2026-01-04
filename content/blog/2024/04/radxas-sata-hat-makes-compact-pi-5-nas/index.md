---
nid: 3363
title: "Radxa's SATA HAT makes compact Pi 5 NAS"
slug: "radxas-sata-hat-makes-compact-pi-5-nas"
date: 2024-04-04T14:08:29+00:00
drupal:
  nid: 3363
  path: /blog/2024/radxas-sata-hat-makes-compact-pi-5-nas
  body_format: markdown
  redirects:
    - /blog/2024/radxa-updates-sata-hat-compact-pi-5-nas
    - /blog/2024/radxa-sata-hat-makes-compact-pi-5-nas
aliases:
  - /blog/2024/radxa-updates-sata-hat-compact-pi-5-nas
  - /blog/2024/radxa-sata-hat-makes-compact-pi-5-nas
  - /comment/34551
tags:
  - nas
  - omv
  - pi 5
  - radxa
  - raspberry pi
  - video
  - youtube
---

Radxa's latest iteration of its [Penta SATA HAT](https://radxa.com/products/accessories/penta-sata-hat) has been retooled to work with the Raspberry Pi 5.

{{< figure src="./radxa-penta-sata-hat-pi-5-and-mug.jpeg" alt="Radxa Penta SATA HAT for Raspberry Pi 5 with a Pi mug" width="700" height="auto" class="insert-image" >}}

The Pi 5 includes a PCIe connector, which allows the SATA hat to interface directly via a JMB585 SATA to PCIe bridge, rather than relying on the older [Dual/Quad SATA HAT's](https://wiki.radxa.com/Dual_Quad_SATA_HAT) SATA-to-USB-to-PCIe setup.

Does the direct PCIe connection help? _Yes._

Is the Pi 5 noticeably faster than the Pi 4 for NAS applications? _Yes._

{{< figure src="./radxa-penta-sata-hat-drives.jpeg" alt="Radxa Penta SATA HAT installed on Pi 5 with Drives next to it" width="700" height="auto" class="insert-image" >}}

Is the Pi 5 + Penta SATA HAT the ultimate low-power NAS solution? _Maybe._

It's more compelling than the Pi 4 was and _could_ fit your use case—even accounting for the Pi 5's slightly higher price points.

I ran through the entire process of setting up and testing the Penta SATA HAT in today's video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/l30sADfDiM8" frameborder='0' allowfullscreen></iframe></div>
</div>

But I'll also summarize some of my key findings:

  - If you want _all_ the test data and notes, check out my GitHub issue [testing the Radxa Penta SATA HAT on Pi 5](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/615). There's an exhaustive benchmarking process through which I discovered [macOS Finder is terrible for network share performance](/blog/2024/macos-finder-still-bad-network-file-copies).
  - Having the HAT distribute 12V power to the drives _and_ manage power delivery to the Pi 5's 5V rail via GPIO is very handy. You don't need two power supplies (one for HAT/drives and one for Pi) with this setup.
  - I had to break off three little fins on the official Pi Active Cooler to make room for the 12V barrel plug on the underside of the HAT. It would be nice if Radxa revised the board to not require this modification.
  - I tested an array of 4 Samsung QVO 8TB SSDs in RAID 0, and could get nearly 900 MB/sec at PCIe Gen 3 directly on the Pi.
  - I was only able to write through Samba over the 1 Gbps built-in Ethernet connection around 96 MB/sec (with a 100 GB test folder) from my Mac — read speeds were consistently maxing it out at 122 MB/sec, and on Windows I could get 115 MB/sec write speeds.
  - I installed [openmediavault 7](https://www.openmediavault.org), which worked great with ZFS, but was missing standard RAID configuration options—possibly because I had separately installed `mdadm` in my testing? I would love to try TrueNAS Scale, but it [sounds like iXsystems isn't interested in porting it to Arm](https://twitter.com/kmooresays/status/1774846833069568193).
  - ZFS in RAIDZ1 gave me lower network write speeds around 74 MB/sec from my Mac, and 108 MB/sec on my PC, but read speeds were still maxing out the network connection
  - I installed a [Pineberry Pi HatBRICK! Commander](https://pineberrypi.com/products/hatbrick-commander-2-ports-gen2-for-raspberry-pi-5) and [HatNET! 2.5G](https://pineberrypi.com/products/hatnet-2-5g-2-5-gigabit-ethernet-for-raspberry-pi-5) for 2.5 Gbps networking, and it worked without issue, though it would be nice to find a better way to get things stacked up:

{{< figure src="./radxa-penta-sata-hat-pineberry-pi-commander-pcie-2.5g-network.jpg" alt="Radxa Penta SATA HAT on Pi 5 with 2.5G Networking" width="700" height="auto" class="insert-image" >}}

Using that setup, I could consistently get 230 MB/sec read speeds over the network, but writes were still bottlenecked around 100 MB/sec on my Mac. It's not easy to pin down the problem on my Mac, but on Windows 11, it was consistently giving me 150 MB/sec, so it's not the Pi's fault.

With the PCIe Gen 2 switch in the way, storage _and_ networking are both downgraded to Gen 2 speeds, which results in the bottleneck preventing faster write speeds. You could get a little faster with RAID 0, since you wouldn't need to write parity data, but that's not recommended for most network storage use cases!

| Item | Price |
| --- | --- |
| Raspberry Pi 5 (8GB) | $80 |
| Radxa Penta SATA HAT | $45 |
| 12V 5A Power Adapter | $10 |
| 32GB microSD Card | $12 |
| TOTAL | **$147** |

My conclusion? The Pi 5 + Penta SATA HAT is most useful for read-heavy environments, but works great for any basic NAS use case. All-in, spending $150 or less on a small, energy-efficient NAS (this setup used 6-8W at idle, and 10-16W under load) isn't the worst way to build DIY network storage.

I also _really_ wish Raspberry Pi included 2.5 Gbps networking out of the box... the RP1 chip certainly has the bandwidth, but it seems like more was allocated to the DSI/CSI imaging pipeline and multiple USB 3.0/2.0 buses than networking, for this go-round.

Radxa will hopefully sell a case and fan control board at some point, to make this a more robust solution, but those aren't available currently.
