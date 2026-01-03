---
nid: 3174
title: "It's dire: Raspberry Pi availability tracker is launched"
slug: "its-dire-raspberry-pi-availability-tracker-launched"
date: 2022-01-31T20:30:02+00:00
drupal:
  nid: 3174
  path: /blog/2022/its-dire-raspberry-pi-availability-tracker-launched
  body_format: markdown
  redirects: []
tags:
  - cm4
  - compute module
  - parts shortage
  - pico
  - raspberry pi
  - websites
  - zero 2 w
---

Yesterday André Costa emailed me about his new website, [rpilocator](https://rpilocator.com).

{{< figure src="./rpilocator-website-screenshot.png" alt="rpilocator website screenshot as of Jan 31 2022" width="700" height="394" class="insert-image" >}}

It's a website to track Raspberry Pi 4 model B, Compute Module 4, Pi Zero 2 W, and Pico availability across multiple retailers in different countries.

In his own words:

> This database was created out of frustration trying to locate a Raspberry Pi product in the height of the chip and supply chain shortages of 2021. I got tired of visiting multiple websites every day trying to figure out if there were any Raspberry Pi's in stock. I coded this website in a few days during my spare time and had it hosted on a Raspberry Pi for a couple of weeks before deciding to make it publicly available. This is not hosted on a Raspberry Pi anymore.

André has tried including all the official Pi vendors (who contractually will sell Pi models at MSRP and not the insane markups you'll find on eBay or Amazon), but some block script-based access, so only about half the vendors are currently accounted for.

Checking yesterday, two models were available—across all the 29 models tracked. And today that number's down to one, a lonely CM4 model with 2 GB of RAM, 32 GB eMMC storage, and WiFi/Bluetooth.

When will the situation improve? Well, there's this, straight from the horse's mouth:

<blockquote class="twitter-tweet" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">Ex-stock availability is going to take a while, but we&#39;re planning to build ~150ku this quarter, and nearly ~500ku next quarter. That compares to 250ku in the whole of 2021.</p>&mdash; Eben Upton (@EbenUpton) <a href="https://twitter.com/EbenUpton/status/1486107991271260168?ref_src=twsrc%5Etfw">January 25, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

It seems the CM4 availability _may_ improve later this year, but when exactly is anyone's guess. Many people see lead times of "late 2022" or "January 2023", and think the worst, but usually if it's more than six months out, that just means the retailer is like `¯\_(ツ)_/¯` and it could be anywhere from weeks to years before they get stock.

For the Pi 4, the situation may improve even sooner:

<blockquote class="twitter-tweet" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">We&#39;re building as fast as we can, prioritising 2GB and 4GB, but 8GB stock should start to flow through in the next few weeks.</p>&mdash; Eben Upton (@EbenUpton) <a href="https://twitter.com/EbenUpton/status/1483013315462930435?ref_src=twsrc%5Etfw">January 17, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

But it remains to be seen. Right now, the best we can do is dig through drawers and boxes and find that old Pi 3 model B to tide us over until a Pi 4 is available again...

Check out [https://rpilocator.com](https://rpilocator.com) — and at least for Newark, PiShop, SparkFun, Seeed Studio, Farnell, The Pi Hut, and Adafruit, maybe it can save you a few dozen page refreshes every day.
