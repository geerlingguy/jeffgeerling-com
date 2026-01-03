---
nid: 3253
title: "Getting to 1.5 Gbps WiFi 6E on the Raspberry Pi CM4"
slug: "getting-15-gbps-wifi-6e-on-raspberry-pi-cm4"
date: 2023-01-05T15:00:02+00:00
drupal:
  nid: 3253
  path: /blog/2023/getting-15-gbps-wifi-6e-on-raspberry-pi-cm4
  body_format: markdown
  redirects:
    - /blog/2022/getting-15-gbps-wifi-6e-on-raspberry-pi-cm4
aliases:
  - /blog/2022/getting-15-gbps-wifi-6e-on-raspberry-pi-cm4
tags:
  - linux
  - netgear
  - networking
  - performance
  - raspberry pi
  - wifi
  - wifi 6
  - wifi 6e
  - wpa_supplicant
---

In the pursuit of doing crazy things on a Raspberry Pi, my latest endeavor was to see if I could consistently pipe more than a gigabit per second of traffic through WiFi using a Raspberry Pi.

{{< figure src="./raspberry-pi-wifi-6e-intel-ax210.jpeg" alt="Raspberry Pi Compute Module 4 IO Board with Intel AX210 on M.2 adapter card" width="700" height="467" class="insert-image" >}}

In the past, I had some faltering attempts where sometimes things would work—sort-of—using WiFi 6 (802.11ax, 40 MHz bandwidth, 2x2) using an Intel AX200 M.2 card on the Raspberry Pi Compute Module 4.

But Netgear saw my post about [upgrading to 2.5 Gbps networking](/blog/2022/25-gigabit-homelab-upgrade-poe-wifi-6-ap) and decided to send me an upgraded Insight WAX630E access point—the one that does WiFi 6E with full support for 6 GHz and 160 MHz channel width. I had previously tested on an ASUS RT-AX86U (WiFi 6 only) and Netgear WAX620 (also WiFi 6 only), and it was high time I tried everything on the latest version of Raspberry Pi OS.

Here's my test setup:

{{< figure src="./raspberry-pi-cm4-m2-macbook-air-wifi-benchmark.jpg" alt="Raspberry Pi CM4 with Intel AX210 versus M2 MacBook Air WiFi Benchmark" width="700" height="394" class="insert-image" >}}

If you want to skip the rest of this post, I also made a YouTube video about how I upgraded my home WiFi using the Netgear WAX630E pictured in the background, how I got the Pi working on the 6 GHz network with an Intel AX210, and how I benchmarked it against my M2 MacBook Air. You can watch that video here:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/TdUxWEyafUg" frameborder="0" allowfullscreen=""></iframe></div>
</div>

## Getting to 6 GHz - wpa_supplicant

I set up a normal connection inside `wpa_supplicant.conf`, but that connected through the Raspberry Pi's own internal WiFi (`wlan0`). So I [made a more specific supplicant file for `wlan1` only](/blog/2021/working-multiple-wifi-interfaces-on-raspberry-pi), and put in the following config:

```
network={
        ssid="mynetwork"
        psk="PASSWORD_HERE"
}
```

At first I tried a mixed 2.4/5/6 SSID on the Netgear, but I realized the AX210 would first connect to 2.4 GHz and then to 5 GHz, but not the 6 GHz. So I tried splitting the networks, so I had three SSIDs:

  - mynetwork-2.4g
  - mynetwork-5g
  - mynetwork-6g

And I tried forcing the issue by changing the `ssid` to `mynetwork-6g`. But it wouldn't connect. Eventually I discovered the version of wpa_supplicant that currently ships with Debian 11 / Raspberry Pi OS 11 is 2.9, and _that_ version doesn't fully support WiFi 6E.

