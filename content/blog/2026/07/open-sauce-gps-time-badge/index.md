---
date: '2026-07-22T09:00:00-05:00'
tags: ['time', 'open sauce', 'gps', 'badge', 'electronics', 'videos', 'youtube']
title: 'Open Sauce and GPS time were my summer AI Antiseptics'
slug: 'open-sauce-gps-time-badge'
---
In the midst of our AI slop revolution, traveling to the West coast for [Open Sauce](https://www.opensauce.com) this past weekend was the perfect antiseptic for rising costs, summer heat, and online divisiveness.

It's ironic, then, that I used Claude to vibe code my [Tufty GPS Time Badge](https://github.com/geerlingguy/tufty-gps-time).

{{< figure
  src="./tufty-gps-time-badge.jpeg"
  alt="Pimoroni's Tufty 2350 running my GPS Time App with a GPS module"
  width="700"
  height="auto"
  class="insert-image"
>}}

Partly due to time constraints, and partly because I wanted to see if I could complete a personal project end-to-end, without editing a line of code, I throw my [requirements](https://github.com/geerlingguy/tufty-gps-time/blob/master/Requirements.md) at Claude and ultimately came up with [this 2141-line MicroPython app](https://github.com/geerlingguy/tufty-gps-time/blob/master/gps_time/__init__.py) for Pimoroni's Badgeware ecosystem.

## GPS Time Badge

Using Pimoroni's Tufty 2350 and Adafruit's PA1010D MiniGPS addon module, I built a Badgeware App called '[GPS Time](https://github.com/geerlingguy/tufty-gps-time)' which disciplined the badge's internal RTC using GPS's time data, which can be accurate to the nanosecond.

I say _can be_ because I wasn't able to find a GPIO pin available on the Tufty 2350 for PPS input[^tuftygpio]. Therefore I was reliant on MicroPython's rough timing and I2C interrupts to displine the internal clock. This is not ideal, and in some conditions, resulted in the clock being 100-200ms off. Most often, it was only a few milliseconds, but the variation is likely due to BadgeOS's highly abstracted architecture.

It's easy to program (especially for quick UIs), but not built to be a robust real-time OS!

{{< figure
  src="./tufty-gps-time-badge-sky-view-satellites.jpeg"
  alt="GPS Satellite Sky View pane for GPS Time App on my badge"
  width="700"
  height="auto"
  class="insert-image"
>}}

The point of the Time Badge was "to have the best time" at Open Sauce, though—what's a few microseconds between friends?

I could get PPS out to compare my _GPS_ to other clocks—and I did that (more in the video embedded later in this post). But I also wanted to do a little experimentation. Having direct access to a wearable GPS module's data, I logged GPS satellite and fix quality throughout the day, as I walked around the venue.

With a few thousand datapoints, I whipped up this visualization of all the data points using Claude:

{{< figure
  src="./gps-best-time-track-points-street.png"
  link="/blog/2026/07/open-sauce-gps-time-badge/gps-log-map.html"
  alt="GPS log data from walking around the Open Sauce venue for a day"
  width="700"
  height="auto"
  class="insert-image"
>}}

(You can click on the above image to go to an [interactive web page](/blog/2026/07/open-sauce-gps-time-badge/gps-log-map.html).)

One-off coding of scripts and side projects is handy, but the main use case I've had for AI tools is data visualization. I was always terrible at turning datasets into useful interactice graphs (I struggled mightily back when I was running [Server Check.in](https://servercheck.in))... but this was pretty useful _and_ usable. I did have to redirect Claude a few times, to do the right thing (AI is pretty dumb, still).

One thing I quickly learned: besides the hall where the Main Stage was located, all the buildings had either wood or otherwise RF-transparent roofs. I was getting pretty good 6-8 satellite fixes wherever I went!

There were a few sections where I saw more interference (that's where most of the red dots come from), but on the whole, it was easy to have a good time at Open Sauce.

## Open Sauce

But that's just _GPS_ time. I also had a great time interacting with everyone. And as I mentioned in the introduction to this blog post, it was incredibly refreshing to have 8+ hours with no screens present, no AI, only direct human interaction[^retreat]. 

I met more than a few of the HN crowd at Open Sauce this year[^hncrowd]. A venn diagram of Hacker News readers and those who would enjoy the majority of the Open Sauce exhibits is practically a circle.

{{< figure
  src="./astronaut-matthew-dominick-737-flight-simulator.jpg"
  alt="NASA astronaut Matthew Dominick landing a Boeing 737 in a 3D printed flight simulator"
  width="700"
  height="auto"
  class="insert-image"
>}}

There were numerous exhibits of note:

  - A 3D printed orbit-accurate [replica of our solar system](https://www.youtube.com/watch?v=r-pmrUJGm6w)—complete with each planet's moons
  - Multiple Raspberry-Pi controlled pianos
  - Multiple driving couches
  - A functional [3D printed 737 cockpit](https://www.youtube.com/watch?v=2_hVGkwJtps) (in which I witnessed NASA astronaut Matthew Dominick buzz the entire bay area while egged on by Scott Manley and a large crowd of bystanders)
  - Nifty [Apollo-era space hardware](https://www.curiousmarc.com) CuriousMarc, Ken Sheriff, and TubeTime bring for on-the-floor restoration and display
  - Roving freely on the floor: a Mac Classic on tracks, a Prusa Core One 3D printer on hexapod legs (actively printing), a walking coffee table, multiple star wars droids](https://www.bayareadroidbuilders.com), even [TROGDOR!](https://www.instagram.com/p/Da8e88YuoLt/)
  - [Taser Chess](https://www.youtube.com/@EverythingIsHacked/videos) (which I was lucky enough to experience)
  - A drone that converts into a car (and vice-versa)
  - A moon rock from Apollo 15, and part of Artemis' heat shield, at a NASA Ames Research Center exhibit

There's far too much to cover in this blog post—I tried to do so [last year](/blog/2025/open-sauce-confoundingly-brilliant-bay-area-event/), only to realize I still missed about 30% of the booths!

So here's a video showing some of my highlights, especially relating to my personal theme this year, _time_:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/ziPIbxoFc_g' frameborder='0' allowfullscreen></iframe></div>
</div>

Some people come to see their favorite content creators, but the main draw for me is talking to exhibitors and attendees. Most of them give me a severe case of imposter syndrome.

[^tuftygpio]: Pimoroni made a special edition [GitHub Universe Edition](https://github.com/badger/home/blob/main/README.md) of the Tufty, which exposed four GPIO pins externally. Unfortunately those don't seem to be broken out anywhere on the final production Tufty 2350 :(

[^retreat]: I used to go on at least one 2-3 day silent retreat every year. I should probably find a way to do that again. While being away from screens was great, being away from screens and _alone with hours of quiet time_ would be nice too. Having five kids tends to null out any available free time, though :D

[^hncrowd]: Let's be honest, since Google traffic dwindles to almost nothing (AI summaries often throw my blog link in a footnote nowadays), Hacker News visitors are probably 70-80% of this blog's human readership, with the other 20% being those who read via RSS feed.
