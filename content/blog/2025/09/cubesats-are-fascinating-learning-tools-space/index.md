---
nid: 3492
title: "CubeSats are fascinating learning tools for space"
slug: "cubesats-are-fascinating-learning-tools-space"
date: 2025-09-12T14:01:41+00:00
drupal:
  nid: 3492
  path: /blog/2025/cubesats-are-fascinating-learning-tools-space
  body_format: markdown
  redirects:
    - /blog/2025/cubesats-are-fascinating-introduction-space-hardware
aliases:
  - /blog/2025/cubesats-are-fascinating-introduction-space-hardware
tags:
  - cubesat
  - microcontroller
  - raspberry pi
  - satellite
  - space
  - video
  - youtube
---

{{< figure src="./four-cubesats-together.jpeg" alt="Cubesats together" width="700" height="394" class="insert-image" >}}

These are CubeSats. Satellites that are going to space—or at least, the ones I have here are _prototypes_. But these have one thing in common: they're all powered by either a Raspberry Pi, or a microcontroller.

There are already Pis in space, like on Mark Rober's [SatGus](https://space.crunchlabs.com), on [GASPACS](https://www.raspberrypi.com/news/worlds-first-raspberry-pi-powered-cubesat-celebrates-record-making-orbit/), and the [Astro Pis on the Space station](https://astro-pi.org). Another Pi is going up _this weekend_, which is why I'm posting _this_ today. I'll get to that one, but I wanted to spend some time talking about two things that fascinate me: Raspberry Pis, and putting them space!

In this post, I'll cover:

  - What is a CubeSat
  - Who builds and launches CubeSats
  - How _you_ can build your own CubeSat

Then for a bonus, in today's video, I interviewed two people helping students launch SilverSat into space (this weekend!), and a YouTuber who I've learned a lot from about track satellites (including CubeSats) from your own backyard!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/qvN3sE2Nv4U" frameborder='0' allowfullscreen></iframe></div>
</div>

The rest of this post contains a lightly-edited transcript of the video above.

So let's dive in.

## What's a CubeSat?

What's a CubeSat? Well, it's in the name—it's a satellite that's a cube!

But they don't have to be a cube, these smallest ones are '1U', or 10 x 10 x 10 centimeters. You can also find 2U CubeSats, like the taller Build a CubeSat, which is _20_ centimeters tall. (Well, technically the current prototype is 1.5U).

