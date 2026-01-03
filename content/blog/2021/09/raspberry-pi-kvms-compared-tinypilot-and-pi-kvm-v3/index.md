---
nid: 3127
title: "Raspberry Pi KVMs compared: TinyPilot and Pi-KVM v3"
slug: "raspberry-pi-kvms-compared-tinypilot-and-pi-kvm-v3"
date: 2021-09-22T14:07:05+00:00
drupal:
  nid: 3127
  path: /blog/2021/raspberry-pi-kvms-compared-tinypilot-and-pi-kvm-v3
  body_format: markdown
  redirects: []
tags:
  - dad
  - kvm
  - pi-kvm
  - radio
  - raspberry pi
  - remote
  - remote access
  - tinypilot
  - video
  - youtube
---

In a strange coincidence, the authors of [TinyPilot](https://tinypilotkvm.com) and [Pi-KVM](https://pikvm.org) both emailed me within a week of each other and asked if I'd be interested in one of their KVM devices.

{{< figure src="./tinypilot-vs-pi-kvm-price.jpg" alt="TinyPilot vs Pi-KVM v3 Price comparison" width="600" height="340" class="insert-image" >}}

Michael Lynch, founder of Tiny Pilot, said he'd used some of my Ansible work in building the [TinyPilot update system](https://github.com/tiny-pilot/tinypilot), and Maxim Devaev, of Pi-KVM, liked my Pi open source content, and wanted to see what I thought of the new v3 kit that's [currently on Kickstarter](https://www.kickstarter.com/projects/mdevaev/pikvm-v3-hat).

I took them both up on the offer, and dug into both devices.

Both have HDMI and USB inputs, so you can plug them into any Mac or PC and get full control, up to and including BIOS/UEFI settings, remote desktop management (with no software on the managed computer), and mounting of USB ISO images for re-installing an OS or maintaining a system.

{{< figure src="./pi-kvm-atx-breakout.jpg" alt="Pi-KVM ATX breakout board" width="461" height="400" class="insert-image" >}}

But the Pi-KVM goes even further with hardware ATX support for things like pressing the physical power button, pressing the reset button, and monitoring the power and status LEDs through the motherboard.

It also seems to have a bit more of the 'hacker' mentality in all things around it, including the code, the DIY aspects, and even the full v3 kit that comes with some assembly required, and also doesn't include a Pi 4 model B or a pre-flashed microSD card.

The TinyPilot Voyager, on the other hand, comes with everything set up, ready to go. It's truly a plug-and-play experience.

But you pay for that! It's a bit more expensive than a Pi-KVM v3, even after the price of all the additional parts is factored in. The TinyPilot Voyager is $350, though there's a Kit version with a little less panache for less than $200. The Pi-KVM is $150 currently, but as mentioned requires some additional accessories, including a Raspberry Pi.

I made a video reviewing both devices in a bit more detail, and I also included an in-depth review / interview with my Dad, who's a radio engineer, and has a _lot_ more experience than I do deploying KVMs.

{{< figure src="./rack-room-kmox-st-louis.jpg" alt="Rack room at KMOX Studios in St. Louis, MO" width="533" height="400" class="insert-image" >}}

His main studio facility in St. Louis feeds over 40 remote tower sites for different radio stations, and as the sole engineer for his radio network, he needs as much remote control as he can get—otherwise when stations go off the air, it's time for someone to hop in a car and get to the broken computer!

Check out the full video for that interview and my final thoughts on these two KVM devices:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/TIrkEr2AeDY" frameborder='0' allowfullscreen></iframe></div>
</div>
