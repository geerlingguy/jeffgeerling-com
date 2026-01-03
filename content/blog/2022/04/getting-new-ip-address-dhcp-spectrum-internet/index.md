---
nid: 3199
title: "Getting a new IP address via DHCP from Spectrum Internet"
slug: "getting-new-ip-address-dhcp-spectrum-internet"
date: 2022-04-05T16:35:33+00:00
drupal:
  nid: 3199
  path: /blog/2022/getting-new-ip-address-dhcp-spectrum-internet
  body_format: markdown
  redirects: []
tags:
  - cable
  - ddos
  - dns
  - homelab
  - ip
  - isp
  - spectrum
---

Recently this website's [been the target](/blog/2022/three-ddos-attacks-on-my-personal-website) of malicious DDoS attacks.

But after accidentally leaking my home IP address in some network benchmarking clips in a recent YouTube video, the same attacker (I assume) decided to point the DDoS cannon at my home IP.

I have things relatively locked down here—more on homelab security coming soon!—but a DDoS isn't something most residential ISPs take too kindly. So it was time for me to recycle my home IP. Lucky for me, I don't pay for a static IP address. That makes home hosting more annoying sometimes, since I have to deal with tunnels and dynamic DNS, but it also means I can hop to a new IP address if one is under attack.

## Getting a new IP address

At least with the DOCSIS 3.1 modem I'm using, the overall process is as follows:

  1. Turn off the cable modem.
  2. Set a new MAC address on the router.
  3. Restart the router.
  4. Restart the cable modem.

As an alternative for #2, you could just plug a different device directly into the cable modem. The main thing is, if the cable modem (and thus your ISP's endpoint) sees a new MAC address for the device attached to the modem, it will assign a new IP address via DHCP.

On my own router, an ASUS, there's a simple method you can use to change the MAC address—you go into the WAN settings, then under 'Special Requirement from ISP', there's a custom MAC address field.

You can either clone your current computer's MAC address into the field by clicking 'MAC Clone', or enter a valid MAC address for some other device here. Press 'Apply', and wait for the router to restart before turning the cable modem back on.

If you want to drop the custom MAC address and switch back to the router's default WAN MAC address, you could do that at some point—but I'd give it a day or two, since that's the typical DHCP address timeout. If you switch back right away, your ISP will probably hand out the same IP address you just had.

Thanks to [this Spectrum community discussion](https://community.spectrum.net/discussion/159758/how-can-i-change-my-public-ip-address) for the idea.

> Aside: When I contacted Spectrum's support this morning, their recommendation was to replace both my cable modem and router. It technically would achieve the same goal, but I wasn't about to spend a few hundred bucks replacing equipment! I'm surprised they don't have a mechanism internally to release an IP, but maybe that's not available to their lower support tiers.
