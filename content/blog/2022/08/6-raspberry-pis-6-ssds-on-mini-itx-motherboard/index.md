---
nid: 3229
title: "6 Raspberry Pis, 6 SSDs on a Mini ITX Motherboard"
slug: "6-raspberry-pis-6-ssds-on-mini-itx-motherboard"
date: 2022-08-17T14:00:50+00:00
drupal:
  nid: 3229
  path: /blog/2022/6-raspberry-pis-6-ssds-on-mini-itx-motherboard
  body_format: markdown
  redirects: []
tags:
  - ceph
  - cluster
  - deskpi
  - k3s
  - kubernetes
  - raspberry pi
  - reviews
  - storage
  - super6c
  - video
  - youtube
---

A few months ago someone told me about a new Raspberry Pi Compute Module 4 cluster board, the [DeskPi Super6c](https://deskpi.com/collections/deskpi-super6c/products/deskpi-super6c-raspberry-pi-cm4-cluster-mini-itx-board-6-rpi-cm4-supported).

{{< figure src="./deskpi-super6c-running.jpg" alt="DeskPi Super6c Running on Desk" width="700" height="479" class="insert-image" >}}

You may have heard of another Pi CM4 cluster board, the [Turing Pi 2](/blog/2021/turing-pi-2-4-raspberry-pi-nodes-on-mini-itx-board), but that board is not yet shipping. It had [a _very_ successful Kickstarter campaign](https://www.kickstarter.com/projects/turingpi/turing-pi-cluster-board), but production has been delayed due to parts shortages.

The Turing Pi 2 offers some unique features, like Jetson Nano compatibility, remote management, a fully managed Ethernet switch (capable of VLAN support and link aggregation). But if you just want to slap a bunch of Raspberry Pis inside a tiny form factor, the Super6c is about as trim as you can get—and it's available today!

{{< figure src="./deskpi-super6c-top.jpeg" alt="DeskPi Super6c Top" width="700" height="524" class="insert-image" >}}

On the top, there are slots for up to _six_ Compute Module 4s, and each slot exposes IO pins (though not the full Pi GPIO), a Micro USB port for flashing eMMC CM4 modules, and some status LEDs.

{{< figure src="./deskpi-super6c-bottom.jpeg" alt="DeskPi Super6c bottom" width="700" height="453" class="insert-image" >}}

On the bottom, there are _six_ NVMe SSD slots (M.2 2280 M-key), and six microSD card slots, so you can boot Lite CM4 modules (those without built-in eMMC).

{{< figure src="./deskpi-super6c-io.jpeg" alt="DeskPi Super6c IO ports" width="700" height="467" class="insert-image" >}}

On the IO side, there are a bunch of ports tied to CM4 slot 1—dual HDMI, two USB 2.0 (plus an internal USB 2.0 header), and micro USB, so you can manage the entire cluster self-contained. You can plug a keyboard, monitor, and mouse into the first node, and use it to set up everything else if you want. (That was one complaint I had with the Turing Pi 2—there was no option of managing the cluster without using another computer.)

There's also two power inputs: a barrel jack accepting 19-24V DC (the board comes with a 100W power adapter), and a 4-pin ATX 12V power header if you want to use an internal PSU.

Finally, there are six little activity LEDs sticking out the back, one for each Pi. Watching the cluster as Ceph was running made me think of [WOPR, from the movie War Games](https://www.youtube.com/watch?v=_aUHQKneAdw)—just on a much smaller scale!

## Ceph storage cluster

{{< figure src="./deskpi-super6c-storage-nvme-kioxia-xg6.jpg" alt="DeskPi Super6c bottom showing 6 NVMe SSDs - KIOXIA XG6" width="700" height="394" class="insert-image" >}}

Since this board exposes so much storage directly on the underside, I decided to install [Ceph](https://ceph.com/en/) on it using cephadm [following this guide](https://ceph.com/en/news/blog/2022/install-ceph-in-a-raspberrypi-4-cluster/).

Ceph is an open-source storage cluster solution that manages object/block/file-level storage across multiple computers and drives, similar to RAID on one computer—except you can aggregate multiple storage devices across multiple computers.

I had to do a couple extra steps during the install since I decided to run Raspberry Pi OS (a Debian derivative) instead of running Fedora like the guide suggested:

  1. I had to enable the backports repo by adding the line `deb http://deb.debian.org/debian unstable main contrib non-free` to my `/etc/apt/sources.list` file and then running `sudo apt update`.
  2. I added a file at `/etc/apt/preferences.d/99pin-unstable` with the lines:

         Package: *
         Pin: release a=stable
         Pin-Priority: 900
         
         Package: *
         Pin: release a=unstable
         Pin-Priority: 10

  3. After that, I could install cephadm with `sudo apt install -y cephadm`

Once `cephadm` was installed, I could set up the Ceph cluster using the following command (inserting the first node's IP address):

```
# cephadm bootstrap --mon-ip 10.0.100.149
```

This bootstraps a Ceph cluster, but you still need to add individual hosts to the cluster, and I elected to do that via Ceph's web UI. The `bootstrap` command outputs an admin login and the dashboard URL, so I went there, logged in, updated my password, and started adding hosts:

{{< figure src="./ceph-storage-hosts-super6c.jpg" alt="Super6c Ceph Storage Hosts dashboard 3.3 TiB" width="700" height="394" class="insert-image" >}}

I built [this Ansible playbook](https://github.com/geerlingguy/deskpi-super6c-cluster) to help with the setup, since there are a couple other steps that have to be run on _all_ the nodes, like copying the Ceph pubkey to each node's root user `authorized_keys` file, and installing Podman and LVM2 on each node.

But once that was done, and all my hosts were added, I was able to set up a storage pool on the cluster, using the 3.3 TiB of built-in NVMe storage (distributed across five nodes). I used Ceph's built-in benchmarking tool `rados` to run some sequential write and read tests:

{{< figure src="./ceph-benchmarks-super6c-rados.jpg" alt="Ceph Super6c rados benchmarks for Pi storage cluster" width="700" height="394" class="insert-image" >}}

I was able to get 70-80 MB/sec write speeds on the cluster, and 110 MB/sec read speeds. Not too bad, considering the entire thing's running over a 1 Gbps network. You can't really increase throughput due to the Pi's IO limitations—maybe in the next generation of Pi, we can get faster networking!

Throw in other features like encryption, though, and the speeds are sure to fall off a bit more. I also wanted to test an NFS mount across the Pis from my Mac, but I [kept getting errors when I tried adding the NFS service](https://github.com/geerlingguy/deskpi-super6c-cluster/issues/1) to the cluster.

If you want to stick with an ARM build, a dedicated Ceph storage appliance like the [Mars 400](https://store.avantek.co.uk/mars-400-ceph-storage-appliance.html) is still going to obliterate a hobbyist board like this, in terms of network bandwidth and IOPS—despite its slower CPUs. Of course, that performance comes at a cost; the Mars 400 is a $12,000 server!

## Video

I produced a full video of the cluster build, with more information about the hardware and how I set it up, and that's embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/ecdm3oA-QdQ" frameborder="0" allowfullscreen=""></iframe></div>
</div>

For this project, I published the Ansible automation playbooks I set up in the [DeskPi Super6c Cluster](https://github.com/geerlingguy/deskpi-super6c-cluster) repo on GitHub, and I've also uploaded the [custom IO shield](https://www.thingiverse.com/thing:5465766) I designed to Thingiverse.

## Conclusion

This board seems ideal for experimentation—assuming [you can find a bunch of CM4s for list price](https://rpilocator.com). Especially if you're dipping your toes into the waters of K3s, Kubernetes, or Ceph, this board lets you throw together up to six physical nodes, without having to manage six power adapters, six network cables, and a separate network switch.

Many people will say "just buy one PC and run VMs on it!", but to that, I say "phooey." Dealing with physical nodes is a great way to learn more about networking, distributed storage, and multi-node application performance—much more so than running VMs inside a faster single node!

{{< figure src="./kill-a-watt-super6c-idle-6-pis.jpg" alt="Kill-A-Watt showing 17.9W idle power consumption for Super6c Pi cluster board" width="700" height="394" class="insert-image" >}}

In terms of _production_ usage, the Super6c could be useful in some edge computing scenarios, especially considering it uses just 17W of power for 6 nodes at idle, or about 24W maximum, but honestly, using other more powerful mini/SFF PCs would be more cost effective right now.

You can buy the [DeskPi Super6c on Amazon](https://amzn.to/3psoOmE) or [on DeskPi's website](https://deskpi.com/collections/deskpi-super6c/products/deskpi-super6c-raspberry-pi-cm4-cluster-mini-itx-board-6-rpi-cm4-supported) for $199.99.
