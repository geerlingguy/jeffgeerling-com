---
nid: 3028
title: "The Pi 4 Compute Module might support NVMe storage"
slug: "pi-4-compute-module-might-support-nvme-storage"
date: 2020-07-17T21:17:58+00:00
drupal:
  nid: 3028
  path: /blog/2020/pi-4-compute-module-might-support-nvme-storage
  body_format: markdown
  redirects: []
tags:
  - compute module
  - nvme
  - pcie
  - performance
  - raspberry pi
  - ssd
---

> There is a companion video to this post: [Is fast NVMe storage coming to the Raspberry Pi?](https://www.youtube.com/watch?v=3yTyhR0Adao).

A couple days ago, Tom's Hardware posted an article stating [NVMe support might be coming to the Raspberry Pi Compute Module 4](https://www.tomshardware.com/news/raspberry-pi-nvme-support-coming).

On the [first episode of The Pi Cast](https://www.youtube.com/watch?v=fTJ5eLn58to), Eben Upton, the CEO of Raspberry Pi, said "microSD will always be the baseline for storage", but "it's fairly likely we'll support NVMe soon on the Compute Module 4, to some degree, using single-lane PCI Express." (Skip to about 11 minutes into the video for the NVMe discussion).

He also said NVMe support is _not without cost_, since there's an extra connector silicon required. And with the System on a Chip used in the Pi 4, there's also a tradeoff involved: There's only one PCIe 1x lane, and it's currently used for the Pi 4's USB 3.0. If you want to add NVMe support, you'd have to drop the USB 3.0 ports.

For some people, the tradeoff might be worth it, though—but why?

## NVMe vs SATA SSDs

What benefit does NVMe storage offer over other options like using a [USB 3.0 SSD with UASP](/blog/2020/uasp-makes-raspberry-pi-4-disk-io-50-faster)?

Well, this is an SATA (Serial ATA) SSD drive:

{{< figure src="./ssd-sata-connector.jpeg" alt="SATA SSD drive" width="600" height="429" class="insert-image" >}}

And this is an NVMe (Non-Volatile Memory express) drive that uses the M.2 connector:

{{< figure src="./nvme-m2-ssd-storage.jpeg" alt="NVMe M.2 connector and controller chip - SSD" width="600" height="411" class="insert-image" >}}

The main difference is the [Serial ATA interface](https://en.wikipedia.org/wiki/Serial_ATA) was originally designed in the year 2000 for hard drives that used slow spinning platters (and before that, many HDDs used [IDE/Parallel ATA](https://en.wikipedia.org/wiki/Parallel_ATA), which was slower still).

NVMe drives have similar _guts_ to an SATA drive, but they directly attach to your computer's PCI express bus and bypass the overhead of the older SATA protocol.

An NVMe drive in the same price range _generally_ performs better than an SATA SSD, and the difference will only get better over time, because the theoretical limit of NVMe storage is 32 GB/sec—most SATA drives are limited to 600 MB/sec:

{{< figure src="./sata-nvme-theoretical-limit.png" alt="SATA SSD vs NVMe theoretical performance limit" width="530" height="287" class="insert-image" >}}

You can use either type of drive with a Raspberry Pi 4 via USB 3.0 if you have the right adapter, like [this one](https://www.amazon.com/gp/product/B00FCLG65U/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=8c1608c99e52153b32cd7c2dd4643709&language=en_US) for SATA drives, or [this one](https://www.amazon.com/TDBT-Enclosure-Thermal-Cooling-External/dp/B07TJT6W8K/ref=as_li_ss_tl?dchild=1&keywords=tdbt+superc&qid=1595019312&s=electronics&sr=1-3&linkCode=ll1&tag=mmjjg-20&linkId=ecfedcb1215ee0360c01eb804f994f65&language=en_US) for NVMe drives.

## NVMe on the Compute Module 4?

With a new Compute Module 4, though, you might be able to plug an NVMe directly into the PCIe bus on the Raspberry Pi, instead of having to [desolder the USB controller chip](http://mloduchowski.com/en/blog/raspberry-pi-4-b-pci-express/) like you'd have to do on the Pi 4.

And as I mentioned earlier, that could have tradeoffs, because it sounds like Eben said it would incur more cost and would probably require more connectors. But people who use the Compute Module often have the resources to build custom PCBs and enclosures that pack the functionality they need into a tight space.

As an example, the [Turing Pi board](https://turingpi.com) I've been using for my [Raspberry Pi Cluster series](https://www.youtube.com/watch?v=kgVz4-SEhbE) packs a lot functionality into a Mini-ITX form factor, and can run seven Pi Compute Modules at the same time. It'd be cool if you could attach an NVMe drive to each one—it would make a much better-performing NAS or give me really fast storage for Kubernetes or other apps.

{{< figure src="./compute-module-cm3-plus-vs-raspberry-pi-4-model-b.jpeg" alt="Compute Module 3+ vs Raspberry Pi 4 model B" width="600" height="490" class="insert-image" >}}

One thing to keep in mind, though: we're talking about the Compute Module (current CM3+ pictured at top), not the regular Raspberry Pi 4 model B (pictured at bottom), which is the Pi 95% of people are familiar with. If there were a version of the Pi 4 available with a PCI express connection or an NVMe connection, it wouldn't fit into the same form factor and cases Raspberry Pi users are familiar with for all the model B computers since the original Pi.

{{< figure src="./pcie-nvme-m2-adapter-with-pi-4-case.jpeg" alt="PCIe NVMe M.2 adapter card with Pi 4 model B case" width="600" height="499" class="insert-image" >}}

And to illustrate that example, the adapter pictured above would allow you to plug in standard M.2 NVMe drives into a 1x PCI Express slot that could work with the Pi 4, but it wouldn't fit into any standard Raspberry Pi 4 model B case. If a Pi had a built-in M.2 slot (versus PCIe), there are shorter NVMe drives which could fit, but not without increasing the clearance on the bottom of most Pi cases.

So I think, long-term, for most projects, it'll still be easiest to use a microSD card, and to pick a really good one, like the one I use and recommend, the Samsung Evo Plus. (See my [2019 microSD card review post](/blog/2019/raspberry-pi-microsd-card-performance-comparison-2019) for benchmarks and recommendations.)

Even if we might not be seeing an M.2 connector on the Raspberry Pi 4 model B anytime soon, it's still exciting to see the Raspberry Pi platform will be offering new possibilities with new hardware... hopefully within the next year or so!
