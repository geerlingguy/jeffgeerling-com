---
nid: 3316
title: "Forcing PCI Express Gen 3.0 speeds on the Pi 5"
slug: "forcing-pci-express-gen-30-speeds-on-pi-5"
date: 2023-10-11T14:12:53+00:00
drupal:
  nid: 3316
  path: /blog/2023/forcing-pci-express-gen-30-speeds-on-pi-5
  body_format: markdown
  redirects: []
tags:
  - config
  - coral
  - insertion loss
  - linux
  - pcie
  - pi 5
  - raspberry pi
---

The Raspberry Pi 5 includes 5 active PCI Express lanes—4 go to the new RP1 chip for I/O like USB, Ethernet, MIPI Camera and Display, and GPIO, and 1 goes to a new external PCIe connector:

{{< figure src="./pi-pcie-raspberry-pi-5.jpg" alt="Raspberry Pi 5 PCIe connector" width="700" height="274" class="insert-image" >}}

By default, all PCIe lanes operate at Gen 2.0 speeds, or about 5 GT/sec per lane. Currently there's no way to change that default for the RP1 chip's 'internal' lanes, but on the external connector, you can add the following lines inside `/boot/firmware/config.txt` (and reboot) to upgrade the connection to Gen 3.0 (8 GT/sec, almost double the speed):

```
dtparam=pciex1
dtparam=pciex1_gen=3
```

And yes, you can also _downgrade_ the connection to Gen 1.0 speeds (2.5 GT/sec) if you like.

## Why default to PCIe Gen 2.0?

Why is it defaulted to Gen 2.0? Because that's the speed at which the board could be certified for PCI Express. Even older standards like 2.0 and 3.0 are considered 'high speed' interconnects. And with any connection on a board, interference and signal issues can cause problems with higher bandwidth.

On expensive motherboards, PCIe Gen 5 and even Gen 4 have issues with some configurations, especially if people use risers for things like vertically-mounted GPUs.

{{< figure src="./pi-5-pcie-fpc-connector-flat-cable.jpeg" alt="Raspberry Pi 5 PCIe external FPC Connector - Flat cable" width="700" height="394" class="insert-image" >}}

But even on the tiny Pi 5, things like the [insertion loss](https://www.electronicdesign.com/technologies/communications/article/21267698/astera-labs-how-to-manage-the-pcie-50-channel-insertion-loss-budget) from the flat FPC connection can cause issues at higher speeds. I encountered some link errors from time to time, and they were compounded on certain devices which don't handle them as gracefully.

One such device was the Google Coral TPU, which seemed to like resetting its connection to the Pi 5 constantly, to the point I can't get it working yet (under Gen 1, 2, or 3!). You can [follow the saga here](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/44), but other devices do see a massive benefit with Gen 3.0 speeds:

  - My [10G ASUS Network Card](https://pipci.jeffgeerling.com/cards_network/asus-xg-c100c-10g.html) now gets 6 Gbps (instead of about 3.5) with the Pi 5.
  - My [Kioxa XG8 NVMe SSD](https://pipci.jeffgeerling.com/cards_m2/kioxia-xg8-m2-nvme-ssd.html) now gets 900 MB/sec reads versus 450 MB/sec under Gen 2.0.

It'd be _really_ interesting to see if we can hack a Pi 5 board to expose all _five_ lanes of PCIe from the BCM2712, and uprate all of them to Gen 3. You could conceivably run a 10 Gbps NAS or multi-port 2.5 Gbps router or firewall pretty easily with that bandwidth, sucking down 2-3W at idle.

## Where to go for more

I've been tracking all of my experiences with PCI Express devices on Raspberry Pis for years now, and will continue to do so for the Pi 5, over on my [Raspberry Pi PCIe Database](https://pipci.jeffgeerling.com).

Also see my initial post on [Testing PCIe on the Raspberry Pi 5](/blog/2023/testing-pcie-on-raspberry-pi-5).
