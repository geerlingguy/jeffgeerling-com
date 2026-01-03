---
nid: 3149
title: "Mini-ITX Seaberry adds 11 PCIe slots to a Raspberry Pi"
slug: "mini-itx-seaberry-adds-11-pcie-slots-raspberry-pi"
date: 2021-11-24T15:00:31+00:00
drupal:
  nid: 3149
  path: /blog/2021/mini-itx-seaberry-adds-11-pcie-slots-raspberry-pi
  body_format: markdown
  redirects:
    - /blog/2021/alftels-seaberry-adds-11-pcie-slots-raspberry-pi
    - /blog/2021/alftels-mini-itx-seaberry-adds-11-pcie-slots-raspberry-pi
aliases:
  - /blog/2021/alftels-seaberry-adds-11-pcie-slots-raspberry-pi
  - /blog/2021/alftels-mini-itx-seaberry-adds-11-pcie-slots-raspberry-pi
tags:
  - alftel
  - cm4
  - compute module
  - pcie
  - raspberry pi
  - reviews
  - seaberry
  - video
  - youtube
---

Since the Compute Module 4 came along last year, there have been a few projects that use it that make me do a double-take: _They did **what** with a Pi?_

{{< figure src="./alftel-seaberry-board-cm4-top.jpeg" alt="Alftel Seaberry mini ITX board for the Raspberry Pi Compute Module 4 - top" width="700" height="467" class="insert-image" >}}

Alftel's [Seaberry](https://www.tindie.com/products/alftel/seaberry-pi-cm4-carrier-board/) is a carrier board for the CM4 in the Mini ITX form factor that adds on _eleven_ PCI Express slots:

  - 1 x16 slot (with x1 lane) in the standard ITX location
  - 1 x1 slot on board edge
  - 4 mini PCIe slots
  - 4 M.2 E-key slots (with dual PCIe lines so you can run specialty cards like dual-TPU accelerators)
  - 1 M.2 M-key slot for NVMe SSD

