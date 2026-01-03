---
nid: 2740
title: "Review: Satechi USB Type-C inline Power Meter (ST-TCPM)"
slug: "review-satechi-usb-type-c-inline-power-meter-st-tcpm"
date: 2017-02-05T21:49:32+00:00
drupal:
  nid: 2740
  path: /blog/2017/review-satechi-usb-type-c-inline-power-meter-st-tcpm
  body_format: markdown
  redirects: []
tags:
  - power
  - reviews
  - satechi
  - usb
  - usb-c
---

> **tl;dr**: It's a _power meter_, not a protection circuit. It works well and is worth the money if you need to monitor power consumption, but it's made of plastic and doesn't feel like it can take a beating, so handle with care.

For some time, I've used a [PowerJive USB Power Meter](https://www.amazon.com/PowerJive-Voltage-Multimeter-chargers-capacity/dp/B013FANC9W/ref=as_li_ss_tl?ie=UTF8&qid=1486229789&sr=8-1&keywords=powerjive&linkCode=ll1&tag=mmjjg-20&linkId=7cf3abf390eec12bfc282a54ec09318f) to measure the charging rate of various USB power adapters, and even things like [how much power a Rasbperry Pi uses under load](https://www.pidramble.com/wiki/benchmarks/power-consumption).

But now that more devices are coming out with USB-C support (technically 'USB Type-C'), the older meters are more annoying to use (since they require dongles), and don't work in a bidirectional manner—USB-C allows power to flow in or out of many ports (like the ports on a new MacBook or 2016 MacBook Pro), so a dedicated USB-C-flavored power meter that supports bi-directional power metering is helpful.

<p style="text-align: center;">{{< figure src="./satechi-usb-c-power-meter-input-2060mA.jpg" alt="Satechi USB-C Power Meter input 2.06A" width="650" height="345" class="insert-image" >}}<br>
<em>The Satechi USB-C power meter inline with my MacBook Pro's included charger.</em></p>

I was excited to see one of the first low-cost meters available on Amazon, the [Satechi USB Type-C inline Power Meter](https://www.amazon.com/Satechi-Multimeter-Chargers-External-Capacity/dp/B01MT8MC3N/ref=as_li_ss_tl?ie=UTF8&qid=1486265356&sr=8-1&keywords=ST-TCPM&linkCode=ll1&tag=mmjjg-20&linkId=76f7e479a4bca82b337cc78d0f8ea80d), so I ordered one and have been testing it in various charging scenarios with my 2016 13" MacBook Pro.

## Important note on _Protection_

Let's get one thing clear: AFAICT, **the Satechi power meter doesn't offer any protection** against bad cables or poor USB-C power negotiation that results in fried circuits. It is merely a meter, not a protection circuit. The advice learned the hard way by Google engineer Benson Leung, and chronicled through Amazon.com product reviews and [this USB Type C Cables and Accessories Reviews](https://plus.google.com/collection/s0Inv) collection, should not be ignored—thoroughly vet your USB-C cables, and spend extra for known-good USB-C accessories. Don't damage your $2k+ laptop just by plugging in a cheap cable that saved you $10!

Articles like "Satechi's New USB-C Power Meter Helps Protect Against Faulty Cables, Chargers" are disingenuous at best, and fatal to your electronic devices at worst. Don't use this meter to test if a cable meets the correct charging spec; use this meter to meter current and direction for known-compatible devices and cables.

## Build Quality and Durability

From the pictures on Amazon's product page, and even the pictures above, you'd be forgiven for thinking this device is build from a solid slab of aluminum! Unfortunately, the shell is just plastic with an aluminum finish on the surface. It's definitely more compact and put together better than most other < $50 USB power devices... but it's not built to be tossed in a toolbox and rattled around for years.

I have put mine in a small foam pouch in my USB device cubby in my workshop, and when I plug it in and remove it, I'm sure to do so gently, rocking it back and forth and not stressing the connectors too much. There's a slight amount of wiggle to the connections, and I'm betting that a hard yank (or at least a few hard yanks) would either break the thing or make readings much less reliable. The truth is, USB-C connections are generally a lot tighter than USB A (and even Micro) connections, and any of these cheaper connectors will not survive wear and tear over hundreds of plug-unplug cycles—treat them carefully, though, and you'll get a few years' use.

The screen itself is a low-refresh-rate dot matrix, and easy enough to read in any lightning conditions. It's set back a few mm from the case front, so you have to look straight on to be able to see all the information. But it's definitely easier to read from multiple angles than the PowerJive I'm used to using.

## Usage and Functionality

Usage couldn't be easier. You plug the device into a USB-C port or cable, then plug another USB-C device into the other end. After 5 seconds of boot time, a status display shows measured voltage, amperage, total power used (in mAh), and the direction in which current is flowing:

<p style="text-align: center;">{{< figure src="./satechi-usb-c-power-meter-input-2980mA.jpg" alt="Satechi USB-C Power Meter input 2.98A" width="650" height="430" class="insert-image" >}}<br>
<em>When my AUKEY battery is charging my MacBook Pro, the arrow points towards the laptop...</em></p>

<p style="text-align: center;">{{< figure src="./satechi-usb-c-power-meter-output-1980mA.jpg" alt="Satechi USB-C Power Meter output 1.98A" width="650" height="353" class="insert-image" >}}<br>
<em>...and when my MacBook Pro is charging my iPad, the arrow points towards the iPad.</em></p>

Besides the 5 second boot time, there's nothing I'd change about this device. Some people don't like that it doesn't turn on until power is flowing one direction or the other... but I'm okay with that because I just want to measure that current, not prove that a port is active or not.

## Summary

There's not a whole lot to write about. It seems accurate based on similar measurements made with my PowerJive meter, and expected power usage. It works with all my OEM cables and devices, as well as with an AUKEY power bank I'm testing for later review, and it's more durable and nice-looking than most other cheap meters (though it's not a premium product, like something you'd get from Apple or Google directly).

If you want to see how much power is being transferred via USB-C, this is pretty much the only way to do it on the cheap right now. As long as you don't expect circuit _protection_ (just metering), this is a great little device.

You can buy the [Satechi USB C Power Meter](https://www.amazon.com/Satechi-Multimeter-Chargers-External-Capacity/dp/B01MT8MC3N/ref=as_li_ss_tl?ie=UTF8&qid=1486265356&sr=8-1&keywords=ST-TCPM&linkCode=ll1&tag=mmjjg-20&linkId=76f7e479a4bca82b337cc78d0f8ea80d) on Amazon for ~<span itemprop="priceCurrency" content="USD">$</span><span itemprop="price" content="29.99">30</span>.
