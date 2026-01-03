---
nid: 3129
title: "Raspberry Pi 4 model Bs arriving with newer 'C0' stepping"
slug: "raspberry-pi-4-model-bs-arriving-newer-c0-stepping"
date: 2021-09-27T20:04:40+00:00
drupal:
  nid: 3129
  path: /blog/2021/raspberry-pi-4-model-bs-arriving-newer-c0-stepping
  body_format: markdown
  redirects: []
tags:
  - bcm2711
  - compute module
  - cpu
  - pi 400
  - raspberry pi
  - stepping
---

Owing to a mishap with the Pi 4 model B I use for testing—more on how Red Shirt Jeff ruined that board later this week—I had to go buy a new Pi 4 last week.

The local Micro Center only had the 8 GB model in stock, so I went a little over budget and bought it. When I arrived home, I checked the board, and noticed a bit of a difference on the Broadcom SoC:

{{< figure src="./raspberry-pi-4-model-b-stepping-c0-bcm2711-macro.jpeg" alt="Raspberry Pi 4 model B C0 stepping on BCM2711 SoC" width="640" height="427" class="insert-image" >}}

Can you spot it? The model number of the BCM2711 chip on this board is `2711ZPKFSB06C0T`, which is the same as the chip found on the Pi 400.

This is a newer [stepping](https://en.wikipedia.org/wiki/Stepping_level) of the original Pi 4 model B chip, which has the model number `2711ZPKFSB06B0T`. The difference is the third-to-last character, the **C** versus the **B**.

Apparently 8 GB models may have had that version of the chip since their introduction in 2020, if [this GitHub comment by pelwell](https://github.com/raspberrypi/linux/issues/3210#issuecomment-680037065) is to be believed. But according to a few others, even the 2 GB model produced in the past year have this newer `C0` stepping:

<blockquote class="twitter-tweet" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">I found the invoice from April 13th, so that&#39;s the earliest date we know of this new SoC in a Pi 4B for now <a href="https://t.co/zLl5QfXRgm">pic.twitter.com/zLl5QfXRgm</a></p>&mdash; Lucas (@lululombard) <a href="https://twitter.com/lululombard/status/1442550344349671427?ref_src=twsrc%5Etfw">September 27, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

I covered the B0-vs-C0 stepping in an earlier post, my [Raspberry Pi 400 Teardown](/blog/2020/raspberry-pi-400-teardown-and-review), but I've learned a few new things that I'll mention here.

## Identifying the stepping on your Pi 4

If you want to see if you have the newer revision to the BCM2711 SoC on _your_ Pi, there are two ways.

The easiest, if you can take a peek at the SoC on top of the board, is to look at its model number. If it reads 'B0T' at the end, it's the older model. If it's 'C0T', its the newer model (like the one in the Pi 400):

{{< figure src="./Pi-400-BCM2711-SoC-Difference-C0-B07.jpeg" alt="Pi 4 model B and Pi 400 BCM2711 SoC Broadcom chip number difference" width="600" height="338" class="insert-image" >}}

If you can't see the top of the SoC (e.g. if you have it installed in a case), you can determine the revision in software.

From a [comment by `pelwell` on GitHub](https://github.com/raspberrypi/linux/issues/3210#issuecomment-680035201), you run the command `od -An -tx1 /proc/device-tree/emmc2bus/dma-ranges`, and it will give you different output depending on the stepping:

```
# B0
pi@raspberrypi:~$ od -An -tx1 /proc/device-tree/emmc2bus/dma-ranges
 00 00 00 00 c0 00 00 00 00 00 00 00 00 00 00 00
 40 00 00 00

# C0
pi@raspberrypi:~$ od -An -tx1 /proc/device-tree/emmc2bus/dma-ranges
 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
 fc 00 00 00
```

## What's new in the C0 stepping?

So the big question: what am I missing if I have the older B0 stepping? Fortunately, not much. A new stepping doesn't add new features like a faster processor, a better GPU, or more encoders. It represents an updated 'process', usually meaning some bugs in the silicon were fixed.

In the case of the BCM2711, it looks like the [two main fixes](https://github.com/raspberrypi/linux/issues/3210#issuecomment-680007995) are related to RAM addressing:

  1. The EMMC2 bus can only directly address the first 1GB.
  2. The PCIe interface can only directly address the first 3GB.

And this is probably why the chip first showed up 8 GB Pi 4 models, since it wouldn't affect the lower end models as much. And from [other forum posts](https://www.raspberrypi.org/forums/viewtopic.php?p=1880810#p1880597), it looks like there are also 'power gating improvements'.

I have seen more stable overclocks on CM4 and Pi 400 boards, and that's probably because the newer `C0` chips on them are able to handle higher clock speeds with very slightly improved thermals. Though I don't know if anyone will confirm that outside of anecdotal test data. And I don't have the budget to buy hundreds of boards to confirm whether that's just luck or an actual difference in older Pi 4s.

One thing to watch out for is any software that expects the `B0` stepping as a feature flag—like [`u-boot` did until earlier this year](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=255080)—having weird issues on newer Pi 4 model B boards. Software that relies on that level of detail is not too common, though, and none of the things I run on my Pis has had an issue.
