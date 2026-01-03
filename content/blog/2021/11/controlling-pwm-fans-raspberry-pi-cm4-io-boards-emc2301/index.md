---
nid: 3148
title: "Controlling PWM fans with the Raspberry Pi CM4 IO Board's EMC2301"
slug: "controlling-pwm-fans-raspberry-pi-cm4-io-boards-emc2301"
date: 2021-11-22T16:13:55+00:00
drupal:
  nid: 3148
  path: /blog/2021/controlling-pwm-fans-raspberry-pi-cm4-io-boards-emc2301
  body_format: markdown
  redirects: []
tags:
  - cm4
  - compute module
  - fan
  - i2c
  - io board
  - linux
  - pwm
  - raspberry pi
  - script
---

{{< figure src="./noctua-pwm-fan-120mm-raspberry-pi-cm4-io-board.jpeg" alt="Noctua 120mm PWM fan connected to Raspberry Pi CM4 IO Board" width="700" height="454" class="insert-image" >}}

When I initially [reviewed](/blog/2020/raspberry-pi-compute-module-4-review) the Compute Module 4 IO Board, I briefly mentioned there's a 4-pin fan connector. It's connected to the Pi's I2C bus using a little PWM chip, the [EMC2301](https://www.microchip.com/wwwproducts/en/EMC2301).

