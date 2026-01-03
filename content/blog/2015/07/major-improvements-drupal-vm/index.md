---
nid: 2499
title: "Major improvements to Drupal VM - PHP 7, MariaDB, Multi-OS"
slug: "major-improvements-drupal-vm"
date: 2015-07-03T13:17:03+00:00
drupal:
  nid: 2499
  path: /blogs/jeff-geerling/major-improvements-drupal-vm
  body_format: full_html
  redirects: []
tags:
  - development
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - github
  - vagrant
---

<p style="text-align: center;"><a href="http://www.drupalvm.com/">{{< figure src="./drupal-vm-header.png" alt="Drupal VM - Vagrant and Ansible Virtual Machine for Drupal Development" width="584" height="206" >}}</a></p>

For the past couple years, I've been building <a href="http://www.drupalvm.com/">Drupal VM</a> to be an extremely-tunable, highly-performant, super-simple development environment. Since MidCamp earlier this year, the project has really taken off, with almost <a href="https://github.com/geerlingguy/drupal-vm">200 stars on GitHub</a> and a ton of great contributions and ideas for improvement (some implemented, others rejected).

In the time since I wrote <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/developing-drupal-vagrant-and">Developing for Drupal with Vagrant and VMs</a>, I've focused on meeting <em>all</em> my defined criteria for the perfect local development environment. And now, I'm able to say that I use Drupal VM when developing all my projects—as it is now flexible and fast enough to emulate any production environment I use for various Drupal projects.

<h2>Easy PHP 7 testing with CentOS 7 and MariaDB</h2>

After a few weeks of work, Drupal VM now officially supports running PHP 7 (currently, 7.0.0 alpha 2) on CentOS 7 with MariaDB, or you can even tweak the settings to compile PHP from source yourself (<a href="https://galaxy.ansible.com/list#/roles/432">following to the PHP role's documentation</a>).

Doing this allows you to see how your own projects will fare when run with the latest (and fastest) version of PHP. Drupal 8 performance improves dramatically under PHP 7, and most other PHP applications will have similar gains.

Read <a href="https://github.com/geerlingguy/drupal-vm/wiki/PHP-7-on-Drupal-VM">PHP 7 on Drupal VM</a> for more information.

<h2>Other major improvements and features</h2>

Here are some of the other main features that have recently been added or improved:

<ul>
<li><strong>Flexible database support</strong>: MySQL, MariaDB, or (soon) Percona are all supported out of the box, pretty easily. See guide for <a href="https://github.com/geerlingguy/drupal-vm/wiki/Use-MariaDB-instead-of-MySQL">Use MariaDB instead of MySQL</a>.</li>
<li><strong>Flexible OS support</strong>: Drupal VM officially supports Ubuntu 14.04, Ubuntu 12.04, CentOS 7, or CentOS 6 out of the box; other OSes like RHEL, Fedora, Arch and Debian may also work, but are not supported. See: <a href="https://github.com/geerlingguy/drupal-vm/wiki/Using-Different-Base-OSes">Using different base OSes</a>.</li>
<li><strong>Use with any Drupal deployment methodology</strong> — works with any dev workflow, including <a href="https://github.com/geerlingguy/drupal-vm/wiki/Drush-Make-file">Drush make files</a>, <a href="https://github.com/geerlingguy/drupal-vm/wiki/Local-Drupal-codebase">local Drupal codebases</a>, and <a href="https://github.com/geerlingguy/drupal-vm/wiki/Drupal-multisite">multisite installations</a>.</li>
<li><strong>Automatic local drush alias configuration</strong></li>
<li><strong>'Batteries included'</strong> — developer utilities and essentials like Varnish, Solr, MailHog, XHProf are easy to enable or disable.</li>
<li><strong>Production-ready, security-hardened</strong> configuration you can install on DigitalOcean</li>
<li><strong>Thoroughly-documented</strong> — check out the <a href="https://github.com/geerlingguy/drupal-vm/wiki">Drupal VM Wiki</a> on GitHub</li>
<li><strong>First class support for any host OS</strong> — Mac, Linux or Windows</li>
<li><strong>Drupal version agnostic</strong> — works great with 6, 7, or 8.</li>
<li><strong>Easy configuration</strong> of thousands of parameters (powered by a few dozen component-specific Ansible roles) through the <code>config.yml</code> file.</li>
</ul>

I'd especially like to thank the dozens of people who have filed issues against the project to add needed functionality or fix bugs (especially for multi-platform, multi-database support!), and have helped improve Drupal VM through over 130 issues and 17 pull requests.

There are <a href="https://www.drupal.org/node/2232049">dozens</a> of other VM-based or Docker/container-based local development solutions out there, and Drupal VM is one of many, but I think that—even if you don't end up using it for your own work—you will find sound ideas and best practices in environment configuration in the project.
