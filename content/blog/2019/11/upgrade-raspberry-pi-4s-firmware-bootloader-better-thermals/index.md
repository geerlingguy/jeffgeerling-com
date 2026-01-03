---
nid: 2950
title: "Upgrade the Raspberry Pi 4's firmware / bootloader for better thermals"
slug: "upgrade-raspberry-pi-4s-firmware-bootloader-better-thermals"
date: 2019-11-21T16:06:12+00:00
drupal:
  nid: 2950
  path: /blog/2019/upgrade-raspberry-pi-4s-firmware-bootloader-better-thermals
  body_format: markdown
  redirects: []
tags:
  - eeprom
  - firmware
  - raspberry pi
  - raspbian
  - tutorial
  - upgrade
---

In October, the Raspberry Pi Foundation released an updated bootloader/firmware for the Raspberry Pi 4 which dramatically reduces power consumption and overall temperatures on the Pi 4 by setting the USB controller and CPU into a more power-friendly mode.

I wanted to post here the instructions for checking the current version, and upgrading, because I have a large number of Pis to upgrade over time, and I needed a quick reference. For more details, check out the Raspberry Pi Documentation page [Raspberry Pi 4 boot EEPROM](https://www.raspberrypi.org/documentation/hardware/raspberrypi/booteeprom.md).

## Checking if the current bootloader is up to date

Upgrade system packages and install the `rpi-eeprom` utility:

```
$ sudo apt update
$ sudo apt -y full-upgrade
$ sudo apt install -y rpi-eeprom
```

Check if an update is required:

```
$ sudo rpi-eeprom-update
```

If you see a difference in the output, you can restart to update to the newer version. If everything's the same, you're already on the latest version.

You can also use beta versions by modifying the `/etc/default/rpi-eeprom-update` file, or you can lock in a version (e.g. if you don't want the Pi to automatically update to newer versions) using the `FREEZE_VERSION` setting in the EEPROM config file. Read the [EEPROM documentation for more details](https://www.raspberrypi.org/documentation/hardware/raspberrypi/booteeprom.md).
