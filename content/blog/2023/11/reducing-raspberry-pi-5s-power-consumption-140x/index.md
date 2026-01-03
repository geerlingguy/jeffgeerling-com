---
nid: 3323
title: "Reducing Raspberry Pi 5's power consumption by 140x"
slug: "reducing-raspberry-pi-5s-power-consumption-140x"
date: 2023-11-05T20:29:07+00:00
drupal:
  nid: 3323
  path: /blog/2023/reducing-raspberry-pi-5s-power-consumption-140x
  body_format: markdown
  redirects: []
tags:
  - eeprom
  - energy efficiency
  - pi 5
  - power
  - raspberry pi
  - usb-c
---

Sorry to clickbait with that title... but it's actually true. I can help you improve power use by 140x—for _power off_ power consumption, at least.

{{< figure src="./dialog-pmic-raspberry-pi-5.jpg" alt="Dialog PMIC on Raspberry Pi 5" width="700" height="427" class="insert-image" >}}

By default, the Raspberry Pi 5 (like the Pi 4 before it) leaves the SoC powered up (just in a shutdown state) when you shut down the Pi.

Because of this, a Pi 5 will still sit there consuming 1.2-1.6W when completely shut down, even without _anything_ plugged in except power.

That's a lot—even compared to a modern desktop PC!

Why is this?

Apparently [some HATs have trouble if the 3v3 power rail is off, but 5v is still active](https://forums.raspberrypi.com/viewtopic.php?p=1498465&hilit=POWER_OFF_ON_HALT+3v3+hat#p1498465)—which would be the case if you completely power off the SoC, but still have your 5V power supply plugged in.

Because of that, the Pi ships by default with the setting `POWER_OFF_ON_HALT=0`, and the Pi eats up precious watts all the time.

## Fixing the Pi's power consumption

The fix is, thankfully, easy.

Edit your EEPROM config by running `sudo rpi-eeprom-config -e`, and make sure the following settings are configured:

```
[all]
BOOT_UART=1
WAKE_ON_GPIO=0
POWER_OFF_ON_HALT=1
```

The first setting is irrelevant here, but I'm including it for completeness. Also, `WAKE_ON_GPIO` doesn't seem to do anything on Pi 5 (since there's a power button and pads on the board for power switching, instead of GPIO-pin-based power control), but it's still there for now. I'm mostly including it because you can set these options on the Pi 4 too, and get it to reduce it's powered-off consumption too!

Save that configuration and reboot, then next time you shut down, you should see power consumption go down from 1-2W to 0.01W or even less:

{{< figure src="./raspberry-pi-5-power-off-on-shutdown.jpg" alt="Raspberry Pi 5 power off on shutdown 0.01W consumption" width="700" height="394" class="insert-image" >}}

## Why can't we change the default?

Well... if it were up to me, it would be changed. But it's not :)

We could either name and shame the HATs that don't work correctly with 5V but without 3v3, or we could push for the Pi team to figure out some solution that allows everyone to default to `POWER_OFF_ON_HALT=1`.

## Can you still boot the Pi 5 with `POWER_OFF_ON_HALT`?

Yes! The power button still works just as normal, and the red LED is still illuminated when it's shut down.

The RTC still keeps time, too, so watchdog-related functions (like booting during some interval, or at a certain time of day) should also work. I haven't personally tested this (yet), but [here's a forum thread](https://forums.raspberrypi.com/viewtopic.php?p=2151102) with a little more info.
