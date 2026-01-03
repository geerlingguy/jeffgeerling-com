---
nid: 2926
title: "A2-class microSD cards offer no better performance for the Raspberry Pi"
slug: "a2-class-microsd-cards-offer-no-better-performance-raspberry-pi"
date: 2019-07-22T12:56:40+00:00
drupal:
  nid: 2926
  path: /blog/2019/a2-class-microsd-cards-offer-no-better-performance-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - a2
  - benchmarks
  - dramble
  - microsd
  - performance
  - raspberry pi
  - sd
---

> **Update**: See follow-up post about A1 vs A2 performance, [Raspberry Pi microSD follow-up, SD Association fools me twice?](/blog/2019/raspberry-pi-microsd-follow-sd-association-fools-me-twice).

After I published my [2019 Raspberry Pi microSD card performance comparison](/blog/2019/raspberry-pi-microsd-card-performance-comparison-2019), I received a lot of feedback about newer 'A2' Application Performance class microSD cards, and how they could produce even better performance for a Raspberry Pi.

<p style="text-align: center;">{{< figure src="./microsd-cards-a2-performance-class.jpg" alt="A2 Performance Class SanDisk and Lexar microSD cards next to older Samsung and SanDisk cards" width="650" height="480" class="insert-image" >}}<br>
<em>None of these cards are fakes; grainy halftone printing is visible because I shot this with a macro lens.</em></p>

Until last year, it was hard to judge a microSD cards' suitability for the Pi without first purchasing and testing it, because the only marketed rating was for sequential read/write performance (e.g. 'U3' meant the card could write sequential files (e.g. large images or videos) at 30 MB/sec or higher, and 'C10' was for 10 MB/sec or higher). The Pi, as a general purpose computer, reads and writes very small files, and doesn't usually need faster large-file performance.

As more and more people use microSD cards for extra storage on their phones and tablets, or for system boot volumes on devices like the Raspberry Pi, there was a need for a performance metric more relevant to the random access patterns used in these scenarios.

