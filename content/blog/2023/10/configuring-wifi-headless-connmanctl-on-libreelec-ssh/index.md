---
nid: 3318
title: "Configuring wifi headless with connmanctl on LibreELEC via SSH"
slug: "configuring-wifi-headless-connmanctl-on-libreelec-ssh"
date: 2023-10-18T03:03:27+00:00
drupal:
  nid: 3318
  path: /blog/2023/configuring-wifi-headless-connmanctl-on-libreelec-ssh
  body_format: markdown
  redirects: []
tags:
  - connman
  - libreelec
  - linux
  - networking
  - wifi
---

Because I love doing things quite backwards, I found myself in a predicament: I had only a wired direct connection between my laptop and the Raspberry Pi where I was running LibreELEC. Using mDNS I could connect to it directly connected at `LibreELEC.local`, and that's great...

But I wanted to join it to a WiFi network, and I only had a not-great 6-button remote control to plug into the Pi, so entering in long passwords via the UI (if that's even possible without a keyboard?) was not something I wanted to attempt.

Since I could `ssh root@LibreELEC.local`, I figured I'd connect to the available WiFi network, so it would be more convenient to update the device and put more content on it. Not to mention it expands Kodi's capabilities if you give it an Internet connection!

## Enter ConnMan

LibreELEC uses [ConnMan](https://wiki.archlinux.org/title/ConnMan) to manage network interfaces, and setting WiFi is a little strange, but doable:

While logged into the LibreELEC machine, enter `connmanctl` to get into the ConnMan shell.

Then do the following:

```
# scan for access points
connmanctl> scan wifi

# list found access points
connmanctl> services
[list should appear here, with long unique hashes]

# enable ConnMan's agent to provide the WiFi password
connmanctl> agent on

# connect to the WiFi network
connmanctl> connect wifi_[long hash here for your AP]_managed_psk

# enter in the password when it prompts for "Passphrase?"
# wait for it to connect...

# then quit connmanctl
connmanctl> quit
```

Run `ip a` to check what the WiFi IP is; you can also connect via `LibreELEC.local` on the WiFi network, as long as it supports mDNS.
