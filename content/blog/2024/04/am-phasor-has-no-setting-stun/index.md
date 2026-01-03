---
nid: 3367
title: "AM phasor has no setting for 'stun'"
slug: "am-phasor-has-no-setting-stun"
date: 2024-04-17T14:01:59+00:00
drupal:
  nid: 3367
  path: /blog/2024/am-phasor-has-no-setting-stun
  body_format: markdown
  redirects:
    - /blog/2024/phasor-has-no-setting-stun
aliases:
  - /blog/2024/phasor-has-no-setting-stun
tags:
  - am
  - geerling engineering
  - phasor
  - radio
  - rf
  - saint louis
  - video
  - wsdz
  - youtube
---

Today on [Geerling Engineering](https://www.youtube.com/c/GeerlingEngineering), my Dad and I toured the tower site for WSDZ-AM, located in Belleville, IL. It's a 20kW AM radio station broadcasting with an array of _eight_ individual towers:

{{< figure src="./wsdz-tower-site-8-towers-drone-shot.jpeg" alt="WSDZ 8-tower AM transmitter site array" width="700" height="auto" class="insert-image" >}}

How does one get a single coherent signal out of an eight-tower array? Enter the _phasor_:

{{< figure src="./wsdz-phasor-inside.jpg" alt="WSDZ Phasor - Insides" width="700" height="auto" class="insert-image" >}}

{{< figure src="./wsdz-phasor-knobs.jpeg" alt="WSDZ - Phasor Knobs" width="700" height="auto" class="insert-image" >}}

That's _phasor_ with an _o_, not _phaser_ with an _e_, so Trekkies need not fret about a misspelling.

The engineer at the station noticed our other tower tours, and was a friend of my Dad's, so he suggested we come see this site. It has one of the more elaborate AM broadcast phasor setups in the area.

Behind the unassuming front panel with all the cranks, there's a series of _very_ beefy variable inductors and vacuum capacitors, where you crank them around to change the phase, power, and reactance of each of the individual towers—in this case, 5 in a day pattern, and 5 in a night pattern.

The inside looks like something out of Frankenstein's lab:

{{< figure src="./wsdz-phasor-inside-inductors-capacitors.jpeg" alt="Phasor variable inductors inside" width="700" height="auto" class="insert-image" >}}

I'm told by the engineer that when there are issues besides a blown capacitor or a relay gone bad (they tend to do that sometimes, with 20 kW of power flowing through them 24x7), the wizards at Phasetek have him call them up to figure out what to do. The phasor itself is only half the tuning equation—in addition to all of it's knobs and relays, there are ATUs, or Antenna Tuning Units, at the base of each tower. And these are also full of massive inductors and capacitors, matching the towers to the phasor and transmitter:

{{< figure src="./wsdz-atu-inductor.jpeg" alt="WSDZ ATU inductor" width="700" height="auto" class="insert-image" >}}

We have an entire video about the tower site, embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/49bwwQxUgcs" frameborder='0' allowfullscreen></iframe></div>
</div>

In the video, we get into all the equipment on the site, and talk on a high level about tower array design, transmitter room layout, grounding for the building and towers, and more—but we didn't dive _too_ deep into the actual physics of the phasor.

For that, I found this great little intro with some nice 1950's illustrations: [Antenna Theory - Directivity](https://www.youtube.com/watch?v=ysNkjEnoRsU). The idea of a 'phased array' of antennas was [introduced in 1905 by Karl Ferdinand Braun](https://en.wikipedia.org/wiki/Phased_array), and the phasor installed in the WSDZ-AM transmitter site builds on that theory, in a relatively simple way.

Modern beam-forming antennas are used for much more exotic applications, from the [flat Starlink satellite dishes](https://www.youtube.com/watch?v=qs2QcycggWU) to [3D radar systems](https://en.wikipedia.org/wiki/Active_Phased_Array_Radar) deployed by the military.

I would highly recommend [watching the video](https://www.youtube.com/watch?v=49bwwQxUgcs) if you want to see more about the application of this tech in AM radio, especially since we demonstrate one of the interesting quirks of running an AM station with a day/night pattern. To control the signal's directionality and reach at night—when the ionosphere extends the reach of AM signals _much_ further—there's a series of 16+ massive RF relays all remotely operated and automated by switchers like this:

{{< figure src="./wsdz-day-night-pattern-switcher.jpeg" alt="WSDZ day night pattern switcher" width="700" height="auto" class="insert-image" >}}

They make an impressive _ka-chunk_ _ka-chunk_, especially in tandem with the transmitter's brief power-down-power-up cycle!

But even when you split up the 20 kW among 5 towers, [it's never a good idea to touch an AM tower](https://www.youtube.com/watch?v=GgDxXDV4_hc).
