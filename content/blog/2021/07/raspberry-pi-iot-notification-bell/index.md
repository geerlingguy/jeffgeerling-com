---
nid: 3115
title: "The Raspberry Pi IoT Notification Bell"
slug: "raspberry-pi-iot-notification-bell"
date: 2021-07-01T14:00:44+00:00
drupal:
  nid: 3115
  path: /blog/2021/raspberry-pi-iot-notification-bell
  body_format: markdown
  redirects: []
tags:
  - bell
  - electronics
  - iot
  - python
  - raspberry pi
  - soldering
  - tutorial
  - video
  - youtube
---

_Harbinger of the Internet of Dings_

Last year, I built the first version of what I call the "Raspberry Pi Bell Slapper." It was named that because it used a servo and a metal arm to slap the top of the bell in response to a stimuli—in this case, an email from a donation notification system for a local non-profit radio station.

This year, that same radio station had another one of their fund-raisers (a radiothon), and to celebrate, I thought I'd do the thing justice, with a better circuit (using a solenoid instead of a servo) and a 3D printed enclosure. And this is the result:

{{< figure src="./final-pi-notification-bell.jpeg" alt="Clarence 2.0 - The Raspberry Pi Notification Bell" width="600" height="400" class="insert-image" >}}

There is a Raspberry Pi Zero W with a custom solenoid control HAT on top inside the case to the left, and the solenoid right up against the bell, which is mounted on the right.

I also posted a video on YouTube exploring the project in detail: [The Raspberry Pi IoT Notification Bell](https://www.youtube.com/watch?v=o5wOzNzShrA).

## Building the Solenoid control HAT

It's not technically a HAT but it's like a HAT so I'll call it a HAT; I translated the following [circuito.io circuit diagram](https://www.circuito.io/app?components=9443,11015,200000):

{{< figure src="./circuito-circuit-pi-solenoid.png" alt="Circuito Pi Solenoid Diagram" width="477" height="538" class="insert-image" >}}

...into the following protoboard circuit:

{{< figure src="./solder-job-pi-notification-bell.jpeg" alt="Raspberry Pi solenoid control HAT circuit prototype board botched solder job" width="600" height="400" class="insert-image" >}}

It's not my best work, but my excuse is that I had about 30 minutes to complete the thing (while trying to record it for a YouTube video), and didn't even spend time laying it out before soldering it in place. Plus I didn't have any strip board available—bridging with globs of solder is inherently uglier 🤪

But hey, it works. What more can you ask? Someday I might [create a proper PCB](https://github.com/geerlingguy/pi-bell-slapper/issues/6) for it, who knows.

## Building the 3D printed case

I was prepared to spend a few hours designing a new case from the ground up, when I found user [@tenderlove published his Analog Terminal Bell case design](https://github.com/tenderlove/analog-terminal-bell/tree/master/case).

So I decided to learn OpenSCAD and hack that case design a bit to fit my larger Pi Zero and HAT.

And voila! I had a case:

{{< figure src="./3d-printed-case-pi-bell-slapper.gif" alt="3D Printed Pi Bell Notification case" width="320" height="180" class="insert-image" >}}

## Putting it all together

The solenoid circuit is wired up to the Pi's GPIO pin 4, so controlling it with Python is pretty simple:

```
from time import sleep

# GPIO Pin where solenoid control circuit is connected.
solenoid_pin = 4

# Define the Pin numbering type and define Servo Pin as output pin.
GPIO.setmode(GPIO.BCM)
GPIO.setup(solenoid_pin, GPIO.OUT)

# Slap the bell.
GPIO.output(4, GPIO.HIGH)
sleep(0.01)
GPIO.output(4, GPIO.LOW)

GPIO.cleanup()
```

The final script is a little more robust—check out `bell_slap.py` in the [Pi Bell Slapper repository](https://github.com/geerlingguy/pi-bell-slapper).

It basically:

  1. Sets up GPIO.
  2. Briefly sets pin 4 'high'.
  3. Cleans up GPIO.

Then there's an [`email_check.py`](https://github.com/geerlingguy/pi-bell-slapper/blob/master/email_check.py) script that ties into a configured email account to check for a specific notification email, then call out to `bell_slap.py` any time a donation email is found.

{{< figure src="./clarence-2.0-ding.gif" alt="Clarence 2.0 Raspberry Pi Bell Slapper in action with solenoid dinging bell" width="400" height="225" class="insert-image" >}}

You can check out all the source (and a lot more documentation) in the [Raspberry Pi Bell Slapper](https://github.com/geerlingguy/pi-bell-slapper) repository—and if you haven't watched the video, check it out on YouTube: [The Raspberry Pi IoT Notification Bell](https://www.youtube.com/watch?v=o5wOzNzShrA).
