---
date: '2026-08-07T09:00:00-05:00'
tags: ['dell', 'xps', 'macbook neo', 'apple', 'efficiency', 'youtube', 'benchmark', 'hpl', 'intel', 'laptop', 'reviews']
title: "I'm excited for Intel after testing the XPS 13"
slug: 'excited-for-intel-efficiency'
# description: 'description_here'
---
Shortly after Apple launched the [MacBook Neo](https://github.com/geerlingguy/sbc-reviews/issues/102), upending the expectation of what you get in a 'budget laptop', Dell announced the [XPS 13](https://www.dell.com/en-us/shop/dell-laptops/new-xps-13-laptop/spd/xps13dx13260laptop).

TODO: Photo here.

Matching the Neo's _current_ pricing, it starts at $699, or $599 with an educational discount. That discount is currently set to expire on November 2, and with the current component pricing insanity, I'd be surprised if we don't see a price increase in general by the end of the year.

But I spent some time using the XPS 13, and ran it through my [gauntlet of benchmarks](https://github.com/geerlingguy/sbc-reviews/issues/111). I published a review of the XPS 13 itself on my YouTube channel:

<div class="yt-embed">
  TODO: Video here
</div>

Some headline improvements over the Air, in case you're wondering:

  - Higher-resolution touchscreen display, with a more matte finish
  - Backlit keyboard (includes a CoPilot button, ick)
  - Both USB-C ports are 10 Gbps with DisplayPort and PD
  - Base storage is 512GB, the included SSD is faster than the Neo's built-in storage, _and it's upgradeable_ (2230-sized NVMe).
  - Linux support is specifically not advertised, but I was able to get all hardware functionality working in Fedora 44, including WiFi 7 (I had to plug in a USB Ethernet adapter temporarily to run `dnf upgrade`)

A few things are worse, of course:

  - The top-hinge trackpad makes it hard to click anywhere besides the bottom
  - The built-in webcam and microphone are a bit lower quality
  - Sound from the built-in speakers is noticeably worse
  - There's no headphone jack
  - It only _officially_ supports Windows 11, and comes with _Home_

Watch the video for opinions on the laptop itself.

In this blog post, I thought I'd dive deeper into the most interesting part _for me_: the Intel Core 5 320.

## Intel Core 5 320

Intel's had a string of decent low-end SoCs, incorporating a CPU, GPU, and more recently, NPU, along with a decent amount of IO.

At the lowest end, the N150 and N350 match or surpass even midrange Arm SoCs, while keeping wide x86 compatibility Intel's known for.

TODO: Photo here.

TODO.

## Power Efficiency

TODO.

## Conclusion

TODO.
