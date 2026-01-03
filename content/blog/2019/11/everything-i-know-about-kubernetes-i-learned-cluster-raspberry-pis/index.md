---
nid: 2953
title: "Everything I know about Kubernetes I learned from a cluster of Raspberry Pis"
slug: "everything-i-know-about-kubernetes-i-learned-cluster-raspberry-pis"
date: 2019-11-26T20:54:39+00:00
drupal:
  nid: 2953
  path: /blog/2019/everything-i-know-about-kubernetes-i-learned-cluster-raspberry-pis
  body_format: markdown
  redirects: []
tags:
  - appearances
  - dramble
  - drupal
  - drupal planet
  - drupalcon
  - kubernetes
  - presentations
  - raspberry pi
---

I realized I haven't posted about my DrupalCon Seattle 2019 session titled [Everything I know about Kubernetes I learned from a cluster of Raspberry Pis](https://events.drupal.org/seattle2019/sessions/everything-i-know-about-kubernetes-i-learned-cluster-raspberry-pis), so I thought I'd remedy that. First, here's a video of the recorded session:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/yLzO88h40uw" frameborder='0' allowfullscreen></iframe></div>

<p style="text-align: center;">{{< figure src="./pi-dramble-original.jpeg" alt="The original Raspberry Pi Dramble Cluster" width="390" height="589" class="insert-image" >}}<br>
<em>The original Pi Dramble 6-node cluster, running the LAMP stack.</em></p>

I started running the [Raspberry Pi Dramble](https://www.pidramble.com) in 2014, after I realized I could automate the setup of everything in a LAMP stack on a set of Raspberry Pi 2s using Ansible (one Pi for an HTTP load balancer/reverse proxy, two for PHP app backends, and two for MySQL redundancy. Kubernetes was the logical next step, so I moved things towards Kubernetes in 2017, but running Kubernetes was a lesson in pain due to the Pi's limited memory (1 GB maximum) at the time.

When the Raspberry Pi 4 came around, I acquired some 2 GB models as quickly as I could, and redeployed onto them. Gone were the restrictions that were causing Kubernetes' API to be flaky with the older Pis, and now the Pi 4 cluster is extremely reliable. Early on, [cooling was an issue](//www.jeffgeerling.com/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one), but the recent firmware update has made that less problematic. I now power the cluster using the official PoE HAT, which means I only have one plug for each Pi, and everything fits nicely into a small travel case (if I want to bring the cluster with me anywhere).

<p style="text-align: center;">{{< figure src="./pi-dramble-4-k8s-edition.jpeg" alt="Raspberry Pi Dramble 4 Kubernetes edition cluster" width="650" height="432" class="insert-image" >}}<br>
<em>The current Pi Dramble, running Kubernetes and sporting <a href="https://www.blinkstick.com/products/blinkstick-nano">BlinkStick Nanos</a>.</em></p>

I even got it all to run off a 10,000 mAh battery pack with a bunch of USB splitters... but it did not stay powered long, and kept giving low power warnings—so I'll have to consider other options for a highly-mobile four-node Kubernetes bare-metal cluster.

I've continually updated the cluster so it is tested in a [Docker-based Kubernetes environment](https://github.com/geerlingguy/raspberry-pi-dramble/tree/master/testing/docker), a [Vagrant-based Kubernetes local development environment](https://github.com/geerlingguy/raspberry-pi-dramble/tree/master/testing/vagrant), and of course, the Pi environment. The latter environment causes much consternation, as many common container images are not maintained in an `armv6` or `linux/arm` format, which is required when running on the 32-bit ARM OS the Pi uses, Raspbian. But the Pi Dramble abides, and it quietly goes on, serving up traffic for [https://www.pidramble.com](https://www.pidramble.com) through the years.

The official [Pi Dramble Wiki](https://www.pidramble.com/wiki) has all the instructions for building your own Pi Kubernetes cluster, with links to buy all the parts I have, along with every step to get it running using open source Ansible roles to install Kubernetes and Docker for ARM, then configure a new four-node cluster.
