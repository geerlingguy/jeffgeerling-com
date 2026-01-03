---
nid: 3245
title: "Automating my Homelab with Ansible (AnsibleFest 2022)"
slug: "automating-my-homelab-ansible-ansiblefest-2022"
date: 2022-10-19T14:01:57+00:00
drupal:
  nid: 3245
  path: /blog/2022/automating-my-homelab-ansible-ansiblefest-2022
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansiblefest
  - appearances
  - presentations
---

At AnsibleFest 2022, I presented [Ansible for the Homelab](https://events.experiences.redhat.com/widget/redhat/rhaf22/SessionCatalog2022/session/1652910586803001DTXx).

{{< figure src="./jeff-geerling-homelab-2022-rack-basement.jpeg" alt="Jeff Geerling's Homelab Rack in 2022" width="700" height="467" class="insert-image" >}}

In the presentation, I gave a tour of my homelab, highlighting it's growth from a modem and 5-port switch to a full 24U rack with a petabyte of storage and multiple 10 gigabit switches!

Then I spent some time discussing how various components are automated using Ansible, mostly using open source projects on GitHub.

Unfortunately for attendees, the room my session was in was packed, and a lot of people who wanted to see it were turned away.

{{< figure src="./jeff-geerling-ansiblefest-2022-homelab-session.jpeg" alt="Jeff Geerling at AnsibleFest 2022 delivering presentation on Ansible and the Homelab" width="700" height="443" class="insert-image" >}}

Luckily I also pre-recorded the presentation and posted it on my YouTube channel. So now _everyone_ can watch it!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/yoFTL0Zm3tw" frameborder="0" allowfullscreen=""></iframe></div>
</div>

I mentioned a number of Ansible playbooks and open source projects in the presentation; here's a list of all of them:

  - You can get a [free copy](https://www.jeffgeerling.com/ansible-2022) of my book [Ansible for DevOps](https://www.ansiblefordevops.com)—feel free to pass along the link to others!
  - My Dad and I [upgraded my 20U rack to a new, much deeper 24U rack](https://www.youtube.com/watch?v=pvr1mKs1UjE) on the Geerling Engineering YouTube channel—and we had a little _too_ much fun!
  - Last year I built the [PetaPi - a single Raspberry Pi addressing a _petabyte_ of storage](https://www.youtube.com/watch?v=BBnomwpF_uY).
  - See how I use a [Raspberry Pi to monitor my home Internet](https://www.youtube.com/watch?v=rIUc4C4TXog).
  - For fast, low-latency video editing, I built an [All-SSD Edit NAS running TrueNAS](https://www.youtube.com/watch?v=xvE4HNJZeIg).
  - I recently started [Monitoring my ASUS WiFi router with Prometheus and Grafana](/blog/2022/monitoring-my-asus-rt-ax86u-router-prometheus-and-grafana).
  - See [My Backup Plan](https://github.com/geerlingguy/my-backup-plan), which includes the scripts I run on one of the Raspberry Pis in my rack to back things up to Amazon Glacier.
  - [Drupal Pi](https://github.com/geerlingguy/drupal-pi) is what I'm currently using to serve the Drupal website [pidramble.com](http://pidramble.com) directly from my home.
  - I'm currently testing a number of open source NVR (Network Video Recorder) applications on the Raspberry Pi, and documenting my work in my [pi-nvr project](https://github.com/geerlingguy/pi-nvr).
  - One of the Raspberry Pis in my rack runs [Pi-VPN](https://pivpn.io), giving me access to my homelab from anywhere.
  - I even manage my two Macs, using the popular [Mac Development Ansible Playbook](https://github.com/geerlingguy/mac-dev-playbook).
  - I'm experimenting setting up a [Raspberry Pi-based Router](https://github.com/geerlingguy/pi-router) to either supplement my existing Internet connection or replace my current ASUS router.

I put a listing of all the Homelab equipment I'm currently using (as of October 2022) in the [description of the YouTube video](https://www.youtube.com/watch?v=yoFTL0Zm3tw).

If you have any other questions about my homelab, or how I automate different parts of it, please feel free to ask in the comments! I may do a more formal 'homelab tour' later this year or early next year, so make sure you're [subscribed to my YouTube channel](https://www.youtube.com/c/JeffGeerling) to see it!
