---
nid: 3134
title: "Kubesail's PiBox mini 2 - 16 TB of SSD storage on a Pi"
slug: "kubesails-pibox-mini-2-16-tb-ssd-storage-on-pi"
date: 2021-10-25T14:05:45+00:00
drupal:
  nid: 3134
  path: /blog/2021/kubesails-pibox-mini-2-16-tb-ssd-storage-on-pi
  body_format: markdown
  redirects:
    - /blog/2021/kubesails-pibox-mini-2-offers-16-tb-ssd-storage-on-pi
aliases:
  - /blog/2021/kubesails-pibox-mini-2-offers-16-tb-ssd-storage-on-pi
tags:
  - cm4
  - compute module
  - kubernetes
  - kubesail
  - microk8s
  - nas
  - pibox
  - raspberry pi
  - ssd
  - youtube
---

{{< figure src="./pibox-mini-2-front-side-exposed.jpeg" alt="Kubesail Raspberry PiBox mini 2 front side exposed" width="600" height="400" class="insert-image" >}}

Many months ago, when I was first [testing different SATA cards](https://pipci.jeffgeerling.com/#sata-cards-and-storage) on the Raspberry Pi Compute Module 4, I started [hearing from GitHub user PastuDan](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/64) about his experiences testing a few different SATA interface chips on the CM4.

As it turns out, he was working on the design for the [PiBox mini 2](https://pibox.io), a small two-drive NAS unit powered by a Compute Module 4 with 2 native SATA ports (providing data and power), 1 Gbps Ethernet, HDMI, USB 2, and a front-panel LCD for information display.

## The Hardware

The PiBox mini 2 is powered by the Compute Module 4 on this interesting carrier board:

{{< figure src="./pibox-mini-carrier.jpeg" alt="PiBox mini carrier board with Raspberry Pi Compute Module 4" width="600" height="400" class="insert-image" >}}

Notice the edge connector? It's a PCI Express x4 plug—but this board doesn't plug into a PCI Express slot—rather, it uses that hardware connector to plug into a special backplane, which holds the SATA chip, 2 SATA connectors for hard drives or SSDs, and has a status display connector and activity LEDs.

The backplane fits nicely into their 3D case design:

{{< figure src="./pibox-mini-inside-no-drives-backplane.jpeg" alt="PiBox mini SATA backplane" width="600" height="400" class="insert-image" >}}

A metal enclosure will be provided at a later time, but the 3D enclosure is already pretty nice—much more compact than anything else I've used with similar specs.

{{< figure src="./pibox-mini-rear-io.jpeg" alt="PiBox mini 2 rear IO" width="600" height="400" class="insert-image" >}}

All the IO is on the rear, and it's nothing amazing, but having a full size HDMI port means this NAS could pull double-duty and run media software like Plex and be connected directly to a TV.

{{< figure src="./pibox-kubesail-ui.jpg" alt="PiBox Kubesail Kubernetes management web UI" width="594" height="334" class="insert-image" >}}

## Kubesail and MicroK8s

The box came pre-installed with MicroK8s and the Kubesail Agent, which ties the little Kubernetes endpoint into [Kubesail](https://kubesail.com/), a semi-managed Kubernetes platform that allows you to bring your own cluster (you don't need PiBox to use it!) and proxies traffic to the cluster to make self-hosting much easier.

I didn't spend a whole lot of time testing Kubesail itself, but I did like the overall approach, and especially liked the documentation and ability to dive straight into my cluster's YAML templates when needed, all through a web UI.

As stated previously, there's no need to run Kubernetes or Kubesail at all—if you just want to run [OpenMediaVault](https://www.openmediavault.org) or some other OS install, that's easy to do, and Kubesail even publishes a [guide for customizing other OSes](https://docs.kubesail.com/guides/pibox/os/) for the PiBox, so things like the front-panel LCD and PWM fan control still work.

## Disk performance

I ran some baseline performance tests, though the ASM1061 SATA-III controller used is similar in performance to the other boards I've tested with the Compute Module 4—meaning the maximum throughput is limited by the ~3.6 Gbps real-world throughput of the Pi's PCIe Gen 2.0 x1 lane.

Using `mdadm` (`sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/sda /dev/sdb`), I created a RAID 1 array with two [Samsung 8TB 870 QVO SSDs](https://amzn.to/3j4Ph6K) (don't ask how much these things cost...). Then I used `fio` to test:

### 1M Sequential Read

```
fio --name TEST --eta-newline=5s --filename=fio-tempfile.dat --rw=read --size=500m --io_size=10g --blocksize=1024k --ioengine=libaio --fsync=10000 --iodepth=32 --direct=1 --numjobs=1 --runtime=60 --group_reporting
```

{{< figure src="./1m-sequential-read-perf-pibox-resized.png" alt="1M Sequential Read PiBox mini fio performance benchmark" width="700" height="394" class="insert-image" >}}

### 1M Sequential Write

```
fio --name TEST --eta-newline=5s --filename=fio-tempfile.dat --rw=write --size=500m --io_size=10g --blocksize=1024k --ioengine=libaio --fsync=10000 --iodepth=32 --direct=1 --numjobs=1 --runtime=60 --group_reporting
```

{{< figure src="./1m-sequential-write-perf-pibox-resized.png" alt="1M Sequential Write PiBox mini fio performance benchmark" width="700" height="394" class="insert-image" >}}

### 4K Random Read

```
fio --name TEST --eta-newline=5s --filename=fio-tempfile.dat --rw=randread --size=500m --io_size=10g --blocksize=4k --ioengine=libaio --fsync=1 --iodepth=1 --direct=1 --numjobs=1 --runtime=60 --group_reporting
```

{{< figure src="./4k-random-read-perf-pibox-resized.png" alt="4K Random Read PiBox mini fio performance benchmark" width="700" height="394" class="insert-image" >}}

The numbers aren't ground-breaking, but they're in line with what I've gotten on other Pi storage tests when using native SATA-III drives directly on the Pi's PCIe bus (instead of through USB-to-SATA adapters, as is popular to do in older Pi NAS products like the [Argon Eon](https://www.kickstarter.com/projects/argonforty/argon-eon-4-bay-network-storage-powered-by-raspberry-pi-4).

And _for a Pi_, 7000 IOPS is nothing to be scoffed at. The best I've gotten with microSD cards or eMMC storage is around 2-3000 IOPS.

Running things Kubernetes' storage or log output on SSDs also saves the microSD card or built-in eMMC storage from many small writes, greatly extending their life.

Unfortunately, right _now_ you can't fully boot the Pi off native SATA storage. Hopefully that will change someday!

## Teardown and Review

I compiled all the details about my teardown and review of the PiBox mini 2 in this YouTube video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/YtdVotS3018" frameborder='0' allowfullscreen></iframe></div>
</div>

If you're interested in getting one, they're currently running a [Kickstarter for the PiBox mini 2](https://www.kickstarter.com/projects/pastudan/pibox-a-modular-raspberry-pi-storage-server), and Kubesail is planning on making some other versions, too, eventually including a 5-bay 3.5" NAS!

The PiBox mini 2 isn't the _only_ full-featured NAS product I'm testing right now, either—I've just started testing a new NAS build using Radxa's Taco! Make sure you [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) for the latest news.
