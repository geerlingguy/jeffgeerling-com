---
nid: 2741
title: "Review: AUKEY 30,000 mAh USB-C Portable Charger (with USB A, USB C, Micro USB)"
slug: "review-aukey-30000-mah-usb-c-portable-charger-usb-usb-c-micro-usb"
date: 2017-03-28T14:25:06+00:00
drupal:
  nid: 2741
  path: /blog/2017/review-aukey-30000-mah-usb-c-portable-charger-usb-usb-c-micro-usb
  body_format: markdown
  redirects: []
tags:
  - aukey
  - battery
  - charger
  - power
  - reviews
  - usb
  - usb-c
---

**Jeff's Rating**: 3/5

> **tl;dr**: Slightly pricey, could use a better interface for charge status, and holds 20% less than the advertised capacity, but the still-plentiful amount of stored energy and the ability to charge via USB-C or USB-A makes this a versatile and potent power pack for the price.

Ever since the mid 90s, when I was able to lug around 'power bricks' with my then-amazing PowerBook 190 and 180c (hand-me-downs from relatives), I've been hoping for a reasonably-priced power brick that would double my laptop's battery life, affording me the ability to work all day even when I'm doing a ton of crazy things, like building a ton of VMs and Docker images.

{{< figure src="./aukey-30000-mah-portable-charger.jpg" alt="AUKEY 30000 mAh Portable Charger" width="650" height="422" class="insert-image" >}}

AUKEY emailed me a few months ago and asked if I'd be interested in reviewing their first high-capacity USB-C charging pack, the beastly [AUKEY 30000 mAh USB-C charger](https://www.amazon.com/AUKEY-30000mAh-Portable-Charger-Lightning/dp/B01HRAG2KM/ref=as_li_ss_tl?ie=UTF8&qid=1488213556&sr=8-2&keywords=aukey+30000+usb+c&linkCode=ll1&tag=mmjjg-20&linkId=d7e29dda7de759c1efa568ec4e915803). Since I had just purchased a 2016 MacBook Pro, which _only_ has USB-C ports, I decided to give it a shot.

So over the course of the next few months, I tested the battery pack with my MacBook Pro (USB-C), my iPhone 7, and my iPad Air 2, along with a cluster of Raspberry Pi model 3s.

## Build Quality and Features

