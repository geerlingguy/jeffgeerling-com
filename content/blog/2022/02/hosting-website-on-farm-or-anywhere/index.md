---
nid: 3178
title: "Hosting this website on a farm - or anywhere"
slug: "hosting-website-on-farm-or-anywhere"
date: 2022-02-09T15:02:14+00:00
drupal:
  nid: 3178
  path: /blog/2022/hosting-website-on-farm-or-anywhere
  body_format: markdown
  redirects:
    - /blog/2022/hosting-website-on-farm
    - /blog/2022/hosting-website-on-farm—or-anywhere
aliases:
  - /blog/2022/hosting-website-on-farm
  - /blog/2022/hosting-website-on-farm—or-anywhere
tags:
  - 4g
  - battery
  - cluster
  - ecoflow
  - k3s
  - kubernetes
  - lte
  - raspberry pi
  - solar
  - sponsored
  - turing pi
---

> **tl;dr**: This website is currently being hosted off-grid, on a cluster of Raspberry Pis, via 4G LTE—or at some points through the same tunnel via WiFi if signal strength gets too low. [Here's the GitHub repo for the project](https://github.com/geerlingguy/turing-pi-2-cluster).

> **Note**: The website was down for a few hours this morning, as shortly after this post I started getting a 40-50 Mbps flood of POST requests (over 6 million in a 30 minute time frame)... and yeah, no way the little Pi cluster could handle that. Thanks, Internet. It's back up through Cloudflare now, and I'll post more on this 'fun' experience later.

A couple weeks ago, after months of preparation, I took my 4-node Turing Pi 2 cluster ([see my earlier review](/blog/2021/turing-pi-2-4-raspberry-pi-nodes-on-mini-itx-board)) to my cousin's farm, and ran this website (JeffGeerling.com) on it, live on the Internet—completely disconnected from grid power or hard-wired Internet.

{{< figure src="./turing-pi-2-cluster-at-farm-solar-panels-battery.jpeg" alt="Turing Pi 2 cluster with EcoFlow Battery and Solar Panels at my cousin's farm" width="700" height="453" class="insert-image" >}}

_Right now_ this website is running on the same cluster, using the same configuration, but at my house (I couldn't leave the cluster at my cousin's farm indefinitely—the cows would get it!)

But what's special about _my_ cluster? Well, my goal at the outset was to build an **energy efficient Pi cluster** that I could take _literally_ anywhere (within reason), and continue hosting this website.

I automated the entire cluster setup in my [Turing Pi 2 Cluster repository](https://github.com/geerlingguy/turing-pi-2-cluster) on GitHub.

I can't relate the _whole_ story in this post—for that, watch the video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/OLRldZjty_s" frameborder="0" allowfullscreen=""></iframe></div>
</div>

<p style="text-align: center;"><em>Full Disclosure: The YouTube video I made for this project was sponsored by EcoFlow.</em></p>

In this post, I'll give a quick rundown of the major problems I encountered, and my solutions.

## Networking

{{< figure src="./quarter-resistor-turing-pi-2.jpeg" alt="Turing Pi 2 SMD Resistor on Quarter" width="700" height="467" class="insert-image" >}}

**4G Connectivity**: After finding a hardware bug with the prototype board (caused by the resistor pictured above), I used a Quectel EC25-A 4G modem and a [SixFab SIM card](https://sixfab.com/sim/) to get connected to the Internet.

I wrote up an entire post about the process: [Using 4G LTE wireless modems on a Raspberry Pi](https://www.jeffgeerling.com/blog/2022/using-4g-lte-wireless-modems-on-raspberry-pi).

I could get connected to the Internet, but in doing so, I encountered another new problem:

**CG-NAT**: Because I couldn't get a publicly-addressable IPv4 address (and IPv6 support across different carriers isn't reliable), I had to set up an SSH tunnel between the cluster and a VPS under my control, which I configured as a reverse proxy (using Nginx).

{{< figure src="./Reverse-Proxy-SSH-Tunnel.png" alt="Reverse proxy SSH tunnel" width="700" height="400" class="insert-image" >}}

I wrote up a post on that, too: [SSH and HTTP to a Raspberry Pi behind CG-NAT](https://www.jeffgeerling.com/blog/2022/ssh-and-http-raspberry-pi-behind-cg-nat).

All these things are great for a _single_ Raspberry Pi, but my Turing Pi 2 cluster is made up of _four_ Pis, all together in a Kubernetes cluster.

Not wanting to compromise on the flexibility a 4-node cluster gives me, I decided to set up the first node (the one with the 4G modem) as a lightweight router.

This was doubly necessary as Kubernetes was _very_ unhappy when the control plane and all the nodes would change IP addresses as I swapped the cluster between various networks (LAN at my house, LAN at a friend's house, a separate WiFi network, a 4G hotspot, etc.).

Because getting Kubernetes running on top of OpenWRT [is a pain](https://5pi.de/2019/05/10/k8s-on-openwrt/), I instead [set up `dnsmasq` and `iptables` to bridge the first node's connection](https://github.com/geerlingguy/turing-pi-2-cluster/blob/master/tasks/networking/router.yml) to the rest of the cluster through the Turing Pi 2's built-in network, on a subnet separate from my LAN.

Finally, I needed a way to switch between Ethernet, WiFi, and USB (4G) interfaces, so I learned how to do that using network route priorities (`metric`s) in `dhcpcd` in Debian... and of _course_ I wrote up that process: [Network interface routing priority on a Raspberry Pi](https://www.jeffgeerling.com/blog/2022/network-interface-routing-priority-on-raspberry-pi).

There are a few other tidbits I did in the Turing Pi 2 Cluster Ansible playbook, but those were the major challenges.

## Storage

Everyone knows how unreliable microSD cards are for longevity, especially under random-write-heavy workloads (even [the best ones](/blog/2019/raspberry-pi-microsd-card-performance-comparison-2019)).

And seeing as I'd be monitoring the cluster with Prometheus and Grafana, plus running my site's MariaDB database on the Pis, storing everything on microSD (or even eMMC) storage was a non-starter.

{{< figure src="./crucial-mx500-ssds-in-turing-pi-2-cluster-zfs-raid.jpg" alt="Crucial MX500 SSDs in RAIDZ1 mirror" width="700" height="394" class="insert-image" >}}

Luckily, the Turing Pi 2 includes two SATA III connections directly attached to node 3. So I set up a RAIDZ1 ZFS mirror zpool on two [Crucial MX500 SSDs](https://amzn.to/3uBHvbh) and configured an NFS share—and [I wrote this up in my ZFS for Raspberry Pi post](/blog/2021/htgwa-create-zfs-raidz1-zpool-on-raspberry-pi).

In Kubernetes, I set up the `nfs-client` provisioner so I could have Drupal and MariaDB store their persistent data on NFS volumes.

The storage situation isn't perfect: now nodes 1 (for network routing) and 3 (for storage) are both critical to the functioning of the cluster, and are both Single Points of Failure (SPOF).

Ideally I'd have fast storage on each node, and I'd create a distributed filesystem with Rook/Ceph or GlusterFS... but I can't have _everything_ on a $75 Raspberry Pi (I'm running the 8GB Lite versions with WiFi + Bluetooth).

## Power

As I mentioned earlier, one of my main goals was to create a completely portable system that could be run anywhere—grid connection or not. And for power, I'm plugging the cluster into an [EcoFlow Delta Max](https://ecoflow.com/collections/delta-series?aff=212) portable power station, with 1,612 Watt-hours of battery capacity.

I contacted EcoFlow on a whim after seeing Matthias Wandel try [overloading one of their 'Pro' units last year](https://www.youtube.com/watch?v=CPv4IUSyIPk), and they were happy to assist on this project—even throwing in sponsorship so I could devote more time and budget to making the video at the top of the post!

They sent the Delta Max—which I've tested as being able to run the cluster (at about 17W average consumption) for up to 42 hours—along with two [400W solar panels](https://ecoflow.com/products/400w-solar-panel?aff=212).

{{< figure src="./ecoflow-400w-solar-panel-setup.jpg" alt="EcoFlow 400W solar panels - farm setup" width="700" height="394" class="insert-image" >}}

These panels are pretty massive (each one weighs 12.5 kg or about 30 lbs), but they live up to the marketing—I was able to pull down 460W using just one in full sunlight, and was hitting 700-800W power input on the Delta Max when I had them connected in series. That's plenty of juice to keep the battery topped off so I can power the cluster _indefinitely_.

It was a little awkward to carry everything while plugged in, but I was able to transfer the battery and cluster from my car to the solar panels (to top off their charge), then inside, and back to my car—and the cluster remained online the entire time.

## Physical Protection

Finally, to make sure I could transport the Turing Pi 2 cluster safely, I [racked it up in a 2U Mini ITX server enclosure](https://www.youtube.com/watch?v=RijuRF0ITdE) made by MyElectronics.nl, then mounted that inside [this SKB 2U soft rack case](https://amzn.to/3J51O4O).

And here it sits—this picture was taken before I turned in for the night on February 8, a few hours before this blog post is set to go live on the 9th:

{{< figure src="./skb-2u-soft-case-with-turing-pi-2-cluster-inside-running.jpeg" alt="SKB 2U soft case with Turing Pi 2 cluster running inside" width="700" height="427" class="insert-image" >}}

## Conclusion

There are some things I still want to improve. As noted in [this issue](https://github.com/geerlingguy/turing-pi-2-cluster/issues/14), I'd love to build a more automated 'switch between VPS and remote cluster' setup—though the hardest part of that is pulling down or pushing up the database, and rsync'ing the 1.2 GB or so of files I have on this website.

Even with a stable 4G connection, I can sometimes only get a few megabits of upload bandwidth, and that means to do the 'failover' correctly, I could either miss some comments or other site data during the long process, or I'd have to have my site offline for a long (to me) period of time, in the range of _minutes_. (Not fun for someone who prides himself on having 99.998% of uptime since 2009!)

As it is, I'm happy with how this all turned out. Things have been running quite stable:

{{< figure src="./node-exporter-grafana-turing-pi-2-prometheus.png" alt="Node Exporter view in Grafana of Turing Pi 2 cluster networking and disk IO" width="700" height="394" class="insert-image" >}}

I have, multiple times, hard-power-cycled the cluster, booted it with either 4G or WiFi routing, and it _always_ connects back through it's tunnel to my VPS, and always resumes serving web traffic.

There was one time CoreDNS stopped working—[of _course_ it's DNS](https://redshirtjeff.com/listing/it-was-dns-shirt?product=211)—but a quick reboot fixed that, and it's been surprisingly reliable since.

Of course, if this post gets any traction on HN, Reddit, or elsewhere... that could change 😅.
