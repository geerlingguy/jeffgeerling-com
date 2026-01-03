---
nid: 3087
title: "Raspberry Pi 2.5 Gbps 16 TB OMV NAS - Setup and Performance"
slug: "raspberry-pi-25-gbps-16-tb-omv-nas-setup-and-performance"
date: 2021-04-02T16:30:36+00:00
drupal:
  nid: 3087
  path: /blog/2021/raspberry-pi-25-gbps-16-tb-omv-nas-setup-and-performance
  body_format: markdown
  redirects: []
tags:
  - asustor
  - benchmarks
  - hard drive
  - nas
  - raid
  - raspberry pi
  - video
---

{{< figure src="./raspberry-pi-2.5g-nas.jpeg" alt="Raspberry Pi CM4 2.5 Gbps NAS build" width="600" height="369" class="insert-image" >}}

Last week, I posted about the [Pi NAS hardware build](/blog/2021/building-25-gbps-5-drive-pi-nas-hardware-setup), and compared setting up an off-the-shelf [ASUSTOR Lockerstor 4](https://amzn.to/3woHIN8) to the same thing, but with a Raspberry Pi Compute Module 4 an IO Board.

Some people wondered why not just use a Raspberry Pi 4 model B with USB hard drives, and there are a few reasons:

  1. The model B's USB 3.0 ports add about a 10% overhead to SATA operations, which is more apparent over small file operations.
  2. You can't RAID together USB 3.0 drives using OMV or other NAS-specific software, since RAID over USB is not very reliable.
  3. The Compute Module 4 IO Board's PCI Express slot lets me plug in multiple cards, like a [2.5 Gbps Rosewill NIC](https://pipci.jeffgeerling.com/cards_network/rosewill-rc20001-25gbe.html) _and_ a [5-port IOCrest SATA controller](https://pipci.jeffgeerling.com/cards_storage/iocrest-sata-5-port-jmb585.html).

## Video

There is a video to go along with this blog post, that goes into much more depth on the full setup process on the ASUSTOR Lockerstor 4 and OMV on the Raspberry Pi:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/KhHAf7mTxkk" frameborder='0' allowfullscreen></iframe></div>
</div>

## Open Media Vault

With that out of the way, and the hardware set up and running, I went to install [Open Media Vault](https://www.openmediavault.org), and found the process to be pretty painless; I just had to run one command to run their [install script for Pi OS](https://github.com/OpenMediaVault-Plugin-Developers/installScript):

```
wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash
```

After that completed, I used `sudo nmap -sn 10.0.100.0/24 | grep pi` to find the Pi's new IP address (OMV usually changes the IP as part of its setup process), and then logged into the web management UI in my browser (default credentials `admin`/`openmediavault`):

{{< figure src="./omv-browser-login.jpg" alt="Open Media Vault browser login screen" width="700" height="394" class="insert-image" >}}

The UI is straightforward and utilitarian. After having set up the Lockerstor 4, which uses ADM, a custom Linux distro built on top of Busybox, it felt a little less polished having to do things like manage filesystems and click through 3-5 different screens to set up a new network share in OMV.

But it's definitely manageable, and a one-time task; the only real annoyance was the fact that after I clicked 'OK' for a settings change, there would be a bar that appeared at the top of the screen 3-5 seconds later telling me I also had to apply the change for it to take effect. I'm not sure why it wouldn't just apply it when I click 'OK' or 'Save' in the first place:

{{< figure src="./omv-apply-configuration-changes.jpg" alt="OMV Do you really want to apply configuration changes?" width="700" height="394" class="insert-image" >}}

## Performance

I decided to stick with Samba (SMB) shares and Windows 10 for the performance testing, mostly because I have a PC tied into my 10 Gbps network with a DAC sitting in my office, and its easier to run uninterrupted benchmarks on it with nothing else running than it is to do so on my main Mac workstation.

{{< figure src="./copy-file-from-pc-to-pi-nas.jpg" alt="File copy in Windows 10 from PC to Raspberry Pi NAS" width="500" height="282" class="insert-image" >}}

Copies to the Pi NAS, with three [Seagate IronWolf 8TB NAS drives](https://amzn.to/3wlO9AC) in RAID 5, measured around 95 MB/sec. Copies _from_ the Pi clocked in around 193 MB/sec.

But I noticed two things when I ran `atop` during the copy:

  1. When writing to the RAID 5 array, after the RAM cache would fill up (after about 0.5 GB of data copied), the single-threaded `smb` process would be around 70% CPU, one core would hit around 50% interrupts (network packets seem to only be able to go through one CPU core on the current Pi generation), and the CPU in general would run between 40-70% CPU.
  2. When reading from the array, interrupts on the single core would hit 99% and the copy would top out around 1.7 Gbps (about 200 MB/sec).

Using Jumbo Frames (9000 MTU) could mitigate the network packet overhead issue, but I also remember from previous testing that overclocking the CPU also produced a noticeable speed gain.

Overclocked to 2.0 GHz, the Raspberry Pi was able to put through about 100 MB/sec write speeds, and 200 MB/sec read speeds. Not too bad, but also a bit less than the ASUSTOR, which has a faster Intel CPU inside, and much more PCI Express bandwidth to go around. Even without SSD caching, the ASUSTOR wrote to the drives more than twice as fast as the Pi:

{{< figure src="./smb-network-copy-asustor-vs-pi-2.5g.png" alt="Samba network file copy performance - ASUSTOR Lockerstor 4 vs Raspberry Pi NAS 2.5 Gbps" width="700" height="394" class="insert-image" >}}

I also tried a RAID 0 array on the Pi, to take out the overhead associated with RAID parity calculations. This seemed to go well, as a write to the Pi was solid at 230 MB/sec... but then the Pi locked up partway through the copy. This happened every time I tried copying to and from the RAID 0 array, and I'm still trying to figure out why.

I didn't have four similar drives to test out RAID 10, but I may test that out when I get a chance.

## Conclusion

As I mentioned in the video, I think for most people who need network storage and don't need the extreme customization (or performance, if building a server with a better processor/ECC RAM), an out-of-the-box NAS like the Lockerstor (or a Synology, QNAP, etc.) is the best option.

Modern NASes like the Lockerstor I tested are performant, well-supported, and easy to set up and configure.

If you don't need the faster networking, though, there is one Pi-based option I'm keeping my eye on, the [Wiretrustee SATA](https://wiretrustee.com), a CM4-based board that will incorporate a SATA controller and power for the drives.

{{< figure src="./wiretrustee-sata-pi-cm4-2.5in-case.jpg" alt="Wiretrustee SATA inside case 2.5 in hard drives" width="600" height="533" class="insert-image" >}}

Using it with 2.5" SATA drives would make for a very compact, fast-enough 1 Gbps NAS.

But if you want more performance, want ECC memory, or if you need something like FreeNAS or ZFS, neither of which run that well on a Raspberry Pi, you'll have to stick to a custom build or higher end server for now.
