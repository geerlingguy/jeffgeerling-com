---
nid: 3049
title: "The Raspberry Pi 400 can be overclocked to 2.2 GHz"
slug: "raspberry-pi-400-can-be-overclocked-22-ghz"
date: 2020-11-02T22:34:06+00:00
drupal:
  nid: 3049
  path: /blog/2020/raspberry-pi-400-can-be-overclocked-22-ghz
  body_format: markdown
  redirects:
    - /blog/2020/how-much-can-raspberry-pi-400-be-overclocked-and-other-questions
aliases:
  - /blog/2020/how-much-can-raspberry-pi-400-be-overclocked-and-other-questions
tags:
  - overclock
  - performance
  - pi 400
  - raspberry pi
  - video
  - youtube
---

After the [Raspberry Pi 400](https://www.raspberrypi.org/products/raspberry-pi-400/) was launched earlier this morning, there was a lot of discussion over the thermals and performance of the upgraded 1.8 GHz System on a Chip inside:

{{< figure src="./Pi-400-BCM2711-SoC-Difference-C0-B07.jpeg" alt="Pi 4 model B and Pi 400 BCM2711 SoC Broadcom chip number difference" width="600" height="338" class="insert-image" >}}

I wanted to spend a little time in this post testing overclocking, performance, power consumption, and thermals in depth.

## Video version

There is also a video that goes along with this post, if you're more visually-inclined:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/b7_RkCkaJjE" frameborder='0' allowfullscreen></iframe></div>

## Thermal Performance at 1.8 GHz

A few other reviewers did some tests (like [Explaining Computers](https://www.youtube.com/watch?v=P1E5xszQqV8&list=PLcd1Q0-YkB1euCFXbFXgAQYy9ZCig6-eA&index=1)) and found the Pi 400 was able to stay cooler than a Pi 4 inside a [Flirc passive heat sink case](https://www.amazon.com/Flirc-Raspberry-Pi-Case-Silver/dp/B07WG4DW52/ref=as_li_ss_tl?crid=QWQ4BCURT0RB&cv_ct_cx=flirc+case+raspberry+pi+4&dchild=1&keywords=flirc+case+raspberry+pi+4&pd_rd_i=B07WG4DW52&pd_rd_r=1993ae7d-0466-42dd-903c-8e9337cb283a&pd_rd_w=GyXPS&pd_rd_wg=SQnaO&pf_rd_p=5be4970c-0256-4afe-9550-68021bd84e5b&pf_rd_r=MBE7A582808HDTCKZDA6&psc=1&qid=1604336339&sprefix=flirc+,aps,173&sr=1-1-791c2399-d602-4248-afbb-8a79de2d236f&linkCode=ll1&tag=mmjjg-20&linkId=e134dc9286474ccc9ffb186a5fed28b5&language=en_US), but was not quite as cool as a Pi 4 running with an [ICE cooling tower](https://www.amazon.com/GeeekPi-Raspberry-Cooling-Cooler-Heatsink/dp/B07V35SXMC/ref=as_li_ss_tl?crid=34RW3JJELJ85J&dchild=1&keywords=ice+cooler+raspberry+pi&qid=1604336383&s=electronics&sprefix=ice+c,electronics,172&sr=1-2&linkCode=ll1&tag=mmjjg-20&linkId=cb9dab820b0542a5be217330c48cde79&language=en_US).

I wanted to see if there's any level at which the CPU gets near throttling, so I set up a test scenario and started measuring temperatures, both internally and with my [Seek IR camera](https://www.amazon.com/Seek-Thermal-Compact-All-Purpose-Imaging/dp/B00NYWABAA/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=875a500c0e5c7d83bd23a33e16bd6e29&language=en_US).

I took a thermal image of the board before running any tests:

{{< figure src="./pi400-keyboard-idle-1.8ghz.jpeg" alt="Pi 400 idle - thermal IR image" width="480" height="360" class="insert-image" >}}

At idle, the exterior of the keyboard is indistinguishable from the environment around it. Plastic isn't the best thermal conductor, and later I found that most of the heat output goes through the ports in the back and the vent on the bottom.

And then I started dumping temperature data into a CSV file with the command:

```
while :; do echo `date +"%Y-%m-%d %T"`','`vcgencmd measure_temp | tail -c +6 | sed "s/'C//g"` >> temperatures.csv; sleep 1; done
```

I kicked off `stress-ng` to load up all the four CPU cores on the Pi, and let it run for 30 minutes at the default 1.8 GHz clock on the Pi 400:

```
sudo apt install -y stress-ng  # if it's not already installed
stress-ng -c 4
```

And here's a graph of the temperature over 30 minutes:

{{< figure src="./pi400-cpu-temp-1800.png" alt="Pi 400 temperature over 30 minutes of CPU stress" width="600" height="371" class="insert-image" >}}

The maximum temperature it reached was 52°C, though the surface of the keyboard never went above 31°C:

{{< figure src="./pi400-keyboard-stress-1.8ghz.jpeg" alt="Pi 400 Keyboard stress 1.8 GHz IR thermal camera" width="480" height="360" class="insert-image" >}}

The bottom was _very slightly_ warm, and the ports on the back were warm to the touch, but not even close to the painful 'ouch' I would get touching some parts on the Pi 4 under load!

## Overclocking to 2.2 GHz

So... the Pi 400 is the first Pi I'm able to reliably run at more than 2.147 GHz. After reading [this Tom's Hardware review of the Pi 400](https://www.tomshardware.com/news/raspberry-pi-400-review-faster-cpu-new-layout-better-thermals), I noted that Les Pounder was able to get the chip to run at 2.2 GHz.

My first attempt to overclock to 2.147 GHz, by setting the following in `/boot/config.txt`, resulted in a Pi that would only boot halfway then get locked up:

```
over_voltage=6
arm_freq=2147
```

If could set `arm_freq=2000` successfully, but I figured I should _go big or go home_. I figured it was a power issue, and to set `over_voltage` higher than 6, I had to set `force_turbo=1`.

```
force_turbo=1
over_voltage=8
arm_freq=2200
```

And now it booted up and ran at 2.2 GHz, just like in the Tom's Hardware review!

> **NOTE**: [Setting `force_turbo` may _void your warranty_](https://www.raspberrypi.org/documentation/configuration/config-txt/overclocking.md)—do this at your own risk!

I ran the same `stress-ng` test for a full 30 minutes, and here's the temperature graph:

{{< figure src="./pi400-cpu-temp-2200.png" alt="Raspberry Pi 400 temperature over 30 minutes of CPU stress - 2.2 GHz clock" width="600" height="371" class="insert-image" >}}

It reached a peak of 63°C, which is still well under the throttling temperature. For comparison, check out the same graph from my [overclocked benchmarks on the Compute Module 4](/blog/2020/overclocking-raspberry-pi-compute-module-4), with a massive fan (but no heat sink):

{{< figure src="./cpu-temperature-graph.png" alt="CPU temperature graph - Compute Module 4" class="insert-image" >}}

And _without_ a fan, the CM4 behaves like a Pi 4 model B, and reaches 75°C and beyond, throttling the CPU after a while. It's great to see the passively-cooled Pi 400 can keep from throttling, even overclocked to 2.2 GHz!

Here's a thermal image after 30 minutes of `stress-ng` at 2.2 GHz:

{{< figure src="./pi400-keyboard-stress-2.2ghz.jpeg" alt="Pi 400 Keyboard stress 2.2 GHz IR thermal camera" width="480" height="360" class="insert-image" >}}

The top was very slightly warm, though still not an issue at all. The bottom was noticeably warm now, like the back of my phone when I use it to watch some streaming videos for a while, but not uncomfortably so. The ports on the back still showed the highest external temps overall, at 42°C:

{{< figure src="./pi400-keyboard-stress-ports-2.2ghz.jpeg" alt="Raspberry Pi 400 external ports 42 degrees Celcius thermal IR camera" width="480" height="360" class="insert-image" >}}

Another important difference from the Pi 4 model B: it seems like the microSD card itself doesn't get quite as hot either (though I only measured by touch), maybe due to the fact that the SoC's heat is transferred out more through the heat sink than the Pi's board itself.

## Performance (Phoronix Benchmarks)

I also ran a set of Phoronix CPU benchmarks—specifically, [this benchmark](https://gist.github.com/geerlingguy/570e13f4f81a40a5395688667b1f79af) that I have been running on all the Pi 4 series computers—and here are the results at 2.2 GHz, compared to an actively-cooled Pi Compute Module 4 running at 1.5 and 2.0 GHz:

{{< figure src="./phoronix-benchmarks-pi400-2_2_ghz.png" alt="Phoronix Raspberry Pi 400 2.2 GHz benchmarks compared to 1.5 and 2.0 GHz Compute Module 4" width="632" height="531" class="insert-image" >}}

Performance scales pretty much linearly with respect to the clock speed, which is to be expected with the exact same CPU architecture.

I did some testing with YouTube, and found that playing back videos at 1080p was much more enjoyable at the 2.2 GHz clock, though doing things like switching between fullscreen playback and windowed playback was still a bit slow.

## Power Consumption

I also measured the average power consumption while the CPU was at 1.8 and 2.2 GHz, and it looks like it's close, though the 2.2 GHz clock with `force_turbo` uses about 0.01A more power at idle, and 0.10A more power at full tilt.

All measurements were taken with my [Satechi USB-C Power Meter](https://www.amazon.com/gp/product/B01MT8MC3N/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=98fb364b153ab0cc4123a6e7585904c0&language=en_US).

Here's idle power consumption, first for the 1.8 GHz clock, and then for the 2.2 GHz clock:

{{< figure src="./pi400-idle-1_8ghz-500mA.jpeg" alt=".50A power consumption on Pi 400 at 1.8 GHz" width="500" height="334" class="insert-image" >}}

{{< figure src="./pi400-idle-2_2ghz-510mA.jpeg" alt=".51A power consumption on Pi 400 at 2.2 GHz" width="500" height="334" class="insert-image" >}}

And here's power consumption at both speeds when running `stress-ng`:

{{< figure src="./pi400-stress-1_8ghz-1200mA.jpeg" alt="Pi 400 power consumption at 1.8 GHz stress-ng" width="500" height="334" class="insert-image" >}}

{{< figure src="./pi400-stress-2_2ghz-1300mA.jpeg" alt="Pi 400 power consumption at 2.2 GHz stress-ng" width="500" height="334" class="insert-image" >}}

## Overclocking beyond 2.2 GHz

I don't think you can go beyond 2.2 GHz, at least not for now. I tried 2.4, 2.3, and 2.21 and none of those resulted in a full boot. I went back to 2.2 GHz and the Pi 400 seems to be running stable, at least after a few hours of use.

The design of the Pi 400's giant heat sink lets you run the Pi 400 with any workload and not really run into the danger of overheating. It looks like the thermal design of this Pi is the best yet—with the caveat that the other Pis to this point have had no real heat sink or fan included!
