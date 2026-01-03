---
nid: 2326
title: "AirPort Express - Flashing Yellow Light, Not Getting DHCP Address from Cable Modem"
slug: "airport-express-flashing"
date: 2011-07-09T20:38:15+00:00
drupal:
  nid: 2326
  path: /blogs/jeff-geerling/airport-express-flashing
  body_format: filtered_html
  redirects: []
tags:
  - airport
  - airport express
  - cable
  - dhcp
  - modem
  - motorola
  - networking
  - router
  - sb5105
  - Stub
  - wifi
aliases:
  - /blogs/jeff-geerling/airport-express-flashing
---

I spent the greater part of this afternoon trying to get my AirPort Express to connect to the Internet and share an IP address using a Motorola SB5101 Cable modem (with Charter Internet)... and since the solution was so simple and annoyingly stupid, I thought I'd post it here, for my reference and for anyone else spending an afternoon thinking his AirPort Express is dead.

As it turns out, the cable modem (this one, and likely <a href="http://100essays.blogspot.com/2008/07/comcast-airport-express-and-dhcp.html">many others</a>) will only remember the MAC address of the first device it recognized when you last power cycled the modem.

When the Internet went down at my condo yesterday, I turned off my cable modem, plugged my Mac straight into it, turned the modem on, and use the internet via this direct connection for a while. When I plugged the AirPort Express back into the SB5101, I just got a flashing yellow (amber) light, and in the Airport Utility, a notice that the 'Internet Connection wasn't working'.

After trying hundreds (well, tens, I guess) of different configurations, and having no luck, I finally power cycled the SB5101 while it was plugged into the AirPort Express, and voila! It worked!

Never had that problem with any of my other modems... but most of them were modem/router combos, so they were a little more intelligent anyways.

Now I can happily print to my printer wirelessly and share audio to my living room speakers easily again :-)
