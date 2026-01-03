---
nid: 3146
title: "Working with multiple WiFi interfaces on a Raspberry Pi"
slug: "working-multiple-wifi-interfaces-on-raspberry-pi"
date: 2021-11-18T22:47:45+00:00
drupal:
  nid: 3146
  path: /blog/2021/working-multiple-wifi-interfaces-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - linux
  - networking
  - raspberry pi
  - wifi
  - wifi 6
  - wpa_supplicant
---

> **Update for Bookworm / Pi OS 12+**: After Debian 12 / Pi OS 12, the directions below using `wpa_supplicant` no longer apply. See [this comment](#comment-33691) for updated instructions using `nmcli` and `nmtui` with NetworkManager instead.
>
> Also see my newer blog post, [nmcli for WiFi on Raspberry Pi OS 12 'Bookworm'](/blog/2023/nmcli-wifi-on-raspberry-pi-os-12-bookworm).

Sometimes I like to connect to multiple WiFi networks on my Pi for... reasons.

Other times I like being able to use a better wireless interface than the built-in WiFi module on the Pi 4 or CM4, but don't want to add `dtoverlay=disable-wifi` in my `/boot/config.txt` and reboot.

Since Pi OS uses `wpa_supplicant`, it's actually easy to do this.

First, see what interfaces you have available, e.g. with `ip a`:

```
$ ip a
...
3: wlan0: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
    link/ether e4:5f:01:4e:f0:22 brd ff:ff:ff:ff:ff:ff
4: wlan1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 84:5c:f3:f6:e9:29 brd ff:ff:ff:ff:ff:ff
```

If you want to specify a network configuration that _only_ applies to `wlan1`, create a file named `/etc/wpa_supplicant/wpa_supplicant-wlan1.conf`, and put your network credentials inside:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
	ssid="my-network-name"
	psk="my-network-password"
}
```

Obviously, substitute your own values where relevant.

It _should_ try connecting on `wlan1` automatically (you should be able to follow with `dmesg --follow`), but sometimes, for some strange reason, it won't, and you'll have to reboot the Pi to pick up the changes.

The logic for the naming of `wpa_supplicant.conf` files is located inside `/usr/share/dhcpcd/hooks/10-wpa_supplicant`. And if you need to manually bring down an interface, run `sudo ifconfig wlan0 down`. You can also try reloading the wpa_supplicant config manually with `sudo wpa_cli -i wlan0 reconfigure`, but sometimes that doesn't seem to work for me.
