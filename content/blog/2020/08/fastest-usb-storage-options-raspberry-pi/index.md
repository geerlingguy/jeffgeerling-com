---
nid: 3031
title: "The fastest USB storage options for Raspberry Pi"
slug: "fastest-usb-storage-options-raspberry-pi"
date: 2020-08-06T20:20:31+00:00
drupal:
  nid: 3031
  path: /blog/2020/fastest-usb-storage-options-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - benchmarks
  - flash
  - nvme
  - performance
  - raspberry pi
  - ssd
  - usb
---

For years, I've been maintaining [benchmarks for microSD cards on the Raspberry Pi](http://www.pidramble.com/wiki/benchmarks/microsd-cards), but I only spent a little time testing external USB storage, due to historic limitations with the Pi's USB 2.0 bus.

But the Pi 4 cleared away the limitations with a full-speed USB 3.0 bus offering much better performance, so I've done a lot of testing with USB boot, and with all the USB SSDs I had at my disposal. You can see some of those results in this [blog post and video on booting a Pi 4 via USB](/blog/2020/im-booting-my-raspberry-pi-4-usb-ssd).

After posting my tests concerning [UASP support in USB SATA adapters](/blog/2020/uasp-makes-raspberry-pi-4-disk-io-50-faster), I got an email from Rob Logan mentioning the performance of some other types of drives he had with him. And he even offered to ship a few drives to me for comparisons!

There's also a video that accompanies this blog post, for the more visually-inclined:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/lxuKqBYvDQs" frameborder='0' allowfullscreen></iframe></div>

So I took Rob up on the offer, and he sent me an XPG NVMe drive in a TDBT enclosure and an Arcanite AK58 USB 3.1 flash drive, touted by some as 'one of the fastest USB flash drives available'. I added a couple other drives to the test, pictured below:

{{< figure src="./all-flash-and-usb-drives-pi-4.jpeg" alt="Flash drives and USB SSD and NVMe from Arcanite Corsair TDBT XPG and Kingston with Raspberry Pi 4" width="600" height="398" class="insert-image" >}}

