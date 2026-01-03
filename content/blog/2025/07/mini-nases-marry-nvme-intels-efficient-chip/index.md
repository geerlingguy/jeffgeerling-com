---
nid: 3476
title: "Mini NASes marry NVMe to Intel's efficient chip"
slug: "mini-nases-marry-nvme-intels-efficient-chip"
date: 2025-07-04T14:00:57+00:00
drupal:
  nid: 3476
  path: /blog/2025/mini-nases-marry-nvme-intels-efficient-chip
  body_format: markdown
  redirects: []
tags:
  - aiffro
  - beelink
  - gmktec
  - homelab
  - linux
  - mini rack
  - nas
  - reviews
  - storage
  - video
  - youtube
---

{{< figure src="./mini-nas-lineup-with-coffee-mug.jpg" alt="Mini NAS lineup with Coffee Mug" width="700" height="394" class="insert-image" >}}

I'm in the process of rebuilding my homelab from the ground up, moving from a 24U full-size 4-post rack to a [mini rack](https://mini-rack.jeffgeerling.com).

One of the most difficult devices to downsize (especially _economically_) is a NAS. But as my needs have changed, I'm bucking the trend of all [datahoarders](https://www.reddit.com/r/DataHoarder/) and I need _less_ storage than the 120 TB (80 TB usable) I currently have.

