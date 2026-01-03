---
nid: 3190
title: "Playing sounds with Python on a Raspberry Pi"
slug: "playing-sounds-python-on-raspberry-pi"
date: 2022-03-10T18:01:11+00:00
drupal:
  nid: 3190
  path: /blog/2022/playing-sounds-python-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - alsa
  - audio
  - bell
  - programming
  - python
  - raspberry pi
  - tutorial
  - usb
---

Today I needed to play back an MP3 or WAV file through a USB audio device on a Raspberry Pi, in a Python script. "_Should be easy!_" I thought!

{{< figure src="./raspberry-pi-clarence-bell-speaker-sound-usb-audio-python.jpeg" alt="Clarence the Raspberry Pi Bell Slapper with USB audio output and speaker" width="700" height="469" class="insert-image" >}}

Well, a couple hours later I decided to write this blog post to document the easiest way to do it, since I had to take quite a journey to get to the point where sound actually plays through the USB audio output.

The problem is most guides, like [this simple one from Raspberry Pi's project site](https://projects.raspberrypi.org/en/projects/generic-python-playing-sound-files), assume two things:

  1. Your Raspberry Pi has a default sound device (e.g. `0`) that works already
  2. You're running code interactively or in some way that it magically works without understanding how the underlying APIs work

The problem is, in my case, running a USB sound device off a headless Raspberry Pi Zero, neither of those assumptions were true.

## Getting USB Audio working

The first step is to detect the USB audio device, and to tell your system to use it as the default audio device. There are other ways to detect and/or choose a specific device in the Python code itself, but it's easiest if you can just set the default system-wide and let Python use that default.

First, you need to make sure your sound device (in my case a little $9 [Vantec NBA-120U adapter](https://amzn.to/3i3fK3z)) is recognized. Run the following command, and you should see it listed as the device with 'USB' in the name:

```
$ cat /proc/asound/modules
 1 snd_usb_audio
```

Some Pi models will also show a `0` for a built-in device (e.g. the sound output on a model B version). By default, the ALSA (Advanced Linux Sound Architecture) audio system will try to use device `0`, no matter what. To tell it to use device `1` (the `snd_usb_audio` device), you can configure either the global `/etc/asound.conf` file, or a user-local `~/.asoundrc` file.

Inside one of those two files (I chose to configure the Pi user's `~/.asoundrc` file), put the following contents:

```
pcm.!default {
        type hw
        card 1
}

ctl.!default {
        type hw
        card 1
}
```

This tells ALSA to default to `card 1`, the USB device. Now, to test that it's working, plug headphones or speakers into the output, and run:

```
$ speaker-test -c2 -twav -l7
```

You should start hearing sounds like "front left" and "front right" through your speakers or headphones.

## Playing back sound with `pygame.mixer`

I had a simple "ding.wav" file that was the sound of a bell dinging, for my [Raspberry Pi Bell Slapper](https://github.com/geerlingguy/pi-bell-slapper) project. I wanted to set it up so the Pi would not only ding a physical bell with a solenoid connected to the Pi's GPIO, but it also a ding sound through speakers so someone could hear the ding in another room.

Here's the minimal Python code required to play the file using `pygame`:

```
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('/home/pi/ding.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)
```

This requires `pygame`, which can be installed with `pip3 install pygame`. Pygame will also fail without the required mixer libraries, so you also need to run `apt-get install libsdl2-mixer-2.0-0`.

Once you've done that, you should be able to run the script (`python3 play-sound.py`), and it should play the file.

The `while` loop at the end is important—without it, the script will exit before the sound even gets a chance to play! That was the last bit that was missing from all the 'play sound with Python' tutorials I was seeing, and it's [thanks to user1509818](https://stackoverflow.com/a/11382133/100134) that I found it.
