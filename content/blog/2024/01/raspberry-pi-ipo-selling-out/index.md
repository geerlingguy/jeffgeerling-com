---
nid: 3343
title: "Raspberry Pi IPO: Selling out?"
slug: "raspberry-pi-ipo-selling-out"
date: 2024-01-31T03:37:17+00:00
drupal:
  nid: 3343
  path: /blog/2024/raspberry-pi-ipo-selling-out
  body_format: markdown
  redirects: []
tags:
  - arm
  - ipo
  - open source
  - pi 5
  - raspberry pi
  - sbc
  - video
---

{{< figure src="./pi-hundred-dollar-bill-8bit.png" alt="Raspberry Pi 5 blended into 100 dollar bill USD" width="500" height="auto" class="insert-image" >}}

[Raspberry Pi is looking into an IPO](https://www.bloomberg.com/news/articles/2024-01-29/raspberry-pi-picks-banks-for-ipo-choosing-london-over-new-york) (Initial Public Offering).

But wait, Raspberry Pi's a non-profit! They can't do that? And who would want stock in Raspberry Pi anyway? Their core market hates them—they abandoned hobbyists and makers years ago!

And there are like tons of clones and competitors, nobody even needs Raspberry Pi? Plus, aren't they crazy-expensive? It's like a hundred bucks now, and that's if you can even find one to buy!

Well, hold on a second... there are a _lotta_ misconceptions out there. In this post, I'll walk through what's actually happening, and also through things I see online.

> This blog post is a lightly-edited transcript of a video on my YouTube channel, which you can watch below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/hrhE6MnGi1A" frameborder='0' allowfullscreen></iframe></div>
</div>

## What Actually Happened Today

So first, what _actually_ happened today? Well, Eben Upton, who's the CEO of Raspberry Pi, told Bloomberg that Raspberry Pi's planning an IPO 'when the market for IPOs reopens'.

They're talking to banks in the UK, not the US, and that's a sticking point... apparently the markets haven't been as kind over the UK for IPOs. Many companies, even Arm—another Cambridge-based company—chose to list their stocks in the US instead.

Eben said the markets in London are in a good enough place that Raspberry Pi would be comfortable doing an IPO there.

When that happens, Raspberry Pi's ownership would be split up in the stock market, and earlier _private_ investors like [Sony](https://www.cnbc.com/2023/04/12/sony-backs-raspberry-pi-with-fresh-funding-access-to-ai-chips.html), [Arm](https://newsroom.arm.com/news/raspberry-pi-investment), and even the Raspberry Pi Foundation, would get large chunks of it.

The main takeaway is being a publicly-traded company creates different incentives.

You have less control, and certain things you do are goverened more by a board of directors or the public ownership at large. And the direction and control of a company is less about a small team of founders and more about... profit.

Now, do I think Raspberry Pi's going down the toilet? No. Definitely not in the short-term.

And the IPO might still never happen!

Back in late 2021, there were [rumors flying about an IPO](https://news.ycombinator.com/item?id=29392649), but that didn't pan out, and probably a good thing since Raspberry Pi had trouble even making their tiny single board computers for a few years!

But regardless, the fact that Raspberry Pi is turning more corporate means changes will happen, one way or another.

I think for many of us, who followed along in the first few years, when the first Pi was hacked together and brand new, it's the death of that original ragtag idea that hurts.

Right now, Eben Upton is still CEO. And in an [interview with the Register](https://www.theregister.com/2024/01/30/raspberry_pi_ipo/), he even said "we'll keep doing the same stuff, Certainly while I'm in charge." I have no reason to believe he's lying.

The Compute Module 5 is right around the corner. And they could probably knock out a really cool iteration on the Pi 400 if they just put in a Pi 5 and an NVMe slot. And maybe gave us a nicer keyboard—I can dream, can't I?

But long-term, will Eben's vision for what makes Raspberry Pi change? Will there be turnover and some of the people who make the Pi a joy to use be gone?

Will the software side start leaning on subscriptions to increase revenues to make shareholders happy?

And ultimately, could Eben be replaced, and would that change things? Yes, probably, but I won't speculating about any that here. See my [blog post about enshittification](https://www.jeffgeerling.com/blog/2023/forget-spaceships-i-just-want-my-music) from last month if you wanna read more about that topic.

What I will do is answer some misconceptions I've seen about Raspberry Pi and the IPO.

## Misconceptions

First of all, Raspberry Pi is _not_ a nonprofit. Well... actually it is. And it isn't. Let me explain.

[Raspberry Pi _Trading_](https://www.raspberrypi.com) is a for-profit company in the UK that designs and manufacturers all the hardware.

And the [Raspberry Pi _Foundation_](https://www.raspberrypi.org) is a charity to help young people get into computing.

If you visit their website, you'll see the mission is entirely different. Now, they _are_ related. And if you look at the [Foundation's governance](https://www.raspberrypi.org/about/governance/), you'll see there are some of the same people too.

Does that make the Pi Foundation shady? No. They do a lot of great things, one of my favorite is the [Astro Pi challenge](https://astro-pi.org), where kids can get their code to run on a Pi in _space_.

But they are different entities and have been since pretty much the beginning. Does the Foundation stand to profit from Raspberry Pi Trading's IPO? Probably. I mean [almost ten million pounds of their 2022 income](https://static.raspberrypi.org/files/about/RaspberryPiFoundationAnnualReview2022.pdf) came out of Raspberry Pi Trading's profits.

Regardless, Raspberry Pi _Trading_, the for-profit wing, is the one that would be going public.

Another thing I've heard is the Raspberry Pi's too expensive now, and nobody outside of industrial customers are even buying it.

That's... I mean I don't know what planet these people are on, but the Pi 5 has been sold _exclusively_ to individuals for the past few months, and every batch sells out quickly. By my estimates, we're around half a million Pi 5s sold already, and judging by people's posts on social media, it's not just faceless corporations and scalpers buying them all.

But yes, the Pi 5 is the most expensive Pi yet. I even wrote _last week_ about how for desktop computing, [it probably doesn't make much sense](/blog/2024/when-did-raspberry-pi-get-so-expensive), especially with low-end mini PCs coming down in price.

That doesn't mean the Pi is too expensive, though. The Pi Zero 2 W is probably the absolute perfect Pi for so many use cases where the Pi makes sense—that is, when you need more compute than a microcontroller, but less than a desktop, and you want a board that's less than $20.

Plus, the Compute Module 5 is on the way, according to Eben, and the CM4 is _still_ selling out all the time, since so many projects use it.

Now, there is a nugget of truth in the accusation that Raspberry Pi sold out hobbyists and makers. They do have some responsibility there, and I think for a _lot_ of us, _myself included_, it's meant spending a lot more time trying out other boards.

Like last year I spent a fair bit of time with the [Rock 5 B and Orange Pi 5](/blog/2023/rock-5-b-not-raspberry-pi-killer-yet), and I did a whole video [testing almost a dozen Compute Module 4 clones](https://www.youtube.com/watch?v=KghZIgkKZcs).

But Raspberry Pi is still in a much better position, even if you're just an individual maker, and even if you had to wait to buy one.

Does that mean I think Raspberry Pi will always be king? No. They might, but I keep asking: why have none of the other companies focused on the things that _matter_ long-term—like good support for a board—even a couple years after release?

Heck, [Raspberry Pi OS](https://www.raspberrypi.com/software/) is _still_ supported on the _original_ Pi, more than a _decade_ later!

That kind of support earns loyalty, and community support like what [Armbian](https://www.armbian.com) does for some boards is awesome, it just doesn't mean the same thing.

Another thing I see is this refrain that Raspberry Pi was open source, but now they're not, or that their open source nature was their only competitive advantage.

First of all, they were never open source, at least the hardware. They do have a more open nature to them, but you can't just grab their RP2040 design and fab your own chip. And don't get me started on Broadcom's chips.

I don't begrudge hardware manufacturers, and I would love to see more true open source hardware. But even if you love Rockchip and ESP32 devices, you have to realize that all these hardware manufacturers have proprietary bits somewhere in their stack.

The more open, the better, but I won't hold my breath to wait for 100% open-source-hardware rolling out in a competitive single board computer design.

## Summary

So a Raspberry Pi IPO. I'm disappointed, but not surprised. And there's always the possibility more money and public markets make things _better_. But that'd be a pretty optimistic take, and would be counter to all my instincts seeing other IPOs over the years.

I don't think this changes anything in the short term. And an IPO would definitely change the _character_ of Raspberry Pi. But there's still hope it doesn't ultimately kill off the things we love about Pi.

And heck, it just extends the opportunity for _any_ of Raspberry Pi's competition to do better. I'm still waiting for a true Raspberry Pi killer, but until then, I'm happy using a Pi in my projects.
