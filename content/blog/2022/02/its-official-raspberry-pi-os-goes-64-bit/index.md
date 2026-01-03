---
nid: 3176
title: "It's official: Raspberry Pi OS goes 64-bit"
slug: "its-official-raspberry-pi-os-goes-64-bit"
date: 2022-02-03T19:35:32+00:00
drupal:
  nid: 3176
  path: /blog/2022/its-official-raspberry-pi-os-goes-64-bit
  body_format: markdown
  redirects: []
tags:
  - 64-bit
  - arm64
  - linux
  - raspberry pi
  - video
  - youtube
---

64-bits. More is always better, right?

Well, not exactly. And that's why it's taken years for Raspberry Pi OS to add an officially-supported 64-bit version, in addition to the 32-bit version they've had since the original Pi came out.

Since [May 2020](https://forums.raspberrypi.com/viewtopic.php?t=275370), there's been a beta 64-bit version of Pi OS, but it wasn't intended for beginners, and was never linked from the main downloads page.

You had to kinda be 'in the know' to get it. And the reason for that is it's actually branched directly off of Debian Linux and had a few growing pains. But almost all those problems have been ironed out now, and apparently it's time for the Raspberry Pi's 64-bit era.

{{< figure src="./pi-os-64-bit-blog-post.png" alt="Raspberry Pi OS 64-bit blog post" width="700" height="394" class="insert-image" >}}

Yesterday Raspberry Pi [announced the 64-bit version is finally official](https://www.raspberrypi.com/software/operating-systems/). It's no longer hidden away in a crusty forum link, it's linked straight from their public downloads page and the Raspberry Pi Imager. Check out [this video from leepspvideo](https://www.youtube.com/watch?v=oSVnsqX_8iw) for a guide on how to get it installed on your Pi.

The 32-bit image is still listed first because it's still compatible with _every_ Raspberry Pi ever made—including this ancient first generation model B!

{{< figure src="./raspberrypi-gen-1.jpg" alt="Gen 1 Raspberry Pi model B" width="700" height="448" class="insert-image" >}}

And it probably won't go away for a while either, because Raspberry Pi still supports the Compute Module _1_, which has the same processor, and that'll be [supported until the end of 2026](https://www.raspberrypi.com/products/compute-module-1/)!

The 64-bit release is only compatible with more recent Pis, like the Pi 3 and Pi 4 generations, as well as the Pi Zero 2 W.

## 64-bits, why?

But what are some reasons you might wanna run 64-bit Pi OS? Well, since I've been running it on all my Pis since spring last year, I'll tell you why _I_ run it.

### RAM

The first reason has to do with RAM.

If you have less than 4 gigs of RAM, then memory isn't a huge concern and the 32-bit OS should run fine.

But 32-bit OSes can't address more than 4 gigabytes of RAM without some weird hacks like the one Pi OS uses, called [Large Physical Address Extension](https://en.wikipedia.org/wiki/ARM_architecture#Large_Physical_Address_Extension_(LPAE)). That allows the full 8 gigs to be addressed, but only up to 4 gigabytes for any single process, like a Chromium browser tab. That means for _most_ applications, RAM is a non-issue.

But there are some cases, especially with servers or things like data processing, where one process could use more than 4 gigs, and in those cases, you should definitely use the 64-bit OS.

And for most people running a 64-bit OS won't cause any problems, except for maybe gobbling up a little extra RAM. You might not realize it, but 64-bit memory addresses actually take up a little more space than 32-bit addresses, meaning you have a little less free RAM when you run a 64-bit OS.

It's not a _huge_ difference, but I tested both Lite images on my Pi Zero 2 with its measly 512 MB of RAM, and I saw 66 MiB used on the 64-bit OS, but only 48 MiB on the 32-bit OS. That's a 32% difference! So if you run heavier apps, the total memory usage will be a little higher when you run it on a 64-bit OS.

I think that's the main reason why the 32-bit Pi OS is still listed first—Raspberry Pi doesn't want people running out of memory on their newest Pi, the Zero 2 W, which only has 512 MB of RAM!

So RAM could be a factor depending on what you run on your Pis, and which Pi you run, but that's not the primary reason _I_ run the 64-bit version.

### Software compatibility

The biggest reason is software compatibility.

Outside the Pi and embedded computer ecosystems, almost _nobody_ runs 32-bit operating systems anymore. Because of that, almost all modern software is built for 64-bit. Some software is _also_ built for 32-bit, but it only runs because of dedicated support from Pi users or maintainers who still care about 32-bit support.

The problem is supporting 32-bits gets harder every year, especially as modern software uses optimizations and libraries that might not even be _tested_ on 32-bit processors!

As a concrete example, you [can't install Elasticsearch anymore](https://www.docker.elastic.co/r/elasticsearch) on 32-bit Pi OS.

So moving to a 64-bit operating system means a lot more things, from downloadable apps to Docker images, run without any changes.

I think more and more projects that have been maintaining 32-bit support will probably drop it as users transition to 64-bit Pi OS.

### Performance

The last reason I prefer the 64-bit OS is because some of the software I run uses optimizations that are only available on the newer processor architecture.

For example, the [A64 instruction set](https://developer.arm.com/architectures/instruction-sets/base-isas/a64) has more and wider registers, and has some new instructions that can speed up certain operations quite a bit.

{{< figure src="./bcm2711-macro.jpg" alt="Broadcom BCM2711 on Raspberry Pi 400 Computer Board - Macro" width="700" height="468" class="insert-image" >}}

The fastest chip currently used by Raspberry Pi, the BCM2711 pictured above, doesn't support _everything_, though. Cryptography-related extensions aren't built into this chip. But for some specific things, you can get 5-30% faster performance just by running an application with the 64-bit version.

Some 64-bit ARM instructions are even better for energy efficiency, too, so you get better performance _and_ use less power doing it!

But day-to-day use like booting up your Pi, browsing the web, or editing a document won't see any impact. But for people like me who run their Pis as servers, and run things like Kubernetes and network utilities, it can make things a lot more efficient.

## Issues with 64-bit Pi OS

{{< figure src="./disney-plus-widevine-not-supported.jpg" alt="Disney+ warning when Widevine and 64-bit Chromium is not working on Raspberry Pi" width="700" height="379" class="insert-image" >}}

But running 64-bit Pi OS isn't all rainbows and butterflies, at least not yet. There are still a few issues, for example, Widevine DRM is currently incompatible with the 64-bit build of Chromium. So if you wanna watch Netflix or Disney+ on your Pi, you have to manually install the 32-bit version of Chromium on 64-bit Pi OS. The Pi blog post has instructions for doing that.

Though, to be honest, maybe broken DRM's a good excuse to protest DRM and find some other source of entertainment.

There are also hardware video acceleration issues with 64-bit Pi OS that might slow down video playback in some cases, but hopefully those'll be resolved soon.

## Conclusion

In the end, I'd say basically if you run a modern 4th-generation Raspberry Pi, like the Pi 4 model B, Pi 400, or Compute Module 4, go ahead and use the 64-bit Pi OS. The downsides are minimal for almost everyone, and the wider usage will hopefully lead to the final major bugs being squashed once and for all.

Moving forward, the 32-bit Pi OS will probably stick around until at least 2026, but then my new question is, when will it switch places on the download list, making 64-bit the default? After all, if there are ever new Pis with even more RAM or a newer processor and more ARM 64-bit-only instructions, the 32-bit OS will become even more slow and more irrelevant!
