---
date: '2026-03-13T09:00:00-05:00'
tags: ['xserve', 'g5', 'retro', 'mac', 'apple', 'youtube', 'video', 'recap', 'capacitor plague', 'repair', 'vintage']
title: 'Restoring an Xserve G5: When Apple built real servers'
slug: 'restoring-xserve-g5-apple-server'
---
Recently I came into posession of a few Apple Xserves. The one in question today is an Xserve G5, [RackMac3,1](https://everymac.com/systems/apple/xserve/specs/xserve_g5_2.0.html), which was built when Apple at the top—and bottom—of it's PowerPC era.

{{< figure
  src="./xserve-g5-hero.jpeg"
  alt="Xserve G5 on Jeff's desk"
  width="700"
  height="auto"
  class="insert-image"
>}}

This isn't the first Xserve—that honor belongs to the G4. And it wasn't the last—there were a few generations of Intel Xeon-powered RackMacs that followed. But in my opinion, it was the most interesting.

Unfortunately, being manufactured in 2004, this Mac's Delta power supply, especially, suffers from the [Capacitor Plague](https://en.wikipedia.org/wiki/Capacitor_plague). If it won't boot, chances are the PSU needs a recap. The PSU in here tends to run hot, and some of the capacitors weren't even 105°C-rated, so they tend to wear out regardless, especially if the Xserve was running high-end workloads.

The one I have ran gene-sequencing software, judging by the pile of CDs that came with it. Between that and the dust I had to blast out of it, I'm guessing it's seen some use!

This blog post is more about the overall Xserve experience, but if you want to see in detail how I restored the Xserve's PSU, installed Mac OS X Server 10.3, and how it runs, check out today's video:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/kFnvZ4NWr00' frameborder='0' allowfullscreen></iframe></div>
</div>

## Restoring the PSU

The first order of business was recapping the PSU, and luckily [The House of Moth](https://thehouseofmoth.com/recapping-an-xserve-g5-power-supply-part-1-preparations/) maintains a guide for the process. I got in touch and was able to snag a pre-sorted kit of the right electrolytic capacitors for the job (13 total).

{{< figure
  src="./xserve-g5-psu-recap-soldering.jpeg"
  alt="Xserve G5 PSU - Jeff Geerling recapping soldering iron"
  width="700"
  height="auto"
  class="insert-image"
>}}

The video has the whole process, but the PSU has a number of small SMD (Surface Mount Device) components on the underside—usually right in the mix with the legs of the through-hole-soldered capacitors. That meant my trusty [Hakko FR-301](https://amzn.to/40xDkfg) with it's default tip was hard to use in a couple spots.

I had to go back and forth between flowing in fresh solder, wicking a little away, cleaning up the solder on a couple nearby components, and sucking out the holes for the capacitor legs on four or five joints.

All's well that ends well, and I could measure 12V after reassembling the PSU. There's a little coil whine, but I'm not sure if that's normal or not. It's certainly masked by the fans on the system, once they're powered up :)

## SATA HDD Trays and an interesting lock

Besides the non-standard PSU, the Xserve used a non-standard connector for the hot-swap hard drive trays. The drive trays themselves hold up well, but the wires inside seem a little delicate. And the few ventilation holes under the drive handles seemed to be clogged with dust—so I give these drive trays a C- for overall function.

{{< figure
  src="./xserve-g5-ssd-in-sata-hdd-tray.jpeg"
  alt="Xserve G5 SATA SSD in proprietary HDD tray"
  width="700"
  height="auto"
  class="insert-image"
>}}

I first tried a 120 GB Inland SSD, but it wouldn't be recognized by the Mac OS X Server 10.3 install CD that came with the system. So I tried a 240 GB drive (one that's a couple years newer—both were SATA-III), and that worked!

While I was installing Mac OS X Server, I took a peek around the rest of the chassis. Most things were standard—or at least as standard as you see on Apple hardware—but the drive/system lock mechanism was certainly quirky:

{{< figure
  src="./xserve-g5-lock-mechanism.jpg"
  alt="Xserve G5 locking mechanism and front panel connections"
  width="700"
  height="auto"
  class="insert-image"
>}}

Apple made a heavy knurled hex key for the system lock, and when you turned it, a long rod with a worm gear would lock in the drive trays. Partway down the rod, there were two white cylinders—these pass over either optical or magnetic sensors, which tell the system when the lock is active (which lights up a lock LED on the front as well).

## Power Consumption and Noise

Also during installation, I started taking measurements of power consumption

{{< figure
  src="./xserve-g5-dual-g5-cpu-2ghz.jpeg"
  alt="Xserve G5 power consumption - 200W"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO.

{{< figure
  src="./xserve-g5-200w-power-consumption.jpeg"
  alt="Xserve G5 power consumption - 200W"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO.

{{< figure
  src="./xserve-g5-noise-60dba.jpeg"
  alt="Xserve G5 noise - 60 dBa"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO.

## The Mac OS X Server Experience

TODO.

{{< figure
  src="./xserve-g5-ati-pci-graphics.jpeg"
  alt="Xserve G5 ATI PCI Graphics Card"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO: (graphics card, VGA, wavy display)

{{< figure
  src="./xserve-g5-mac-os-x-server-monitor.jpg"
  alt="Xserve G5 running Mac OS X 10.3 Server Monitor App"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO.

## Remote Access and an actual Purpose

TODO.

{{< figure
  src="./xserve-g5-in-rack.jpeg"
  alt="Xserve G5 installed in Rack"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO.

{{< figure
  src="./xserve-g5-ports-fw800-serial-usb.jpeg"
  alt="Xserve G5 ports on rear - 9-pin Serial, FireWire 800, and USB"
  width="700"
  height="auto"
  class="insert-image"
>}}

TODO.