The rear of the board also has a decent mix of built-in IO, including a Cisco-style serial console cable you can use with an [easy-to-find USB adapter](https://amzn.to/3csnhXa) so you can [attach to a Raspberry Pi's Serial Console (UART) for debugging](https://www.jeffgeerling.com/blog/2021/attaching-raspberry-pis-serial-console-uart-debugging).

I've been using the board for a couple weeks, even installing it inside my smallest ITX PC case, a [Goodisory MX01](https://amzn.to/3xnJmj9). This is the first Pi board I've used that fits in a standard PC form factor, marking the first time I've been able to build a 'custom PC' with a Pi, using standardized components and not requiring extra time strapping together a makeshift or 3D-printed case:

{{< figure src="./seaberry-inside-mini-itx-case.jpg" alt="Seaberry installed in mini ITX case" width="507" height="337" class="insert-image" >}}

And the Seaberry needs all that room, to jam in all the ports! I tested an [Intel i350 dual-gigabit LAN card](https://pipci.jeffgeerling.com/cards_network/jetway-jadmpedila-mini-pcie-lan.html), a [Dual-TPU Coral M.2 Accelerator](https://pipci.jeffgeerling.com/cards_m2/coral-m2-accelerator-dual-edge-tpu.html), a [KIOXIA XG6 M.2 NVMe SSD](https://pipci.jeffgeerling.com/cards_m2/kioxia-xg6-m2-nvme-ssd.html), a [Compex WLE200NX 802.11n WiFi card](https://pipci.jeffgeerling.com/cards_network/compex-wle200nx.html), an [Intel AX210 WiFi 6E card](https://pipci.jeffgeerling.com/cards_network/intel-ax210-wifi-6e.html), a [dual SATA controller](https://pipci.jeffgeerling.com/cards_storage/iocrest-mini-pcie-dual-sata.html), and more—_and everything worked_ (more or less...).

Many cards have built-in drivers in Pi OS—the NVMe drive and the SATA SSD I plugged in worked right away, and required no custom drivers or kernel rebuilds. (For power, the board also includes a four-pin berg header to power SATA drives and other peripherals).

Cards like Intel's AX210 required the installation of custom firmware and Intel's driver, but worked great afterwards (giving me over 1 Gbps wireless on my home's WiFi 6 network!).

Google's Coral TPU cards still _don't_ work, unfortunately—the PCI Express implementation on the BCM2711 seems to not handle some of the memory access patterns it needs—but that brings me to another feature of the Seaberry (and many other CM4 boards): it is also supposedly compatible with [Radxa's CM3](https://wiki.radxa.com/Rock3/CM3) and [Pine64's SOQuartz](https://wiki.pine64.org/wiki/SOQuartz), two 'pin compatible' replacements for the CM4.

I have a CM3 and am awaiting shipment of the SOQuartz, so I'll test them out later this year.

{{< figure src="./amd-radeon-gpu-in-seaberry-motherboard.jpg" alt="AMD Radeon GPU graphics card on Seaberry Raspberry Pi CM4 carrier" width="600" height="338" class="insert-image" >}}

The other type of card I'm keen to get working with ARM64 SBCs is any kind of graphics card—mostly for the fun of it. I've struggled mightily to get AMD's `radeon` and `amdgpu` drivers working, and Nvidia's black box driver also has the same problem with the CM4—random hard lockups and kernel panics.

Anyways, the Seaberry is the perfect platform for my testing—and I even installed [Alftel's 12-card M.2 carrier board](https://pipci.jeffgeerling.com/cards_m2/alftel-12x-pcie-m2-carrier-board.html) in the thing, so I could have 20 PCI Express devices wired into the Pi at once.

{{< figure src="./seaberry-with-alftel-12-slot-carrier.jpg" alt="Alftel Seaberry with 12-slot PCIe carrier board" width="600" height="338" class="insert-image" >}}

Doing so also uncovered one limitation with the CM4 (besides the anemic x1 Gen 2.0 lane): if I plugged in more than three NVMe drives at once, it seemed the `nvme` driver would have some strange kernel panics either at boot or shutdown. Sometimes it would boot fine with four NVMe drives, but never with five or more.

## Video

I have an entire video up on my YouTube channel that goes through the Seaberry in much more detail:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/6dzSFUt6C6U" frameborder='0' allowfullscreen></iframe></div>
</div>

## Missing things

Besides price—which I'll get to in a bit—there are a couple things I was missing on my prototype board. The board I had is very close to the final production board, minus a few small tweaks they are making based on my testing and feedback.

  1. A proper front panel header. I actually figured out how to [get front panel ATX connections working](/blog/2021/using-compute-module-4-io-board-pins-atx-case-front-panel-header), but having labeled pins for the purpose would be nicer.
  2. Built-in USB 3.0. It would add to the BOM, but by my count, there's one extra PCIe lane available, so it would be very nice to have 2x USB 3.0 ports on the rear, and maybe expose the USB 2.0 ports through a front-panel header.
  3. PWM fan control fixes; on the board I had, we actually identified a few bugs in the original IO Board design it was based off of. It seems the fixes to enable [full PWM fan control](/blog/2021/controlling-pwm-fans-raspberry-pi-cm4-io-boards-emc2301) will make it to the final production board.
  4. A built-in RTC battery holder—my board, at least, has an RTC, but to use a battery I would have to solder in my own battery holder.

## Price and Availability

The Seaberry is expensive, at $435. A lot of that price comes from some of the components required for such an exotic board. The Broadcom PCIe switch used—a PEX8619—[costs over $125](https://www.digikey.com/en/products/detail/broadcom-limited/PEX8619-BA50BI-G/6150791) from DigiKey... and it isn't even in stock, so I don't know what kind of magic incantations Alftel had to go through to get a supply of chips!

But it's definitely a specialty board. People who need a low-power ARM-based development or experimentation platform could use this board like I do, to test more exotic configurations on the Pi. And it's looking like it will be the first commercially-available (though not cheapest) ways to install a Pi into a standard desktop or rackmount PC case, since it's mini ITX.

As long as you don't need to pump through more than 5 Gbps of data, this board has more PCIe connectivity than most PC mainboards. But unless you're Red Shirt Jeff-level crazy, you might not be able to use it all!
