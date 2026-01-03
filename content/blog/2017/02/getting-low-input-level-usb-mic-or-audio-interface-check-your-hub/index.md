---
nid: 2751
title: "Getting low input level with a USB mic or audio interface? Check your hub"
slug: "getting-low-input-level-usb-mic-or-audio-interface-check-your-hub"
date: 2017-02-24T19:43:29+00:00
drupal:
  nid: 2751
  path: /blog/2017/getting-low-input-level-usb-mic-or-audio-interface-check-your-hub
  body_format: markdown
  redirects: []
tags:
  - audio
  - behringer
  - mac
  - mic-level
  - microphone
  - sound
  - usb
---

A few months ago, I decided to get more serious about my recording setup in my home office. I do a lot more screencasts both for [my YouTube channel](https://www.youtube.com/user/geerlingguy) and for other purposes than I used to, and I can't stand poor audio quality. Therefore I finally decided to get some sound absorption panels for my office, rearrange furniture a little for better isolation, and—most importantly—buy a proper USB audio interface and microphone.

So, after purchasing and connecting a [U-Phoria UMC202HD](https://www.amazon.com/gp/product/B00QHURUBE/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=7dd50c707ef5c0f810ccaa8f98ec875d) and an [Electro-Voice RE320](https://www.amazon.com/EV-RE320-Variable-D-Instrument-Microphone/dp/B00KCN83VI/ref=as_li_ss_tl?s=musical-instruments&ie=UTF8&qid=1487964692&sr=1-1&keywords=re320&linkCode=ll1&tag=mmjjg-20&linkId=1f9fdf66013d4b25978f4bf92ae1e1e8) microphone, I was quite pleased with the sound quality!

I could tweak the levels so I could get a solid signal, 10-15 bars according to the macOS System Preferences' Sound input settings:

{{< figure src="./input-bars-15-level-system-preferences.png" alt="Input bars at 15 - good sound in System Preferences Sound Input panel" width="650" height="487" class="insert-image" >}}

Life was good.

But suddenly, one morning during a video chat through Zoom, others in the chat noticed that they could barely hear me! I checked the input levels and, sure enough, System Preferences said I was barely getting 1/4 of the normal levels!

{{< figure src="./yelling-six-bars-input-level-mac-sound-system-preferences-input.png" alt="Input bars at 6 max - not good sound in System Preferences Sound Input panel" width="650" height="487" class="insert-image" >}}

Putting on my debugger hat, I first checked all the physical connections:

  - I switched microphones—no difference.
  - I switched inputs on the Behringer—no difference.
  - I adjusted all the levels and tried to pad/not pad the inputs on the Behringer—no difference.
  - I switched XLR cables—no difference.
  - I tried different audio apps to see if I got any level differences—no difference.
  - I plugged and unplugged the USB cable on the back of the Behringer—no difference.

Something was seriously haywire! I finally thought about the full signal path going _into_ my Mac, and how I've had issues with my Gigabit Ethernet adapter (USB 3.0) not getting the full GigE speeds when there was a loose USB connection, or a flaky/cheap hub in the route from Ethernet to Mac... and so the next thing I tried immediately resolved the issue:

I unplugged the Behringer USB audio device from my TP-LINK 7-port USB 3 hub, and plugged it straight into my Mac.

Problem solved, full input levels again!

So, if you ever run into strange issues with your USB audio device, and it's plugged into a USB hub, check first whether it could just be a flaky USB port or a problem with the hub itself by directly plugging the device into your computer!
