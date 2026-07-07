---
date: '2026-07-08T09:00:00-05:00'
tags: ['raspberry pi', 'pi 4', 'youtube', 'video', 'dram', 'shortage', 'binning']
title: 'The Special Value Pi 4 was extremely short-lived'
slug: 'special-value-pi-4-extremely-short-lived'
---
{{< figure
  src="./special-value-pi-4-4gb.jpg"
  alt="Special Value Pi 4 4GB in hand"
  width="700"
  height="auto"
  class="insert-image"
>}}

The 'Special Value' Pi 4 pictured above is probably the rarest Raspberry Pi I own—even rarer than my [blue special edition Pi](/blog/2025/limited-time-flavor-blue-raspberry-pi/).

A Raspberry Pi reseller [briefly listed a special 'value edition' Pi 4](https://www.cnx-software.com/2026/06/26/discounted-1-25-ghz-raspberry-pi-4-model-b/). But the product page 404's now. While it was up, my curiosity got the better of me, and now I have two 'value' Pi 4s.

What makes them a 'value'? They're only certified to run at 1.25 GHz (retail Pi 4s run at 1.8 GHz, and can usually be overclocked).

The price for the 4GB edition was $89—before shipping and tariffs. All-in, I paid $160 to get it to my door. If I run over to Micro Center and grab a 4GB Pi 4 off the shelf, it's just [$94.99 plus tax](https://www.microcenter.com/product/637834/raspberry-pi-4-model-b). [What a savings](https://www.youtube.com/watch?v=oewMbg8wFQU)...

> **Note**: The 1 GB Pi 4 is still $35, at least at Micro Center — however, higher-memory SKUs have gotten eye-wateringly expensive, with the 16GB Pi 5 hitting $299!

But what do you get, when you buy the world's slowest Pi 4?

_This blog post is a lightly-edited transcript of the following video:_

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/o4Lcg3YBYzg' frameborder='0' allowfullscreen></iframe></div>
</div>

## Inspecting with camera closeup

Comparing it closely with one of my retail Pi 4s, I couldn't find _any difference at all_. The main chip markings are the same, the board is marked the same, both are made in the UK...

{{< figure
  src="./special-value-pi-4-8gb-comparison.jpg"
  alt="Special Value Pi 4 to the right of an older retail Pi 4"
  width="700"
  height="auto"
  class="insert-image"
>}}

The only discernible difference is the LPDDR4 DRAM package, which is different because Raspberry Pi's had to scramble (like everyone else in the hardware business) to find stock for new boards. (Even with older hardware, I've seen Pis use multiple RAM vendors, so this isn't a big deal.)

The 8GB model had an older [B0 stepping](/blog/2021/raspberry-pi-4-model-bs-arriving-newer-c0-stepping/), which is the same as my oldest retail Pi 4s, but there's still B0 stock here and there.

Externally, there's _nothing_ different about these 'value' boards. That's probably why the listing was pulled.

Could you imagine, people buying up binned Pis, _some which could actually run at 1.8 GHz, but were never validated for that clock speed_, and then reselling them as normal Pis? Not great for the end user.

## Benchmarking - Power and Performance

I didn't know what to expect booting one up, but I put Pi OS on a microSD card, and it booted right up, and ran at 1.8 GHz.

{{< figure
  src="./special-value-pi-1.8ghz-btop.jpg"
  alt="Special Value Pi 4 running without issue at 1.8 GHz"
  width="700"
  height="auto"
  class="insert-image"
>}}

I don't know what I was expecting, but certainly not for it to run at 1.8 GHz. Maybe that's a lesson that even if something's binned, that doesn't mean it can't run _at all_ at the higher clocks, just that it didn't pass whatever validation Raspberry Pi runs at the factory.

{{< figure
  src="./special-value-pi-8gb-kernel-panic.jpg"
  alt="Special Value Pi 4 8GB kernel panic at bad clocks"
  width="700"
  height="auto"
  class="insert-image"
>}}

So I plugged in the 8 GB, and in this case, I got kernel panics and clock speed errors. I modified the Pi boot config to force the arm cores to 1.25 GHz, and it booted up fine.

Running at that speed, everything worked, just... slightly slower than a regular Pi 4.

Power consumption was different than expected, though. This Pi used _3W_ at idle. Most Pi 4's I've tested idle at less than 2W.

To find out why, I asked a Pi engineer.

## Binning for Industry

He said they ['bin' hardware](https://en.wikipedia.org/wiki/Product_binning), something every manufacturer does. He said less than .01% of Pis they build don't test at normal voltages and frequencies, so they put them aside.

It sounds like they can separate those out and sell batches to specific industrial customers **who know what they're getting into**. That saves them from e-wasting small batches of failed Pis, and gives some partners a slight discount.

But for every Pi, there's dynamic adjustments to the chip voltage, that's part of DVFS, or [Dynamic Voltage and Frequency Scaling](https://chipress.online/2024/11/04/what-is-dvfs-what-is-avfs/). For lower-binned chips, the Pi might actually need to _raise_ the voltage to hit acceptable performance, even at lower clock speeds (thus higher power draw at a given clock).

For better chips, they can run at default clocks using even a little less power. Using DVFS, the Pi's firmware can normalize the performance across all Pis. So even with retail Pis, one Pi might be _just slightly_ more efficient than another.

That's why _some_ of my Pi 5s [I can overclock to 3 or even 3.4 Gigahertz](/blog/2024/hacking-pi-firmware-get-fastest-overclock/). But other ones can't even get to 2.6. It's just the silicon lottery, and this strange Pi gave me a peek behind the scenes into one area of parts binning I never thought about.

I have [all my benchmarks up on GitHub](https://github.com/geerlingguy/sbc-reviews/issues/110) and I'll link to them below, but all that to say, I'm not a silicon engineer, so take everything I'm saying here with a grain of sodium chloride.
