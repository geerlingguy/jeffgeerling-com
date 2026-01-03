---
nid: 3495
title: "How much radiation can a Pi handle in space?"
slug: "how-much-radiation-can-pi-handle-space"
date: 2025-10-08T15:32:50+00:00
drupal:
  nid: 3495
  path: /blog/2025/how-much-radiation-can-pi-handle-space
  body_format: markdown
  redirects: []
tags:
  - cubesat
  - mark rober
  - nasa
  - radiation
  - raspberry pi
  - satellite
  - space
  - youtube
---

Late in the cycle while researching [CubeSats using Pis in space](/blog/2025/cubesats-are-fascinating-learning-tools-space), I got in touch with [Ian Charnas](https://www.iancharnas.com)[^ian-charnas], the chief engineer for the [Mark Rober](https://www.youtube.com/channel/UCY1kMZp36IQSyNx_9h4mpCg) YouTube channel.

Earlier this year, Crunchlabs launched [SatGus](https://space.crunchlabs.com), which is [currently orbiting Earth](https://www.n2yo.com/satellite/?s=62713) taking 'space selfies'.

{{< figure src="./space-selfie-mark-rober-crunchlabs-satgus.jpg" alt="Space Selfie of Geerling family on SatGus earlier this year" width="700" height="553" class="insert-image" >}}

The way it works:

  - You upload a photo on the [Space Selfie](https://space.crunchlabs.com) website
  - The photo is scheduled to be taken aboard SatGus on its onboard Google Pixel phone, using a camera built by [Redwire Space](https://redwirespace.com)
  - The flight computer (FCM) receives batches of photos and associated metadata over [S band](https://en.wikipedia.org/wiki/S_band), and stores it onboard
  - A Raspberry Pi Compute Module 4 (on a custom carrier board designed by [Tyvak International](https://tyvak.eu/missions/satgus/)) uses USB [ADB](https://developer.android.com/tools/adb) to control the Pixel phone and display the image
  - The camera snaps the photo, and batches of photos are downlinked over S-band by the flight computer (FCM)

I was interested from the outset, because launching a 12U CubeSat into space isn't cheap, and requires a _lot_ of engineering. I'm guessing that's why Mark Rober's team partnered with Tyvak and Redwire: focus on the 'space selfies' bit while letting an established satellite provider focus on flight control, power, and the main chassis.

Couple that with the Raspberry Pi onboard, which I had only learned of a couple days before publishing my [PIS IN SPACE!](https://www.youtube.com/watch?v=qvN3sE2Nv4U) video, and I and many viewers wanted to know: _how well does a Pi fare in space?_

[NASA has extensive documentation on radiation risks in Low Earth Orbit (LEO)](https://ntrs.nasa.gov/api/citations/20240008413/downloads/Minow%20-%20COSPAR%202024%20-%20Radiation%20-%20final.pdf), and many COTS (Commercial Off-the-Shelf) parts—including the Raspberry Pi—are not rated for space, nor do they handle things like [bit-flips from radiation exposure](https://blog.mozilla.org/data/2022/04/13/this-week-in-glean-what-flips-your-bit/) well.

I asked Ian (the chief engineer) what research _they_ had done, and he said they worked with both UC Davis and the University of Maryland on radiation testing.

## Rad-hardened Raspberry Pi?

{{< figure src="./build-a-cubesat-hero.jpeg" alt="Build a CubeSat" width="700" height="394" class="insert-image" >}}

According to Ian (and a couple other people who've flown Pis in space), the Raspberry Pis in space—including the multiple Pis [flying on the ISS](https://astro-pi.org)—are not special in any way; there's no radiation-hardened chips being swapped out, they're the same boards you'd find if you walked into Micro Center and purchased one today.

Instead, because there _is_ a risk of the Pi shutting down, it's simply not in the critical path for flight operations. It's used for auxiliary tasks, which can be briefly interrupted. The main flight computer uses a [watchdog timer](https://en.wikipedia.org/wiki/Watchdog_timer) or some other means to reboot the Pi in case of issues. Sometimes a small amount of metal shielding is added around the Pi, but this only delays the inevitable—[single-event upsets](https://en.wikipedia.org/wiki/Single-event_upset) are bound to happen, even under ideal conditions.

But in the absence of hard data to back up their build plans, Mark Rober's team blasted the Pi with radiation to see how it might fare.

## So... how much radiation can the Pi handle?

First, Ian said they tested the phone they were flying, the Google Pixel 7 Pro. It was chosen over the Pixel 9 Pro because 3rd party testing indicated the display on the 7 was slightly more radiation-tolerant.

{{< figure src="./uc-davis-cyclotron-diagram.jpg" alt="Cyclotron status panel at UC Davis" width="700" height="394" class="insert-image" >}}

After a number of tests, they had a single event upset every 63.5 Rads, using a [cyclotron at UC Davis](https://crocker.ucdavis.edu/cyclotron-services) (status panel pictured above), which was pumping out a beam at 50 Rads/minute.

The phone would reboot, then function normally, through multiple test cycles.

To see how far the phone could go, they bumped the rate to 1,000 Rad/min (20x higher), and finally got the Pixel phone to die around 9.2 kRads into the experiment.

{{< figure src="./uc-davis-cyclotron-raspberry-pi-cm4-io-board.jpg" alt="Raspberry Pi CM4 IO Board and Compute Module 4 facing the cyclotron beam at UC Davis" width="700" height="394" class="insert-image" >}}

Then they switched gears to the Raspberry Pi Compute Module 4. It is pictured above, opposite the beam window, on the other side of the CM4 IO Board facing away from us. You don't want to be in its position while the beam is active[^proton-therapy]!

In the first tests, at 50 Rads/minute, the CM4 reset on average every 39.3 Rads. They ran out of time to do a 'test until failure' high-dosage test while at UC Davis, so if anyone out there has a cyclotron, please leave a comment with your data if you can point it at a Pi for me!

_No, seriously: I'll ship you a few CM4 if you like ;)_

### Gamma testing

They also did gamma testing using a [Cobalt-60 radiation source at the University of Maryland](https://radiation.umd.edu/irradiator/).

The Pixel 7 Pro survived 10,000 Rads at 17.5 Rads/second with no discernible issues, as did the Raspberry Pi CM4. They even tested a Pi display from 'Wisecoco', and it survived too!

They were able to test until failure this time, and the CM4 + Wisecoco display setup had a permanent failure at 57.8 kRads.

{{< figure src="./wisecoco-pi-cm4-gamma-radiation-test-results.jpg" alt="Wisecoco Pi CM4 Gamma Radiation Test Results" width="700" height="620" class="insert-image" >}}

They tested with a number of identical units (between 5-10 each time) so they would have a good dataset (which they've kindly shared in [this PDF](https://drive.google.com/file/d/132eccmYpLPDXJAnjqv-2GAj9-PkJ_k_b/view)), and they worked with a radiation expert to determine how much shielding they should put in the CubeSat.

A 5mm thick aluminum enclosure was chosen for SatGus. The hope is that will prevent a 'kill dose' for the entire mission (at least 1 year).

## Conclusion

Ian had nothing but high praise for both UC Davis and the University of Maryland teams they worked with. I'm extremely grateful he got back to me about the details of their experiments. This is the type of test data that would likely get lost in the ether, as Mark Rober's team moves on to their next fun science project!

And regarding Pis in space, this entire post assumes we're talking LEO ([Low Earth Orbit](https://en.wikipedia.org/wiki/Low_Earth_orbit)). At higher orbits, the radiation can be much higher, so more planning would need to take place, if you wanted to blast a Pi up into MEO or HEO (Medium/High Earth Orbit), you'd need to spend a bit more time planning!

If you have questions about irradiating your _own_ Raspberry Pi, and you're looking for detailed scientific answers, I'm probably not the best source.

[^ian-charnas]: Ian shared with me the last three images in this post as well. Thanks so much for Crunchlabs' willingness to share test data!

[^proton-therapy]: Even if you were undergoing proton therapy to remove a tumor... this particular cyclotron isn't configured for patient use!
