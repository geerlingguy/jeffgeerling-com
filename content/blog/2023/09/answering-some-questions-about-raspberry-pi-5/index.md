---
nid: 3314
title: "Answering some questions about the Raspberry Pi 5"
slug: "answering-some-questions-about-raspberry-pi-5"
date: 2023-09-28T15:37:46+00:00
drupal:
  nid: 3314
  path: /blog/2023/answering-some-questions-about-raspberry-pi-5
  body_format: markdown
  redirects: []
tags:
  - linux
  - pcie
  - pi 5
  - raspberry pi
  - usb-c
---

It's less than 12 hours since the Pi 5 launch, and already there's a few hundred questions whizzing about—I thought I'd answer some of the things I see people asking most frequently, like:

### Does the new Case have room for the Active Cooler, or other Pi HATs?

{{< figure src="./pi-case-active-cooler.jpeg" alt="Raspberry Pi 5 case with active cooler" width="700" height="467" class="insert-image" >}}

Yes, indeed it does! You can pop out the fan bracket in the new Case, and fit many normal-size Pi HATs. This is useful also if you want to stack cases—assuming the HAT has mounting points, you could put some spacers in and stack another Pi or Pi + Case on top!

### Have you tested [insert PCIe device here] yet?

Yes, check out my earlier post [testing various PCIe devices on the Pi 5](/blog/2023/testing-pcie-on-raspberry-pi-5).

### Will there be an official M.2 NVMe SSD HAT?

It looks like the answer is yes—sometime in early 2024, if [Raspberry Pi's official blog post](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/) is any indication:

> From early 2024, we will be offering a pair of mechanical adapter boards which convert between this connector and a subset of the M.2 standard, allowing users to attach NVMe SSDs and other M.2-format accessories. The first, which conforms to the standard HAT form factor, is intended for mounting larger devices. The second, which shares the L-shaped form factor of the new PoE+ HAT, supports mounting 2230- and 2242-format devices inside the Raspberry Pi 5 case.

### Have you compared the Pi 5 to Orange Pi 5?

Yes, also the Rock 5 B—see the comparisons in the [performance section of my Pi 5 video](https://youtu.be/nBtOEmUqASQ?t=486). It is about as fast for PHP and media encoding, but the RK3588 and RK3588s (with their four additional Arm A55 cores) smoke the Pi in many compute-heavy benchmarks.

### Can you explain more of the PCIe, USB, and peripheral architecture?

Yes, for starters, check out my [Pi 5 issue on my sbc-reviews project on GitHub](https://github.com/geerlingguy/sbc-reviews/issues/21), there is active discussion there with all the gory details.

The RP1 chip uses four PCIe Gen 2 lanes off the BCM2712, and the external PCIe FPC connector exposes an additional Gen 2 lane off the BCM2712. The user has control over that lane and can uprate it to Gen 3 (10 GT/sec) if they so choose.

The USB-C port used for Power Delivery also supports USB OTG at USB 2.0 speeds (though I haven't had time to test it out yet—it should work similar to the Pi 4, though power delivery through that port can be interesting.

### Does the USB-C port negotiate PD at 9V or 12V?

No, only 5V, and I've tested 5V at 5A (using the official Pi USB-C PD PSU), and 5V at 3A (using the official Pi USB-C 3A PSU).

{{< figure src="./radxa-usb-c-pd-pi-5-power-adapter.jpeg" alt="Radxa USB-C PD 30W and Pi 5 Power adapter PSU" width="700" height="467" class="insert-image" >}}

I also tested the [Radxa USB-C PD 30W power adapter](https://docs.radxa.com/en/accessories/pd_30w), which says it will output 5V at 5A, but the Pi only negotiates 3A with it right now. I've been in contact with Pi engineers and it seems like they have one on the way to test to see why it's not negotiating more.

I should also note the official adapter lists 12V at 2.25A output as an option, so maybe some future Pi could take that and run with it, for increased compatibility with more USB-C PD adapters (5V at 5A is a rarely seen, though it's an option in the spec).

{{< figure src="./kill-a-watt-pi-5-idle-1.8w.jpg" alt="Kill-A-Watt Pi 5 idle power consumption" width="700" height="468" class="insert-image" >}}

### Do you have any numbers for performance?

Yes, check out the [sbc-reviews Pi 5 issue](https://github.com/geerlingguy/sbc-reviews/issues/21) for specific numbers, and also see the links in that issue to a top500 HPL benchmark result, Geekbench 6 results, and more.

### Do you have any numbers on energy efficiency?

Yes, in fact—check out the [sbc-reviews Pi 5 issue](https://github.com/geerlingguy/sbc-reviews/issues/21) for specific numbers, but I should add a few caveats:

  1. I was testing mainly with the Pi 5V/5A PSU, Pi 5V/3A PSU, and Radxa 30W PSU. With each, idle power consumption as measured at the wall differed by as much as 1W. My 1.8W idle result came from the official 5A PSU and a Kill-A-Watt. With the Radxa PSU I was seeing as much as 3W idle.
  1. I don't currently have a high quality inline USB-C PD-aware analyzer, but my little cheap chinesium one reported 2-3W idle power use (even while the Kill-A-Watt reported 1.8-2W).
  1. At all power levels, the Pi 5 can perform more using less energy than a Pi 4 at anything besides pure idle.
  1. I have only tested overclocking in a very rudimentary manner, bumping my Pi to 2.6 and 2.8 GHz. Both worked, but 2.8 GHz got a little unstable.
  1. Users who care more about idle power consumption, and who don't need to run performance-heavy workloads may be better served with a Pi 4, Pi 3, or Pi Zero 2W instead. Heck, if you can run it on a Pico or Arduino, you'll save even more mW :)

### Is there any hardware video encoding support?

No. Raspberry Pi recommends software encoding, and in my testing, I could get decent enough data rates for H.264 in HD resolutions, but 4K bogged down a bit.

The [libcamera encoder app](https://github.com/raspberrypi/libcamera-apps/blob/1c1d1c1a2a86d70cf873edc8bb72d174f037973a/encoder/libav_encoder.cpp#L33) includes a preset with defaults Pi engineers have chosen for their efficiency on the BCM2712; it should encode 1080p60 using about 25% CPU load.

4K60 HEVC (H.265) _decoding_ is hardware-accelerated, though.

_I will be updating this post throughout the day as more questions roll in._
