---
nid: 3279
title: "TV for one million: Exploring KSDK's broadcast tower"
slug: "tv-one-million-exploring-ksdks-broadcast-tower"
date: 2023-03-23T03:01:27+00:00
drupal:
  nid: 3279
  path: /blog/2023/tv-one-million-exploring-ksdks-broadcast-tower
  body_format: markdown
  redirects: []
tags:
  - broadcast
  - geerling engineering
  - ksdk
  - saint louis
  - television
  - tower
  - tv
  - video
  - youtube
---

KSDK-TV broadcasts to well over 1 million households in the St. Louis metro area. And my Dad and I went to their broadcast tower last month to explore how the digital TV signal is delivered through the air to so many people.

{{< figure src="./drone-three-towers-ksdk-top-shrewsbury.jpeg" alt="Three towers KSDK-TV in Shrewsbury St. Louis MO" width="700" height="370" class="insert-image" >}}

On our tour, we explored over 75 years of television broadcast history, seeing how things transitioned from thousands of volts down to hundreds, and from analog audio and video to all-digital.

And we even found strange artifacts of the past, like this random microwave dish that received a signal through the _roof of the broadcast building_ for a time:

{{< figure src="./microwave-dish-in-roof-skylight.jpg" alt="Microwave dish in roof of KSDK Transmitter building" width="700" height="394" class="insert-image" >}}

No longer in use, it's one of the reminders that there's only one constant in broadcasting: change.

## Touring the Tower Site

Indeed, over in the main comms room—which has enough equipment to run independent of the downtown studios, should the need arise—we see even more evidence of change:

{{< figure src="./Sony-Wega-Trinitron-HD-1080-CRT-Front.jpeg" alt="Sony 1080p CRT Trinitron TV" width="700" height="394" class="insert-image" >}}

This TV was the pinnacle of the CRT era, weighing so much it took at least two capable bodies just to lift it to its final resting place. As HD replaced analog, so Plasma and LCD TVs replaced 'tube' TVs and their scanning electron guns.

But looking a few feet away, there's an array of software-controlled remote SDRs used to send back feeds of local police and emergency comms:

{{< figure src="./Uniden-Radio-Receivers-for-Public-ID-Scanning-for-Newsroom-KSDK.jpeg" alt="Uniden radio receivers for scanning for the newsroom" width="700" height="394" class="insert-image" >}}

The newsroom uses those feeds when gathering breaking news, since the tower site is located optimally for coverage of the entire metro area.

The tower itself isn't decorated quite so densely as the [Supertower we visited last year](/blog/2022/1-million-watts-rf-how-fm-supertower-works), but it still hosts two backup FM transmitters, an FM repeater, a 2nd low-power TV station, and a variety of other smaller clients.

Indeed, the radio network my Dad works for is the reason we had so much knowledge of the site (besides the great assistance of KSDK engineers)—he recently had these antennas installed around 750' in the air for a 250W FM repeater he operates:

{{< figure src="./tower-climber-ksdk-fm-antenna-install-stl-clayton-skyline-drone.jpeg" alt="KSDK FM Antenna install tower climber" width="700" height="370" class="insert-image" >}}

But the star of the show is the 50 kW signal that's passed through a variety of high-power filters before being delivered up to the top of the tower. First the digital signal is fed into the transmitter through redundant microwave and fiber Internet connections:

{{< figure src="./KSDK-Transmitter-Exciters-Rear.jpeg" alt="Transmitter redundant microwave fiber connections" width="700" height="394" class="insert-image" >}}

Then a multitude of power amplifiers generates the massive RF signal—there are 'twin' transmitters that work together to generate the full signal strength, and this is just one of the two:

{{< figure src="./Transmitter-Power-Amplifiers-KSDK.jpeg" alt="Power amplifiers in broadcast transmitter" width="700" height="394" class="insert-image" >}}

The RF signal is brought out through four coaxial cables and combined into two in the space behind:

{{< figure src="./Dad-showing-KSDK-Transmitter-Feed-Lines.jpeg" alt="Dad showing the transmitter feed lines and coax combiners" width="700" height="394" class="insert-image" >}}

It travels across the room into a set of band-pass filters—though these are quite a bit larger than you might be used to!

{{< figure src="./Transmitter-Feed-Line-Band-Pass-Filter.jpeg" alt="Band pass filters for KSDK-TV tower RF signal" width="700" height="394" class="insert-image" >}}

The signal then routes through a giant custom-built waveguide that combines the output into one 9" coax feed line that goes out to the tower:

{{< figure src="./KSDK-Transmitter-Room-Waveguide-Above.jpeg" alt="Waveguide and coax output to tower at KSDK-TV" width="700" height="394" class="insert-image" >}}

And if you think this setup is massive, consider this: the digital transmitter, along with _all_ the redundant signal reception equipment for microwave and fiber signals from the studio, takes up much less than _half_ the space of KSDK's original transmitter installation. There's a huge gap on the left side of this room where the analog main transmitter used to sit:

{{< figure src="./Transmitter-Room-Half-Empty-KSDK.jpeg" alt="Gap where analog TV transmitter used to sit" width="700" height="394" class="insert-image" >}}

But even using half the floor space, things get _hot_. And that necessitates impeccably-routed redundant water cooling systems. Even the _dummy load_, which is used when testing a transmitter with its signal not routed up to the tower, is water cooled, as it gets extremely hot. There are redundant cooling systems for both transmitters, the dummy load, and other parts of the system, _in addition to_ a few large chillers for all the rest of the systems on site.

{{< figure src="./Dad-showing-Water-Cooling-Pumps-at-KSDK.jpeg" alt="Redundant water pumps for water cooling TV tower transmitters" width="700" height="394" class="insert-image" >}}

But all of this would be for nothing if the power goes out—so as with everything else, there is redundancy in the power systems. This beefy Caterpillar generator kicks in after just seconds of power loss, and supplies power to the entire facility:

{{< figure src="./Caterpillar-Generator-Engine-Interior-KSDK.jpeg" alt="Caterpillar generator" width="700" height="394" class="insert-image" >}}

I could easily park my sedan inside the generator's enclosure, it's that big!

As with the FM tower, nitrogen is used to pressurize the coaxial feed line, to keep out moisture:

{{< figure src="./Nitrogen-Controls-for-KSDK-Tower.jpeg" alt="Nitrogen feed line for KSDK-TV transmitter feed line" width="700" height="394" class="insert-image" >}}

RF loves to arc at such high power levels. It will happily (and nearly instantaneously) burn through 9" copper coaxial cabling if given the opportunity to do so. Therefore it's important to have a reliable nitrogen system onsite, and monitoring in place should it fail.

Walking around a facility like this, you see plenty of little interfaces that look like they came straight out of a Bond film:

{{< figure src="./Remote-Satellite-Dish-Controls.jpeg" alt="RF system control for satellite dish" width="700" height="394" class="insert-image" >}}

...but they're just artifacts of a bygone era, when interfaces were built to be logical, and digestible by humans, rather than remote controlled software with indiscernible interfaces built on display technology like Flash that's obsolete within decades (at best).

## In-Depth Tour Video

You can view our entire video of the tour (with more detail) on the Geerling Engineering YouTube channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/W_U9pFfXjYA" frameborder="0" allowfullscreen=""></iframe></div>
</div>
