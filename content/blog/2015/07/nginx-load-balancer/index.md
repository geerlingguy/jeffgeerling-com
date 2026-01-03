---
nid: 2502
title: "Nginx Load Balancer Visualization on a Raspberry Pi Cluster"
slug: "nginx-load-balancer"
date: 2015-07-28T17:03:30+00:00
drupal:
  nid: 2502
  path: /blogs/jeff-geerling/nginx-load-balancer
  body_format: full_html
  redirects: []
tags:
  - ansible
  - dramble
  - drupal
  - drupal 8
  - drupal planet
  - raspberry pi
  - video
---

After some more tinkering with the <a href="https://github.com/geerlingguy/raspberry-pi-dramble">Raspberry Pi Dramble</a> (a cluster of 6 Raspberry Pis used to demonstrate Drupal 8 deployments using Ansible), I finally was able to <a href="https://github.com/geerlingguy/raspberry-pi-dramble/issues/45">get the RGB LEDs to react to Nginx accesses</a>—meaning every time a request is received by Nginx, the LED toggles to red momentarily.

This visualization allows me to see exactly how Nginx is distributing requests among the servers in different load balancer configurations. The default (not only for Nginx, but also for Varnish, HAProxy, and other balancers) is to use round-robin distribution, meaning each request is sent to the next server. This is demonstrated first, in the video below, followed by a demonstration of Nginx's <code>ip_hash</code> method, which pins one person's IP address to one backend server, based on a hash of the person's IP address:

<div style="text-align: center;"><iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/7Tf2f5gdO4I?rel=0" frameborder="0" allowfullscreen></iframe></div>

It's fun to be able to visualize things like Drupal deployments, Nginx requests, etc., on this cluster of Raspberry Pis, and in addition to a presentation on <a href="https://servercheck.in/blog/midcamp-2015-ansible-drupal-8-presentation">Ansible + Drupal 8</a> at MidCamp, and <a href="https://www.youtube.com/watch?v=ZNB1at8mJWY">Ansible 101</a>, I'll be showing the Dramble in a soon-to-be-released episode of <a href="https://www.acquia.com/jams-drupal-camp">Jam's Drupal Camp</a> from Acquia—stay tuned!
