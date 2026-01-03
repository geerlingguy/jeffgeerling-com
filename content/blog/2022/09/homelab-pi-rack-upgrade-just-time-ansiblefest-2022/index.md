---
nid: 3239
title: "Homelab Pi Rack upgrade, just in time for AnsibleFest 2022"
slug: "homelab-pi-rack-upgrade-just-time-ansiblefest-2022"
date: 2022-09-23T14:05:43+00:00
drupal:
  nid: 3239
  path: /blog/2022/homelab-pi-rack-upgrade-just-time-ansiblefest-2022
  body_format: markdown
  redirects: []
tags:
  - homelab
  - rack
  - raspberry pi
  - reviews
  - uctronics
  - video
  - youtube
---

[AnsibleFest](https://www.ansible.com/ansiblefest) is fast approaching, and this year it'll finally be back in person, in Chicago. Since that's a short jaunt from St. Louis, I'll be headed up to talk about my Homelab this year!

More specifically, I'll be giving a talk titled [Ansible for the Homelab](https://events.experiences.redhat.com/widget/redhat/rhaf22/SessionCatalog2022/session/1652910586803001DTXx), and I'll walk through how I have at least _part_ of my sprawling homelab environment automated using Ansible.

{{< figure src="./pi-rack-pro-detail.jpeg" alt="Raspberry Pi Rack Pro by UCTRONICS" width="700" height="467" class="insert-image" >}}

I'll be posting a version of the AnsibleFest talk to my YouTube channel, but leading up to it, the folks at UCTRONICS sent me their [Pi Rack Pro](https://amzn.to/3dzyl8T) to test out. I've been running four Raspberry Pi 4 model B computers in my rack for the past year, each one assuming a certain amount of responsibility for my homelab:

  1. Pi-Hole, Prometheus, and Grafana for Internet monitoring, local DNS, and privacy control. Runs my [internet-pi](https://github.com/geerlingguy/internet-pi) Ansible playbook.
  2. Drupal web server running the [Raspberry Pi Dramble](http://pidramble.com) website, currently with the configuration from my [drupal-pi](https://github.com/geerlingguy/drupal-pi) Ansible playbook.
  3. Backup server managing [my-backup-plan](http://github.com/geerlingguy/my-backup-plan) so I have a full 3-2-1 backup with offsite and offline copies of all my important data.
  4. Private VPN courtesy of [PiVPN](https://pivpn.io/).

These four Pis have gone through a number of mounting solutions, from sitting atop a network switch, to my first [3D printed 1U Pi rackmount](/blog/2021/my-6-node-1u-raspberry-pi-rack-mount-cluster), to a [MyElectronics hot-swap rack](/blog/2021/review-myelectronics-raspberry-pi-hot-swap-rack-system). This new setup incorporates many nice-to-haves, like captive thumbscrews for front-loading the Pis, a full metal enclosure, a built-in display and power button, a front panel push-push microSD slot, and an integrated SATA SSD sled, fitting four fully-outfitted Pis in 1U of rackspace.

I documented the process of upgrading to the new enclosure in today's video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/akJ97oqmQlU" frameborder="0" allowfullscreen=""></iframe></div>
</div>

It's not perfect (ventilation is my biggest gripe, as I mention in the video), and I'm currently customizing the LCD display panel more to my liking, but _if you're kind of insane like I am_ about Pis in racks, this is the best 1U solution available at any price.

Thanks again to UCTRONICS for sending me this rackmount unit for evaluation, and if you're interested (and the price isn't too high!), you can [buy the Pi Rack Pro on Amazon](https://amzn.to/3dzyl8T) for just under $300.

I'm not sure how long this particular iteration of the four-Pi-cluster will exist in my homelab, though—I noticed [Uptime.Lab is getting closer to releasing the Compute Blade](https://www.instagram.com/p/CiLDPfWtavu/). That could provide a lot more Pi compute density in 1U of rackspace!
