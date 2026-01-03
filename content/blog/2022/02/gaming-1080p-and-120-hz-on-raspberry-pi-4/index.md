---
nid: 3184
title: "Gaming at 1080p and 120 Hz on a Raspberry Pi 4"
slug: "gaming-1080p-and-120-hz-on-raspberry-pi-4"
date: 2022-02-17T18:55:04+00:00
drupal:
  nid: 3184
  path: /blog/2022/gaming-1080p-and-120-hz-on-raspberry-pi-4
  body_format: markdown
  redirects:
    - /blog/2022/getting-1080p-120-hz-on-raspberry-pi-4
aliases:
  - /blog/2022/getting-1080p-120-hz-on-raspberry-pi-4
tags:
  - gaming
  - hdmi
  - linux
  - monitor
  - raspberry pi
  - refresh rate
  - video
  - xrandr
---

I often like exploring what's possible on a Raspberry Pi (or other low-end hardware). One area I haven't explored much is GPU performance. I typically run my Pi's headless, and have only dabbled in embedded machine vision with Pi cameras, so most of my experience is on the programming / software side.

But seeing Apple's 120 Hz 'ProMotion', and ever-higher refresh rates in the enthusiast gaming realm ([we may hit 480 Hz soon](https://www.intehill.com/blogs/portable-monitor/boe-480hz-monitor)!), I wanted to see how a tiny Raspberry Pi could perform in this realm.

