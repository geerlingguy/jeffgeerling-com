---
date: '2026-11-26T23:18:00-06:00'
tags: ['mac', 'macos', 'linux', 'raspberry pi', 'usb', 'utilities', 'uhubctl', 'remote control']
title: 'Remotely unplugging a USB device on my Mac, without touching it'
slug: 'remote-control-usb-hub'
---
Tonight I was remote debugging a USB-C device with custom firmware, which was plugged into my Mac Studio at work. I was accessing it over a WireGuard VPN tunnel.

{{< figure
  src="m4-max-mac-studio-front.jpeg"
  alt="Front of M4 Max Mac Studio"
  width="700"
  height="auto"
  class="insert-image"
>}}

Part of the debugging process involves flashing firmware to the device using [MIDI SysEx messages](https://www.sweetwater.com/sweetcare/articles/how-do-i-send-and-receive-sysex-on-pc-or-mac/), and while handy, this technique can also be flaky, leaving the device in a partially-flashed state that needs a physical re-plug to recover from.

Unfortunately (well, fortunately, in terms of me taking some time off for Thanksgiving!), I am not physically present at the Mac, and the device I was testing _did_ need a physical unplug-and-replug.

I was going to give up, but instead I wondered if there was a way to power off a USB port on macOS, and then power it back on, which would effectively do what I needed.

A little research with Claude uncovered [`uhubctl`](https://github.com/mvp/uhubctl) which allows 'USB Hub per-port power control'—exactly what I wanted.

It works with Linux or macOS, and supports a ton of USB Hubs, but only listed explicit Mac support for the "M4 Mac mini (2 front ports only)" and "MacBook Air (Late 2010)".

Hoping I'd get lucky, I checked the status on my M4 Max Mac Studio:

```
# Install uhubctl with Homebrew
$ brew install uhubctl

# List all available ports
$ uhubctl
Current status for hub 8-3 [05ac:8009 Apple USB2 Hub 7423J07, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0103 power enable connect [3434:0b10 Keychron Keychron Q1 HE]
  Port 4: 0503 power highspeed enable connect [05e3:0610 GenesysLogic USB2.0 Hub, USB 2.00, 4 ports, ganged]
Current status for hub 8-1 [05ac:800a Apple USB3 Gen2 Hub 7423J07, USB 3.20, 4 ports, ppps]
  Port 1: 0203 power 5gbps U0 enable connect [0bad:c0de Device Under Test]
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 0203 power 5gbps U0 enable connect [05e3:0617 GenesysLogic USB3.0 Hub, USB 3.00, 4 ports, ganged]
```

I was in luck! The leftmost front USB-C port on the Mac Studio looked to be controllable. I ran the command to power cycle `Port 1` on `hub 8-1` with a 5 second delay between (`-d 5`):

```
$ sudo uhubctl -l 8-1 -p 1 -a cycle -d 5
Current status for hub 8-3 [05ac:8009 Apple USB2 Hub 7423J07, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
Sent power off request
New status for hub 8-3 [05ac:8009 Apple USB2 Hub 7423J07, USB 2.10, 4 ports, ppps]
  Port 1: 0000 off
Current status for hub 8-1 [05ac:800a Apple USB3 Gen2 Hub 7423J07, USB 3.20, 4 ports, ppps]
  Port 1: 0203 power 5gbps U0 enable connect [0bad:c0de Device Under Test]
Sent power off request
New status for hub 8-1 [05ac:800a Apple USB3 Gen2 Hub 7423J07, USB 3.20, 4 ports, ppps]
  Port 1: 00a0 off
Current status for hub 8-3 [05ac:8009 Apple USB2 Hub 7423J07, USB 2.10, 4 ports, ppps]
  Port 1: 0000 off
Sent power on request
New status for hub 8-3 [05ac:8009 Apple USB2 Hub 7423J07, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
Current status for hub 8-1 [05ac:800a Apple USB3 Gen2 Hub 7423J07, USB 3.20, 4 ports, ppps]
  Port 1: 00a0 off
Sent power on request
New status for hub 8-1 [05ac:800a Apple USB3 Gen2 Hub 7423J07, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
```

The device was power-cycled and re-connected (along with the corresponding USB 2 port, since both have to be toggled at the same time), and I could finish the firmware update.

What a handy tool! It doesn't work with Thunderbolt ports, but all the regular USB-C and USB-A ports on my Studio were available. And apparently it works on most models of Raspberry Pi, though their odd USB configuration means [you can only toggle power to all four ports at once](https://github.com/mvp/uhubctl#raspberry-pi-5).

Since it wasn't in the support matrix yet, I filed a PR to add the Mac Studio: [Add M4 Max Mac Studio](https://github.com/mvp/uhubctl/pull/691).
