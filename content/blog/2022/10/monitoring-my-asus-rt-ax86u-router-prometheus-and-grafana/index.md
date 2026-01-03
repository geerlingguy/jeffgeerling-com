---
nid: 3242
title: "Monitoring my ASUS RT-AX86U Router with Prometheus and Grafana"
slug: "monitoring-my-asus-rt-ax86u-router-prometheus-and-grafana"
date: 2022-10-06T17:33:23+00:00
drupal:
  nid: 3242
  path: /blog/2022/monitoring-my-asus-rt-ax86u-router-prometheus-and-grafana
  body_format: markdown
  redirects: []
tags:
  - asus
  - asuswrt
  - grafana
  - monitoring
  - networking
  - prometheus
  - router
---

I've been running my [Internet Monitoring Pi](https://github.com/geerlingguy/internet-pi) for a year or so, and it's nice to collect data on Internet performance from _inside_ my network.

But my router—currently an ASUS RT-AX86U—also tracks its own metrics for inbound and outbound traffic, among other things:

{{< figure src="./asuswrt-system-status-dashboard.jpg" alt="ASUSWRT-Merlin System Status Dashboard metrics" width="500" height="340" class="insert-image" >}}

Sometimes having the raw data from the router that's on the edge of the network can tell a different story than measuring things _behind_ the router. So I want to grab this data and put it into Prometheus.

With the stock ASUS firmware, this isn't really possible. But after reading a blog post about someone else [monitoring an RT-AC86U with Prometheus](https://ashwinikd.github.io/monitoring/router/prometheus/2020/07/30/router-series-1.html), I decided to give it a shot on mine. I already run the [ASUSWRT-Merlin firmware](https://www.asuswrt-merlin.net) on my router, since I like having SSH access to it and can install some network utilities on it [via a USB stick](https://github.com/RMerl/asuswrt-merlin.ng/wiki/Disk-formatting).

## Installing `node_exporter` on the router

The first step is to get [node-exporter](https://github.com/prometheus/node_exporter) running on the router, to expose data that my Prometheus instance can scrape.

And to do that, I needed to grab the URL of the latest `arm64` Linux release on the [node-exporter Releases](https://github.com/prometheus/node_exporter/releases) page.

I have an USB flash drive plugged in, and it's mounted at `/mnt/SANDISK`. I created a node_exporter directory, and downloaded the binary inside:

```
mkdir -p /mnt/SANDISK/node_exporter
cd /mnt/SANDISK/node_exporter
wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-arm64.tar.gz
tar xzf node_exporter-1.3.1.linux-arm64.tar.gz
mv node_exporter-1.3.1.linux-arm64/node_exporter ./node_exporter
rm -rf node_exporter-1.3.1.linux-arm64*
```

To make sure it's working, I ran:

```
admin@RT-AX86U-FAC0:/tmp/mnt/SANDISK/node_exporter# ./node_exporter --version
node_exporter, version 1.3.1 (branch: HEAD, revision: a2321e7b940ddcff26873612bccdf7cd4c42b6b6)
  build user:       root@243aafa5525c
  build date:       20211205-11:10:22
  go version:       go1.17.3
  platform:         linux/arm64
```

> **NOTE**: I initially tried node_exporter version `1.4.0`, but was having trouble getting all the network statistics. I opened this issue to investigate: [netdev collector failing with 'couldn't get netstats: incorrect size' since 1.4.0](https://github.com/prometheus/node_exporter/issues/2502). Versions 1.3.1 and all earlier versions I tried down to 1.0.0 worked fine.

To make sure it starts running and will always run after a reboot, I added this shell script, based on [this other blog post](https://blog.sim22.co.uk/monitor-asus-dsl-ac68u-with-prometheus-and-grafana-dashboard-2/), and saved it as `/mnt/SANDISK/node_exporter/node_exporter_start.sh`:

```
#!/bin/bash

pidof node_exporter

if [[ $? -ne 0 ]] ; then
    /mnt/SANDISK/node_exporter/node_exporter --web.listen-address=":9100" >>/mnt/SANDISK/node_exporter/node_exporter.log 2>&1 &
fi
```

I gave it execute permissions with `chmod +x node_exporter_start.sh`.

You can use `cru a` to create a cron job, but with the ASUS firmware, the system boots into a RAM-only filesystem, meaning anything you change that's not inside a special persistent area will get wiped on reboot.

So I needed to add a 'user script' in the persistent [JFFS filesystem](https://github.com/RMerl/asuswrt-merlin.ng/wiki/JFFS). First, make sure JFFS scripts are enabled; to do that, in the router's UI, visit Administration > System, and make sure you have the 'Yes' option selected for "Enable JFFS custom scripts and configs".

Then SSH into the router and place a file named `/jffs/scripts/init-start`, with the contents:

```
#!/bin/sh
cru a node-exporter '* * * * * sh /tmp/mnt/SANDISK/node_exporter/node_exporter_start.sh'
```

Make that script executable (`chmod +x /jffs/scripts/init-start`), then to start node_exporter in the background, either manually run the `cru` command above, or reboot the router and it should be started. You can confirm it's running by visiting your router's IP at port 9100 in the browser, or run `ps w | grep node_exporter` via SSH and make sure it's running.

## Configuring Prometheus to scrape the data

Now that node_exporter is running, it's time to set Prometheus to scrape data from the router. Inside the `scrape_configs` in your `prometheus.yml` file, add the following job:

```
scrape_configs:
  [...]
  - job_name: 'node'
    scrape_interval: 5s
    static_configs:
      - targets: ['10.0.100.1:9100']
```

If you already have a job named `node`, you could just add the router's IP/port to the list of `targets`. That's what I'm doing to get node information from all my monitored nodes in my homelab, in my [internet-pi](https://github.com/geerlingguy/internet-pi) playbook.

Restart Prometheus, and if you check in Prometheus' UI, you should see the node target as 'up' after a few seconds—assuming Prometheus can see your router and node_exporter is running:

{{< figure src="./prometheus-node-exporter-up.png" alt="Prometheus node exporter up and running" width="700" height="127" class="insert-image" >}}

The final step is adding a dashboard in Grafana to view the statistics in a clean way, over time. And for that, I'm relying on the [Node Exporter Full](https://grafana.com/grafana/dashboards/1860-node-exporter-full/) dashboard—for some reason I couldn't just download the JSON using the button on Grafana's website, I had to go to the source repo and download the raw source for [node-exporter-full.json](https://github.com/rfmoz/grafana-dashboards/blob/master/prometheus/node-exporter-full.json).

After importing that into Grafana, I could see all the metrics for my router:

{{< figure src="./grafana-node-exporter-full-router-monitoring.jpg" alt="Grafana dashboard for node exporter from ASUS router" width="700" height="433" class="insert-image" >}}

All those little spikes you see are the traffic flows in and out of various ports on the router during every-half-hour speedtests I use to monitor my available Internet bandwidth over time.

I'll likely work on a custom dashboard that gives me only the metrics I'm interested in at a glance, like in/out Internet bandwidth over time (just through the `eth0` WAN connection), device CPU and memory usage, and individual graphs for each of the other interface types (e.g. 2.4 GHz and 5 GHz WiFi bands).

The ASUS RT-AX86U is actually quite a capable router, as far as up-to-1 Gbps connections are concerned. If I ever have a better ISP and can go beyond a gigabit down, or beyond 35 Mbps up, I'll probably build out a beefier router.
