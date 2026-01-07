---
nid: 2511
title: "Raspberry Pi Zero - Conserve power and reduce draw to 80mA"
slug: "raspberry-pi-zero-conserve-energy"
date: 2015-11-30T02:55:13+00:00
drupal:
  nid: 2511
  path: /blogs/jeff-geerling/raspberry-pi-zero-conserve-energy
  body_format: full_html
  redirects: []
tags:
  - consumption
  - energy efficiency
  - power
  - raspberry pi
aliases:
  - /blogs/jeff-geerling/raspberry-pi-zero-conserve-energy
---

<blockquote><strong>Update 2015-12-01</strong>: I bought a <a href="http://www.amazon.com/gp/product/B013FANC9W">PowerJive USB power meter</a> and re-tested everything, and came up with ~80 mA instead of the ~30 mA reported by the Charger Doctor that I was using prior. This seems to be more in line with the results others were measuring with <em>much</em> more expensive/accurate meters in the Raspberry Pi forums: <a href="https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=127210&p=851245#p851245">Raspberry Pi Zero power consumption</a>. I've updated the numbers in the post below to reflect this change. Seems the Pi Zero is only incrementally better than the A+—still excellent news, but not nearly as amazing as I originally thought :(</blockquote>

<blockquote><strong>Update 2021-10-28</strong>: With the new Pi Zero 2 W, you can also <a href="/blog/2021/disabling-cores-reduce-pi-zero-2-ws-power-consumption-half">disable some of the CPU cores</a> to reduce power consumption for a heavily-utilized Pi if it doesn't need all the CPU cores running.</blockquote>

Yesterday my post <a href="/blogs/jeff-geerling/raspberry-pi-zero-power">comparing the Raspberry Pi Zero's power consumption to other Pis</a> hit the Hacker News front page, and commenters there offered a few suggestions that could be used to reduce the power draw even further, including disabling HDMI, changing the overclock settings, and futzing with the lone ACT LED.

<p style="text-align: center;">{{< figure src="./pi-zero-new.jpg" alt="Raspberry Pi Zero - new with adapter cable" width="450" height="404" >}}

I decided to spend some time testing these theoretical power-saving techniques on my Pi Zero, and here are some of the tips I've come up with (note that these techniques work with any Pi, not just the Zero):

<table border="0">
<thead>
<tr>
<th>Technique</th>
<th>Power Saved</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td width="20%">Disable HDMI</td>
<td width="20%">25mA</td>
<td width="60%">If you're running a headless Raspberry Pi, there's no need to power the display circuitry, and you can save a little power by running <code>/usr/bin/tvservice -o</code> (<code>-p</code> to re-enable). Add the line to <code>/etc/rc.local</code> to disable HDMI on boot.</td>
</tr>
<tr>
<td>Disable LEDs</td>
<td>5mA per LED</td>
<td>If you don't care to waste 5+ mA for each LED on your Raspberry Pi, you can <a href="/blogs/jeff-geerling/controlling-pwr-act-leds-raspberry-pi">disable the ACT LED</a> on the Pi Zero.</td>
</tr>
<tr>
<td>Minimize Accessories</td>
<td>50+ mA</td>
<td>Every active device you plug into the Raspberry Pi will consume some energy; even a mouse or a simple keyboard will eat up 50-100 mA! If you don't need it, don't plug it in.</td>
</tr>
<tr>
<td>Be Discerning with Software</td>
<td>100+ mA</td>
<td>If you're running five or six daemons on your Raspberry Pi, those daemons can waste energy as they cause the processor (or other subsystems) to wake and use extra power frequently. Unless you absolutely need something running, don't install it. Also consider using more power-efficient applications that don't require a large stack of software (e.g. LAMP/LEMP or LEMR) to run.</td>
</tr>
<tr>
<td>Turn off WiFi Radio (wireless models)</td>
<td>10+ mA</td>
<td>Disabling WiFi via `sudo rfkill block wifi` can save a little power, though for many applications this also removes the single communication protocol the Pi uses for things like IoT connections or remote control via SSH, so this is not always an option. Make the change persistent by adding the [`disable-bt` and `disable-wifi` overlays](https://github.com/raspberrypi/firmware/blob/2d08e8a2ae963819db9605b81f6cb366ec25acc0/boot/overlays/README#L701-L713) in your `/boot/config.txt`.</td>
</tr>
</tbody></table>

A few other seemingly obvious optimizations, like under-clocking the CPU, don't make a discernible impact on idle power consumption, and make a minimal difference in any real-world projects that I've measured. Do you have any other sneaky techniques to steal back a few mA?

For the Raspberry Pi Zero, I used all the above techniques, and here were the results:

<ol>
<li>Raspbian Jessie Lite nothing besides microSD card, and ACT LED on: <strong>100 mA @ idle</strong></li>
<li>Same as #1, but disable ACT LED and disable HDMI: <strong>80 mA @ idle</strong></li>
<li>Same as #1, but plug in a display, keyboard, trackpad, and WiFi adapter: <strong>310 mA @ idle</strong>(!!)</li>
</ol>

As you can see, it pays to conserve—if you don't need it, cut it away to save power! With the Pi Zero and these power saving techniques, you can extract a <em>lot</em> of usage even in low-power scenarios, like solar energy or running off a battery.

See related:

<ul>
<li><a href="/blogs/jeff-geerling/raspberry-pi-zero-power">Raspberry Pi Zero - Power Consumption Comparison</a></li>
</ul>
