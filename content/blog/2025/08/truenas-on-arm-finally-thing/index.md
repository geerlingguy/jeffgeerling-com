---
nid: 3487
title: "TrueNAS on Arm is finally a thing"
slug: "truenas-on-arm-finally-thing"
date: 2025-08-22T19:43:56+00:00
drupal:
  nid: 3487
  path: /blog/2025/truenas-on-arm-finally-thing
  body_format: markdown
  redirects: []
tags:
  - ampere
  - arm
  - homelab
  - linux
  - raspberry pi
  - server
  - truenas
  - zfs
---

A few years ago, I admit it was rare to find someone running Arm hardware more powerful than a Raspberry Pi in a homelab (or more serious) setting, outside of cloud providers running Ampere or custom Arm CPUs.

{{< figure src="./radxa-penta-sata-hat-pi-5.jpeg" alt="Radxa Penta SATA HAT on Pi 5" width="700" height="394" class="insert-image" >}}

But as Pis and Rockchip boards have become more powerful (and efficient), and Apple's M-series silicon has become more interesting (the M4 mini being an excellent value proposition for a quiet, tiny server), and even Ampere Altra pricing coming down a bit since it's an 'old' server CPU now, still offering 64 or 128 lanes of PCIe Gen 4... I don't think I'm weird in suggesting Arm is a viable platform for reliable, even powerful servers.

Even for storage.

I had posted two separate threads in iXsystems' (now just 'TrueNAS') forums about potential Arm support for TrueNAS Scale, as I already had my own [Arm NAS project](https://github.com/geerlingguy/arm-nas) running for a while, deploying ZFS and replication across an [Ampere Altra 32-core rackmount server](/blog/2024/building-efficient-server-grade-arm-nas) and a [Raspberry Pi 5 with four SATA SSDs](/blog/2024/radxas-sata-hat-makes-compact-pi-5-nas).

One sticking point has always been UEFI and Arm SystemReady support, as each Arm board needed customized Linux ISOs to run with specialized Device Trees. But that's slowly changing, as you can buy the [Radxa Orion O6](/blog/2025/radxa-orion-o6-brings-arm-midrange-pc) with SystemReady support and run any flavor of vanilla Linux, or even Windows on Arm, just like on the Ampere Altra/Altra Max servers I've tested.

You can even set up [UEFI on a Pi 5](https://github.com/NumberOneGit/rpi5-uefi) with support for at least _some_ of the hardware—enough for many use cases—with vanilla Linux installs...

But TrueNAS was always a holdout, until recently. A few people were mentioning the thread [TrueNAS on ARM - Now Availalbe](https://forums.truenas.com/t/truenas-on-arm-now-available/49160/15), where forum user Joel mentions [his fork with Arm support](https://git.jmay.us/truenas/).

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/GryCOpcglyI" frameborder='0' allowfullscreen></iframe></div>
</div>

I hope to give it a spin soon, but I at least wanted to raise some awareness since I think this is a cool development, and hopefully will be adopted by TrueNAS proper at some point, so we can build tinier and more efficient TrueNAS servers, instead of having to tweak ZFS by hand on our own, without TrueNAS's fancy install wizard and UI...

[Update: Also I'm guessing [this video interviewing the dev who worked on the fork](https://www.youtube.com/watch?v=tmaNtEjpdoA) is the reason why so many people mentioned this to me today. Definitely worth a watch!]
