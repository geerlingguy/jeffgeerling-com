---
nid: 3310
title: "Testing 10 GbE throughput on Windows - iperf3 is outdated"
slug: "testing-10-gbe-throughput-on-windows-iperf3-outdated"
date: 2023-09-05T22:48:36+00:00
drupal:
  nid: 3310
  path: /blog/2023/testing-10-gbe-throughput-on-windows-iperf3-outdated
  body_format: markdown
  redirects: []
tags:
  - 10 gbps
  - iperf3
  - networking
  - windows
---

{{< figure src="./Screenshot%202023-09-05%20at%206.08.34%20PM.png" alt="iperf3 only showing 4.5 gbps in Windows" width="700" height="363" class="insert-image" >}}

Recently I [upgraded my AMD-based PC](https://www.youtube.com/watch?v=hsp-CimwNK4&lc=Ugz8uVo1ZhvsEWSQ-sV4AaABAg.9mUXVfBaPNz9mU_fihrDvn) on a livestream, and I installed an [Innodisk EGPL-T101 10 Gbps M.2 NIC](https://amzn.to/3PrewAR) ([link to Innodisk product page](https://www.innodisk.com/en/products/embedded-peripheral/communication/egpl-t101)).

Under Linux, I could get through 9.4 Gbps using `iperf3` between the PC and my Mac Studio. But under Windows, I could only get up to about 4.5 Gbps (tested around [1h 27m into the stream](https://youtu.be/hsp-CimwNK4?t=5231))!

I had downloaded the latest version of [iperf3 for Windows](https://iperf.fr/iperf-download.php#windows) from the iperf.fr website, which was listed as version `3.1.3` from June of _2016_! I thought that was pretty old, and indeed, looking at all the downloads on that page... they are all _very_ old. What gives?

 Well, even though that site seems to be at the top of all search results for iperf3 downloads, it doesn't have the latest version of iperf3. On Linux and macOS, I just `apt|brew|dnf install iperf3` and I have a fairly up-to-date version.

On Windows, it looks like [`choco` (Chocolatey)](https://community.chocolatey.org/packages/iperf3) pulls iperf3 binaries for Windows from [`files.budman.pw`](https://files.budman.pw), and there is also a GitHub project maintaining releases of iperf3 for windows, [`ar51an/iperf3-win-builds`](https://github.com/ar51an/iperf3-win-builds/releases).

I have downloaded and run iperf3 successfully from both sources (getting 9.40 Gbps on that PC), and it seems like both builds come out of the kind efforts of Neowin users:

  - BudMan [has been providing builds since 2014](https://www.neowin.net/forum/topic/1234695-iperf-314-windows-build/)
  - CryptAnalyst is maintaining `ar51an/iperf3-win-builds` and is [active in BudMan's thread](https://www.neowin.net/forum/topic/1234695-iperf-314-windows-build/page/5/#comment-598795462) as well

So I'm not sure if one is recommended over the other, really—especially for my needs, where I'm doing local bandwidth testing between two machines and don't need SSL support or multithreading. The `files.budman.pw` site is linked from the [`obtaining.rst` doc in the `esnet/iperf` project](https://github.com/esnet/iperf/blob/master/docs/obtaining.rst), FWIW.
