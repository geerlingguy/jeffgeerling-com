---
nid: 3223
title: "Building a fast all-SSD NAS (on a budget)"
slug: "building-fast-all-ssd-nas-on-budget"
date: 2022-07-20T14:00:41+00:00
drupal:
  nid: 3223
  path: /blog/2022/building-fast-all-ssd-nas-on-budget
  body_format: markdown
  redirects: []
tags:
  - build
  - freebsd
  - kioxia
  - mini itx
  - motherboard
  - nas
  - samsung
  - server
  - ssd
  - supermicro
  - truenas
  - video
  - youtube
---

{{< figure src="./all-ssd-edit-nas-complete.jpeg" alt="All SSD Edit NAS build - completed" width="700" height="402" class="insert-image" >}}

I edit videos non-stop nowadays. In a former life, I had a 2 TB backup volume and that stored my entire digital life—all my photos, family video clips, and every bit of code and text I'd ever written.

Video is a different beast, entirely.

Every minute of 4K ProRes LT footage (which is a very lightweight format, compared to RAW) is 3 GB of space. A typical video I produce has between 30-60 minutes of raw footage (which brings the total project size up to around 100-200 GB).

To edit footage _well_, the data not only needs to move _fast_ (1 Gbps barely cuts it for a single stream), it also needs to have very low latency, otherwise Final Cut Pro (my editor of choice) lags quite a bit while scrubbing over dozens of video clips.

Therefore, I always _used_ to edit videos off my local SSD drive. And sometimes over the network using macOS's built-in file sharing. But as my video workflow matures, I find myself needing a central storage solution disconnected from my main workstation.

Thus, the all-SSD high-performance edit NAS—on a budget.

