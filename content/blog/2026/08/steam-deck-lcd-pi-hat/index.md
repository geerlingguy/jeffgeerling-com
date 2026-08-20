---
date: '2026-08-20T09:00:00-05:00'
tags: ['steam deck', 'hat', 'raspberry pi', 'level 2 jeff', 'youtube', 'video', 'touchscreen', 'linux']
title: 'Getting the Steam Deck LCD working on a Raspberry Pi'
slug: 'steam-deck-lcd-pi-hat'
---
The [BOE TV070WXM-TV0 LCD](https://www.aliexpress.us/item/3256806531632512.html?gatewayAdapt=glo2usa4itemAdapt) used in the original Steam Deck can be had for around $30. It's a serviceable 7" touchscreen with 400 nits of brightness and a resolution of 1280x800 (for a sharp 216 ppi).

{{< figure
  src="./steam-deck-lcd-pi-front-touch.jpeg"
  alt="Steam Deck LCD working on a Raspberry Pi 5"
  width="700"
  height="auto"
  class="insert-image"
>}}

The specs are a lot nicer than the [Pi 7" Touch Display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/), which costs twice as much, with giant bezels and half the resolution!

Until today, the Steam Deck LCD didn't work with a Raspberry Pi. But the folks at [Scandent](https://www.scandent.com) were trying to standardize on a mass-market touchscreen for one of their own devices, and built a [Linux kernel driver](https://github.com/ScandentLLC/tv070wxm-hat/blob/master/linux-rpi-6.12.y-panel-boe-tv070wxm.patch) for it which they intend to upstream.

Not only that, they've open sourced a [Pi HAT design](https://github.com/ScandentLLC/tv070wxm-hat/) which adapts the Raspberry Pi 5 or CM4's MIPI connection[^cm5] to the special 39-pin connector on the Steam Deck LCD.

{{< figure
  src="./steam-deck-lcd-pi-rear.jpeg"
  alt="Steam Deck LCD with a Raspberry Pi 5 mounted on its back"
  width="700"
  height="auto"
  class="insert-image"
>}}

The repository linked above has detailed build instructions, and the KiCAD project if you'd like to build a HAT of your own. Scandent was kind enough to send me not one but _two_ prototype HATs (the first one was damaged in shipping), and I put together this setup for testing:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/1pdZ7oePo-M' frameborder='0' allowfullscreen></iframe></div>
</div>

Scandent isn't planning on productizing the HAT, they just wanted a decent touchscreen they could use that will be in good supply for at least a few years. Making it more accessible to hobbyists or others building Pi-based touchscreen projects should strengthen the market for this LCD, too.

From what I understand, LCD panels like these are often built for a specific purpose, and if a product line that uses it stops being manufactured, the specific LCD gets discontinued at some point, meaning downstream users have to work on supporting _another_ one.

Just like switching from one SoC to another creates annoying rework, trying to sync up hardware signaling and a working kernel driver with multiple touchscreens is a pain.

{{< figure
  src="./steam-deck-lcd-assembly-pi-5-hat.jpg"
  alt="Steam Deck LCD working on a Raspberry Pi 5"
  width="700"
  height="auto"
  class="insert-image"
>}}

I tested the Steam Deck LCD on a Raspberry Pi 5, and found it to work quite well. In person, I didn't see any real flickering or waviness, and brightness was good, even under my studio lights.

The touch targets are a little bit iffy at the Pi's default resolution scaling, but if you bump that up or build your own HMI/UI, you can make this thing quite usable. Maybe someone out there will build out the rest of the hardware and a 3D print for a RetroPie-based open source Steam Deck?

[^cm5]: The CM5 should work, but has not yet been tested.
