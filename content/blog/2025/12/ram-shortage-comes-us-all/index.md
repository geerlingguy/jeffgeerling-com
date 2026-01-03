---
nid: 3518
title: "The RAM Shortage Comes for Us All"
slug: "ram-shortage-comes-us-all"
date: 2025-12-04T18:43:47+00:00
drupal:
  nid: 3518
  path: /blog/2025/ram-shortage-comes-us-all
  body_format: markdown
  redirects: []
tags:
  - ai
  - computer
  - industry
  - memory
  - parts shortage
  - pc
  - ram
---

Memory price inflation comes for us all, and if you're not affected yet, just wait.

I was building a new PC last month using some parts I had bought earlier this year. The 64 Gigabyte T-Create DDR5 memory kit I used cost $209 then. Today? The [same kit costs $650](https://www.microcenter.com/product/680461/teamgroup-t-create-expert-64gb-(2-x-32gb)-ddr5-6400-pc5-51200-cl34-dual-channel-desktop-memory-kit-ctced564g6400hc34bdc01-black)!

Just in the past week, we found out [Raspberry Pi's increasing their single board computer prices](https://www.raspberrypi.com/news/1gb-raspberry-pi-5-now-available-at-45-and-memory-driven-price-rises/). Micron's [killing the Crucial brand of RAM and storage devices _completely_](https://investors.micron.com/news-releases/news-release-details/micron-announces-exit-crucial-consumer-business), meaning there's gonna be one fewer consumer memory manufacturer. [_Samsung_ can't even buy RAM from themselves](https://www.pcworld.com/article/2998935/ram-is-so-expensive-samsung-wont-even-sell-it-to-samsung.html) to build their own Smartphones, and small vendors like [Libre Computer](https://x.com/librecomputer/status/1995592912063922578) and [Mono](https://www.youtube.com/watch?v=AyueVGLT7qI) are seeing RAM prices double, triple, or even _worse_, and they're not even buying the latest RAM tech!

{{< figure src="./2025.12.04.usd_.ram_.ddr5_.6000.2x16384.5cd324eb79715651e5c39693bcec4df7.png" alt="PC Parts Picker RAM Graph" width="700" height="288" class="insert-image" >}}

I think PC builders might be the first crowd to get impacted across the board—just look at these [insane graphs from PC Parts Picker](https://pcpartpicker.com/trends/price/memory/), showing RAM prices going from like $30 to $120 for DDR4, or like $150 to _five hundred dollars_ for 64 gigs of DDR5.

But the impacts are only just starting to hit other markets.

[Libre Computer mentioned on Twitter](https://x.com/librecomputer/status/1995592912063922578) a single 4 gigabyte module of LPDDR4 memory costs $35. That's more expensive than every other component on one of their single board computers _combined_! You can't survive selling products at a loss, so once the current production batches are sold through, either prices will be increased, or certain product lines will go out of stock.

The smaller the company, the worse the price hit will be. Even Raspberry Pi, who I'm sure has a little more margin built in, already raised SBC prices (and introduced a 1 GB Pi 5—maybe a good excuse for developers to drop Javascript frameworks and program for lower memory requirements again?).

Cameras, gaming consoles, tablets, almost anything that has memory will get hit sooner or later.

I can't believe I'm saying this, but compared to the _current_ market, Apple's insane memory upgrade pricing is... actually in line with the rest of the industry.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/9rbz0akyLyQ" frameborder='0' allowfullscreen></iframe></div>
</div>

The reason for all this, of course, is AI datacenter buildouts. I have no clue if there's any price fixing going on like there was [a few decades ago](https://en.wikipedia.org/wiki/DRAM_price_fixing_scandal)—that's something conspiracy theorists can debate—but the problem is there's only a few companies producing all the world's memory supplies.

And those companies all realized they can make _billions_ more dollars making RAM just for AI datacenter products, and neglect the rest of the market.

So they're shutting down their consumer memory lines, and devoting all production to AI.

Even companies like GPU board manufacturers are getting shafted; [Nvidia's not giving memory to them along with their chips like they used to](https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-no-longer-supplying-vram-to-its-gpu-board-partners-in-response-to-memory-crunch-rumor-claims-vendors-will-only-get-the-die-forced-to-source-memory-on-their-own), basically telling them "good luck, you're on your own for VRAM now!"

Which is especially rich, because [Nvidia's profiting _obscenely_ off of all this stuff](https://techcrunch.com/2025/11/19/nvidias-record-57b-revenue-and-upbeat-forecast-quiets-ai-bubble-talk/).

That's all bad enough, but some people see a silver lining. I've seen some people say "well, once the AI bubble bursts, at least we'll have a ton of cheap hardware flooding the market!"

And yes, in past decades, that might be one outcome.

But the problem here is the RAM they're making, a ton of it is either integrated into specialized GPUs that won't run on normal computers, or being fitted into special types of memory modules that don't work on consumer PCs, either. (See: [HBM](https://en.wikipedia.org/wiki/High_Bandwidth_Memory)).

That, and the GPUs and servers being deployed now don't even run on normal power and cooling, they're part of _massive_ systems that would take a ton of effort to get running in even the most well-equipped homelabs. It's not like the classic [Dell R720](https://merox.dev/blog/dell-r720/) that just needs some air and a wall outlet to run.

That is to say, we might be hitting a weird era where the PC building hobby is gutted, SBCs get prohibitively expensive, and anyone who didn't stockpile parts earlier this year is, pretty much, in a lurch.

Even [Lenovo admits to stockpiling RAM](https://www.pcworld.com/article/2986266/lenovo-stockpiles-ram-to-hopefully-keep-laptop-prices-down.html), making this like the toilet paper situation back in 2020, except for massive corporations. Not enough supply, so companies who _can_ afford to get some will buy it all up, hoping to stave off the shortages that will probably last longer, partly _because_ of that stockpiling.

I don't think it's completely outlandish to think some companies will start [scavenging memory chips](https://www.youtube.com/shorts/WO-VvucMq4E) (ala [dosdude1](https://www.youtube.com/user/dosdude1)) off other systems for stock, especially if RAM prices keep going up.

It's either that, or just stop making products. There are some echoes to the global chip shortages that hit in 2021-2022, and that really shook up the market for smaller companies.

I hate to see it happening again, but somehow, here we are a few years later, except this time, the AI bubble is to blame.

Sorry for not having a positive note to end this on, but I guess... maybe it's a good time to dig into that pile of old projects you never finished instead of buying something new this year.

How long will this last? That's anybody's guess. But I've already put off some projects I was gonna do for 2026, and I'm sure I'm not the only one.
