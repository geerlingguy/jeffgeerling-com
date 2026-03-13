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

This isn't the first Xserve—that honor belongs to the G4[^xserveintro]. And it wasn't the last—there were a few generations of Intel Xeon-powered RackMacs that followed. But in my opinion, it was the most interesting.

Unfortunately, being manufactured in 2004, this Mac's Delta power supply suffers from the [Capacitor Plague](https://en.wikipedia.org/wiki/Capacitor_plague). The PSU tends to run hot, and some of the capacitors weren't even 105°C-rated, so they tend to wear out, especially if the Xserve was running high-end workloads.

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

The video has the whole process, but the PSU has a number of small SMD (Surface Mount Device) components on the underside—usually right in the mix with the legs of the through-hole-soldered capacitors. That meant my trusty [Hakko FR-301](https://amzn.to/40xDkfg) with it's default tip was hard to use in a couple spots[^hakkotip].

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

I first tried a [120 GB Inland Professional SSD](https://amzn.to/4rsrMEW), but it wasn't recognized by Mac OS X Server 10.3's Install CD Disk Utility. So I tried a [240 GB Inland Platinum drive](https://www.microcenter.com/product/645077/inland-platinum-256gb-ssd-3d-tlc-nand-sata-iii-6gb-s-25-internal-solid-state-drive) (both were SATA-III), and that worked!

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

Also during installation, I checked how much power the Xserve was gobbling. Turned off, around 9W (which is honestly not terrible, for the era). Turned on, before booting up fully, around 199W (which is a lot).

{{< figure
  src="./xserve-g5-200w-power-consumption.jpeg"
  alt="Xserve G5 power consumption - 200W"
  width="700"
  height="auto"
  class="insert-image"
>}}

After booting, it would settle in around 140W at idle. I know there's [CHUD Tools](https://www.betalogue.com/2004/01/03/trying-chuds-nap-feature-on-my-power-mac-g4-mdd/) (Computer Hardware Understanding Development), which installs a System Preference pane to disable one of the CPUs entirely, but I haven't checked if that works on the Xserve G5.

{{< figure
  src="./xserve-g5-dual-g5-cpu-2ghz.jpeg"
  alt="Xserve G5 power consumption - 200W"
  width="700"
  height="auto"
  class="insert-image"
>}}

I think if you run one of these things, you just have to get over the power consumption; the fans alone are likely 20W-40W of that total!

The other thing you'll have to get used to—if you're not used to server hardware—is the noise:

{{< figure
  src="./xserve-g5-noise-60dba.jpeg"
  alt="Xserve G5 noise - 60 dBa"
  width="700"
  height="auto"
  class="insert-image"
>}}

Honestly the fans aren't as loud as other 1U servers I've used. Even networking gear can get up to the 70-80 dBa range. The fans in the Xserve seem tuned well enough, and I was surprised when I noticed there's no fan blowing air [_under_ the motherboard](https://thehouseofmoth.com/a-little-known-fact-about-the-power-mac-g5-and-what-to-do-with-this-information/)[^northbridge].

The G5 was the pinnacle of Apple's PowerPC chips. Unfortunately it was also the hottest chip Apple used, as [IBM had trouble shrinking process nodes for more efficiency](https://www.eweek.com/apple/3ghz-powerpc-g5-eludes-ibm/). This was the direct motivation for their [move to Intel](https://en.wikipedia.org/wiki/Mac_transition_to_Intel_processors), which not only allowed Apple to hit 3 GHz clock speeds, it gave them a path forward for faster laptops.

## The Mac OS X Server Experience

After 15 minutes or so (SSDs are _so_ much faster than hard drives on this system), Mac OS X Server 10.3 was installed.

While I was using the system, I saw different wavy patterns in the VGA output (I was using a 1080p HP monitor with VGA input).

I know old, tired capacitors can lead to artifacts on the display, with analog tech like VGA or composite output... and it looks like there's a good number of surface-mount caps on the other side of this ATI PCI-X VGA card:

{{< figure
  src="./xserve-g5-ati-pci-graphics.jpeg"
  alt="Xserve G5 ATI PCI Graphics Card"
  width="700"
  height="auto"
  class="insert-image"
>}}

The pattern got less annoying (or I just got used to it), and I started testing out the built-in server apps Apple shipped with [10.3 Server](https://macintoshgarden.org/apps/mac-os-x-server-103-unlimited-clients-edition).

{{< figure
  src="./xserve-g5-mac-os-x-server-monitor.jpg"
  alt="Xserve G5 running Mac OS X 10.3 Server Monitor App"
  width="700"
  height="auto"
  class="insert-image"
>}}

The monitoring apps and GUI for managing services like Apache, NTP, File Sharing, etc. were straightforward, and refreshingly simple.

Apparently managing the services _behind_ these apps was frustrating if you were used to the control you'd get on, say, Linux. But I can imagine many school district admins loving the push-button simplicity of spinning up a local webserver, or clicking one button to launch [QuickTime Streaming Server](https://en.wikipedia.org/wiki/QuickTime_Streaming_Server).

## Remote Access and an actual Purpose

Besides wanting to see what the Xserve was like, I do have a use for this Xserve G5—at least I hope.

It came with a full rackmount kit, so I dutifully installed it in my rack:

{{< figure
  src="./xserve-g5-in-rack.jpeg"
  alt="Xserve G5 installed in Rack"
  width="700"
  height="auto"
  class="insert-image"
>}}

It is not a good rackmount kit.

The enclosure _is_ the rackmount, which is as annoying as it sounds. You have to hold the entire enclosure in place while you screw in the front screws, then slide some braces and extra brackets in the back, for a 4-post rack install.

And heaven forbid the enclosure is not square—that makes the installation even more difficult[^cagenuts].

But my purpose for this Xserve involves one of the most unique ports on any Mac made since the 80s:

{{< figure
  src="./xserve-g5-ports-fw800-serial-usb.jpeg"
  alt="Xserve G5 ports on rear - 9-pin Serial, FireWire 800, and USB"
  width="700"
  height="auto"
  class="insert-image"
>}}

That's a full DB9 serial port, used on this Mac as a Console port. I _think_ it's possible to use the port like a regular 'ol serial port in macOS, but if that's not the case, I might try a PowerPC-specific version of Linux.

My goal is to get a GPS signal in through serial, so I can consume both the NMEA sentence (which delivers time/datestamps), _and_ PPS (a precise signal to mark the beginning of each second).

If the clock line works like I _think_ it should, I might be able to build the world's most accurate Mac time server!

There might be ways to do it better on modern Macs, but any good timing infrastructure on modern macOS seems tucked away behind private APIs :(

[^xserveintro]: Watch Steve Jobs introduce the Xserve at the [2002 Apple Special Event](https://archive.org/details/2002-05-13-wwdc-xserve-introduction). It's the first (and maybe last?) time I've heard Apple introduce a product with the word 'humble' as the tagline!

[^hakkotip]: Hakko makes [specialized tips](https://amzn.to/3MY8zgw) for tight work around other components... I may buy a few in various sizes since I do some SMD work that could benefit from it.

[^northbridge]: Unlike the desktop G5, the motherboard on the Xserve G5 puts the hot northbridge IO chip on the topside. I guess Apple assumed there was enough airflow in the chassis to keep it cool with a smaller heatsink. The backside cooling on the desktop G5 was elaborate, and very annoying to service.

[^cagenuts]: As if getting cut inserting cage nuts isn't trying enough!
