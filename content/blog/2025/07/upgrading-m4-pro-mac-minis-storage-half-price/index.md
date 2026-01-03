---
nid: 3478
title: "Upgrading an M4 Pro Mac mini's storage for half the price"
slug: "upgrading-m4-pro-mac-minis-storage-half-price"
date: 2025-07-11T14:00:11+00:00
drupal:
  nid: 3478
  path: /blog/2025/upgrading-m4-pro-mac-minis-storage-half-price
  body_format: markdown
  redirects: []
tags:
  - m4
  - mac
  - mac mini
  - mini
  - ssd
  - upgrade
  - video
  - youtube
---

A few months ago, I [upgraded my M4 Mac mini from 1 to 2 TB of internal storage](https://www.youtube.com/watch?v=eLtE2kMTVOQ), using a then-$269 DIY upgrade kit from ExpandMacMini.

At the time, there was no option for upgrading the M4 Pro Mac mini, despite it _also_ using a [user-replaceable](https://support.apple.com/en-us/121003), socketed storage drive.

{{< figure src="./m4-pro-mac-mini-internal-guts.jpg" alt="M4 Pro Mac mini guts with M4-SSD 4TB Upgrade Installed" width="700" height="394" class="insert-image" >}}

But the folks at [M4-SSD](https://m4-ssd.com) reached out and asked if I'd be willing to test out one of their new M4 Pro upgrades, in this case, upgrading the mini I use at the studio for editing from a stock 512 GB SSD to _4 TB_.

I said yes, and here we are!

I documented the entire upgrade—along with taking my old M4 mini 1TB SSD and putting it in my _Dad's_ M4 mini—in today's video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/cqmPjO-iHLo" frameborder='0' allowfullscreen></iframe></div>
</div>

But please continue reading, if you prefer text over video, like I do :)

The [upgrade process](https://www.ifixit.com/Guide/How+to+Replace+the+SSD+in+your+Mac+mini+(2024)/180199) itself is straightforward (if you've ever worked on laptop hardware before, at least), though removing the rear plastic cover (which also has the power button attached) is a bit annoying.

There are four metal pegs that are retained in clips in the bottom metal cover, and you have to slide a thin piece of metal / pry tool into the very minimal gap between the plastic bottom cover and the aluminum case, then pry it up. And if you're not careful on that step, you'll not only scratch the aluminum (and maybe crack the plastic bottom), but there's a good chance you rip the fragile (and tiny) power button connector too!

Besides that, it's a matter of removing a number of small torx screws; all the bits I needed were present in the cheapest iFixit assortment I have at my desk.

The only substantial difference between the M4 and M4 Pro mini SSD is the size and relative location—the M4 Pro has a much longer slot, a little more than a standard 2242-size NVMe SSD, while the M4 has a shorter slot, closer to a 2230.

## DFU Restore

Speaking of standards... you _have_ to do a full DFU (Device Firmware Update) restore, because unlike conventional M.2 NVMe storage, the M4 uses a proprietary connector, a proprietary-sized slot, and splits up the typical layout—the card that's user-replaceable is actually just flash chips and supporting power circuits, while the storage controller (the NVMe 'brains') is part of the M4 SoC (System on a Chip). Apple could use standard NVMe slots, but they seem to think the controller being part of the SoC brings better security... it certainly doesn't bring any cost savings, resiliency in terms of quick recovery from failure in the field, or performance advantage!

{{< figure src="./m4-pro-mac-mini-internal-drive.jpg" alt="M4 Pro Mac mini upgraded DIY drive 4TB" width="700" height="394" class="insert-image" >}}

Since DFU restore is necessary, in my earlier video, I suggested you need an Apple Silicon mac (M1 or later) as the other computer.

But I was corrected by my viewers, who mentioned you can use many Intel Macs as well—I believe as long as a T2 chip is present, you're good to go. Just connect to the _middle_ Thunderbolt port on the rear of the Mac mini, then press and hold the power button while plugging it into AC power. The other Mac should pop up an 'Allow this device to connect?' dialog and then you can proceed to the [DFU process](https://support.apple.com/en-us/108900) from there.

> As far as I'm aware, no Hackintosh or other computer can be made to do a DFU restore.

I've done three upgrades (two on M4 minis, one on an M4 Pro mini), and all three were easy. The second one, I thought I had an issue, but it was just a confirmation dialog that wound up _behind_ the active window.

## Performance

I decided to also use an external Thunderbolt 5 NVMe enclosure from M4-SSD along with my (rather expensive) 8TB Sabrent Rocket Q SSD, and do a performance comparison.

See the video at the beginning of this post for some more detail (like all the numbers from [AmorphousDiskMark](https://katsurashareware.com/amorphousdiskmark/) and [Blackmagic Disk Speed Test](https://apps.apple.com/us/app/blackmagic-disk-speed-test/id425264550?mt=12)), but here are the raw numbers for large file copy performance:

{{< figure src="./m4-pro-mac-mini-upgrade-benchmarks.png" alt="M4 Pro mac mini benchmark performance SSDs" width="700" height="394" class="insert-image" >}}

The upgraded 4TB module performed noticeably better in writes, likely because it has more flash chips on it to spread out the write activity. Reads were pretty close to the same, with minor variance in performance across different file sizes and access patterns.

The external TB5 drive was the laggard, but is still ridiculously fast (by my standards, editing 4K video). And it would likely be faster if I used a good PCIe Gen 4x4 drive (the Rocket Q is Gen 3x4).

But the internal storage on these Mac minis is very fast, and even better, very _consistently_ fast. The external Thunderbolt drive would slow down briefly every minute or so, after 100+ GB were copied—and I verified both with `smartctl` and [my thermal camera](https://amzn.to/3IlrX48) that the drive was not overheating.

{{< figure src="./m4-pro-mac-mini-thunderbolt-diskspeedtest-smartctl.jpg" alt="M4 Pro Mac mini thunderbolt diskspeedtest smartctl thermals" width="700" height="394" class="insert-image" >}}

This is likely due to the internal DRAM cache on the NVMe SSD not being able to keep up with the high transfer speeds over long periods of time.

## Conclusion

I was provided the [$699 M4 Pro 4TB SSD upgrade](https://store.m4-ssd.com/products/third-party-ssd-for-mac-mini-m4-pro?variant=45569474199706) by M4-SSD. It's quite expensive (especially compared to _normal_ 4TB NVMe SSDs, which range from $200-400)...

But it's not nearly as expensive as Apple's own offering, which at the time of this writing is _$1,200_!

{{< figure src="./m4-pro-mac-mini-apple-pricing.jpg" alt="Apple M4 Pro mac mini upgrade pricing 1200" width="700" height="394" class="insert-image" >}}
