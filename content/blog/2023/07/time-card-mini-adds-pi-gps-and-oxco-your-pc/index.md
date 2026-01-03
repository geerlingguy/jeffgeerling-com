---
nid: 3301
title: "Time Card mini adds Pi, GPS, and OCXO to your PC"
slug: "time-card-mini-adds-pi-gps-and-oxco-your-pc"
date: 2023-07-27T13:59:33+00:00
drupal:
  nid: 3301
  path: /blog/2023/time-card-mini-adds-pi-gps-and-oxco-your-pc
  body_format: markdown
  redirects: []
tags:
  - gps
  - ltx
  - ltx2023
  - ocxo
  - pcie
  - raspberry pi
  - time card
  - video
  - youtube
---

For [LTX 2023](https://www.ltxexpo.com), I built this:

{{< figure src="./cm4-timecard-mini-running-gps-locked.jpeg" alt="CM4 Timecard mini GPS locked" width="700" height="467" class="insert-image" >}}

This build centers around the [Time Card mini](https://store.timebeat.app/collections/timecard-mini). Typically you'd install this PCI Express card inside another computer, but in my case, I just wanted to power the board in a semi-portable way, and so I plugged it into a CM4 IO Board.

The Time Card mini is a PCIe-based carrier board for the Raspberry Pi Compute Module 4, and by itself, it allows you to install a CM4 into a PC, and access the CM4's serial console via PCIe.

But the real power comes in 'sandwich' boards:

{{< figure src="./timecard-gps-sandwiches-cm4-pcie.jpeg" alt="Time Card GPS sandwich boards with Raspberry Pi CM4" width="700" height="405" class="insert-image" >}}

For the Raspberry Pi 4, people add on HAT—Hardware Attached on Top. But this configuration reverses that trend—the hardware addons are on _bottom_, so I'm calling it a Pi sandwich:

{{< figure src="./timecard-cm4.jpeg" alt="Time Card with U-blox GPS sandwich and CM4" width="700" height="394" class="insert-image" >}}

Timebeat is selling a variety of GPS module sandwich boards, and the one I'm using in my build is the most premium, pairing a [U-blox LEA-M8F](https://store.timebeat.app/products/gnss-raspberry-pi-cm4-module?variant=42280855699627) with the Time Card mini.

(This blog post is a summary of my [video on the Time Card mini on YouTube](https://www.youtube.com/watch?v=dxtVyDXvIBE), embedded below:)

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/dxtVyDXvIBE" frameborder="0" allowfullscreen=""></iframe></div>
</div>

These modules don't run cheap—the LEA-M8F is a little over $250. But it's one of the best GPS modules on the market, and has another feature time nerds love: it can use an external OCXO ([Oven-Controlled Crystal Oscillator](https://en.wikipedia.org/wiki/Crystal_oven)). And Timebeat sent me a [SiTime module](https://store.timebeat.app/products/si5721-sitime-mems-expansion-module?pr_prod_strat=use_description&amp;pr_rec_id=99fed999f&amp;pr_rec_pid=7538686099627&amp;pr_ref_pid=7374750351531&amp;pr_seq=uniform) capable of keeping a second to within 5 ppb!

{{< figure src="./timecard-sitime-osp-tap-oscillator-oxco.jpg" alt="SiTime OCXO on Time Card mini" width="700" height="423" class="insert-image" >}}

An oven inside _that_ little chip? Yes.

The OCXO isn't for baking cookies, though, it's a special highly-accurate oscillator. Much more accurate than the tiny little quartz crystals used in itty-bitty oscillators you'll find on practically every computing device, ever.

Quartz crystals are pretty accurate, but under normal conditions, they can drift as the temperature changes. OCXOs _heat up_ the crystal inside to something like 100°C, and the stable high temperature makes it way more stable. In the case of the SiTime, accurate within 5 ppb of a true second.

Only CSACs (Chip-Scale Atomic Clocks) and exotic clocks like the NIST F2 cesium fountain are substantially better—though they certainly wouldn't look small compared to a Raspberry Pi CM4!

But why the need for accurate holdover if you already have GPS? GPS provides incredibly accurate time, and is the time base for most modern devices that need better-than-NTP accuracy.

Well, GPS isn't perfect. Like if you're inside, it's hard to get a good GPS signal.

And if you're in a noisy radio environment—or heck, maybe even over in Ukraine where [Russia's been jamming GPS signals!](https://www.gpsworld.com/ukraine-attacks-changed-russian-gps-jamming/)—having accurate clock holdover is important.

But what for? NTP (Network Time Protocol) is plenty accurate if you just need to know time down to a few milliseconds.

But every day, more and more things rely on high-precision clocks:

  - VR uses accurate clocks for more accurate positioning data, down to the _millimeter_.
  - Submarines require [precision clocks](https://www.slx-timing.com/underwater-system-precision-clock/) for anything from positioning to sonar.
  - [Radio telescopes](https://en.wikipedia.org/wiki/Very-long-baseline_interferometry) coordinate incoming data using highly-accurate clocks.
  - Data centers and banks timestamp all transactions for global and distributed sync.

Or—in my case—I wanted a timer to help manage my [LTX 2023 Homelab Creator Livestream](https://www.youtube.com/watch?v=wHlJR6vpRkc)! To make sure we don't ramble on too long, I built this:

{{< figure src="./timecard-gps-locked-cm4-running.jpeg" alt="Timecard GPS locked with CM4 and Blinkstick Nano" width="700" height="394" class="insert-image" >}}

This thing is kind of a frankenstein board, but I'm happy with it. I have the Time card mini plugged into a Compute Module 4 IO board using a 90° PCIe riser. The U-blox LEA-M8F is on the sandwich board with the SiTime OCXO connected, then a Compute Module 4 sits on top.

I have a USB Blinkstick to indicate how much time is left, splitting up an hour into 5 minute segments:

  - For the first three minutes, it is green.
  - For the fourth minute, it changes to amber.
  - For the fifth minute, it starts orange, then changes to red with 30 seconds left.
  - With 10 seconds remaining, it switches to flashing red.

And finally, there's an Adafruit miniPiTFT 1.3" display showing time and GPS status in the style of WOPR:

{{< figure src="./wopr-service-adafruit.jpg" alt="WOPR service Adafruit display HAT" width="700" height="430" class="insert-image" >}}

My goal? To have the most accurate clock at LTX.

And to do that, I didn't even have to use half the features of the Time Card mini!

  - With the full height bracket, I could plug in a pulse-per-second input and output, or even another external 10 Mhz clock reference!
  - I could pair the Time Card mini with a NIC with PPS input (e.g. Nvidia Connect-X 6, Intel i225, etc.) for datacenter-scale PTP services.
  - I could even set up the CM4 itself for hardware PTP timestamping—the NIC supports it, though probably only for a few hundred systems.
  - Plugging it into a PC would expose the CM4 serial console _and_ the U-blox directly to the host PC, making it easy to control without even going over the network (this is the first for a Pi-on-PCIe board, AFAICT).

For a deeper dive into my entire bringup experience—including testing the CM4 Pi OS image Timebeat maintains—check out [this issue on my Pi PCIe site](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/497).

To be completely transparent, Timebeat sent these to me for testing. I probably couldn't justify buying one just for the fun of it, and technically, just using NTP or an external GPS module alone would be plenty accurate for the purposes of a 1-hour livestream! (Just... a lot less fun).

Even so, this solution is cheaper than most dedicated time appliances.

## How it's made

For LTX 2023, I will be streaming from deep within the expo hall. Because I can't rely on GPS signals getting through, I'm powering the whole setup using a [12v 3000 mAh battery](https://amzn.to/3QgcrbU).

That's plugged into the CM4 IO Board, and the Time Card mini is plugged into the IO Board's PCIe slot (it doesn't require a Pi to be installed to provide power to the PCIe slot).

I rely on Timebeat's software to acquire the GPS signal and set the system clock (plus provide PTP out through the Pi's built-in Ethernet—should someone at LTX require it!). Then I wrote three small Python services to manage the Blinkstick and Adafruit display:

  - One service watches Timebeat to see if GPS time is locked in, and writes a file to the filesystem to indicate whether it is locked or not.
  - Another service prints text on the display: the time, and whether GPS time is locked in.
  - A third service manages the Blinkstick, changing colors at the proper times, dividing the hour up into 5 minute segments.

I don't know if I'll have a good time or a bad time, but I can guarantee I'll have the most _accurate_ time at LTX.

Unless I find someone carrying around a stratum 0 clock in their backpack...

All the code's open source in my [ltx2023 repo on GitHub](https://github.com/geerlingguy/ltx2023), and I include detailed setup instructions. Thanks to my [Patrons](https://www.patreon.com/geerlingguy) and [Sponsors](https://github.com/sponsors/geerlingguy), I can continue open sourcing all my work!

## Conclusion

LTX is just two days away. Make sure you sign up to get notified when our livestream begins!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/wHlJR6vpRkc" frameborder="0" allowfullscreen=""></iframe></div>
</div>

Chris (from [Crosstalk Solutions](https://www.youtube.com/channel/UCVS6ejD9NLZvjsvhcbiDzjw)) and I will interview:

  - Patrick from [ServeTheHome](https://www.youtube.com/channel/UCv6J_jJa8GJqFwQNgNrMuww)
  - Jake from [LTT](https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw)
  - Wendell from [Level1Techs](https://www.youtube.com/@Level1Techs)
  - Jeff from [Craft Computing](https://www.youtube.com/@CraftComputing)
  - Chris from [Chris Titus Tech](https://www.youtube.com/@ChrisTitusTech)
  - Quinn from [Snazzy Labs](https://www.youtube.com/@snazzy)
  - Brandon from [TechHut](https://www.youtube.com/@TechHut)
  - Colten from [Hardware Haven](https://www.youtube.com/@HardwareHaven)
  - and even Tim and Dan from LTT!

It's gonna be a blast, and we're hoping to raise some money for the [ITDRC](https://www.itdrc.org). Make sure to [watch the livestream on Saturday, July 29](https://www.youtube.com/watch?v=wHlJR6vpRkc)!
