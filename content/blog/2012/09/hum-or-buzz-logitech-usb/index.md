---
nid: 2448
title: "Hum or Buzz with a Logitech USB Headset"
slug: "hum-or-buzz-logitech-usb"
date: 2012-09-14T23:27:34+00:00
drupal:
  nid: 2448
  path: /blogs/jeff-geerling/hum-or-buzz-logitech-usb
  body_format: full_html
  redirects: []
tags:
  - audio
  - ground loop
  - headset
  - logitech
  - microphone
  - usb
---

<a href="http://www.amazon.com/gp/product/B003NREDG4/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B003NREDG4&amp;linkCode=as2&amp;tag=mmjjg-20">{{< figure src="./logitech-usb-headset.jpg" alt="Logitech USB Headset" width="300" height="300" >}}</a><strong>Problem</strong>: I've heard from a lot of people about hum or background 'buzz' in recordings and Skype conversations when using a USB headset (like the one I have, the <a href="http://www.amazon.com/gp/product/B003NREDG4/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B003NREDG4&amp;linkCode=as2&amp;tag=mmjjg-20">Logitech USB Headset H350</a>). Almost every time I hear someone having this trouble, they're having the problem while using the headset with a laptop.

<strong>Solution</strong>: about 99% of the time, the problem is fixed by simply plugging the laptop into a grounded (3-prong) outlet.

On a Mac, if you're using the Apple power adapter without the extra power cable (with a 3-prong plug instead of the 2-prong plug), you may get a buzzing sound. On a PC, different adapters work differently, but hopefully you have a power adapter with a 3-prong plug.

The problem is caused by a well-known phenomena, a <a href="http://en.wikipedia.org/wiki/Ground_loop_(electricity)">ground loop</a>. When you plug in your laptop to a grounded outlet (3 prongs), the circuits for audio in the laptop have a 'ground' signal to make sure the audio doesn't get any interference. Sometimes, if your laptop or a USB accessory is made of metal, you might notice the buzz goes away if you touch a metal part. This is a surefire sign you have a ground loop problem.

With USB headsets, the only way to fix this is to plug your laptop into a grounded outlet. With analog headsets, there are some other ways of fixing the problem by isolating the signal better.

See related: <a href="http://www.jeffgeerling.com/articles/audio-and-video/2012/buzz-or-hum-computer-speakers">Buzz or Hum in Computer Speakers</a>.
