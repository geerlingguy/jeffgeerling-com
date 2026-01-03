---
nid: 3042
title: "What does Nvidia buying ARM mean for Raspberry Pi?"
slug: "what-does-nvidia-buying-arm-mean-raspberry-pi"
date: 2020-09-14T14:45:36+00:00
drupal:
  nid: 3042
  path: /blog/2020/what-does-nvidia-buying-arm-mean-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - arm64
  - broadcom
  - cpu
  - nvidia
  - raspberry pi
  - softbank
---

Over the weekend, Nvidia confirmed [it would purchase ARM](https://nvidianews.nvidia.com/news/nvidia-to-acquire-arm-for-40-billion-creating-worlds-premier-computing-company-for-the-age-of-ai) from Softbank for $40 billion.

Now, what is ARM, why is Nvidia buying it, and what does any of this have to do with the Raspberry Pi?

Well, let's start with ARM.

> This blog post also has a [video version to go along with it](https://www.youtube.com/watch?v=-x_ghgOSHco).

## What is ARM?

ARM can refer to a number of things, but let's start by talking about the company, [Arm Holdings](https://en.wikipedia.org/wiki/Arm_Holdings). They have lineage dating back to [Acorn computers](https://en.wikipedia.org/wiki/Acorn_Computers), a British computer manufacturer founded in the late 1970s that designed the first 'Acorn RISC Machine architecture' chips, AKA 'ARM'.

{{< figure src="./BBC_Micro_Front_Restored.jpg" alt="BBC Micro Minicomputer - Source: Wikipedia" width="512" height="365" class="insert-image" >}}

The first ARM products they made went into the [BBC Micro](https://en.wikipedia.org/wiki/BBC_Micro) computers... which were built with an emphasis for education and were actually an inspiration for the Raspberry Pi we know and love today!

Anyways, ARM continued evolving its chip designs, and eventually started licensing the 'blueprints' for ARM processors, to the point that today, ARM-architecture chips power almost all mobile phones, the majority of tablet computers, and soon, even common desktop and laptop computers, once Apple starts selling it's new ARM-based Macs.

> Read my related article: [What does Apple Silicon mean for the Raspberry Pi and ARM64?](/blog/2020/what-does-apple-silicon-mean-raspberry-pi-and-arm64).

So ARM is a pretty big deal. And there are tons of companies who license ARM core designs in their products, including Apple, Amazon, Atmel, Texas Instruments, Broadcom, and even Nvidia.

Now, why is Nvidia buying ARM? And why is SoftBank, ARM's current owner, willing to give it up?

## Why is Nvidia buying Arm Holdings?

Well, someone could probably write a book about [why](https://markets.businessinsider.com/news/stocks/wirecard-timeline-what-you-need-to-know-2bn-fintech-scandal-2020-6-1029337346?op=1#) [SoftBank](https://www.vox.com/recode/2019/9/24/20882174/wework-adam-neumann-softbank-ipo) [is](https://www.business-standard.com/article/international/softbank-unmasked-as-nasdaq-whale-that-stoked-tech-rally-report-120090500079_1.html) [selling](https://www.msn.com/en-us/money/companies/credit-suisse-starts-probe-into-softbank-linked-funds/ar-BB15SlI3) [ARM](https://www.metro.us/softbank-sheds-13-billion/) after how its other investments have been doing in 2020, so I won't explore that topic here. But one of the main reasons Nvidia is willing to pay _$40 billion_ for ARM is to entrench themselves even further into the realm of Artificial Intelligence (AI) and Machine Learning (ML) processing.

Nvidia is incredibly popular in the AI and ML space, and again, I'm sure someone could write a book about the reasons why. But why buy ARM? Well, mostly, I think, because the power of the combined buzzwords between Nvidia and ARM is irresistable to technologists and investors. Just listen to this paragraph from Nvidia's [press release](https://nvidianews.nvidia.com/news/nvidia-to-acquire-arm-for-40-billion-creating-worlds-premier-computing-company-for-the-age-of-ai):

> "Uniting NVIDIA’s AI computing capabilities with the vast ecosystem of Arm’s CPU, we can advance computing from the cloud, smartphones, PCs, self-driving cars and robotics, to edge IoT, and expand AI computing to every corner of the globe."

I mean, what hot tech buzzword _wasn't_ mentioned in that paragraph? I guess maybe Kubernetes and space rockets, but I digress.

Anyways, Nvidia is buying ARM to up its game in the AI and machine learning space. But what does any of that have to do with the Pi?

Well, two things.

{{< figure src="./nvidia-jetson-nano.jpg" alt="Nvidia Jetson Nano" width="595" height="335" class="insert-image" >}}

First, Nvidia has a development board, the [Jetson Nano](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/), which is a direct competitor to the higher-end Raspberry Pi 4. It's a bit pricier and offers only a few features that differentiate it from the Pi, but I don't doubt Nvidia would set its sights on the Pi maker space if the profit margins were good enough and they had a better relationship with the free and open source software community.

{{< figure src="./pi-4-model-b-broadcom-chip.jpg" alt="Raspberry Pi 4 model B Broadcom SoC" width="600" height="338" class="insert-image" >}}

But second, and more important, every Raspberry Pi ever made is powered by a System on a Chip built by Broadcom, with ARM-licensed cores.

So the important question is this: _how is Broadcom's relationship with Nvidia?_

Well, there's bad news and there's good news. And note that no video I make here would be able to do justice to the long and winding history of the semiconductor industry that has led us to today's news.

The bad news? Broadcom and Nvidia are direct competitors in many spaces, especially in some of the 'hot growth' markets like "Internet of Things" (IoT) and "Edge computing". So don't expect Nvidia to cut Broadcom slack in licensing deals.

Also, outside of their relationship with Broadcom, Nvidia is not necessarily known for being a friendly free and open source company all the time, though they do have their toes in the open source water.

The good news? Nothing is likely to change in the short term. Nvidia's keeping ARM's structure and licenses as-is, at least for the foreseeable future. So we should expect _at least_ a few more years of new mobile chips that trickle their way down to inexpensive single board Linux computers like the Raspberry Pi.

And in other good news, a shakeup is bound to happen as Intel's seeming stranglehold they had on the entire CPU industry for years is unraveling this decade. And competition could make for better, cheaper chips.

## Positive Signs in the Industry

{{< figure src="./risc-v-logo.png" alt="RISC-V Logo" width="440" height="83" class="insert-image" >}}

For example, IBM completely [open sourced the POWER architecture](https://newsroom.ibm.com/2019-08-21-IBM-Demonstrates-Commitment-to-Open-Hardware-Movement) late last year, and there's also the [RISC-V CPU architecture](https://en.wikipedia.org/wiki/RISC-V) which is completely license-free and open source, and there are already some manufacturers building RISC-V chips.

As we've seen with Apple, and even Linux in recent years, switching CPU architectures is not impossible, and sometimes brings major benefits. In the case of Apple with PowerPC to Intel, it brought about better mobile performance. In the case of Intel to ARM on tablets and mobile devices, it brought about vast improvements in battery life and in performance-per-watt efficiency.

A forced transition from ARM to something else could be a net benefit in computing, if it has to happen someday. I'm an optimist, so I hope that'd be the case.

But that's all speculation. I know for the foreseeable future, we won't see much change, just newer, faster Raspberry Pis.

But it _is_ a little sad to see a plucky British computer manufacturer, the Raspberry Pi Foundation, who used a CPU architecture built by another long-time British computer manufacturer, have to now say they're using tech licensed through a US company (even if ARM's HQ will still be in Cambridge).

I'm not even British, but it feels similar to how Mini, a uniquely and in Mini's case somewhat oddball British thing, is not the same now that it's [owned by a German company, BMW](https://en.wikipedia.org/wiki/Mini_(marque)).

Do the massive tech conglomerates in the US really need to eat up another non-US company? I guess so. At least, NVDA investors seem happy today, with the stock price up nearly 10%:

{{< figure src="./nvidia-stock.jpg" alt="NVDA stock price on September 14" width="600" height="338" class="insert-image" >}}

I hope that there's nothing but good news for everyone after this deal goes through. All I know is I'm ready to compile my Raspberry Pi projects on whatever chip architecture it takes. I'm too in love with these tiny inexpensive computers to stop using them!