Clockwise, from the Inateck case in the top middle:

  - [Inatech SATA enclosure w/ UASP](https://www.amazon.com/gp/product/B00FCLG65U/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=e127daa32a0ea0e149f2d33561f8b048&language=en_US) and [Kingston 120 GB SSD](https://www.amazon.com/gp/product/B01N6JQS8C/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=2814de246bb8861d0270885665844b4e&language=en_US)
  - [TDBT M.2 NVMe Enclosure](https://www.amazon.com/TDBT-Enclosure-Thermal-Cooling-External/dp/B07TJT6W8K/ref=as_li_ss_tl?dchild=1&keywords=tdbt+nvme&qid=1596741190&s=electronics&sr=1-1&linkCode=ll1&tag=mmjjg-20&linkId=6cec59da75a3dc3f4a35f3bc73e6284b&language=en_US) and [XPG SX6000 Lite 128GB](https://www.amazon.com/XPG-SX6000-Gen3x4-1200MB-ASX6000LNP-128GT-C/dp/B07MTVVXG7/ref=as_li_ss_tl?dchild=1&keywords=XPG+SX6000+NVMe+128gb&qid=1596741302&sr=8-5&linkCode=ll1&tag=mmjjg-20&linkId=b9b79e9f18d27789d5a95dd7f614f3ba&language=en_US)
  - [Corsair Flash Voyager GTX 128GB flash drive](https://www.amazon.com/gp/product/B079NVJPKV/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=b00538595d19e1b64dd57f95b5f96464&language=en_US)
  - [Arcanite 128GB USB 3.1 flash drive](https://www.amazon.com/ARCANITE-128GB-USB-Flash-Drive/dp/B07RWPF43G/ref=as_li_ss_tl?crid=2JPBL5JYLH38D&dchild=1&keywords=arcanite+flash+drive&qid=1596741434&s=electronics&sprefix=arcanite+f,electronics,172&sr=1-3&linkCode=ll1&tag=mmjjg-20&linkId=15db12854dc233112f50a8ffd00d7762&language=en_US)
  - [SanDisk Ultra Flair 16GB USB 3.0 flash drive](https://www.amazon.com/gp/product/B015CH1GTO/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=770cb12016db16ce445cb01cd0fc45df&language=en_US)
  - [SanDisk Ultra Fit 128GB USB 3.0 flash drive](https://www.amazon.com/gp/product/B01BGTG2A0/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=5eac5a05452b63a93d6af0d9169a2774&language=en_US)
  - (Inside the Raspberry Pi) [Samsung Evo Plus 32GB microSD card](https://www.amazon.com/dp/B00WR4IJBE/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=66ba7843fd0583820d9dc304f5bdf732&language=en_US)

I ran benchmarks on every one of these drives, testing their sequential read and write performance with `hdparm` and `dd` (to test large file operations), as well as their random 4K read and write performance with `iozone` (to test more general usage patterns when booting or running apps on a Pi).

## Benchmark results

So how did all these drives perform? I ran all the tests booting the Pi from the device that was being tested, and I also ran the same benchmarks on my fastest microSD card, a Samsung Evo Plus.

### Sequential I/O performance

{{< figure src="./bench-1-sequential.png" alt="Sequential performance of different USB drives on Raspberry Pi" width="640" height="360" class="insert-image" >}}

The sequential results show a huge gap between the SSDs and fast new USB flash drives and the cheaper older-generation flash drives and the microSD card.

From what I've found, it seems like most USB flash drives perform the same as a microSD card in a USB adapter:

{{< figure src="./all-microsd-always-has-been.jpg" alt="Wait... its all microsd - always has been astronaut meme" width="624" height="351" class="insert-image" >}}

The Arcanite does well here, but it does lag a little bit behind the SSDs and even the Corsair GTX.

### Random I/O Performance

{{< figure src="./bench-2-random.png" alt="Random IO performance of different USB drives on Raspberry Pi" width="640" height="360" class="insert-image" >}}

Random IO performance paints a more complex picture. The performance of the older flash drives remains abysmal, with even the microSD card _trouncing_ them in random 4K write performance.

But the Arcanite also falls off quite a bit in comparison to the SSDs and the Corsair. And the XPG NMVe drive is at least twice as fast as every other option when it comes to random write performance.

So overall, it looks like a decent quality NVMe drive and USB enclosure is going to give the best overall performance. And the Corsair GTX is by far the fastest USB flash drive I've ever tested.

But there's one other test I wanted to do before closing the book on performance, and that's a 10 GB file copy over the network.

This test doesn't sustain the maximum sequential throughput for the drive, but it does take a long time and tests how well the different devices handle heat from constant write activity.

### Large file copy over network

> NOTE: This graph is a little misleading. I _believe_ that the scale should be 'Mbps', but I need to go back to my data and verify what exactly was measured, and re-generate the graph below. The relative scale is correct, however:

{{< figure src="./bench-3-network.png" alt="Large file network copy performance of different USB drives on Raspberry Pi" width="640" height="360" class="insert-image" >}}

This shows some interesting results. The Arcanite and the SanDisk Ultra Fit perform much worse for long-duration file copies than all the rest.

The Arcanite was only a tiny bit slower than the SSDs and the Corsair in the quick sequential tests, and the Ultra Fit was actually slightly faster than the Ultra Flair.

Why do they perform so much worse in this benchmark?

### Thermals

Well, I pulled out my Seek thermal camera and took a reading on the Ultra Fit:

{{< figure src="./ultra-fit-overheated.jpg" alt="Ultra fit gets very hot in thermal image" width="480" height="360" class="insert-image" >}}

I put some thermal tape on the tiny bit of metal that was exposed when it's plugged in, and the temperature measured over 60°C (140°F)!

The Arcanite's plastic body didn't measure quite so hot, but that's just the problem—plastic is a good thermal insulator, and that's why you often see it used in coolers. Metal, on the other hand, is good at dispersing heat, but you have to have enough area for the metal to disperse the heat, or the drive is going to get really hot.

The Arcanite's plastic body traps the heat inside, which leads to overheating, while the Ultra Fit's tiny profile doesn't leave enough room to dissipate heat.

Compare that to the much beefier Corsair GTX, which is larger (lots more surface area) and made of solid metal. Even under heavy write load, the Corsair kept its cool at 36°C (<100°F):

{{< figure src="./corsair-flash-even-heat.jpg" alt="Corsair Flash Voyager GTX thermal image" width="480" height="360" class="insert-image" >}}

When you look at the benchmarks on the packaging, or even benchmarks posted to Amazon reviews from CrystalDiskMark, remember most of them don't reflect the _true_ performance of these drives tested under real-world conditions.

SSDs and NVMe drives typically have a lot more surface area for heat dispersion, so they tend to perform more consistently since they can avoid overheating issues.

Most USB flash drives are designed more for compactness and convenience, and performance with general computing tasks or over long periods of time is usually more of an afterthought.

Usually, that is, unless we're talking about the Corsair—it's the first USB flash drive I've tested that compares favorably to USB SSDs!

## Price Comparison

But what about price?

What drive gives the most value? After all, the Corsair is $55, while the cheapest option, the SanDisk USB Fit, is about $7. When you go to buy a USB drive for your Pi, you want the best overall value, and you might want to sacrifice a little performance for a lot in savings!

So comparing all these drives (using the price for the 128 GB version), I came up with these two graphs:

{{< figure src="./bench-4-ppsequential.png" alt="Price vs performance sequential IO for flash drives for Raspberry Pi" width="640" height="360" class="insert-image" >}}

This graph compares how many dollars you have to spend per MB/sec on a large file copy. The Arcanite gives the best bang for your buck (assuming you're not constantly writing to it all day), with double the value of the SSDs or the Corsair GTX. The Kingston SSD comes in second... while the microSD and older SanDisk flash drives are a pretty poor choice when it comes to value for sequential access.

{{< figure src="./bench-5-pprandom.png" alt="Price vs performance random IO for flash drives for Raspberry Pi" width="640" height="360" class="insert-image" >}}

In this graph, showing value for random IO activity, the microSD card fares much better, but the older SanDisk flash drives are still a terrible value.

But the XPG NVMe (with an enclosure) becomes the best value, with the Kingston SSD and Corsair GTX in close pursuit. The Arcanite is a bit of a laggard, but it's still respectable with performance similar to the microSD drive.

## Conclusion

What do these values mean? Should you get the XPG drive or the Corsair for the best raw performance? Or should you stick with the Arcanite, which gives the best bang for the buck for sequential performance (in some conditions)?

Well, that's impossible for me to answer. If you're going to store large files on the drive, and use it as a media server or NAS, then an Arcanite might be the best option. If you want to run applications or use the Pi as a desktop, the NVMe and an enclosure is probably the best option.

Or, if you want the most portable Pi possible, using the least amount of space and energy, you might be willing to sacrifice a little more performance and stick with a reliable microSD card.

Or if you need even more performance, you might want to look at a different single board computer that offers built-in SATA or NVMe support.

In the end, it's really up to how you want to use your Raspberry Pi, I just hope this helps make your decision a little easier.

## More Information

I put all the raw performance data and benchmarks used in [this issue on the Raspberry Pi Dramble issue tracker](https://github.com/geerlingguy/raspberry-pi-dramble/issues/183).

Also, Rob sent me many more results for other drives he tested, and was generous enough to allow me to share some of those results. They are summarized in the table below:

| Drive                                | hdparm - sequential | 4k rand read | 4k rand write |
| ------------------------------------ | --------------- | ------------ | ------------- |
| [Inland Premium 256GB NVMe 3.0 x4 SSD](https://www.amazon.com/Inland-Premium-256GB-Internal-Solid/dp/B07P6STQ54/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=6ba4aa45a425f858d70987fa658ee831&language=en_US) | 308.46 | 19.41 | 31.80 |
| [SanDisk 128GB Extreme Pro USB 3.1 Flash Drive](https://www.amazon.com/SanDisk-SDCZ880-128G-G46-Extreme-128GB-Solid/dp/B01MU8TZRV/ref=as_li_ss_tl?dchild=1&keywords=SanDisk+128GB+Extreme+Pro+USB+3.1+Flash+Drive&qid=1596744767&s=electronics&sr=1-3&linkCode=ll1&tag=mmjjg-20&linkId=b8cf47d80a46226a2c312b9fd5da6894&language=en_US) | 221.08 | 10.96 | 11.51 |
| [eMMC 5.1 module](https://www.amazon.com/SmartFly-info-Sinlge-Computer-ODroid/dp/B08229QKV3?dchild=1&keywords=EMMC%2B5.1%2Bmodule&qid=1596744841&sr=8-6&th=1&linkCode=ll1&tag=mmjjg-20&linkId=f7a3957d883ab716e92e95e578f5f8eb&language=en_US&ref_=as_li_ss_tl) in [USB 3.1 adapter](https://www.amazon.com/dp/B07BHQ615Q/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=858e43f1d776cbb6cf4fdb7f0efc6478&language=en_US) | 113.11 | 8.28 | 4.84 |
| [Netac Z8 250GB SM2258XT](https://www.amazon.com/gp/product/B088BT9PKJ/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=69ac4bb010db0f3af87792449555f57a&language=en_US) | 299.05 | 20.48 | 31.47 |
| [Inland Pro 120GB PS3111-S11](https://www.amazon.com/Inland-Professional-120GB-Internal-Solid/dp/B076XMH2JT/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=18d2cb6a98eee2f8d4db869414daba15&language=en_US) | 313.05 | 18.59 | 24.66 |
| [eVtran 128GB ASM1153E](https://www.aliexpress.com/item/32940862928.html) | 334.49 | 19.14 | 29.40 |

And he sent over a few pictures of some of the drives he tested, one of which I'll share here, for your reference:

{{< figure src="./robs-tested-drives.jpg" alt="Drives Rob Logan tested - actually only a few of the ones he tested" width="600" height="501" class="insert-image" >}}
