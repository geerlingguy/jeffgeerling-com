---
nid: 3457
title: "BPS is a GPS alternative that nobody's heard of"
slug: "bps-gps-alternative-nobodys-heard"
date: 2025-04-08T21:25:32+00:00
drupal:
  nid: 3457
  path: /blog/2025/bps-gps-alternative-nobodys-heard
  body_format: markdown
  redirects:
    - /blog/2025/bps-alternative-gps-nobodys-heard
aliases:
  - /blog/2025/bps-alternative-gps-nobodys-heard
tags:
  - bps
  - broadcast
  - gps
  - location
  - nab
  - time
  - timing
---

I came to the NAB (National Association of Broadcasters) show this year with my Dad to learn more about time in broadcast and live production.

I was expecting to learn more about grandmaster clocks, AV sync, timing in protocols like Dante, Livewire, AES67, and more—and I _have_. But then on the first day here I found this odd little corner of the building with a completely empty booth:

{{< figure src="./bps-demo-booth-empty.jpeg" alt="BPS Demo Booth - it is empty" width="700" height="467" class="insert-image" >}}

When you see an oscilloscope that costs 3x the value of your car on a trade show floor... well, let's just say my interest was piqued.

I looked at it, and found something interesting—the trigger was on a GPS PPS timing signal output from a u-blox GPS receiver. But the 2nd channel was monitoring [KSNV-TV](https://news3lv.com), a US television station broadcasting an _ATSC 3.0_ signal.

{{< figure src="./bps-gps-vs-ksnv-timing-signal.jpg" alt="BPS KSNV-TV vs GPS pps" width="700" height="394" class="insert-image" >}}

The scope showed a PPS output (Pulse Per Second) demonstrating a pulse sync of +/- 10 ns between GPS and the TV signal output—which so happens to be _BPS_ (Broadcast Positioning System), an experimental timing standard that may be incorporated into the ATSC 3.0 rollout in the US (there are currently about 1,700 TV stations that could be upgraded).

{{< figure src="./bps-scope-10-ns-sync-gps.jpg" alt="BPS showing 10ns sync" width="700" height="394" class="insert-image" >}}

After seeing the demo, I found out there _are_ a few people who've heard of BPS... and many of them were presenting on it, as they were also the ones who were doing the initial rollout and experimentation.

ATSC 3.0 is a newer IP broadcast standard being rolled out in some countries—my own home city has two TV stations broadcasting it right now, under the 'NEXTGEN TV' moniker. But so far only a few TV stations are participating in the BPS testing.

Because accurate timing is critical in many areas, from media, to the power grid, to 5G and communications, having a reliable terrestrial backup to GPS—especially one that can be hardened against different types of jamming attempts—may be important to our economy, communications and power grid... or people like who just want to have a good time!

And speaking of time stuff at the NAB Show... can you guess what I'm pointing to in this photo, from the ASUS booth?

{{< figure src="./jeff-geerling-nab-2025-asus-proart-motherboard-pps-tgpio.jpeg" alt="Jeff Geerling pointing to PPS in out on ASUS ProArt motherboard" width="700" height="394" class="insert-image" >}}

If you guessed built-in PPS in/out connectors on a consumer Intel motherboard that syncs to [TGPIO](https://eci.intel.com/docs/3.0/development/tcc-tools.html) (Time-Aware GPIO) on an Intel CPU... you'd be right! And if you have no clue what that means, well, I'll cover it more in depth later this year :)

Anyway, I am still learning about BPS, so I'll probably go deeper into it later in my timing series on my YouTube channel, but for now, I'll leave with with a quick video showing the demo (below), and a couple links for those who want to learn more:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/cPCzNdUz5z0" frameborder='0' allowfullscreen></iframe></div>
</div>

More resources:

  - [BPS / NIST time experiment results](https://www.nab.org/bps/ITM25-0009.pdf)
  - [NAB PILOT - BPS Info](https://nabpilot.org/broadcast-positioning-system-bps/)
  - [UrsaNav's eLoran timing](https://www.ursanav.com/wp-content/uploads/UrsaNav-PTTI-Conference-Presentation.pdf)
