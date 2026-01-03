---
nid: 3497
title: "You can finally manage Macs with FileVault remotely in Tahoe"
slug: "you-can-finally-manage-macs-filevault-remotely-tahoe"
date: 2025-09-19T18:44:01+00:00
drupal:
  nid: 3497
  path: /blog/2025/you-can-finally-manage-macs-filevault-remotely-tahoe
  body_format: markdown
  redirects: []
tags:
  - level2jeff
  - mac
  - macos
  - remote access
  - ssh
  - tahoe
  - video
  - youtube
---

For years, I've had a couple Macs running at home and at my studio, which I use to remotely manage my video projects or some coding project.

{{< figure src="./mac-mini-m4-power-button-workbench.jpg" alt="M4 Mac mini workbench powering on" width="700" height="394" class="insert-image" >}}

It's nice to have a workstation set up that you can access anywhere via Screen Sharing to check on progress, jot down a note, etc.—and not be tied to a web app or some cloud service.

I run a Wireguard VPN at home and at my studio, so I can remotely log into any of my infrastructure through the VPN—Macs included.

_However_, after working through installing [NUT on a Pi for network UPS management](/blog/2025/nut-on-my-pi-so-my-servers-dont-die), I discovered my Mac, once rebooted, would not allow remote access until I was _physically present_ to type in my account password.

Why? Because FileVault encryption means the Mac won't fully _boot_ until you log in, physically, at the machine.

## Remote SSH before boot in macOS Tahoe 26

{{< figure src="./macos-tahoe-26-remote-login-ssh.jpg" alt="macOS Tahoe 26 remote login SSH enable in Sharing" width="700" height="394" class="insert-image" >}}

But with macOS Tahoe, if you have 'Remote Access' enabled in your Sharing settings (this enables SSH access), you can now log in via SSH _pre_ user login, then enter an Administrator's account password to 'unlock' the machine and complete the full boot.

And at that point, you can either log in via normal SSH, or use tools like Screen Sharing.

I made a quick video on my 2nd channel documenting this process and how it looks:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/bSLBkZB5o1o" frameborder='0' allowfullscreen></iframe></div>
</div>

One quirk: if my Mac was only connected to WiFi, I couldn't get connected pre-login. If I plugged it into Ethernet (wired networking), it worked fine. Not sure if that's a bug or if that's by design (maybe the WiFi password, which is stored in the account's Keychain, isn't accessible during early boot stages when the 'lightweight SSH' server is running?).
