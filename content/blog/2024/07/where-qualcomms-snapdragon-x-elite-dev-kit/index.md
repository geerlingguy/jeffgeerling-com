---
nid: 3391
title: "Where is Qualcomm's Snapdragon X Elite Dev Kit?"
slug: "where-qualcomms-snapdragon-x-elite-dev-kit"
date: 2024-07-19T14:04:14+00:00
drupal:
  nid: 3391
  path: /blog/2024/where-qualcomms-snapdragon-x-elite-dev-kit
  body_format: markdown
  redirects:
    - /blog/2024/what-happened-qualcomms-snapdragon-x-elite-dev-kit
aliases:
  - /blog/2024/what-happened-qualcomms-snapdragon-x-elite-dev-kit
tags:
  - arm
  - dev
  - linux
  - qualcomm
  - snapdragon
  - video
  - windows
  - youtube
---

> **Update - September 26**: Today my Dev Kit finally arrived! And of course, the first thing I did was tear it down—check out my [teardown photos of the Snapdragon Dev Kit internals here](/blog/2024/qualcomm-snapdragon-dev-kit-windows-teardown-2024).
>
> **Update 2 - October 17**: Today [Qualcomm cancelled all remaining orders, and will no longer support the Dev Kit](/blog/2024/qualcomm-cancels-snapdragon-dev-kit-refunds-all-orders).

I signed up to buy a Qualcomm Snapdragon X Dev Kit the second I found out about it. It's _supposed to be_ the [Mac mini killer for Windows](https://www.xda-developers.com/3-reasons-snapdragon-dev-kit-mac-mini-killer/).

{{< figure src="./snapdragon-dev-kit-transparent.jpg" alt="Snapdragon X Elite Dev Kit Transparent" width="700" height="auto" class="insert-image" >}}

They even promoted it with [this amazing-looking transparent shell](https://www.theverge.com/2024/5/21/24158603/qualcomm-windows-snapdragon-dev-kit-x-elite), and I and hundreds of other devs were ready to pony up the $899 Qualcomm was asking.

Their pre-order form said it would be out June 18. Almost exactly one month later, I got an email saying it was available. Great!

So I went to [the purchase page on Arrow](https://www.arrow.com/en/products/c8380-12c-mp-32g/thundercomm)... and it showed as out of stock. That was about 15 minutes after receiving the email.

There were three possibilities:

  - They vastly underestimated the demand, and/or there was a crush of orders immediately upon launch.
  - They didn't actually have any for sale yet.
  - They didn't coordinate with Arrow on the launch timing, so Arrow didn't show any stock yet.

In any case, I was surprised to see they had stock the next day (Tuesday). Well... at least it said "In stock: 1 part".

Since the order page said "Ships in 1 day", I placed an order, hoping to receive a dev kit by the end of this week.

I'm glad I didn't pay for overnight shipping, though, because Wednesday, the shipping date on my order slipped from Thursday to... June 12, **2026**! I bemusingly documented the saga on Twitter/X:

<blockquote class="twitter-tweet" data-conversation="none" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">lol 2026 estimated ship date now <a href="https://t.co/aZpRIuSHvW">pic.twitter.com/aZpRIuSHvW</a></p>&mdash; Jeff Geerling (@geerlingguy) <a href="https://twitter.com/geerlingguy/status/1813621844152619058?ref_src=twsrc%5Etfw">July 17, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

I'll update this post as the shipping date changes over time. As of late Thursday, Arrow's product listing says: "5 parts: Ships in 2 days", and my order now says "Est. Ship: 14 Aug 2024".

August is a _little_ more reasonable than 2026, but I wonder how many units Qualcomm produced, and whether they completely whiffed on their estimate of how many people would want a Snapdragon Dev Kit.

I originally planned on putting the X Elite through its paces in early July, measuring efficiency and testing Linux on it. [Linaro's been working on Linux support for the Snapdragon X](https://www.linaro.org/blog/qualcomm-and-linaro-enable-latest-flagship-snapdragon-compute-soc/), but according to the few people I've seen testing it on X Elite laptops, there are rough edges.

I posted a video testing some other things on Arm _Linux_, where I think hardware support and compatibility is in a better state than Windows on Arm, despite Microsoft's massive marketing campaign around 'Copilot Plus' and 'Redefining the PC'... you can watch that video here:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/thz5S_uciHk" frameborder='0' allowfullscreen></iframe></div>
</div>
