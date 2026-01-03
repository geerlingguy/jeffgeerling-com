---
nid: 3196
title: "Installing the Asahi Linux Alpha on my M1 Mac mini"
slug: "installing-asahi-linux-alpha-on-my-m1-mac-mini"
date: 2022-03-25T21:15:22+00:00
drupal:
  nid: 3196
  path: /blog/2022/installing-asahi-linux-alpha-on-my-m1-mac-mini
  body_format: markdown
  redirects: []
tags:
  - apple
  - asahi
  - linux
  - m1
  - mac
  - mac mini
  - open source
  - tutorial
---

After [upgrading my main workstation to a Mac Studio](/blog/2022/mac-studio-4x-more-efficient-my-new-amd-pc), I decided to break tradition.

Usually, I sell off my old workstation to offset the cost of the new one. But just last week, [Asahi Linux announced their first alpha release](https://asahilinux.org/2022/03/asahi-linux-alpha-release/).

{{< figure src="./asahi-linux-macbook-pro.png" alt="Asahi Linux MacBook Pro" width="500" height="290" class="insert-image" >}}

If you haven't heard of Asahi, it's a Linux distribution based on Arch Linux that aims to bring a polished Linux experience on Apple Silicon Macs (all the current M1 Macs, and any new Apple Silicon Macs that come in the future).

{{< figure src="./m1-mac-mini-front.jpeg" alt="M1 Mac mini front" width="500" height="281" class="insert-image" >}}

So instead of selling my M1 Mac mini, I wanted to see if I could repurpose it: I run a lot of services on Raspberry Pis—which have ARM64-architecture CPUs just like the M1 Mac mini—and it would be interesting to see if I could run services on the M1 mini—way faster than on the Pis.

Full support of all M1 features (most notably, the GPU) isn't complete, and it's nowhere near a final release, but I thought it would be fun to try it out, and see how well Linux (at least one distro) runs on Apple's ARM64 architecture.

## Installing Asahi

The instructions in the blog post give a `curl | sudo bash` style instruction to run `curl https://alx.sh | sh`. Since I'm okay with completely nuking this Mac back to factory defaults if things go wrong, I'll take them up on the offer.

At some point the Asahi community might also offer an App download or USB-stick-based installer too, but right now the easiest way to get all the partitions in order is to run a script from their site. The `alx.sh` URL just loads in an installer from `https://cdn.asahilinux.org/installer` and some data files to kick off the installation process.

{{< figure src="./installer-asahi-partitions.jpg" alt="Asahi Installer - Partitions" width="700" height="477" class="insert-image" >}}

The prompts are fairly straightforward, though you should probably not attempt installing Asahi (it's alpha after all!) unless you're familiar with at least the basics of the command line and Linux. Some of the options, if chosen without understanding, could lead to a bit of a degraded experience if you choose poorly, so don't just dive in on your main or only Mac if you rely on it day to day! If you want to get more comfortable with the process, I highly recommend reading Asahi's [Introduction to Apple Silicon](https://github.com/AsahiLinux/docs/wiki/Introduction-to-Apple-Silicon).

I was a little surprised how long the partitioning took (pictured above)—almost an hour on my M1 mini! At the end, this warning appeared:

{{< figure src="./asahi-installer-warning.jpeg" alt="Asahi Linux installer reboot warning" width="700" height="394" class="insert-image" >}}

It's important to wait for the Mac to shut down completely. Then you need to hold down the power button continuously until it boots into recoveryOS, a special lightweight system that comes on M1 Macs that allows you to choose boot OSes other than the primary macOS installation:

{{< figure src="./asahi-linux-recoveryos-boot-select-macos.jpg" alt="Boot select OS Image in recoveryOS" width="700" height="403" class="insert-image" >}}

After selecting Asahi Linux, you're prompted for your macOS administrator password, then the Asahi installer completes its installation process from recoveryOS. As part of this process, you have to enter your administrator password _again_ to set the computer's boot policy to 'permissive' mode, to allow non-macOS operating systems to run.

Once _that's_ done, you're greeted with a very cheerful Asahi Linux setup wizard:

{{< figure src="./asahi-linux-setup-wizard-all-done.jpeg" alt="Asahi Linux setup wizard" width="700" height="467" class="insert-image" >}}

## Trying Docker

The first thing I wanted to test was how much better (or worse) the Docker experience was running under Asahi Linux (which is based on Arch, btw) than running under Docker Desktop for Mac on macOS.

I glanced at the graphical software center but didn't see a Docker install option in there, so I went to the command line.

Knowing this was based on Arch Linux, I tried installing with `pacman`:

```
$ sudo pacman -S docker
```

But this resulted in an error; it said the dependent package `containerd-1.6.1-1-aarch64.pkg.tar.xz` couldn't be found. After asking about it in the #asahi IRC channel on OFTC, I found out `pacman`, like Debian's `apt`, needs its caches managed—I had assumed it was more like `dnf` on Fedora/RedHat, where it would update its repo caches on every command. Oops.

I don't normally use Arch, btw.

So I ran `pacman -Syu` to update everything, and then Docker installed correctly. But it wouldn't run—I was seeing in the logs messages like `"devmapper not configured"` and `error initializing graphdriver: loopback attach failed`. It turns out a reboot was all that I needed.

I added my user to the `docker` group, logged out and logged back in, then I could run any Docker images just like I would on my Mac. I installed Docker Compose with `pip3 install docker-compose`, and added `export PATH="$HOME/.local/bin:$PATH"` to my `.zshrc` file so `docker-compose` would work.

I tested my [Raspberry Pi Linux kernel cross-compile process](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile), which runs in Docker, and the results were very encouraging:

{{< figure src="./Asahi-vs-macOS-Linux-Cross-Compile.jpg" alt="Linux cross-compile in Docker on macOS" width="700" height="394" class="insert-image" >}}

And I also ran two processes involved in setting up my [jeffgeerling-com website codebase](https://github.com/geerlingguy/jeffgeerling-com) locally, `composer install`ing all my site's dependencies over a shared volume, and installing Drupal, and both are markedly faster under Docker in Asahi:

{{< figure src="./Asahi-vs-macOS-Drupal-in-Docker.jpg" alt="Asahi vs macOS Docker Drupal PHP benchmarking" width="700" height="394" class="insert-image" >}}

But Docker for Mac runs in a lightweight virtualized environment, and even with the new VirtioFS file sharing method, it's known to be slower than a native Linux environment.

So you can't draw the conclusion that 'Asahi Linux is faster than macOS' just based on Docker results. Michael Larabel over on Phoronix did a [_lot_ more benchmarking](https://www.phoronix.com/scan.php?page=article&amp;item=apple-m1-linux-perf), and found that there are a number of natively-compiled apps that _do_ run faster on Asahi, on the exact same hardware.

But because Asahi doesn't have some optimizations, like boosting the efficiency CPU core clocks, nor does it have drivers for the GPU (so no Vulkan, Metal, or OpenGL support), there's still a ways to go before it can reach full parity for benchmarks. But progress is being made, and rapidly!

## Networking

For example, not many people seem to have been testing M1 Mac minis with 10G networking built in; I did test that, and the result was disappointing:

{{< figure src="./networking-1.5gbps-10g-pcie-x1.jpeg" alt="Networking iperf3 benchmark 1.5G PCIe x1 link Asahi Linux" width="700" height="394" class="insert-image" >}}

As it turns out, a PCIe flag was setting the link speed for the network adapter to x1 instead of x4, which severely crippled the NIC, limiting it to about 1.5 Gbps over a 2.5, 5, or 10Gbase-T connection.

Within minutes of my mention in IRC, jannau validated the problem on a Mac Studio (oh, did I mention Asahi can run on the Mac Studio already?), and [submitted a PR with the fix](https://github.com/AsahiLinux/m1n1/pull/178).

I also tested WiFi, and it seemed to work without issue, giving me 700-800 Mbps over a WiFi 6 connection, though some users report it needing to be toggled on and off from time to time to work.

## Other software

I also tried installing a ton of other software on Asahi. One of the same problems plagues Asahi currently that I've run into on the Raspberry Pi—most software that has a Linux download either:

  - Only supports AMD64/Intel
  - Only supports Ubuntu/Debian 'officially' (and sometimes Fedora/RedHat)

For the former, it can be impossible to get the software to compile on an ARM64 system like the M1. In the past, the excuse for not supporting the ARM64 platform has been a lack of server-grade hardware.

"Why support ARM64," project leaders ask, "if the best hardware people can run our software on is a Raspberry Pi with 8 GB of RAM?"

More and more, that's a bad take: above the hobbyist-tier Raspberry Pi, Ampere and AWS have already paved a path towards data-center-scale ARM, Solid-Run has shown some (pricey, but adequate) mid-range servers and workstation boards, and now Apple has put out not just the base-level M1, but the midrange-workstation-grade M1 Max and Ultra chips, which can battle with higher-end Intel and AMD chips (though not yet on the highest performance servers).

In the next 5 years, as used prices for the original M1 Mac mini go sub-$500... this machine would be _perfect_ to run as a silent, efficient homelab server. Heck, it could run a lot of SMB applications via Asahi or any other compatible Linux distribution.

Enough of my rant, though: I ran a number of applications, from LibreOffice to K3s, and anything that had an ARM64 build worked flawlessly—and incredibly fast, especially since my only other ARM experience comes from running apps on a Pi 400, Pi 4, or CM4, which are far slower than Apple's M1.

## Conclusion

I have a full guide and demo of Asahi Linux in my latest YouTube video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/L2p_fGuldt0" frameborder='0' allowfullscreen></iframe></div>
</div>

But my main takeaway is this:

All the software vendors and communities who've dismissed the ARM64 builds when Raspberry Pi users ask: it's time to reconsider. ARM64 isn't just for hobby boards and mobile devices anymore—AWS, Apple, and even Nvidia are proving it's even _better_ for many use cases on both the desktop and in hyperscale environments.
