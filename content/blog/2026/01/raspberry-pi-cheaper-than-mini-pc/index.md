---
date: '2026-01-05T16:00:00-06:00'
title: "Raspberry Pi is cheaper than a Mini PC again (that's not good)"
slug: 'raspberry-pi-cheaper-than-mini-pc'
tags: ['raspberry pi', 'pi 5', 'mini pc', 'gmktec', 'youtube', 'video', 'level2jeff']
---
Almost a year ago, I found that [N100 Mini PCs were cheaper than a decked-out Raspberry Pi 5](/blog/2025/intel-n100-better-value-raspberry-pi/). So comparing systems with:

  - 16GB of RAM
  - 512GB NVMe SSD
  - Including case, cooler, and power adapter

Back in March last year, a GMKtec Mini PC was $159, and a similar-spec Pi 5 was $208.

Today? The [same GMKtec Mini PC](https://amzn.to/4srcKB3) is $246.99, and the same Pi 5 is $246.95:

{{< figure
  src="./costs-gmktec-vs-pi-5.jpg"
  alt="GMKtec N100 Mini PC vs Pi 5 16GB pricing 2025"
  width="700"
  height="auto"
  class="insert-image"
>}}

Today, because of the wonderful RAM shortages[^sarcasm], the Mini PC is the same price as a fully kitted-out Raspberry Pi 5.

And that stinks.

_Both_ of these systems have gone up in price, just the Pi a little less than the mini PCs.

{{< figure
  src="./costs-pi-5-16gb.jpg"
  alt="Pi 5 16GB pricing 2025"
  width="700"
  height="auto"
  class="insert-image"
>}}

The Pi got a [smaller price bump](https://www.raspberrypi.com/news/5-10-price-increases-for-some-4gb-and-8gb-products/#comments) late last year due to tight memory chip supplies, and they even introduced a lighter 1 GB RAM model.

The usefulness of 1 GB of RAM is, sadly, not much in today's memory-hungry world. But it does keep the base model Pi 5 below $50, where you can find them in stock.

{{< figure
  src="./costs-gmktec-costs.jpg"
  alt="GMKtec N100 16GB pricing 2025"
  width="700"
  height="auto"
  class="insert-image"
>}}

The Mini PC's price rose more dramatically, and in many ways, it's a bit more catastrophic.

With the incredibly low system costs (I saw many N100 PCs for $99 or $129 on sale), people got into homelabbing and put these little systems _everywhere_.

It was the cheapest way to get into Jellyfin transcoding, very lightweight gaming, kiosk PC building, etc. And they were just good enough to do useful things, despite some of the 'value' brands offering terrible support for their boxes.

But now the Pi's gone from around $200 to $250, and the PC from $150 to $250. Far fewer people can justify those prices for a little hobby machine.

## Finding value in the old

I think that the theme of 2026 is going to be repurposing used hardware.

If you can be resourceful and use your existing gear in different ways, that's going to be a lot more valuable and you're going to save a lot of money. That's always been true, but is even more so as we enter 2026.

I don't know when the AI bubble will pop and RAM prices will come back down to reality, but it doesn't sound like this is a short-term thing.

Even if there's a new fab announced, it takes 2-3 years to bring it online.

On the Pi side, if you _can_ live with 1 or 2 GB of RAM, and don't need NVMe speeds, you can still get into the high-end Pi 5 ecosystem with a full kit under $80:

{{< figure
  src="./costs-pi5-1gb.jpg"
  alt="GMKtec N100 16GB pricing 2025"
  width="700"
  height="auto"
  class="insert-image"
>}}

Even better, if your needs are _truly_ minimal, you can still buy a Pi Zero 2W for $15—if you can find one in stock.

And you can buy a Pi clone as well—some of the boards from Radxa, Orange Pi, etc. are halfway decent these days... though support for them is all over the board. (Check out my [SBC Reviews](https://sbc-reviews.jeffgeerling.com) site for my own testing with many of them.)

Of course, used is always going to be cheaper.[^used]

But I thought I'd take a look at the numbers, re-evaluate a year later, and write up this post.

I also posted this basic premise in video form over on my 2nd channel, Level2Jeff. I don't know why you'd want to, since you've already read this post, but you can watch it here: [Raspberry Pis are cheaper than Mini PCs again](https://www.youtube.com/watch?v=YDM4lewqz9U).

[^sarcasm]: Yes, I'm being sarcastic.

[^used]: Like clockwork, whenever I post about any kind of hardware, someone comments "that's way too expensive, I bought a used XYZ for like 30% less!" Yes. We get it! Used is cheaper; unless the market is completely out of whack, that's how the world works! There are tradeoffs buying used hardware, and sometimes you need some of the benefits of buying new.
