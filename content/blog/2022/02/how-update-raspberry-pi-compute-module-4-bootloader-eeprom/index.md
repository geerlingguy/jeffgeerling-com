---
nid: 3182
title: "How to update the Raspberry Pi Compute Module 4 Bootloader / EEPROM"
slug: "how-update-raspberry-pi-compute-module-4-bootloader-eeprom"
date: 2022-02-15T20:32:14+00:00
drupal:
  nid: 3182
  path: /blog/2022/how-update-raspberry-pi-compute-module-4-bootloader-eeprom
  body_format: markdown
  redirects: []
tags:
  - bootloader
  - cm4
  - compute module
  - eeprom
  - firmware
  - io board
  - raspberry pi
---

The Raspberry Pi 4 and Pi 400 share the same Broadcom BCM2711 SoC with the Compute Module 4. All three devices _also_ share an SPI EEPROM flash chip, which stores the Raspberry Pi's bootloader.

{{< figure src="./spi-eeprom-flash-raspberry-pi-4.jpeg" alt="SPI EEPROM Flash bootloader chip on Raspberry Pi 4 model B" width="700" height="467" class="insert-image" >}}

But the Compute Module 4 differs in how you _update_ the bootloader. With the Pi 4 or Pi 400, you can use Raspberry Pi imager to write a utility image to a microSD card to update the bootloader. You put in the card, power on the Pi, and the bootloader is updated.

On the Compute Module 4, because it may be used in remote or embedded environments, its bootloader can actually be hardware write-protected!

And to update it (when not write-protected), you have to use Raspberry Pi's `usbboot`/`rpiboot` utility.

> Note: While it uses the same base project, this process is slightly different than the one used to [flash eMMC Compute Modules](/blog/2020/how-flash-raspberry-pi-os-compute-module-4-emmc-usbboot#comment-16012).

First, make sure you have `libusb` installed. On my Mac, I ran `brew install libusb`, but on a Debian system or Raspberry Pi, you can install it with `sudo apt install libusb-1.0-0-dev`.

Then, clone Raspberry Pi's `usbboot` project to your computer:

```
git clone --depth=1 https://github.com/raspberrypi/usbboot
```

Change into the usbboot directory and build the `rpiboot` binary:

```
$ cd usbboot
$ make
```

Now, change into the `recovery` directory, and modify the `boot.conf` file to your liking. Check out the [CM4 Bootloader documentation](https://www.raspberrypi.com/documentation/computers/compute-module.html#modifying-the-bootloader-configuration) for some examples, in addition to the [Raspberry Pi 4 bootloader configuration options](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-4-bootloader-configuration) documentation.

In my case, I wanted to try out the [new Network Install feature](https://www.raspberrypi.com/news/network-install-beta-test-your-help-required/), so I added the line `NET_INSTALL_ENABLED=1` to my `boot.conf`, and I replaced the `pieeprom.original.bin` file in the recovery directory with the beta network install bootloader file [`pieeprom-2022-02-04.bin`](https://github.com/raspberrypi/rpi-eeprom/blob/master/firmware/beta/pieeprom-2022-02-04.bin).

Now, run ` ./update-pieeprom.sh` to update the `pieeprom.bin` image file.

> **Note**: If you get a message like `Source image "pieeprom.original.bin" not found`, run `git submodule init && git submodule update` to get the latest EEPROM files.

With the Compute Module 4 plugged into your computer, with the 'disable eMMC boot' jumper set (so it will not boot up normally), run `rpiboot` and it should load in the new `pieeprom.bin`:

```
$ ../rpiboot -d .
RPIBOOT: build-date Feb  4 2022 version 20220131~101805 693d5beb
Loading: ./bootcode4.bin
Waiting for BCM2835/6/7/2711...
Loading: ./bootcode4.bin
Sending bootcode.bin
Successful read 4 bytes 
Waiting for BCM2835/6/7/2711...
Loading: ./bootcode4.bin
Second stage boot server
Loading: ./config.txt
File read: config.txt
Loading: ./pieeprom.bin
Loading: ./pieeprom.bin
Loading: ./pieeprom.sig
File read: pieeprom.sig
Loading: ./pieeprom.bin
File read: pieeprom.bin
Second stage boot server done
```

Once it's complete, your terminal session should drop you back to your prompt, the green ACT LED on the CM4 IO Board should start flashing green, and if you have an HDMI display plugged in, it should show a green screen to indicate success.

Now, power off the CM4, pull the 'disable eMMC boot' jumper, and power it back on, and it _should_ be running the latest bootloader.

You can verify with:

```
$ sudo rpi-eeprom-update
BOOTLOADER: up to date
   CURRENT: Thu 29 Apr 16:11:25 UTC 2021 (1619712685)
    LATEST: Thu 29 Apr 16:11:25 UTC 2021 (1619712685)
   RELEASE: default (/lib/firmware/raspberrypi/bootloader/default)
            Use raspi-config to change the release.
```

You can also use `rpi-eeprom-config` to check on the current bootloader configuration, e.g.:

```
pi@pi4:~ $ rpi-eeprom-config
[all]
BOOT_UART=0
WAKE_ON_GPIO=1
ENABLE_SELF_UPDATE=1
BOOT_ORDER=0xf51
```

And you can edit the configuration with `sudo rpi-eeprom-config --edit`, or if you just want to change the boot order, use `sudo raspi-config`, and change that inside the Advanced Options.
