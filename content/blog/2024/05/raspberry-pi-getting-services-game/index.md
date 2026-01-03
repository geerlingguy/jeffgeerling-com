---
nid: 3372
title: "Raspberry Pi is getting into the services game"
slug: "raspberry-pi-getting-services-game"
date: 2024-05-07T13:00:11+00:00
drupal:
  nid: 3372
  path: /blog/2024/raspberry-pi-getting-services-game
  body_format: markdown
  redirects: []
tags:
  - linux
  - pi os
  - raspberry pi
  - realvnc
  - remote access
  - video
  - vnc
  - youtube
---

...and it's all free—_so far_.

{{< figure src="./raspberry-pi-connect-logo.jpg" alt="Raspberry Pi Connect Beta Logo" width="700" height="auto" class="insert-image" >}}

Raspberry Pi today launched [Raspberry Pi Connect](https://connect.raspberrypi.com), a free remote VPN service for all Pi OS users.

If you create a [Raspberry Pi ID](https://id.raspberrypi.com/), you can sign up for Connect, install `rpi-connect` on a Pi 4 or 5 running 64-bit Pi OS 12 'Bookworm', and register that Pi with the service.

Then, on any other device's web browser, you can log in and remote control your Pi through Connect's web-based VNC viewer.

{{< figure src="./raspberry-pi-connect-demo.jpg" alt="Raspberry Pi Connect Demo" width="700" height="auto" class="insert-image" >}}

The VNC server is based on [wayvnc](https://github.com/any1/wayvnc), and the Connect service allows for as many registered Pis as you want (though I'm guessing the interface is optimized for the majority use case of one or a few).

Raspberry Pi Connect was likely shipped in response to RealVNC's slow migration from X11 to Wayland compatibility. RealVNC is installed by default on Pi OS, and has been for a long time, and many Pi users came to rely on it for remote Pi access.

When Pi OS 12 'Bookworm' was launched, [they switched from X11 to Wayland](https://www.raspberrypi.com/news/bookworm-the-new-version-of-raspberry-pi-os/), and a number of GUI-reliant apps needed tweaks. RealVNC hasn't been updated to work with Wayland, so it is not runnable by default on the latest Pis or Pi OS—though [you can force Pi OS back to X11 instead of Wayland to get RealVNC working](https://help.realvnc.com/hc/en-us/articles/14110635000221-Raspberry-Pi-5-Bookworm-and-RealVNC-Connect).

I've been using Connect for a few weeks in early beta access, and it's been about as decent as any other VNC solution. It's not quite as good as Microsoft's Remote Desktop under bandwidth-constrained use, but it's not bad either.

In this video, I go over use from home to the office (wired cable and fiber Internet) to use on a slow 5G connection (< 1 Mbps with 500ms ping times), and in all cases it's usable, but it's certainly less enjoyable on the slow connection!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/mgbTNZD1Vcw" frameborder='0' allowfullscreen></iframe></div>
</div>

There are a few quirks about Connect, like on mobile (I tested on my iPad and iPhone), there's no way to bring up the virtual keyboard, so text entry is impossible unless you use a USB or Bluetooth keyboard.

{{< figure src="./raspberry-pi-connect-ipad-keyboard.jpg" alt="Raspberry Pi Connect with an external keyboard on iPad" width="700" height="auto" class="insert-image" >}}

RealVNC has a full mobile app, so you're able to fully control a remote PC, Mac, or Linux machine much more easily.

Also, Raspberry Pi Connect can do odd things like pick the wrong display if you have multiple monitors connected. You can switch displays in the Pi OS settings, but RealVNC, again, handles that situation better, allowing you to pick a monitor directly in its own UI, or show all monitors.

There are a number of other advantages to RealVNC as well, like multi-user accounts, so I hope they will update to work with Wayland soon. But it's nice to have a free option directly from Raspberry Pi. Especially when it's so simple to use.

I'm especially happy Raspberry Pi added a basic CLI to `rpi-connect`—you can even sign into the service on a Pi over SSH with the command `rpi-connect signin`. Copy out the URL, log in via a browser, and the Pi will connect headlessly:

{{< figure src="./raspberry-pi-connect-cli-signin.jpg" alt="rpi-connect signin" width="700" height="auto" class="insert-image" >}}

You _do_ need to be running the full desktop Pi OS—Pi OS Lite won't work. And you also need auto-login enabled... at least for the time being. Eventually, I imagine you'll be able to configure Raspberry Pi Connect while flashing the OS using Raspberry Pi Imager, but the service is in Beta, so I'm sure things will change quickly!

I'm sure some people better suited to discussing Connect's security will do that in good time, but I didn't see anything bad in that regard in my initial testing. Keeping the service so simple helps keep the attack surface small. Especially when the potential damage (allowing someone direct remote control access to your Pi, and by extension, your network) is so great!

I have a few other thoughts in the video embedded above, especially regarding whether the service could be monetized at some point, but I'm interested in hearing your thoughts too! The comment form is below, and will always be free!
