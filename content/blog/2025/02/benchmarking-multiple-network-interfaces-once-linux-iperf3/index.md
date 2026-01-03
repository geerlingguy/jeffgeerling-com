---
nid: 3446
title: "Benchmarking multiple network interfaces at once in Linux with iperf3"
slug: "benchmarking-multiple-network-interfaces-once-linux-iperf3"
date: 2025-02-23T23:43:04+00:00
drupal:
  nid: 3446
  path: /blog/2025/benchmarking-multiple-network-interfaces-once-linux-iperf3
  body_format: markdown
  redirects: []
tags:
  - 2.5 gbps
  - bandwidth
  - benchmarking
  - hat
  - iperf3
  - linux
  - networking
  - raspberry pi
---

Recently, I've been working on a Pi router build with multiple 2.5 Gbps Ethernet ports using [Radxa's Dual 2.5G Router HAT](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/647).

I wanted a simple way to check on total network TCP throughput using _both_ interfaces (or really, as many interfaces as possible) to multiple computers on my network, and I noticed `iperf3`'s `--bind` option (like `--bind [ip address of interface]`) was not splitting the traffic on both interfaces—it would just route all traffic through one!

Luckily, I found the issue [Failing to bind to interface when multiple interfaces are present](https://github.com/esnet/iperf/issues/1572), and in it, @bmah888 mentioned the `--bind-dev` option, which is new as of iperf 3.10+.

Using that option (like `--bind-dev [interface name]`), you can force an instance of iperf3 to bind to one particular device. For example, assuming I have two servers on my network running `iperf3 -s`, I can run the following on the Pi to saturate both connections as much as the Pi will allow:

```
iperf3 --no-delay -c 10.0.2.5 --bind-dev eth1 --interval 0 --parallel 1 --time 30 &
iperf3 --no-delay -c 10.0.2.6 --bind-dev eth2 --interval 0 --parallel 1 --time 30 &
```

I've encountered some weird issues with multiple interfaces on iperf before, too—wrangling multiple connections in Linux (or any OS) can be tricky, since the OS usually has routing optimizations in place that interfere with your intentions! (See my [Network interface routing priority on a Raspberry Pi](/blog/2022/network-interface-routing-priority-on-raspberry-pi) blog post about that.
