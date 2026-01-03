---
nid: 3371
title: "4-way NVMe RAID comes to Raspberry Pi 5"
slug: "4-way-nvme-raid-comes-raspberry-pi-5"
date: 2024-05-01T15:59:58+00:00
drupal:
  nid: 3371
  path: /blog/2024/4-way-nvme-raid-comes-raspberry-pi-5
  body_format: markdown
  redirects: []
tags:
  - cm3588
  - geekworm
  - homelab
  - nvme
  - pi 5
  - raspberry pi
  - ssd
---

With the Raspberry Pi 5's exposed PCI Express connector comes many new possibilities—which I test and document in my [Pi PCIe Database](https://pipci.jeffgeerling.com/hats). Today's board is the [Geekwork X1011](https://geekworm.com/products/x1011), which puts four NVMe SSDs under a Raspberry Pi.

{{< figure src="./x1011-08-pi-nas-nvme-inland.jpeg" alt="Inland 256GB NVMe SSDs installed on X1011 on Raspberry Pi 5" width="700" height="auto" class="insert-image" >}}

Unlike the [Penta SATA HAT](/blog/2024/radxas-sata-hat-makes-compact-pi-5-nas) I tested last month, this carrier uses thinner and faster NVMe storage, making it a highly-compact storage expansion option, which has the added benefit of freeing up the top of the Pi 5 for other HAT expansion options.

{{< figure src="./x1011-01-raspberry-pi-5.jpeg" alt="Raspberry Pi 5 installed atop Geekworm X1011 NVMe SSD carrier" width="700" height="auto" class="insert-image" >}}

The board isn't without its flaws and oddities, though—for example, power is a little strange. I opted for a 27W GaN USB-C charger from Argon forty for my testing:

{{< figure src="./x1011-02-argon-gan-5v-usb-c.jpeg" alt="Argon GaN 27W USB-C charger" width="700" height="auto" class="insert-image" >}}

I noticed there was also a "DC5V" connector on the X1011, so I initially assumed I'd need to find a 5V DC barrel plug power supply, but when I went to [Geekworm's Wiki](https://wiki.geekworm.com/X1011), I found this line:

> Don't power the X1011 via DC powe [sic] jack and the Raspberry Pi5 via USB-C at the same time.

It seems like they have a bit of a dumb power circuit that might not have protection from backfeeding, so I would heed their caution and _not_ plug two power supplies in at the same time.

> Want a video instead? I reviewed this board with a little more detail over on my Level 2 Jeff YouTube channel. Watch here: [Tiny Pi NAS: It's impossible to recommend](https://www.youtube.com/watch?v=yLZET7Jhza8).

But how does the board get power from the Pi 5? Raspberry Pi maintains you shouldn't draw more than 5W through the PCIe FFC, so where does the board get up to 5A 5V power? It's through these [pogo pins](https://en.wikipedia.org/wiki/Pogo_pin):

{{< figure src="./x1011-pogo-power-pins.jpg" alt="X1011 Pogo Power Pins" width="700" height="auto" class="insert-image" >}}

Pogo pins aren't unheard of in Pi undermount boards. In fact, there's a grid of test points on the bottom of the Pi—5V power rail included—and tapping into them with a spring-loaded connector is a clever hack that avoids mechanical connectors or use of the GPIO header.

Personally I have run a couple Pi Zeros with pogo pin connections for USB and power before, and only had issues one time when one of the pins bent a little so wasn't making great contact. And I'm guessing Raspberry Pi doesn't finish off test point solder to a degree of precision where every pogo pin contact will be perfect... but it worked in my testing on _this_ board with _this_ Pi 5, so I won't complain too much.

If you're considering using this in a high-vibration environment, maybe look elsewhere; that's the achilles heel of even the best pogo pins!

{{< figure src="./x1011-03-pcie-ffc.jpeg" alt="Geekworm X1011 PCIe FFC with angled bends to bypass microSD card slot" width="700" height="auto" class="insert-image" >}}

Moving on to something that should be a lot less controversial, the FFC (Flat Flexible Cable) that connects the board to the Pi 5's PCIe header uses a double-90° design like I first saw in [Pimoroni's NVMe BASE](https://shop.pimoroni.com/products/nvme-base?variant=41219587178579), which allows for easy access to the microSD card slot on the edge of the Pi 5. I like that design, and the impedance-matched cable seems well designed and durable enough. Geekworm even includes two, in case you damage one or it gets flaky.

Back to something that is a little disappointing:

{{< figure src="./x1011-04-asm1184e-pcie-switch-chip.jpeg" alt="Geekworm X1011 ASM1184e PCIe Gen 2 switch chip" width="700" height="auto" class="insert-image" >}}

Because the Pi 5 only exposes one lane (x1) of PCI Express Gen 2, you need a PCI Express switch chip (much like a network switch) to split that single lane into four connections.

The ASM1184e is a solid, reliable PCIe Gen 2 switch, but it is limited to Gen 2 speeds (5 GT/sec), whereas the Pi's internal bus can be pushed to PCIe Gen 3 speeds (8 GB/sec).

Considering the speed of even cheaper NVMe SSDs, you're sacrificing that much more performance splitting up the lower Gen 2 bandwidth among four devices. In reality, the Pi's other IO is an even bigger bottleneck here (it only has 1 Gbps built-in Ethernet, though you can get 2.5 Gbps using a USB 3 adapter), so it's not as big a problem as it may seem. But it is a problem—across four NVMe SSDs in RAID 0, the maximum raw throughput will top out around 430 MB/sec:

| Benchmark | Result |
| --- | --- |
| iozone 4K random read | 46.43 MB/s |
| iozone 4K random write | 138.80 MB/s |
| iozone 1M random read | 418.14 MB/s |
| iozone 1M random write | 393.81 MB/s |
| iozone 1M sequential read | 430.45 MB/s |
| iozone 1M sequential write | 398.13 MB/s |

This is where a device like [Friendlyelec's CM3588](https://www.friendlyelec.com/index.php?route=product/product&product_id=294) shines—the RK3588 SoC used in it includes _four_ PCIe Gen 3 lanes, for a total of 32 GT/sec of bandwidth. That's... a lot more :)

{{< figure src="./x1011-05-thermals.jpeg" alt="Geekworm X1011 thermals with hot ASM1184 PCIe Gen 2 switch chip" width="700" height="auto" class="insert-image" >}}

The switch chip is also the hottest part of this entire setup, running at 55°C or so after an hour of repeated storage benchmarks in open air. If you put this in a case, I would highly recommend either a fan, or a heatsink over the chip to prevent any performance issues.

The drives themselves don't seem to heat up that much—but that's dependent on what NVMe SSDs you install.

{{< figure src="./x1011-06-inland-nvme-thermals.jpeg" alt="Geekworm X1011 NVMe SSD thermals" width="700" height="auto" class="insert-image" >}}

I put in some very inexpensive TLC drives suitable more for read-heavy use, some [Inland TN320](https://www.microcenter.com/product/661858/inland-tn320-256gb-ssd-nvme-pcie-gen-30x4-m2-2280-3d-nand-tlc-internal-solid-state-drive) SSDs I picked up at Micro Center. They seemed to stay under 50°C even after many read/write benchmarks, writing through a few TB of data in a ZFS RAIDZ1 array.

Interestingly, in addition to the four NVMe activity LEDs on top of the Geekworm board, the Inland SSDs actually have an integrated green LED, so no matter what way you flip the board, you'll get some [blinkenlights](https://en.wikipedia.org/wiki/Blinkenlights):

{{< figure src="./x1011-07-running-port-side-network.jpeg" alt="Geekworm X1011 with Raspberry Pi 5 - ports" width="700" height="auto" class="insert-image" >}}

Always welcome in my homelab.

I mentioned the [Friendlyelec's CM3588](https://www.friendlyelec.com/index.php?route=product/product&product_id=294) above—it's probably the most appropriate board to compare to, and [LTT did a video on it, testing OMV](https://www.youtube.com/watch?v=QsM6b5yix0U). So comparing on _price alone_, how do the boards stack up?

| Item | Pi 5 + X1011 | Friendlyelec CM3588 | 
| --- | --- | --- |
| 4x NVMe carrier board | $51 | $95 |
| SBC/SoM | $59 (4GB Pi 5) | $35 (4GB RK3588) |
| Power Supply | $10 | $10 |
| microSD (for boot) | $12 | $12 |
| NVMe Drives (4x 256GB) | $111.96 | $111.96 |
| **TOTAL** | **$243.96** | **$263.96** |

Pricing doesn't take into account durability, software support, or anything else. For example, you can already buy a [PoE HAT](https://amzn.to/3UDoFwO) for the Pi 5, meaning you could run this entire system over PoE. Running the CM3588 over PoE would require an external adapter to break out PoE power. And Pi OS already runs great with ZFS, OMV, and other storage solutions, though _neither_ of these builds runs more popular NAS OSes like Unraid (see latest [Unraid on Arm discussion](https://forums.unraid.net/topic/133935-is-arm-support-anywhere-in-the-making/)) or TrueNAS (see latest [TrueNAS on Arm discussion](https://forums.truenas.com/t/truenas-scale-on-arm-2024-thread/2706/4)).

That said, [I've been running vanilla ZFS on two Arm NASes](https://github.com/geerlingguy/arm-nas) in production for months, with zero hiccups and no extra overhead... so do you really need all the fancy chrome and shiny buttons one of those NAS UIs give you?

I also haven't found anyone designing a 3D case for the X1011 yet, but I'll update this post with a link to one if I do. There's a [CM3588 case design from sgofferj](https://github.com/sgofferj/CM3588-NAS-case) with space for two small fans.

One caveat: [until this firmware issue is resolved](https://github.com/raspberrypi/firmware/issues/1833), you can't _boot_ direct off an NVMe drive behind a PCIe switch (like on the X1011) without having the first stage bootloader on another storage device (like USB or microSD card). Hopefully that's resolved soon!

For the latest testing and info about this board, and other PCI Express devices for Raspberry Pi, check out the issue on GitHub: [Geekworm X1011 PCIe to Four M.2 NVMe SSD HAT](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/618).

Watch the that goes along with this blog post:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/yLZET7Jhza8 " frameborder='0' allowfullscreen></iframe></div>
</div>
