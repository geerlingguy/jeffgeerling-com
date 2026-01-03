---
nid: 3514
title: "How to silence the fan on a CM5 after shutdown"
slug: "how-silence-fan-on-cm5-after-shutdown"
date: 2025-11-20T15:27:40+00:00
drupal:
  nid: 3514
  path: /blog/2025/how-silence-fan-on-cm5-after-shutdown
  body_format: markdown
  redirects: []
tags:
  - cm5
  - eeprom
  - fan
  - raspberry pi
---

Out of the box, if you buy a Raspberry Pi Compute Module 5, install it on the official CM5 IO Board, and install a fan on it (e.g. my current favorite, the [EDAtec CM5 Active Cooler](https://www.digikey.com/en/products/detail/edatec/ED-CM5ACOOLER/25696857)), you'll notice the fan ramps up to 100% speed after you shut down the Pi.

{{< figure src="./cm5-io-board-fan-running.jpeg" alt="CM5 IO Board - Fan spinning" width="700" height="467" class="insert-image" >}}

That's not fun, since at least for a couple of my CM5s, they are more often powered down than running, creating a slight cacophany!

I created the forum thread [Compute Module 5 Fan goes to 100% on shutdown](https://forums.raspberrypi.com/viewtopic.php?t=380543), and through some back and forth, it was found the firmware on the CM5 needed a little tweaking to support powering off the fan completely on shutdown.

In [this December EEPROM update](https://github.com/raspberrypi/rpi-eeprom/pull/645), Raspberry Pi added some code to ensure the fan would power off (and stay powered off) on shutdown, but only if you have:

```
POWER_OFF_ON_HALT=0
```

In your Pi's EEPROM config.

First, make sure your firmware is up to date, e.g.:

```
$ sudo rpi-eeprom-update 
BOOTLOADER: up to date
   CURRENT: Wed  5 Nov 17:37:18 UTC 2025 (1762364238)
    LATEST: Wed  5 Nov 17:37:18 UTC 2025 (1762364238)
   RELEASE: latest (/usr/lib/firmware/raspberrypi/bootloader-2712/latest)
            Use raspi-config to change the release.
```

Run `sudo rpi-eeprom-update -a` to update to the latest version, if needed, then reboot.

To edit the EEPROM config, run `sudo rpi-eeprom-config --edit`, and add the following line at the bottom:

```
POWER_OFF_ON_HALT=0
```

Save that change, wait for the config to apply, then reboot.

Now, next time you shut down the CM5, it should be blissfully silent.

Hackaday user Eontronics also [designed a modchip](https://hackaday.io/project/202403-cm5-io-board-fan-halt) that can be soldered onto the CM5 IO board for a hardware fix for this problem, if you can't use the `POWER_OFF_ON_HALT=0` option.
