---
nid: 3312
title: "nmcli for WiFi on Raspberry Pi OS 12 'Bookworm'"
slug: "nmcli-wifi-on-raspberry-pi-os-12-bookworm"
date: 2023-09-30T03:53:31+00:00
drupal:
  nid: 3312
  path: /blog/2023/nmcli-wifi-on-raspberry-pi-os-12-bookworm
  body_format: markdown
  redirects:
    - /blog/2023/getting-started-nmcli-on-raspberry-pi-os-12-bookworm
    - /blog/2023/getting-started-nmcli-wifi-management-on-raspberry-pi-os-12-bookworm
    - /blog/2023/nmcli-wifi-management-on-raspberry-pi-os-12-bookworm
aliases:
  - /blog/2023/getting-started-nmcli-on-raspberry-pi-os-12-bookworm
  - /blog/2023/getting-started-nmcli-wifi-management-on-raspberry-pi-os-12-bookworm
  - /blog/2023/nmcli-wifi-management-on-raspberry-pi-os-12-bookworm
tags:
  - command line
  - linux
  - networkmanager
  - nmcli
  - pi os
  - raspberry pi
  - wifi
---

If you haven't already, check out my [full video on the Raspberry Pi 5](https://www.youtube.com/watch?v=nBtOEmUqASQ), which inspired this post.

{{< figure src="./raspberry-pi-5-angle.jpg" alt="Raspberry Pi 5 at an angle" width="700" height="403" class="insert-image" >}}

Raspberry Pi OS 12 'Bookworm' is coming alongside the release of the Raspberry Pi 5, and with it comes a fairly drastic change from using `wpa_supplicant` for WiFi interface management to everything network-related running through `nmcli`, or [NetworkManager](https://networkmanager.dev/docs/api/latest/nmcli.html).

`nmcli` is widely adopted in Linux these days, and it makes managing WiFi, LAN, and other network connections much simpler.

I thought I'd jot down my notes using `nmcli` for some Pi testing, mostly for my own reference. There are tons of guides with hundreds of examples to choose from, but these are some of the commands I find myself running frequently:

```
# Quick status of all interfaces
nmcli dev status

# Detailed overview of all interfaces
nmcli

# Get a list of all WiFi SSIDs
nmcli d wifi list

# Disconnect from a WiFi network
nmcli con  # Get the NAME of the WiFi connection
nmcli con down "connection_name_here"

# Connect to a WiFi network on a specific WiFi interface
sudo nmcli d wifi connect "ssid_here" password "password_here" ifname wlan1
```

> `nmcli` commands often require root privileges, so add `sudo` before the command if you get a warning like "[XYZ] failed: Not authorized to [do XYZ]."

For debugging WiFi issues, `iw` is always handy as well:

```
# Show detailed information about a specific WiFi interface
iw dev wlan0 info

# Show WiFi link details (signal strength, bitrates)
iw dev wlan0 link
```

And of course, if you're using the GUI on the Raspberry Pi, they have a handy little WiFi connection menu you can use.

Alternatively, there's a more user-friendly console front end for NetworkManager, `nmtui` (which should also be present on Pi OS):

{{< figure src="./nmtui-raspberry-pi.jpg" alt="nmtui Network Manager Terminal User Interface on a Raspberry Pi" width="700" height="369" class="insert-image" >}}

For the quickest way to monitor link quality (instead of using `watch` with one of the above commands), install `wavemon` and run `wavemon wlan1` (or whatever interface you want to monitor). Press 'l' to view a graph over time of link signal quality, and play with your antenna location.
