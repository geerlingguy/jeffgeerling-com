---
nid: 3288
title: "Building a tiny 6-drive M.2 NAS with the Rock 5 model B"
slug: "building-tiny-6-drive-m2-nas-rock-5-model-b"
date: 2023-07-10T14:00:19+00:00
drupal:
  nid: 3288
  path: /blog/2023/building-tiny-6-drive-m2-nas-rock-5-model-b
  body_format: markdown
  redirects: []
tags:
  - armbian
  - nas
  - omv
  - radxa
  - rock 5
  - storage
---

As promised in [my video](https://www.youtube.com/watch?v=5QH8Dj6g_Nk) comparing SilverTip Lab's DIY Pocket NAS (express your interest [here](https://rpgtavern.live/index.php?page=mininas)) to the ASUSTOR Flashstor 12 Pro, this blog post outlines how I built a 6-drive M.2 NAS with the Rock 5 model B.

The Rockchip RK3588 SoC on the Rock 5 packs an 8-core CPU (4x A76, 4x A55, in a 'big.LITTLE' configuration). This SoC powers a PCIe Gen 3 x4 M.2 slot on the back, which is used in this tiny 6-drive design to make a compact, but fast, all-flash NAS:

{{< figure src="./6-bay-rock5-nas.jpeg" alt="6-bay Rock 5 NAS" width="700" height="467" class="insert-image" >}}

Pair that with the built-in 2.5 Gbps Ethernet port on the Rock 5, and... could this little package compete against commercial offerings like those from [QNAP](https://amzn.to/3Pi6oD0) and [ASUSTOR](https://amzn.to/43YLYDd)? It's certainly a lot more compact:

{{< figure src="./6-bay-rock5-nas-asustor-12-bay-m2-nas.jpeg" alt="ASUSTOR 12-bay M.2 Flashstor NAS with Rock 5 model B compact 6-bay SATA NAS" width="700" height="394" class="insert-image" >}}

Watch the video linked at the top of this post to find out. And if you're interested in a Pocket NAS-style device (the one I tested is just a prototype), [express your interest here](https://rpgtavern.live/index.php?page=mininas)!

The rest of this blog post details how I set up [OpenMediaVault](https://www.openmediavault.org) on the Rock 5 to test SMB sharing performance on my network.

## Preparing the Rock 5 for OMV (Armbian setup)

  1. Download [Armbian 23.02 Bullseye CLI (minimal)](https://www.armbian.com/rock-5b/) (Go to 'Archived versions for reference and troubleshooting) – the specific version I downloaded was `Armbian_23.02.2_Rock-5b_bullseye_legacy_5.10.110_minimal.img.xz`
  1. Flash the ISO to a microSD card with Etcher
  1. Insert the microSD card and boot the Rock 5
  1. Log into the Rock 5 via SSH and follow the first time setup (initial login is `root` / `1234`)
  1. Install `git`: `apt update && apt install -y git`
  1. Get the fan set up (see separate instructions below)
  1. Run updates: `sudo apt update && sudo apt upgrade -y`
  1. Reboot: `sudo reboot`

## Set up the PWM fan

{{< figure src="./6-bay-rock5-nas-fan.jpeg" alt="WINSINN fan on top of 6-bay Rock 5 model B NAS" width="700" height="467" class="insert-image" >}}

  1. Clone the fan control software to the Rock 5: `git clone https://github.com/XZhouQD/Rock5B_Naive_Pwm_Fan.git`
  1. Switch to root user: `sudo su`
  1. Enter the fan control directory: `cd Rock5B_Naive_Pwm_Fan`
  1. Copy the fan control binary: `cp fan_pwm /usr/local/bin/.`
  1. Make it executable: `chmod +x /usr/local/bin/fan_pwm`
  1. Set up the fan control systemd service: `cp fan_pwm.service /etc/systemd/system/.`
  1. Reload systemd: `systemctl daemon-reload`
  1. Start the fan service and enable it at system boot: `systemctl start fan_pwm &amp;&amp; systemctl enable fan_pwm`

As an alternative to the PWM fan control app detailed above, you could instead use [https://github.com/pymumu/fan-control-rock5b](https://github.com/pymumu/fan-control-rock5b).

## Install OMV

The last step is to install [OpenMediaVault](https://www.openmediavault.org), a nice NAS-style management UI and ecosystem that works great on Arm boards like the Rock 5 model B.

  1. Install OMV: `sudo wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash`
  1. After reboot, access the IP address of the Rock 5, and log into openmediavault with login `admin` / `openmediavault`.
  1. In OMV, to create a SMB share for testing (make sure you click 'Apply' when it pops up in the UI after each step!):
     1. Go to Storage &gt; Software RAID, and add a new software RAID device. I chose three drives and RAID 5, but you can choose what you want.
     1. While the RAID volume is sycning, go to File Systems, and add a new one; I chose EXT4 for mine.
     1. After the File System is created, it is not mounted. You have to click on it and click the 'Play' button to mount it.
     1. Go to 'Shared Folders' and create a new one; I created one with the defaults called 'test'.
     1. Go to Services &gt; SMB/CIFS &gt; Settings, and check the 'Enabled' checkbox. Click 'Save' at the bottom of the settings page.
     1. Go to Services &gt; SMB/CIFS &gt; Shares, and add a new SMB Share. Select the Shared Folder you created earlier, and configure permissions as you see fit. I enabled full public read/write access for testing.
  1. Wait for OMV to finish syncing the RAID 5 array (you can monitor progress under Storage &gt; Software RAID).
  1. Once the array is finished syncing, the 'State' should read "clean"
  1. On another computer on the network, access the SMB share. On my Mac, in the Finder, I chose Go &gt; Connect to Server (⌘ K), then entered the address `smb://[ip address of Rock 5]/test`

Log in using a user account on the system, and you can now copy files to and from the SMB share to your heart's content!

On the Rock 5 model B, I was getting around 100 MB/sec write speeds, and 200 MB/sec read speeds, using a 3-drive RAID 5 volume over my 2.5 Gbps network. Write speeds were an improvement over the Raspberry Pi CM4 NAS I built last year, but not double or triple the speed as I was hoping. And SMB read speeds could hit about 1.9-2.1 Gbps but still couldn't saturate the Ethernet connection. So... _good_, but not as marked an improvement over a slower and older Pi as I was hoping.

For more details, and a full comparison, [watch the full video on the Pocket NAS and Flashstor 12 Pro](https://www.youtube.com/watch?v=5QH8Dj6g_Nk).
