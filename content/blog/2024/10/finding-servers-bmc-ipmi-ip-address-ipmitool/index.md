---
nid: 3414
title: "Finding a server's BMC / IPMI IP address with ipmitool"
slug: "finding-servers-bmc-ipmi-ip-address-ipmitool"
date: 2024-10-28T16:17:02+00:00
drupal:
  nid: 3414
  path: /blog/2024/finding-servers-bmc-ipmi-ip-address-ipmitool
  body_format: markdown
  redirects: []
tags:
  - administration
  - bmc
  - homelab
  - ipmi
  - remote access
  - server
  - supermicro
---

I test servers on a temporary basis a lot, and many enterprise servers don't have as user-friendly external port indications, or little OLED displays to provide useful information. They're no-frills because they don't need frills, you just deploy them and they run for years.

I often need to gain access to the server's IPMI/BMC interface to manage the server remotely, and it's not always obvious what IP address is assigned if you don't manually assign one via your router and a MAC address.

I could scan my network for the IP address, but assuming I have the server booted and it's a modern Supermicro or other standard system, I can use `ipmitool` to grab the BMC IP:

```
$ sudo ipmitool lan print

Set in Progress         : Set Complete
Auth Type Support       : 
Auth Type Enable        : Callback : 
                        : User     : 
                        : Operator : 
                        : Admin    : 
                        : OEM      : 
IP Address Source       : DHCP Address
IP Address              : 10.0.2.213
Subnet Mask             : 255.255.255.0
MAC Address             : e6:33:6f:f7:a1:07
SNMP Community String   : public
```

If you want the IPv6 address, change it to `lan6`:

```
ipmitool lan6 print
```

This also makes it easy to grab the MAC address for the BMC if you _do_ want to assign it a static IP in your router configuration.
