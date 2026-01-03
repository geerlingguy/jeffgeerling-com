---
nid: 3267
title: "Using PiBenchmarks.com for SBC disk performance testing"
slug: "using-pibenchmarkscom-sbc-disk-performance-testing"
date: 2023-01-25T20:23:08+00:00
drupal:
  nid: 3267
  path: /blog/2023/using-pibenchmarkscom-sbc-disk-performance-testing
  body_format: markdown
  redirects: []
tags:
  - benchmarking
  - benchmarks
  - microsd
  - nvme
  - raspberry pi
  - sbc
  - ssd
---

For many years, I've maintained some scripts to do basic disk benchmarking for SBCs, to test 1M and 4K sequential and random access speeds, since those are the two most relevant tests for the Linux workloads I run on my Pis.

I've been using [this script](https://github.com/geerlingguy/pi-cluster/blob/master/benchmarks/disk-benchmark.sh) for years, and it uses `fio` and `iozone` to get the metrics I need.

And from time to time, I would test a [number of microSD cards on the Pi](/blog/2019/raspberry-pi-microsd-card-performance-comparison-2019), or run tests on NVMe SSDs on the Pi, Rock 5 model B, or other SBCs. But my results were usually geared towards a single blog post or a video project.

In 2021 [James Chambers set up PiBenchmarks](https://jamesachambers.com/raspberry-pi-storage-benchmarks-2019-benchmarking-script/) to move to a more community-driven testing dataset.

You can run the following command on your SBC to test the boot storage and upload results directly to [PiBenchmarks.com](https://pibenchmarks.com):

```
sudo curl https://raw.githubusercontent.com/TheRemote/PiBenchmarks/master/Storage.sh | sudo bash
```

Or, if you want to test a device like an SSD or NVMe drive (or even a hard disk!) connected via SAS, SATA, NVMe, or whatever interface, run:

```
curl -o Storage.sh https://raw.githubusercontent.com/TheRemote/PiBenchmarks/master/Storage.sh
chmod +x Storage.sh
sudo ./Storage.sh /path/to/mount/point
```

(For benchmarking, I usually [format large devices in Linux with `parted`](/blog/2021/htgwa-partition-format-and-mount-large-disk-linux-parted) and don't run the benchmarks on a boot volume unless absolutely necessary.)

Looking through the results on [PiBenchmarks.com](https://pibenchmarks.com), you can sort by fastest by SBC, fastest by device type, and drill down to averages and individual results. I have been running some benchmarks and uploading the results under my username [geerlingguy](https://pibenchmarks.com/search/geerlingguy/), though there's no user authentication mechanism, so it seems the results operate by trust.

{{< figure src="./pibenchmarks-geerlingguy.png" alt="PiBenchmarks.com - geerlingguy results" width="700" height="394" class="insert-image" >}}

And sometimes I see a crazy result where the average is like 25,000 but there's one result at like 90,000 running on a beefy X86 desktop machine! So the results need to be interpreted correctly and reproduced for maximum accuracy, but I do love this tool.
