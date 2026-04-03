---
date: '2026-04-03T09:00:00-05:00'
tags: ['raspberry pi', 'modem', 'dial up', 'marchintosh', 'youtube', 'video', 'ibook', 'g3', 'apple', 'mac', 'linux', 'open source', 'ppp']
title: 'Build your own Dial-up ISP with a Raspberry Pi'
slug: 'build-your-own-dial-up-isp-with-a-raspberry-pi'
---
Last year my aunt let me add her [original Tangerine iBook G3 clamshell](https://everymac.com/systems/apple/ibook/specs/ibook.html) to my collection of old Macs[^midlifecrisis].

{{< figure
  src="./pi-isp-ibook-hero.jpeg"
  alt="iBook G3 accessing dial-up Internet over WiFi browsing the vintage web"
  width="700"
  height="auto"
  class="insert-image"
>}}

It came with an AirPort card—a $99 add-on Apple made that ushered in the Wi-Fi era. The iBook G3 was the first consumer laptop with built-in Wi-Fi antennas, and by _far_ [the cheapest way](https://www.eetimes.com/the-secret-success-of-steve-jobs-wireless-internet/) to get a computer onto an 802.11 wireless network.

I go into more of the history of Apple's AirPort and iBook G3 in today's video (embedded below), but something I've always wanted to do is emulate a dial-up ISP locally.

What better way to do it than through Wi-Fi? Wait, _what?_

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/GbIoEZZwcgw' frameborder='0' allowfullscreen></iframe></div>
</div>

Wi-Fi as we know it today typically routes fiber or cable Internet connections, with bandwidth measured in megabits or even _gigabits_.

But WiFi in 1999 (when the AirPort was released) maxed out at 11 Mbps. And half that, in real world conditions.

{{< figure
  src="./pi-isp-airport-missing-apple-leaf.jpeg"
  alt="Apple AirPort Base Station with missing Apple Leaf"
  width="700"
  height="auto"
  caption="It's hard to find an AirPort Base Station with an intact Apple leaf."
  class="insert-image"
>}}

The AirPort Base Station included a 10base-T Ethernet jack (for the rare few who had access to broadband), alongside a 56K dial-up modem. Most people going wireless in 1999 were still using AOL or some other dial-up ISP.

I had purchased a used first-generation AirPort Base Station _years_ ago for an unrelated project that never got anywhere, so I figured I'd challenge myself this [#MARCHintosh](https://marchintosh.com) to see if I could run my own local dial-up ISP, using a Raspberry Pi—and then unite dial-up speed with 802.11b Wi-Fi!

## Hardware

{{< figure
  src="./pi-isp-dle-200-pi-5.jpeg"
  alt="Pi ISP Hardware - Raspberry Pi, StarTech.com 56K Modem, and Viking DLE-200B"
  width="700"
  height="auto"
  class="insert-image"
>}}

POTS, or the Plain Old Telephone System, is tricky to emulate. You can't just plug one modem into another. So in addition to a modem for my 'Pi ISP', I need a telephone line simulator.

> Aside: I could also build my own little [PBX](https://en.wikipedia.org/wiki/Business_telephone_system) with some VoIP hardware, but I'm saving that for a future project... I have plans :)

I chose the following hardware to build out my ISP:

  - SBC ($40): Raspberry Pi 3, 4, or 5[^sbcchoice]
  - Phone Line Simulator ($120): [Viking DLE-200B Two-Way Line Simulator](https://amzn.to/3NnJETN)
  - Modem ($45): [StarTech.com 56K USB Dial-up Modem](https://amzn.to/3NJMeTZ)

You may also need a few phone cords to plug everything together. You plug the USB modem into a USB port on the SBC, then plug a phone cord between the modem and the phone line simulator.

Then plug another computer (in my case, the iBook G3) into the other phone jack on the phone line simulator.

I switched dip switch #3 to the 'UP' position to decrease the audio volume, since the modems can achieve slightly better speeds that way.

With this setup, assuming you haven't changed any other defaults on the DLE-200B, either modem picking up will ring twice, then automatically pick up the other line.

{{< figure
  src="./pi-isp-all-parts.jpeg"
  alt="Pi ISP Hardware - including old phones"
  width="700"
  height="auto"
  class="insert-image"
>}}

If you want to get fancy like I did, you can add in a bell-style telephone in the mix (pictured above). Plug the 'Line' jack into the phone line simulator, and the modem in to the 'Data' jack.

With this setup, whenever the computer calls into the ISP, any rings will result in a nice, loud _physical_ ring on the phone before the ISP modem picks up (useful for debugging!).

## Software

TODO: https://github.com/geerlingguy/pi-isp

## The Internet at 33.6 kbps

pi-isp-remote-access-mac-os9.jpeg

TODO.

pi-isp-download-2.8kbps-bugdom.jpeg

TODO.

pi-isp-macproxy-classic-proxy-ie.jpeg
pi-isp-macproxy-classic-jeffgeerling-ssl.jpeg

pi-isp-pickup-phone-modem-connected.jpeg

TODO.

## Dial-up over WiFi

pi-isp-new-battery-ibook.jpeg

TODO.

pi-isp-airport-connected-dialup.jpeg

TODO.

pi-isp-wavelan-powerbook-g3.jpeg

TODO.

## Conclusion

TODO.

[^midlifecrisis]: Apparently collecting and restoring old computers has become my mid-life crisis. In the beginning I told myself I'd keep it to one rack's worth of computers. Now I have multiple generations of Macs, a few PCs, a couple drawer sets of spare parts, bins for cleaning, multiple rework stations, a few broken donor units... what have I gotten into?!

[^sbcchoice]: You can technically use any computer, though. Use some old PC if you want, the main thing is it needs to run Debian-flavored Linux, to work with the software I set up. Other Linux distros may work, but might need some tweaks.
