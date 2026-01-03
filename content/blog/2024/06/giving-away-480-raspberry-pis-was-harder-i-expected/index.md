---
nid: 3385
title: "Giving away 480 Raspberry Pis was harder than I expected"
slug: "giving-away-480-raspberry-pis-was-harder-i-expected"
date: 2024-06-13T20:27:26+00:00
drupal:
  nid: 3385
  path: /blog/2024/giving-away-480-raspberry-pis-was-harder-i-expected
  body_format: markdown
  redirects: []
tags:
  - 3d printing
  - maker
  - open sauce
  - pico
  - raspberry pi
  - video
  - youtube
---

I gave away 480 Raspberry Pi _Picos_ at [Open Sauce](https://opensauce.com) last weekend, and ran into a number of challenges doing so. All of them self-inflicted, of course. I didn't want to just hand them out like candy—or, well... that's _exactly_ what I did:

{{< figure src="./piz-dispenser-with-pez-dispenser.jpg" alt="Raspberry PIZ Dispenser with little Star Wars PEZ Dispenser" width="700" height="auto" class="insert-image" >}}

My initial plan was to build a backpack mount for a [full 480-Pico reel](https://makerbright.com/raspberry-pi-pico-reel-bulk.html) (they sell them in bulk like that, for pick-n-place machines). However, there was a major flaw with that design.

## Constraints

I needed to get through TSA, so I could fly to San Francisco. Driving was out of the question, as my wife is almost full-term and I could not leave her for more than a week in the middle of summer, when the kids have about 15 events per week!

A full reel would require a knife or scissors, and I didn't want to check the bag whatever I built was in.

> Note: A few weeks later, I now realize I could've acquired the appropriate size knife/scissors in San Francisco, or packed the sharp object in a checked bag, and not had to worry about the TSA issue. Oh well, hindsight.

The other constraint was I needed to fit whatever I built in my carryon, and it had to have something 'maker-ish' about it (so not just pouring Picos in a giant bowl and handing them out that way).

So my idea? A PIZ dispenser. Like a [PEZ dispenser](https://us.pez.com/collections/dispensers), but for Pis.

{{< figure src="./piz-dispenser-16.jpeg" alt="PIZ Dispenser next to PEZ Dispenser Darth Vader" width="700" height="auto" class="insert-image" >}}

There are some notable differences between Picos and PEZ hard candy:

  - PEZ have a more brick-like shape, meaning they are a rigid structure with no voids around the outside or flimsy bits. Picos come in trays with a flimsy plastic tray and an even more flimsy protective plastic film on top
  - PEZ are much taller, proportionally. You can pack more Picos in one dispenser, but they do not take up as much vertical space, so the pusher mechanism can't be quite as simple
  - Picos are not edible[^edible]

## Learning Fusion 360—in one day

I've long wanted to learn two bits of 3D design software: Blender and Fusion 360. For years, I've used Photoshop and Illustrator to retouch photos, design vector art, and generate 2D artwork.

So I thought at least some of those illustrator skills would be transferrable to 3D CAD software. Unfortunately, they are not.

Fusion 360 was a bit frustrating to learn. The premise is: sketch in 2D, extrude, and modify. But the sketching is sketchy, the extrusions are sometimes a bit maddening, and modifying them creates a strange dependency chain that can be hard to navigate if you need to modify certain aspects later!

{{< figure src="./fusion-360-pi-head-design-piz-dispenser.jpeg" alt="Fusion 360 - Pi Head Design" width="700" height="auto" class="insert-image" >}}

I touch on some of the weird things I encountered in my video (embedded later), but I will say I _do not_ recommend trying to learn Fusion 360 in a day. Especially if you need some production-ready parts printed 3 days later.

It's also expensive, and I kinda hate how Autodesk killed off Meshmixer and doesn't really seem to have a maker-friendly outlook with their subscription models and software design.

They *do* have a pretty strong support site and community, so it's not that hard to get over all the normal humps you encounter... but it wasn't simple, and sometimes I almost longed for OpenSCAD and raw algebra instead of the quirky GUI.

## 3D Printing has evolved

The _huge_ problem I ran into on Monday—with four days remaining—was 3D printer speeds. I was stuck waiting for 6, 9, or _12_ hours per part on my Ender 3 V2. Even with that and my Ender 3 S1 going at the same time, I could only print a few parts a day.

My plan was to print 40 parts total (pusher, tray, shell, and head), and I calculated it would take at least two weeks printing 24x7.

So I did two things:

  1. Phone a friend — I asked local maker [STL Denise 3D](https://stldenise3d.com) if she could help, and she graciously tasked a couple of her printers to shells and pushers.
  2. Bought a new printer — I ran to Micro Center and bought the fastest 3D printer they had in stock, the [Bambu Labs P1S Combo with AMS](https://www.microcenter.com/product/668656/bambu-lab-p1s-combo-(with-ams)-3d-printer).

And _oh my gosh_ the P1S was a game-changer. I had no idea modern 3D printers were so fast! The thing was at least 10x faster than my Ender 3's (though I've since learned the latest Ender 3's, Prusa MK4, and other flagship models are pretty near in speed, like an order of magnitude faster than the older generation printers I'm used to.

Instead of waiting 3-4 hours for a pusher to pop off the bed, it took less than an hour. Instead of 9 hours for one tray, I could have 4 printed on the same bed in 6 hours.

That was _huge_, and I went from crisis mode to feeling like I could actually have ten fully-functional Piz Dispensers by Friday!

{{< figure src="./bambu-labs-p1s-printing-piz-heads_0.jpeg" alt="Bambu Labs P1S Printing 6 Piz Dispenser Heads" width="700" height="auto" class="insert-image" >}}

The move from my Ender 3's to the P1S feels a lot like when my Dad had an HP DeskJet (the original one) printing a page every minute or so, to a LaserWriter NT, spitting out a page every 10 seconds or so.

It's not anywhere near the speed of printers _today_, but the [cycle time](https://www.lean.org/lexicon-terms/cycle-time/) for design iterations was reduced to the point I could do a few revisions per day, instead of one or maybe two.

I'm excited where this new printer leads—and at Open Sauce, I met with Josef Prusa, the folks behind Voron, and some of the Positron team. Not only that, about half the audience seemed to be deeper into 3D printing than I'll ever be, and I learned a _lot_ in a very short amount of time.

With my skills leveled up from "complete noob" to "mostly noob" in Fusion 360, I may be able to incorporate some nicer case designs into my homelab and Pi testing builds now!

## Integration Hell

Printing is only half the battle, though. After I had printed parts, I found out the 9mm gun magazine springs I _thought_ would work, were just too narrow. And they were round-wire springs, which means they are prone to bending outward, and eventually getting a bit caught up, causing the pusher mechanism to get stuck deep inside the dispenser, instead of pushing the stack of Pis up to the top.

{{< figure src="./piz-dispenser-springs-sprinco-ar-15.jpeg" alt="Sprinco AR-15 30-rd magazine springs next to 9mm springs and PEZ spring" width="700" height="auto" class="insert-image" >}}

Eventually I overnighted a couple sets of Sprinco AR-15 30-round magazine springs, and I regretted not ordering more... because I had to build a few dispensers with the 9mm springs, and _all_ of those were troublesome out on the floor at Open Sauce!

My wife and I cut all 480 individual Picos off the reel, and I loaded about 120 into the dispensers (I could fit more in the flat-spring AR-15-spring-equipped dispensers than the 9mm dispensers—if I overloaded the 9mm springs, they would kink out of shape!).

## Conclusion and Video

The whole process (and the process of giving out 480 Picos on the floor at Open Sauce) is documented in my video on the project:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/n5d0hzgA9BI" frameborder='0' allowfullscreen></iframe></div>
</div>

If you'd like to print a Piz dispenser of your own, I have the 3D models up on Printables: [PIZ Dispenser by geerlingguy](https://www.printables.com/model/915677-piz-dispenser).

And thanks to Raspberry Pi for sending a reel of Picos to give away at Open Sauce, thanks to William Osman and the whole Open Sauce team for making a great event for all who attended, and thanks to STL Denise 3D and others in the maker and open source communities who assisted me on this journey!

[^edible]: It's debatable whether PEZ are edible—my wife disagrees with me on whether one should eat one.
