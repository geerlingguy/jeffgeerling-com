---
nid: 3156
title: "My Backup Plan"
slug: "my-backup-plan"
date: 2021-12-08T15:08:24+00:00
drupal:
  nid: 3156
  path: /blog/2021/my-backup-plan
  body_format: markdown
  redirects: []
tags:
  - backup
  - disaster avoidance
  - nas
  - open source
  - raspberry pi
---

I've had a number of people ask about my backup strategy—how I ensure the 6 TB of video project files and a few TB of other files stays intact over time.

{{< figure src="./3-2-1-backup-slide-resized.jpeg" alt="3-2-1 backup plan" width="700" height="394" class="insert-image" >}}

Over the past year, since I got more serious about my growing YouTube channel's success, I decided to document and automate as much of my backups as possible, following a **3-2-1 backup plan**:

  - 3 Copies of all my data
  - 2 Copies on different storage media
  - 1 Offsite copy

The culmination of that work is this GitHub repository: [my-backup-plan](https://github.com/geerlingguy/my-backup-plan).

The first thing I needed to do was take a data inventory—all the files important enough for me to worry about fell into six main categories:

{{< figure src="./data-inventory-resized.jpeg" alt="6 backup categories" width="700" height="394" class="insert-image" >}}

For each category, I have at least three copies, on different storage media (locally on my main Mac and NAS, or on my primary and secondary NAS in the case of video files), and one copy in the cloud (some data uses cloud storage, other data is `rclone`d to AWS Glacier (using an S3 Glacier-backed bucket).

{{< figure src="./backup-pi.jpg" alt="Backup Raspberry Pi in rack" width="600" height="330" class="insert-image" >}}

I manage `rclone` and automated [`gickup` runs for Git backups](https://github.com/cooperspencer/gickup)) on my 'backup Pi', which is managed via Ansible and has a few simple scripts and cron jobs to upload to AWS direct from my NAS.

This allows me to have full disaster recovery quickly if just my main computer or primary NAS dies, and a little slower if my house burns down or someone nukes St. Louis (hopefully neither of those things happens...).

Many people have asked about Glacier pricing, also about how expensive retrieval is. Well, for storage, it costs about $4/month for more than 6 TB of data. Retrieval is more expensive, and there was one instance where I needed to spend about $5 to pull down 30 GB of data as quickly as possible... but that's not the main annoyance with Glacier.

The main problem is it took over 12 hours—since I'm using Deep Archive—to even _start_ that data transfer, since the data had to be brought back from cold storage.

But it's a price I'm willing to pay, to save a ton on the monthly costs, and to have a dead-simple remote storage solution ([`rclone`](https://rclone.org) is seriously awesome, and simple).

Anyways, for even more detail about my backups, check out my latest video on YouTube:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/S0KZ5iXTkzg" frameborder='0' allowfullscreen></iframe></div>
</div>

And be sure to check out my GitHub repository, which goes into a LOT more detail: [my-backup-plan](https://github.com/geerlingguy/my-backup-plan).
