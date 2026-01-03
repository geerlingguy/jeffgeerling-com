---
nid: 2753
title: "How I discovered my left AirPod was bad"
slug: "how-i-discovered-my-left-airpod-was-bad"
date: 2017-03-03T03:15:41+00:00
drupal:
  nid: 2753
  path: /blog/2017/how-i-discovered-my-left-airpod-was-bad
  body_format: markdown
  redirects: []
tags:
  - airpods
  - apple
  - bluetooth
  - connection
  - interference
  - mac
  - rf
  - wireless
---

> **tl;dr**: My left AirPod had some hardware issue. I got a new one. Now the AirPods work great.

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/8dmgSbObmOw" frameborder='0' allowfullscreen></iframe></div>

The morning Apple's AirPods went up for sale, I was boarding a plane, and had just gotten to my seat on the plane. I knew they'd be in short supply (though I didn't know _just how short_—my local Apple Store only gets a small batch every week, and they're sold out in hours!), so I quickly ordered a pair, then set my iPhone in airplane mode for takeoff.

<p style="text-align: center;">{{< figure src="./airpods-on-brown-paper.jpg" alt="AirPods on Brown Paper" width="520" height="335" class="insert-image" >}}<br>
<em>These things are awesome... though a little pricey.</em></p>

A few weeks later, I received my AirPods, and since then have been using them as my main audio headset and headphones with an iPad, iPhone and two MacBook Pros. _For the most part_, they've been amazing. Pairing _just works_ (no other way of putting it), switching between devices is great, and besides no ability to easily control volume, I have had no gripes with fit, finish, and functionality.

That is, except for a pesky connection problem that made use with my Macs a bit annoying. I noticed that if I were more than 2' away from my Mac, audio would drop momentarily, then as packets were retransmitted, audio would speed up and catch up to real-time again. The same thing happened with the mic on the AirPods, and it made for a truly annoying (and inconsistent) audio/video conferencing setup compared to my rock-solid (but tethered) USB audio headset.

