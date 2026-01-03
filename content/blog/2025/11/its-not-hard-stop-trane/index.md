---
nid: 3509
title: "It's not that hard to stop a Trane"
slug: "its-not-hard-stop-trane"
date: 2025-11-04T22:55:37+00:00
drupal:
  nid: 3509
  path: /blog/2025/its-not-hard-stop-trane
  body_format: markdown
  redirects: []
tags: []
---

Six years ago, I replaced the old HVAC system that came with our house, a central forced air system installed in 1995[^oldinstall].

The new system is a Trane XR AC paired with an [S9V2 96% efficiency forced-air gas furnace](https://www.trane.com/residential/en/products/furnaces/premier-96/). And it ran great! Better efficiency, quieter, multiple fan speeds so I can circulate air and prevent stale air in some parts of the house... what's not to love?

Well, apparently the engineering:

{{< figure src="./trane-s9v2-furnace-inside.jpg" alt="Trane S9V2 Forced-air variable speed gas furnace" width="700" height="525" class="insert-image" >}}

And yes, before you comment, I know a heat pump would be wonderful. Maybe someday, but these systems are a substantial investment, and six years ago the heat pump market (not only the hardware, but the installers and HVAC pro support available in a given area) was not as good as it is today in the US.

But above is what the inside of this system looks like, with the front cover removed.

There's a gas heating element at the top, with the black bar providing a ton of natural gas into four burners. They burn fresh air that comes in from a PVC pipe on the top, which gets fresh air from outside. Then the combustion exhaust (after heat is removed in a heat exchanger) is forced out another PVC pipe (again, outside the house) through the 'draft inducer fan', the large circular black thing.

Well, two weeks ago, we woke up to a chilly house, and a furnace that wasn't heating (even though the thermostat was on and calling for heat). The fan was still running, so I knew at least _some_ part of the HVAC system was still operational, so as any good IT person does, I went downstairs and switched off power to the system, and switched it back on.

That successfully shut it down, and when it came back on, it powered up the thermostat... and nothing else (including the blower fan).

After getting a few space heaters secured for the next two nights (because these things always happen on a weekend, and emergency service rates are... a _lot_), I popped off the cover to investigate.

## The video

I recorded a quick video overview of the problem and my temporary fix, and posted it on my 2nd channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/cKtHvw8fPvA" frameborder='0' allowfullscreen></iframe></div>
</div>

## The problem

Because it's using outside air, and heating it, and because my furnace is in the basement (with no ability to lay the vent pipes sloped outside), any condensation in either of the two supply PVC pipes will wind up in the furnace.

And indeed, after six years, there's evidence the supply air pipe has let in some water, as there's rust on the burner, the gas solenoid, and even the draft inducer blower motor parts.

{{< figure src="./trane-furnace-top-rusty-pvc-intake.jpg" alt="Trane S9V2 gas heating element rusting from intake PVC condensate entrance" width="700" height="394" class="insert-image" >}}

There's apparently an in-line drain, part number [BAYCNDTRAP2A](https://elibrary.tranetechnologies.com/public/trane-history/Literature/Installation/18-CE06D1-1B-EN_07012020), that's supposed to be added on basement installs like mine, but I don't have one. So I've ordered one, and I guess I'll pop that on there myself?

But that's not actually what stopped my Trane this year. It's [hard to stop a Trane](https://www.youtube.com/watch?v=hRQa1JxNcrI), but apparently not _too_ hard—just a few drops of water will do:

{{< figure src="./water-damage-trane-s9v2-control-board.jpg" alt="Trane S9V2 water damage to main PCB" width="700" height="394" class="insert-image" >}}

The annoying thing is, this water droplet _wasn't_ from that condensation dripping down from the air intake. No, this water droplet (and I've since found many more) are leaking out of the draft inducer fan housing!

That housing deals with enough water there are two drains attached to it — one at the lowest point, and another at the junction between the PVC pipe and the housing.

And it has been leaking enough water that it completely killed one control board, and caused the replacement to reset itself over the weekend (thus leading to further investigation, and this blog post).

The PCB is only protected a little on the top (just a 1" overhang of plastic) and insulated from the metal surface it's mounted to by a plastic tray.

Ideally, since this compartment could get a LOT more water for any number of reasons, and since according to my bill, the board costs $630 alone, there'd be more protection over the top.

But as it is, most of the high power connectors are across the top of the board, meaning any water that _does_ drip down from above, will end up wicking its way along the wiring harnesses, or at least dripping more towards the board than away.

The HVAC tech who came out the second time had an ingenious (but temporary) solution: take my silicone soldering mat, and wedge it into the plastic cover, so it will drain the dripping water _away_ from the precious PCB. I fashioned up a little drainage receptacle below:

{{< figure src="./silicone-mat-drainage-trane-furnace-hvac.jpg" alt="Silicone mat draining water away from control PCB in Trane S9V2 furnace" width="400" height="auto" class="insert-image" >}}

It remains this way[^efficiency] currently, as I await another technician to come decide what to do about the draft inducer motor and housing... Hopefully a replacement.

But even then, if the replacement has the same flaw that my existing one did, in five or six years I guess we'll go through this whole cycle again.

It'd be nice if newer technology were even half as reliable as older, less-efficient technology. It seems like with laptops, furnaces, refrigerators, dishwashers, cars, and more, the answer is more often to discard and replace, rather than repair.

How much more efficient is it, really, if you have to throw out the whole thing three times in the same period an old unit would run with minimal maintenance?

[^oldinstall]: I believe it was 1995. It was in the 90s, at least.

[^efficiency]: Sadly, this modification means the unit is not currently achieving 96% efficiency, since the cover is off, allowing it to draw combustion air in from the basement, and not only from outside.