It turns out, when you stop running an entire YouTube channel in your home (I'm in a studio now), you don't need more than a few terabytes, so my new conservative estimate is _6_ terabytes of usable space. That's within the realm of NVMe SSD storage for a few hundred bucks, so that's my new target.

Three new mini NASes were released over the past year that are great candidates, and I have relationships with all three companies making them, so I am lucky to have been offered review units of each:

  - [GMKtec G9](https://amzn.to/3Tb9Kso)
  - [Aiffro K100](https://www.aiffro.com/products/all-ssd-nas-k100)
  - [Beelink ME mini](https://amzn.to/4lvu6Zv)

I've compiled _all_ my experience with the three NASes into one concise YouTube video, which I've embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/8VBnxEQKG3o" frameborder='0' allowfullscreen></iframe></div>
</div>

However, I thought I'd at least give a few notes here for those interested in reading, not watching.

Generally, all three mini NASes use an Intel N100/N150 chip, and divvy up its 9 PCIe Gen 3 lanes into 4 (or in the Beelink's case, 6) M.2 NVMe SSD slots. They all have 2.5 Gbps networking, though the GMKtec and Beelink have _dual_ 2.5 Gbps NICs.

The difference is in the execution, and each box has one or two minor issues that keep me from giving a whole-hearted recommendation. When you're dealing with tiny devices, there's _always_ a compromise. So you have to see which compromises you're most willing to deal with. (Or just buy a full size NAS if you have the space/power for it.)

## GMKtec G9

{{< figure src="./gmktec-g9-disassembled-cooling-issues.jpg" alt="GMKtec G9 cooling issues - disassembled" width="700" height="394" class="insert-image" >}}

I previously reviewed this NAS in April; see my blog post [The (almost) perfect mini NAS for my mini rack](/blog/2025/almost-perfect-mini-nas-my-mini-rack).

That 'almost' is doing a lot of heavy lifting, though; there were inherent cooling issues if you ran the box with four NVMe drives, and it was bad enough GMKtec went through a design revision.

Their newer version of the G9 has a much larger cooling vent on the side, and I believe they may have tweaked some other aspects of the design. I'm not sure how it ends up, though, so I'll have to post an updated review if I can get my hands on one of these updated models.

## Aiffro K100

{{< figure src="./aiffro-k100-smb-performance.jpg" alt="Aiffro K100 SMB performance" width="700" height="394" class="insert-image" >}}

The K100 is even smaller than the G9, and it keeps things cool much better, likely owing to much more ventilation on the sides, a heatsink that covers VRMs (Voltage Regulation Modules) and some of the other hot chips, and a full metal enclosure.

The major downside is despite costing $299 (over $100 more than the G9's base spec), it drops eMMC (so you have to install an OS on one of the 4 NVMe SSDs, or on an external USB stick), and drops WiFi (this is wired only—and a single 2.5 Gbps port versus 2 on the other two mini NASes.

The BIOS is also very light on customization, only really allowing tweaking the power restore behavior and performance profile.

But it's very quiet (less than 37 dBa under load), absolutely tiny, and uses the least power of all the Intel mini NASes I tested.

## Beelink ME mini

{{< figure src="./beelink-me-mini-4-nvme.jpg" alt="Beelink ME mini with 4 Kingspec NVMe SSDs" width="700" height="394" class="insert-image" >}}

Speaking of quiet, the ME mini is even more quiet. It's not _silent_, but the larger fan and 'chimney' heatsink design (reminiscent of Apple's Trash Can Mac) mean it can keep from throttling even in 'performance' mode indefinitely—and barely scratch 35 dBa while doing so.

It has not 4 but _6_ NVMe slots, though 5 of those slots are PCIe Gen 3 x1 (one lane of bandwidth is 8 GT/sec), and the last slot is x2 (two lanes).

If you order one with a Crucial SSD pre-installed, it will be installed in that last x2 slot for maximum performance—and the test unit I was shipped came with Windows 11 preinstalled.

But it has built-in eMMC (64 GB), and I installed Ubuntu on that for my testing. Another nice feature is a built-in power supply, which is quite rare on these mini PCs. Often you buy the thing based on the size of the mini PC, then hanging out back, there's a DC power supply the same size as the mini PC!

Not here, it's got a small power supply tucked inside one part of the heatsink, though I'm not sure how much thermal transfer there is between the heatsink and the power supply. I didn't encounter any overheating issues, though, and even with the preinstalled Crucial SSD only touching the thermal pad where the NVMe controller chip sits (there was an air gap between the thermal pad and all the flash storage chips), I didn't have any concerns over thermals.

It did run a little hotter overall than the K100, but it was also in full performance/turbo boost mode, whereas the K100 comes from the factory with a more balanced power profile.

## Conclusion

The G9 is definitely the winner in terms of price, but the cooling tradeoffs at least with the initial revision I reviewed were not worth it, because it would lock up and reboot if it overheated. The ME mini is currently $209 (starting) on pre-sale, but that price could go up:

{{< figure src="./mini-nases-graph-price.jpg" alt="Mini NAS pricing graph" width="700" height="394" class="insert-image" >}}

All three NASes would perform fine for my homelab needs, giving at least around 250 MB/sec of read/write performance, though the Beelink seems to suffer a little splitting out all those NVMe slots with x1 bandwidth:

{{< figure src="./mini-nases-graph-network-file-copy.jpg" alt="Mini NAS Samba network file copy performance graph" width="700" height="394" class="insert-image" >}}

And as I mentioned earlier, the K100 was definitely the most efficient, partly due to it shipping with a balanced power profile instead of 'performance', and also by the fact it ditches features like WiFi and eMMC which eat up a little more power:

{{< figure src="./mini-nases-graph-power-draw.jpg" alt="Mini NAS power draw graph" width="700" height="394" class="insert-image" >}}

In the end, there's no clear winner for all cases. The GMKtec is the budget option, and supposedly they have a new thermal design that should solve the stability issues I was encountering. The K100 is tiny, uses the least energy, and runs the coolest... but is also the most expensive, and has no built-in eMMC. The Beelink is the most expandable, and is currently cheaper than the K100, but that's a pre-sale price. And the extra drive slots means each drive only taps into one lane of bandwidth instead of _two_.

So if you're in the market for a tiny homelab storage server, pick one based on your own requirements.

For me, I'm leaning towards the K100, but only if I can find a good deal on 4 TB NVMe SSDs, because I need at least 6 TB of usable space in a RAIDZ1 array.
