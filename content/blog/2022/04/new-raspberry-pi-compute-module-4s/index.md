---
nid: 3198
title: "New Raspberry Pi: Compute Module 4S"
slug: "new-raspberry-pi-compute-module-4s"
date: 2022-04-04T21:47:35+00:00
drupal:
  nid: 3198
  path: /blog/2022/new-raspberry-pi-compute-module-4s
  body_format: markdown
  redirects: []
tags:
  - cm3
  - compute module
  - parts shortage
  - raspberry pi
  - video
  - youtube
---

> Update: The [Compute Module 4S is now listed on Raspberry Pi's website](https://www.raspberrypi.com/products/compute-module-4s/). But they state it "is not for general sale."

Strange times beget strange things.

And that's an apt description of the new Raspberry Pi Compute Module 4S:

{{< figure src="./Differences-Compute-Module-Raspberry-Pi.png" alt="Raspberry Pi Compute Module 3+ to 4S Differences" width="700" height="482" class="insert-image" >}}

The above chart is from [Revolution Pi's page announcing the RevPi S and SE](https://revolutionpi.com/new-s-series-and-se-series/), which are updates to their popular CM3+-based industrial DIN rail computers.

They've been working on a RevPi 4 built around the Compute Module 4 that was announced in 2020, but after many delays, it seems they brokered a deal with Raspberry Pi to use a cut down Compute Module 4S, which eschews not features like gigabit Ethernet and PCI Express, as well as the entire _form factor_ of the CM4.

The CM4S mashes a BCM2711 SoC into the Compute Module 1, 3, and 3+ form factor—which was used for years until the switch to 2x 100-pin board-to-board connectors on the CM4 (pictured on the left):

{{< figure src="./cm3-cm4-connectors.jpeg" alt="Compute Module 4 and CM3+ edge connectors and board to board SO-DIMM 200-pin" width="700" height="468" class="insert-image" >}}

I'm guessing the reason this board was produced is because Raspberry Pi can't secure enough of the older 40nm process SoCs that powered older-generation Pis.

Instead of leaving industrial customers who designed around the old SO-DIMM form factor out to dry, they updated the design to use the 28nm BCM2711, which _does_ seem to be available in quantities [surpassing 500,000 per month currently](https://www.raspberrypi.com/news/production-and-supply-chain-update/).

So far, I don't know if the CM4S will be made available to anyone outside of Revolution Pi, though I've posted on the forum asking as much: [New Compute Module 4S? [Raspberry Pi Forums]](https://forums.raspberrypi.com/viewtopic.php?p=1990528).

While the CM3+ and earlier Compute Module models weren't quite as popular as the CM4 is today (owing to their slower SoCs and weaker IO), they _are_ in a lot of embedded devices. I'm sure many customers would love a drop-in upgrade to the BCM2711, with it's doubled CPU performance, faster GPU, and doubled memory bandwidth.

For a little more detail on the CM4S, check out my latest YouTube video, embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/MAMoPVOR38U" frameborder='0' allowfullscreen></iframe></div>
</div>
