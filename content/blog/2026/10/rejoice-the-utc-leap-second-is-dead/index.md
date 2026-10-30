---
date: '2026-10-30T09:00:00-05:00'
tags: ['leap second', 'utc', 'time', 'youtube', 'nist', 'bipm', 'cgpm', 'ut1', 'news']
title: 'Rejoice, leap seconds are dead!'
slug: 'rejoice-the-utc-leap-second-is-dead'
---
There will never be a leap second again. At least not for UTC.

{{< figure
  src="cgpm-resolution-5.jpg"
  alt="CGPM Resolution 5"
  width="700"
  height="auto"
  class="insert-image"
>}}

[At the CGPM](https://www.bipm.org/en/cgpm-2026/resolution-5), they decided the last leap second we'll ever see for UTC, or Coordinated Universal Time, happened back at the [end of 2016](https://kb.meinbergglobal.com/kb/time_sync/leap_seconds/leap_second_announcement_2016).

Of _course_ they made that decision while I was out on vacation, so I'm just getting this video up now:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/vFMU2m-TZ3s' frameborder='0' allowfullscreen></iframe></div>
</div>

But what's the CGPM, why does this matter, and why am I excited about it?

## CGPM and BIPM

The CGPM is the [General Conference on Weights and Measures](https://www.bipm.org/en/committees/cg/cgpm), and yes, 'GCWM' is not 'CGPM', because CGPM is an abbreviation for the _French_ title: _Conférence Générale des Poids et Mesures_.

And don't get me started on UTC, which stands for "Coordinated Universal Time". It's not CUT, and it's not even the French version, TUC, [it's a compromise](https://www.timeanddate.com/time/utc-abbreviation.html) so _neither_ language would win![^utc]

Anyway, the CGPM is a conference overseeing the BIPM, the [International Bureau of Weights and Measures](https://www.bipm.org/en/). The CGPM is where they talk about things like redefining measurement units.

This year, they passed Resolution 5, killing the leap second 8 years earlier than the 2035 deadline [they had set](https://www.bipm.org/en/cgpm-2022/resolution-4) in their 2022 meeting.

Starting on **May 20, 2027**, _UTC will never have another leap second added or taken away_.

UTC will be allowed to deviate from UT1, the Earth rotation time, for up to 1 hour. So we could have 'leap hours' someday, but the resolution doesn't say anything about them, and it'll take centuries to drift that far. That's a problem for future horologists.

## Negative leap second

But why now? Why couldn't they just kick the can down the road like we've been doing since 2016?

{{< figure
  src="earth-rotation-speeding-up.jpg"
  alt="Earth's rotation is speeding up"
  width="700"
  height="auto"
  class="insert-image"
>}}

The big problem is there was a 30% chance we'd need a _negative_ leap second between now and 2035, because the Earth's rotation is has been [_accelerating_](https://www.sciencefocus.com/planet-earth/earth-rotation-speed) lately. We've had 27 _positive_ leap seconds between 1972 and today, but we've never taken one _off_.

Imagine every computer program that deals with time having to work in a condition that's never been tested before. It'd likely be worse than [Y2K](https://en.wikipedia.org/wiki/Year_2000_problem)!

The resolution called this out specifically:

> "Industrial users and the synchronization needs of national critical infrastructures, for example transportation, energy distribution, telecommunication, and space projects require UTC to be continuous without any future adjustment."

(By the way, if you're a time-nut and into this stuff, watch the entire [CGPM Day 3 Livestream](https://www.youtube.com/watch?v=TptRsUua2WE), which the source of the slide at the top of this section. Riveting stuff!)

Technically these industries _can_ handle leap seconds, but the pain is not worth the benefit, especially since astronomers _already_ deal with time offsets for Earth's rotation, using UT1, which is a variable time offset from UTC.

We still have plenty of other time problems we'll have to deal with like [Y2K38](https://en.wikipedia.org/wiki/Year_2038_problem). So I think BIPM members were thinking, "We have a chance to fix _one_ of these problems, so let's at least do that!"

Thus, UTC will forever be locked 37 seconds ahead of TAI ([International Atomic Time](https://en.wikipedia.org/wiki/International_Atomic_Time)).

By the time it's a problem, we'll probably be working on a _galactic_ time standard, and UTC will be a quaint hobby for [time-nuts](http://www.leapsecond.com/time-nuts.htm), much like water and pendulum clocks.

## Why it's okay

But won't it cause problems for scientists and astronomers, if we let UTC drift from the Earth's actual rotation a few seconds? Not really.

At least not worse than things like timezones. Timezones and the politics with things like Daylight Saving Time are all kinds of crazy!

But we can deal with those time _offsets_ more easily. We already use them for time zones and astronomy.

It's much harder to deal with absolute time scales (like UTC) that add or remove seconds. Computers hate it when a billion nanoseconds suddenly vanish or appear while they're running.

Companies like Meta, AWS, and Google [spent tons of money](https://arstechnica.com/science/2022/08/record-short-days-could-speed-up-debate-on-leap-seconds/) building 'time smearing' features into their infrastructure to deal with _positive_ leap seconds, and they [still ran into problems](https://engineering.fb.com/2022/07/25/production-engineering/its-time-to-leave-the-leap-second-in-the-past/).

Even assuming technical perfection, there's risk involved in the rollout of a leap second. Since they're decided by committee, you can't automate when one is added, your system has to either constantly update a leapseconds file, or you have to have someone monitor the leap second announcements and update your software to adjust, assuming it's offline. Remember that not every piece of time-critical software is tied into Internet time systems!

And assuming every company monitors for leap seconds, they also have to build and test their own system to add or remove a second. It was hard even for giant corporations in 2016; I can't imagine the vibe-coded disasters that await us now.

A cool side effect is software can drop leap second handling now. That code was always a little flaky, and not all programs even acknolwedged leap seconds' _existence_. Some programs would just YOLO it, and that's a recipe for disaster.

## WWV/WWVB

There are downsides. WWV radio time has a special field in its data for leap second handling. They broadcast [DUT1](https://en.wikipedia.org/wiki/DUT1), which is the Earth Rotation-based time UT1 minus UTC, and their current signals assume it's always less than 1 second.

Astronomers and certain navigation systems use that time for their work, so once it's off by more than 0.9 seconds, that could create problems. They have probably 5 to 10 years to solve it, but it _is_ a bit of a pickle.

## Why does Earth's rotation change?

But one question you might have is why is Earth's rotation speeding up? I know I did. Apparently there are changes in the Earth's core which are hard for us to see, but easy to measure. And those are speeding up the rotation right now.

I'm not an expert on geodesy, but over the long term, the Earth should go back to slowing down.

## Other developments

There are some other reasons I think this is good news. Leap seconds were always an annoyance for timekeepers.

{{< figure
  src="nist-f4-clock.jpg"
  alt="NIST F4 clock bringup from NIST public domain video"
  width="700"
  height="auto"
  class="insert-image"
>}}

They'd much rather spend time on bigger changes, like redefining the second. Right now it's based on the [hyperfine transition frequency of cesium-133](https://en.wikipedia.org/wiki/Caesium_standard), as it has been for decades. But newer clocks are orders of magnitude more precise. Seconds will probably be shift to optical, or maybe even _nuclear_ clocks (pictured above: NIST's F4, still a cesium fountain clock, but cool nonetheless!).

But changing the second will change _other_ definitions governed by the BIPM, like how long a meter is, because [that's based on time](https://en.wikipedia.org/wiki/Metre#cite_note-SIBrochure9thEd-3), too!

On top of that, if we _do_ start exploring space more rapidly, UTC might lose relevance. We've already seen Lunar clocks running about [56µs faster](https://physics.stackexchange.com/questions/809010/how-long-is-a-second-on-the-moon) per day than clocks on Earth. If we have a mission to Mars, we'll have to figure out a better interplanetary time scale.

## Conclusion

But in the end, especially as a programmer who's dealt with time bugs, I'm happy to see one annoying feature of UTC get removed.

[^utc]: It also conveniently aligns with 'Universal Time', which is used for UT1 (Earth's rotational time) and UT0 (which is no longer used).
