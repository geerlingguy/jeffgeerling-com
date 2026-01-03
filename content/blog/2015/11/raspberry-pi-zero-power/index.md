---
nid: 2513
title: "Raspberry Pi Zero - Power Consumption Comparison"
slug: "raspberry-pi-zero-power"
date: 2015-11-27T19:59:46+00:00
drupal:
  nid: 2513
  path: /blogs/jeff-geerling/raspberry-pi-zero-power
  body_format: full_html
  redirects: []
tags:
  - arduino
  - comparison
  - consumption
  - power
  - raspberry pi
  - zero
aliases:
  - /blogs/jeff-geerling/raspberry-pi-zero-power
   - /blogs/jeff-geerling/raspberry-pi-zero-power
---

<blockquote><strong>tl;dr</strong>: The Raspberry Pi Zero uses about the same amount of power as the A+, and at least 50% less power than any other Pi (B+, 2 B, 3 B).</blockquote>

On November 26, the Raspberry Pi foundation announced the <a href="https://www.raspberrypi.org/blog/raspberry-pi-zero/">Raspberry Pi Zero</a>, a $5 USD computer that shares the same architecture as the original Raspberry Pi and A+/B+ models, with a slightly faster processor clock (1 Ghz), 512 MB of RAM, and sans many of the essential ports and connectors required for using the Pi as an out-of-the-box computer.

<p style="text-align: center;">{{< figure src="./pi-zero-new.jpg" alt="Raspberry Pi Zero - new with adapter cable" width="450" height="404" >}}
The Raspberry Pi Zero - quite a small Linux computer!</p>

If you're considering buying on Pi Zero and using it as a 'lite' desktop computer, you might want to rethink your strategy; the Pi model 2 B has four full-size USB 2.0 ports, a LAN port, full-size HDMI, audio/video out, and more. This little Zero just has one micro USB port and mini HDMI port (both require adapters for most uses), no network port, <s>no camera</s> (the latest Zero revision includes a mini camera connector!) or display connectors, and if you want a header for GPIO use, you have to solder one on yourself!

But this board <em>is</em> pretty awesome for some use cases, like embedded computing (think popping one into a halloween costume, or using a few in a robotics project), or experimentation where you don't want to worry about accidentally blowing up an expensive computer/control device (figuratively <em>or</em> literally!).

One of the most important questions, then, is how much power does the Pi Zero consume? If you want to use it in an embedded application, you need to make sure it's using as little power as possible.

<table style="text-align: center;">
<tr>
<td>
<p>{{< figure src="./pi-zero-power-consumption-max-boot.jpg" alt="Raspberry Pi Zero - Power consumption maximum during boot" width="300" height="220" >}}
Consumption stayed around 120-140mA during boot...</p>
</td>
<td>
<p>{{< figure src="./pi-zero-power-consumption-min-idle.jpg" alt="Raspberry Pi Zero - Power consumption minimum during idle" width="300" height="218" >}}
...and dropped to 50-70 mA during idle.</p>
</td>
</tr>
</table>

In the past, for the <a href="https://github.com/geerlingguy/raspberry-pi-dramble/wiki">Pi Dramble</a> project, I've measured <a href="https://github.com/geerlingguy/raspberry-pi-dramble/wiki/Power-Consumption">power consumption for all the other Pi models</a> I own (A+, B+, and model 2), so I thought I'd use my <a href="https://www.amazon.com/PowerJive-Voltage-Multimeter-chargers-capacity/dp/B013FANC9W/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=2fbe64dad50fdda17bcbb7a803c6b717">PowerJive USB Power Meter</a> to measure the usage for the Zero for comparison:

<table>
<thead>
<tr>
<th>Pi Model</th>
<th>Pi State</th>
<th>Power Consumption</th>
</tr>
</thead>
<tbody>
<tr>
<td>A+</td>
<td>Idle, HDMI disabled, LED disabled</td>
<td>80 mA (0.4W)</td>
</tr>
<tr>
<td>A+</td>
<td>Idle, HDMI disabled, LED disabled, USB WiFi adapter</td>
<td>160 mA (0.8W)</td>
</tr>
<tr>
<td>B+</td>
<td>Idle, HDMI disabled, LED disabled</td>
<td>180 mA (0.9W)</td>
</tr>
<tr>
<td>B+</td>
<td>Idle, HDMI disabled, LED disabled, USB WiFi adapter</td>
<td>	220 mA (1.1W)</td>
</tr>
<tr>
<td>model 2 B</td>
<td>Idle, HDMI disabled, LED disabled</td>
<td>200 mA (1.0W)</td>
</tr>
<tr>
<td>model 2 B</td>
<td>Idle, HDMI disabled, LED disabled, USB WiFi adapter</td>
<td>240 mA (1.2W)</td>
</tr>
<tr>
<td>Zero</td>
<td>Idle, HDMI disabled, LED disabled</td>
<td>80 mA (0.4W)</td>
</tr>
<tr>
<td>Zero</td>
<td>Idle, HDMI disabled, LED disabled, USB WiFi adapter</td>
<td>120 mA (0.7W)</td>
</tr>
</tbody>
</table>

As you can see in the table above, the Zero uses a similar amount of power as the long-time power-sipping champ, the A+—both use less than half the power of any other more fully-equipped Pi. This is no doubt due to the lack of extra ports and circuits that are active on the Pi itself. This means that a small battery pack (say, a flat Li-Ion pack rated at 1,400 mAh) should last well over 4 hours, even if you have moderate activity while using a cheap USB WiFi dongle!

If you don't need WiFi or some other network adapter, <a href="/blogs/jeff-geerling/controlling-both-pwr-and-act">disable the ACT/PWR LED</a>, <a href="/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy">follow these other Pi energy-saving tips</a>, and use a 2,000+ mAh battery pack (like one of the cheap ones you can get for phone charging), you can probably eke out a day's worth of Pi Zero usage, or more.

This isn't quite as good as you can get with an Arduino (sipping energy at 10-30 mA, or less if you optimize for power savings), but I'm a lot more likely to run Pi Zeros 24x7 for monitoring projects (as long as their networking needs are limited) than any other Pi model.

See related:

<ul>
<li><a href="/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy">Raspberry Pi Zero - Conserve power and reduce draw to 30mA</a></li>
<li><a href="http://www.pidramble.com/wiki/benchmarks/power-consumption">Raspberry Pi Power Consumption</a></li>
</ul>
