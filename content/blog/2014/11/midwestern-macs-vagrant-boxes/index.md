---
nid: 2472
title: "Midwestern Mac's Vagrant Boxes - CentOS and Ubuntu"
slug: "midwestern-macs-vagrant-boxes"
date: 2014-11-13T04:01:47+00:00
drupal:
  nid: 2472
  path: /blogs/jeff-geerling/midwestern-macs-vagrant-boxes
  body_format: full_html
  redirects: []
tags:
  - ansible
  - devops
  - drupal
  - drupal planet
  - packer
  - vagrant
  - virtualbox
---

In support of my mission to make local development easier and faster, I've released boxes for four of the most popular Linux distributions I use and see used for Drupal sites: CentOS 6/7 and Ubuntu 12.04/14.04.

<p style="text-align: center;"><a href="http://files.jeffgeerling.com/">{{< figure src="./vagrant-boxes-mm-files.png" alt="Vagrant Boxes - Midwestern Mac, LLC" width="600" height="223" >}}</a>

I've been using other base boxes in the past, but it's hard to find updated boxes (especially for newer OSes) from people or companies you can trust that are truly minimal base boxes (e.g. no extra configuration management tools or junk to kludge up my development environment!). These boxes are all minimal installs that let you bring your own configuration however you want; I typically use an Ansible playbook to build a <a href="https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/lamp">LAMP server</a>, or a <a href="https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/solr">Solr server</a>, or an <a href="https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/elk">ELK server</a> for monitoring all the other servers...

You can find all the info on the boxes (including links to the Packer/Ansible build configuration used to create the boxes) on <a href="http://files.jeffgeerling.com/">files.jeffgeerling.com</a>, and the boxes are also available on Vagrant Cloud: <a href="https://vagrantcloud.com/geerlingguy">geerlingguy's boxes</a>.

You can quickly build a Linux VM using Vagrant and VirtualBox for local Drupal development with <code>vagrant init geerlingguy/[boxname]</code> (e.g. for Ubuntu 14.04, <code>vagrant init geerlingguy/ubuntu1404</code>. These boxes are also used as the base boxes for the <a href="https://github.com/geerlingguy/drupal-dev-vm">Drupal Development VM</a> (which is currently being reworked to be much more powerful/flexible) and <a href="https://github.com/geerlingguy/acquia-cloud-vm">Acquia Cloud VM</a> (which simulates the Acquia Cloud environment locally).

I'll be writing more about local development with these VMs as well as many other interesting DevOps-related tidbits in <a href="https://leanpub.com/ansible-for-devops">Ansible for DevOps</a>, on this blog, and on the <a href="https://servercheck.in/blog">Server Check.in Blog</a>.
