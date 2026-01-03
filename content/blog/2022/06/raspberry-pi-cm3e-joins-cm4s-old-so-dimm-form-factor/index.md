---
nid: 3215
title: "Raspberry Pi CM3E joins CM4S in the old SO-DIMM form factor"
slug: "raspberry-pi-cm3e-joins-cm4s-old-so-dimm-form-factor"
date: 2022-06-14T17:06:59+00:00
drupal:
  nid: 3215
  path: /blog/2022/raspberry-pi-cm3e-joins-cm4s-old-so-dimm-form-factor
  body_format: markdown
  redirects: []
tags:
  - cm3
  - cm3e
  - cm4
  - cm4s
  - compute module
  - parts shortage
  - raspberry pi
---

Last week this Tweet crossed my timeline:

<blockquote class="twitter-tweet" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">Just taken delivery of a shiny <a href="https://twitter.com/wallboxchargers?ref_src=twsrc%5Etfw">@wallboxchargers</a> EV charger and spotted the super shiny new <a href="https://twitter.com/Raspberry_Pi?ref_src=twsrc%5Etfw">@Raspberry_Pi</a> CM3E in there with its super swanky combined CPU/RAM package 😎 <a href="https://t.co/oEUqKPMwTK">pic.twitter.com/oEUqKPMwTK</a></p>&mdash; Pi 0 in your Pocket (@Pi0CKET) <a href="https://twitter.com/Pi0CKET/status/1534810655441752064?ref_src=twsrc%5Etfw">June 9, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

If you look closely, that's a "Raspberry Pi Compute Module 3E"—which is so far not listed on Raspberry Pi's website.

This Pi joins the mythical [Compute Module 4S](/blog/2022/new-raspberry-pi-compute-module-4s) as one of two Pi models mere mortals are unable to obtain—believe me, I've tried. The folks at Pi HQ in the UK apparently don't even have them on _their_ shelves. The CM4S is at least [listed on Raspberry Pi's website now](https://www.raspberrypi.com/products/compute-module-4s/), though with the following note:

> Based on the Raspberry Pi 4 Model B architecture, Compute Module 4S is intended for specific industrial customers migrating from Compute Module 3 or Compute Module 3+ and is not for general sale.

If you look closely at the CM3E, the SoC on the board is an `RP3A0-AU`. That's the same chip from the [Raspberry Pi Zero W 2](/blog/2021/look-inside-raspberry-pi-zero-2-w-and-rp3a0-au) introduced last year.

Raspberry Pi has had to shift parts around and rely on some previously-shelved designs, it seems, to fulfill industry orders for devices that integrate the 200-pin SO-DIMM form factor that was used by the CM1, CM3, and CM3+ models. It would seem stocks are running low on SoCs like the BCM2837 used in the prior Compute Module revisions.

Apparently [there was even a CM2 in the works](https://forums.raspberrypi.com/viewtopic.php?t=252662) at some point, but I doubt that'll come back from the dead, since that SoC was the last in the Pi lineup without 64-bit support!