[SatGus](https://isstracker.pl/en/satellites/62713), Mark Rober's satellite taking space selfies, is a whopping [12U](https://www.youtube.com/watch?v=6KcV1C1Ui5s)! They needed all that extra space to fit a phone, a mechanism to _deploy_ the phone, a camera to take the selfie, a Raspberry Pi to control the phone, and redundant systems for _everything_. They've already taken _thousands_ of selfies, and SatGus has me beat. My best Pi might get to [3.4 Gigahertz](https://www.youtube.com/watch?v=OXXKi-J0gs4), but the Pi on SatGus is whizzing through space at almost [_17,000 miles per hour_](https://www.pulsesat.com/satellites/s/302a5e31-68b8-422a-86fd-cfe32474ef6e/). That's _7,570 meters per second_ for everyone else in the world.

But back to CubeSats. Having standards means you can build off existing work for the hard things, like a space-rated Aluminum frame, or the complex EPS, or Electrical Power System board.

Then you can add in custom parts, like a Pi to run experiments, a communications board with antennas and radios, cameras, sensors, and more!

{{< figure src="./cubesat-build-a-cubesat-antennas.jpeg" alt="Build a CubeSat Antennas" width="700" height="394" class="insert-image" >}}

And _these_ cubesats have normal screw-on antennas, but the way these things are deployed, you only get 10x10x10 centimeters—you can't have an antenna poking out the top. So they use cool things like [flexible tape antennas](https://link.springer.com/chapter/10.1007/978-981-19-7474-8_15) that pop out once your CubeSat deploys.

What else makes CubeSats cool?

Well, how about price? In the old days, you had to have like $10 million to build a satellite, and $60+ million to launch it into space.

Today, you can build a space-ready CubeSat using a few _thousand_ dollars of parts. Then you can launch it on a rideshare for... well, [$85 grand](https://nanoracks.com/wp-content/uploads/Cubesat-Services.pdf). Which is a _lot_, but it's not _$60 million-a-lot_.

So most of us won't be launching one of these things into space, unless maybe you can get a grant. But that doesn't mean they're not useful to us.

## Who builds CubeSats?

Like with many projects, I love these things for the challenge, the way they break some of my assumptions, like working with Raspberry Pis.

If you're building a device that's less than 2 kilograms, has 1.8W of maximum continuous power draw, and needs to be operated remotely—even for just a month—you're immediately going to change your assumptions about how you build things.

I would hack Home Assistant onto a mini PC to monitor some sensors if I was feeling lazy—but that Mini PC would use an order of magnitude too much power for a CubeSat (much less the internal volume it would occupy).

On CubeSats, every millimeter, and every milliAmp has to be accounted for.

So to me, CubeSats are like Swiss watches of modern electronics. How many sensors can you fit in one? How much throughput can you get on a tiny radio with a small antenna? Can you get enough power out of tiny solar cells to keep the main flight computer working? How do you control thermals without air? How do you design it so it can recover from a complete power loss?

Every step of the way there are challenges; and that's before we even launch one! Someone who I think illustrates this best is Manuel, with his [Build a CubeSat](https://codeberg.org/buildacubesat-project) project. He's working on this Cubesat:

{{< figure src="./cubesat-build-a-cubesat.jpeg" alt="Build a CubeSat" width="700" height="394" class="insert-image" >}}

He did a weather balloon launch this year, and he's [documenting everything on YouTube](https://www.youtube.com/@buildacubesat).

His first launch had many small problems. But also great learning, especially around redundancy and how to get the thing off the _launch_ stand without problems.

And you're not only dealing with hardware, but also with _software_. And software that, at its core, _has_ to be remotely accessed. And not only remote, but also _wireless_, meaning anyone _else_ on earth within range can access it too.

So how do you keep it secure? That's something Tim from [Ethos Labs](https://ethoslabs.space) is also dealing with with _this_, his T.E.M.P.E.S.T. CubeSat:

{{< figure src="./cubesat-tempest-with-ground-station.jpeg" alt="CubeSat TEMPEST" width="700" height="394" class="insert-image" >}}

This thing is actually made to be _not_ secure. It has intentional vulnerabilities, and he uses those to teach people different ways to make _their_ CubeSats _more_ secure.

You have complex hardware, running in limited space, with limited power and communications, and you want cram in as much functionality as possible.

Do you see where I'm going with this? That kind of problem is perfect for the microcontrollers and low-power SBCs that I love testing and playing with every day.

Except instead of me worrying about something consuming 10 watts, these guys are looking at a power budget of _one_ watt. Or less!

These problems are _hard_. And not everyone has the patience for a completely custom project like Build a CubeSat, so there are also some small companies building _kits_ to help you learn all these lessons with a little less stress.

Like what hardware do you need for a 100% self-contained CubeSat? And how do you get it certified for flight on a SpaceX rocket?

## Your own CubeSat

Well, I'll quickly cover two products that are meant for like STEM classroom education, one from the lower end, and one that's based on a CubeSat that just flew this summer.

{{< figure src="./cubesat-mysat.jpeg" alt="MySat CubeSat" width="700" height="394" class="insert-image" >}}

The first one is the [MySat Kit](https://www.mysatkit.com), that you can buy from MySat in Ukraine. It comes with a board powered by an ESP32 with a camera, light sensors, an LED, gyroscope, accelerometer, barometer, clock, and a few other boards. And these are all off-the-shelf components you can buy replacements for or use 'em with other hardware, like a Raspberry Pi.

The way it's put together won't hold up on a rocket launch, but it's not meant for that. It's meant to show you how it's built, how you can communicate with it, and that sort of thing.

It took like an hour to build, and once I put it together I tried flashing the flight control firmware with my Mac... but I ran into some issues with Arduino IDE, and that's a _me_ problem and not so much a MySat problem. Plus the team behind it has a whole war going on that they've been dealing with, so I'll be patient and try getting it going later.

The MySat goes from like $130 for a basic kit where you 3D print your own frame, or up to $300 for a full kit including deployable solar panels.

On the higher end, there's [RASCube](https://www.robinson-aerospace.com/cubesat), and Edward Robinson, the 21 year old founder of Robinson Space, sent it over after he saw me posting about CubeSats online.

The RASCube comes from Australia, and Edward's mission is to teach students about space through hands-on building.

{{< figure src="./rascube-lb-rbf-tag.jpeg" alt="RASCube LB CubeSat" width="700" height="394" class="insert-image" >}}

I just built this LS version of the cube last week; it's the little brother to their V2 design, which _flew in space_ on a Falcon 9 rocket earlier this year.

Like MySat, you build the kit with an EPS board for power, a computer board with all the controls, and a radio board that ties in GPS and radio comms.

The RASCubes are a bit more expensive, coming in at around $430 each for the LB, and $600 each for the full aluminum V2s. But the price tag on that also covers full lesson plans and resources for teachers.

I love these things—all the people I've talked to on this journey are motivated by the same thing: learning about space, electronics, and integrating hardware in a new way, and sharing what they learn with others, especially students.

## CubeSat T.E.M.P.E.S.T. and Build a CubeSat

Like take Build a Cubesat. For that project, [_everything_ is open source hardware](https://codeberg.org/buildacubesat-project/bac-hardware), and every part of the journey is being documented on YouTube.

One thing I learned from the [first flight test](https://www.youtube.com/watch?v=bDQ_N9Gvzqs) was how weird it is to have your Pi go from like overheating on the ground, to getting really cold as it goes higher, but then overheating again in the upper atmosphere because there's not enough air to dissipate heat!

You start to realize some of the crazy physical conditions you'll deal with on orbit.

{{< figure src="./cubesat-tempest-ground-station-pico.jpeg" alt="CubeSat TEMPEST Ground Station Raspberry Pi Pico" width="700" height="394" class="insert-image" >}}

Back down to earth, though, for CubeSat Tempest: the whole reason this exists is to help people learn why security is important, even for a tiny CubeSat. More importantly, [Tim Fowler's course](https://www.antisyphontraining.com/product/foundations-in-space-cybersecurity-hardware-edition-with-tim-fowler/) teaches people _how_ to secure things like uplinks (see: the ground station pictured above) and flight control systems.

There are so many people like Tim, who work in their free time to try to teach about space, or engineering, or just small slices of things like security, using these tactile little cubes you can build and put next to your laptop on a desk.

It's crazy to think we're to a point where _students_ can build these things, write flight control software, and even _launch 'em into space_!

And that brings me to [SilverSat](https://silversat.org).

## SilverSat

There's another CubeSat with a Raspberry Pi onboard, and it's launching NET _Sunday_, at 6:11 p.m. Eastern time, aboard a Falcon 9 rocket. What does NET mean? Well, as I found out when I visited Florida this summer, that means "No Earlier Than", and in spaceflight, many things delay launches.

The students who built SilverSat are no strangers to delays—they were originally supposed to see their CubeSat launch earlier this year, but the cargo module they were on got [damaged during transport](https://arstechnica.com/space/2025/03/nasa-sidelines-cygnus-spacecraft-after-damage-in-transit-to-launch-site/), and that delayed them for _months_.

I got to talk to two of the adults guiding the students on their first space launch, and I discussed the history of the project (it started up in _2017_), how they are supported by NASA's [CubeSat Launch Initiative](https://www.nasa.gov/cubesat-launch-initiative-introduction/), the importance of amateur radio for CubeSats, and why they chose a Raspberry Pi Zero for their onboard computer.

{{< figure src="./raspberry-pi-zero-2w-rbf-tag.jpeg" alt="Raspberry Pi with CubeSats" width="700" height="394" class="insert-image" >}}

That interview is tucked away in the last half of the video at the top of this post.

## Tracking Satellites from your backyard

Also in that video, I spoke to Gabe from [saveitforparts](https://www.youtube.com/@saveitforparts), and he mentioned it's not that difficult to listen in on satellites on orbit—including amateur CubeSats!

SilverSat will be broadcasting [SSDV](https://github.com/silver-sat/systems/wiki/SSDV) (Slow-Scan Digital Video) at set times, and the [schedule for that](https://silversat.org/mission-status/) should be posted on their website.

Check out the video embedded in this post (near the top), or Gabe's own channel for ideas for tracking satellites. It can be done with under $100 of equipment (usually just an SDR and a cheap antenna).

## Infectious Enthusiasm for Learning (and Teaching)

I feel like a broken record, but one thing I love, talking to _anyone_ in the CubeSat community is this sense of infectious enthusiasm. And I was going to cut this video out for time, but watching it back, I realized other people would probably enjoy Tim showing off some neat CubeSats in his personal collection as much as I did. So I put up some bonus content on my second channel, Level 2 Jeff; you can watch another 8 minutes of CubeSat hardware below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/woO0w92YuC0" frameborder='0' allowfullscreen></iframe></div>
</div>

Thank you to _everyone_ who taught me about CubeSats for this video and blog post.
