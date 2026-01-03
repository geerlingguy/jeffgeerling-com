---
nid: 3345
title: "Resolving 'Temporary failure in name resolution' on Pi OS 12 Bookworm"
slug: "resolving-temporary-failure-name-resolution-on-pi-os-12-bookworm"
date: 2024-02-04T03:51:21+00:00
drupal:
  nid: 3345
  path: /blog/2024/resolving-temporary-failure-name-resolution-on-pi-os-12-bookworm
  body_format: markdown
  redirects: []
tags:
  - debian
  - dns
  - docker
  - networkmanager
  - nmcli
  - pi os
  - raspberry pi
---

Raspberry Pi OS version 12 (based on Debian 12 Bookworm) uses NetworkManager instead of dhcpcd for managing network connections, DNS resolution settings, DHCP, etc.

I've already mentioned [using `nmcli` and `nmtui` for managing WiFi settings](https://www.jeffgeerling.com/blog/2023/nmcli-wifi-on-raspberry-pi-os-12-bookworm), but I ran into a strange issue after installing Docker on a fresh Raspberry Pi OS installation today. Suddenly DNS stopped working.

Trying to ping anything on the Internet gave me:

```
$ ping www.google.com
ping: www.google.com: Temporary failure in name resolution
```

As always, [It was DNS](https://redshirtjeff.com/listing/it-was-dns-shirt?product=211). It was like DNS just gave up the ghost! Trying to change settings via `nmtui` seemed to not work (I tried DHCP for IPv4 with manual DNS, and that wasn't working).

Luckily, I found [this post](https://serverfault.com/a/810639) and followup comments mentioning the proper `nmcli` incantation to override DNS settings for an interface, so here it is (assuming built-in Ethernet):

```
$ sudo nmcli device mod eth0 ipv4.dns "8.8.8.8 8.8.4.4"
Connection successfully reapplied to device 'eth0'.
```

But you'll still need to restart NetworkManager for the change to take effect:

```
$ sudo systemctl restart NetworkManager
```

Now DNS works. I will have to do some more digging into why Docker seems to have eaten my DNS. This particular Pi is doing a couple interesting network-related things though, sooo... I can't lay all the blame on Docker. It may be that some of Docker's virtual networking blew up a configuration I had made earlier :)
