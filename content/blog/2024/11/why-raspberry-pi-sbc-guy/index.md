---
nid: 3417
title: "Why Raspberry Pi for an SBC guy"
slug: "why-raspberry-pi-sbc-guy"
date: 2024-11-09T01:04:17+00:00
drupal:
  nid: 3417
  path: /blog/2024/why-raspberry-pi-sbc-guy
  body_format: markdown
  redirects: []
tags:
  - armsom
  - banana pi
  - hardware
  - linux
  - raspberry pi
  - sbc
---

{{< figure src="./armsom-bpi-sige7-purple-case.jpeg" alt="ArmSoM Sige7 purple enclosure" width="700" height="auto" class="insert-image" >}}

If anyone asks why I prefer to work with Raspberry Pis when I want to tinker on a random project, consider:

I just spent the past hour with a brand new ArmSoM Sige7 board ([see my debugging notes in my `sbc-reviews` repo](https://github.com/geerlingguy/sbc-reviews/issues/56)). This SBC has been on the market for months, with [glowing reviews](https://www.electronics-lab.com/armsom-sige7-review-a-rockchip-rk3588-sbc-with-dual-2-5gbe-ethernet-nvme-storage-and-triple-display-output/) all the way back in May...

It took about 30 minutes before I could get it to boot (20 minutes to find an image that would flash and at least *start* booting). Then 20 to try getting boot to go all the way through and get logged in. And the last 10 trying to set up an account on [ArmSoM's forum](https://forum.armsom.org/t/sige7-username-and-password/176) to ask what the default user/pass for Ubuntu is (since all the other defaults I could scrounge up in their docs and forum posts didn't work).

It was especially fun having to dig through their [official Google Drive folder of OS images, last updated in July](https://drive.google.com/drive/folders/1ijH2PoVUtHwe7fyiIpiQ7bsDZV3nx-MB), to find one that would both flash to a microSD card with Etcher, and boot the device. (/s)

This is not an isolated incident. So many times I hop on a new SBC board train, and end up spending more time just getting to the point I can start doing a project... than actually doing a project 🤦‍♂️

The hardware looks cool, though. Hopefully I can get logged in next week!
