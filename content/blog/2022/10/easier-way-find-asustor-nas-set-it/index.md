---
nid: 3248
title: "An easier way to find an ASUSTOR NAS to set it up"
slug: "easier-way-find-asustor-nas-set-it"
date: 2022-10-21T19:15:11+00:00
drupal:
  nid: 3248
  path: /blog/2022/easier-way-find-asustor-nas-set-it
  body_format: markdown
  redirects: []
tags:
  - asustor
  - iot
  - networking
  - nmap
  - terminal
  - tips
---

I have a few ASUSTOR NASes at my house, and I don't like installing a custom application just to identify the NAS so I can visit it's web UI the first time.

The official [ASUSTOR getting started guide](https://www.asustor.com/getting_start/steps?series=3) recommends installing [ASUSTOR Control Center](https://www.asustor.com/service/download_acc), which does a good job of identifying ASUSTOR devices on your network. And that's about it.

But behind the scenes, it's likely just scanning your network and matching any MAC addresses in Asustek's range. Which is easy to do without a third party app.

In my case, I can just run the following `nmap` command in the terminal and it spits out a list of all ASUS/ASUSTOR devices on my network:

```
$ sudo nmap -sn 10.0.100.0/24 | grep -B 2 Asustek
Nmap scan report for 10.0.100.1
Host is up (0.00083s latency).
MAC Address: 3C:7C:3F:6A:FA:C0 (Asustek Computer)
--
Nmap scan report for 10.0.100.220
Host is up (0.00023s latency).
MAC Address: 24:4B:FE:83:EB:F8 (Asustek Computer)
```

The first device is my router, an [ASUS RT-AX86U](https://amzn.to/3TteIiz), and the second device is a new [ASUSTOR Drivestor 4 Pro](https://amzn.to/3CMQpow) I just plugged into the network.

> Note: When you run this command, substitute your own network's IP range (e.g. `192.168.0.0`) where I have mine (`10.0.100.0`).
>
> The same command can be used for Synology or QNAP devices; just search for `Synology` or `Qnap` insteaad of `Asustek`.

Copy out the IP address, tack on the default port (8001), and visit http://10.0.100.220:8001/, and [bob's your uncle](https://en.wikipedia.org/wiki/Bob%27s_your_uncle)!

I don't generally like downloading an app just to identify a new device. It's more user-friendly, but it's a lot of hassle when there are multiple other ways to do the same thing.
