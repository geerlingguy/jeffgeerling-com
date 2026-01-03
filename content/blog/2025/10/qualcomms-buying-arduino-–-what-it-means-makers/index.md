---
nid: 3502
title: "Qualcomm's buying Arduino \u2013 what it means for makers"
slug: "qualcomms-buying-arduino-\u2013-what-it-means-makers"
date: 2025-10-07T13:01:08+00:00
drupal:
  nid: 3502
  path: /blog/2025/qualcomms-buying-arduino-–-what-it-means-makers
  body_format: markdown
  redirects:
    - /blog/2025/qualcomm-bought-arduino-what-it-means-makers
aliases:
  - /blog/2025/qualcomm-bought-arduino-what-it-means-makers
tags:
  - acquisition
  - arduino
  - news
  - qualcomm
  - sbc
  - video
  - youtube
---

{{< figure src="./arduino-uno-q.jpg" alt="Arduino Uno Q SBC microcontroller board" width="700" height="371" class="insert-image" >}}

[Qualcomm just announced they're acquiring Arduino](https://www.qualcomm.com/news/releases/2025/10/qualcomm-to-acquire-arduino-accelerating-developers--access-to-i), the company that introduced a whole generation of tinkerers to microcontrollers and embedded electronics.

The [Uno R3](https://amzn.to/46FlNpp) was the first microcontroller board I owned. Over a decade ago, I blinked my first LED with an Uno; the [code for that is actually still up on my GitHub](https://github.com/geerlingguy/blinky).

The $45 [Uno Q](https://www.arduino.cc/product-uno-q), a new SBC-microcontroller hybrid (pictured at the top of this post), is the latest release in the Uno lineup, replacing the $27 [Uno R4 WiFi](https://amzn.to/46VkP74). I'll get to the Uno Q later in this post.

## Video

I published a video version of this blog post on my YouTube channel; you can watch it below, but if you're like me, and prefer text—just scroll on past!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/CfKX616-nsE" frameborder='0' allowfullscreen></iframe></div>
</div>

## Arduino's legacy

Arduino was my gateway into the world of tiny computer-controlled electronics. Today, there's the Raspberry Pi Pico and EspressIf's ESP boards, and I make use of all three ecosystems in my projects.

But Arduino holds a special place in the maker and electronics tinkering community. They took chips like the Atmel ATMega on Uno boards, and built software (like [Arduino IDE](https://www.arduino.cc/en/software/)) and guides to help people program them without having to to spend years learning how microcontrollers work.

But why would _Qualcomm_ want Arduino?

This is speculation on my part, but for _Qualcomm_, I think this is partly about making their dev kits and IoT product lines more approachable to students, tinkerers, and hackers who might be making purchasing decisions in the next decade.

On a more immediate level, companies are mixing solutions like an Arduino or ESP32 for controls, and a little Linux computer to run AI vision models, so why not put them together on the same board?

I don't know how much I trust Qualcomm to be great stewards of the Arduino brand and community, and I'm sure some people will jump ship after reading this news.

{{< figure src="./qualcomm-arduino-logos.jpg" alt="Qualcomm and Arduino Logos" width="700" height="394" class="insert-image" >}}

On Arduino's side, they've dealt with some crazy situations in the past. Like the dispute where [one of the founders trademarked the name in Italy](https://lwn.net/Articles/637755/), but wasn't affiliated with the main group that trademarked it in the _rest_ of the world. They spent _years_ sorting that out, until [they got it settled in 2017](https://blog.arduino.cc/2017/07/28/a-new-era-for-arduino-begins-today/).

Since then, Arduino expanded their hardware lineup to include industrial hardware in their [Pro line](https://www.arduino.cc/pro/platform-hardware). I'm guessing direct access to Qualcomm's arsenal of efficienty 5G 'AI' Arm SoCs could boost that business line.

## Uno Q

{{< figure src="./arduino-uno-q-front-and-back.jpg" alt="Arduino Uno Q front and back" width="700" height="394" class="insert-image" >}}

The first thing they're building together is the [Uno Q](https://www.arduino.cc/product-uno-q). It'll start at $44 for a board with 2 gigs of RAM and 16 gigs of eMMC storage. It's basically an Arm SBC in an Uno form factor. The architecture is more like what [Radxa did with their X4](/blog/2024/radxa-x4-sbc-unites-intel-n100-and-raspberry-pi-rp2040) (a microcontroller separate from the main computer) than a Raspberry Pi. Qualcomm's [Dragonwing QRB2210](https://www.qualcomm.com/products/internet-of-things/robotics-processors/qrb2210) runs Linux. Flip the board over, and there's an Arduino microcontroller, below the eMMC chip.

They're betting on people [building smart devices, robots, and industrial controls](https://www.thundercomm.com/product/qualcomm-robotics-rb1-platform/) with it. Will it pay off? I'm not sure. The nice thing is it keeps the classic Uno form factor (and should be compatible with existing [shields](https://store.arduino.cc/collections/shields-carriers)). On the Linux side, it looks like it'll have enough grunt to match like Pi 3 or maybe Pi 4 levels of performance, but with a more efficient chip (the QRB2210 is a <s>4nm</s> 11nm chip) and faster I/O.

But I have two big questions:

  1. How well will Qualcomm support Linux? It will ship with Debian, but will they devote the same amount of effort to keeping it up to date as Raspberry Pi, or will they abandon it in a couple years?
  2. How will they make it easier to develop things that fully utilize the little microcontroller? In other words: what makes this different than plugging an Uno into an SBC?

For _that_, they're also announcing [Arduino App Lab](https://www.arduino.cc/en/software/). You can run it on the Uno Q directly, or another computer. It should make it easier to build and maintain mixed Linux-plus-microcontroller apps. It can be messy developing a Python vision app on the Pi that also works with MicroPython to control motors with a Pi Pico. Same thing if you're building something for the Radxa X4.

But on a Raspberry Pi, you could skip the microcontroller and use the built-in GPIO with Python directly. You won't get the same realtime processing you get with a separate microcontroller, but that's not always required.

One other aspect of the Arduino that's attracted me and many others is the open source nature of the product. The board schematics <s>will be</s> [are](https://docs.arduino.cc/hardware/uno-q/) open source, and they have new high speed connectors on the bottom for HDMI, Ethernet, and other standard I/O. But can someone design their own version of the Uno Q and get a Dragonwing chip to install on it? Hopefully. I was told by my Qualcomm contact this _should_ happen, but no word on when.

Currently, you'd have to be a Qualcomm partner and likely order in the hundreds (if not thousands) if you wanted to pick up bare Dragonwing SoCs.

## Conclusion

But the Uno Q is just their first product. And nobody's tested it yet, so it's all speculation for now.

Besides performance and efficiency on the Linux side, the biggest question I have—assuming all the regulatory hurdles are cleared—will they still target the educational and maker markets, or are we going to see a bigger push into the more lucrative industrial space?

{{< figure src="./arduino-uno-q-pricing-availability.jpg" alt="Arduino Uno Q pricing and availability" width="700" height="394" class="insert-image" >}}

The price of the Uno has gone up over the years, and with the Uno Q, we're hitting the same price point as a base model Raspberry Pi 5, but with performance that's a couple years behind.

To fund educational resources, you do need higher profit margins on high end parts, so I'm not against a 'pro' line. But all these companies have to find the balance between catering to students and makers, and catering to enterprise.

I'm not as deep into microcontrollers and embedded electronics as many of you _reading_ this are, so please let me know your thoughts in the comments.

---

_Images used in this blog post were provided by Qualcomm prior to today's announcement._
