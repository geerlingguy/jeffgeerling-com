---
nid: 3096
title: "Trying KIOXIA CM6 and PM6 Enterprise SSDs on a Raspberry Pi"
slug: "trying-kioxia-cm6-and-pm6-enterprise-ssds-on-raspberry-pi"
date: 2021-05-14T14:49:12+00:00
drupal:
  nid: 3096
  path: /blog/2021/trying-kioxia-cm6-and-pm6-enterprise-ssds-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - hard drive
  - kioxia
  - nvme
  - raspberry pi
  - sas
  - ssd
  - video
  - youtube
---

Late last year, an engineer at Broadcom sent me some hardware and offered some help getting Broadcom's MegaRAID card working on the Raspberry Pi. It took some time, but eventually we were able to get the card and a demonstrator 'UBM' backplane working on the Pi, and it culminated in my posting about [Hardware RAID on the Pi](/blog/2021/hardware-raid-on-raspberry-pi-cm4), and on a livestream, getting [16 hard drives working on a Pi](https://www.youtube.com/watch?v=HPI5B9QNCY4).

The one thing I couldn't test in those earlier videos was the backplane and storage card's 'Tri-mode' support, allowing PCI Express NVMe drives—like KIOXIA's CM6—to work in the _same slot_ as the SATA and SAS drives I was used to testing.

So after some conversation with reps at KIOXIA, I was able to get a PM6 and three CM6 drives on loan to test them:

{{< figure src="./pm6-cm6-kioxia-raspberry-pi-cm4-compute-module-ssd.jpeg" alt="KIOXIA CM6 and PM6 SSD with Raspberry Pi Compute Module 4" width="700" height="467" class="insert-image" >}}

I tested both drives inside the experimental 'Elrond' backplane, which is a demonstrator for Universal Backplane Management ([SFF-TA-1005](https://members.snia.org/document/dl/27952)), connected through the [Broadcom MegaRAID 9460-16i](https://pipci.jeffgeerling.com/cards_storage/broadcom-megaraid-9460-16i.html) card, and as promised, I was able to hot-swap SATA, SAS, and NVMe drives using the same slots.

## Video

There is a video to go along with this post, which goes into a little more detail:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/jOU-NDDyyuY" frameborder='0' allowfullscreen></iframe></div>
</div>

## Why SFF NVMe?

Before getting to the benchmarks, I figured I should explain a little more about the 'U.3' (SFF-TA-1001) NVMe drive I tested, the CM6.

Most people are familiar with NVMe drives in the M.2 form factor:

{{< figure src="./m.2-drive-in-raspberry-pi-compute-module-4-io-board.jpeg" alt="M.2 NVMe SSD Samsung 970 EVO in Raspberry Pi Compute Module 4 IO Board" width="700" height="534" class="insert-image" >}}

But in enterprise storage, most servers have storage backplanes that offer slots with multiple SFF 2.5" drive bays. Traditionally, the bays would accept SATA or SAS drives, but with the rise in popularity of PCI Express-based storage, Intel soon created the U.2 standard to allow NVMe storage using the same connector—but with a different and incompatible pinout.

Therefore server vendors would have to decide to cable ports on their drive bays for _either_ SATA/SAS, _or_ NVMe. Thus the need for a new protocol—SFF-TA-1001, sometimes referred to as 'U.3'—which allows the same connector _and_ the same cabling to support all three drive types.

{{< figure src="./kioxia-cm6.jpeg" alt="KIOXIA CM6 PCIe NVMe Drive U.3" width="700" height="540" class="insert-image" >}}

And in both U.2 and U.3's case, the basic idea is to have a larger volume to support hot swap, higher capacities, _and_ better cooling, making a much more enterprise-ready package than the diminutive M.2 form factor.

##  Benchmarks

Now, getting to the meat of this post, I tested both of these drives against each other, and against some other drives I had on hand.

First, comparing the PM6 and CM6 on the Pi:

{{< figure src="./kioxia-pm6-vs-cm6-benchmark.png" alt="KIOXIA PM6 vs CM6 on Raspberry Pi Compute Module 4" width="768" height="432" class="insert-image" >}}

The CM6 beats out the PM6 in random write performance, but otherwise displays that the underlying flash storage's similarity between the two drives results in roughly equivalent numbers. I should note that these drives are _capable_ of 4 to _7_ GiB/sec of performance. The Raspberry Pi's x1 Gen 2 bus really is the limiting factor (besides the anemic CPU performance), and results in the Pi getting a 17x performance penalty compared to a nice, new PCI Express Gen 4 server.

I also compared the CM6 standalone to the CM6 in RAID 0, and found it was very slightly faster, but mostly I think I'm running into the Pi's CPU bottlenecks (in addition to the bus limitations):

{{< figure src="./kioxia-cm6-vs-cm6-raid0-benchmark.png" alt="KIOXIA CM6 vs CM6 in RAID 0 on Raspberry Pi Compute Module 4" width="768" height="432" class="insert-image" >}}

As a final test I wanted to see how the CM6 compared to the cheaper consumer Kingston SSDs I was testing on the Pi:

{{< figure src="./kioxia-cm6-vs-sata-ssd-vs-hdd.png" alt="KIOXIA CM6 vs SSD vs HDD on Raspberry Pi Compute Module 4" width="768" height="432" class="insert-image" >}}

And it's good to know these blazing-fast enterprise SSDs _are_, indeed, faster than the $30 off-the-shelf bargain bin SSDs. But that's not the only reason you'd spend the extra money for 'Enterprise'-grade SSDs—these SSDs are rated for at least 1 DWPD (so they should last much longer in write or read-heavy workloads), they have better cooling, they have better warranties—and that's all before mentioning they use an interface allowing for 10-20x more throughput than the SATA on the consumer SSD!

Thanks to KIOXIA for loaning me these drives to test, and thanks again to Broadcom for sending their UBM enclosure and a MegaRAID card, plus the engineering time to help get their driver patched for the Pi!
