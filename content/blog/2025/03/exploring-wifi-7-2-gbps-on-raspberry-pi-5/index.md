---
nid: 3451
title: "Exploring WiFi 7 (at 2 Gbps) on a Raspberry Pi 5"
slug: "exploring-wifi-7-2-gbps-on-raspberry-pi-5"
date: 2025-03-14T14:02:12+00:00
drupal:
  nid: 3451
  path: /blog/2025/exploring-wifi-7-2-gbps-on-raspberry-pi-5
  body_format: markdown
  redirects:
    - /blog/2025/wifi-7-on-raspberry-pi-just-got-whole-lot-easier
    - /blog/2025/exploring-wifi-7-on-raspberry-pi-5
aliases:
  - /blog/2025/wifi-7-on-raspberry-pi-just-got-whole-lot-easier
  - /blog/2025/exploring-wifi-7-on-raspberry-pi-5
tags:
  - be200
  - intel
  - linux
  - pi 5
  - raspberry pi
  - wifi
  - wifi 6e
  - wifi 7
---

{{< figure src="./pi5-waveshare-m2-hat-wifi-7.jpg" alt="Raspberry Pi 5 with Waveshare WiFi HAT+" width="700" height="394" class="insert-image" >}}

Last time I seriously dug into 6 GHz WiFi was with 6E on a [Raspberry Pi CM4 with Intel's AX210 card](/blog/2023/getting-15-gbps-wifi-6e-on-raspberry-pi-cm4), in 2023.

Back then—and even up until recently—using WiFi 6E or WiFi 7 on a Raspberry Pi meant [recompiling Linux](/blog/2025/how-recompile-linux-on-raspberry-pi), as the `iwlwifi` Linux drivers weren't included with the default Pi OS install.

But recently, the [Intel WiFi drivers were added by default](https://github.com/raspberrypi/linux/issues/6497), and now all that's required is loading in the right firmware.

I've now tested cheap [AX210](https://amzn.to/3QKsWvM) (WiFi 6E) and [BE200](https://amzn.to/3XpNGg2) (WiFi 7) cards, and both work great, giving 1 Gbps+ of wireless throughput on the Pi 5. And some people even have [AP mode working on Intel cards](https://archfx.me/posts/2025/02/router/), meaning you can set up a Pi with something like [RaspAP](https://raspap.com) for a completely custom portable Linux WiFi travel router!

I was testing these mostly to see how the multi-gig WiFi experience was on the Raspberry Pi, and also as a way to justify upgrading to a WiFi 7 AP at my studio—I just ordered a [Netgear WBE710 WiFi 7 AP](https://amzn.to/3XmEycc), and I'll be poking and prodding with the Pi since it's the only other device I own with WiFi 7 besides my iPhone.

## WiFi 7

But quickly, what's WiFi 7—besides the latest iteration of the WiFi standard?

At a very high level, it's kind of 'WiFi 6E+'—WiFi 6 had the golden opportunity to be the "version 6" that introduced 6 GHz wireless frequencies... except it didn't. It still used the 5 GHz wireless band (in addition to 2.4 GHz).

It wasn't until WiFi 6E (or 802.11ax) that the much-less-saturated 6 GHz band was put to use. WiFi 6E also added more bandwidth through wider channels (e.g. 160 MHz instead of 20/40/80 MHz), tricks like 1024-QAM, MU-MIMO, and OFDMA to cram more capacity into the same amount of wireless spectrum.

WiFi 7 basically amps up WiFi 6E, tacking on a couple new features, most notably MLO, or Multi-Link Operation. This allows for more than one channel to be in use at the same time, kind of like hard-wired Ethernet's Link Aggregation or bonding (though more transparent to the user).

WiFi 6E support was just barely showing up in drivers and end-user devices when WiFi 7 was launched, and even though many companies sell WiFi 7 devices, very few consumer products have radios that will take advantage. WiFi 6E is still new enough that 6 GHz radios are sometimes disabled in brand new WiFi 7 access points by default, as was the case with my new Netgear AP!

Bottom line, WiFi 7 takes all the features that made WiFi 6E great—most notably the additional less-crowded 6 GHz wireless spectrum—and takes them just a little further, offering multi-gigabit wireless connections that can scale to dozens or even _hundreds_ of users per access point, with the right hardware.

## Connecting WiFi over PCIe

{{< figure src="./intel-be200-raspberrypi-wifi-7.jpg" alt="Intel BE200 Wireless WiFi 7 card on Waveshare HAT+ E-Key on Pi 5" width="700" height="368" class="insert-image" >}}

For my _own_ setup, I'm using one of Waveshare's new [PCIe to M.2 E-key HAT+ adapters](https://amzn.to/3Fio922). The one I just linked includes PoE+, so you can power your WiFi Pi directly from a suitable PoE+ switch. The one pictured in this post is their [non-PoE version](https://amzn.to/3DBWybJ) for a little cheaper.

Mount the HAT onto a Pi 5, and insert any standard M.2 E-key WiFi card into the HAT—I tested both an AX210 and BE200.

## Video

I published a video showing the setup of my new WiFi 7 AP, installing the HAT on the Pi 5, and configuring Raspberry Pi OS / Linux for WiFi 7, over on my YouTube channel. You can also watch that video here:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/1oXrJ4wQ2dQ" frameborder='0' allowfullscreen></iframe></div>
</div>

## Intel WiFi - Setup on the Pi, in Linux

Boot up the Pi and use `lspci` to check if your card is identified. It should show up alongside two Broadcom PCIe bridges and the RP1 South Bridge:

```
pi@pi5-wifi:~ $ lspci
0000:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
0000:01:00.0 Network controller: Intel Corporation Wi-Fi 7(802.11be) AX1775*/AX1790*/BE20*/BE401/BE1750* 2x2 (rev 1a)
0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
0001:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
```

If you use `lspci -vv`, you'll see that the Pi even identifies the right `iwlwifi` kernel module for the card:

```
0000:01:00.0 Network controller: Intel Corporation Wi-Fi 7(802.11be) AX1775*/AX1790*/BE20*/BE401/BE1750* 2x2 (rev 1a)
	Subsystem: Intel Corporation Wi-Fi 7(802.11be) AX1775*/AX1790*/BE20*/BE401/BE1750* 2x2 (BE200 320MHz [Gale Peak])
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 38
	Region 0: Memory at 1b80000000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: iwlwifi
	Kernel modules: iwlwifi
```

> **Note**: If you _don't_ see `iwlwifi`, make sure you're on the latest version of Pi OS. Run `sudo apt update && sudo apt upgrade -y` to upgrade.

However, if you run `ip a` or `nmcli`, you won't find the adapter listed. That's because the _firmware_ is still needs to be installed. You can confirm the exact firmware the Pi is looking for with:

```
$ dmesg | grep iwlwifi
...
[    5.104112] Intel(R) Wireless WiFi driver for Linux
[    5.104193] iwlwifi 0000:01:00.0: enabling device (0000 -> 0002)
[    5.124277] iwlwifi 0000:01:00.0: Detected crf-id 0x400410, cnv-id 0x400410 wfpm id 0x80000000
[    5.124300] iwlwifi 0000:01:00.0: PCI dev 2725/0024, rev=0x420, rfid=0x10d000
[    5.124397] iwlwifi 0000:01:00.0: Direct firmware load for iwlwifi-ty-a0-gf-a0-83.ucode failed with error -2
[    5.124413] iwlwifi 0000:01:00.0: Direct firmware load for iwlwifi-ty-a0-gf-a0-82.ucode failed with error -2
[    5.124631] iwlwifi 0000:01:00.0: no suitable firmware found!
...
```

To get the firmware, you would normally install the `iwlwifi-firmware` package, but since these cards are newer, it seems the firmware package is out of sync with what's actually expected in the `iwlwifi` kernel module.

So instead, following the [Linux Wireless documentation's guide](https://wireless.docs.kernel.org/en/latest/en/users/drivers/iwlwifi.html), you can download the Intel firmware directly from the `linux-firmware` Git repo:

```
# NOTE: Firmware versions may be different; check dmesg logs to be certain!

# WiFi firmware
cd /lib/firmware
sudo wget -o - -q https://web.git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/iwlwifi-gl-c0-fm-c0-83.ucode
sudo wget -o - -q https://web.git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/iwlwifi-gl-c0-fm-c0.pnvm

# Bluetooth firmware (optional; see Bluetooth section later in this post)
sudo mkdir -p /lib/firmware/intel
cd /lib/firmware/intel
sudo wget -o - -q https://web.git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/intel/ibt-0041-0041.ddc
sudo wget -o - -q https://web.git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/intel/ibt-0041-0041.sfi
```

Reboot the Pi, and check with `dmesg | grep iwlwifi` to ensure the module loaded correctly. Then confirm you can see the device with `nmcli` as well:

```
$ nmcli
...
wlan1: unavailable
        "Intel 7 AX1775*/AX1790*/BE20*/BE401/BE1750* 2x2"
        wifi (iwlwifi), C8:15:4E:26:D3:BF, sw disabled, hw, mtu 1500
...
```

Unless you disabled the Pi's internal WiFi, you'll also see the `wlan0` interface.

If the interface reports as `unavailable`, that probably means you haven't set a regulatory WiFi Country. Do so with `sudo raspi-config` or via the Pi settings app in the GUI. WiFi radios are disabled until you select a country, because different countries have different frequency use regulations.

Now it should show as `disconnected` in `nmcli`, and if you want to connect to a network, get a list of all available SSIDs and connect using the following commands:

```
# Connect to a WiFi network on wlan1, the PCIe card
$ nmcli d wifi list
$ sudo nmcli d wifi connect "ssid_here" password "password_here" ifname wlan1
```

_Hopefully_ you're connected. Get connection details with:

```
# Show WiFi information and connection details
$ nmcli device show wlan1
GENERAL.DEVICE:                         wlan1
GENERAL.TYPE:                           wifi
GENERAL.HWADDR:                         C8:15:4E:26:D3:BF
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     [redacted]
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/3
IP4.ADDRESS[1]:                         10.0.2.234/24
IP4.GATEWAY:                            10.0.2.1
IP4.ROUTE[1]:                           dst = 10.0.2.0/24, nh = 0.0.0.0, mt = 600
IP4.ROUTE[2]:                           dst = 0.0.0.0/0, nh = 10.0.2.1, mt = 600
IP4.DNS[1]:                             10.0.2.1
IP4.DOMAIN[1]:                          mmoffice.net
IP6.ADDRESS[1]:                         fe80::d609:2a3c:870f:c90e/64
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = fe80::/64, nh = ::, mt = 1024

$ iw dev wlan1 info
Interface wlan1
	ifindex 4
	wdev 0x100000001
	addr c8:15:4e:26:d3:bf
	ssid [redacted]
	type managed
	wiphy 1
	channel 40 (5200 MHz), width: 80 MHz, center1: 5210 MHz
	txpower 21.00 dBm
	multicast TXQ:
		qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets
		0	0	0	0	0	0	0	0		0
```

But more than likely, if you connected to a 6 GHz network, the Broadcom WiFi drivers might've rained on your parade—at least they did in my case. I saw it got disconnected pretty quickly, and when I checked the system logs with `dmesg`, I found the culprit:

```
[ 1046.305801] brcmfmac: brcmf_set_channel: set chanspec 0xd022 fail, reason -52
```

It seemed related to the Broadcom WiFi driver for the internal WiFi chip, so I added `disable-wifi` inside `/boot/firmware/config.txt`, and rebooted:

```
[all]
dtoverlay=disable-wifi
```

Reboot and try connecting again. You can use `sudo nmtui` for a more graphical interface. The Pi OS GUI actually shows 6 GHz connections, but _currently_ they are [falsely labeled as 5G](https://github.com/raspberrypi/bookworm-feedback/issues/386).

## Testing WiFi throughput

{{< figure src="./pi-wifi-antennas-external-waveshare-7-be200.jpg" alt="Pi 5 WiFi 7 with external antennas" width="700" height="394" class="insert-image" >}}

To see how fast your WiFi connection is, install `iperf3`: `sudo apt install -y iperf3`. Use another computer on your LAN (ideally connected directly to the WiFi router via Ethernet, or through some other wired connection—otherwise it's own WiFi connection could taint your results!

Then run `iperf3 -s` on your main computer (the one connected via wired Ethernet), and run `iperf3 -c [ip]` on your Pi:

```
$ iperf3 -c 10.0.2.15
Connecting to host 10.0.2.15, port 5201
[  5] local 10.0.2.234 port 48918 connected to 10.0.2.15 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  49.5 MBytes   415 Mbits/sec    0   1.85 MBytes       
[  5]   1.00-2.00   sec  52.5 MBytes   441 Mbits/sec    0   2.46 MBytes       
[  5]   2.00-3.00   sec  53.8 MBytes   451 Mbits/sec    0   2.59 MBytes       
[  5]   3.00-4.00   sec  52.5 MBytes   440 Mbits/sec    0   2.59 MBytes       
[  5]   4.00-5.00   sec  55.0 MBytes   461 Mbits/sec    0   3.28 MBytes       
[  5]   5.00-6.00   sec  55.0 MBytes   461 Mbits/sec    0   3.46 MBytes       
[  5]   6.00-7.00   sec  53.8 MBytes   451 Mbits/sec    0   3.46 MBytes       
[  5]   7.00-8.00   sec  55.0 MBytes   461 Mbits/sec    0   3.66 MBytes       
[  5]   8.00-9.00   sec  55.0 MBytes   461 Mbits/sec    0   3.66 MBytes       
[  5]   9.00-10.00  sec  52.5 MBytes   440 Mbits/sec    0   3.66 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   534 MBytes   448 Mbits/sec    0             sender
[  5]   0.00-10.02  sec   533 MBytes   446 Mbits/sec                  receiver

iperf Done.
```

Don't be alarmed if you're not getting gigabit-plus speeds, even on a WiFi 7 network!

There are many reasons you might have diminished performance:

  - The closer the better; RF follows the inverse square law, so you'll have less signal the further you are from the WiFi router/AP.
  - Your router/AP might have suboptimal WiFi 5/6/7 settings, like narrow channel bandwidth. Or it might not have QAM or other optional settings enabled that speeds up the connection.
  - Your network might be in a high-interference environment, especially on the 2.4 or 5 GHz bands. Sometimes there's little you can do (e.g. if you're in an apartment complex or noisy office environment.
  - If you have a mixed network (e.g. it is one SSID on 2.4, 5, and 6 GHz bands), the Pi might choose a more stable/reliable frequency (e.g. 2.4 or 5 GHz) instead of the faster 6 GHz band—especially if you're more than a few feet away from your WiFi router/AP!

## Improving the signal using `wavemon`

The version of `wavemon` that ships with Raspberry Pi OS 12 doesn't seem to support the latest Intel WiFi adapters, so you may need to build it from source:

```
sudo apt remove -y wavemon  # If you already have it installed
sudo apt-get -y install pkg-config libncursesw6 libtinfo6 libncurses-dev libnl-cli-3-dev git
git clone https://github.com/uoaerg/wavemon.git
cd wavemon
./configure && make && sudo make install
```

To monitor your WiFi connection, run the version of `wavemon` you just built, passing it the `wlan0` interface:

```
./wavemon -i wlan0
```

If successful, you should get a live-updating screen with all the WiFi connection details:

{{< figure src="./wavemon-wifi-7.jpg" alt="Wavemon monitoring wifi 7" width="700" height="369" class="insert-image" >}}

You can also press F2 to get a histogram (a graph of the signal level over time).

Use these visual tools to find the best antenna positioning for speed and stable connection (or to test different antennas—not all are created equal!).

## What about 6 GHz?

If you have a newer WiFi router or AP with WiFi 6E or 7 support, _and_ you have a 6 GHz radio enabled (many current-gen devices disable the 6 GHz band by default), you might notice the Pi is only using 2.4 or 5 GHz bands. To get the _fastest_ speeds, you need to use the 6 GHz band (taking into account the signal issues I listed earlier).

The Pi's current version of NetworkManager—version 1.42.x—doesn't display 6 GHz information:

```
$ nmcli -f wifi-properties dev show wlan0
WIFI-PROPERTIES.WEP:                    yes
WIFI-PROPERTIES.WPA:                    yes
WIFI-PROPERTIES.WPA2:                   yes
WIFI-PROPERTIES.TKIP:                   yes
WIFI-PROPERTIES.CCMP:                   yes
WIFI-PROPERTIES.AP:                     yes
WIFI-PROPERTIES.ADHOC:                  yes
WIFI-PROPERTIES.2GHZ:                   yes
WIFI-PROPERTIES.5GHZ:                   yes
WIFI-PROPERTIES.MESH:                   no
WIFI-PROPERTIES.IBSS-RSN:               yes
```

It shows `2GHZ` and `5GHZ`, but no `6GHZ`. Support for the 6 GHz band was [added in version 1.46](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/merge_requests/1739), but technically 6 GHz bands will still work, you just might not see all the information in NetworkManager UIs.

### Installing a newer version of NetworkManager (OPTIONAL)

If you want to get your Pi on the latest version of NetworkManager, you could switch to Debian's `testing` repository, to get the latest tested versions of all the packages required.

This is kind of the 'shotgun' approach—just updating _everything_ on the system—but you could tweak your apt preferences to just target the networking packages for update instead.

Edit your Apt sources: `sudo nano /etc/apt/sources.list`, and add in the Debian testing repository. Add the following line to the end of that file and save it:

```
deb http://deb.debian.org/debian testing main contrib non-free
```

Then run the following commands to update apt, remove a conflicting package (I hope you don't need `ppp`!), and upgrade everything:

```
$ sudo apt update
$ sudo apt remove ppp
$ sudo apt upgrade -y
```

The upgrade will take a while—when it's done, reboot (`sudo reboot`), and you _should_ have a later version of NetworkManager. Check with `nmcli -v`:

```
$ nmcli -v
nmcli tool, version 1.50.3
```

And assuming you still have your WiFi card plugged in, you should see `6GHZ` now:

```
$ nmcli -f wifi-properties dev show wlan0
...
WIFI-PROPERTIES.2GHZ:                   yes
WIFI-PROPERTIES.5GHZ:                   yes
WIFI-PROPERTIES.6GHZ:                   yes
```

### _Actually_ getting 6 GHz

If you check the WiFi status (`iw dev wlan1 info`), you might _still_ see it using a 5 or 2.4 GHz band—what gives?

Well, since 6 GHz is the shortest wavelength, it typically has the worst signal of the three, so I've found the driver often chooses one of the lower bands.

NetworkManager allows you to force a band, with the `wifi.band` property. You can configure it under `[wifi]` inside `/etc/NetworkManager/system-connections`, but it's just as easy to use `nmcli`, for example:

```
# Force 2.4 GHz bands only
$ sudo nmcli connection modify YOUR_SSID_HERE wifi.band bg

# Force 5 GHz bands only
$ sudo nmcli connection modify YOUR_SSID_HERE wifi.band a
```

However, for 6 GHz bands (WiFi 6E / `ax`, or WiFi 7 / `be`), it doesn't work:

```
$ sudo nmcli connection modify GE_6G wifi.band ax
Error: failed to modify 802-11-wireless.band: 'ax' not among [a, bg].
```

It seems the feature's just not implemented in NetworkManager yet, so I opened a feature request for it: [Allow configuration of 6 Ghz (ax/be) WiFi bands](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues/1735).

It'll be a while for that to get fixed, so the next best option is to configure a separate 6 GHz-only SSID on your wireless router or AP.

On my [Netgear WBE710](https://amzn.to/3Fdksee) it's easy enough... though many consumer APs might not make it as easy to create separate networks for different radio bands.

After separating out a `GE_6G` SSID with _just_ the 6 GHz network in `be` mode, and a `GE_BE` SSID with all three radios for testing things like MLO (Multi-Link Operation), I connected to each on the Pi 5.

That resolved the connection issues, and I was able to connect on 2.4, 5, or 6 GHz networks, for example:

```
$ iw dev wlan0 info
Interface wlan0
	ifindex 3
	wdev 0x1
	addr c8:15:4e:26:d3:bf
	ssid GE_6G
	type managed
	wiphy 0
	channel 5 (5975 MHz), width: 320 MHz, center1: 6105 MHz
	txpower 22.00 dBm
```

With external WiFi antennas connected, I was able to get 1.4 Gbps of bandwidth. And looking closer at my `lspci` output, I noticed the BE200 supports PCIe Gen 4x1 speeds, up to 16 GT/sec. The Pi 5 by default only runs at PCIe Gen 2, or 5 GT/sec. If I [bumped up the PCIe lane to Gen 3](/blog/2023/forcing-pci-express-gen-30-speeds-on-pi-5), I was able to get nearly _2 Gbps_!

```
$ iperf3 -c 10.0.2.15
Connecting to host 10.0.2.15, port 5201
[  5] local 10.0.2.245 port 33668 connected to 10.0.2.15 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   194 MBytes  1.63 Gbits/sec    0   3.13 MBytes       
[  5]   1.00-2.00   sec   219 MBytes  1.84 Gbits/sec    0   3.13 MBytes       
[  5]   2.00-3.00   sec   220 MBytes  1.85 Gbits/sec    0   3.32 MBytes       
[  5]   3.00-4.00   sec   220 MBytes  1.85 Gbits/sec    0   3.32 MBytes       
[  5]   4.00-5.00   sec   211 MBytes  1.77 Gbits/sec    0   3.32 MBytes       
[  5]   5.00-6.00   sec   206 MBytes  1.73 Gbits/sec    0   3.54 MBytes       
[  5]   6.00-7.00   sec   219 MBytes  1.84 Gbits/sec    0   3.54 MBytes       
[  5]   7.00-8.00   sec   220 MBytes  1.85 Gbits/sec    0   3.54 MBytes       
[  5]   8.00-9.00   sec   238 MBytes  1.99 Gbits/sec    0   3.54 MBytes       
[  5]   9.00-10.00  sec   238 MBytes  1.99 Gbits/sec    0   3.54 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.13 GBytes  1.83 Gbits/sec    0             sender
[  5]   0.00-10.00  sec  2.13 GBytes  1.83 Gbits/sec                  receiver
```

Not bad at all! Even with `--bidir` simulating maximum throughput both ways, I was able to get 1.3 Gbps down, and 472 Mbps up.

I also tried testing MLO (Multi-Link Operation), which join two bands together (e.g. 5 GHz and 6 GHz) for even more speed, but I wasn't able to get that working—not sure if it's a feature that needs support from NetworkManager, Pi OS, the Intel Driver, or what, but even when it was enabled on the AP, it never seemed to make a difference in my tests.

## Raspberry Pi as a WiFi 7 AP?

All this leads to the natural question of whether you can run a Raspberry Pi 5 as a WiFi 7 Access Point... to which the answer is _maybe_.

Intel's drivers notoriously make using AP mode (where the Pi is basically your WiFi router, giving wireless clients access to a wired network) difficult, though people have found ways to get it working.

On my BE200 it _shows_ as being supported in NetworkManager, and I naively attempted [creating a Pi hotspot](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/709#issuecomment-2711737787), but couldn't get it working that way.

Apparently [Aruna Jayasena has configured the BE200 for a 2.4/5 GHz RaspAP Travel Router](https://archfx.me/posts/2025/02/router/), and I'm going to attempt something similar soon (so stay tuned!). And projects like [RaspAP](https://github.com/RaspAP/raspap-webgui) and [OpenWRT](https://openwrt.org/toh/raspberry_pi_foundation/raspberry_pi) are probably the best candidates for a Pi travel router build.

But since I haven't personally gotten it to work, I can't give any specific recommendations for AP or Ad-Hoc mode.

## Bluetooth

Earlier I mentioned optional bluetooth setup—Intel's WiFi adapters also include the latest and greatest Bluetooth functionality, and it can not only provide a little boost over the range and quality of the Pi's built-in Bluetooth, it also allows for easier external antenna connections, if you have your Pi in a metal enclosure!

Check if the Bluetooth functionality is working with: `dmesg | grep Bluetooth`

Since the Bluetooth connection is routed through USB pins on the E-key M.2 connector, you _must_ have a HAT that adapts those pins to a header or port you plug into one of the Pi's USB ports. Otherwise Bluetooth _will not_ work.

Assuming you have it plugged in, and you have the proper Bluetooth firmware files installed (reboot after adding them), you can use `hciconfig` to check on Bluetooth status:

```
$ sudo hciconfig
hci1:	Type: Primary  Bus: UART
	BD Address: D8:3A:DD:84:FB:3C  ACL MTU: 1021:8  SCO MTU: 64:1
	UP RUNNING 
	RX bytes:3701 acl:0 sco:0 events:388 errors:0
	TX bytes:66466 acl:0 sco:0 commands:388 errors:0

hci0:	Type: Primary  Bus: USB
	BD Address: C8:15:4E:26:D3:C3  ACL MTU: 1021:4  SCO MTU: 96:6
	DOWN 
	RX bytes:24877 acl:0 sco:0 events:4023 errors:0
	TX bytes:997549 acl:0 sco:0 commands:4021 errors:0
```

In this case, `hci1` is the internal Pi Bluetooth, and `hci0` is the Intel Bluetooth. I want to disable internal Bluetooth and enable Intel, so I'll run:

```
$ sudo hciconfig hci1 down
$ sudo hciconfig hci0 up
Can't init device hci0: Operation not possible due to RF-kill (132)
```

If you get this `RF-kill` message, check what's blocking it, and if it's just `Soft blocked`, use `rfkill unblock` to get it working:

```
$ rfkill list all
0: hci0: Bluetooth
	Soft blocked: yes
	Hard blocked: no
1: hci1: Bluetooth
	Soft blocked: no
	Hard blocked: no
2: phy0: Wireless LAN
	Soft blocked: no
	Hard blocked: no
3: phy1: Wireless LAN
	Soft blocked: no
	Hard blocked: no

$ sudo rfkill unblock bluetooth
```

### Testing Bluetooth functionality

Now you should be able to get Bluetooth functionality through the Intel adapter:

```
pi@pi5-wifi:~ $ sudo hciconfig hci0 up
pi@pi5-wifi:~ $ sudo hciconfig
hci1:	Type: Primary  Bus: UART
	BD Address: D8:3A:DD:84:FB:3C  ACL MTU: 1021:8  SCO MTU: 64:1
	DOWN 
	RX bytes:4461 acl:0 sco:0 events:433 errors:0
	TX bytes:67252 acl:0 sco:0 commands:433 errors:0

hci0:	Type: Primary  Bus: USB
	BD Address: C8:15:4E:26:D3:C3  ACL MTU: 1021:4  SCO MTU: 96:6
	UP RUNNING 
	RX bytes:25759 acl:0 sco:0 events:4085 errors:0
	TX bytes:998415 acl:0 sco:0 commands:4083 errors:0
```

Use `bluetoothctl` to work with the Bluetooth interface—or if you're running a GUI, try using its Bluetooth options in the menu bar (note: I haven't tested Intel WiFi with Raspberry Pi OS's menu bar Bluetooth settings menu. Not sure if that works!):

```
$ bluetoothctl
Agent registered
[CHG] Controller D8:3A:DD:84:FB:3C Pairable: yes
[CHG] Controller C8:15:4E:26:D3:C3 Pairable: yes
[bluetooth]# scan on
Discovery started
[CHG] Controller C8:15:4E:26:D3:C3 Discovering: yes
[NEW] Device 5B:2E:B8:30:1F:E2 5B-2E-B8-30-1F-E2
[NEW] Device 76:1C:2A:13:AD:D9 76-1C-2A-13-AD-D9
[NEW] Device 4A:FC:E4:08:02:B3 4A-FC-E4-08-02-B3
[NEW] Device D2:EE:48:DB:23:95 Logi M550 L
```

For all my debugging and test details, please check the following GitHub issues:

  - [PiPCI: Intel BE200 WiFi adapter](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/670)
  - [PiPCI: Intel AX210 WiFi adapter](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/120)
  - [Waveshare PCIe to M.2 E-Key WiFi HAT+](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/709)