So I upgraded it following [this advice on the Raspberry Pi forums](https://forums.raspberrypi.com/viewtopic.php?t=338937#p2029874):

  1. Create a backports file for apt: `sudo nano /etc/apt/sources.list.d/backports.list`
  2. Put this inside: `deb http://deb.debian.org/debian bullseye-backports main`
  3. Update apt caches: `sudo apt update`
  4. Install the version of `wpa_supplicant` from backports: `sudo apt install wpasupplicant/bullseye-backports`

I restarted after that was done, but WiFi still wouldn't connect! So my next step was to run `wpa_supplicant` in debug mode, to see what was going on behind the scenes:

```
pi@wifitest:~ $ sudo pkill wpa_supplicant
pi@wifitest:~ $ sudo wpa_supplicant -dd -i wlan1 -c /etc/wpa_supplicant/wpa_supplicant-wlan1.conf 
...
wlan1: Selecting BSS from priority group 0
wlan1: 0: c8:9e:43:13:4a:81 ssid='mynetwork-6g' wpa_ie_len=0 rsn_ie_len=20 caps=0x511 level=-27 freq=6135 
wlan1:    skip RSN IE - key mgmt mismatch
wlan1:    reject due to mismatch with WPA/WPA2
```

And _that_ apparently, was because the default settings in `wpa_supplicant` seem to align with WPA/WPA2. The Netgear was set up to use WPA3 Personal.

## Getting to 6 GHz - WPA3

Following [this ArchLinux guide](https://wiki.archlinux.org/title/wpa_supplicant#Connections_to_pure_WPA3-SAE_access_points), I found the solution was to add two more options in my network configuration in `wpa_supplicant-wlan1.conf`:

```
network={
        ssid="mynetwork-6g"
        psk="PASSWORD_HERE"
        key_mgmt=SAE
        ieee80211w=2
}
```

After doing that, the Pi connected over the 6 GHz network, and at the full 160 MHz channel bandwidth:

```
pi@wifitest:~ $ iw dev wlan1 info
Interface wlan1
	ifindex 4
	wdev 0x100000001
	addr 84:5c:f3:f6:e9:29
	ssid mynetwork-6g
	type managed
	wiphy 1
	channel 37 (6135 MHz), width: 160 MHz, center1: 6185 MHz
	txpower 22.00 dBm
	multicast TXQ:
		qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets
		0	0	0	0	0	0	0	0		0
```

Further, I placed the Pi setup about a foot from the AP in my basement, so it could get the best possible signal:

```
pi@wifitest:~ $ iwconfig wlan1
wlan1     IEEE 802.11  ESSID:"mynetwork-6g"
...
          Link Quality=70/70  Signal level=-19 dBm  
```

With that, it was time to run a speed test!

```
pi@wifitest:~ $ iperf3 -c 10.0.100.15 -p 5432
Connecting to host 10.0.100.15, port 5432
[  5] local 10.0.100.26 port 41196 connected to 10.0.100.15 port 5432
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   164 MBytes  1.38 Gbits/sec    0   3.76 MBytes       
[  5]   1.00-2.00   sec   186 MBytes  1.56 Gbits/sec    0   3.97 MBytes       
[  5]   2.00-3.00   sec   188 MBytes  1.57 Gbits/sec    0   3.97 MBytes       
[  5]   3.00-4.00   sec   186 MBytes  1.56 Gbits/sec    0   3.97 MBytes       
[  5]   4.00-5.00   sec   188 MBytes  1.57 Gbits/sec    0   3.97 MBytes       
[  5]   5.00-6.00   sec   185 MBytes  1.55 Gbits/sec    0   3.97 MBytes       
[  5]   6.00-7.00   sec   186 MBytes  1.56 Gbits/sec    0   3.97 MBytes       
[  5]   7.00-8.00   sec   186 MBytes  1.56 Gbits/sec    0   3.97 MBytes       
[  5]   8.00-9.00   sec   188 MBytes  1.57 Gbits/sec    0   3.97 MBytes       
[  5]   9.00-10.00  sec   186 MBytes  1.56 Gbits/sec    0   3.97 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.80 GBytes  1.55 Gbits/sec    0             sender
[  5]   0.00-10.01  sec  1.80 GBytes  1.54 Gbits/sec                  receiver

iperf Done.
```

Indeed; using `--bidir` to flood TCP traffic both ways, I was seeing over 650 Mbps up _and_ down concurrently, so I have a new wireless speed champion in the house.

It's annoying that my brand new M2 MacBook Air which cost about eight times as much (even accounting for the CM4, IO Board, M.2 to A+E-key adapter, and Intel AX210 card) gets WiFi speeds in the 700-900 Mbps range over the same network, since Apple is sticking with slower WiFi 6 radios in their current Mac lineup.
