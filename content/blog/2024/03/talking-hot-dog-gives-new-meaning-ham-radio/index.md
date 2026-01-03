---
nid: 3361
title: "Talking Hot Dog gives new meaning to 'Ham radio'"
slug: "talking-hot-dog-gives-new-meaning-ham-radio"
date: 2024-03-28T02:50:45+00:00
drupal:
  nid: 3361
  path: /blog/2024/talking-hot-dog-gives-new-meaning-ham-radio
  body_format: markdown
  redirects: []
tags:
  - am
  - geerling engineering
  - hot dog
  - radio
  - rf
  - safety
  - tower
  - video
  - youtube
---

...except it was a beef frank. Make your _wurst_ jokes in the comments.

{{< figure src="./hot-dog-rf-burns-geerling-engineering.jpg" alt="Hot Dog exhibiting severe RF burns" width="700" height="auto" class="insert-image" >}}

What you see above is the remains of a hot dog after it has been applied to an AM radio tower operating in its daytime pattern, at around 6 kW.

A couple months ago, soon after we posted our [If I touch this tower, I die](https://www.youtube.com/watch?v=Aax-ehkRTnQ) video, a few commenters mentioned you likely wouldn't _die_ after touching a high-power AM tower—rather, you'd have serious RF burns.

I was trying to figure out a way to _somewhat_ safely test the scenario: what would happen if someone walked up and touched the tower, while standing on the ground?

<blockquote><p>If reading's not your thing, check out the short video we posted on Geerling Engineering:</p>
<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/GgDxXDV4_hc" frameborder='0' allowfullscreen></iframe></div>
</div>
</blockquote>

No test scenario can be perfect—and with high-power RF, 100% safe... but after discussing it with my Dad a bit, we determined a hot dog could be a decent proxy for a human finger, and holding it far away on a wooden rod would provide enough safety margin, assuming we accounted for [RF exposure limits](https://www.fcc.gov/general/radio-frequency-safety-0) at the site.

{{< figure src="./test-hot-dog-apparatus-rf-exposure-safety-jeff-geerling.jpg" alt="Test hot dog apparatus for RF Safety Exposure" width="700" height="auto" class="insert-image" >}}

> **IMPORTANT**: Do not attempt to replicate our experiment. It is meant to demonstrate the dangers of RF, and there are a number of radio engineers, landscaping professionals, and other personnel who have written RF safety rules with their blood (or, in most cases, a permanent and painful RF burn that goes through the inside of their body). Don't touch radio towers—AM or otherwise.

I used a 2m wooden broom pole as an insulator, and wire-tied 12-2 romex to the end, leaving about 1m of wire hanging off the bottom. I exposed about 5cm of wire at the end, and on the hot dog attachment point, I bent the wire into a three-pronged 'hot dog fork'. The other end, I left the three wires flat, so they would easily clamp to a set of jumper cables, which would then be attached to the tower's [extensive grounding system](https://www.radioworld.com/industry/am-ground-systems).

{{< figure src="./hot-dog-rf-safety-apparatus-grounded.jpg" alt="Hot Dog RF Safety demonstration with grounding straps attached" width="700" height="auto" class="insert-image" >}}

The hot dog is attached directly to earth ground to demonstrate what would happen if a human were to approach the tower and touch it—even with a thin insulating layer of rubber in shoes, your body offers a pretty effective path from the mast to the antenna's ground plane—which extends pretty far out via radials under the base of the tower.

The effect, when touching the hot dog to the tower, is catastrophic:

{{< figure src="./hot-dog-tower-arc-1.jpg" alt="Hot dog tower RF arcing - smoking" width="700" height="auto" class="insert-image" >}}

{{< figure src="./hot-dog-tower-arc-2.jpg" alt="Hot dog tower RF arcing - flame" width="700" height="auto" class="insert-image" >}}

You really should [watch the video](https://www.youtube.com/watch?v=GgDxXDV4_hc) for the full effect, though. Pictures can't convey what happens.

I predicted the hot dog would either explode, or do pretty much nothing. My Dad imagined there would be some arcing.

Well, he was right—the hot dog wound up being a _very effective loudspeaker_, transmitting the audible sound with pretty high fidelity, at a volume around that of a yelling human, maybe 80-100 dBa. (Next time we attempt such an experiment, we may bring a dB meter and spectrum analyzer to judge the sound reproduction capabilities of different meats[^meats]).

My Dad also tested whether one could 'cook' a hot dog with the 1460 kHz AM radio signal, from a distance of approximately 1.2cm:

{{< figure src="./rf-cooking-hot-dog-tower-am.jpg" alt="RF cooking a hot dog on an AM tower" width="700" height="auto" class="insert-image" >}}

This experiment was a failure: the hot dog was not even warm to the touch, after holding it thus for around 30 seconds. (Any longer and we were getting near the employee safe exposure limits for this broadcast tower in its daytime pattern, approximately 6 kW).

Besides a little chatter of the energy radiating the giant copper inductors in the 'doghouse'—the small Antenna Tuning Unit (ATU) at the base of the tower—if you listen intently towards the end of the video, even when the hot dog is _not_ grounded, there is a little bit of noise as it contacts the tower:

{{< figure src="./hot-dog-ungrounded-touching-tower.jpg" alt="Ungrounded hot dog touching AM tower" width="700" height="auto" class="insert-image" >}}

Bottom line: even if you jump onto an AM tower, or you use an insulated ladder to climb onto the tower, you aren't 100% safe.

Some engineers and tower climbers still use those methods when replacing tower lights or performing other maintenance. They might even turn the transmitter power down—but after our testing, even on this 6 kW tower, I don't think we'd recommend that.

I am not a radio engineer. I know just enough to kill myself. Fortunately, I have other experts to rely on, and so does my Dad. Those experts all recommend _not_ messing with live towers.

If you do, the sound of _Oh Oh Oh, O'Reilly!_ blaring out of the end of your finger might sear itself into your brain the rest of your life.

{{< figure src="./hot-dog-rf-burn-vaporized.jpg" alt="Hot Dog RF burns vaporized" width="700" height="auto" class="insert-image" >}}

I would be remiss if I didn't acknowledge the original inspiration for this experiment, the infamous [am radio tower power](https://www.youtube.com/watch?v=uo9nGzIzSPw) video, posted about 8 years ago.

[^meats]: This experiment's test subjects were Oscar Meyer Classic Uncured Beef Franks.
