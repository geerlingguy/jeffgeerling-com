---
date: '2026-06-24T09:00:00-05:00'
tags: ['framework', 'video', 'level2jeff', 'youtube', 'laptop', 'wisdpi', '10g', 'ethernet', 'usb-c']
title: "Framework's 10G Ethernet module exposes USB-C's complexity"
slug: 'framework-10g-ethernet-module-usb-c-complexity'
---
{{< figure
  src="./wisdpi-framework-10g-module.jpeg"
  alt="WisdPi's Framework 10G Ethernet module"
  width="700"
  height="auto"
  class="insert-image"
>}}

I've been following WisdPi's development of various [5 Gbps](https://www.youtube.com/watch?v=tRG_I_3VeTc) and [10 Gbps](/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/) Ethernet adapters for the past couple years.

They use newer Realtek Ethernet chips, which sometimes have performance quirks—most frequently encountered under Linux.

In today's video, I tested the new [WisdPi 10G Ethernet Expansion Card](https://frame.work/products/wisdpi-10g-ethernet-expansion-card) for Framework computers. It fits in any available Framework Expansion slot—even on the Framework Desktop.

But Expansion Cards use USB-C for their connection to the mainboard—and therein lies the rub...

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/fMXT6mEPR0Q' frameborder='0' allowfullscreen></iframe></div>
</div>

The main problem is USB-C's bandwidth complexity—especially when paired with the Realtek RTL8159 Ethernet controller, which requires USB 3.2 Gen 2x2 (20 Gbps) to get the full rated 10 Gbps speeds.

On many Framework laptops, you'll wind up getting considerably less than 10 Gbps (9.4 Gbps real-world max):

{{< figure
  src="./wisdpi-framework-10g-module-iperf-windows-7.3gbps.jpeg"
  alt="Windows 11 showing 7.4 Gbps with USB 3.2 Gen 2x1"
  width="700"
  height="auto"
  class="insert-image"
>}}

The above image shows the average bandwidth I get on Windows 11 on a Framework 13 with AMD's Ryzen AI 5 340. Linux fares slightly worse on that laptop, but it surprised me because [Framework's own port documentation](https://knowledgebase.frame.work/usb-port-definition-matrix-framework-laptop-13-HkHVUHaTge#:~:text=Framework%20Laptop%2013%20(AMD%20Ryzen™%20AI%20300%20Series)) for my laptop says it should support USB 3.2 Gen 2x2—at least on ports 1 and 3!

{{< figure
  src="./wisdpi-framework-10g-module-rtl8159-chip.jpeg"
  alt="Realtek RTL8159 chip on module"
  width="700"
  height="auto"
  class="insert-image"
>}}

The RTL8159 is bottlenecked on a many USB4 and all USB 3.2 Gen 2x1 connections. Unfortunately, that caps the bandwidth well under 8 Gbps.

{{< figure
  src="./framework-laptop-12-usb32-gen2x2-matrix.jpeg"
  alt="Framework Laptop 12 USB port definition matrix"
  width="700"
  height="auto"
  class="insert-image"
>}}

I tested on my Framework 12—with a slower Intel 13th Gen mobile CPU—and I found it _does_ support USB 3.2 Gen 2x2 speeds [as documented](https://knowledgebase.frame.work/en_us/search?q=usb+port+definition+matrix), and I _should_ get closer to 10 Gbps.

{{< figure
  src="./wisdpi-framework-10g-module-20gbps-usb-linux.jpeg"
  alt="USB 3.2 Gen 2 20000 mbps lsusb rating"
  width="700"
  height="auto"
  class="insert-image"
>}}

Except—at least in Linux—it didn't. The port showed up as `20000` Mbps (20 Gbps) via `lsusb`, but `iperf3` only got me 7 Gbps. I tried to download and compile the Realtek driver, but it errored out on Ubuntu 26.04, presumably because the Linux kernel in that distro (7.x) is too new.

So I switched to Windows 11, and after confirming the port showed up as Gen 2x2 with [USB Tree Viewer](https://www.uwe-sieber.de/usbtreeview_e.html), I got the same `iperf3` performance as in Linux—at least with the built-in driver.

On Windows, though, the Realtek driver installed without a problem, and I finally got the 9.4+ Gbps I was looking for:

{{< figure
  src="./wisdpi-framework-10g-module-iperf3-windows-realtek-driver-9.4gbps.jpeg"
  alt="9.4 Gbps on Windows 11 iperf3"
  width="700"
  height="auto"
  class="insert-image"
>}}

Doing a bidirectional test, I could get around 9 Gbps up, and 4-5 Gbps down, but after running these tests for a while, I ran into a _new_ issue. The module was getting _very_ hot. Enough that I pulled out my thermal camera to check on it:

{{< figure
  src="./wisdpi-framework-10g-module-heat-66C.jpeg"
  alt="WisdPi Framework 10G Ethernet module heat at 66C"
  width="700"
  height="auto"
  class="insert-image"
>}}

That's getting close to 70°C on the bottom plastic surface, and while it won't give you an immediate contact burn, it would certainly give you Toasted Skin Syndrome—something I remember hearing about back when [MacBook Pros would leave marks on users' legs](https://www.cultofmac.com/news/add-toasted-skin-syndrome-from-laptops-to-tech-hazards)!

I asked WisdPi about this, and they said the plastic surface temperatures is in compliance with [IEC 62368-1 temperature safety limits](https://regulatorydecoded.com/temperature-limits-in-product-design/). As long as you don't keep skin in contact with the surface for more than 10 seconds, you're good to go.

But this is a _laptop_. And I use it on my lap frequently! In fact, I'm writing this blog post on it from my couch...

{{< figure
  src="./wisdpi-framework-10g-module-blinkenlights.jpeg"
  alt="WisdPi Framework 10G Ethernet module blinkenlights"
  width="700"
  height="auto"
  class="insert-image"
>}}

Of course, 99% of the time I have it in my lap, I'm on WiFi. Also, the module itself extends a couple cm out from the laptop, so you have to remove it if you're using a laptop sleeve or have a snug-fitting bag.

So in terms of heat, my recommendation is to only use this module in scenarios where you won't be using it on your lap.

And in terms of getting the best performance, I've compiled the following chart, with bandwidth results from WisdPi's and my own tests, showing the best case scenario for different Framework computers:

{{< figure
  src="./wisdpi-framework-10g-throughput-tested.jpg"
  alt="WisdPi Framework 10G Ethernet module performance in various computers"
  width="700"
  height="auto"
  class="insert-image"
>}}

My recommendation for _most_ people, then, is to consider the regular ol' [Ethernet Expansion Card](https://frame.work/products/ethernet-expansion-card?v=FRACCTBZ00), which is good for 2.5 Gbps and costs about $40.

If you need something faster, and don't want an external USB-C dongle, then and only then should you consider the $99 [WisdPi 10G Card](https://frame.work/products/wisdpi-10g-ethernet-expansion-card). As of this writing, the card was out of stock.

The unit I tested was sent to me by WisdPi for testing and review.
