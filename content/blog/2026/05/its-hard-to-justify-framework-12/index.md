---
date: '2026-05-29T09:00:00-05:00'
tags: ['framework', 'laptop', 'review', 'macbook neo', 'apple', 'youtube', 'video']
title: "It's hard to justify buying a Framework 12"
slug: 'its-hard-to-justify-framework-12'
---
My nephew just graduated high school, and wants a laptop. When he decides what computer to buy, price (or more precisely, _value_) is the most important attribute.

Apple's MacBook Neo upended the 'value laptop' equation—Apple's not supposed to be both the cheapest option _and_ the best value... but it seems like that's squarely where the Neo landed for the good-but-cheap laptop category.

{{< figure
  src="./macbook-neo-and-framework-12.jpeg"
  alt="MacBook Neo on top of Framework 12"
  width="700"
  height="auto"
  class="insert-image"
>}}

My nephew is also my godson, and to kick off his computing journey, I thought I'd let him choose from a Framework 12 I bought to test, or the MacBook Neo I bought a couple months ago to use around the studio.

I had already put both laptops through my benchmark gauntlet, which revealed one theme: the Mac is faster (in most cases), more efficient, quieter, built better, has a much nicer display, and costs much less.

The Framework is more expensive, slower (in most cases), louder (its fan ramps up quite often), has a pretty poor display, but it _is_ a touchscreen, has a 360° hinge, and is more repairable and upgradeable[^upgradeable].

{{< figure
  src="./framework-12-vs-macbook-neo-features-price.jpeg"
  alt="MacBook Neo vs Framework 12 features and price"
  width="700"
  height="auto"
  class="insert-image"
>}}

The problem is, for an overall worse experience, are you willing to pay 20-40% more? Because that's the difference for the low-end Framework, which starts at $749 for a DIY edition (accounting for a used 8GB stick of RAM and a 256GB SSD), or $799 for a pre-built.

For students like my nephew, Apple offers up the base model Neo for $499.

I posted a video covering my experience with the laptop, and my nephew's decision to pick the Neo, over on YouTube:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/aPVAnwuSjfk' frameborder='0' allowfullscreen></iframe></div>
</div>

## Performance

I won't get into the full depth of my benchmarks here—for that, check out these issues:

  - [MacBook Neo benchmark results](https://github.com/geerlingguy/sbc-reviews/issues/102)
  - [Framework 12 - Intel i3 results](https://github.com/geerlingguy/sbc-reviews/issues/107)

But I will cover a few of the most telling results.

First, Geekbench 6 is terrible for larger systems, but is a decent proxy for real-world performance for systems with less than 16 cores. And the result shows how much faster Apple's low-end CPU cores are than Intel's:

{{< figure
  src="./framework-12-vs-macbook-neo-geekbench-6.jpeg"
  alt="MacBook Neo vs Framework 12 benchmarks - Geekbench 6"
  width="700"
  height="auto"
  class="insert-image"
>}}

The Neo is also silent throughout (owing to its lack of a fan), and for all tasks I tested, almost twice as efficient:

{{< figure
  src="./framework-12-vs-macbook-neo-hpl-cpu-efficiency.jpeg"
  alt="MacBook Neo vs Framework 12 - HPL Efficiency"
  width="700"
  height="auto"
  class="insert-image"
>}}

But there's one performance-related area where the Framework pulls ahead—a little—and that's sustained performance. When running a heavy workload like HPL (a FP64 HPC task, that taxes the CPU and RAM constantly for many minutes), the Framework's fans allow it to throttle less than the Neo.

{{< figure
  src="./framework-12-vs-macbook-neo-hpl-cpu.jpeg"
  alt="MacBook Neo vs Framework 12 - HPL Result"
  width="700"
  height="auto"
  class="insert-image"
>}}

Both reduce clock speed pretty quickly after the initial burst of work, but the Neo has to reduce its clock speed further since there's no fan to move heat away faster.

The Framework 12's fan will quickly ramp up to 100%, and at that level, it produces about 40-45 dBa of sound measured near the computer (versus nothing discernible over the 33 dBa noise floor of my studio). And even with the fan, it's not a big delta between the two.

The GPU fares poorly on Intel's side:

{{< figure
  src="./framework-12-vs-macbook-neo-gpu-gravitymark.jpeg"
  alt="MacBook Neo vs Framework 12 - GravityMark GPU result"
  width="700"
  height="auto"
  class="insert-image"
>}}

GravityMark is the best benchmark I've found to give raw GPU performance, but general UI responsiveness and things like 4K video playback weren't noticeably different between the two systems. It's only in gaming or GPU-accelerated compute tasks where you'd notice.

## It's hard to cost down

The build quality of the MacBook Neo is far above its price class—that's Apple's scale working in their favor. But it's obvious the Framework had to cut costs and compromise to hit their price and size targets:

  - The display's colors are noticeably off. It's better than $300 Chromebooks I use, but far behind the Neo.
  - It's thicker and heavier than the Neo, despite the screen being smaller. I do like the 16:10 aspect ratio.
  - The plastic top cover presses against the rubber feet when you fold the display in tablet mode, and I have to keep cleaning off dirt from that. Quite annoying, but I guess I'll have to get use to the patina.
  - The speakers are pretty bad. The Neo's speakers aren't amazing, but at least they don't eat up the entire low end of whatever you're playing (and have a better stereo image).
  - The webcam and mic are passable, and I really like the physical privacy switches for both. I wish more computers had that.
  - The biggest win is the modular ports. You can put four 'expansion modules' in the laptop, and get up to USB 3.2 Gen 2x1 performance out of each. The MacBook Neo just has 2 ports, and only one is USB 3.2 Gen 2x1.

{{< figure
  src="./macbook-neo-framework-12-screen-colors.jpeg"
  alt="MacBook Neo vs Framework 12 - display color rendition comparison"
  width="700"
  height="auto"
  class="insert-image"
>}}

I think Framework's in a hard place with the Framework 12. Because it's an odd dimension, and because they wanted a full 360° hinge for tablet mode, they had to compromise on the display.

They could've compensated by making the touchscreen and stylus functionality that much better, but [they're using older stylus tech](https://www.youtube.com/watch?v=STzF3xm-E_I), resulting in a worse tablet/drawing mode than what you'd expect on a modern iPad or Surface display.

My nephew chose the MacBook Neo, which I was using around the studio. It'll be interesting to see how well I adjust to using the Framework as my 'utility laptop'. I thought the tablet mode would be more useful, but after trying it that way, I realized a laptop-as-a-tablet is quite cumbersome.

As I mention in my video, the Framework 12 isn't a _bad laptop_, it's just a _bad value_, especially in comparison to the Neo.

Some of that is due to factors out of Framework's control[^control]. For now, I think Framework's 13" lineup is more compelling if you favor repairability/upgradeability and top-tier Linux support. (Lenovo seems to have [a good option](https://www.ifixit.com/lenovo) too, now.)

[^upgradeable]: While the Neo is probably one of the easiest Mac laptops to _repair_ in recent memory, the Framework 12 allows you to upgrade components including a DDR5 SODIMM, 2230-sized NVMe SSD, WiFi card, and even four modular ports around the sides. I outfitted mine with 2x USB-C, 1x USB-A, and 1x full-size HDMI.

[^control]: For example, because of their scale, Apple can convince a manufacturer to build a nice display exactly to their specification. Framework has to find an off-the-shelf component to fit their needs. This usually results in some compromise.
