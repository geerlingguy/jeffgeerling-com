---
nid: 2927
title: "Raspberry Pi microSD follow-up, SD Association fools me twice?"
slug: "raspberry-pi-microsd-follow-sd-association-fools-me-twice"
date: 2019-07-25T15:27:30+00:00
drupal:
  nid: 2927
  path: /blog/2019/raspberry-pi-microsd-follow-sd-association-fools-me-twice
  body_format: markdown
  redirects: []
tags:
  - benchmarks
  - dramble
  - microsd
  - performance
  - raspberry pi
  - sd
---

____________________________________________
    / Fool me once, shame on you. Fool me twice, \
    \ prepare to die. (Klingon Proverb)          /
     --------------------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

(Excerpt from [Ansible for DevOps](https://www.ansiblefordevops.com), chapter 12.)

The fallout from this year's [microSD card performance comparison](/blog/2019/raspberry-pi-microsd-card-performance-comparison-2019) has turned into quite a rabbit hole; first I found that new 'A1' and 'A2' classifications were supposed to offer better performance than the not-Application-Performance-class-rated cards I have been testing. Then I found that [A2 rated cards offer no better performance for the Raspberry Pi](/blog/2019/a2-class-microsd-cards-offer-no-better-performance-raspberry-pi)—in fact they didn't even perform _half_ as well as they were supposed to, for 4K random reads and writes, on any hardware I have in my possession.

{{< figure src="./microsd-cards-a1-a2-and-pile-raspberry-pi-review.jpg" alt="Pile of microSD cards A1 A2 and Raspberry Pi NOOBS card" width="650" height="442" class="insert-image" >}}

And now, I've discovered that _A1_ class cards like the [SanDisk Extreme Pro A1](https://www.amazon.com/gp/product/B06XYHN68L/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=def3c663e1e6cc69822e4d0ccdb2c78b&language=en_US) actually perform _better_ than A2 cards I've tested. And in a complete about-face from their A2 counterparts, it seems like A1 cards actually perform 2x _better_ than their rated minimum spec:

{{< figure src="./raspberry-pi-microsd-a1-sandisk-extreme-pro-speed.png" alt="Raspberry Pi microSD card benchmark showing SanDisk Extreme Pro A1 comparison" width="650" height="359" class="insert-image" >}}

The Extreme Pro A1 finally tops the random write performance of the three-year-old Samsung Evo+, though it's still a bit shy of the random read performance. What's more interesting to me (since I buy a ton of these little cards and cost is a major consideration) is the IOPS you get per US dollar:

<table>
  <tr>
    <th>Card</th>
    <th>Price (mid-2019)</th>
    <th>IOPS/USD (read)</th>
    <th>IOPS/USD (write)</th>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?keywords=evo++32gb&qid=1564068218&s=gateway&sr=8-5&linkCode=ll1&tag=mmjjg-20&linkId=f00824e44ec982d799d9dc8069540e6b&language=en_US">Samsung Evo+ 32GB</a></td>
    <td>8.60</td>
    <td>322</td>
    <td>115</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/gp/product/B07FCMBLV6/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=86e1ac3905e7e6937536336c67ec715f&language=en_US">SanDisk Extreme A2 64GB</a></td>
    <td>15.49</td>
    <td>122</td>
    <td>61</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/gp/product/B06XYHN68L/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=8a92b9c326e5edccf407c4cfe9415d88&language=en_US">SanDisk Extreme Pro A1 32GB</a></td>
    <td>13.73</td>
    <td>183</td>
    <td>88</td>
  </tr>
</table>

So, unless SanDisk decides to halve their price points, the Samsung microSD cards seem to be the best value for any kind of 'application' level performance, even though it seems Samsung has not yet applied for any A1/A2 ratings on their cards yet. (Note: I couldn't find a 32GB version of the A2 SanDisk Extreme to purchase and test, so I'm sticking with the 64GB pricing.)

After posting the A2 card performance article, I received a lot of feedback in comments on Reddit and Hacker News, and one thing I learned is that to achieve the rated performance, it seems you need to have special firmware and/or kernel-level support for A2 Command Queue and Cache functions. From [/u/farptr's comment summarizing the requirements](https://www.reddit.com/r/raspberry_pi/comments/cgcveg/a2class_microsd_cards_offer_no_better_performance/eugmel4):

> **Command Queue**
> 
> The new CQ mechanism allows the SD memory card to accept several commands in a series (without their associated data) and execute them (with the data) whenever the memory card is ready. It contributes mainly to random read performance.
> During the data transfer, additional commands may be sent to the card as long as the maximum number of queued commands does not exceed the maximum queue depth supported by the card (the SD standard allows queue depth of min 2, max 32).
> With CQ, advanced information on intended commands is provided to the card. The card may manage and optimize its internal operations to prepare for the various commands in advance. Multiple tasks can be handled at one time in arbitrary order. New information on next commands may be sent to the card during current execution and during data transfer.
> 
> **Cache function**
> 
> In order to overcome the relatively limited write speed operation of flash memory, the Cache function allows the card to accumulate the data accepted by the host in a high-speed memory (e.g., RAM or SLC flash)) first, release the busy line and perform the actual write to the non-volatile slower memory (e.g., TLC NAND Flash) in the background or upon flush command. The card may cache the host data during write and read operation. Cache size is card-implementation specific; flushing of contents stored in cache is done in less than one second. It is supported by OSs today for embedded memory devices and is assumed to be easy to implement for cards.

It seems like, for A1 cards, the _card_ has to do all the hard work in its controller to achieve the IOPS benchmarks, whereas on A2 cards, a lot of the heavy lifting would be offloaded to the device or operating system. This has a couple interesting implications:

  - A2 cards, if they are ever properly supported by devices like the Raspberry Pi, may have different behavior in situations where the power supply is inadequate. For older microSD cards, a common problem is data corruption if you use a low quality power supply (and this has become a bigger problem every generation of Pi—you need a good power supply or you'll have a lot of annoying problems).
  - A2 cards seem to sacrifice some performance when used with hardware which doesn't have A2 Command Queue and Cache functions, versus A1 cards, which offer the same random I/O performance on any device.

So unless and until more devices and operating systems support A2 functionality, it's best to avoid purchasing any A2 cards. If you buy an A1 card, you'll get better performance now, and quite possibly forever. A2 might not _technically_ be marketing BS, but in the real world, I stand by my assertion that it still is.

I haven't seen any indication there is work being done to add support in the Linux kernel, nor in the Raspberry Pi hardware, so I'd posit that, at least for most general computing purposes, the A1 and A2 designations from the SD Association are pretty meaningless, and you still have to rely on 3rd party testing to determine which cards give the best performance.
