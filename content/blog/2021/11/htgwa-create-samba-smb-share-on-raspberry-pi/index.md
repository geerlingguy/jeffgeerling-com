---
nid: 3142
title: "HTGWA: Create a Samba (SMB) share on a Raspberry Pi"
slug: "htgwa-create-samba-smb-share-on-raspberry-pi"
date: 2021-11-12T03:48:17+00:00
drupal:
  nid: 3142
  path: /blog/2021/htgwa-create-samba-smb-share-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - htgwa
  - linux
  - raspberry pi
  - samba
  - sharing
  - smb
  - tutorial
  - windows
---

This is a simple guide, part of a series I'll call 'How-To Guide Without Ads'. In it, I'm going to document how I create Samba (SMB) shares in Linux on a Raspberry Pi.

## Install Samba

This is important, for obvious reasons:

```
$ sudo apt install -y samba samba-common-bin
```

## Create a shared directory

```
$ sudo mkdir /mnt/mydrive/shared
$ sudo chmod -R 777 /mnt/mydrive/shared
```

I won't deal with permissions in this post; [read the Samba docs](https://www.samba.org/samba/docs/using_samba/ch09.html) for that.

## Configure Samba to share that directory

Edit the Samba config file with `sudo nano /etc/samba/smb.conf`, and add the following:

```
[shared]
path=/mnt/mydrive/shared
writeable=Yes
create mask=0777
directory mask=0777
public=no
```

Restart Samba so the new shared directory is available:

```
$ sudo systemctl restart smbd
```

## Create a password for Samba access

The user must already exist on the system; in this example, I'll use the default `pi` user:

```
$ sudo smbpasswd -a pi
<enter password as prompted>
Added user pi.
```

## Connect to the share

From another computer, access: `smb://[hostname-or-ip-of-pi]/`, and enter the username and password you just configured.
