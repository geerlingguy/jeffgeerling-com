---
nid: 3260
title: "Limiting Handbrake threads to prevent throttling on M2 Macbook Air"
slug: "limiting-handbrake-threads-prevent-throttling-on-m2-macbook-air"
date: 2022-12-19T20:31:11+00:00
drupal:
  nid: 3260
  path: /blog/2022/limiting-handbrake-threads-prevent-throttling-on-m2-macbook-air
  body_format: markdown
  redirects: []
tags:
  - handbrake
  - m2
  - macbook
  - macbook air
  - overheating
  - throttling
  - transcoding
---

Due to a recent surgery, I've been recovering at a location outside my home for a few weeks. I brought all my media with me on a spare hard drive, but one movie I had ripped but never transcoded wouldn't play on the 'Smart' TV here.

It seems to do okay with some H.264 profiles, but not the one for this 4K Blu-Ray rip. Therefore, I thought I'd transcode the file so it would play.

I also wanted to do other work on my laptop—in my lap. And unfortunately for Apple's latest M2 MacBook Air, [there's no fan or heat sink to keep the M2 SoC cool](https://www.theregister.com/2022/07/21/m2_macbook_air_teardown/).

And that meant the temperature around the top middle of the keyboard—and the bottom middle of the laptop—got quite uncomfortably hot with Handbrake's default settings, which would max out the CPU during the transcoding process.

I could encode anywhere between 10-18 fps at 4K resolution with x264, but the SoC temperature rose to 105°C and was uncomfortably hot within a minute or so.

So to limit Handbrake a bit—which would slow rendering to 5-10 fps but also not cook my lap—I added `threads=2` to the 'Additional Options' field in Handbrake's Video settings:

{{< figure src="./handbrake-threads-2.jpg" alt="Handbrake threads=2 setting in video encoding options for x264" width="700" height="538" class="insert-image" >}}

It seems that for x265, the setting you may need is `pools=2` instead of `threads=2`, but I haven't tested that (the 'smart' TV on which I'm trying to play back the file might be too old to support H.265 and I'm too lazy to encode a file and test it, or to find the TV's model number and look up the specs).

Now the CPU is happily distributing the load amongst the four performance cores and keeping the SoC down at a more sane 85°C average:

{{< figure src="./85-degrees-C-menubar.png" alt="85 degrees celcius SoC temperature on M2 MacBook Air" width="488" height="74" class="insert-image" >}}

(The menu bar stats thing is called [iStat Menus](https://bjango.com/mac/istatmenus/).)

And yes, I could just play back the file from my laptop straight to the TV, but that would require I dig around to find a USB-C to HDMI adapter, since this M2 MacBook Air only has ThunderBolt 4 USB Type C ports.

Maybe I should've just gotten an M1 Max MacBook Pro instead. It has a fan, built-in HDMI, and for good measure, a built-in SD card reader so I could skip carrying around a separate dongle for _that_ too!