Therefore the [SD Association created 'Application Performance' class designations](https://www.sdcard.org/developers/overview/application/index.html), A1 and A2. The minimum ratings are stated in this table:

{{< figure src="./microsd-a1-a2-performance-class-specifications.jpg" alt="microSD A1 and A2 Application performance class standards" width="596" height="350" class="insert-image" >}}

This kind of performance metric is _much_ more helpful for someone like me, so I was excited to purchase a few A2 cards and see how much more random I/O / IOPS I could get out of them. After all, 2000 IOPS for 4K random writes is approaching a low-end SSD's performance on an older SATA bus.

So I opened up an issue in the Raspberry Pi Dramble cluster's issue queue: [Add three more microSD cards to the benchmarks, test A2 performance](https://github.com/geerlingguy/raspberry-pi-dramble/issues/161), and put two new A2 cards to the test (and one A1 card—it's results are in the linked issue):

  - [SanDisk Extreme 64GB U3 V30 A2](https://www.amazon.com/gp/product/B07FCMBLV6/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=d65c4ec6f33497b1596134e3ac06da2a&language=en_US)
  - [Lexar Professional U3 A2 V30 128GB](https://www.amazon.com/Lexar-Professional-128GB-microSDXC-LSDMI128BNA667A/dp/B07NHCB6N3/ref=as_li_ss_tl?dchild=1&keywords=Lexar+Professional+U3+A2+V30+128GB&qid=1590159603&sr=8-1&linkCode=ll1&tag=mmjjg-20&linkId=649828747de640152ccccea21b191726&language=en_US)
  - [Samsung Pro Endurance 32GB U1](https://www.amazon.com/gp/product/B07B98GXQT/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=6bec0a6dbb665304e450c086e2b704fc&language=en_US)

I ran [my usual microSD benchmarks](https://www.pidramble.com/wiki/benchmarks/microsd-cards#benchmarks) (hdparm and dd to test sequential read/write speeds, then iozone to test random I/O), and what I found surprised me:

{{< figure src="./a2-application-performance-class-speed-comparison-to-older-microsd.png" alt="A2 Application Performance class microSD cards compared to older non-A1 cards" width="650" height="361" class="insert-image" >}}

Not only were both cards underperforming the minimum required spec to meet A2 compliance—by more than half (4000 IOPS read, 2000 IOPS write)—they were _also_ slower than some of my older microSD cards produced years before the 'A1' and 'A2' class designations.

I'm a skeptic, though, and I always like to challenge my own assumptions. So, before accusing manufacturers of inflating their card's performance claims, or the SD Association of rubber-stamping card performance designations, I wanted to see if there was any possible way for me to get the IOPS they were supposedly able to get.

## Testing on two Macs

I used [AmorphousDiskMark](http://www.katsurashareware.com/pgs/adm.html) on macOS to test 4K random writes on both of the following Macs:

  - MacBook Pro 13" 2015 i7
  - MacBook Pro 13" 2016 i5 Function Keys

I also tested with four different readers: [AUKEY USB-C hub with microSD reader](https://www.amazon.com/gp/product/B07J62G3JG/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=53e597b11482afcd228945a271d854e0&language=en_US), [Rocketek XQD/SD card reader](https://www.amazon.com/gp/product/B07M91SJJ1/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=49e8393b791bcd7c532649ccea15d4e9&language=en_US) with two different SD card to microSD adapters (Samsung and Lexar), the built-in SD card reader on the 2015 MacBook Pro, and a [UGreen UHS-II USB-C SD and microSD card reader](https://www.amazon.com/gp/product/B072M6S5F8/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=83d9412fae9293e0d8d8a23c57b2141a&language=en_US).

The numbers were nearly identical in every test and device. I didn't put down all test results in the previously-linked GitHub test, but I was very thorough.

## SD 6.0 Part I physical specification

So, thinking maybe I'm measuring something completely different (e.g. [air compressor CFM ratings are complete BS](https://www.youtube.com/watch?v=cfjSm_ieRkE)), I read through the [SD 6.0 Part I physical specification](https://www.sdcard.org/downloads/pls/index.html) to see exactly how they benchmark these cards. I read every relevant portion, including the most important bit:

> Note that unit of random performance [IOPS] indicate number of 4KB sized I/O Operations completed in one second, wherein each transaction was targeted to a random address generated for 256MB address range.

So it was definitely IOPS measured with 4KB random I/O, however the only tiny detail that was different was the address range; I use 100 MB for most of my tests, just to save time benchmarking many cards. I also tested with 512 MB and 1 GB ranges, and found the same performance numbers.

I fired up the Pi again, and ran the following iozone command to simulate the exact scenario listed in the SD 6.0 specification:

    ./iozone -e -I -a -s 256M -r 4k -i 0 -i 2

Nope. Same result, 9.58 MB/sec read, 2.55 MB/sec write. In fact, the speeds were so consistent (some microSD cards have a standard deviation in the 5-10% range!), maybe I've discovered the flaw in the SD Association's tests—instead of measuring success by IOPS, they're measuring success by low standard deviation! /s

I looked around the Internet to see if there were any other posts either supporting or contradicting my claims. I didn't find much, but one detailed post I _did_ find seemed to conclude with the same results: [The newest, fastest "app class" microSD cards are still not very good for apps](https://www.androidpolice.com/2019/02/13/sandisk-a2-and-400gb-microsd-roundup-review-buy-for-storage-not-apps/). In their post, they said:

> None of these cards were even able to hit A2 speeds in our tests. However SanDisk is calculating its IOPS (perhaps in super-short bursts, or with different IO request sizes?) it doesn't jibe with benchmarks.

I haven't found anyone performing real-world benchmarks proving any A2 cards reach the IOPS in the spec.

## So A2 Application Class is marketing BS?

Yes.

If one of the microSD card manufacturers (in this case, SanDisk or Lexar), or the SD Association disagrees with my opinion, I'd invite them to show me any way to get the performance out of these cards that they claim they should be producing. I've tested with five different card interfaces, some over USB 3.1 and USB 3.0, on some very fast computers, with multiple disk benchmarking tools, and the results were consistently very poor.

All I can conclude is the microSD manufacturers are taking batches of their former 'not-A2-rated' cards and stamping an A2 on it, then doubling the price for the exact same card.

Conclusion: **Don't buy A2 cards**. Save half the money and buy the same card I've been recommending for years, the [Samsung Evo+](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?keywords=samsung+evo++microsd&qid=1562707245&s=gateway&sr=8-5&linkCode=ll1&tag=mmjjg-20&linkId=019797e6b450340f7d7c739ae8ad1203&language=en_US), which is not even 'A1' rated, but still beats any other card I've tested for price-to-value.
