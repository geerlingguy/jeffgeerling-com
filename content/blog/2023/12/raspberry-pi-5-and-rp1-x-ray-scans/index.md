---
nid: 3332
title: "Raspberry Pi 5 and RP1 X-ray scans"
slug: "raspberry-pi-5-and-rp1-x-ray-scans"
date: 2023-12-07T15:02:23+00:00
drupal:
  nid: 3332
  path: /blog/2023/raspberry-pi-5-and-rp1-x-ray-scans
  body_format: markdown
  redirects:
    - /blog/2023/x-ray-scans-new-raspberry-pi-5-and-rp1
aliases:
  - /blog/2023/x-ray-scans-new-raspberry-pi-5-and-rp1
tags:
  - pi 5
  - raspberry pi
  - scan
  - xray
---

Following up on my [X-ray scans of the Raspberry Pi Zero 2 W](/blog/2021/look-inside-raspberry-pi-zero-2-w-and-rp3a0-au) two years ago, I had the opportunity to scan the Raspberry Pi 5, working with an electronics inspection lab:

{{< figure src="./raspberry-pi-5-transition-x-ray.jpg" alt="Raspberry Pi 5 Transition to X-ray" width="700" height="auto" class="insert-image" >}}

I posted [a video detailing everything I imaged on the board](https://www.youtube.com/watch?v=MoTSSTfPXEA), but in this blog post, I'll hit on the highlights—the new chips at the heart of the Pi 5: the BCM2712 SoC and the RP1 'southbridge'.

> **Aside**: [If you are Casetify](https://techcrunch.com/2023/11/27/dbrand-is-suing-casetify-over-stolen-designs/?guccounter=1&guce_referrer=aHR0cHM6Ly9kdWNrZHVja2dvLmNvbS8&guce_referrer_sig=AQAAAAsyaMKBmgkLtDZk76Xz60YpBcn1m0Zqy5yZSj61dcrHt3KTJkrhNDYovTHreaAvXCOC_ytxVN6NpapEILLNvXUfWfHeMk5UjwOdGCOZXYJXmIG69VVt0SkQX9TfmT1cCGq3GzPFWKmJomy9Ul2MbBxwtEImjATgDAio_K0fw-sq), then _yes_, I have retouched these images in a couple extremely minor ways to ensure I have digital provenance 😘.
>
> Oh, and I'm selling a [Pi 5 X-ray tee shirt](https://redshirtjeff.com/listing/x-ray-pi-5?product=46) and [hoodie](https://redshirtjeff.com/listing/x-ray-pi-5?product=212).

{{< figure src="./raspberry-pi-5-xray-black-jeff-geerling.jpg" alt="Raspberry Pi 5 X-ray white on black" width="700" height="auto" class="insert-image" >}}

The board layout has some radical departures from the earlier Pi 4—besides the Ethernet port and PoE pins swapping sides back to a Pi 3 and earlier arrangement, the majority of the middle of the board is dominated by expanded IO: 5 total PCIe lanes, LPDDR4x memory channels, and HDMI signals all routed through the SoC.

## BCM2712 Arm SoC

{{< figure src="./bcm2712-xray-raspberry-pi-5.jpg" alt="BCM2712 X-ray image of Raspberry Pi 5 SoC" width="700" height="auto" class="insert-image" >}}

The SoC at the heart of the Pi 5 is a new BCM2712 chip from Broadcom, with a VideoCore VII GPU and four Arm A76 CPU cores clocked at 2.4 GHz.

The package is much smaller than the total package dimension, and you can just make out some of the bonding wires around it in the image above.

I counted all the package solder balls so you don't have to—there are 586 pins coming off the BCM2712 (in a 25 x 25 BGA, with some pads empty). Those pins route signals to and from all parts of the Pi, but besides the dual 4K60-capable HDMI ports, a lot of that signaling goes through the 4 PCI Express lanes attached to the RP1 chip.

## RP1 Southbridge

{{< figure src="./rp1-xray-pcie-lanes-raspberry-pi-5.jpg" alt="RP1 PCIe lanes X-ray image of Raspberry Pi 5" width="400" height="auto" class="insert-image" >}}

Those lanes form a little '8-lane highway' on the surface of the Pi's PCB, with each differential pair holding a tiny set of capacitor 'cars' at one point or another along the route, making the highway analogy complete.

{{< figure src="./rp1-xray-top-raspberry-pi-5.jpg" alt="RP1 top X-ray image on Raspberry Pi 5" width="700" height="auto" class="insert-image" >}}

The RP1 itself is less than a quarter the size of the full package, with 265 total pins in its BGA, laid out in an 18 x 18 grid.

## Other tidbits

There are a few other parts of the board that were especially interesting, like the integrated WiFi antenna cut into the PCB itself:

{{< figure src="./wifi-antenna-pcb-raspberry-pi-5-xray.jpg" alt="Raspberry Pi 5 PCB antenna and WiFi and Bluetooth module" width="700" height="auto" class="insert-image" >}}

And also the new (and somewhat controversial) 5V 5A board power supply:

{{< figure src="./pmic-power-stage-rasperry-pi-5-xray.jpg" alt="Raspberry Pi 5 board power supply" width="700" height="auto" class="insert-image" >}}

To see the rest of the X-ray images, please [watch the video](https://www.youtube.com/watch?v=MoTSSTfPXEA) over on my YouTube channel. I hope to get more posted up in full resolution at some point, maybe on Flickr or another blog post, but for now, the full set is visible in that video.
