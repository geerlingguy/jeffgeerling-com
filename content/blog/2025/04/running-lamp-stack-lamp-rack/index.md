---
nid: 3456
title: "Running the LAMP Stack in a Lamp Rack"
slug: "running-lamp-stack-lamp-rack"
date: 2025-04-01T14:01:08+00:00
drupal:
  nid: 3456
  path: /blog/2025/running-lamp-stack-lamp-rack
  body_format: markdown
  redirects:
    - /blog/2025/lamp-rack-ai-cluster-your-living-room
    - /blog/2025/i-run-lamp-stack-on-my-lamp-rack
    - /blog/2025/i-run-lamp-stack-my-lamp-rack
aliases:
  - /blog/2025/lamp-rack-ai-cluster-your-living-room
  - /blog/2025/i-run-lamp-stack-on-my-lamp-rack
  - /blog/2025/i-run-lamp-stack-my-lamp-rack
tags:
  - april fools
  - cluster
  - kubernetes
  - lamp
  - mini rack
  - rack
  - raspberry pi
  - video
  - youtube
---

{{< figure src="./lamp-rack-geerling.jpeg" alt="Lamp rack for a LAMP stack - Jeff Geerling mini rack" width="700" height="394" class="insert-image" >}}

I typically don't do anything for April Fool's Day, but this year I thought I'd unite a bit of a meme in the homelab community with something I wanted to make a video on anyway: a _lamp rack_.

What's a lamp rack? Well, you're looking at one! It's a floor lamp with an integrated [mini rack](https://mini-rack.jeffgeerling.com)!

I didn't want to make a video about a floor lamp, but more on the fact you don't _need_ fancy racks or any new hardware at _all_ to start a homelab.

If you have an old laptop, throw Proxmox on it, start tinkering, and boom! There's a homelab! And if you buy the same [Sunmory Floor Lamp](https://amzn.to/42s0gOA) that I did, you could set the laptop on one of the shelves, plug it in, and consolidate your lamp and your homelab, for the most effective use of a tight space!

But I went a little extra. I installed 4U of rack rails for an almost-perfect mini-rack in the same tier as the built-in PDU (well... the Sunmory has hot glued ungrounded power outlets, but _technically_ it's still a PDU!), placed a UPS on the bottom, and had the _lamborghini_ of lamp racks.

Then, I did the only logical thing: I installed the LAMP stack in my Lamp Rack.

I also made a full video on the rack, you can view it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/CE6MTBxDSpE" frameborder='0' allowfullscreen></iframe></div>
</div>

But I'll go through a few more details here, in case you're crazy enough to replicate my build.

## The LAMP Cluster - Hardware

{{< figure src="./lamp-rack-hardware.jpeg" alt="Lamp rack hardware setup" width="700" height="394" class="insert-image" >}}

To mount everything, I bought a [$14 set of 4U rack ears](https://amzn.to/4hUUd9O), and screwed them into the pillars of the top shelf of the lamp, facing each other.

Then, I put in a 1U blanking panel on the bottom (for future expansion possibilities!), a 2U [LabStack mini](https://github.com/JaredC01/LabStack) cluster (I'll get to the contents next), and a [Netgear GS305P PoE+ Switch](https://amzn.to/4iS8Ig4).

I printed a [2U LabStack mini 4-module bracket](https://github.com/JaredC01/LabStack/blob/main/LabStack%20Mini/STLs/2U%20Mini%204x%20LabStack%20Module%20M3x4x5mm%20Heatset%20Bracket.stl) and installed four modules, from left to right:

  1. A [Blank module](https://github.com/JaredC01/LabStack/blob/main/Modules/STLs/Module%20Blank.stl)
  2. A [JetKVM + 2x Keystone Jack module](https://github.com/JaredC01/LabStack/blob/main/Modules/STLs/Module%201x%20JetKVM%202x%20Keystone.stl)
  3. A [Raspberry Pi + HAT module](https://github.com/JaredC01/LabStack/blob/main/Modules/STLs/Module%201x%20Pi%20with%20HAT.stl)
  4. A [2x Raspberry Pi module](https://github.com/JaredC01/LabStack/blob/main/Modules/STLs/Module%202x%20Pi.stl)

{{< figure src="./lamp-rack-hat.jpeg" alt="Lamp rack - Pi HAT NVMe HackerGadgets PoE" width="700" height="394" class="insert-image" >}}

Each of the three Raspberry Pi 5s has a [HackerGadgets PoE+ NVMe HAT](https://hackergadgets.com/products/nvme-and-poe-hat-for-raspberry-pi-5), with 2242-sized NVMe SSDs installed running Pi OS.

These are currently the most compact and robust HATs that combine PoE and an M.2 NVMe slot, and they _just barely_ fit within the LabStack mini system if you stack two on top of each other. I could go more dense, cramming in _eight_ Pi 5s this way, but (a) I don't have that many Pi 5s, and (b) I only have a 5-port network switch to use for this build!

{{< figure src="./lamp-rack-ups.jpeg" alt="Lamp rack UPS on bottom" width="700" height="394" class="insert-image" >}}

Powering the whole setup, I installed an [APC 425VA Battery Backup](https://amzn.to/3G08wN0) in the base of the floor lamp, both to provide stability, and to provide a much nicer power source than the hot-glued-together mess that is the included AC/USB power strip!

## The LAMP Cluster - Software

{{< figure src="./lamp-rack-jetkvm-k9s.jpeg" alt="Lamp Rack JetKVM K9s CLI" width="700" height="394" class="insert-image" >}}

For software, I ran my [Raspberry Pi Cluster playbook](https://github.com/geerlingguy/pi-cluster), which uses Ansible to configure all the nodes into a K3s Kubernetes cluster.

That playbook also installs Drupal, and I installed the [K9s CLI](https://k9scli.io) on the main Pi so I could inspect all the running resources (see above picture).

I'm not running through the _entire_ setup process here, because I've done similar setups in the past, and I'd rather you go into the deeper dives I've posted before:

  - [Kubernetes 101](https://kube101.jeffgeerling.com) - a free series on Kubernetes
  - [Ansible for DevOps](https://www.ansiblefordevops.com) - a book on Ansible (I also published [Ansible 101](/blog/2020/ansible-101-jeff-geerling-youtube-streaming-series) in 2020).

## Conclusion

{{< figure src="./lamp-rack-labstack.jpeg" alt="Lamp Rack Labstack" width="700" height="394" class="insert-image" >}}

My main goal was to make a fun custom mini rack build in a literal lamp, after [@gwzcomps jokingly suggested it on Twitter](https://x.com/gwzcomps/status/1894862941574385669).

But through the process of building it, I realized how easy it is to turn many everyday objects into homelab artifacts. And in this case, despite the wobbly construction and inadequate PSU, it turns out bringing your homelab into your living space has never been easier.

{{< figure src="./lamp-rack-black-and-white.jpeg" alt="LAMP Rack Black and White vintage mini rack" width="700" height="467" class="insert-image" >}}
