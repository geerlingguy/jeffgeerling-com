---
nid: 2649
title: "SSH into a Raspberry Pi with only a network cable using OS X's 'Internet Sharing'"
slug: "ssh-raspberry-pi-only-network-cable-using-os-xs-internet-sharing"
date: 2016-05-11T03:10:17+00:00
drupal:
  nid: 2649
  path: /blog/2016/ssh-raspberry-pi-only-network-cable-using-os-xs-internet-sharing
  body_format: markdown
  redirects: []
tags:
  - internet
  - mac
  - networking
  - raspberry pi
  - ssh
  - tether
---

Recently, I found myself in a situation where I had to connect to a Raspberry Pi to set it up for a presentation, but I did not have:

  - A keyboard and/or other input device to use to type anything into the Pi
  - An HDMI cable to connect the Pi to a display so I could view anything on the Pi
  - A microSD card reader so I could modify the contents of the Pi's microSD card

Because of this, none of the standard methods of setting a static IP address, reconfiguring the Pi's WiFi configuration, or logging in on the Pi itself to find it's IP address or set things up so I could connect over a local network would work.

I remembered that Mac OS X handily includes an 'Internet Sharing' feature, which sets up a bridged network interface so your Mac is effectively a router and DHCP server to any devices connected to the shared interface.

In my case, I just wanted to take a stock Pi, and be able to connect to it via SSH, but I needed an IP address I could use to connect to it. Since it's configured to use DHCP for it's default wired network connection, I plugged in a standard ethernet cable between my Mac and the Pi's LAN port, then did the following steps:

  1. Open System Preferences, and go to 'Sharing'
  2. Click on the 'Internet Sharing' row in the service list, and choose an interface to share from (in my case, WiFi)
  3. Check the box next to your wired network interface (in my case, 'USB 10/100/1000 LAN')
  4. Check the 'On' checkbox next to Internet Sharing to enable it
  5. Wait a few seconds to let things work
  6. In Terminal, type in `ifconfig` to get a list of all interfaces—there should be a new `bridge100` interface at the end of the list
  7. Copy that IP address, then add 1 to the last number. That should be the IP address of the Pi.
  8. Enter `ssh pi@[bridge100-ip-address-plus-one-goes-here]`, and log in using the default password `raspberry`.

Next time, I'll remember to bring a keyboard and HDMI cable. Or a microSD card reader.
