---
nid: 3334
title: "My SimpliSafe doorbell lit its own fire this winter"
slug: "my-simplisafe-doorbell-lit-its-own-fire-winter"
date: 2023-12-18T20:10:25+00:00
drupal:
  nid: 3334
  path: /blog/2023/my-simplisafe-doorbell-lit-its-own-fire-winter
  body_format: markdown
  redirects: []
tags:
  - battery
  - burn
  - doorbell
  - fire
  - iot
  - security
  - simplisafe
---

...I'm just glad it was on the outside of the building, attached to non-flammable material :)

As part of my [new studio/office buildout](https://www.youtube.com/watch?v=VV-QOQE9A_4&list=PL2_OBreMn7FpmFf_nipMxvjKtz4Ch1ZgX), I needed a 'smart' doorbell, so I could accept deliveries or see who rang, even if I was far from the door or recording.

I bought a SimpliSafe system for my location, and tied it into Home Assistant. It was easy to set up, the monthly cost was a fraction of what ADT wanted to charge, and _yes_, I know it's wireless-only communication can be tampered with. It's like a lock—it helps keep people honest, and is only one small part of a balanced security diet.

{{< figure src="./simplisafe-doorbell-pro.jpg" alt="SimpliSafe Video Doorbell Pro" width="700" height="auto" class="insert-image" >}}

But I installed their [Video Doorbell Pro](https://simplisafe.com/video-doorbell-pro) a couple weeks ago, and setup was a breeze. Just get 24v doorbell wire to it, and bingo! You have a smart doorbell.

It worked great for about a week, then in the app it said the doorbell was 'Offline'. Actually, my kids were the first to notice—they visited and I heard knocking on the window... they said they tried ringing the doorbell but it wouldn't do anything!

Well, today I finally had the time to troubleshoot it, and I [followed SimpliSafe's guide](https://support.simplisafe.com/articles/video-doorbell-pro/video-doorbell-pro-stopped-working/6347edf36d37080c83e5b0d1), but nothing got any response. The thing was dead as a doornail. Or, well, as a doorbell, I guess.

Probing the device further, I found I could pop off the front cover, and get at 8 screws around the perimeter. Removing those, I noticed the bottom would not pop out. I explored the back, and thought there may be a hidden 'warranty voiding' screw under the serial number sticker, but no... the bottom was just kinda glued to the case.

And after prying it carefully open, I found out why:

{{< figure src="./simplisafe-doorbell-disassemble.jpg" alt="SimpliSafe Video Doorbell Pro Teardown Disassembled" width="700" height="auto" class="insert-image" >}}

Looking more closely at the bottom wires—where it looks like the battery wires come off and go around a small PCB to a soldered connection—the plastic insulation was completely burnt off for a few mm, and they were obviously shorting to each other:

{{< figure src="./simplisafe-video-doorbell-burnt-wires.jpg" alt="SimpliSafe Video Doorbell Pro burnt wires" width="700" height="auto" class="insert-image" >}}

It looks like it could be a design flaw—it probably isn't a problem _most_ of the time, but when you have the Li-Ion battery wires pass through a space where they could get pinched by a PCB during assembly... that could easily become the point of failure on many devices.

My best guess is my particular unit was assembled in a way where the battery wires were not carefully positioned as the PCB stack was inserted into the enclosure, and they got pinched between the outer plastic and the PCB.

It only took a week or so of running through hot/cold cycles (my doorbell is on a South-facing wall) before the little battery wires started to short out and burn up the plastic inside.

I contacted SimpliSafe, and a replacement unit is on the way (I may crack it open and take a peek at the wires before installing it!). I also have to give them a shout out for not having _any_ proprietary screw heads or warranty-void-if-removed stickers impeding access to the device.

> **Update, Dec 9**: SimpliSafe actually reached out today after noticing my Twitter post, and we talked in detail about the failure. They mentioned 24v is actually around the upper end of what the doorbell can handle. I re-measured the leads on the base coming from the AC transformer I bought, and it's 26V...
>
> So then I went over to the [Amazon page for the Jameco Reliapro MGT2450P](https://amzn.to/3Ru8C1C) transformer I bought, and dove into the reviews. Someone else ('Evicient') seems to have had the _exact_ same problem I did:
>
> {{< figure src="./smoked-doorbell-jameco-24v-transformer0.jpg" alt="Burnt up SimpliSafe with 24v Jameco Transformer" width="700" height="auto" class="insert-image" >}}
>
> I'm waiting to hear back from the SimpliSafe engineers tomorrow, but it sounds like the problem may be their doorbell is really not meant to exceed 24V—and this transformer supplied just a tad bit too much power.
>
> That would also explain why it worked fine for a week or so... then eventually the wires melted as they're just not able to handle anything more than 24V. I've asked what transformer they might recommend as a replacement. I also suggested their setup guide maybe provide recommendations for new builds, as it currently assumes you're replacing an existing doorbell.
>
> Kudos to them for being proactive about this—and maybe they'll introduce a Video Doorbell Pro 2 with a higher voltage tolerance ;)
