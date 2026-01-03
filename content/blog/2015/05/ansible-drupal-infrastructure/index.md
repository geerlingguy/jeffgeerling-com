---
nid: 2495
title: "Ansible for Drupal infrastructure and deployments - DrupalCon LA 2015 BoF"
slug: "ansible-drupal-infrastructure"
date: 2015-05-13T21:57:08+00:00
drupal:
  nid: 2495
  path: /blogs/jeff-geerling/ansible-drupal-infrastructure
  body_format: full_html
  redirects: []
tags:
  - ansible
  - deployment
  - dramble
  - drupal
  - drupal 8
  - drupal planet
  - drupalcon
  - raspberry pi
---

We had a great discussion about how different companies and individuals are using Ansible for Drupal infrastructure management and deployments at DrupalCon LA, and I wanted to post some slides from my (short) intro to Ansible presentation here, as well as a few notes from the presentation.

The slides are below:

<div style="text-align: center;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/Fy7AHxhL1AUeNw" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe></div>

And video/audio from the BoF:

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/cmFmg3d8ZcY" frameborder="0" allowfullscreen></iframe></div>

<h2>Notes from the BoF</h2>

If first gave an overview of the basics of Ansible, demonstrating some Ad-Hoc commands on my <a href="https://github.com/geerlingguy/raspberry-pi-dramble">Raspberry Pi Dramble</a> (a cluster of six Raspberry Pi 2 computers running Drupal 8), then we dove headfirst into a great conversation about Ansible and Drupal.

<p style="text-align: center;">{{< figure src="./raspberry-pi-dramble-hero.jpg" alt="Raspberry Pi Dramble - Hero" width="271" height="350" >}}
<a href="https://github.com/geerlingguy/raspberry-pi-dramble">The Raspberry Pi #Dramble</a></p>

Some notes from that discussion:

<ul>
<li>There are now many different local and production open source environment stacks built with Ansible, like <a href="http://www.drupalvm.com/">Drupal VM</a>, <a href="https://www.drupal.org/project/devshop">DevShop</a>, <a href="https://github.com/NBCUTechnology/pubstack">Pubstack</a>, <a href="http://www.getvalkyrie.com/">Valkyrie</a>, and <a href="http://vlad-docs.readthedocs.org/en/latest/">Vlad</a>.</li>
<li>Many companies are using Ansible as an infrastructure management tool, but sticking with tools like Cobbler, Bower, etc. for actual code deployment. Some people also use Ansible for deployment, but it really depends on the project/team's needs.</li>
<li>A lot of people liked (especially in comparison to tools like Chef and Puppet) how approachable and straightforward Ansible is; instead of taking days or weeks to get up to speed, you can dive right into Ansible and start using it in a day.</li>
<li>Connor Krukowsky has <a href="https://twitter.com/mattkineme/status/597895927127379968">Drupal 8 running on his 8-core rooted Android phone</a>!</li>
</ul>

<h2>Discount on Ansible for DevOps</h2>

I'm almost finished writing <a href="http://bit.ly/a4d-drupalcon">Ansible for DevOps</a>, and you can purchase it now from LeanPub and keep getting updates as I continue writing—here's a <a href="http://bit.ly/a4d-drupalcon">coupon code for half off</a>!

<h2>Summary</h2>

It was a great BoF, and I hope we can keep the discussion going about how different teams are using Ansible with Drupal infrastructure, and how we can all help each other through shared projects, roles, and techniques!

And maybe I'll finally get back to my work on a drush module for Ansible ;)
