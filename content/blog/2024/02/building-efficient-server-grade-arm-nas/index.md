---
nid: 3347
title: "Building an efficient server-grade Arm NAS"
slug: "building-efficient-server-grade-arm-nas"
date: 2024-02-11T14:01:13+00:00
drupal:
  nid: 3347
  path: /blog/2024/building-efficient-server-grade-arm-nas
  body_format: markdown
  redirects: []
tags:
  - ampere
  - arm
  - arm64
  - asrock rack
  - hardware
  - hl15
  - homelab
  - nas
  - noctua
  - video
  - youtube
---

{{< figure src="./hl15-asrock-rack-motherboard-noctua-ampere-altra-fan.jpg" alt="HL15 with ASRock Rack Motherboard and Noctua Ampere Altra CPU Cooler installed" width="700" height="auto" class="insert-image" >}}

It's not _cheap_, but it's _efficient_. At least, that's my hope.

Over the past few months, I worked with a number of vendors to assemble what I _hope_ will make an efficient but high-performance arm64 NAS. In the video embedded below, I've put together the following (some of these links are affiliate links):

  - Motherboard: [ASRock Rack ALTRAD8UD-1L2T](https://reurl.cc/qrnXNp) ([specs](https://reurl.cc/67jk0V))
  - Case: [45Homelab HL15](https://store.45homelab.com/configure/hl15) (backplane + PSU)
  - PSU: [Corsair RM750e](https://amzn.to/3OyDQ79) (included with HL15)
  - RAM: [4x Samsung 16GB 1Rx4 ECC RDIMM M393A2K40DB3-CWE PC25600](https://amzn.to/49lCtkb)
  - NVMe: [Kioxia XG8 2TB NVMe SSD](https://amzn.to/3Uzag5d)
  - CPU: [Ampere Altra Q32-17](https://amperecomputing.com/briefs/ampere-altra-family-product-brief)
  - SSDs: [4x Samsung 8TB 870 QVO 2.5" SATA](https://amzn.to/3OylbZk)
  - HDDs: [6x Seagate EXOS 20TB SATA HDD](https://amzn.to/3OA2CDM)
  - HBA: [Broadcom MegaRAID 9405W-16i](https://amzn.to/3srcZOh)
  - Power: [Comeap PCIe to 8-pin CPU adapter](https://amzn.to/3Sx52o4) (to supplement the two CPU power plugs that came with the RM750e)
  - Cooler: [Noctua NH-D9 AMP-4926 4U](https://noctua.at/en/nh-d9-amp-4926-4u)
  - Case Fans: [6x Coolerguys CG12025M12B2-3Y 120mmx25mm](https://amzn.to/42tTwhD) (included with HL15)

ServeTheHome [covered the ASRock Rack ALTRAD8UD-1L2T motherboard](https://www.servethehome.com/asrock-rack-altrad8ud-1l2t-review-this-is-the-ampere-arm-motherboard-you-want/), as well as the [prototype Ampere Altra / Altra Max Noctua CPU coolers](https://www.servethehome.com/making-arm-desktops-viable-ampere-altra-noctua-nh-d9-amp-4926-4u-and-nh-u14s-amp-4926/), but if you want some raw footage of the assembly process and some of my unfiltered thoughts, check out my video putting together this machine:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Hz5k5WgTkcc" frameborder='0' allowfullscreen></iframe></div>
</div>

I won't be posting a full review of the system yet, because hardware is only half the equation—and even that isn't set in stone.

> **Note**: I was provided hardware for this build by 45Drives, ASRock Rack, Noctua, and Ampere. So take my opinions with all that in mind. Besides the equipment, no other money exchanged hands and none of these organizations had any say in the contents of this blog post or my YouTube video.

My power budget for this machine is around 100W idle, and right now it sits just over 150W. I think I can get it down below 100W, and some of that will be achieved with hardware tweaks (and a few possible substitutions), and maybe some in software.

{{< figure src="./seagate-exos-hdd-6x-in-hl15-45homelab-server-nas.jpg" alt="Seagate EXOS 20TB HDDs in HL15" width="700" height="auto" class="insert-image" >}}

Regarding the hardware itself, here are some of my initial thoughts after completing this build:

  - The 45Homelab HL15 case seems ideal for ATX and EATX motherboards. This 'deep micro ATX' motherboard is a bit cramped towards the plug-side... it _works_, but I think another cm or two of clearance would be better for it.
  - I had an early unit off 45Drive's production run of the HL15, and my unit had a mis-wired power button; it seems like [this problem was noted and fixed](https://forum.45homelab.com/t/power-button-doesnt-work/740/11).
  - The ASRock Rack motherboard came with OpenBMC, and it mostly worked great out of the box. I did experience a few bugs with the popout KVM window, but closing it and re-opening it always fixed the problems.
  - The HL15 includes _six_ CoolerGuys fans running at full speed (no PWM control). It would be nice if their fan power hub allowed PWM passthrough so the fans wouldn't run full blast if not needed... but that's not how it comes from the factory. It is billed as a 'quiet' system—and it is, compared to enterprise gear. But I may modify the cooling to make it half as quiet still, even though it'll go in a server closet.
  - For RAM, [make sure you buy _RDIMM_ memory sticks](https://forums.servethehome.com/index.php?threads/ampere-altra-q64-22-asrock-rack-altrad8ud-does-not-post-or-power-on.42699/), not _UDIMM_.
  - If you're building your own system, and want to throw in any other parts than what I've listed, please take a look at [Ampere's compatibility lists](https://amperecomputing.com/customer-connect/products/mt-jade), as they have gone through the hassle of validating many different types of hardware on their platform already. If it hasn't been tested, that doesn't mean it won't work, but there's a better chance of success if you use things that are validated.

{{< figure src="./ampere-altra-q32-17-cpu.jpg" alt="Ampere Altra Q32-17 CPU" width="700" height="auto" class="insert-image" >}}

If you would like to replicate my build, at this point everything _besides the Noctua fans_ is available at retail—see the links earlier in this post. The ASRock Rack motherboard keeps going in and out of stock at NewEgg, but I'm assured if you place a backorder, new batches are shipping regularly now.

An Ampere Altra-based system like the one I built isn't a performance champ, but for certain use cases where efficiency and tons of PCIe lanes are requirements, Ampere's existing platform may still pack a punch against AMD and Intel's similarly-priced CPUs.
