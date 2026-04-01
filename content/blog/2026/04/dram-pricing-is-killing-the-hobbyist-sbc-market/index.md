---
date: '2026-04-01T16:00:00-05:00'
tags: ['sbc', 'raspberry pi', 'shortage', 'dram', 'industry', 'youtube', 'video']
title: 'DRAM pricing is killing the hobbyist SBC market'
slug: 'dram-pricing-is-killing-the-hobbyist-sbc-market'
---
Today Raspberry Pi announced [more price increases for all Pis with LPDDR4 RAM](https://www.raspberrypi.com/news/a-new-3gb-raspberry-pi-4-for-83-75-and-more-memory-driven-price-increases/), alongside a 'right-sized' 3GB RAM Pi 4 for $83.75.

The price increases bring the 16GB Pi 5 up to _$299.99_.

Despite today's date, this is not a joke.

I published a video going over the state of the hobbyist 'high end SBC' market (4/8/16 GB models in the current generation), which I'll embed below:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/HeX22LnKdFY' frameborder='0' allowfullscreen></iframe></div>
</div>

But if you'd like the **tl;dr**:

Unless the DRAM pricing situation changes _radically_, I think the hobbyist SBC market is dying—or at least on life support. And I don't just mean Raspberry Pis, but all SBC vendors. LPDDR chips now account for the majority of board cost from the vendors I've checked with.

{{< figure
  src="./raspberry-pi-price-increase-since-launch.jpg"
  alt="Raspberry Pi 5 Price Increases since launch 2 4 and 16 GB models"
  width="700"
  height="auto"
  class="insert-image"
>}}

Besides causing a radical reduction in new boards launched (Radxa seems to be the only vendor that had some cadence last year), the price increases for boards with greater than 4 GB of RAM have put those boards out of the reach of most hobbyists.

Even mini PCs, which for a time were a _great_ deal, have risen to $250+ for 8 GB models. _Used_ PC are also more expensive, especially with more than 4 GB of RAM.

I design most of my projects so they can be replicated for less than $100. Learning is easier on cheaper parts you won't fret over too much when you break them. With prices going up, this limits the types of projects I take on.

I'm working more with older SBCs and microcontrollers now, and I think that's the direction many in the hobbyist space are going.

Maybe, as Eben Upton says in Raspberry Pi's post,

> memory prices won’t remain at their current very high level indefinitely; the circumstances in which we find ourselves are challenging, but in the future they will abate.

But I'm not sure how long we'll have to wait, or if a hobbyist SBC market will exist by the time the bubble bursts.

Lucky for Raspberry Pi, they have a thriving microcontroller ecosystem and industrial base to keep them going. I fear smaller vendors won't be able to go on like this forever.
