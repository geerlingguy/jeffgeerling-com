---
nid: 3220
title: "The Raspberry Pi Pico W brings WiFi for $6"
slug: "raspberry-pi-pico-w-brings-wifi-6"
date: 2022-06-30T06:59:48+00:00
drupal:
  nid: 3220
  path: /blog/2022/raspberry-pi-pico-w-brings-wifi-6
  body_format: markdown
  redirects: []
tags:
  - arduino
  - esphome
  - microcontroller
  - pico
  - raspberry pi
  - wifi
---

Today, Raspberry Pi announced the [Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/), a new $6 version of the Pico that includes WiFi.

{{< figure src="./raspberry-pi-pico-w.jpeg" alt="Raspberry Pi Pico W on breadboard" width="700" height="467" class="insert-image" >}}

No word yet on Bluetooth. The WiFi chip in the Pico W ([Infineon CYW43439](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw43439/)) supports it, but right now the RP2040 firmware lacks Bluetooth support.

The Pico W being available for just $6 is huge, because one of the chief complaints about the original Pico (powered by Raspberry Pi's own RP2040) was its lack of wireless support—a feature present on similarly-priced boards based on the ESP32 and ESP8266.

A little over a year later, we're in the midst of a historic electronic components shortage, and the RP2040 has achieved massive success in part because of it's design, but most especially due to one feature few rivals have right now: _widespread availability_.

There have been a few boards that marry the RP2040 to WiFi, like the [Wio RP2040](https://www.seeedstudio.com/Wio-RP2040-Module-p-4932.html) and the [Arduino Nano RP2040 Connect](https://amzn.to/3y66dQV), but you usually have to pay a bit more for those—and you might not need some of their more specialized features, like 16 MB of flash storage.

> **Video**: I also have a video about the Pico W on YouTube: [The new Raspberry Pi Pico W is just $6](https://www.youtube.com/watch?v=VEWdxvIphnI).

## Building a Wireless Garage Door Sensor

I was sent a single Pico W for pre-launch testing, and I've been putting it through it's paces. I'm by no means a microcontroller genius, but I can program enough in MicroPython to be dangerous.

My first Pico W project is a wireless garage door sensor, one which I hope to attach to my local Home Assistant setup. That way when I'll be one step ahead of my wife so she doesn't have to complain when I forget I left the garage door up all day!

I'm working on that project here: [Pico W Garage Door Sensor](https://github.com/geerlingguy/pico-w-garage-door-sensor), and the MicroPython code to connect to WiFi is:

```
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140)  # Diable powersave mode
wlan.connect('ssid', 'password')
```

My [`garage-door.py` script](https://github.com/geerlingguy/pico-w-garage-door-sensor/blob/master/micropython/garage-door.py) makes use of the `uasyncio` library to both run a webserver (for garage door status) and display the garage door state on the Pico W's built-in LED.

But you can use `socket` or whatever other method you want in MicroPython to either serve web requests or make your own requests to external services. And if you use the C SDK, you can make use of the Lightweight IP (`lwip`) library.

I'll have more to come on my Pico W Garage Door Sensor project soon.

## WiFi Performance

Since it runs MicroPython, I hopped in the Pico W's Python shell via Thonny IDE, and installed and ran `uiperf3`:

```
# Install uiperf3
>>> import network
>>> wlan = network.WLAN(network.STA_IF)
>>> wlan.active(True)
>>> wlan.connect('Wireless Network', 'The Password')
>>> import upip
>>> upip.install("uiperf3")

# Run benchmark
>>> import uiperf3
>>> uiperf3.client('10.0.100.110')
```

I was able to get a little over 9 Mbps when near my 2.4 GHz base station, and about 6 Mbps when I was at the farthest point in my house. The connection speeds were fairly stable, though the Pico was not in any enclosure during my testing. There's no way to add an external antenna like you could on the Compute Module 4.

The default WiFi mode, with powersave enabled, resulted in a lot of jitter when I was running a continuous ping:

```
round-trip min/avg/max/stddev = 20.522/74.713/149.913/32.277 ms
```

If I disabled powersave with `wlan.config(pm = 0xa11140)`, then the ping times were much more stable:

```
round-trip min/avg/max/stddev = 9.194/16.173/52.182/8.491 ms
```

(Ping times were better when I moved the Pico W closer to my base station.)

I don't have hard data on power consumption yet—due to an unexpected hospital visit, my testing was cut short—but while running Apache Bench (`ab`) on a simple web page running on the Pico W, my USB power meter showed between 70-80 mA being used (at 5.15v, so 412 mW):

{{< figure src="./usb-power-meter-80ma-pico-w.jpg" alt="USB power meter measuring 80mA power consumption from Pico W during WiFi benchmark" width="700" height="398" class="insert-image" >}}

I should have more time for power testing later, as I get deeper into my Garage Door Sensor project.

## Hardware changes

{{< figure src="./pico-and-pico-w-comparison.jpeg" alt="Raspberry Pi Pico and Pico W side-by-side" width="700" height="460" class="insert-image" >}}

Looking at a side-by-side with the normal Pico, the most obvious difference is the inclusion of the wireless chip (and associated RF shield), as well as the move of the three debug pins to the middle of the board, to make way for the antenna on the edge of the board.

Raspberry Pi played Tetris with a few power components, and the only other major difference is the LED now hangs off a pin on the WiFi chip—not on GPIO Pin 25 like on the regular Pico. To use the LED in MicroPython, you can use:

```
import time
from machine import Pin

led = Pin("LED", Pin.OUT, value=1)
led.toggle()
```

Use of the Pico W's features require different firmware than the original Pico, and if you're silly like me and accidentally flash the original Pico's MicroPython firmware to the Pico W, thus bricking it, you can copy the [flash_nuke.uf2](https://www.raspberrypi.org/documentation/rp2040/getting-started/static/6f6f31460c258138bd33cc96ddd76b91/flash_nuke.uf2) file to the Pico W when you have it mounted, and it should wipe all contents so you can re-flash it with the proper firmware.

I ran into a funky issue where the Pico W would basically disable some of my host computer's USB devices when I plugged it in, until I fixed it with the right firmware.

Thonny, I believe, will natively support the Pico W soon. Other IDEs should follow.

## ESPHome Support

_Personally_ I'm most excited about ESPHome supporting the Pico. I mentioned recently [work was underway to get ESPHome to work with the Pico](https://www.jeffgeerling.com/blog/2022/esphome-on-raspberry-pi-pico), and I've heard Nabu Casa has a Pico W and are working on compatibility for an upcoming release.

That means programming a Pico W as a device in the Home Assistant universe will be as easy as a few lines of YAML!

My goal for the Garage Door Sensor project is to get that going using ESPHome instead of MicroPython, just to make maintenance easier.

## Conclusion

I typically have more time to get more raw numbers for an initial review like this, but alas, I got stuck in the hospital last week, and that knocked out a few of the days when I planned on the 'boring but necessary' data-gathering for this post.

{{< figure src="./raspberry-pi-pico-w-esp8266-d1-mini.jpeg" alt="Raspberry Pi Pico W next to ESP8266-based D1 mini" width="700" height="444" class="insert-image" >}}

I imagine I'll be picking up a few more, once they hit Micro Center's shelves. It's often tricky finding some of the cheaper ESP-based boards locally, but they've had Picos in stock almost since launch. Let's hope Raspberry Pi can keep up with the demand.

At a price of $6, I'm sure many will be eager to get their hands on one—or a few.
