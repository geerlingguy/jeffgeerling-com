---
nid: 3086
title: "Building a 2.5 Gbps 5-drive Pi NAS - Hardware Setup"
slug: "building-25-gbps-5-drive-pi-nas-hardware-setup"
date: 2021-03-26T15:00:28+00:00
drupal:
  nid: 3086
  path: /blog/2021/building-25-gbps-5-drive-pi-nas-hardware-setup
  body_format: markdown
  redirects:
    - /blog/2021/building-25-gbps-5-drive-raspberry-pi-nas-hardware-setup
aliases:
  - /blog/2021/building-25-gbps-5-drive-raspberry-pi-nas-hardware-setup
tags:
  - asustor
  - nas
  - raspberry pi
  - tutorial
  - video
  - youtube
---

A few months ago, an ASUSTOR representative emailed me with an offer I couldn't refuse. He saw my blog post and video about [building the fastest Raspberry Pi NAS](/blog/2020/building-fastest-raspberry-pi-nas-sata-raid), and asked if I wanted to put up my best Pi-based NAS against an Asustor NAS.

We settled on the Asustor Lockerstor 4, with dual-2.5 Gbps networking, 4 GB of RAM, and a quad-core Intel CPU. To make things even, he convinced Seagate to send four 8TB IronWolf NAS drives. I don't fancy he thought it would be a good show if I kept on using my four used WD GreenPower drives from 2010!

I posted a video of the hardware build process for _both_ NASes on my YouTube channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/vBccak8f-VY" frameborder='0' allowfullscreen></iframe></div>
</div>

But _this_ blog post will focus on what it takes to build your own Raspberry Pi NAS, with the best specs and performance you can possibly get—on a Raspberry Pi, at least!

## Parts Required

{{< figure src="./pi-all-parts.jpeg" alt="Raspberry Pi NAS build - all parts on table" width="600" height="346" class="insert-image" >}}

Here's the official parts list, with all the items I ended up using in my NAS (note: Amazon links are affiliate links):

<div style="max-width: 600px; margin: 0 auto;"><table>
    <thead>
        <tr>
            <th>Part</th>
            <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a href="https://www.raspberrypi.org/products/compute-module-4/">Raspberry Pi Compute Module 4 4GB Lite</a></td>
            <td>$45</td>
        </tr>
        <tr>
            <td><a href="https://www.raspberrypi.org/products/compute-module-4-io-board/">Raspberry Pi Compute Module 4 IO Board</a></td>
            <td>$35</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/3vKhLaT">SanDisk Extreme microSD card - 32GB</a></td>
            <td>$10</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/3cYmdKz">I/O Crest SI-PEX60016 2 port PCIe Switch</a></td>
            <td>$25</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/3cJk19t">PCIe 1x to 16x extension cable</a></td>
            <td>$19</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/3tsOfEv">Rosewill 2.5 Gpbs PCIe 1x card</a></td>
            <td>$20</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/30VjKdX">IO Crest 5-port SATA III PCIe JMB585 HBA</a></td>
            <td>$50</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/2NrMhVs">Noctua 120mm 1700 rpm NF-P12 fan</a></td>
            <td>$14</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/3tvPB15">Noctua NA-FC1 PWM fan controller</a></td>
            <td>$21</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/3cJkjgz">CableCreation SATA III cables (5 pack</a></td>
            <td>$7</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/3vz3UUt">Phanteks 3.5&quot; HDD bracket (2 pack x2</a></td>
            <td>$26</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/3vC5q8A">Redragon 700W fully-modular PSU</a></td>
            <td>$80</td>
        </tr>
        <tr>
            <td><a href="https://amzn.to/38Prwuc">Kentek 4-pin Molex to 4-pin Floppy adapter</a></td>
            <td>$5</td>
        </tr>
        <tr>
            <td><strong>TOTAL</strong></td>
            <td><strong>$357</strong></td>
        </tr>
    </tbody>