In the past, I've hesitated when asked for reviews of non-US manufactured power devices. I still don't often charge my laptop or other devices using third-party chargers—check out [Ken Shiriff's excellent post on the main reason why](http://www.righto.com/2014/05/a-look-inside-ipad-chargers-pricey.html). I haven't cracked open this battery pack's case, but I have used enough of AUKEY's other devices to know their build quality is at least a step above the cheapest knockoff chargers (though not as nice as Apple's or Samsung's, or other first-party manufacturers.

The battery pack is a solid plastic 'brick' that's just large enough to not fit in a typical jeans pocket—though you're not purchasing this battery pack strictly for portability reasons! Besides the ports, the only other feature on the brick is the power button on top. There are no buttons, no pop-open doors, etc. It's heavy (about 1 lb.), but the weight is evenly-distributed.

It has a nice assortment of ports:

  - USB-C (bi-directional—can be used for charging the pack or charging a USB-C device)
  - 2x USB-A (for charging devices)
  - 1x Micro USB (only for charging the pack)
  - 1x Lightning (TODO - does mine have it?

The power button depresses easily, and has a status LED below, and this is the weak point of the hardware design: the LED changes colors (red, green, and white) to indicate power level, and either pulsates or flashes to indicate status. It's a worthy attempt at providing power level and status all in one button (and simplifies the device design, for sure), but it falls a bit short when compared to a full LCD or multiple LEDs.

<p style="text-align: center;">{{< figure src="./aukey-30000-mah-power-button.jpg" alt="AUKEY 30000 mAh Portable Charger - Power Button" width="650" height="394" class="insert-image" >}}<br>
<em>The power button is the only button... and only status indicator on the entire brick.</em></p>

On most other 'premium' large capacity battery packs, there's either an LCD with a percentage readout, or a series of LEDs that indicate percentage in 20 or 25% increments. Having only a single indicator (albeit with a decent status indication) makes it more difficult to determine just how much juice is left. And for a battery pack that takes 3-5 hours (minimum!) to charge, you can't just top if off on a whim.

The other thing I don't like about the status LED is that it's a bit dim. Often I appreciate more subtle LED indicators, but in this case, it could use a tad bit more brightness. Here's a gif of how the status indicator pulsates in typical lighting conditions:

<p class="text-align: center;">{{< figure src="./aukey-charger-light.gif" alt="AUKEY charger - dim button for power status" width="480" height="270" class="insert-image" >}}<br>
<em>It's really that hard to see the light in a typical indoor environment.</em></p>

It's quite difficult to see with standard lighting or in a bright area in general. I usually have to press the button then cup my hand over the power button to see if it's red, green, or white.

<p class="text-align: center;">{{< figure src="./aukey-charger-covered.gif" alt="AUKEY charger - hold hand over button to see light" width="480" height="270" class="insert-image" >}}<br>
<em>You have to be in a dark location or hold your hand over the light to see it.</em></p>

## Some issues

Through the course of my testing, I noticed a few odd behaviors that made this power brick less than perfect (and a good reason to knock it down to a 4/5 instead of 5/5 rating):

  - The USB-C port is _supposed_ to be bi-directional, but there were two cases when it's behavior was surprising or strange:
    - If you run the battery down to empty, the USB-C port won't accept any charge _into_ the battery pack until after it's been charged up about 5% using the Micro USB port. Not sure why, but once I charged it a little, the USB-C port started allowing current to flow into the battery pack from my Apple USB-C wall charger and cable.
    - If you have a USB-C device like a MacBook set to 'not sleep when connected to power', this creates a strange race condition—the battery will keep the MacBook topped off until it starts getting low on power (when the red light comes on under the power button)... but then this triggers the MacBook to, in turn, charge the battery... then the battery charges the MacBook again after a while, and vice-versa. This is all well and good, but eventually, both the laptop and charger are drained to nothing, and it caused my MacBook to get a little funky—the clock reset and some applications needed a couple restarts to be happy!
  - Lower-power devices (like a Raspberry Pi Zero using very little energy, or an iPhone after trickle-charging) don't draw enough current for the charger to stay on, therefore it shuts off, and won't start charging again until the power button is pressed. Unfortunately, this means you could wake up to an iPhone with not much battery power left if the phone decides to perform a system update or something along those lines!
  - Through the course of three full charge and discharge cycles, <s>I could never measure more than 25,000 mAh of power going into or out of the charger</s> (Edit: apparently this battery is rated for ~3.7V devices, which is used to calculate the 30k mAh number... so at 5V output, it is reasonable to expect less than 30k mAh!). See the picture below for one of the charge cycles—after about 23,000 mAh, the charge went from 2.9A to 0.01A, so unless it were trickle charging for months, it didn't seem like it would ever get up to 30,000 mAh (with 5V draw).

<p style="text-align: center;">{{< figure src="./23000-mah-charge-measure-usb-c.jpg" alt="23,000 mAh as measured by Satechi USB-C plug" width="650" height="369" class="insert-image" >}}<br>
<em>The charger never output more than 25,000 mAh in charge/discharge cycles (20% lower than advertised).</em></p>

## Charging rates

I don't have any devices which support the 'Qualcomm Quick Charge' protocol, so I wasn't able to test that charging rate, but I was able to measure ~3A current, continuously, going both ways on the USB-C port, and 1.5-2.5A current output through the USB-A ports (enough to charge my power-hungry iPad Air 2 slightly faster than the 10W Apple wall charger!).

{{< figure src="./aukey-charging-macbook-pro-and-ipad-usb-c-usb-a-4790mA.jpg" alt="AUKEY 30000 mAh Charging MacBook Pro at 3A and iPad at 2A" width="650" height="430" class="insert-image" >}}

To measure the current, I used the [PowerJive USB-A power meter](https://www.amazon.com/PowerJive-Voltage-Multimeter-chargers-capacity/dp/B013FANC9W/ref=as_li_ss_tl?ie=UTF8&qid=1486229789&sr=8-1&keywords=powerjive&linkCode=ll1&tag=mmjjg-20&linkId=18bdb02c8b72d97649eed9a00fe9b41e) (for USB-A devices), and the [Satechi USB Type-C inline Power Meter](https://www.amazon.com/Satechi-Multimeter-Chargers-External-Capacity/dp/B01MT8MC3N/ref=as_li_ss_tl?ie=UTF8&qid=1486265356&sr=8-1&keywords=ST-TCPM&linkCode=ll1&tag=mmjjg-20&linkId=76f7e479a4bca82b337cc78d0f8ea80d) (for USB-C devices).

## Charging the 2016 13" MacBook Pro

{{< figure src="./aukey-charging-macbook-pro-3A-closeup.jpg" alt="AUKEY 30000 mAh Charging MacBook Pro at 3A - up close" width="650" height="430" class="insert-image" >}}

The main reason I was interested in testing this charger was its ability to charge USB-C devices. The good news: it does charge my 2016 MacBook Pro, and gives it about 3-5 extra hours of juice (enough to stay away from an outlet for an entire day!

{{< figure src="./aukey-battery-not-charging-cable-matters.png" alt="AUKEY 30000 mAh Charging MacBook Pro - Battery not charging" width="314" height="130" class="insert-image" >}}

The bad news, though, is that the charging rate tops out around ~3A, meaning that the battery can basically maintain a charge level, but unless you're not using the laptop, the Mac's battery won't actually charge; it will just remain at whatever charge level it was when you plugged in the AUKEY.

The other bad news is that, once the AUKEY gets down into its 'red' charge level (10% or lower), strange things can happen due to the bidirectional nature of USB-C power. One time, when I left my Mac plugged into an external display overnight, I discovered that both the AUKEY and my MacBook Pro were at 0%; and the MacBook Pro must've gotten confused (since it was 'plugged into external power), because it required a good 10 minutes plugged into AC mains power before it would boot. And when it _did_ boot, the clock was off, and a few applications did weird things until the Mac got its time back in sync!

This isn't to say the AUKEY charger is bad or shouldn't ever be used with a high-current-draw device like the MacBook Pro. But you should probably be judicious in your use—use it to top off a charge, or to squeeze out a couple hours of extra use. Just don't drain it all the way, because that's when weird things happen with USB-C.

> Note: Also, since the time I ran the battery down to zero, the ability to recharge the battery pack via USB-C is hit-or-miss. It seems you have to charge the pack up to 10-20% charge using the mini USB port, then the USB-C port works for the rest of the charge.

## Maximum output!

I also ran a test where I ran my MacBook Pro, my iPad Air 2, and iPhone 7, all at full brightness, playing or compressing videos, while plugged into the AUKEY. It continued putting out around 5.5-6 Amps continuously, and got a little warm (enough that I wouldn't consider doing that inside a bag on the road!), but it seemed to handle that scenario well, too.

I think it's a better plan to stick to one device at a time, if at all possible, as batteries and electronics don't like heat, and you'll likely get more efficiency if you don't push the pack too hard. But it's nice to know the pack's got it where it counts!

## Summary

I was hoping to give this portable power device a 5/5 rating, and in some regards it was close. But the difficulty and confusion when it comes to both how to get it charging, and how much charge is currently available made me take off one star. Add in a couple other quirks like strange USB-C bi-directional behavior and 20% less-than-advertised capacity, and that's two stars off an otherwise stellar device.

You can buy the [AUKEY 30,000 mAh USB-C Charger](https://www.amazon.com/AUKEY-30000mAh-Portable-Charger-Micro-USB/dp/B01F8IRIN0/ref=as_li_ss_tl?srs=9359766011&ie=UTF8&qid=1486265101&sr=8-1&keywords=usb-c+30000&linkCode=ll1&tag=mmjjg-20&linkId=3a275588a6d39ec725d48395de5e93a0) on Amazon for ~<span itemprop="priceCurrency" content="USD">$</span><span itemprop="price" content="54.99">55</span>.
