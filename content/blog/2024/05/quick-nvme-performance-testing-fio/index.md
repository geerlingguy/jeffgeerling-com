---
nid: 3375
title: "Quick NVMe performance testing with fio"
slug: "quick-nvme-performance-testing-fio"
date: 2024-05-13T20:55:45+00:00
drupal:
  nid: 3375
  path: /blog/2024/quick-nvme-performance-testing-fio
  body_format: markdown
  redirects: []
tags:
  - benchmarking
  - benchmarks
  - fio
  - nvme
  - pcie
  - testing
---

I've recently been debugging some NVMe / PCIe bus errors on a Raspberry Pi, and I wanted a quick way to test NVMe devices without needing to create a filesystem and use a tool like `iozone`. I don't care about benchmarks, I just want to quickly push the drive and read and write some data to it.

`fio` is the tool for the job, and after a quick install `sudo apt install -y fio`, I create a configuration file named `nvme-read.fio`:

```
[global]
name=nvme-seq-read
time_based
ramp_time=5
runtime=30
readwrite=read
bs=256k
ioengine=libaio
direct=1
numjobs=1
iodepth=32
group_reporting=1
[nvme0]
filename=/dev/nvme0n1
```

Then run it with:

```
sudo fio nvme-read.fio
```

Easy way to put some stress on the drive, and test your PCIe setup and the drive itself.
