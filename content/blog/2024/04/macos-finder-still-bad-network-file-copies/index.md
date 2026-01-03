---
nid: 3364
title: "macOS Finder is still bad at network file copies"
slug: "macos-finder-still-bad-network-file-copies"
date: 2024-04-03T21:56:51+00:00
drupal:
  nid: 3364
  path: /blog/2024/macos-finder-still-bad-network-file-copies
  body_format: markdown
  redirects: []
tags:
  - finder
  - mac
  - macos
  - nas
  - networking
  - nfs
  - raspberry pi
  - samba
  - windows
---

In what is becoming a kind of hobby for me, I've just finished testing another tiny NAS—more on that tomorrow.

But as I was testing, I started getting frustrated with the fact I've never been able to get a Raspberry Pi—regardless of internal storage speeds, even with 800+ MB/sec PCIe-based storage—to consistently _write_ more than around 100 MB/sec write speeds over the network, with either Samba or NFS.

NFS would be more consistent... but it ran around 82 MB/sec:

{{< figure src="./nfs-file-copy-to-pi-5-macos.png" alt="NFS file copy to Raspberry Pi 5 stalled at 80 MB per second" width="398" height="auto" class="insert-image" >}}

Samba would peak around 115 MB/sec, but it was wildly inconsistent, averaging around 70 MB/sec:

{{< figure src="./samba-file-copy-to-pi-5-macos.png" alt="Samba file copy to Raspberry Pi 5 wild undulations" width="426" height="auto" class="insert-image" >}}

I have a problem: I use macOS[^usemac].

This blog post isn't about whether _macOS_ is good or bad, but it _is_ about network shares on macOS. And quantitatively, through the years, network shares on Mac OS, Mac OS X, and macOS have always been _bad_.

No matter what incantations I tried, with NFS, Samba, client, or server—and yes, I've even spoken to one of the Samba devs about it—there was no way to get beyond 100 MB/sec write speeds on the Pi from my Mac[^hl15].

_Read_ speeds were always fine, when copying from the Pi to my Mac. I could peg it at 122 MB/sec over the Pi's 1 Gbps connection, and 230 MB/sec over a 2.5 Gbps connection (courtesy of the Pineberry Pi [HatNET! 2.5G](https://pineberrypi.com/products/hatnet-2-5g-2-5-gigabit-ethernet-for-raspberry-pi-5)).

I started wondering if the problem was truly on the Raspberry Pi after [tkaiser recommended monitoring more deeply with `atop`](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/615#issuecomment-2034981369). I didn't see _anything_ amiss, and the Pi had a ton of headroom (CPU, network, interrupts, and disk IO were all well in hand).

So that led me down a rabbit hole of testing:

  - I verified using `iperf3` that my network connections were at line speed. `iperf3` showed 940 Mbps to and from on the 1 Gbps LAN, and about 2 Gbps on the 2.5 Gbps connection—lower than the normal 2.35 Gbps because it's through a PCIe Gen 2 packet switch.
  - I verified using `iozone` that my storage was writing through at over 800 MB/sec to a 4-drive RAIDZ1 array of SATA SSDs (tested with a 50 GB test file in 1M chunks).
  - macOS Sonoma doesn't seem to have an `/etc/nsmb.conf` file by default, but according to many, in _past_ macOS releases adding `signing_required=no` in this file would speed things up by disabling Samba packet signing (a security feature not really required on LANs).
  - It [didn't seem like signing was active](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/615#issuecomment-2035286025) on this connection, from all my research, but I did spend an hour or so force-disabling it everywhere... which made no difference.
  - I tried a bunch of other server-side tweaks, none of them seemed to make any difference.
  - I tried [using `cp` and `rsync`](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/615#issuecomment-2035518436) to see if it was just the Finder where this issue cropped up—both were more consistent in their write speed to the share, but slower overall.
  - I fired up [Transmit](https://panic.com/transmit/), my SFTP client, and copied the same directory over using SSH / scp, and it [copied at 112 MB/sec](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/615#issuecomment-2035504903), very consistently. Yay for SSH file copies being faster than Samba, I guess!

I'll spare you [many hours of debugging](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/615)—I eventually booted up [my Windows 11 PC](/blog/2023/moving-my-pc-my-rack-2u-case) and ran all the same tests, with the same 50 GB video project folder[^sizematters].

On there?

{{< figure src="./samba-file-copy-to-pi-5-windows.png" alt="Samba file copy to Pi 5 Windows 11" width="447" height="auto" class="insert-image" >}}

Consistent 108 MB/sec write speeds for the entire copy over the 1 Gbps connection.

{{< figure src="./samba-file-copy-to-pi-5-windows-2.5g.png" alt="Samba file copy to Pi 5 from Windows 2.5 Gbps" width="447" height="auto" class="insert-image" >}}

And then it ran at 150 MB/sec over the 2.5 Gbps connection. (The bottleneck, in this case, is the PCIe Gen 2 switch, used to install a 2.5G PCIe NIC in addition to four SATA SSDs on the Pi 5's single PCIe lane. More on that tomorrow!)

Read speeds are the same from macOS to Windows, though. Since ZFS doesn't need to do the parity calculation and writes, it can read out from the four drive array a bit faster.

{{< figure src="./samba-file-copy-from-pi-5-to-windows.png" alt="Samba file copy from Pi 5 to Windows 2.5 Gbps" width="447" height="auto" class="insert-image" >}}

What I still don't understand is where the bottleneck lies on macOS's side. I don't see anything that screams bottleneck when monitoring with Activity Monitor or `htop` on my Mac. And I don't know of any equivalent to `atop` that will let me monitor interrupts and other resources like I can on Linux.

Any other ideas why macOS is so bad at writes to network shares?

I guess I should be happy network shares work _at all_ though... in the past I would fight against macOS's built-in NFS support [to even get them _mounted_](https://apple.stackexchange.com/q/413767/17366)!

[^usemac]: At least for my primary workstation where I edit video and build and test infrastructure automation.

[^hl15]: On my HL15 NAS—[which also runs on Arm, though a beefier server Ampere chip](/blog/2024/building-efficient-server-grade-arm-nas)—I can get 500+ MB/sec, though even there, the write speed goes up and down a lot. I just thought that was normal... but may not.

[^sizematters]: Whenever you're benchmarking network storage, you should try to use file or directory sizes that are many times larger than the RAM on the server, that way Linux filesystem caches or ZFS caching won't give you false results. You should have files much larger than any potential cache size so you can test access all the way through to the disks.
