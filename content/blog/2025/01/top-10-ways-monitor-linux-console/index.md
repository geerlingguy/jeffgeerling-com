---
nid: 3350
title: "Top 10 ways to monitor Linux in the console"
slug: "top-10-ways-monitor-linux-console"
date: 2025-01-15T17:36:34+00:00
drupal:
  nid: 3350
  path: /blog/2025/top-10-ways-monitor-linux-console
  body_format: markdown
  redirects:
    - /blog/2024/top-10-ways-monitor-linux-console
aliases:
  - /blog/2024/top-10-ways-monitor-linux-console
tags:
  - iotop
  - linux
  - monitoring
  - performance
  - raspberry pi
  - terminal
  - top
---

{{< figure src="./btop-bokeh.jpg" alt="btop colorful Linux graph" width="700" height="auto" class="insert-image" >}}

`top` (pictured _below_... above is [btop](#btop)) is the first utility everyone recommends to monitor Linux (or any form of UNIX, including macOS) resource usage. It's efficient, available almost everywhere... but it's also a bit basic. It shows essential metrics, but looks like it's from the 80s. There are ways to brighten it up, like highlighting active processes or changing color schemes, but it's not the only game in town!

{{< figure src="./top.jpg" alt="Top running in Linux" width="700" height="auto" class="insert-image" >}}

Nowadays, there are a _lot_ of modern monitoring tools—and some not so modern, but immensely useful—to choose from. This blog post will run through some of the ones I rely on most often. Let me know in the comments if you use any others I didn't cover!

## Contents

  - [s-tui](#s-tui)
  - [htop](#htop)
  - [atop](#atop)
  - [iftop](#iftop)
  - [iotop](#iotop)
  - [nvtop](#nvtop)
  - [asitop](#asitop)
  - [btop](#btop)
  - [perf](#perf)
  - [wavemon](#wavemon)

If you'd like to see all these tools in action, check out the video that goes along with this blog post, embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/4isEhE2rvmA" frameborder='0' allowfullscreen></iframe></div>
</div>

## s-tui<a name="s-tui"></a>

{{< figure src="./s-tui.jpg" alt="s-tui running a stress test in Linux" width="700" height="auto" class="insert-image" >}}

```
# Install on Debian/Ubuntu Linux
apt install -y stress-ng s-tui
```

If I want to quickly observe the system's CPU frequency and temperatures while running a stress benchmark, this is by far the best way.

I originally discovered this tool through ServeTheHome—Patrick uses it and displays it on the giant screen behind him to monitor core to core stability when running a system under load.

It has two basic modes, 'Monitor' and 'Stress', and while running in Stress mode, it will use `stress` or `stress-ng` to stress all CPU cores (you can configure `stress` options within `s-tui`'s configuration).

I've used it on Linux and macOS, and it seems to pick up the right temperature sensors on most hardware, even exotic systems like the AmpereOne!

## htop<a name="htop"></a>

{{< figure src="./htop.jpg" alt="htop running in Linux for process and CPU monitoring" width="700" height="auto" class="insert-image" >}}

```
sudo apt install htop
```

htop is often installed by default (e.g. on Raspberry Pi OS), and is like top, but focuses visually on CPU metrics more than memory. It provides more visual indication of system load through bar graphs, and it's usually a tossup whether I choose `htop` or `top`.

## atop<a name="atop"></a>

> **WARNING (2025-03)**: [Some versions of Atop are vulnerable to local attacks which could lock up the machine](https://openwall.com/lists/oss-security/2025/03/29/1).

{{< figure src="./atop.jpg" alt="atop running in Linux for resource monitoring" width="700" height="auto" class="insert-image" >}}

```
sudo apt install atop
```

`atop` breaks out a lot of critical performance metrics into a dizzying array of metrics, with a process list below. There are two features I like about `atop` that draws me to it instead of other tools when I'm debugging hardware bottlenecks:

First, it uses color sparingly to indicate resources reaching saturation (e.g. 90% of disk, memory, or CPU usage turns that metric red).

Second, it breaks out IRQ consumption, network packets in and out, and some other metrics that are either hidden or buried in other tools. This tool has been especially helpful when troubleshooting bottlenecks like network file copy slowdowns, which sometimes are affected by CPU core affinity, PCIe bottlenecks, or disk IO (or a combination of all!).

## iftop<a name="iftop"></a>

{{< figure src="./iftop.jpg" alt="iftop running in Linux for network interface monitoring eth0" width="700" height="auto" class="insert-image" >}}

```
sudo apt install iftop
```

If I'm just focused on bandwidth monitoring—seeing how much data is going through a network interface, there's no simpler tool than `iftop`. It shows total bandwidth over the interface, along with a running total of download and upload size. Then it lists every connection with traffic up and down, with a simple bar graph display for each.

## iotop<a name="iotop"></a>

{{< figure src="./iotop.jpg" alt="iotop running in Linux for disk IO monitoring" width="700" height="auto" class="insert-image" >}}

```
sudo apt install iotop
```

What `iftop` is for network bandwidth, `iotop` is for disk bandwidth.

The nice party trick is it also breaks out the disk IO _by process_, so if you are experiencing slow disk access, or want to see what processes are hogging a drive, this is the quickest way to get at that info.

If you want to get even fancier, `sysdig` (`sudo apt install -y sysdig`) comes with a console UI `csysdig` which lets you dig directly into processes by volume of data written or ops! Very handy.

## nvtop<a name="nvtop"></a>

{{< figure src="./nvtop.jpg" alt="nvtop running in Linux for GPU monitoring an AMD Graphics Card" width="700" height="auto" class="insert-image" >}}

```
sudo apt install nvtop
```

[`nvtop`](https://github.com/Syllo/nvtop) is a lightweight task viewer for AMD, Intel, Nvidia, and Apple GPUs. Some tools like `btop` (shown later) include very simple GPU metrics (sometimes...), but `nvtop` gives you all the hardware details, like power consumption, fan speed, memory consumption, and a process breakdown.

There are tools like `radeontop` and [`amdgpu_top`](https://github.com/Umio-Yasuno/amdgpu_top) for AMD, or [`nvitop`](https://github.com/XuehaiPan/nvitop) for Nvidia... but `nvtop` is almost universally available, and works on the largest variety of GPUs. It's nice to know one tool for all, and even nicer when it's an `apt install` away. Or `brew install nvtop` on macOS!

## asitop<a name="asitop"></a>

{{< figure src="./asitop.jpg" alt="asitop running on macOS for CPU and GPU and power monitoring" width="700" height="auto" class="insert-image" >}}

```
pip3 install asitop
```

I try not to get too platform-specific with my tooling, but sometimes when I'm on a Mac, I don't have access to the full gauntlet of process monitoring tools I get on Linux.

Lucky for me, there's `asitop`, which is a handy visual tool to monitor CPU, GPU, power, and clock speeds. It even breaks down visuals based on E and P cores!

## btop<a name="btop"></a>

{{< figure src="./btop.jpg" alt="btop running on Linux for resource monitoring" width="700" height="auto" class="insert-image" >}}

```
sudo apt install btop
```

Now we get to it—the _Lamborghini_ of `top`s. Not only does it have full color, mouse support, and a sensible video-game-like menu system (no arcane hidden features here!), it makes you look like you're hacking away on TV set.

The visuals aren't all eye-candy, either. Color schemes and almost infinite settings and layouts mean you can set it up for precisely the metrics you want to monitor, usually with just a few keystrokes.

It's worth spending the time to learn some of `btop`'s options. `btop` is usually the first tool I install when getting a feel for a new computer or SBC. Sometimes the colors can get a bit wacky, especially over SSH sessions, but a quick trip to the menus (`o`) and setting `Truecolor` to `False` fixes that right up.

This is by far the tool I get the most comments about when it appears in one of my YouTube videos. The visuals are not only pretty, but functional.

## perf<a name="perf"></a>

{{< figure src="./perf.jpg" alt="perf running on Linux for performance monitoring" width="700" height="auto" class="insert-image" >}}

```
sudo apt install linux-perf
```

And after the beauty of `btop`, we have to go in the complete opposite direction. `perf` isn't a `top` at all! Well, then, why is it in the list?

Because usually once you monitor a system with a lightweight tool like `btop` or `atop`, you need to actually _figure out the bottleneck_. And `perf` has deep kernel integration to pull out performance data you didn't even know existed!

I can't even scratch the surface of what it can do—I'll let the guy who I've learned the like 0.2% of `perf`'s features from describe it so much better: [Brendan Gregg's `perf` Examples](https://www.brendangregg.com/perf.html). He even writes a book on Linux performance monitoring!

And _yes_, that's the same Brendan Gregg famous for [Shouting in the Datacenter](https://www.youtube.com/watch?v=tDacjrSCeq4).

## wavemon<a name="wavemon"></a>

{{< figure src="./wavemon.jpg" alt="Wavemon running in Linux for WiFi metrics monitoring and signal strength" width="700" height="auto" class="insert-image" >}}

```
sudo apt install wavemon
```

Since we're off on a tangent of non-`top` monitoring tools, I figured I'd throw an honorable mention out to `wavemon`.

Before I discovered this tool, I would use `watch -n 1` with `nmcli` or `iwconfig`... but that was not ideal, and a tool like `iwconfig` occupies some weird head space where I can never remember the exact name, because there's also `ipconfig` or `ifconfig` or `ip` or whatever other networking tools that have overloaded those registers in my brain.

But now I can see precisely which direction to orient my external wifi antenna, or find a way to eke out an extra 100 Mbps from an otherwise-stable connection!

That rounds out my list of the top 10 ways to monitor Linux... but as I mentioned in the `perf` section, this is barely scratching the surface. Seriously, go read through Brendan Gregg's [Linux Performance](https://www.brendangregg.com/linuxperf.html) page if you want to go much, _much_ deeper.
