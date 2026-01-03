---
nid: 3143
title: "HTGWA: Create an NFS share in Linux on a Raspberry Pi"
slug: "htgwa-create-nfs-share-linux-on-raspberry-pi"
date: 2021-11-12T04:17:34+00:00
drupal:
  nid: 3143
  path: /blog/2021/htgwa-create-nfs-share-linux-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - file
  - files
  - htgwa
  - linux
  - networking
  - nfs
  - sharing
  - tutorial
---

This is a simple guide, part of a series I'll call 'How-To Guide Without Ads'. In it, I'm going to document how I create an NFS share in Linux on a Raspberry Pi.

## Install NFS

```
$ sudo apt-get install -y nfs-kernel-server
```

## Create a shared directory

```
$ sudo mkdir /mnt/mydrive/shared
$ sudo chmod -R 777 /mnt/mydrive/shared
```

I won't deal with permissions in this post; [read this post](https://serverfault.com/a/241272) for more suggestions.

## Configure NFS to share that directory

Edit the NFS exports file with `sudo nano /etc/exports`, and add the following:

```
/mnt/mydrive/shared *(rw,all_squash,insecure,async,no_subtree_check,anonuid=1000,anongid=1000)
```

## Update the NFS active exports

```
sudo exportfs -ra
```

## Connect to the share

From another computer, access: `nfs://[hostname-or-ip-of-pi]/mnt/mydrive/shared`
