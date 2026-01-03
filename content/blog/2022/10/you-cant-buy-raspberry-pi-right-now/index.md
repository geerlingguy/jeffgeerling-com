---
nid: 3240
title: "You can't buy a Raspberry Pi right now"
slug: "you-cant-buy-raspberry-pi-right-now"
date: 2022-10-03T15:20:47+00:00
drupal:
  nid: 3240
  path: /blog/2022/you-cant-buy-raspberry-pi-right-now
  body_format: markdown
  redirects: []
tags:
  - livestream
  - parts shortage
  - raspberry pi
  - sbc
  - video
---

...or at least, not without a _lot_ of patience or a fat wallet.

{{< figure src="./raspberry-pi-scalping-ebay.jpg" alt="Scalping Prices of the Raspberry Pi on eBay" width="700" height="394" class="insert-image" >}}

But _why_? And are there any signs Raspberry Pis will become available to the general public again soon?

To be clear, I'm speaking of the _mainstream_ SBC Raspberry Pis, like the Pi 4 model B, the Compute Module 4, the Pi Zero 2 W, and even in many cases the Pi 400. The Pico and Pico W are both readily available, at least in most markets where I've looked (local shortages always exist, but typically not for months or _years_ like with full-size Pis).

A service has even been set up since early this year just to scan different vendors to find when Pis are in stock, and alert people via Twitter and other means. Long-time followers of [rpilocator.com](https://rpilocator.com) know how short-lived Raspberry Pis are at official retailers like Adafruit and Pi-Shop, even with purchasing limitations in place.

Sadly, the only _reliable_ way to buy a Pi immediately is to pay scalping prices on eBay or buy bundles that include often-unneeded components to pad out the price of a normally-$35 Pi to $100 and beyond.

## Why?

The big question is: _why_?

Well, two reasons:

  1. Raspberry Pi is one of the few SBC vendors (maybe the _only_ one) to tackle the most important feature for adoption and ongoing end-user happiness: **support**.

     Instead of throwing hardware at the wall, seeing what sticks, and relying on developer communities to support their hardware with distributions like [Armbian](https://www.armbian.com), Raspberry Pi actively supports their boards, all the way back to the original Pi model B. They ship Raspberry Pi OS. They continually improve their [documentation](https://www.raspberrypi.com/documentation/) and focus on a great end-user experience for beginners and advanced users.
  2. Production limitations because of the global components shortage.

And because of the second point, Raspberry Pi can produce a limited number of Pi models based on the Broadcom BCM2711 SoC. This is the same issue [plaguing car manufacturers](https://www.carsdirect.com/deals-articles/latest-new-car-chip-shortage-updates). Even behemoths like [Nvidia, Intel, AMD, and Apple](https://www.datacenterdynamics.com/en/news/tsmc-intel-and-nvidia-warn-of-years-of-chip-shortages/) are still being affected.

{{< figure src="./bcm2711-closeup-pi-400.jpeg" alt="Raspberry Pi 4 BCM2711 SoC" width="700" height="468" class="insert-image" >}}

Because of the shortages, Raspberry Pi have not been able to increase production to meet demand, therefore they have to prioritize where the Pis they make go... and right now they are still prioritizing OEM partners over end-user retailers like Adafruit, PiShop.us, Micro Center, and other retailers selling individual units.

This is far from ideal, and many in the maker/hacker community (myself included) feel betrayed by an organization that grew quickly based on the grassroots adoption of the Raspberry Pi since 2012.

How many of the commercial and industrial users of the Pi would be incorporating it into their products (thus depending on Pi stock for their own survival) without the huge community of individual developers, makers, hobbyists, and educators who made the Raspberry Pi as popular as it is today?

## Official response from RPi

With all this in mind, and since there hasn't been an official update since [Eben Upton's post on the Raspberry Pi blog in April](https://www.raspberrypi.com/news/production-and-supply-chain-update/), I asked directly about the shortage. Eben said, basically:

  - Everything in the April blog post is still valid
  - They are still supply constrained
  - They are still prioritizing OEM customers (who have built their products around the Pi)
  - They are [ring-fencing](https://www.merriam-webster.com/dictionary/ring-fence) some supply for customers (they did not mention how many, exactly)
  - They set up a new process to ensure the OEM's they're supplying aren't scalping the boards
  - Any OEM who is not getting the Pis they need should email [business@raspberrypi.com](mailto:business@raspberrypi.com)
  - Raspberry Pi's main goal during the shortage is to not let companies that rely on Raspberry Pi to die.
  - They are currently producing _400,000_ Raspberry Pis per month.

And finally, they wanted to make clear their main point of differentiation in the SBC space:

> We value our approach to software support, maintenance and quality over and above everything else. You can be confident that our software will run on all Raspberry Pis even those now over ten years old, and it is still being updated!

Indeed, that's why people pay double, or even _triple_, the MSRP for a used Raspberry Pi. For some projects, getting things running on the Pi (and knowing they'll have software updates for _years_) is still much easier than doing the same on another SBC.

And though the Pi 4's BCM2711 is getting long in the tooth—most competing boards are already far surpassing it in CPU, memory, and IO performance—it is still a great option for energy-efficient computing and certain edge use cases.

## Raspberry Pi Alternatives

But because the Pi is now _realistically_ a $100 computer (for the time being), people have started considering alternatives.

If you want a slightly faster and more generic computer, buying a used 'one liter' PC (one of those little PCs you see strapped to a monitor at a doctor's office) can get you something on par with—or faster than—a Pi 4 for less than $80, or cheaper if you get lucky. But these PCs lack some features like GPIO or any kind of HAT compatibility, so are only an option if you use the Pi as a generic computer.

If you want a comparable SBC with features like GPIO and a faster CPU and GPU, with native SATA ports or other more exotic features, Khadas, Radxa, OrangePi, and other vendors have made some great hardware over the past two years, with many options under $100.

But getting started with a Pi clone can be daunting—unlike the first-time experience with a Pi, where you have helpful [Getting Started Guide](https://www.raspberrypi.com/documentation/computers/getting-started.html) and a plethora of blog posts, videos, and books available, you may encounter a sparse documentation page (if anything) pointing you to an ISO download and telling you to flash an image to a microSD card.

Where Raspberry Pi assumes nothing and guides you along every step, most other manufacturers assume you're familiar with SBCs, flashing ISOs, and quite possibly debugging problems over a USB serial connection!

## Some Alternatives Work Fine

That's not always the case, and I was pleasantly surprised by BigTreeTech's new CB1 board (a clone of the Compute Module 4, running an Allwinner H616 SoC). Check out my experience with that board in my recent livestream:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/Krpac-MaD5s" frameborder="0" allowfullscreen=""></iframe></div>
</div>

But the CB1 is an outlier in my experience. Almost every non-Pi board I test requires more work than just 'download ISO, flash it, and the SBC boots and works'. Some images don't have basic functionality like HDMI or networking, and sometimes you can't even find an image with a modern and secure Linux OS, only Android images (which is unhelpful for general use).

I'm not saying you should avoid alternate SBCs, but don't expect the same level of user experience and support you get with a Raspberry Pi.

In the end, I will echo what I've recommended before:

  - If you need a Raspberry Pi, either be patient and keep checking [rpilocator.com](https://rpilocator.com), or if the need is more urgent, consider emailing [business@raspberrypi.com](mailto:business@raspberrypi.com).
  - If you're considering an alternative, know that the experience may not be as simple, but try to get an idea of what you're getting into by finding reviews from others to make sure the board will solve the problems you have first.
  - The shortage likely won't let up this year. I'm still hopeful it will relax in 2023, but who knows what the future holds.
