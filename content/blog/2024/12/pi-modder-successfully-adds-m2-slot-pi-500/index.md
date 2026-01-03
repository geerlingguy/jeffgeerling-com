---
nid: 3428
title: "Pi modder successfully adds M.2 slot to Pi 500"
slug: "pi-modder-successfully-adds-m2-slot-pi-500"
date: 2024-12-13T16:59:08+00:00
drupal:
  nid: 3428
  path: /blog/2024/pi-modder-successfully-adds-m2-slot-pi-500
  body_format: markdown
  redirects: []
tags:
  - hacks
  - hardware
  - nvme
  - pi 500
  - raspberry pi
  - ssd
---

As I briefly mentioned yesterday, someone [mentioned in this blog's comments](/comment/34602#comment-34602) a successful M.2 socket installation on the empty header on the Pi 500 ([something I attempted, rather poorly!](https://www.youtube.com/watch?v=omYWRb1dLA4)). With a few added components, and 3.3V supplied to a pad on the bottom via a bench power supply, the M.2 slot works just fine, allowing the use of NVMe SSDs or [other PCIe devices](https://pipci.jeffgeerling.com).

{{< figure src="./pi-500-ssd-console-output.jpg" alt="Pi 500 NVMe dmesg boot info" width="700" height="auto" class="insert-image" >}}

Indeed, this person emailed me further proof, along with notes for anyone wishing to follow in their footsteps.

First, solder on four minuscule capacitors (rating may be gleaned off the CM5 IO Board schematics, I think?) on the PCIe lines heading to the NVMe slot. These are _incredibly_ small, so a good microscope and decent SMD soldering skills are pretty necessary.

{{< figure src="./pi-500-ssd-nvme-data-caps.jpg" alt="Pi 500 NVMe capacitors PCIe data lines" width="700" height="auto" class="insert-image" >}}

The M.2 socket is comparatively easy—though that didn't stop me from making a mess of mine, which did not look _nearly_ as nice as the one above!

Then, using a bench power supply, apply +3.3V to the indicated pad in red, and ground to the pad in blue, and boot up the Pi 500.

{{< figure src="./pi-500-ssd-power-pads.jpg" alt="Pi 500 SSD power pads bottom" width="700" height="auto" class="insert-image" >}}

If you don't see the device right away, you may need to [enable the PCIe connection and set it to Gen 3 speed](/blog/2023/forcing-pci-express-gen-30-speeds-on-pi-5) in your boot config.

Regarding the ICs required to get this working _without_ a bench power supply:

> Now I need to figure out which DC/DC converter they used on the backside of the PCB. It needs to be something with 3.3V and ENABLE functionality, because they need to disable power to ssd during Pi500 power down.

<s>Maybe something could be gleaned from the [CM5 IO Board Design Files](https://pip.raspberrypi.com/categories/1098-design-files)?</s> [According to Bluesky user @eliasrm.bsky.social‬](https://bsky.app/profile/eliasrm.bsky.social/post/3ld7cpziit222), it could be a [AP3441SHE-7B](https://www.digikey.com/en/products/detail/diodes-incorporated/ap3441she-7b/9765636). I also bought [this M.2 socket](https://www.digikey.com/en/products/detail/attend-technology/123A-30M00/23626211), not sure on the other tiny components required but please feel free to post in the comments!

> **Update**: X user [@ChoptecOfficial put the whole circuit together](https://x.com/ChoptecOfficial/status/1868350222671478982), and can run it all of the Pi 500's internal power supply.

And the post from yesterday concluded with:

> I intend to use it as a second linux PC, NVMe SSD is a must!

Indeed. I think for most of us, seeing the pads there, but unpopulated, was a giant head-scratcher. The Pi 500 would've been more of a slam-dunk win with the slot in place, even if empty.
