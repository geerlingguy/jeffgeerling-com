---
nid: 2481
title: "Getting Gigabit Networking on a Raspberry Pi 2, 3 and B+"
slug: "getting-gigabit-networking"
date: 2015-02-17T04:11:41+00:00
drupal:
  nid: 2481
  path: /blogs/jeff-geerling/getting-gigabit-networking
  body_format: full_html
  redirects: []
tags:
  - gigabit
  - networking
  - performance
  - raspberry pi
  - usb
  - wifi
---

<blockquote><strong>tl;dr</strong> You can get Gigabit networking working on any current Raspberry Pi (A+, B+, Pi 2 model B, Pi 3 model B), and you can increase the throughput to at least 300+ Mbps (up from the standard 100 Mbps connection via built-in Ethernet).</blockquote>

<blockquote><strong>Note about model 3 B+</strong>: The Raspberry Pi 3 model B+ includes a Gigabit wired LAN adapter onboard—though it's still hampered by the USB 2.0 bus speed (so in real world use you get ~224 Mbps instead of ~950 Mbps). So if you have a 3 B+, there's no need to buy an external USB Gigabit adapter if you want to max out the wired networking speed!</blockquote>

<blockquote><strong>Note about model 4</strong>: The Raspberry Pi 4 model B finally has true Gigabit wired LAN, owing to it's new I/O architecture. If you're taxing the CPU and USB device bandwidth on the new USB 3.0 ports, you might not get consistent Gbps-range performance, but in my testing so far, the Pi 4 can sustain over 900 Mbps [with adequate cooling](//www.jeffgeerling.com/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one).</blockquote>

I received a shipment of some Raspberry Pi 2 model B computers for a project I'm working on (more on that to come!), and as part of my project, I've been performing a ton of benchmarks on every aspect of the 2, B+, and A+ Pis I have on hand—CPU, disk (microSD), external SSD, external HDD, memory, and networking.

I've tested the onboard LAN port (rated as 10/100 Fast Ethernet, and driven through the onboard USB 2.0 bus), and a few different 802.11n WiFi cards, and the raw throughput speeds ranged from ~45 Mbps with the 802.11n cards (with a very strong signal) to ~94 Mbps with the onboard LAN.

I then purchased a <a href="http://www.amazon.com/gp/product/B00FFJ0RKE/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00FFJ0RKE&linkCode=as2&tag=mmjjg-20&linkId=7QHY4ZTHOAC6B46S">TRENDnet USB 3.0 Gigabit adapter</a> from Amazon to test on my Pi. After configuring the interface by editing <code>/etc/network/interfaces</code> and adding a line for the new <code>eth1</code> adapter, I ran standard <code>iperf</code> benchmarks on all the interfaces and found the following results:

<ul>
<li>Internal LAN (10/100): 94.4 Mbits/sec (11.8 MB/sec)</li>
<li>USB 802.11n WiFi: 44.5 Mbits/sec (5.6 MB/sec)</li>
<li>USB Gigabit LAN (10/100/1000): 321 Mbits/sec (40 MB/sec)</li>
</ul>

(These were as measured on a Pi 3—the model 2 and B+ have slight speed differences which I'll enumerate in a chart below).

Or, in a nice graphical format (note that this chart is slightly out of date as of early 2016):

<p style="text-align: center;">{{< figure src="./raspberry-pi-network-interface-speed-comparison-gigabit.png" alt="Raspberry Pi Network Interface Speed Comparison - Internal LAN WiFi Gigabit" width="518" height="333" >}}</p>

For certain use cases, this more-than-doubled bandwidth can be extremely beneficial (e.g. streaming full-res HD video, streaming and processing large amounts of data, etc.). However, for many real-world use cases, the Pi's other subsystems (CPU and disk I/O especially, since I/O is on a single, shared USB 2.0 bus) will limit the available bandwidth.

If you're hungry for faster networking, and you can't wait until the Raspberry Pi 4 (or whatever starts including Gigabit Ethernet), know that you can more-than-double the built-in bandwidth capacity.

Here's an additional graph, comparing speeds between the B+/A+ and the model 2/3 (the onboard LAN has been dramatically improved, and I double-checked these results to confirm the increased download bandwidth!):

<p style="text-align: center;">{{< figure src="./network-speeds-raspberry-pi.png" alt="Raspberry Pi 2 and model B+ network throughput speed comparisons" width="718" height="396" >}}</p>

<h2>Real-world implications</h2>

In working on building a high-performance cluster of Raspberry Pi 3s for my <a href="https://github.com/geerlingguy/raspberry-pi-dramble">Dramble</a> cluster, I wanted to see just how scalable I could make the Nginx load balancer (which was also acting as a reverse proxy cache).

After making sure the Nginx configuration could support thousands of requests per second on the 4-core Pi, I discovered that I was easily able to saturate the onboard 10/100 LAN at about 95 Mbps serving cached content at around 1800 requests/second.

Switching to a Gigabit adapter <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/13#issuecomment-76218148">almost doubled the throughput</a>, and I was able to serve about 5000 requests/second at a rate of 200 Mbps!

So, if you need the raw throughput increase, using a USB 3.0 Gigabit adapter will definitely take you further than using onboard LAN—at the cost of slightly higher total power consumption and an unsightly dongle hanging off the Pi :)

Further reading:

<ul>
<li><a href="http://www.pidramble.com/wiki/benchmarks/networking">Benchmark various network configurations</a></li>
<li><a href="http://www.raspberrypi.org/forums/viewtopic.php?f=29&t=99235&p=696978#p696978">Pi2 - is the file transfer over ethernet better than B+ ?</a></li>
<li><a href="http://www.raspberrypi.org/forums/viewtopic.php?f=36&t=100991&p=699957#p699957">Dramatic onboard LAN upgrade in model 2?</a></li>
</ul>
