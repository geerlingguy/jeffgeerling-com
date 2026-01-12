---
date: '2026-01-12T09:00:00-06:00'
tags: ['gps', 'clock', 'time', 'timing', 'raspberry pi', 'pico', 'microcontroller', 'waveshare', 'mini rack', 'homelab', 'pps', '3d printing', 'cad', 'video', 'level2jeff']
title: 'Raspberry Pi Pico Mini Rack GPS Clock'
slug: 'pico-gps-clock-mini-rack'
---
I wanted to have the most accurate timepiece possible mounted in my mini rack. Therefore I built this:

{{< figure
  src="./pico-gps-clock-mini-rack.jpg"
  alt="Raspberry Pi Pico GPS Clock for Mini Rack"
  width="700"
  height="auto"
  class="insert-image"
>}}

This is a GPS-based clock running on a Raspberry Pi Pico in a custom 1U 10" rack faceplate. The clock displays time based on a GPS input, and will not display time until a GPS timing lock has been acquired.

  - When you turn on the Pico, the display reads `----`
  - Upon 3D fix, you get a time on the clock, and the colon starts blinking
  - If the 3D fix is lost, the colon goes solid
  - When the 3D fix is regained, the colon starts blinking again

For full details on designing and building this clock, see:

  - [time-pi: Pico 1U GPS Clock for Mini Rack](https://github.com/geerlingguy/time-pi/tree/master/pico-clock-mini-rack#readme)
  - [time-pi Issue #4: Build 7-segment clock display for Mini Rack](https://github.com/geerlingguy/time-pi/issues/4)

I've also published a full build video (including my trials and tribulations designing a 3D print in Fusion. I'm still a bit of a noob there):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/E5qA4fgdS28' frameborder='0' allowfullscreen></iframe></div>
</div>

## Hardware

For my clock, I'm using a Raspberry Pi Pico 2, but you should be able to use any model Pico (including the Wireless versions). Here are all the parts required (some links are affiliate links):

  - [Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack](https://www.adafruit.com/product/879)
  - [Raspberry Pi Pico 2 (with Headers)](https://www.raspberrypi.com/products/raspberry-pi-pico-2/)
    - If you don't have the 'with Header' version, solder on [2x 20 pin headers](https://amzn.to/4jClLn1).
  - [Waveshare L76K GNSS Module for Pico](https://amzn.to/4qgiFaQ)
  - [15cm jumper wires](https://amzn.to/4aT5jwj)
  - [1220 3V Lithium coin cell battery](https://amzn.to/3YzptnL) (if you want RTC clock holdover)
  - [M2x6mm screws](https://amzn.to/45NaeLM) (optional, to hold the display in securely)

## 3D Printed 1U mini rack faceplate

{{< figure
  src="./pico-gps-clock-1u-faceplate.jpg"
  alt="Raspberry Pi Pico GPS Clock - 1U 3D printed assembly"
  width="700"
  height="auto"
  class="insert-image"
>}}

The faceplate design is hosted on Printables: [Pico GPS Clock - 1U Mini Rack faceplate](https://www.printables.com/model/1549682).

The tolerances for the 7 segment display are fairly tight, so you don't necessarily need the M2 screws to hold it in place.

## Software

Plug the Pico into a computer running Thonny, and [install MicroPython following Raspberry Pi's guide](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html). Optionally plug the Waveshare GPS HAT into the Pico at this time, to verify it powers on too.

Copy the MicroPython script `main.py` into the root directory of the Pico. Also copy the following files from this repository to the Pico, alongside `main.py`:

  - `ht16k33.py` and `ht16k33segment.py`, both from [smittytone/HT16K33-Python](https://github.com/smittytone/HT16K33-Python)
  - `micropyGPS.py`, from [inmcm/micropyGPS](https://github.com/inmcm/micropyGPS)

Run the script, to make sure it compiles and runs without errors. Then unplug the Pico.

Saving the script as `main.py` means MicroPython will automatically run the script when you plug in power, even if you don't have it plugged into your computer.

## Assembly

{{< figure
  src="./pico-gps-clock-assembly-back.jpg"
  alt="Raspberry Pi Pico GPS Clock - 1U 3D printed assembly"
  width="700"
  height="auto"
  class="insert-image"
>}}

  1. Insert clock face into clock face cutout, making sure the four through-hole pins on the board are in the small cutout made for that purpose. Ensure the clock face is flush with the front of the panel (the PCB should be in contact with the raised part of the print).
  2. Plug GPS antenna lead into the U.fl connector on the Waveshare HAT board, passing over the top of the board and over the battery, so it exits the correct side once the Pico is installed.
  3. Plug the Pico into the Waveshare HAT. The HAT's button and switch should be on the same side as the Pico's USB plug.
  4. Secure the female SMA jack through the faceplate using the included nut and washer.
  5. Using 4 female-to-female dupont jumper wires, plug the following pins to each other (see illustration above):

| 7-segment pin | Pi Pico pin   |
| :------------ | :------------ |
| VCC           | 36 (VCC)      |
| GND           | 38 (GND)      |
| SDA           | 6 (SDA/Data)  |
| SCL           | 7 (SCL/Clock) |

Once that's finished, plug micro USB power into the Pico, being careful not to push down on the 'BOOT' button under the Pico while doing so, and plug in a GPS antenna to the SMA jack.

That's it! You should now have a fully functional clock.

It will read `----` until a 3D position fix is acquired (this is required for a precise timing lock).

It usually takes 15-30s the first time to acquire a timing signal, or 3-5s if you just unplug it and plug it back in within a few minutes.

If you're not getting a timing signal, make sure you put the GPS antenna outdoors or close to a window with a clear view of the sky, and use good quality cabling. See [Mastering GPS antenna placement](https://www.worldtimesolutions.com/resources/learning/timing-knowledge-centre/mastering-gps-antenna-placement/).

## PPS Output

Currently, there is no PPS output available from the Waveshare HAT.

I spoke to Waveshare support, and they suggested I could add on a small bodge wire to get PPS from the relevant PCB trace (which provides the pulse for the PPS LED):

> The PPS LED does flash, but this signal is usually not directly exposed to the pins of the Pico HAT. If you wish to use this signal externally for verification or detection, you may need to check the schematic diagram to see if there are any relevant lines that can be connected, or consider using additional hardware circuits to lead this signal to the pin.

I'll keep working on this, and maybe add a second SMA cutout for PPS out on the panel once I get it working. Follow [this issue](https://github.com/geerlingguy/time-pi/issues/23) for updates.

## Conclusion (and _Why_?)

You might think a GPS clock (especially with just `HH:MM`) is a bit silly for a home mini rack.

And you'd be right.

But I'm having fun exploring horology, and having a GPS clock gives me a good excuse to route a GPS antenna signal into my homelab. And with that signal (and the precise timing it gives me), I can do more fun things... which I'll get to in the future, probably after building another dozen clocks or so. (I have a bigger post on GPS time coming soon!).