Whenever I got a chance, I would try many different ways of isolating the problem. Starting with [Apple's own suggestions](https://support.apple.com/en-us/HT201542), I ran through the following tests to see if I could isolate some source of interference:

  - I disabled the 2.4 GHz 802.11g/b network on my AirPort Extreme router (Bluetooth also operates on 2.4 GHz)
  - I shut down _and unplugged_ all the other computers within a 20' radius of my MacBook Pro and myself (a Lenovo laptop, two Raspberry Pi 3s, and a Mac mini).
  - I powered off _and unplugged_ my two LG monitors (apparently some monitors can cause a bit of distortion, though it's usually pretty controlled).
  - I disconnected _everything_ in my office, and literally closed the breaker to my office and office lighting, so it was just me, my MacBook Pro (on battery power), and my AirPods.

I documented all the crazy things I was trying (including disabling services like AirDrop and WiFi on my Mac) in [this random Reddit thread](https://www.reddit.com/r/apple/comments/5rw1qv/airpods_anyone_else_have_itunes_pause_then_speed/), and spent more than an hour digging through the system Console logs to see if I could find some _software_ bug causing the issue. It was kinda random, but is _exactly_ the sort of randomness that indicates either:

  - Flaky hardware
  - Flaky software
  - A flaky connection between the two

This is one reason engineers _always_ prefer wired connections—that's the only flaky variable you can control (assuming good cabling!).

Getting nowhere fast, I started going crazy, wondering if my old HVAC system (about 15' away) could be sending some rogue signal, or if there was some NSA satellite beaming interference directly into my house or something. To be clear: my home office is _in my basement_. 8' underground, and I'm in a corner where there are **1' thick concrete walls on two sides**!

So after doing all that, and considering asking my Dad (who's an awesome electrical engineer and well versed in RF as he works in radio) to bring over a [spectrum analyzer](https://www.amazon.com/Rigol-DSA815-TG-Tracking-Generator-Spectrum/dp/B00CLWJA38/ref=as_li_ss_tl?ie=UTF8&qid=1488509154&sr=8-2&keywords=spectrum+analyzer&linkCode=ll1&tag=mmjjg-20&linkId=617dc6dbb33fc31835903248b482656c), I finally found a neat utility from Apple, 'Bluetooth Explorer'. This handy app lets you monitor many aspects of Bluetooth connections _in real time_. This was extremely helpful in finding the culprit.

## Bluetooth Explorer

{{< figure src="./bluetooth-explorer-icon-desktop.jpg" alt="Bluetooth Explorer App for macOS" width="280" height="200" class="insert-image" >}}

You have to download Bluetooth Explorer as part of the 'Additional Tools for Xcode' package that's available (registration required) at [https://developer.apple.com/download/more/](https://developer.apple.com/download/more/). Go to that link, then search for 'Additional', and find the Additional Tools package for the latest version of Xcode (you don't actually need Xcode installed to use the Bluetooth Explorer app!).

> Note: There is a 'Bluetooth Explorer' app on the Mac App Store. This is not at all the same as the one available from Apple!

After downloading it, open it up, and open the 'Connection Quality Monitor' (under the 'Devices' menu), as well as the 'Audio Graphs' (under the 'Tools' menu).

Now the fun begins—click start in both windows to start graphing Bluetooth RSSI and other quality indicators over time, then do things like move around your room, turn your head, turn on and off different devices, etc. But make sure you keep everything in one state/position for at least 5-10 seconds so you can see a good average reading of how it affects data rate, retransmission, RSSI, etc.

{{< figure src="./bluetooth-explorer-rssi-graphs.png" alt="Bluetooth Explorer - RSSI, retransmission, and other signal strength graphs" width="650" height="340" class="insert-image" >}}

The key metric that I monitored was **RSSI**, short for [Received Signal Strength Indication](https://en.wikipedia.org/wiki/Received_signal_strength_indication), a standard measure of the signal quality for wireless digital devices. In the case of bluetooth audio devices, a value from -40 to -60 would be pretty decent. -60 to -70 is marginal, but allows a clear connection. Beyond -70, and even very slight interference or movement can start causing a signal dropout.

So I started moving around the room, turning on and off different things, etc., and finally after trying all kinds of strange things, I popped out my left AirPod. Then I noticed something strange—when I was only using my _right_ AirPod, the RSSI indicated a range around -60 dBm. When I was only using my _left_ AirPod, the RSSI was around -75 dBm—**the left AirPod was almost 30x worse than the right one** ([dB use a log scale](https://en.m.wikipedia.org/wiki/Decibel))! Here's a graph to illustrate the problem:

{{< figure src="./bluetooth-rssi-remove-left-airpod.png" alt="Bluetooth RSSI with left and right airpod difference" width="650" height="406" class="insert-image" >}}

So I measured the same thing (swapping in one or the other AirPod) for a few minutes, with and without music, and also on my wife's MacBook Air and my other MacBook Pro (I have to be thorough!)—and it was exactly the same: about a 15 dBm difference!

After all this, I found that it was likely a _hardware_ problem with the left AirPod. Armed with that knowledge, I chatted online with Apple Support. They directed me to the Apple Store for a Genius Bar appointment. In both cases, I showed the graph, and the representative immediately agreed there was a problem with the left AirPod.

## Getting a new left <s>Ear</s> AirPod

I waited the obligatory 20 minutes or so past my appointment time for a Genius to come help me, and after I showed him the issue, he went to the store room to grab a spare left AirPod (apparently they have three boxes at the Apple Store, one with left AirPods, one with right AirPods, and one with cases!). If my AirPods were out of warranty, a replacement would cost $69, but since mine are still in warranty, it's a free replacement.

He pulled out the AirPod, dropped it in my AirPod case... and we saw an amber (orangeish) blinking light. So we held down the button on the back of the case 15 seconds to reset everything and... still amber! After we tried every possible incantation to get the AirPod, the case, and my good right AirPod synced up together, he went back to the store room to consult with other Geniuses (or who knows what—there always seem to be a dozen or so Apple Store employees streaming in and out of that room!).

<p style="text-align: center;">{{< figure src="./airpod-case-amber-light-noloop.gif" alt="AirPod case - amber light blinking" width="480" height="270" >}}<br />
<em>AirPod case - amber light blinking (click to play again).</em></p>

After another thirty minutes or so, he came back out with a new _case_, and after doing the 15-second reset with both my old (good) right AirPod and the new (also good) left AirPod, the new case displayed a white LED, meaning 'ready to pair'. So I paired it with my iPhone (poor iPhone... I think it had like 8 different 'Jeff's AirPods' in it's Bluetooth device list at this point!), and tested it out, and it finally started working!

Good to know, then: if you are only able to get one of your two AirPods connected to your device, and/or there's a blinking amber light on your AirPods' case and a 15-second-button-reset doesn't help, chances are there's something wrong with your case.

In the end, I brought home the mostly-new set of AirPods and case, and tested it on my two MacBook Pros—in both cases, the left and right AirPods gave almost identical RSSI levels. And instead of being able to walk maybe 10-15' away from my computer and hold a signal, I can walk about 50-60' while listening to music with no dropouts!

_Are you having connection issues with your AirPods? Let me know in the comments here, or on the YouTube video linked at the start of this post!_

> Apparently, you can also use this method to triangulate the position of a missing AirPod (e.g. you drop it and something's on top of it, so Apple's test tone locator doesn't help). Open up Bluetooth Explorer, start scanning, then move your Mac around until the signal strength gets stronger (like a game of hot or cold!). Thanks to [@cscotta](https://twitter.com/cscotta/status/867839516530233344) for that tip!
