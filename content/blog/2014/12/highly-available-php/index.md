---
nid: 2477
title: "Highly-Available PHP infrastructure with Ansible"
slug: "highly-available-php"
date: 2014-12-15T16:03:57+00:00
drupal:
  nid: 2477
  path: /blogs/jeff-geerling/highly-available-php
  body_format: full_html
  redirects: []
tags:
  - ansible
  - apache
  - drupal
  - drupal planet
  - ha
  - infrastructure
  - memcached
  - mysql
  - php
  - varnish
---

I just posted a large excerpt from <a href="http://ansiblefordevops.com/">Ansible for DevOps</a> over on the Server Check.in blog: <a href="https://servercheck.in/blog/highly-available-infrastructure-provisioning-ansible">Highly-Available Infrastructure Provisioning and Configuration with Ansible</a>. In it, I describe a simple set of playbooks that configures a highly-available infrastructure primarily for PHP-based websites and web applications, using Varnish, Apache, Memcached, and MySQL, each configured in a way optimal for high-traffic and highly-available sites.

Here's a diagram of the ultimate infrastructure being built:

<p style="text-align: center;">{{< figure src="./8-highly-available-infrastructure.png" alt="Highly Available Infrastructure" width="450" height="562" >}}</p>

The configuration is similar to what many larger Drupal sites would use, and with the exception of the varnish <code>default.vcl</code> and the actual PHP script being deployed (in the example, it's just a PHP file that tests the rest of the infrastructure and outputs success/fail statuses), you could drop a Drupal site on the Apache servers and immediately start scaling up your traffic!

The example highlights the powerful simplicity of Ansible as a tool for not only configuration management (like Puppet, Chef, etc.), but also for provisioning and managing servers in different cloud providers. With under a hundred lines of YAML configuration, I can spin up the exact same infrastructure locally with Vagrant and VirtualBox, on DigitalOcean droplets, or on AWS EC2 instances!