</table></div>

If you watched the video closely, you may notice I swapped out a few parts for my final build that I used for benchmarking:

  - The [Exacq PCIe Switch with the TI chip](https://pipci.jeffgeerling.com/cards_adapter/exacq-ti-xio3130-2-port-pcie-switch.html) was giving me a little trouble sometimes, so I swapped it out for the IO Crest board.
  - I dropped the separate molex power adapter and the 12V 5A barrel plug power adapter for the PCIe switch and Pi, respectively, and plugged them both directly into the PC PSU. For the Pi, it required a molex to floppy adapter cable, but that was easy enough to find on Amazon.

For comparison, the [Asustor Lockerstor 4](https://amzn.to/3cKjbJr) I'm using costs $549—almost $200 more in total. But the Lockerstor does offer a number of features the Pi doesn't (like dual NVMe SSD caching over a faster bus, dual 2.5G network ports that it can actually saturate (the Pi only has a single PCIe Gen 2 lane), and... an actual case to hold everything).

## Assembly

I already knew from previous research for my [Raspberry Pi PCI Express Database](https://pipci.jeffgeerling.com) that I could get a [Rosewill RC-20001 2.5GBASE-T](https://pipci.jeffgeerling.com/cards_network/rosewill-rc20001-25gbe.html) adapter working if I compile the kernel with `Realtek 8169/8168/8101/8125 ethernet support`. And I knew I could get an [IOCrest JMB585 5-port SATA card](https://pipci.jeffgeerling.com/cards_storage/iocrest-sata-5-port-jmb585.html) working by enabling `AHCI SATA support` and `Marvell SATA support`.

{{< figure src="./pi-2.5g-ethernet.jpg" alt="Raspberry Pi 2.5G Ethernet through PCIe Switch" width="600" height="338" class="insert-image" >}}

But I hadn't yet had them working _together_. So I tried them with an Exacq PCIe switch I had laying around, and surprisingly, on my first try (with a custom kernel), they both powered up and worked.

A few boots later one or the other card wouldn't show, so I swapped out the Exacq switch for an IOCrest switch, and they both were recognized every time.

I used two sets of two [Phanteks 3.5" Hard Drive brackets](https://amzn.to/3vz3UUt) I found on Amazon to hold the drives themselves. I actually like how these cages provide plenty of room for airflow around the drives, and hold them very well, along with rubber grommets to help prevent vibration-related issues.

{{< figure src="./pi-setup-power-supply.jpg" alt="Raspberry Pi NAS Power Supply Setup" width="600" height="338" class="insert-image" >}}

For _power_, I was leery of putting everything into my Redragon 700W PSU, since I had released an older Redragon's [magic smoke](https://redshirtjeff.com/listing/release-the-magic-smoke?product=46) earlier this year doing some testing... but eventually, I decided to connect everything to it, including the 4 SATA drives, the PCI Express switch (using a Molex to floppy adapter), and the Raspberry Pi itself (using another Molex to floppy adapter).

The final setup (well; almost final as pictured—I swapped PSUs for the Pi after taking this picture) is... not nearly as tidy as the ASUSTOR you see sitting in the background:

{{< figure src="./pi-almost-final-setup.jpeg" alt="Raspberry Pi NAS almost final setup" width="600" height="440" class="insert-image" >}}

## What's Next?

Well, I know you want benchmarks and a verdict, but I just haven't had the time yet to compile everything, especially since I ran into a few speed-bumps—with both the Pi _and_ the ASUSTOR.

So software setup, benchmarks, more details about how they run, and my final word on whether I'd go with a Pi NAS (for the value and experience) over an ASUSTOR (or something similar like a QNAP or Synology NAS) is coming _next_ week.

I _can_ reveal that I can get consistent network copies at 200 MB/sec on the Pi over a 2.5 Gbps connection. But the ASUSTOR can go a bit further still.
