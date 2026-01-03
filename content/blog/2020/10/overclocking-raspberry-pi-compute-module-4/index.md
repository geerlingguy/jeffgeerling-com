---
nid: 3045
title: "Overclocking the Raspberry Pi Compute Module 4"
slug: "overclocking-raspberry-pi-compute-module-4"
date: 2020-10-20T21:07:25+00:00
drupal:
  nid: 3045
  path: /blog/2020/overclocking-raspberry-pi-compute-module-4
  body_format: markdown
  redirects: []
tags:
  - cm4
  - compute module
  - cpu
  - overclock
  - performance
  - raspberry pi
---

People have been overclocking Raspberry Pis since the beginning of time, and the Raspberry Pi 4 [is no exception](https://magpi.raspberrypi.org/articles/how-to-overclock-raspberry-pi-4).

I wanted to see if the Compute Module 4 (see my [full review here](/blog/2020/raspberry-pi-compute-module-4-review)) could handle overclocking the same way, and how fast I could get mine to run without crashing.

> There's a video version of this blog post, if you'd like to watch that instead:  
> [Raspberry Pi Compute Module 4 OVERCLOCKED](https://www.youtube.com/watch?v=YYDmaKP2m5M).

I have a giant [Noctua NF-P12](https://www.amazon.com/gp/product/B07CG2PGY6/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=b354ca8736e4f63d23785cf2473f179b&language=en_US) fan that I can plug right into the J17 4-pin fan connector built into the Compute Module 4 IO Board, and for all these tests I let it run full blast, moving a _lot_ of air over the board on my desk. Without active cooling, the SoC overheats pretty quickly under load—though you probably don't need _this_ much cooling!

{{< figure src="./raspberry-pi-cm4-noctua-fan-overclock-test-setup-image.jpeg" alt="Raspberry Pi Compute Module 4 CPU Overclock Setup with Noctua Fan" width="400" height="353" class="insert-image" >}}

At some point I'm going to work on a script that controls the fan's speed using the IO Board's built-in PWM-enabled fan controller chip which is accessible over I<sup>2</sup>C bus 10. But for now it's full speed ahead!

A few points of reference:

  - You can monitor the CPU frequency with: `watch -n 1 vcgencmd measure_clock arm`
  - You can monitor the CPU temperature with: `watch -n 1 vcgencmd measure_temp`
  - You can monitor whether the CPU is throttled with: `watch -n 1 vcgencmd get_throttled`

## Editing the config - setting up the overclock

I wanted to get a nice, clean 2.0 GHz out of my Compute Module; it's default clock maxes out at 1.5 GHz, and getting a solid 30% speedup feels pretty good to me—again, assuming an adequate amount of cooling, and a reliable power supply.

So I edited the `/boot/config.txt` file, and uncommented the `arm_freq=` line. I set that section of the file to contain the following:

```
#uncomment to overclock the arm. 700 MHz is the default.
over_voltage=6
arm_freq=2000
```

The `over_voltage` allows the Pi to give the SoC a little extra power, required when overclocking the CPU frequency. And the `arm_freq` sets a new maximum upper frequency limit. The highest allowed frequency is currently `2147` (2.147 GHz), though I'm not sure why it's capped at exactly that frequency (the docs and blog posts are mum on that topic).

You could also set the `gpu_freq=` value to up to `750` to boost the GPU clock, but I'm happy with a clean 2.0 GHz and the GPU bits running at their default 500 MHz frequency, so I saved and closed the boot config, then rebooted the Pi with `sudo reboot`.

> If you want to 'turn it up to 11' (go as fast as the Pi 4 / CM4 can go), set the following options:
> 
> ```
> over_voltage=6
> arm_freq=2147
> gpu_freq=750
> ```

Once rebooted, I monitored the frequency as I ran `sudo apt-get update`, and confirmed it reached up to 2.0 GHz under load:

```
$ vcgencmd measure_clock arm
frequency(48)=2000478464
```

> **Note**: If you set an overclock and your Pi fails to boot, you can plug in a keyboard and hold down the _Shift_ key while booting to disable overclock. Alternatively, pop the boot volume into another computer (or if using a CM4 with eMMC, set it in mass storage mode using [usbboot](https://github.com/raspberrypi/usbboot)), and comment out the overclock lines in the `/boot/config.txt` file.

## Testing the performance with Phoronix

I wanted to see how the performance at 2.0 GHz compared to 1.5 GHz, so I ran the same three tests using Phoronix that I did in my initial CM4 review, and here are the results:

{{< figure src="./cm4-overclock-2-ghz-benchmark-results.png" alt="Raspberry Pi Compute Module 4 2 GHz overclock benchmark results" width="631" height="519" class="insert-image" >}}

The speedup in each benchmark was almost exactly 28%, which is expected since the clock speed difference between 1.5 and 2.0 GHz is—you guessed it—28%!

> **Note**: If you want to run the exact same test suite, you can use the same benchmark shell script I used: [pi-general-benchmark.sh](https://gist.github.com/geerlingguy/570e13f4f81a40a5395688667b1f79af).

## Measuring the Temperature

During the benchmarks, I plotted the temperature by logging it to a CSV file every second with a really simple Python script:

```
from gpiozero import CPUTemperature
from time import sleep, strftime, time

with open("/home/pi/cpu_temp.csv", "a") as log:
	while True:
		cpu = CPUTemperature()
		log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(cpu.temperature)))
		sleep(1)
```

You can save that as `temp_log.py`, then run it with `python temp_log.py` in Terminal during the benchmarking.

And here's the temperature log during the Phoronix CPU benchmarking:

{{< figure src="./cpu-temperature-graph.png" alt="Raspberry Pi Compute Module 4 CPU temperature under load with overclock" width="600" height="371" class="insert-image" >}}

You can see that the temperature never went above 63°C, and I confirmed there was no throttling at any time. The CPU got the hottest during the first three H.264 compression tests, but was able to keep its cool (with the giant Noctua fan) throughout the other two tests, where it hovered around 40°C.

Here's a thermal image of the entire board when it was under the highest load:

{{< figure src="./thermal-image-55c-pi-compute-module-4.jpg" alt="Raspberry Pi Compute Module 4 55\u00b0C thermal image of SoC with kapton tape" width="480" height="360" class="insert-image" >}}

For this thermal image, I put a little kapton tape on top of the SoC so the temperature reading would be more accurate. It was only about two degrees lower than what `vcgencmd measure_temp` was reporting.

Just to test how quickly the Pi would overheat and throttle without any cooling (and no enclosure), I ran the same benchmark and measured the temperature:

{{< figure src="./cpu-temperature-graph-no-fan.png" alt="Raspberry Pi Compute Module 4 CPU Temperature overheat with no fan" width="600" height="371" class="insert-image" >}}

It only took about 3 minutes before the Pi started throttling the CPU to protect itself from overheating. So active cooling (or at least a massive heatsink) is a hard requirement when overclocking!

## Overclock and NVMe storage performance

One thing I remembered reading in almost all the posts about the SoC's overclocking abilities was that overclocking the GPU could also lead to increased performance in other areas besides just graphics rendering.

Stretching that idea a bit, I wondered if the CPU clock and performance affected the performance of NVMe storage via the PCIe lane at all—and much to my surprise, it did!

I re-ran all the disk performance benchmarks from my review with the 2.0 GHz overclock on my [Samsung 970 EVO Plus](https://www.amazon.com/gp/product/B07MG119KG/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=f52bc20e568b3539dce294b5eeae8c59&language=en_US) using [this NGFF PCIe NVMe adapter](https://www.amazon.com/gp/product/B07JQD2WBN/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=7691953624fce9784993c6082c80355d&language=en_US), and now the numbers for every type of disk operation saw a measurable improvement:

{{< figure src="./cm4-overclock-nvme-results.png" alt="Raspberry Pi Compute Module 4 NVMe overclocked performance benchmark" width="600" height="310" class="insert-image" >}}

I wanted to make sure the benchmark wasn't an anomaly, so I ran the same benchmarks (three times per benchmark) two times in each condition (e.g. run all benchmarks with no overclock, then with overclock, then without, etc.), and the numbers were within about 1% margin of error.

So I can say with some authority that if you want to make bleeding-edge NVMe storage _even faster_ than it already was on the stock Compute Module 4, overclock it to 2.0 GHz and you'll get an _extra 15% speedup_.

I also ran the benchmarks on the same drive over USB, but the results were the same with or without the overclock. That makes sense, since USB 3.0 runs with a different chip controlling the access (in my case, the VL805 inside my [Syba USB 3.0 PCIe card](https://www.amazon.com/gp/product/B019LHYSMI/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=838bdf08cf49b551234578c203b83850&language=en_US)).

## Conclusion

I think it's safe to say the Compute Module 4 hardware handles overclocking as well as a Pi 4 model B, which isn't surprising given that the chips are almost identical (even if the arrangement on the board is slightly more compact).

And if you want to have the fastest possible storage, you should overclock the CPU—and make sure you have some sort of cooling in place to prevent throttling.

Are there any other things you want me to test on the CM4? I'm planning on testing a few more PCIe cards, including a 1x Nvidia GPU and a 4x Intel NIC, and I'll definitely share the testing results when I get them!
