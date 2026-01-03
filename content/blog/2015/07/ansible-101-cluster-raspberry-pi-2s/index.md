---
nid: 2599
title: "Ansible 101 - on a Cluster of Raspberry Pi 2s"
slug: "ansible-101-cluster-raspberry-pi-2s"
date: 2015-07-15T14:55:47+00:00
drupal:
  nid: 2599
  path: /blog/ansible-101-cluster-raspberry-pi-2s
  body_format: full_html
  redirects: []
tags:
  - ansible
  - infrastructure
  - raspberry pi
  - tutorial
  - video
---

<p style="text-align: center;">{{< figure src="./ansible-101-thumb.jpg" alt="Ansible 101 - Raspberry Pi Dramble cluster" width="500" height="281" class="inserted-image" >}}</p>

Over the course of this year, I've acquired six Raspberry Pi model 2 B computers, and configured them in a cluster (or 'bramble') so I can use them to test different infrastructure configurations, mostly for running Drupal 8. All the Ansible playbooks and instructions for building the cluster are available on the GitHub project page for the <a href="https://github.com/geerlingguy/raspberry-pi-dramble">Raspberry Pi Dramble</a>.

Each Raspberry Pi has its own <a href="https://github.com/geerlingguy/raspberry-pi-dramble/wiki/RGB-LEDs-controlled-via-GPIO">RGB LED board</a> that's wired into the GPIO pins, so they're controlled by software. I can demonstrate different ways of managing the cluster via Ansible, and I finally took the time to make a video, <a href="https://www.youtube.com/watch?v=ZNB1at8mJWY">Ansible 101 - on a cluster of Raspberry Pi 2s</a>, which shows how it all works together:

<p style="text-align: center;"><iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/ZNB1at8mJWY?rel=0" frameborder="0" allowfullscreen></iframe></p>

The video demonstrates Ansible's simple and powerful model of SSH-based infrastructure management <em>visually</em>. It's been a lot of fun building the Dramble and hacking both the hardware and the software to make this presentation possible!

Since building the Dramble, I've taken it with me to presentations at <a href="/blog/midcamp-2015-ansible-drupal-8-presentation">MidCamp</a> in Chicago, <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/ansible-drupal-infrastructure">DrupalCon</a> in LA, and local meetups in St. Louis (like the first ever <a href="http://www.meetup.com/Ansible-St-Louis/events/221236470/">Ansible St. Louis meetup</a>!). I've also used the cluster to debug some hard-to-reproduce infrastructure and performance problems in Drupal, and I hope to continue finding fun new things to do with it!

More resources:

<ul>
<li><a href="http://ansiblefordevops.com/">Ansible for DevOps</a> (my book on Ansible)</li>
<li><a href="https://github.com/geerlingguy/raspberry-pi-dramble">Raspberry Pi Dramble</a></li>
<li><a href="https://github.com/geerlingguy/raspberry-pi-dramble/wiki/Raspberry-Pis-and-Accessories">Raspberry Pi Dramble - Parts list</a> (in case you want your own!)</li>
<li><a href="http://docs.ansible.com/">Ansible Documentation</a></li>
</ul>