I had five [8TB Samsung QVO SSDs](https://amzn.to/3AXvJLs) from my insane [$5000 Raspberry Pi server](/blog/2021/i-built-5000-raspberry-pi-server-yes-its-ridiculous) build. Until now, I had them inside my 2.5 Gbps NAS. But I wanted to build my own NAS capable of saturating a 10 Gbps connection, and allowing _extremely_ low latency data access over the network to my two Macs, both of which are connected to my wired 10 Gbps home network.

## Used Server Parts

### Summary

This server build can be done with just as much capability (but a lower storage amount) on a more stringent budget, or can go 'all out' maxing out the RAM and SSD storage space. I'll show a price comparison of both (noting that my needs—tons of RAM and tons of SSD space—may not match your own, if the main goal is 'very fast SSD NAS'):

| Part | Price (low) | Price (high - as built) |
| --- | --- | --- |
| [Supermicro X10SDV-4C-TLN2F motherboard / Xeon D / Dual 10 GbE](https://www.ebay.com/itm/254932365206) (eBay) | $260 | $260 |
| DDR4-2133 ECC RAM (Didion Orf e-waste recycling) | $55 (32GB) | $220 (128GB) |
| [Boot SSD](https://www.microcenter.com/product/635353/supermicro-xg6-kxg60znv512g-512gb-ssd-3d-tlc-nand-m2-2280-pcie-nvme-30-x4-internal-solid-state-drive) | $50 ([256GB USB Drive](https://amzn.to/3okVhuA)) | $125 ([512GB XG6](https://www.microcenter.com/product/635353/supermicro-xg6-kxg60znv512g-512gb-ssd-3d-tlc-nand-m2-2280-pcie-nvme-30-x4-internal-solid-state-drive)) |
| [2U Rackmount Case](https://www.myelectronics.nl/us/19-inch-2u-mini-itx-case-short-depth.html) | $200 | $200 |
| [2x Noctua 80mm case fans](https://amzn.to/3RSJ7Xi) | $34 | $34 |
| Storage SSDs | $180 ([MX500 1TB x2](https://amzn.to/3PlvaPQ)) | $3490 ([QVO 8TB x5](https://amzn.to/3PqRoQA))
| Total | $779 | $4,329 |

When looking at the price discrepancy, you have to realize (a) I already had the 8TB SSDs, from some projects I tested last year... most people don't have those things laying around, and (b) I will actually _use_ that much low-latency storage... most people probably don't and would be better off with less SSD storage and more spinning disks (which are _much_ cheaper per TB).

### Details

{{< figure src="./supermicro-mini-itx-server-motherboard-xeon-d-1521.jpeg" alt="Supermicro Mini ITX server motherboard Xeon D-1521" width="700" height="425" class="insert-image" >}}

The motivation for this build came from finding [this Supermicro X10SDV-4C-TLN2F Mini ITX motherboard](https://www.ebay.com/itm/254932365206). The price ($270 shipped) was low enough I could consider building with it, and it already included an older-but-not-too-power-hungry Xeon D SoC, two 10 Gbps Ethernet ports, and 5 SATA-III connectors, the basic components I needed for the build.

ServeTheHome [gave this motherboard a good review](https://www.servethehome.com/supermicro-x10sdv-4c-tln2f-review-xeon-d-1520/) when it came out, and as long as things were in working order, it should still be a good choice, though less efficient and performant than a more expensive 2020s-era board.

I needed to find a Mini ITX rackmount enclosure, and luckily I'd been in talks with MyElectronics after using their prototype 'blue' enclosure for a [remote Pi cluster installation](/blog/2022/hosting-website-on-farm-or-anywhere) I was testing. They are working on a new [2U mini ITX short-depth enclosure](https://www.myelectronics.nl/us/19-inch-2u-mini-itx-case-short-depth.html), and they sent me an early revision to use in this build:

{{< figure src="./myelectronics-mini-itx-2u-short-depth-enclosure.jpg" alt="MyElectronics 2U Mini ITX short depth enclosure" width="700" height="261" class="insert-image" >}}

They said the enclosure should be available 'soon' for around $200, but they're still working out a few details with port placement, the power supply configuration, and PCIe slot layout.

I already had the SSDs on hand, and to be honest, you could use much less expensive SSDs if you don't _need_ many TB of flash storage—heck, right now I'm only using a few percent of it! But those cost around $3500 new.

To round out the build, I bought a couple Noctua fans, and 128 GB of recycled ECC RAM from [an e-waste recycler](https://www.didionorfrecycling.com/it-assets) only a dozen miles from where I live. They sold me four sticks of 32GB ECC DDR4-2133 RAM (HP branded) for $220.

## Yes there's a sponsor (for the SSD)

To help fund this build, I got Micro Center to sponsor the [build video](https://www.youtube.com/watch?v=xvE4HNJZeIg), and they contributed a Kioxia XG6, which is sold under Supermicro's name:

{{< figure src="./kioxia-xg6-nvme-ssd.jpeg" alt="Kioxia XG6 Supermicro branded NVMe SSD provided by Micro Center" width="700" height="467" class="insert-image" >}}

They sell the [512GB model I used](https://www.microcenter.com/product/635353/supermicro-xg6-kxg60znv512g-512gb-ssd-3d-tlc-nand-m2-2280-pcie-nvme-30-x4-internal-solid-state-drive) for about $125—_in store_! I didn't realize they have some Supermicro (and sometimes Dell/EMC) server gear in stock at their stores in the US. I just wish they had more locations (both here and internationally!).

## BIOS and UEFI

I put all the hardware together, and installed TrueNAS from a USB stick to the NVMe drive. If you're wondering why I chose TrueNAS core, check out the [full video](https://www.youtube.com/watch?v=xvE4HNJZeIg) where I speak to Wendell from Level1Techs about performance considerations and the storage layout for this NAS.

But I had a problem: I couldn't get the Supermicro motherboard to _boot_ off UEFI. I was getting errors about "CPU with APIC ID 0 is not enabled", and I spent an hour messing around in the BIOS before (temporarily) giving up and throwing in a SATA boot SSD.

This motherboard is from around 2015, an era when NVMe boot on servers wasn't commonplace. Couple that with the M.2 slot accepting _either_ SATA or NVMe drives, and most people preferring to boot off a [SuperDOM](https://www.supermicro.com/products/nfo/SATADOM.cfm) instead, and I knew I was kind of on my own debugging it.

{{< figure src="./zfs-data-copy-357mb-ps.jpg" alt="357 MBps copy over Samba on macOS" width="700" height="249" class="insert-image" >}}

With the SATA SSD installed, I was able to get consistent performance using a striped RAIDZ mirror pool with four SSDs and a hot spare—but that performance stayed around 320 MB/sec writes over long periods of time! That's only a third of the available bandwidth, and only a little better than the 200-250 MB/sec I was getting on my 2.5 Gigabit NAS.

After some more consulting with Wendell _and_ talking to Patrick from [ServeTheHome](https://www.servethehome.com), I was able to figure out both the boot issue (just had to mess with the UEFI boot settings a bit more), and the performance issue (it... ended up going away after I replugged everything).

{{< figure src="./zfs-data-copy-737mb-ps.jpg" alt="700 MBps copy over Samba on macOS" width="700" height="297" class="insert-image" >}}

With the built-in SATA ports, I got around 700 MB/sec write speed over the network, and 1.1 GB/sec reads. Latency was great, and editing Final Cut Pro projects felt the same as if editing local.

Just to see what was possible, I also tossed in a [MegaRAID 9405W-16i HBA](https://amzn.to/3srcZOh), and re-tested, and could get 1.1 GB/sec _both_ ways... but I went back to the onboard SATA when I measured 7-15W more power consumption using the HBA. A few hundred MB/sec isn't worth the extra power consumption—especially considering I'd need to figure out how to properly cool the HBA:

{{< figure src="./hba-with-fan-mini-itx-server-build.jpg" alt="Fan directed at MegaRAID HBA installed in all SSD edit NAS for cooling" width="700" height="394" class="insert-image" >}}

## First time using ZFS in production

A few of the things I modified in my TrueNAS storage pool configuration, based on Wendell's recommendations:

  - **Sync: Disabled**: I disabled ZFS's sync option, meaning ZFS would report back to the OS a file was written even before it's fully written to disk. This is risky, but since I'm always copying footage I have a golden copy of _already_, and since I'm running the NAS on a UPS, the risk is minimized. With the 'Standard' setting, ZFS would limp along for a period, then go fast (700+ MB/sec), then limp along again. Speed was very inconsistent.
  - **1M Record Size**: Since I'm mostly pushing video files (with tens of MB/sec) through the server, having a smaller block size would just result in more IO operations. If I were running a database on here, I would consider a smaller size, but this is optimized for video.
  - **Periodic maintenance**: I set up nightly snapshots, weekly scrubs, and weekly S.M.A.R.T. scans, and made sure the server could email me a notification if anything went awry. One of the best benefits of an out-of-the-box solution like TrueNAS is the ease of setting these long-term automation tasks up.

The nightly snapshots (and indeed, ZFS/RAID itself) is _NOT_ at all a substitution for a rigorous backup plan. For now I'll be `rsync`ing the volume to my main NAS nightly, and that's backed up offsite to Amazon Glacier weekly. Eventually I might use ZFS's `sync` functionality to synchronize snapshots to my backup server. We'll see.

For now, I'm happy having a server that can consistently write 700+ MB/sec, and read 1.1 GB/sec, with extremely low latency, over my 10 gigabit network.

Watch the [full video](https://www.youtube.com/watch?v=xvE4HNJZeIg) to learn more about the thought process and some of the struggles I had.
