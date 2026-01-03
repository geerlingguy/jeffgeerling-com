---
nid: 3094
title: "Taking control of the Pi PoE HAT's overly-aggressive fan"
slug: "taking-control-pi-poe-hats-overly-aggressive-fan"
date: 2021-05-05T15:31:50+00:00
drupal:
  nid: 3094
  path: /blog/2021/taking-control-pi-poe-hats-overly-aggressive-fan
  body_format: markdown
  redirects: []
tags:
  - networking
  - poe
  - rack
  - raspberry pi
---

I am starting to rack up more Pis ([quite literally](https://twitter.com/geerlingguy/status/1389775200594583554)) using the official [Pi PoE HAT](https://www.raspberrypi.org/products/poe-hat/) to save on cabling.

The one thing I hate most about those little HATs is the fact the fans [spin up around 40°C](https://github.com/raspberrypi/linux/blob/7fb9d006d3ff3baf2e205e0c85c4e4fd0a64fcd0/arch/arm/boot/dts/overlays/rpi-poe-overlay.dts#L28-L49), and then turn off a few seconds later, once the temperature is back down to 39 or so, all day long.

I'd be happy to let my Pis idle around 50-60°C, and only have the little whiny fans come on beyond those temperatures. Even under moderate load, the Pi rarely goes above 55°C in my basement, where there's adequate natural convection, so the fans would only really be necessary under heavy load.

As it turns out, there are some device tree overlays you can configure in the Pi's `/boot/config.txt` to control the speeds and temperatures when the fan runs on the PoE HAT, and I liked the defaults [user Nooblet-69 suggested](https://github.com/raspberrypi/linux/issues/2715#issuecomment-769405042) on GitHub:

```
# PoE Hat Fan Speeds
dtparam=poe_fan_temp0=50000
dtparam=poe_fan_temp1=60000
dtparam=poe_fan_temp2=70000
dtparam=poe_fan_temp3=80000
```

Toss those lines in the bottom of the boot config file, reboot the Pi, and it should start picking up the new temperature settings.

Ahh, _blissful silence_. Well, at least mostly. My rack-mount UPS's fan needs a good cleaning.

> **Edit**: It looks like the PoE+ HAT is controlled the same way. For the gory technical details, see the [`rpi-poe-fan.c` file](https://github.com/raspberrypi/linux/blob/rpi-5.10.y/drivers/hwmon/rpi-poe-fan.c).
