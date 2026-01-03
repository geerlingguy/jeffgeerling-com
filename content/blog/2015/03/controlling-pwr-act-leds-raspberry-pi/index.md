---
nid: 2512
title: "Controlling PWR and ACT LEDs on the Raspberry Pi"
slug: "controlling-pwr-act-leds-raspberry-pi"
date: 2015-03-15T18:09:17+00:00
drupal:
  nid: 2512
  path: /blogs/jeff-geerling/controlling-pwr-act-leds-raspberry-pi
  body_format: markdown
  redirects:
    - /blogs/jeff-geerling/controlling-both-pwr-and-act
aliases:
  - /blogs/jeff-geerling/controlling-both-pwr-and-act
   - /blogs/jeff-geerling/controlling-pwr-act-leds-raspberry-pi
  - /blogs/jeff-geerling/controlling-pwr-act-leds-raspberry-pi
tags:
  - consumption
  - dramble
  - energy efficiency
  - gpio
  - led
  - model 2
  - power
  - raspberry pi
  - status
  - zero
---

All Raspberry Pi models have a few built-in LEDs; the earlier models had PWR, ACT, and networking status LEDs all lined up on the board itself; for the B+ and model 2 B, the networking LEDs moved onto the network jack itself, leaving just two LEDs; PWR (a red LED) and ACT (a green LED).

Normally, whenever the Pi is powered on—except if the power supply dips below something like 4.5VDC—the red PWR LED remains lit no matter what. If you wanted to 'disable' the LED, you'd have to put a piece of tape or something else over the LED, or get out a soldering iron and modify the hardware a bit.

## Raspberry Pi model 2 B, B+ and A+ (and beyond)

Luckily, with the Pi 2 model B, B+, A+, and Zero, you can control the LEDs in software, in a few different ways. The simplest way to change the way these LEDs work is to modify the <code>trigger</code> for each LED by setting it in <code>/sys/class/leds/led[LED_ID]/trigger</code>, where you replace <code>[LED_ID]</code> with <code>0</code> for the green ACT LED, and <code>1</code> for the red PWR LED.

For example:

```
# Set the PWR LED to GPIO mode (set 'off' by default).
echo gpio | sudo tee /sys/class/leds/led1/trigger

# (Optional) Turn on (1) or off (0) the PWR LED.
echo 1 | sudo tee /sys/class/leds/led1/brightness
echo 0 | sudo tee /sys/class/leds/led1/brightness

# Revert the PWR LED back to 'under-voltage detect' mode.
echo input | sudo tee /sys/class/leds/led1/trigger

# Set the ACT LED to trigger on cpu0 instead of mmc0 (SD card access).
echo cpu0 | sudo tee /sys/class/leds/led0/trigger
```

I'm using this ability to turn off the bright red PWR LED on my Raspberry Pis, as I use decent power supplies and would rather save the few mW used by the LED so I can save a penny or two over the next couple years :)

If you want to disable both LEDs permanently, add the following to `/boot/config.txt`:

```
# Disable the ACT LED.
dtparam=act_led_trigger=none
dtparam=act_led_activelow=off

# Disable the PWR LED.
dtparam=pwr_led_trigger=default-on
dtparam=pwr_led_activelow=off
```

> Note: The method for disabling the power LED was updated following a firmware change that fixed a `pwr_led_trigger` setting on the Pi 3B+ and 4; see [this GitHub issue for details](https://github.com/raspberrypi/firmware/issues/1742).

## Raspberry Pi Zero

The Pi Zero's values are opposite, and it only has one LED, `led0` (labeled 'ACT' on the board). The LED defaults to on (brightness `0`), and turns _off_ (brightness <code>1</code>) to indicate disk activity.

If you want to turn off the LED on the Pi Zero completely, run the following two commands:

```
# Set the Pi Zero ACT LED trigger to 'none'.
echo none | sudo tee /sys/class/leds/led0/trigger

# Turn off the Pi Zero ACT LED.
echo 1 | sudo tee /sys/class/leds/led0/brightness
```

To make these settings permanent, add the following lines to your Pi's `/boot/config.txt` file and reboot:

```
# Disable the ACT LED on the Pi Zero.
dtparam=act_led_trigger=none
dtparam=act_led_activelow=on
```
