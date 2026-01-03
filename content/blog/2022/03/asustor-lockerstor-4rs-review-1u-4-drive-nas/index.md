---
nid: 3191
title: "ASUSTOR Lockerstor 4RS Review - 1U 4-drive NAS"
slug: "asustor-lockerstor-4rs-review-1u-4-drive-nas"
date: 2022-03-14T18:42:32+00:00
drupal:
  nid: 3191
  path: /blog/2022/asustor-lockerstor-4rs-review-1u-4-drive-nas
  body_format: markdown
  redirects: []
tags:
  - asustor
  - geerling engineering
  - nas
  - rack
  - radio
  - server
  - youtube
---

Over on the [Geerling Engineering](https://www.youtube.com/c/GeerlingEngineering) YouTube channel, my Dad and I just posted a video where we installed the [ASUSTOR Lockerstor 4RS - AS6504RS](https://amzn.to/36gFiYG) at his radio station, to increase their raw network storage capacity from 4 to 16 TB:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/kCUZ8-r-fBg" frameborder='0' allowfullscreen></iframe></div>
</div>

In the video, we focused on the installation, though I highlighted the unit's top-line features at the beginning.

In this blog post, I'll quickly recap the main features, then give more impressions of the unit from our experience setting it up, and my Dad's use of it at the station since we recorded the video.

> Note: Since this review, Seagate sent us some 16TB IronWolf Pro hard drives to test out, and we [made another video for the IronWolf Pro upgrade](https://www.youtube.com/watch?v=fUTLeWVsgyI)—check it out too!

## Lockerstor 4RS - 1U NAS

Compared to my [Lockerstor 4](https://www.asustor.com/en-gb/product?p_id=69), the 4RS has a slightly more robust Intel Atom C3538 quad-core CPU, which supports ECC RAM, has 8 MB of L2 cache, and PCIe Gen 3 (vs Gen 2 on the Lockerstor 4).

{{< figure src="./asustor-lockerstor-4rs-open-rear.jpeg" alt="ASUSTOR Lockerstor 4RS open rear ports" width="700" height="402" class="insert-image" >}}

The CPU itself is slightly older, but it supports a lot more connectivity, which the 4RS takes advantage of, offering:

  - Built-in dual 2.5 Gbps Ethernet ports
  - Built-in dual 1 Gbps Ethernet ports
  - 4x USB 3.2 Gen 1 Type A ports (for expansion and one-click backups)
  - 1x PCIe Gen 3 x4 slot (x8 physical) for up to 10 Gbps expansion cards
  - Up to 128 GB of built-in DDR4-2133 RAM (via 4 SO-DIMM slots — one is populated with 8 GB)

{{< figure src="./asustor-lockerstor-4rs-ram.jpeg" alt="ASUSTOR Lockerstor 4RS RAM" width="700" height="467" class="insert-image" >}}

The Atom C3538 is the exact same CPU used in the Lockerstor 4RS's closest competitor, the [Synology RackStation RS820+](https://amzn.to/3tZW0Up). Spec-wise, however, the Lockerstor wins on connectivity and capacity:

  - 4 SO-DIMM slots allows for expansion to 128 GB of RAM. The RS820+ only offers one expansion slot, for up to 18 GB.
  - 2x 2.5 GbE + 2x 1 Gbps ports on the Lockerstor vs 4x 1 Gbps ports on the RS820+

Other than that, the specs and build quality are very similar, and if you don't need the expansion and built-in IO of the Lockerstor, it comes down to whether you're more comfortable with Synology's DSM (DiskStation Manager) software or ASUSTOR's ADM (ASUSTOR Data Master).

Other features on the Lockerstor include:

{{< figure src="./asustor-lockerstor-4rs-hard-drives-seagate.jpeg" alt="ASUSTOR Lockerstor 4RS with 4 Seagate Ironwolf Pro NAS drives" width="700" height="346" class="insert-image" >}}

  - 4x hot-swap SATA drive bays (with metal hot swap cages)
  - Single power supply (RS version) or dual power supply (RD version)
  - Locator LED that can be used to identify the unit via software (front and rear)
  - Wake-on-LAN and Wake-on-WAN support (Wake-on-WAN requires a cloud account)

All in all, the 4RS actually lacks a couple features found in ASUSTOR's better desktop units, like dual M.2 NVMe slots. That means you won't be able to get high speed cache support for large capacity spinning drives—though over a 2.5 Gbps network that might not be an issue, depending on your storage needs.

Since ADM 4 now has at least preliminary support for [SMB Multichannel](https://www.level1techs.com/video/smb-multichannel-how-it-works-troubleshooting-guide), you can even get greater-than 2.5 Gbps throughput with multiple clients (or if clients have multiple gigabit connections) in certain conditions, without upgrading your network to 10 Gbps.

For many small to medium business where the Lockerstor 4RS would be a good fit, it might make more sense to upgrade at least parts of the network to 2.5 Gbps instead of 10 Gbps, especially if buildings and racks are already built out with Cat5e cabling, which supports the faster speed, but would likely not support a full 10 Gbps over copper.

## ASUSTOR's ADM software

ADM runs just the same on this unit as it does on my other ASUSTOR NASes. When you first boot it, there's a simple setup wizard that lets you configure the storage array and networking.

For the radio station where we installed this unit, my Dad and I chose RAID 10 for our four [4 TB Seagate Ironwolf NAS drives](https://amzn.to/3KJodFK). It took a minute or so to configure the array, then about 10 hours to slowly synchronize the disks and set up the EXT4 partition.

You can also use Btrfs instead of basic RAID levels, and that provides support for [Snapshots](https://www.asustor.com/online/College_topic?topic=252) using ADM's snapshot manager. We didn't go this route on this particular build, mostly because my Dad wanted to stick to a tried-and-true setup that I could guarantee wouldn't give him any trouble down the line. Btrfs isn't _new_, but I know the version used in ADM isn't the latest bleeding-edge version and some people have experienced pain when things went wrong.

> Now's a good time to reiterate a basic fact: RAID is NOT a backup! Even using RAID 10, and dual-drive redundancy, my Dad will be taking separate backups and storing a full offsite and offline copy every month. [You need a good backup plan](/blog/2021/my-backup-plan) and a NAS like the Lockerstor 4RS is only _part_ of it!

ADM also lets you run prebuilt apps using their 'App Center':

{{< figure src="./asustor-app-central.png" alt="ASUSTOR ADM App Center" width="700" height="394" class="insert-image" >}}

It has most of the utilities you might want to run on a NAS, though I typically take the approach of only installing the things you _need_, rather than trying to run anything and everything off your NAS. Sometimes this can even protect you from malware, like when users connecting their NASes to ASUSTOR's cloud software ran into [Deadbolt ransomware attacks](https://www.asustor.com/en/knowledge/detail/?id=&amp;group_id=628).

My Dad also wanted to make sure he could get notified if any of the drives failed SMART tests or was offline, so he could repair it quickly before any data was lost on the main NAS. Luckily there are many options for notifications, from the red status LEDs per drive, to SMS, Email, and even push notifications, all configurable in ADM:

{{< figure src="./asustor-notifications-push.png" alt="ASUSTOR Push notifications in ADM" width="700" height="394" class="insert-image" >}}

I had a few other things I wanted to test on the unit, and here are my notes on them:

  - I asked ASUSTOR about support for PCIe to M.2 adapter cards. They said the hardware currently works, but ADM doesn't yet have support for using M.2 SSDs on the Lockerstor 4RS (e.g. as a faster read cache volume, or even as a separate data volume for more volatile storage). They said they may add this feature in the future. (Synology offers the [E10M20-T1](https://amzn.to/37yKtnv) adapter which provides dual M.2 SSD slots _and_ 10 GbE networking on a PCIe expansion card.)
  - I haven't tested other 10 GbE adapters in the unit, but ASUSTOR mentioned they have broad compatibility, and even older cards I have used in the past like a ConnectX3 SFP card _should_ work.

## Conclusion

My Dad's radio station doesn't yet utilize the full performance and capabilities of the Lockerstor 4RS. But the form factor and features are perfect for a small business like his radio station—they have rack space, and were formerly storing files on desktop hard drives attached to one of the studio PCs.

This new rackmount server comes with an adequate and supported storage OS, and the hardware is quiet and works great for their needs.

The price tag ($999) is similar to Synology's unit, but may be a better value considering the upgraded 2.5 GbE ports and larger amount of default RAM (plus greater expandability). QNAP offers an even smaller unit with one built-in 10 Gbps port for a little lower price, but the hardware on it is different enough from the Synology and ASUSTOR models that it's harder to directly compare.

Whether you want to DIY a storage server or go with something like the ASUSTOR Lockerstor 4RS is a personal decision. I think this rackmount server is priced well for the intended audience: SMBs and power users who want a reliable NAS, but don't have the knowledge or time to build something more custom, and want long-term support.

ASUSTOR's been pretty good with supporting even their oldest hardware so far. Even though the recent targeted Deadbolt attacks have given both QNAP and ASUSTOR users something to worry about, those who use a NAS—no matter who makes it—as _part_ of a data storage system, and not _the only_ data storage system, can rest easy with a unit like the Lockerstor 4RS in their rack.

> Note: ASUSTOR also offers a 4-drive 1U dual-PSU unit (the 4RD), as well as a 12-drive 2U unit (the 12RD). A [rail kit](https://shop.asustor.com/index.php?route=product/product&path=25&product_id=51) can be purchased from ASUSTOR's Accessories Store.