But wait... what's I2C, what's PWM, and what's so special about a 4-pin fan connector? I'm glad you asked—this post will answer that _and_ show you how you can control a fan connected to the IO Board, like the quiet [Noctua NF-P12](https://amzn.to/3xboRGg) pictured above with my IO Board.

If you plug a fan like that into the CM4 IO Board, it will start running full blast, 24x7. If you need that much cooling, that's great, but a lot of times, I don't mind my Pi's CPU getting warmer if it means I can run the fan silent most of the time.

> **2022-05 Update**: Recently, a driver for the EMC2301 fan controller was [merged into Raspberry Pi's Linux fork](https://github.com/raspberrypi/linux/pull/5026), so it will appear in the next release of Raspberry Pi OS.
>
> Once that's done, all you'd need to do (if running Pi OS) is add the following line to your `/boot/config.txt` file:
>
> ```
> dtoverlay=i2c-fan,emc2301,i2c_csi_dsi
> ```
>
> See [this comment on GitHub](https://github.com/raspberrypi/linux/issues/4632#issuecomment-1122687644) for more details, and how to control PWM speeds and trigger temperatures.

So what are my options? First of all, I could just buy an inline PWM controller, like a [Noctua NA-FC1](https://amzn.to/3HGSap3). It lets me turn up and down the fan speed with a little dial. But it doesn't know the temperature of my Pi, so it can't increase airflow for higher temperatures or turn off the fan when it's under a certain temperature.

{{< figure src="./emc2301-fan-controller-raspberry-pi-io-board.jpeg" alt="EMC2301 Fan controller on Raspberry Pi CM4 IO Board" width="600" height="371" class="insert-image" >}}

The better option is to use the built-in PWM fan controller on the IO Board (pictured above). And to do that, we're going to need to use the Raspberry Pi's I2C bus!

## What is I2C?

I2C—or more correctly, I<sup>2</sup>C—stands for "Inter-Integrated Circuit" and is a two-wire serial communication interface used by many electronic devices for control and communications.

I'm not going to cover it in detail here, but if you get into any more advanced electronics projects with Arduino, Raspberry Pi, or other microcontrollers or PCs, you'll probably encounter it. To learn the basics of the protocol, I recommend [Analog Device's I<sup>2</sup>C Primer](https://www.analog.com/en/technical-articles/i2c-primer-what-is-i2c-part-1.html).

## Controlling the fan over I<sup>2</sup>C

You have to edit your `/boot/config.txt` file to enable the `i2c_vc` bus, which is bus #1. The [Pi Device Tree Documentation](https://www.raspberrypi.org/documentation/configuration/device-tree.md) actually recommends against touching `i2c_vc` unless you need to, because you could mess up CSI camera or DSI display functionality.

Make sure the following lines exist and are uncommented in `/boot/config.txt` and reboot the Pi:

```
# Enable I2C.
dtparam=i2c_arm=on
# Enable I2C bus 1.
dtparam=i2c_vc=on
```

> **Note**: If you just enable I<sup>2</sup>C under the 'Interfaces' option of `raspi-config`, it will only enable `i2c_arm`. To see the fan controller, you need to enable `i2c_vc` as well.

Make sure the `i2c-tools` package is installed on your system; if it is, the following commands should work straightaway. If not, you will need to install the package with `sudo apt-get install -y i2c-tools`.

Now, check if you can see the fan controller chip on the bus, using `i2cdetect -y 10`:

```
$ i2cdetect -y 10
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- 0c -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 2f
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- 51 -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

The fan is the `2f` device. Test if you can turn off the fan using:

```
$ i2cset -y 10 0x2f 0x30 0x00
```

The fan should now be off. And to turn it back on:

```
$ i2cset -y 10 0x2f 0x30 0xff
```

To _get_ the value of the fan setting, you can use:

```
$ i2cget -y 10 0x2f 0x30
0xff
```

What about setting the fan to a value between 0% (off) and 100% (full on) though? The value is hexadecimal, so `0xFF` stands for `255`, while `0x00` is `0`. Using a high-ish number should be safe, right, to set the fan to a lower speed? Well, let's try it out.

First, set the fan speed to 'off':

```
$ i2cset -y 10 0x2f 0x30 0x00
```

Wait for the fan to spin down entirely, then set the fan to `100` (or `0x64` in hex):

```
$ i2cset -y 10 0x2f 0x30 0x64
```

If you do this, you'll notice the fan comes back on, but hopefully at a much more pleasant speed. On one of my Noctua fans, 100/255 equates to about 40% speed, or 1200 rpm, and it's nearly silent.

Now that we can control the fan over I<sup>2</sup>C, we could write up a script to set fan speeds based on CPU temperatures manually, but there are a few other ways to control the fan speeds.

> Note: The 'Fan' performance option inside `raspi-config` currently has no effect on the operation of a fan through the EMC2301 chip.

## Can I use Linux `lm-sensors` and `fancontrol`?

Unfortunately, the standard way of controlling fan speeds based on sensor data on most common PC hardware doesn't seem to be supported on the CM4 IO Board's I<sup>2</sup>C chip.

If I install `lm-sensors` and `fancontrol` (following [this guide](https://askubuntu.com/a/46135)), then I run `sudo sensors-detect`, I get back the message:

```
Sorry, no sensors were detected.
Either your system has no sensors, or they are not supported, or
they are connected to an I2C or SMBus adapter that is not
supported. If you find out what chips are on your board, check
https://hwmon.wiki.kernel.org/device_support_status for driver status.
```

It did find 'clients' on the I<sup>2</sup>C bus at `0x51` and `0x2f`, but it couldn't identify them. And when I ran `sudo pwmconfig`, I got the message:

```
/usr/sbin/pwmconfig: There are no pwm-capable sensor modules installed
```

So it looks like that's out of the running, unfortunately. There's a [really old patch](http://lkml.iu.edu/hypermail/linux/kernel/1306.1/02473.html) for Linux to add the fan controller to the Linux source tree, but for some reason it never got worked on beyond early stages. There's also an issue discussing the [IO Board fan controller](https://github.com/raspberrypi/linux/issues/4632) in the Raspberry Pi Linux kernel project, in case you want to subscribe and see the latest updates.

> Dec 2021 update: It looks like there's a [newer patch here](https://lore.kernel.org/all/20200928104326.40386-1-biwen.li@oss.nxp.com/) and a new [firmware driver](https://gitlab.traverse.com.au/ls1088firmware/traverse-sensors/-/commit/1cdec49171ebafcf32b347e7701224144de8620b) that some folks at Pine64 have been working on.

## The `cm4io-fan` driver

GitHub user [neg2led](https://github.com/neg2led) is maintaining an open source CM4 IO Board Fan controller driver, which is the next best thing. This driver is based on Traverse Technologies' EMC2301 hwmon driver.

To install it, I made sure I had I<sup>2</sup>C enabled as written above, and ran the following:

```
# Install the Raspberry Pi kernel headers, so the source build works.
sudo apt install raspberrypi-kernel-headers

# Install DKMS, to make updating the driver easier.
sudo apt install dkms

# Get the URL (tar.gz) of the latest release: https://github.com/neg2led/cm4io-fan/releases
wget https://github.com/neg2led/cm4io-fan/archive/refs/tags/0.1.1.tar.gz

# Expand the contents of the download into your /usr/src directory.
sudo tar -xzvf 0.1.1.tar.gz -C /usr/src/

# Build/install the driver with DKMS.
sudo dkms install cm4io-fan/0.1.1
```

At this point, the driver should be installed and will work after a reboot, once you configure it.

> **Note**: I've only tested the driver on 64-bit Pi OS, but other users have reported it successfully compiles and works on 32-bit Pi OS as well.

### Configuring the driver

Configuration can be done in the `/boot/config.txt` file. Add a line like the following:

```
# Control fan speeds.
dtoverlay=cm4io-fan,minrpm=1000,maxrpm=3000
```

This would set the fan to stay on at least at 1000 rpm at all times, and it would go up to 3000 rpm once the Pi's SoC reaches the `maxtemp`, which by default is `5500` in millicelcius (55°C).

You can override other options such as temperature thresholds using [the driver's config options](https://github.com/neg2led/cm4io-fan#config-options).

You can also check the current fan speed with the following command:

```
$ cat /sys/class/hwmon/hwmon2/fan1_input
2146
```

### Driver problems

The driver seems to work better on some CM4 boards than others, and may also have issues with certain PWM fans. One of the issues I encountered seems to be related to a potential bug in the reference design on the official IO Board.

If you encounter issues, check if the problem you hit is already documented in the [cm4io-fan issue queue](https://github.com/neg2led/cm4io-fan/issues).

## Basic Temperature-controlled fan script

As a final option you could write your own [temperature-controlled fan script](https://gist.github.com/geerlingguy/9c9c78463c0e3d9f4a23152912930821), which checks the current temperature, and boosts the fan speed accordingly. It's nowhere near as fully featured as the driver above, but it could work in a pinch:

<script src="https://gist.github.com/geerlingguy/9c9c78463c0e3d9f4a23152912930821.js"></script>

## Conclusion

There are a few different ways to interact with the EMC2301 fan controller on the Raspberry Pi Compute Module 4 IO Board (and a few other [CM4 boards](https://pipci.jeffgeerling.com/boards_cm) I've tested, like the [Seaberry](https://pipci.jeffgeerling.com/boards_cm)), but the cm4io-fan driver seems the most promising.

Hopefully you've learned a little about I<sup>2</sup>C in this post, too—I know I've learned a bit more about it, how PWM fans work, and even why tuning things like fan curves are important!
