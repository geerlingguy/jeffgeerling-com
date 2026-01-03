---
nid: 2835
title: "Raspberry Pi microSD card performance comparison - 2018"
slug: "raspberry-pi-microsd-card-performance-comparison-2018"
date: 2018-04-06T18:13:26+00:00
drupal:
  nid: 2835
  path: /blog/2018/raspberry-pi-microsd-card-performance-comparison-2018
  body_format: markdown
  redirects: []
tags:
  - benchmarks
  - comparison
  - dramble
  - microsd
  - performance
  - raspberry pi
---

{{< figure src="./microsd-cards-jeff-geerling-raspberry-pi-sbc.jpg" alt="Raspberry Pi microSD cards Noobs Samsung Kingston Toshiba Sony SanDisk SD SBC" width="488" height="329" class="insert-image" >}}

Back in 2015, I wrote a popular post [comparing the performance of a number of microSD cards](//www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-microsd-card) when used with the Raspberry Pi. In the intervening three years, the marketplace hasn't changed a ton, but there have been two new revisions to the Raspberry Pi (the model 3 B and just-released model 3 B+). In that article, I stated:

> One of the highest-impact upgrades you can perform to increase Raspberry Pi performance is to buy the fastest possible microSD card—especially for applications where you need to do a lot of random reads and writes.

As part of my work on a comprehensive [review of the Raspberry Pi model 3 B+](https://www.jeffgeerling.com/blog/2018/raspberry-pi-3-b-review-and-performance-comparison), I decided to re-run all the benchmarks for all the Samsung and SanDisk cards (the rest, from Sony, Toshiba, Lexar, and no-name brands were so slow for Pi usage as to not warrant any testing at all!). Without further ado, here are the latest results, tested on a Raspberry Pi model 3 B+:

{{< figure src="./pi-model-3-b-plus-microsd-io-performance-comparison-revised-2.png" alt="Raspberry Pi model 3 B+ microSD card performance comparison" width="650" height="624" class="insert-image" >}}

Just as with the model 2 B and model 3 B, the [Samsung Evo+](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1523037699&sr=1-4&keywords=samsung+evo+plus&dpID=419o58jbNhL&preST=_SX300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=8f5797290f6a6ed3dc53159e8b784f73) outshines the rest of the field in 4K random read and random write—two of the most important metrics for common Raspberry Pi use cases. Since the Pi's microSD I/O is often the major bottleneck (especially now that the onboard LAN and WiFi have upped their bandwidth by at least 2x over the previous generation), it's important to get every bit of speed out of the card that runs the OS as is possible.

The [SanDisk Extreme](https://www.amazon.com/dp/B06XWMQ81P/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=f7777ae07f3aec259621bdfc999b2303) and [Samsung Pro+](https://www.amazon.com/Samsung-Plus-MicroSDHC-Memory-Write/dp/B01273L37G/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1523037862&sr=1-3&keywords=samsung+pro+plus+micro+sd&dpID=41OcqEvr1QL&preST=_SY300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=9c4b4138c2680eb0e1ecef05438f48c9) are also worthy options, but both cost slightly more than the Evo+, and offer slightly less performance overall.

In a simpler format, here are my picks for **the best microSD cards on the market for use with the Raspberry Pi**:

  1. [Samsung Evo+](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1523037699&sr=1-4&keywords=samsung+evo+plus&dpID=419o58jbNhL&preST=_SX300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=8f5797290f6a6ed3dc53159e8b784f73) - $15 on Amazon
  2. [SanDisk Extreme](https://www.amazon.com/dp/B06XWMQ81P/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=f7777ae07f3aec259621bdfc999b2303) - $19 on Amazon
  3. [Samsung Pro+](https://www.amazon.com/Samsung-Plus-MicroSDHC-Memory-Write/dp/B01273L37G/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1523037862&sr=1-3&keywords=samsung+pro+plus+micro+sd&dpID=41OcqEvr1QL&preST=_SY300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=9c4b4138c2680eb0e1ecef05438f48c9) - $27 on Amazon

## Overclocking the Pi's microSD card reader

You can also [overclock the microSD card reader in the Raspberry Pi](//www.jeffgeerling.com/blog/2016/how-overclock-microsd-card-reader-on-raspberry-pi-3) to eke out a tiny bit more performance from the cards in this benchmark (all except the Samsung Pro (non-plus) were stable at a 100 MHz overclock in my testing), but it won't make much of a difference in real-world usage.

{{< figure src="./pi-model-3-b-plus-overclocked-microsd-card.png" alt="Raspberry Pi model 3 B+ microSD card performance - overclock comparison" width="650" height="283" class="insert-image" >}}

There _is_ a measurable performance increase, but when you get to real-world usage, it doesn't make a huge difference (when I did Drupal testing, there was less than 1% difference when overclocked vs not overclocked).

## Benchmark methodology

For the benchmarks, I ran a [standardized I/O benchmark script](https://github.com/geerlingguy/raspberry-pi-dramble/blob/master/setup/benchmarks/microsd-benchmarks.sh) on a freshly-flashed Pi using the latest version of Raspbian Lite, with no modifications or customizations. The script can be run on a Pi running Raspbian using the following command:

```
curl https://raw.githubusercontent.com/geerlingguy/raspberry-pi-dramble/master/setup/benchmarks/microsd-benchmarks.sh | sudo bash
```

You can view all the benchmarks and detailed methodology in my continuously-updated [microSD card benchmarks](http://www.pidramble.com/wiki/benchmarks/microsd-cards) page on the Raspberry Pi Dramble wiki.
