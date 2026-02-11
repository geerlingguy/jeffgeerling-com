---
date: '2026-02-07T09:00:00-06:00'
tags: ['smpte 2110', 'geerling engineering', 'youtube', 'video', 'truck', 'broadcast', 'time', 'ptp']
title: 'Exploring a Modern SMPTE 2110 Broadcast Truck With My Dad'
slug: 'exploring-a-modern-smpte-2110-broadcast-truck-with-my-dad'
---
In October, my Dad and I got to go behind the scenes at two St. Louis Blues (NHL hockey) games, and observe the massive team effort involved in putting together a modern digital sports broadcast.

{{< figure
  src="./blues-game-production-truck-prod-room.jpg"
  alt="Broadcast production room in 45 Flex truck at a Blues game"
  width="700"
  height="auto"
  class="insert-image"
>}}

I wanted to explore the timing and digital side of a modern [SMPTE 2110](https://www.smpte.org/standards/st2110) mobile unit, and my Dad has been involved in studio and live broadcast for decades, so he enjoyed the experience as the engineer _not_ on duty!

We were able to interact with everyone on the broadcast team, from the announcers and camera operators in the bowl, to the team in the truck, and even the engineer and production crew behind the in-house production.

I learned a lot—like why they use bundles of analog copper wire for audio instead of digital fiber—but the part where I learned the most was when I put on the headset in the truck. (My Dad is pictured below, in the tape room:)

{{< figure
  src="./joseph-geerling-headset-broadcast-truck.jpg"
  alt="Broadcast production room in 45 Flex truck at a Blues game"
  width="700"
  height="auto"
  class="insert-image"
>}}

There was constant chatter about upcoming shots, promos to hit, plays that would be referenced at the next break, replays that were ready to go... it was honestly overwhelming, listening in.

But as I mention in our latest Geerling Engineering video on the experience, the overall mood in the truck felt _solemn_.

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/8Ar4wmA4ujM' frameborder='0' allowfullscreen></iframe></div>
</div>

Solemn is strange way to describe it, but it's the only word I can think of. Through the constant chatter, there's a quiet professionalism. Talk is structured, and purposeful.

If you want to see that in effect, watch the video above. I included a few minutes of raw footage from the truck, which conveys the atmosphere a thousand times better than I can put to words.

For the rest of this post, I'll focus on some of the tech and equipment I spotted, since that's easier to describe on the blog.

## SMPTE 2110, PTP Timing, and Media Distribution

The main reason I wanted to tour the truck was to see their clocks. Specifically, the master clocks I *knew* must be present for the digital SMPTE 2110 media network. Video, audio, and metadata have to be in sync just like [black burst sync](https://en.wikipedia.org/wiki/Black_and_burst) of old, because live broadcast is real-time.

{{< figure
  src="./evertz-master-clocks-45flex.jpg"
  alt="Evertz master clocks on 45 Flex SMPTE 2110 broadcast truck"
  width="700"
  height="auto"
  class="insert-image"
>}}

The [45 Flex truck](https://www.mobiletvgroup.com/mobile-unit/45-flex-vmu/) (from Mobile TV Group) had a set of two [Evertz 5700MSC-IP](https://evertz.com/products/5700MSC-IP) 'Root Leader' Grandmaster clocks, along with a [5700ACO Changeover](https://evertz.com/products/5700ACO). This set of timing gear will run you a cool $25-30k, but it's critical to have perfect time sync for all the digital broadcast gear, so the cost seems justified.

Anyone who's worked with PTP has battle scars, and this truck's engineer, Chris Bailey, mentioned a handy tool he relies on to debug timing issues, a [Tektronix PRISM](https://download.tek.com/datasheet/PRISM-Media-Analysis-Solution-Datasheet-2MW614620.pdf) IP engineering test tool:

{{< figure
  src="./tektronix-prism-in-45-flex-truck.jpg"
  alt="Tektronix PRISM in 45 Flex truck"
  width="700"
  height="auto"
  class="insert-image"
>}}

This tool gives insights into timing signals (and other IP traffic) inside the truck's network, so they can quickly debug problems with time services or traffic routing.

I assumed it would use GPS for a precise 'world time' reference, to set its clocks. But when I asked Chris to show me the process, he surprised me by pulling out his mobile phone and manually setting the it with the [Atomic Clock (Gorgy Timing) app](https://apps.apple.com/us/app/atomic-clock-gorgy-timing/id295302256) (pictured above).

Studios and datacenters are fixed infrastructure, and you can plan out a GPS antenna location and cable routing as part of the buildout. But in live event broadcast, where the truck moves from place to place, you're not guaranteed a clear view of the sky, and can't rely on venue timing signals[^enterprise].

So inside the 45 Flex, Chris most often sets the clock manually, accurate to within a second. Apparently they only need true _world_ time if they're synchronizing with more than one truck, or across multiple event spaces (e.g. at the Olympics). Otherwise, the 'precision' in PTP is good enough, and doesn't depend on the accuracy of the actual time (in comparison to UTC, TIA, etc.).

The Evertz boxes output multiple timing signals, but the one I'm most familiar with is [PTP](https://en.wikipedia.org/wiki/Precision_Time_Protocol), or the Precision Timing Protocol. PTP is used to sync time across datacenter networks via IEEE 1588, across audio networks via AES67, and across SMPTE 2110 via [SMPTE 2059-2](https://en.wikipedia.org/wiki/SMPTE_2059).

Timing signals have a lot of acronyms.

But this timing signal distributes a time to the entire truck's IP network, most importantly to the video switcher, cameras, and replay systems (this truck has a tall stack of [EVS XT-VIA](https://evs.com/products/live-production-servers/xt-via) servers for that purpose).

Inside the truck, there's more fiber and Ethernet cabling than SDI and analog audio—though that doesn't always extend _outside_ the truck.

## Hybrid connectivity

Indeed, one of the most impressive sights (and an area that turns into a hive of activity before and after every event) was the Enterprise Center's patch bay:

{{< figure
  src="./patch-bay-enterprise-center.jpg"
  alt="Enterprise Center patch bay on game day"
  width="700"
  height="auto"
  class="insert-image"
>}}

On the left side are hundreds of XLR connections. Giant 'trunk' cables connect multiple balanced audio signals between the truck's exterior IO panel and the patch bay. Then dozens of patches are made into the building's internal wiring, to get headsets, comms, fixed microphones, and wireless receivers patched through to the truck's giant [Calrec Artemis console](https://calrec.com/shop/broadcast-audio-consoles/artemis/).

In the middle there are dozens of yellow fiber patches for data and video routing, and on the right side was a connector entirely new to me, called a [SMPTE connector](https://www.lemo.com/int_en/solutions/specialties/3k-93c-y-smpte-hybrid.html) (or, if you want to get _really_ technical, "3K.93C.Y").

{{< figure
  src="./smtpe-connector-in-enterprise-center.jpg"
  alt="Enterprise Center patch bay on game day"
  width="700"
  height="auto"
  class="insert-image"
>}}

When they [renovated the facility in 2016](https://www.archkey.com/project/enterprise-center/), the Enterprise Center made a ton of infrastructure upgrades, including running fiber all over the place (sometimes alongside old coax runs, which could still be used for older analog productions!).

The SMTPE cabling has a hybrid fiber + copper connection. Data is transferred over the fiber pair, while power is delivered over copper, for up to 8K camera signals over hundreds of meters. Pretty neat stuff, and the connectors are quite rugged.

Speaking to Chris Frome, the building's engineer who worked on the renovations, digital has made video and audio signaling issues a thing of the past—for the most part. He said because so many events come through, each with their own equipment and connections, dirt is one of the greatest enemies. Even with covers on all the patch bay ports and cables, dirt can cause a digital connection to go down enough they know to clean the connectors first, before debugging problems further down the stack.

They probably deal with more 'Layer 0' problems than most!

## Conclusion

There's a ton more in the video I can't relate easily in this post; this is one of the few times I'd recommend watching the video over reading the blog (if you had to choose).

{{< figure
  src="./tony-west-hands-on-robocam-controls.jpg"
  alt="Tony West operating the robocam at a Blues game"
  width="700"
  height="auto"
  class="insert-image"
>}}

But coming out of the experience, the thing that impressed me most was all the human touches, and the team _using_ this equipment.

Like Tony West (pictured above, at the primary robocam's controls): he works to get every shot on the camera that's _always_ closest to the action (hovering slightly over the ice), and doesn't have to think about the cabling and timing signals making his camera integrate seamlessly with the rest of the system.

I met a number of professionals, from audio, to video, to replay, to production specialists. And they were all part of a team, focused on using the technology at hand to deliver the best product they can, to all the fans watching along at home.

And they do this at least a dozen times per month, arriving many hours before each game, working late into the night.

It was an honor to be able to learn from them.

[^enterprise]: The Enterprise Center _does_ have its own robust timing infrastructure, with redundant grandmaster clocks, and two separate GPS antennas—but routing the building's timing signal into the truck is not as convenient as relying on the trucks' own signal for its own broadcast equipment.
