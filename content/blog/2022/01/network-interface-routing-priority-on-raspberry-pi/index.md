---
nid: 3168
title: "Network interface routing priority on a Raspberry Pi"
slug: "network-interface-routing-priority-on-raspberry-pi"
date: 2022-01-13T22:47:23+00:00
drupal:
  nid: 3168
  path: /blog/2022/network-interface-routing-priority-on-raspberry-pi
  body_format: markdown
  redirects:
    - /blog/2022/changing-network-interface-routing-priority-on-raspberry-pi
aliases:
  - /blog/2022/changing-network-interface-routing-priority-on-raspberry-pi
tags:
  - 4g
  - benchmarking
  - dhcpcd
  - eth0
  - ethernet
  - kernel
  - linux
  - lte
  - networking
  - router
  - usb0
---

{{< figure src="./52pi-Raspberry-Pi-CM4-Router-Board.jpeg" alt="52Pi Raspberry Pi Compute Module 4 Router Board" width="650" height="389" class="insert-image" >}}

As I start using Raspberry Pis for more and more network routing activities—especially as the Compute Module 4  routers based on Debian, OpenWRT, and VyOS have started appearing—I've been struggling with one particular problem: _how can I set routing priorities for network interfaces?_

Now, this is a bit of a loaded question. You could dive right into routing tables and start adding and deleting routes from the kernel. You could mess with subnets, modify firewalls, and futz with iptables.

But in my case, my need was simple: I wanted to test the speed of a specific interface, either from one computer to another, or over the Internet (e.g. via `speedtest-cli`).

The problem is, even if you try limiting an application to a specific IP address (each network interface has its own), the Linux kernel will choose whatever network route it deems the best.

But here's the problem: if I have `eth0`, connected to the Internet via a fast gigabit connection, and `usb0`, connected over slow 4G, the route will always be delivered through `eth0`.

## Can't change the `metric`

And that's because by default, at least on Debian / Raspberry Pi OS (which uses dhcpcd), the routing table looks like this:

```
pi@turing-node-1:~ $ ip route list
default via 10.0.100.1 dev eth0 proto dhcp src 10.0.100.250 metric 202 
default via 192.168.225.1 dev usb0 proto dhcp src 192.168.225.57 metric 203 mtu 1360 
10.0.100.0/24 dev eth0 proto dhcp scope link src 10.0.100.250 metric 202 
192.168.225.0/24 dev usb0 proto dhcp scope link src 192.168.225.57 metric 203 mtu 1360
```

The `metric` (which is `202` for `eth0`, and `203` for `usb0`) indicates to Linux that the lowest interface (`eth0`) should be used for any routing to IPs within its scope—which if you run `route -n`, you'll find the `netmask` (labeled `Genmask` here) is `0.0.0.0` for both interfaces.

```
pi@turing-node-1:~ $ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.100.1      0.0.0.0         UG    202    0        0 eth0
0.0.0.0         192.168.225.1   0.0.0.0         UG    203    0        0 usb0
10.0.100.0      0.0.0.0         255.255.255.0   U     202    0        0 eth0
192.168.225.0   0.0.0.0         255.255.255.0   U     203    0        0 usb0
```

So in practice, this means that any traffic out to the Internet will be routed through `eth0`. And traditionally, you could use the `ifmetric` command to change the metric on the fly:

```
$ sudo apt install ifmetric
$ sudo ifmetric eth0 220
```

But that doesn't work:

```
pi@turing-node-1:~ $ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.100.1      0.0.0.0         UG    202    0        0 eth0
0.0.0.0         192.168.225.1   0.0.0.0         UG    203    0        0 usb0
10.0.100.0      0.0.0.0         255.255.255.0   U     202    0        0 eth0
192.168.225.0   0.0.0.0         255.255.255.0   U     203    0        0 usb0
```

## dhcpcd priorities

Because the system uses dhcpcd, you have to override metrics in dhcpcd's config, then restart the service.

The rules for dhcpcd metric calculations seems to be:

  - Metrics are used to prefer an interface over another one, lowest wins.
  - dhcpcd will supply a default metric of 200 + if_nametoindex(3).
  - An extra 100 will be added for wireless interfaces.

Therefore, it seems that since `usb0` comes after `eth0` alphabetically, it loses and becomes the `203` to `eth0`'s `202`.

Basically:

```
# Edit dhcpcd's configuration.
$ sudo nano /etc/dhcpcd.conf

# Add the following to the end of the file and save it:
interface usb0
metric 0

# Restart dhcpcd.
$ sudo systemctl restart dhcpcd

# Et voila!
$ ip route list
default via 192.168.225.1 dev usb0 proto dhcp src 192.168.225.57 mtu 1360 
default via 10.0.100.1 dev eth0 proto dhcp src 10.0.100.250 metric 202 
10.0.100.0/24 dev eth0 proto dhcp scope link src 10.0.100.250 metric 202 
192.168.225.0/24 dev usb0 proto dhcp scope link src 192.168.225.57 mtu 1360
```

At this point, I can guarantee my Internet packets will go out through the `usb0` interface, so I can run my benchmarks through it—even without disconnecting or otherwise disabling `eth0`. This is very helpful when benchmarking a Pi headless without serial console access!

Reverting the changes to `dhcpcd` and restarting the service got the order back to how it was before.

Thanks especially to NetBeez's post [Linux for Network Engineers: How to Set Route Priorities](https://netbeez.net/blog/linux-set-route-priorities/), which, after many hours of DuckDuckGo'ing got me to this answer.
