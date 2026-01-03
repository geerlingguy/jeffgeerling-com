---
nid: 3210
title: "Watching the Earth move with a Raspberry Pi"
slug: "watching-earth-move-raspberry-pi"
date: 2022-05-25T14:03:53+00:00
drupal:
  nid: 3210
  path: /blog/2022/watching-earth-move-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - earthquake
  - raspberry pi
  - raspberry shake
  - science
  - seismology
  - shakenet
  - usgs
  - video
  - youtube
---

A few months ago, someone from the [Raspberry Shake](https://raspberryshake.org) team got in touch, and asked if I'd like to try out a Shake at my home.

As someone who has spent a bit too much time nerding out over space and atmospheric weather, but never touched seismology, I decided it was time to _dig deep_ and learn a bit more about the Earth.

{{< figure src="./raspberry-shake-basement-floor.jpeg" alt="Raspberry Shake on basement floor" width="700" height="467" class="insert-image" >}}

And learn I did! They sent their simplest model, the [Shake 1 RS1D](https://shop.raspberryshake.org/product/turnkey-iot-home-earth-monitor-rs-1d/), I placed it on my concrete basement floor, and then waited.

For the first few weeks, I mostly had fun observing the oscillation of the washing machine's motor during the spin cycle (the up and down lines below), or the noisy 30 Hz tone of the dryer's drum, spinning for an hour or two at a time (the constant noise you see after the undulating washing machine):

{{< figure src="./Raspberry-Shake-Seismogram-Washer-and-Dryer.gif" alt="Raspberry Shake seismogram - washer and dryer cycles" width="700" height="394" class="insert-image" >}}

The Shake itself is a simple contraption, consisting of (at least, as of this writing):

  - A Raspberry Pi 3 model B+
  - A 4.5 Hz Geophone (just one, mounted vertically)
  - A Shake HAT (with the circuit to translate the Geophone into signals the Pi can use)
  - A bullseye level (bubble level) to help with mounting on a flat surface
  - An acrylic case

{{< figure src="./raspberry-shake-closeup.jpeg" alt="Raspberry Shake closeup" width="700" height="467" class="insert-image" >}}

The model I had was pre-assembled and came with an official Pi power supply and a pre-flashed microSD card with the Shake software package preinstalled. They also offer a weatherproof outdoor model, and models with features like vertical and horizontal geophones, sonic sensors for infrasound, and extra motion sensors to detect a wider range of earthquakes.

## My First Earthquake

As luck would have it, just a few weeks into my journey, I finally had something to observe other than my kids stomping around, or traffic driving by the house—my first local Earthquake!

{{< figure src="./my-first-earthquake-stlouis-peerless-park-april-29-2022.png" alt="My first earthquake - Peerless Park St. Louis MO April 29, 2022" width="646" height="468" class="insert-image" >}}

I can reflect on the little earthquake with joy since nobody got hurt; it was [just a 2.8 according to the USGS](https://earthquake.usgs.gov/earthquakes/eventpage/nm60392336/executive), and other than being a hot topic of conversation for the locals, it didn't affect much.

The image you see above was actually pulled by a local geophysicist, [Dr. Robert Herrmann](https://www.slu.edu/arts-and-sciences/earth-atmospheric-sciences/faculty/herrmann-robert.php), who I interviewed at length in my [video on the Raspberry Shake and citizen science](https://www.youtube.com/watch?v=fcuX1FTfeaA). He's maintained a software package called [Computer Programs in Seismology](https://www.eas.slu.edu/eqc/eqccps.html) for _decades_, starting on a PDP 11, and it's been ported to all modern platforms since then.

And yes, it's even been compiled on a Raspberry Pi :)

Using the public data available through Raspberry Shake's ['ShakeNet'](https://shakenet.raspberryshake.org), Dr. Herrmann was able to pull up and correlate sensor data from all the regional Shakes in the [AM ('Amateur') Seismograph Network](http://fdsn.org/networks/detail/AM/):

{{< figure src="./peerless-park-earthquake-april-29-correlated.png" alt="Peerless Park St. Louis earthquake using public AM seismic network Raspberry Shakes" width="666" height="534" class="insert-image" >}}

Using this data, along with the coordinates of each sensor, one can pinpoint the location of the earthquake, and calculate a rough magnitude.

The USGS, of course, samples a huge variety of sensors that are part of regional and international seismic networks, but the fact that there are over 1,600 Raspberry Shakes means you could do a _lot_—things that were only _dreamt_ of 50 years ago when Dr. Herrmann started his work in the field—using only data that's available through ShakeNet.

This post isn't a full review of the Raspberry Shake. Heck, I barely know the differences between a $10,000 Nanometrix Trillium and a Shake! But that's why I spent a few hours with Dr. Herrmann on SLU's campus, and asked him a lot about their on-campus seismic vault, which has been recording data for nearly 100 years:

{{< figure src="./slu-seismic-vault.jpeg" alt="SLU Seismic Vault - Benioff Seismometers and Raspberry Shake" width="700" height="467" class="insert-image" >}}

On one slab of concrete, poured on top of bedrock near the foundation of SLU's 'old gym', sits a century of seismographic history—from hundreds-of-pounds Benioff seismometers, to cutting-edge Trilliums, to a Raspberry Shake 4D.

SLU [continously monitors the Earth's movement](https://www.eas.slu.edu/eqc/eqc_netrt/eqcnetrt.html), and is one of many institutions which helps governments, corporations, and individuals build better structures, remain accountable (the [AFTAC's U.S. Atomic Energy Detection System](https://www.16af.af.mil/Units/AFTAC/) helps enforce the [Partial Nuclear Test Ban Treaty](https://en.wikipedia.org/wiki/Partial_Nuclear_Test_Ban_Treaty)), and learn more about the world under them.

It was awesome learning about all this from Dr. Herrmann. I actually took classes in meteorology and oceanography (and sat in on 'Water Systems Hydrology') when I attended SLU—but I had no idea my alma mater had such a storied seismology department!

{{< figure src="./seismograph-old-film-florissant-mo-earthquake.jpeg" alt="Seismograph of earthquake in Florissant, MO in 1959 at Jesuit station" width="700" height="467" class="insert-image" >}}

You should [watch the video](https://www.youtube.com/watch?v=fcuX1FTfeaA) if this post piqued your interest. I started this journey thinking it would be neat to test out the Raspberry Shake, but now I find myself checking in on the USGS's website more frequently, reading up on the local history of seismology, and hoping to someday visit the [seismometer deep in Cathedral Cave](https://earthquake.usgs.gov/monitoring/operations/stations/IU/CCM/).

I also recommend the article [Desktop seismology: How a maker-inspired device is changing seismic monitoring](https://www.earthmagazine.org/article/desktop-seismology-how-maker-inspired-device-changing-seismic-monitoring) for a little more background on the project (though some of the numbers and stats in the article are outdated—for example, the Shake now samples at 100 times per second instead of the stated 50).
