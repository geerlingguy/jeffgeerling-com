---
date: '2026-07-10T09:00:00-05:00'
tags: ['sdr', 'quadrf', 'crowd supply', 'youtube', 'rf', 'geerling engineering', 'raspberry pi', 'pi 5']
title: 'QuadRF can spot drones and see WiFi through my wall'
slug: 'quadrf-can-spot-drones-and-see-wifi-through-my-wall'
---
{{< figure
  src="./quadrf-antennna-array.jpeg"
  alt="QuadRF antenna array from front"
  width="700"
  height="auto"
  class="insert-image"
>}}

The [QuadRF](https://scalerf.com) (pictured above) a phased-array radio built around a Raspberry Pi 5 and an FPGA board with picosecond-level timing. It does advanced signal processing and beamforming.

It can see WiFi through walls and track drones in flight.

If the open source community can come up with something like this, just imagine what governments are capable of.

When you plug a computer into a network, tools like [Wireshark](https://www.wireshark.org) can show all the hidden traffic you might not even know is there. _WiFi_ packets are the same, but those travel through the air, allowing snooping without physical access.

The QuadRF has built-in software that can stream and decode RF, and you can pipe it out to a more powerful computer for things like WiFi traffic analysis.

I mention this not to scare you—governments have had tools like these for years. It's just better to know what's possible and expose bad security practices than to ban useful tools like these. _So if you're in the CIA, don't get any ideas._

## To the Moon

{{< figure
  src="./moonrf-assembly.jpg"
  alt="ScaleRF Moon Array with large apeture"
  width="700"
  height="auto"
  class="insert-image"
>}}

After spotting QuadRF [on Hackaday](https://hackaday.com/2026/06/20/seeing-the-world-in-radio-waves-with-the-quadrf/), I reached out to Martin McCormick, who's been working on QuadRF as part of a bigger project: a Moon-scale antenna array, capable of EME (Earth-Moon-Earth) radio experiments and radio astronomy.

I think Martin took inspiration from [Dishy](https://arstechnica.com/information-technology/2020/12/teardown-of-dishy-mcflatface-the-spacex-starlink-user-terminal/), SpaceX's original Starlink terminal. (Makes sense, since Martin worked at SpaceX on the team that built Dishy!)

Instead of locking this phased array antenna system into a proprietary satellite system, licensed operators will ideally be able to chain multiple QuadRF modules together for interesting radio experiments, with up to 1.15 MW EIRP—basically, a massive amount of directional antenna gain, for high power RF fun.

But QuadRF is scaled down to handheld-size, and while it isn't powerful enough to send a signal to the moon, it's still quite useful in local SDR applications and visualizing the RF environment—at least in it's frequency range of 4.9-6 GHz.

## Testing QuadRF

But I specifically asked Martin if he'd be willing to send over a prototype QuadRF for my Dad (a retired broadcast radio engineer) and I to test.

I had already placed a pre-order on Crowd Supply (where a [basic kit](https://www.crowdsupply.com/scale-rf/quadrf#products) is $499), but I wanted to see if QuadRF was really as useful or intuitive as it seemed from the videos ScaleRF posted.

Spoilers: it's still a little rough in the UI department, but I was blown away by how well it works. Especially considering everything's running on a Raspberry Pi 5.

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/QESevE2c_cc' frameborder='0' allowfullscreen></iframe></div>
</div>

When you turn it on, the Pi boots up and creates a WiFi hotspot. You connect to that, and visit `http://quadrf/`. That page runs a VNC session in your browser, where you can launch apps from GNU Radio to SDR software, and even their custom AR (Augmented Reality) RF visualizer.

The AR visualizer is the most interesting included software, despite being less useful for real-world SDR applications.

{{< figure
  src="./quadrf-augmented-reality-iphone.jpg"
  alt="QuadRF showing augmented reality WiFi signal overlay on laptop"
  width="700"
  height="auto"
  class="insert-image"
>}}

The UI is a little rough, but you can adjust the alignment between your camera and the phased array, and the gain of the receiver.

Then it will visualize frequencies from 4.9-6 GHz as colorful 'blobs'. The scale is not shown on the display in this early version, but from my testing around the studio, my 5 GHz WiFi network (which was running on Channel 100, or around 5.5 GHz) showed up light blue. Neighboring WiFi networks were showing up red or green.

If you order the Mobile Expansion Pack, it incorporates a battery power pack, and a handheld phone mount, so you can walk around analyzing part of the C-band in real-time.

{{< figure
  src="./quadrf-drone-flying-blob.jpg"
  alt="QuadRF showing 5 GHz signal over drone in augmented reality mode"
  width="700"
  height="auto"
  class="insert-image"
>}}

My Dad and I flew his DJI Mini Pro 4 behind the studio, and the QuadRF had no trouble picking it out of the sky. As it flew away, I had to increase the gain to keep seeing it; it would be nice to have AGC or an easier gain control as the UI was a little clunky when carrying around the contraption.

It sounds like the crowdfunding campaign is already beyond expectations, and they'll be switching the enclosure to an injection mold (the version I have is 3D printed).

## Raspberry Pi 5 MIPI for high-bandwidth RF

{{< figure
  src="./quadrf-open-raspberry-pi-5-mipi-inside.jpg"
  alt="QuadRF open showing Raspberry Pi 5 and MIPI connection to FPGA antenna board inside"
  width="700"
  height="auto"
  class="insert-image"
>}}

One aspect that intrigued me was the use of the Raspberry Pi's MIPI lanes for low latency SDR streaming I/Q (In-phase/Quadrature) at data rates over 5 Gbps. From the [QuadRF Documentation](https://scalerf.com/docs/):

> The novel approach of streaming I/Q over the Pi’s camera and display FFC MIPI connectors has many benefits. MIPI can handle >5 Gbps, low-latency, full-duplex data transfer through the Pi’s RP1 chip. It is simpler and more reliable than USB, adds almost zero hardware cost to the RF board, and can sustain hundreds of MSPS of I/Q with no hiccups or sample loss. Considering cameras and displays are the ultimate form of high-bandwidth signal streaming, it makes sense their standard digital interface is a great match for SDR! We think the industry should adopt it more widely!

It sounds like they had to reverse-engineer the MIPI protocol used on the Pi 5 to do this (since it goes through the RP1 chip), and the way it's architected, you can daisy-chain multiple QuadRF modules together, letting each module calculate it's own phase shift.

I'm not sure how that will work in practice, but it sounds pretty neat. PCIe could probably work in a pinch, too, but this implementation frees up the PCIe connector in case you want high speed storage or even higher speed networking than the Pi offers.

## Conclusion

As with all pre-production gear I test, take everything I've shown with a grain of salt. And with any crowdfunding campaign, if you back it, don't expect the QuadRF to show up on your doorstep overnight.

I was initially skeptical about how useful and fun this little handheld phased array could be, but after using it for a week, I can't wait until the one I pre-ordered ships!
