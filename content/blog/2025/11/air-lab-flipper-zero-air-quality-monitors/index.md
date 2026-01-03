---
nid: 3513
title: "Air Lab is the Flipper Zero of air quality monitors"
slug: "air-lab-flipper-zero-air-quality-monitors"
date: 2025-11-21T15:02:27+00:00
drupal:
  nid: 3513
  path: /blog/2025/air-lab-flipper-zero-air-quality-monitors
  body_format: markdown
  redirects: []
tags:
  - air lab
  - air quality
  - co2
  - home assistant
  - iot
  - monitoring
  - reviews
  - video
---

{{< figure src="./air-lab-aqi-monitor-hero.jpeg" alt="Air Lab AQI Monitor Professor Robin" width="700" height="394" class="insert-image" >}}

This air quality monitor costs $250. It's called the [Air Lab](https://networkedartifacts.com/airlab), and I've been using it to measure the air in my car, home, studio, and a few events over the past few months. And in using it over the course of a road trip I learned to not run recirculate in my car quite as often—more on that later.

[Networked Artifacts](https://networkedartifacts.com) built in some personality:

  - The top surface is a nicely-silkscreened white PCB with exposed SMD buttons
  - It has a large e-paper display
  - The UI includes 'Professor Robin', a quirky scientist who teaches about air quality in small quips.

Overall, it's pretty nice.

But _$250_ nice? That's the question I hope I can answer for you.

This one was sent to me for review, and I like to think of it as like the Flipper Zero of air quality measurement. Air Lab reads CO2, NOx, VOCs, Temperature, Humidity, and Pressure, and it'll log all that data for you wherever you take it.

{{< figure src="./air-lab-studio-data_0.jpg" alt="Air Lab Studio" width="700" height="394" class="insert-image" >}}

When you're back at your computer, you can plug it in and save that data however you like, so it's not locked down or tied to one company's cloud platform, like AirThings.

It can publish the air quality data in real time over [WiFi to Home Assistant](https://www.crowdsupply.com/networked-artifacts/air-lab/updates/a-deep-dive-into-integrating-air-lab-with-home-assistant) or wherever you want using MQTT, and the software and hardware are already very polished for this to be a pre-release device.

## AirGradient ONE at Home

{{< figure src="./airgradient-one-on-desk.jpg" alt="AirGradient ONE on desk" width="700" height="394" class="insert-image" >}}

This is an [AirGradient One](https://www.airgradient.com/indoor/#comparison). It costs a _little_ less, at $230, but I bought _this_ one to set up in my baby's room, to make sure there's enough ventilation in there.

I have some at my studio, too, and I feed them all into Home Assistant, where I built this air quality monitoring dashboard, using ApexCharts:

{{< figure src="./home-assistant-air-quality-dashboard.jpg" alt="Home Assistant Air Quality Dashboard" width="700" height="470" class="insert-image" >}}

Getting back to the basics, why is this type of monitoring important? Well, for me specifically, I use CO2 as a proxy for stale air. If your CO2 concentration is too high (not to mention other particulates, which the AirGradient measures, but the Air Lab doesn't, at least not directly), you can have [_noticeably worse_ mental function](https://pmc.ncbi.nlm.nih.gov/articles/PMC3548274/). As someone who's been stuck in far too many stuffy meeting rooms before... I don't need a study to tell me that.

But as a point of comparison, to set up an AirGradient ONE, you:

  1. Plug in USB-C power
  2. Connect to the WiFi hotspot indicated on the display
  3. Provide your WiFi credentials
  4. Automatically configure it in Home Assistant Integrations (or configure it to send data to [AirGradient's cloud dashboard](https://app.airgradient.com/auth/signin))

You don't need to use their cloud at all, if you don't want to (and indeed, I do not).

If you're interested in seeing the _entire_ setup process, step-by-step, I've included that (along with a little more background on the rest of my Air Lab testing) in this YouTube video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/r21lvaw40nY" frameborder='0' allowfullscreen></iframe></div>
</div>

## Air Lab First Impressions

The Air Lab has a similarly-easy setup process, and can also be used independent of the 'cloud'.

The setup process:

  1. When you open the box, the e-paper display instructs you to plug in USB-C power and press 'A'
  2. The device asks the time, then it asks you to place it outside for a short time for calibration
  3. Bring it inside, and it's ready to go!

You can log data and access it on your computer directly, through the [Air Lab Console](https://studio.networkedartifacts.com/airlab/console). You can also use the console to set up MQTT and Home Assistant integration, though I didn't do that on mine, since I'm mostly using it for measurements outside of my home and studio.

{{< figure src="./air-lab-studio-data-2.jpg" alt="Air Lab Studio - another dataset" width="700" height="394" class="insert-image" >}}

I don't have lab-grade CO2 reference equipment, so I can't give any absolute ratings of the device, but I can say it was within 50-100 ppm of the various AirGradient monitors I tested, and the sensor in use is a [Sensiron SCD41](https://sensirion.com/products/catalog/SCD41), which seems pretty decent. ([All the sensors in use are listed here](https://networkedartifacts.com/airlab#specs).

## Air Lab Field Testing

I took the Air Lab to a friend's party, an outdoor event, and even a St. Louis Blues hockey game, in an indoor arena.

I found some interesting things:

  - At my friend's party, in a relatively small house with 15-20 people, the CO2 levels went beyond 2300 ppm, which is not horrible, but is at a level where I'm able to notice a slight bit of drowsiness or 'brain fog'. Not much, but more than nothing. Their AC was running, but even though the house was a little older and probably 'leaky', it didn't exchange fresh air at a rate that could keep up with the humans breathing inside.
  - The stadium had a much slower rise in CO2 levels, but it was measurable, and consistent with the crowd entering, and then peaked right before the end of the game as many people started leaving.

I also brought the Air Lab around town in my car, to see how different A/C modes would fare:

  - When driving with my wife and kids in our minivan, with recirculate on, the car would very quickly rise to 1800-2000 ppm almost every time we took a trip (even a 5-10 minute trip).
  - When driving alone or with just one other person, with recirculate on, my Leaf would get up to 1500-1800 ppm.

I even took the Air Lab on my road trip to and from Chicago, and wound up seeing 1800 ppm or so in traffic on the highway, and 1500-1600 ppm on average while I was driving normally (all of these numbers with **recirculate on**).

Turning recirculate off always brought the number _way_ down, usually around 100 ppm higher than ambient outdoor CO2 levels—so 480-600 ppm, typically.

{{< figure src="./air-lab-car-recirculate-button.jpg" alt="Air Lab in car - AC Recirculate button lit" width="700" height="394" class="insert-image" >}}

I think the main takeaway for me is to leave recirculate _off_ unless there's a good reason to not enjoy some fresh air (e.g. if driving through an industrial area, or behind a very emissive car), or if you're really trying to preserve conditioned air for humidity or maybe efficiency reasons.

I was a little surprised the ppm in both our minivan and my Leaf topped out under 2000 ppm. I'm guessing they naturally leak / exchange some outside air as a baseline, even with recirculate on?

During these tests, I did have some data from a manual measurement go missing, but that was found to be a firmware bug, and has since been fixed.

## Inside a large convention hall

I mentioned the Blues game earlier, but I also brought the Air Lab with me to VCF Midwest up in Chicago. That's where I was going on the road trip.

{{< figure src="./vcf-midwest-convention-center.jpg" alt="VCF Midwest convention center" width="700" height="394" class="insert-image" >}}

You'd _think_ with all that space in such a new building, stale air wouldn't be a problem. But even there, I saw the numbers going up as the day went on.

So maybe part of that tired feeling you get after a full day at a convention is made just a little bit worse by the stale air. At least that's my theory. It's definitely something I'm more aware of now.

I found myself going outside to get fresh air more often, just because I was aware of the numbers.

Is that a good idea regardless? Sure. But you don't know what you can't measure, and I like being able to put some numbers behind my intuition.

{{< figure src="./air-lab-dead-battery.jpg" alt="Air Lab dead battery" width="700" height="394" class="insert-image" >}}

The battery life is pretty good, too. The first test I did, I got almost five full days. I only noticed it was dead when I clicked the buttons and didn't get a response. It does have a tiny battery indicator, but one improvement could be a message that pops on the screen before the battery goes dead.

## Conclusion

Could you build your own portable air quality monitoring device for less money, using the same sensors Air Lab uses? Yes.

{{< figure src="./air-lab-open-back.jpg" alt="Air Lab open back sensors" width="700" height="488" class="insert-image" >}}

If you have the time and skills, DIY is always cheaper.

But when I wore it on my badge at VCF Midwest, it provoked many conversations. People were intrigued by the idea of measuring air quality on a small battery powered device. And it looks _cool_, especially to other techies.

But I asked every person I talked to: "Is it _$250 cool_?" All but two of them said: "No".

That's the curse of new hardware and a small startup like Networked Artifacts. It's impossible to reach the economies of scale giant corporations do.

So do I think $250 is a lot? Yes. But do I think it's _too much_? No. For me, if you get into a device like this, it's partly for the device, and partly to back the _idea_.

{{< figure src="./air-lab-hero.jpeg" alt="Air Lab on desktop" width="700" height="467" class="insert-image" >}}

It's a fun, quirky, and imperfect battery-powered air quality monitor. And it's not cheap.

But I can get my data off of it without any cloud tie-in, and the team already has better firmware for it than most commercial products.

The one featured in this post was provided for review, and they told me to keep it. So take anything I say with a grain of salt. And maybe a few deep breaths of your wonderful, stuffy air.
