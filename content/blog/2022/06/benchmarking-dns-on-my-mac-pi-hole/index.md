---
nid: 3214
title: "Benchmarking DNS on my Mac with Pi-Hole"
slug: "benchmarking-dns-on-my-mac-pi-hole"
date: 2022-06-10T19:18:50+00:00
drupal:
  nid: 3214
  path: /blog/2022/benchmarking-dns-on-my-mac-pi-hole
  body_format: markdown
  redirects: []
tags:
  - benchmarking
  - dns
  - internet
  - networking
  - pi-hole
  - tcp/ip
---

After watching Level1Techs' [THE FORBIDDEN ROUTER II - DIAL-UP BY DAWN](https://www.youtube.com/watch?v=MBY_QNN3owc) video, I wanted to do some DNS benchmarking on my local network.

Since I run [Pi-hole](https://pi-hole.net) locally, and rely on it for local DNS resolution, I wanted to have a baseline so I could compare performance over time.

In the video, Wendell mentioned the use of Gibson's Windows-only [DNS Benchmark](https://www.grc.com/dns/benchmark.htm) tool. But that's Windows-only. Or maybe Linux under WINE, but definitely not a native / open source tool that's easily used across different platforms.

I looked around and settled on [bulldohzer](https://github.com/commonshost/bulldohzer)—for now, at least—as it's easy to install anywhere Node.js runs. I have Node.js installed via Homebrew on my Mac, so I just ran:

```
npm install --location=global bulldohzer
```

Then I could run a benchmark against Google and my own local DNS resolver (Pi-Hole):

```
$ bulldohzer --dns 10.0.100.3 google

Resolvers

█ 10.0.100.3 DNS
  10.0.100.3
   1.5 ms  1.5 ms  1.9 ms
       ██████

█ Google DNS
  8.8.8.8
  13.7 ms 14.3 ms 14.5 ms
  ██████████████████████████████████████████████████


Response Times

p5    ▅      1.5 ms 🥇 10.0.100.3 DNS

p50  ▁█      1.5 ms 🥇 10.0.100.3 DNS

p95  ▁█      1.9 ms 🥇 10.0.100.3 DNS
```

The documentation site seems to be offline ([https://help.commons.host/bulldohzer/](https://help.commons.host/bulldohzer/)), so right now you have to use [this cached version from the Wayback Machine](https://web.archive.org/web/20210515162023/https://help.commons.host/bulldohzer/cli/#examples).

I also saw many mentions of `namebench` (like [this blog post](https://www.xmodulo.com/how-to-test-dns-server-speed-on-linux.html)), but it seems like development on it stopped around 2016 or so, and there aren't any versions that run on modern Python (3.x) or macOS 64-bit...
