---
date: '2026-10-23T09:00:00-04:00'
tags: ['ubiquiti', 'unifi', 'air quality', 'co2', 'level2jeff', 'video', 'teardown']
title: "Ubiquiti's $99 Vape Detector is actually pretty good"
slug: 'ubiquiti-vape-detector-teardown'
---
Since learning about the effects of high CO2 concentration on attention and cognitive performance—especially at levels much higher than 2000ppm—I've started monitoring CO2 and other air quality indicators in my house, at my studio, and even on the road.

{{< figure
  src="up-air-quality-ubiquiti-vape-detector.jpg"
  alt="Ubiquiti Vape Detector and Air Quality Monitor"
  width="700"
  height="auto"
  class="insert-image"
>}}

I have a few other air quality monitors I'll be covering in the future, but today I wanted to focus on one I only heard about in the comments on a [recent video tearing down a cheap no-name 'Air Quality Detector' from Amazon](https://www.youtube.com/watch?v=t5yAZb5Blbs).

Pictured above is Ubiquiti's [UP-AirQuality](https://store.ui.com/us/en/products/up-airquality), their $99 "Vape Detection & Air Quality Sensor".

I'm used to paying $150-300 for decent-quality air quality monitors that include calibrated CO2 sensing. So a $99 price tag was an immediate red flag. Most cheaper monitors use synthetic readings to 'estimate' CO2, and can be wildly inaccurate.

But I bought one of these monitors, plugged it into my little [portable UniFi network](/blog/2026/mini-homelab-network-fits-in-carry-on/), and started testing it.

Before a full teardown, I wanted to see whether its sensors would match my [AirGradient](https://www.airgradient.com), [Aranet4](https://aranet.com/en/home/products/aranet4-home), and [Air Lab](/blog/2025/air-lab-flipper-zero-air-quality-monitors/) sensors—or at least be within ±50ppm.

To my surprise, it was pretty accurate.

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/bqBD8M_uYnE' frameborder='0' allowfullscreen></iframe></div>
</div>

At one point in the video above, I did the 'breath test'. I breathed directly into the sensor for 10-15 seconds, and observed the sensor readings.

For true CO2 monitors, the CO2 level will very quickly spike, but most other readings (besides humidity) should remain the same, with no corresponding spike.

{{< figure
  src="up-air-quality-co2-dashboard-graph.jpg"
  alt="Ubiquiti Air Quality Monitor CO2 graph"
  width="700"
  height="auto"
  class="insert-image"
>}}

And this must use an actual CO2 monitor, because the level quickly spiked from the ambient 600ppm to almost 4000ppm! (The LED ring around the base also switched from green to red at this point, a nice bit of visual feedback).

But to verify they weren't cheating somehow, I wanted to see the exact sensor they were using. And a quick teardown resulted in this discovery:

{{< figure
  src="sensiron-sen66-sensor.jpg"
  alt="Ubiquiti Air Quality Monitor Sensirion SEN66 sensor"
  width="700"
  height="auto"
  class="insert-image"
>}}

They incorporated the [Sensirion SEN66-SIN-T](https://sensirion.com/products/catalog/SEN66), an all-in-one air quality sensor for PM, RH/T, VOC, NOx and CO2. This was a sensor I'd never seen, and it looked pretty solid, especially compared to earlier generation products.

Usually a well-rounded air quality monitor has to incorporate a number of independent sensors—often incorporating different communication protocols and board footprint requirements.

The SEN66 puts all sensors in one box, on one I2C bus, with one small plug.

Ubiquiti put that device on one side, and separated it from the networking/PoE side with a wall of plastic, molded directly into the lid. The network side is thermally coupled to a large heat spreader attached to the top, and a complex light pipe lets you see the tiny multi-colored status LED on the network side of the puck.

The teardown required me to peel back the rubber strips used as feet, but I could re-stick them afterwards, and it was just four Phillips-head screws holding the top case on. (If you open one, make sure to carefully separate the top case, since the sensor is clipped into it, and plugged into the PCB on the bottom half.)

I was surprised Ubiquiti had the budget to include an air quality sensor that costs $62 (in single unit quantities, at least) in this product. DigiKey has them for $50 in larger quantities, but that still wouldn't leave a huge margin for a device like this.

It's my new favorite CO2 monitor for the price, with one major caveat: you can't use it standalone, like with any old network and Home Assistant. You have to have a Ubiquiti network controller running UniFi Protect. That gives you API access to the sensor data at least, but it means you can't just plug this into any PoE switch and go.
