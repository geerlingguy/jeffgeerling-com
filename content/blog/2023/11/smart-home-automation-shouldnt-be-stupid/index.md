---
nid: 3324
title: "Smart home automation shouldn't be stupid"
slug: "smart-home-automation-shouldnt-be-stupid"
date: 2023-11-06T18:21:13+00:00
drupal:
  nid: 3324
  path: /blog/2023/smart-home-automation-shouldnt-be-stupid
  body_format: markdown
  redirects: []
tags:
  - automation
  - cm4
  - compute module
  - home assistant
  - iot
  - smart home
  - yellow
---

{{< figure src="./jeff-light-switches-smart-iot.jpg" alt="Jeff Geerling holds a dumb not smart light switch" width="700" height="394" class="insert-image" >}}

There are far too many smart home devices which make using a device _harder_. Like a light switch and light bulb that requires a wireless connection to a hub in order to control the lights.

Before, you could flick a switch, and a light would come on.

Now, you have to ensure the light has power, the switch has power, and the hub has power. And the wireless connection between switch, hub, and light needs to be reliable. And the hub can't lock up or go offline. And if it's anything like most modern IoT devices, the hub needs a reliable Internet connection and cloud account, or things will start failing at some point.

That's dumb.

And that's just light switches. Can you imagine relying on this kind of 'smarts' for essential services in your home, like HVAC, water supply, etc.?

To be truly 'smart', I follow three principles for home automation. Every smart device must be:

  1. Local
  2. Private
  3. Additive

Local, meaning all communication must happen on a local network (wired, wireless... it must never need an Internet connection for any functionality).

Private, meaning there should be no cloud account required for any functionality. Nor should any of my usage data ever flow out to the Internet.

Additive, meaning all base functionality must work, regardless of Internet access, local network conditions, etc.

For example, the [Leviton Zigbee light switches](https://amzn.to/3MxsSOp) I use are light switches.

They turn lights on, and turn lights off. You can always turn on and off your light by physically pressing the light switch paddle. No wireless connections required.

They also include a zigbee radio inside so I can _add_ smarts to the switches if I want. But all functionality is available locally at the switch, and they will work regardless of any other automation or smart system.

In my 8th office moving vlog, I walk through how I'm setting up my new _office_ using these smart home automation principles (Local, Private, Additive) using a [Home Assistant Yellow](https://www.home-assistant.io/yellow/):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/vTwyInX4KyM" frameborder='0' allowfullscreen></iframe></div>
</div>
