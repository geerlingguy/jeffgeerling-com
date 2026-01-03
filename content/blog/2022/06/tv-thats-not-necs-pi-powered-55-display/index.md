---
nid: 3213
title: "The TV that's not: NEC's Pi-powered 55\" Display"
slug: "tv-thats-not-necs-pi-powered-55-display"
date: 2022-06-08T14:01:16+00:00
drupal:
  nid: 3213
  path: /blog/2022/tv-thats-not-necs-pi-powered-55-display
  body_format: markdown
  redirects: []
tags:
  - cm4
  - compute module
  - monitor
  - nec
  - raspberry pi
  - tv
  - video
  - youtube
---

{{< figure src="./this-is-not-a-tv-nec-cm4-display.jpeg" alt="This is not a TV - Jeff Geerling with NEC monitor powered by Raspberry Pi" width="700" height="394" class="insert-image" >}}

The [NEC UHD Professional Display M551](https://www.sharpnecdisplays.us/products/displays/m551) pictured here is not a TV—it's a _display_. And it's powered by a Raspberry Pi.

Specifically, it's powered by a Raspberry Pi Compute Module 4, and that is done using Sharp NEC's new [MPI4E carrier board](https://www.sharpnecdisplays.us/products/accessories/mpi4e):

{{< figure src="./nec-cm4-carrier-side.jpeg" alt="Sharp NEC CM4 carrier side" width="700" height="467" class="insert-image" >}}

I've been tracking [dozens of CM4 carrier boards](https://pipci.jeffgeerling.com/boards_cm) since the Compute Module 4's launch, but none have lived inside a display like this one.

Sharp NEC Display Solutions (formed in 2020 after Sharp and NEC Display Solutions merged) creates a range of digital signage products, but the one that is most ubiquitous is the digital signage display, which can be used as part of a multi-display signboard, as illustrated at a Bath &amp; Body Works at my local shopping mall:

{{< figure src="./display-wall-bath-body-works.jpg" alt="Bath &amp;amp; Body Works - multi-display wall digital signboard" width="700" height="394" class="insert-image" >}}

Or used standalone in either portrait or landscape orientation, both of which are utilized at a Sunglass Hut nearby:

{{< figure src="./display-standalone-sunglass-hut.jpg" alt="Sunglass Hut - Digital signboard displays in horizontal and vertical orientations" width="700" height="394" class="insert-image" >}}

On my YouTube channel, I detail how compatible Sharp NEC displays use this Compute Module 4 carrier board to power the display, and how their custom MediaPlayer application runs on it:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/-epPf7D8oMk" frameborder="0" allowfullscreen=""></iframe></div>
</div>

## The Pi Inside

{{< figure src="./nec-cm4-carrier-top.jpeg" alt="Raspberry Pi Compute Module 4 carrier board Sharp NEC" width="700" height="481" class="insert-image" >}}

In the picture above, the heat sink is removed to show the Pi.

This card is a custom layout that's specific to Sharp/NEC-branded displays. Intel has it's own [Smart Display Module (SDM) standard](https://www.intel.com/content/www/us/en/design/products-and-solutions/solutions/smart-display-module/overview.html)—but this is _not_ that, and it is not pin-compatible.

One benefit this affords Sharp NEC is the ability to run a Compute Module 4 and SDM side-by-side, for redundancy. If the active display computer locks up, the display can fail over to the other one.

{{< figure src="./nec-cm4-carrier-ports.jpeg" alt="Sharp NEC CM4 port side" width="700" height="467" class="insert-image" >}}

With the heat sink installed, the Pi stayed below 40°C in all my testing, thanks to the generous passive ventilation in the display, plus the fans along the top that will activate when any part of the system crosses a configurable threshold. In all my testing (in a climate controlled environment), the fans never ran except for during boot!

The custom connector makes it easy to integrate the Pi into the display too—even if you're not running MediaPlayer as the OS!

{{< figure src="./nec-cm4-carrier-edge-slot.jpeg" alt="CM4 Edge slot for Sharp NEC display board" width="700" height="467" class="insert-image" >}}

Through the edge connector, the Pi is exposed to an internal serial bus for display management, an internal 100 Mbps Ethernet network managed by the display (in case you want to connect through the _display's_ Ethernet ports instead of the CM4's own gigabit port), some GPIO lines to things like the remote sensor, and an internal USB hub used for various purposes.

Using the Pi, you can even remotely manage the display's internal configuration via SSH—Sharp NEC even maintains a [Python-based Software Development Kit (SDK)](https://assets.sharpnecdisplays.us/documents/installationguides/nec_raspberry_pi_compute_module4_setup_guide.pdf) for display management, so you could write your own Pi-based display management software for a fleet of these displays.

{{< figure src="./emulation-station-retropie-sharp-nec-display.jpg" alt="Emulation Station RetroPie running on Sharp NEC display MA551" width="700" height="394" class="insert-image" >}}

And since the Pi can run most _any_ OS, I was also able to boot [RetroPie](https://retropie.org.uk), [LibreELEC](https://libreelec.tv) (which runs Kodi), and Raspberry Pi OS natively, all built into the display.

A few caveats:

  - The carrier board doesn't have a microSD card slot, so only eMMC versions of the Compute Module 4 can be used with it
  - Because the BCM2711 can't handle 4K streams seamlessly, MediaPlayer limits the Pi's resolution to 1080p. This isn't a big issue in practice, but I did try some 4K streaming through Kodi/LibreELEC, and found it to not be as smooth an experience as 1080p, so the limitation makes sense.
  - The user manual says USB flash drives can be formatted as exFAT, but it seemed that didn't work, so I had to format my drive as FAT32 to be readable by MediaPlayer.

Overall, this display is one of the best 'TV's I've used—even though it's not, technically-speaking, a 'television'. There isn't any spyware, adware, or other janky software running on it, the colors and brightness are excellent, and most of all it _just works_.

There are OLEDs and other displays with more vibrant color, deeper blacks, and more brightness—but most of them won't last if you run them 24x7 across a variety of environments and try managing them from a central location!

Check out my [video on the Sharp NEC display and Compute Module 4](https://www.youtube.com/watch?v=-epPf7D8oMk) for more details.

The [RaspberryPi 4 System on a Chip Solution - MPI4E](https://www.sharpnecdisplays.us/products/accessories/mpi4e) can also be purchased separately.

> The display, compute module 4 carrier board, stand, and speakers shown in this blog post were provided by Sharp NEC Display Solutions of America for the purposes of review. No other compensation was provided.
