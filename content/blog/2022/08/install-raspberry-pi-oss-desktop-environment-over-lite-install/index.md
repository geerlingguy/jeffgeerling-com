---
nid: 3227
title: "Install Raspberry Pi OS's desktop environment over a Lite install"
slug: "install-raspberry-pi-oss-desktop-environment-over-lite-install"
date: 2022-08-03T20:33:38+00:00
drupal:
  nid: 3227
  path: /blog/2022/install-raspberry-pi-oss-desktop-environment-over-lite-install
  body_format: markdown
  redirects: []
tags:
  - gui
  - lite
  - pi os
  - raspberry pi
  - raspbian
---
> **Update**: I will keep this blog post up to date with future releases of Pi OS. If you see something missing, please let me know in the comments!

Almost every time I set up a Raspberry Pi these days, I use the 'Lite' version of Raspberry Pi OS. That version doesn't come with a GUI, it just boots to the console. It's much smaller in size and contains most things you'd need for a 'headless' Pi setup.

And if you know your way around the command line, it's not daunting to plug in a monitor, keyboard, and mouse, and explore via the shell if you need to.

But every so often, I've had a Lite install that I wanted to switch to GUI, but I'm too lazy to pull the Pi out of wherever it's installed, pull the microSD card, and re-flash it with the full OS, and then re-run my automation on it to set up whatever I had running before.

And that's why it's nice to be able to just install the GUI on top of an existing Lite install!

The instructions differ for various Pi OS releases, so I've split them up below:

## Pi OS 11 'Bullseye'

Install Xorg and the Raspberry Pi 'PIXEL' environment:

```
sudo apt install xserver-xorg raspberrypi-ui-mods
```

## Pi OS 12 'Bookworm'

Xorg is not in use by default, so just install the ui-mods package to get the full GUI:

```
sudo apt install raspberrypi-ui-mods
```

## Pi OS 13 'Trixie'

Raspberry Pi changed quite a bit in the desktop environment, and they don't offer the `ui-mods` package anymore. So, to install the desktop environment:

```
# Basic X desktop:
sudo apt install --no-install-recommends rpd-x-core

# Wayland desktop:
sudo apt install --no-install-recommends rpd-wayland-core
```

If you'd like Raspberry Pi's theme and preferences apps, install them too:

```
sudo apt install rpd-theme rpd-preferences
```

## After installing the desktop environment

Run `sudo raspi-config` and change the system boot option to boot to desktop, instead of the CLI (navigate to System Options > Boot, and select the "Desktop GUI" option).

Reboot, and you should be in the graphical environment!

There are other useful bits of software you can install if you want, like `chromium-browser` or `firefox` (which gives you a web browser).

You can even use an alternate desktop environment if you want—check out [This raspberrytips.com article](https://raspberrytips.com/upgrade-raspbian-lite-to-desktop/) for more on that.