The Pi's VideoCore GPU can output 1080p at refresh rates up to 120 Hz—at least there's a [setting](https://www.raspberrypi.com/documentation/computers/config_txt.html#hdmi_mode) for it. But I'd never tried it. The hardest I pushed a Pi was 4K at 60 Hz for my [Pi 4 a Day challenge](https://www.youtube.com/watch?v=OU6jHvVqJxY), and that didn't go as well as I'd hoped.

{{< figure src="./msi-optix-g241-gaming-monitor-small.png" alt="MSI Optix G241 gaming monitor - 144 hz" width="400" height="321" class="insert-image" >}}

For an upcoming project, I was able to acquire an [MSI Optix G241 'Esports gaming monitor'](https://amzn.to/3oTiHYx) that can run up to 144 Hz. Since the monitor runs at 120 Hz too, I decided to see how it worked with the Pi.

> Note: I tested with a Raspberry Pi Compute Module 4, with 4 GB of RAM, 32 GB of eMMC, and built-in Bluetooth and WiFi. Other models use the same BCM2711 SoC, so performance should be similar across CM4 and Pi 4 models.

## Going beyond 60 Hz

Searching around for how to do it, my first port of call was a Raspberry Pi forum topic; [Running the pi 4 at 120hz](https://forums.raspberrypi.com/viewtopic.php?t=261010). The topic has some hints about overriding the `fkms_max_refresh_rate` in `/boot/firmware/cmdline.txt` and adjusting the `hdmi_group` and `hdmi_mode` in the `/boot/firmware/config.txt`.

Indeed, looking at the [HDMI Mode documentation](https://www.raspberrypi.com/documentation/computers/config_txt.html#hdmi-mode), there's a setting for 1080p at 120 Hz available on the Pi 4 (but only in the CEA mode, or `hdmi_group=1`):

| hdmi_mode | Resolution | Frequency | Screen Aspect | Notes |
| --- | --- | --- | --- | --- |
| 78 | 1080p | 120Hz | 64:27 | Pi 4 |

For `hdmi_group=2` (DMT), it seems like there's only a 1080p option for 60Hz (`hdmi_mode=82`).

So my first attempt at getting greater than 60 Hz was to edit `/boot/firmware/config.txt`, and add the following near the top, near other HDMI options:

```
# 120 Hz
hdmi_group=1
hdmi_mode=78
```

Then reboot.

> The `vc4.fkms_max_refresh_rate` override [isn't required on the latest version of Pi OS](https://github.com/raspberrypi/linux/issues/3677#issuecomment-873311316) because it uses KMS instead of the 'fake' KMS driver Raspberry Pi used to use.

## Checking on things with `xrandr`

Since `ddcprobe` doesn't seem to be a thing on the Pi (I couldn't find a way to install the `xresprobe` package), I used `xrandr` to the monitor's current settings:

```
$ xrandr -q
Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 7680 x 7680
HDMI-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 527mm x 296mm
   1920x1080     60.00*+ 144.01   120.00   119.88    50.00    59.94  
   1680x1050     59.88  
   1280x1024     75.02    60.02  
   1440x900      59.90  
   1280x960      60.00  
   1152x864      75.00  
   1280x720      60.00    50.00    59.94  
   1440x576      50.00  
   1024x768      75.03    70.07    60.00  
   1440x480      60.00    59.94  
   800x600       72.19    75.00    60.32    56.25  
   720x576       50.00  
   720x480       60.00    59.94  
   640x480       75.00    72.81    66.67    60.00    59.94  
   720x400       70.08  
HDMI-2 disconnected (normal left inverted right x axis y axis)
```

The `60.00*+ 144.01   120.00   119.88    50.00    59.94` lists the available refresh rates at the 1080p resolution, and `*` indicates the current selection. But why is it set to 60 Hz? If I check the boot logs:

```
$ dmesg | grep HDMI
[    0.000000] Kernel command line: coherent_pool=1M 8250.nr_uarts=0 snd_bcm2835.enable_compat_alsa=0 snd_bcm2835.enable_hdmi=1 video=HDMI-A-1:1920x1080M@120 smsc95xx.macaddr=DC:A6:32:FF:64:63 vc_mem.mem_base=0x3ec00000 vc_mem.mem_size=0x40000000  vc4.fkms_max_refresh_rate=120 console=ttyS0,115200 console=tty1 root=PARTUUID=3e11d467-02 rootfstype=ext4 fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
[    1.209617] simple-framebuffer 3e3cf000.framebuffer: format=a8r8g8b8, mode=1920x1080x32, linelength=7680
```

So it looks like the Kernel command line is picking up the 120 Hz, but it doesn't look like that's sticking when the window manager/GUI loads up.

> Note: I've created a forum topic to track this issue and hopefully it's a simple fix or oversight on my part: [Pi 4 set at 120 Hz, drops to 60 Hz when GUI starts](https://forums.raspberrypi.com/viewtopic.php?t=329898).

No matter, though, I should be able to force it:

```
# Change the refresh rate to 120.00 Hz.
$ sudo xrandr --output HDMI-1 --mode 1920x1080 --rate 120.00
```

And the first thing I noticed was mouse cursor movements are immediately a _lot_ smoother. So that's good. And now it's showing as the selected resolution:

```
$ xrandr -q
Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 7680 x 7680
HDMI-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 527mm x 296mm
   1920x1080     60.00 + 144.01   120.00*  119.88    50.00    59.94  
...
```

Dragging windows around on the screen is as jittery as it is at 60 or 30 Hz, so I needed more scientific tests to see whether the Pi could render anything larger than a mouse cursor at 120 Hz.

## UFO Test

The first thing I tried was the [UFO in-browser refresh rate test](https://www.testufo.com/refreshrate), but I could only get 80-90 fps:

{{< figure src="./raspberry-pi-120hz-ufotest-normal_1.jpg" alt="120 Hz UFO test on Raspberry Pi with default clock" width="700" height="394" class="insert-image" >}}

## Overclocking for 120 Hz

To get the UFO test to 120 Hz (just barely...), I added the following configuration in `/boot/firmware/config.txt`, to drive the Pi at 2.14 GHz and the GPU at 750 MHz;

```
# Overclock
over_voltage=6
arm_freq=2147
gpu_freq=750
```

Could it be driven higher? Yeah, if you have good cooling and/or get lucky in the silicon lottery. Heck, someone used ice spray direct on the chip (sans heat spreader) and [momentarily broke 3 GHz on a CM4](https://twitter.com/Claude1079/status/1448312145268051968) last year.

Anyways, with the overclock in place, and after a reboot and another refresh rate setting with `xrandr`, the UFO test was now giving me almost precisely 120 Hz.

{{< figure src="./raspberry-pi-120hz-ufotest-overclock.jpg" alt="120 Hz UFO test on Raspberry Pi with overclock" width="700" height="394" class="insert-image" >}}

Moving the mouse on the screen was enough to bump it down to 'unstable performance' and 118-119 fps. And  while doing anything useful like opening a new browser tab or switching applications, it would drop to 70-100 fps.

But now that my basic target was met, I moved on to other tests.

## Gaming Test

To confirm I could get more than 60 fps in a 3D game, I also installed Quake III Arena (the open source version, at least) with the following commands:

```
sudo apt install quake3
game-data-packager quake3 -i --gain-root-command sudo
```

I launched Quake III Arena and had immediate nostalgia for my high school days, when I would frag people online from my old Mac, only slightly annoyed that Unreal Tournament was more prevalent among the local LAN parties back in the day (I knew the maps in Quake much better than UT).

Anyways, back to the point: I set all the settings pretty low, just to see what the maximum FPS I could get would be, and with the Pi's _default_ clock, I could get around 70-80 fps in less complex outdoor environments, or 50-60 fps in the middle of some action:

{{< figure src="./major-ate-unnamedplayers-rocket-quake-3-arena-fps.jpg" alt="Major ate UnnamedPlayer's rocket in Quake III Arena on a Raspberry Pi" width="700" height="525" class="insert-image" >}}

Blast a rocket in a tight hallway, though, and it drops to 30-50 fps.

How about the 2.14 GHz / 750 MHz overclock, though?

{{< figure src="./quake-iii-arena-raspberrypi-overclocked-88fps.jpg" alt="Quake III Arena on Raspberry Pi - 88fps overclock" width="700" height="525" class="insert-image" >}}

I was able to get 70-90 fps and the game was even more playable, even when I nudged the resolution beyond 480p.

> Note: It might be possible to eke out even more performance with a more optimized version of a game like Quake III Arena, like Q3Lite, but alas, that game's maintainer hasn't had the time to work on [getting it running on the Pi 4 or compiling under Bullseye](https://github.com/cdev-tux/q3lite/issues/19).
> 
> Note 2: To show FPS during gameplay, enter the in-game console with `~`, then type in `\cg_drawFPS 1`
>
> Note 3: FPS is capped at 90 by default; to raise that limit, enter the console and type in `\com_maxfps 250` (where `250` is the desired limit)

## Conclusion

The Raspberry Pi 4 (and CM4/Pi 400) hardware is _capable_ of driving monitors beyond 60 Hz... but not amazingly well. With an overclock, you can expect to see rendering in the 60-90 Hz range, depending on what you're doing.

But if you just want the most butter-smooth mouse cursor you can get on a Raspberry Pi, 120 Hz is perfect for that. You just need to make sure you're using a reliable HDMI cable and a monitor capable of high refresh rates.

## Follow-up

After posting this, someone mentioned being able to set 144 Hz on their Pi 400. So I tried it on the CM4 and was able to get 120-144 Hz on the refresh rate test, but the Pi was much less stable at that refresh rate. The HDMI output would just go blank sometimes, plus the actual rendered frame rate would still dip down to 70-80 fps (even with overclock) whenever there was any heavy activity.

{{< figure src="./144-hz-raspberry-pi.jpg" alt="144 Hz Raspberry Pi monitor" width="700" height="394" class="insert-image" >}}

I even tried overclocking to 2.4 GHz CPU / 800 MHz GPU, and the Pi would run for a bit but it was extremely unstable on my chip.
