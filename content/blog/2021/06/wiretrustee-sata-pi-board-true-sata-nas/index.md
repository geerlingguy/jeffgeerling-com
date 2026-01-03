---
nid: 3107
title: "The Wiretrustee SATA Pi Board is a true SATA NAS"
slug: "wiretrustee-sata-pi-board-true-sata-nas"
date: 2021-06-10T14:00:18+00:00
drupal:
  nid: 3107
  path: /blog/2021/wiretrustee-sata-pi-board-true-sata-nas
  body_format: markdown
  redirects: []
tags:
  - cm4
  - compute module
  - nas
  - raspberry pi
  - sata
  - video
  - wiretrustee
---

In my earlier posts about building a custom [Raspberry Pi SATA NAS](/blog/2020/building-fastest-raspberry-pi-nas-sata-raid), and supercharging it with [2.5G networking and OMV](/blog/2021/raspberry-pi-25-gbps-16-tb-omv-nas-setup-and-performance), I noted that my builds were experimental only—they were a mess of cables and parts, with a hilariously-oversized 700W PC power supply.

I lamented the fact there was no simple "SATA backplane on a board" for the Raspberry Pi Compute Module 4. But no longer.

{{< figure src="./wiretrustee-sata.jpeg" alt="Wiretrustee SATA Board for Raspberry Pi OMV NAS" width="550" height="310" class="insert-image" >}}

Wiretrustee's [SATA Board](https://wiretrustee.com) integrates a SATA controller and data and power for up to four SATA drives with a Raspberry Pi Compute Module 4.

And their entire solution makes for a great little Raspberry Pi-based NAS, using software like [OpenMediaVault](https://www.openmediavault.org).

{{< figure src="./wiretrustee-sata-25-35-in-case.jpg" alt="Wiretrustee SATA 2.5 inch and 3.5 inch drive NAS enclosures" width="575" height="388" class="insert-image" >}}

You can get a 2.5" or 3.5" kit—in the video below I set up the 3.5" version—and you plug in four SSDs or Hard Drives, and (for now) recompile the Pi OS kernel to include AHCI support, then you have one of the most compact and convenient NAS builds available.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/ahrdx3TYxZc" frameborder='0' allowfullscreen></iframe></div>
</div>

I haven't done formal benchmarks on this setup, but could easily saturate a gigabit network connection with over 115 MB/sec reads and writes depending on the disk speed and workload. The Pi is well-suited to the task, and the internal PCI x1 Gen 2.0 lane can handle internal throughput of around 400 MiB/sec.

{{< figure src="./marvell-sata-pci-express-chip-wiretrustee-raspberry-pi-sata.jpeg" alt="Marvell SATA chip on Raspberry Pi Compute Module 4 SATA NAS Wiretrustee board" width="600" height="400" class="insert-image" >}}

Check out the video above for more details about the hardware and their custom case, and also check out my [database of CM4-based boards and projects](https://pipci.jeffgeerling.com/boards_cm) for more inspiration—there are some other great new products I'm seeing like [these](https://github.com/antmicro/scalenode) [two](https://www.instagram.com/p/CPqhoJnLRy6/) Pi blade servers, and [two](https://ib-wistinghausen.de/sigmoid-series-3d-printer-control-unit) [unique](https://www.element14.com/community/docs/DOC-96583/l/episode-496-compute-module-4-powered-3d-printer-board) Pi 3D Printer control boards!
