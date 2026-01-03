---
nid: 2594
title: "Ansible deployments Visualized with a Raspberry Pi cluster"
slug: "ansible-deployments-visualized-raspberry-pi"
date: 2015-03-09T02:04:36+00:00
drupal:
  nid: 2594
  path: /blog/ansible-deployments-visualized-raspberry-pi
  body_format: full_html
  redirects: []
tags:
  - ansible
  - dramble
  - electronics
  - led
  - raspberry pi
  - video
aliases:
  - /blog/ansible-deployments-visualized-raspberry-pi
---

<p style="text-align: center;">{{< figure src="./raspberry-pi-dramble-cluster_1.jpg" alt="Raspberry Pi Dramble - cluster of Raspberry Pi computers" width="309" height="400" >}}</p>

For the past few weeks, I've been building a cluster of six Raspberry Pis to test and demonstrate Ansible playbooks for Drupal deployment at upcoming events (like <a href="http://2015.midcamp.org/session-proposal/ansible-drupal-fortuitous-devops-match">MidCamp</a> and <a href="https://events.drupal.org/losangeles2015/sessions/deploying-drupal-8-bare-metal-ansible-live">DrupalCon LA</a>).

I added an RGB LED to each of the Raspberry Pis that can be controlled via software (for example, <a href="https://github.com/geerlingguy/raspberry-pi-dramble/blob/dfe8b763513566e664506ee06378b261673ab831/playbooks/roles/leds/templates/rgb.j2">here's a Python script to turn on one individual color on the LED</a>), and as part of the demonstration, I'm using the LEDs to indicate which server Ansible is currently working with.

<p style="text-align: center;">{{< figure src="./dramble-led-board-detail_0.jpg" alt="RGB LED board for Raspberry Pi GPIO" width="233" height="275" >}}
(<a href="https://github.com/geerlingguy/raspberry-pi-dramble/wiki/RGB-LEDs-controlled-via-GPIO">See how the LEDs are wired and controlled on the Wiki</a>)</p>

Ansible allows you to run playbooks and tasks (or parts of plays) in many different ways. It's most efficient to run a task or playbook on all the servers at once (with as high a <code>forks</code> value in your configuration as your workstation or network can support). But it's often helpful to deploy something to one or a small subset of servers, verify it's working, then move on to the next batch (using <code>serial</code> along with <code>max_fail_percentage</code> can be very helpful!).

I made a quick demonstration video so you can see how Ansible deploys to servers when using different common <code>serial</code>/<code>forks</code> settings:

<p style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/rRJQiHydVG4" frameborder="0" allowfullscreen></iframe></p>

A lot of the research and testing I'm doing on this cluster of six Raspberry Pi 2 computers (christened the <em><a href="https://github.com/geerlingguy/raspberry-pi-dramble">Dramble</a></em>) is helping improve <a href="http://ansiblefordevops.com/">Ansible for DevOps</a>, a book I'm writing on Ansible. I'll be posting more here and elsewhere on experiences with the Raspberry Pi Dramble cluster in the coming weeks!

For more on using Ansible's <code>forks</code>, <code>serial</code>, and <code>max_fail_percentage</code>, read the documentation:

<ul>
<li><a href="http://docs.ansible.com/playbooks_delegation.html">Delegation, Rolling Updates, and Local Actions</a></li>
<li><a href="http://docs.ansible.com/intro_configuration.html#forks">The Ansible Configuration File - Forks</a></li>
</ul>
