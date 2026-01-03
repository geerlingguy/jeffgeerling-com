---
nid: 3263
title: "How many AMD RX 7900 XTX's are defective?"
slug: "how-many-amd-rx-7900-xtxs-are-defective"
date: 2023-01-11T21:39:50+00:00
drupal:
  nid: 3263
  path: /blog/2023/how-many-amd-rx-7900-xtxs-are-defective
  body_format: markdown
  redirects: []
tags:
  - amd
  - broken
  - gpu
  - graphics
  - rx 7900 xt
  - testing
---

I'm working on a project—a very dumb project, mind you—and I was trying to acquire the two current-gen flagship GPUs: an Nvidia RTX 4090, and an AMD Radeon RX 7900 XTX.

In some weird stroke of luck (it has been difficult to find either in stock), I was able to get one of each this week.

{{< figure src="./rx7900xtx-versus-4090.jpeg" alt="AMD RX 7900 XTX Reference Sapphire edition versus Nvidia RTX 4090 Gigabyte boxes" width="700" height="467" class="insert-image" >}}

(lol at the size difference...)

Besides exorbitant price gouging, Nvidia's ownership of the crown in terms of GPU performance remains in this generation, as the 4090 blows past any competing card so far. But AMD's 7900 XTX was poised to be the best value in terms of price, performance, and efficiency (at least compared to any Nvidia offering).

Unfortunately, [many have experienced unexpected overheating on the 7900 XTX reference design](https://www.pcworld.com/article/1446335/amd-confirms-radeon-rx-7900-xtx-overheating-what-you-need-to-know.html), and [der8auer even went so far as to rip open a vapor chamber to get to the bottom of the issue](https://www.youtube.com/watch?v=rxaDZ6n2MNo).

AMD originally stated that 110°C junction temps were normal, but seemed to back off that statement as more evidence (like der8auer's videos) came to light demonstrating inadequate cooling only in a particular orientation.

When I got my 7900 XTX in the mail, I decided to run some tests. Light gaming on my 1080p monitor didn't seem to hit it too hard, but the card was getting pretty loud as the fans ramped up.

{{< figure src="./msi-kombustor-vertical-110c.jpeg" alt="MSI Kombustor GPU stress test 110 degrees C AMD RX 7900 XTX" width="700" height="467" class="insert-image" >}}

I then ran [MSI Kombustor](https://geeks3d.com/furmark/kombustor/)'s furmark donut test, which basically pushes the GPU to 100%. After less than 7 minutes, my card's 'junction temperature' hit 110°C, and I saw the GPU clocks and power draw drop about 5-7% as the poor fans struggled to keep up, ramping up to a loud 2900 rpm:

{{< figure src="./msi-kombustor-vertical-110c-closeup.jpeg" alt="MSI Kombustor GPU stress test 110 degrees C AMD RX 7900 XTX - closeup of stats" width="700" height="467" class="insert-image" >}}

This testing was done with the card installed in my PC in the horizontal orientation—that is, I have a tower PC, and the motherboard is vertical, with the 7900 XTX installed so the fans are parallel to the ground.

It seems that for a bit of time, the cooler can keep up, but after 5-7 minutes, there's just not enough cooling capacity in this orientation, as the vapor chamber _literally_ runs out of steam. (Or, well... water, I guess.)

So I shut down my computer, laid it on its side (so the graphics card was in the vertical orientation), and ran the tests again. This time, the fans were a quieter 1700 rpm, the max junction temperature was 92°C, and there was no throttling or power reduction for over 15 minutes:

{{< figure src="./msi-kombustor-horizontal-92c.jpeg" alt="MSI Kombustor GPU stress test 110 degrees C AMD RX 7900 XTX - PC horizontal, card vertical" width="700" height="467" class="insert-image" >}}

To be complete, I shut down the computer and re-tested in the vertical orientation, then again in horizontal, and the results were identical. With my PC in it's typical upright configuration, I could only get about 5 minutes of the 7900 XTX's full performance before it started throttling (and very loudly, at that!). If I lay my PC on its side, I could get full performance all day (with about half the noise).

Something was definitely wrong with the vapor chamber.

AMD said "customers experiencing this unexpected limitation should contact AMD support", but if you head to the support page, and call the US support phone number, it directs you to the warranty claims page on the website. On that page, it guides you through a wizard and determines if you didn't buy the AMD card from AMD.com itself, you have to contact the partner manufacturer (even though in this case it's the reference design, just packaged by Sapphire).

So I contacted Sapphire support, and got the following:

> This is a known issue for this card, you may contact your retailer for return and purchase a different version of the RX7900 series, Sapphire offers Pulse and Nitro series which do not exhibits this issue.

I asked if there was any way they could service the card or replace it, or even offer a paid upgrade to one of their own partner boards (like the aforementioned Pulse or Nitro). They responded:

> we do not handle that type of request here, only support and warranty service. Please continue to check retailers site for availability.

So off to NewEgg the return goes!

{{< figure src="./jeff-holding-sapphire-rx-7900-xtx.jpeg" alt="Jeff holding RX 7900 XTX Sapphire reference board box" width="700" height="525" class="insert-image" >}}

I guess I'll be sticking with [team green](https://qr.ae/pr2AfV) this round.

After seeing AMD's representative stating:

> We believe the issue is related to the thermal solution used in AMD’s reference design and is occurring in a limited number of cards sold.

...why are they not pulling cards off the shelves (and instructing partners to do so), if they know it is 'limited' in scope? If they truly know that, they should be able to narrow down the batch to a set of serial numbers that they could allow customers to check.

But if they don't actually know the scope of the problem—or if its a design flaw affecting all reference models—they should consider pulling all stock until they're fixed.

And maybe don't pass the buck to Sapphire, PowerColor, and other partners who have to give their customers a bad experience, since no comparable replacement cards can be had without paying scalpers on eBay.
