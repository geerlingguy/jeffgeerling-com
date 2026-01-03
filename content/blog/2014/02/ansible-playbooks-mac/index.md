---
nid: 2446
title: "Ansible Playbooks for Drupal 8 Testing and Mac Dev"
slug: "ansible-playbooks-mac"
date: 2014-02-14T17:15:44+00:00
drupal:
  nid: 2446
  path: /blogs/jeff-geerling/ansible-playbooks-mac
  body_format: full_html
  redirects: []
tags:
  - ansible
  - drupal
  - drupal 8
  - drupal planet
  - mac
  - mac os x
  - provisioning
---

Lately, I've been working a lot with <a href="http://www.ansible.com/">Ansible</a>, a simple but powerful infrastructure management platform. I now use Ansible playbooks and ad-hoc commands to manage all of Midwestern Mac's infrastructure (this site, <a href="http://hostedapachesolr.com/">Hosted Apache Solr</a>, <a href="https://servercheck.in/">Server Check.in</a>, and many ancillary servers), and as a result, I've started using Ansible for pretty much any kind of work I need to do in development—including configuring my own Mac, and developing with Drupal 8.

<h2>Meet Ansible</h2>

<p style="text-align: center;">{{< figure src="./ansible-logo-black.png" alt="Ansible Logo - Black transparent" width="400" height="57" >}}</p>

For those who haven't heard of Ansible before, it's often described as being a little like Puppet or Chef, used for configuration management. You define the configuration of a server, and Ansible makes sure the server is configured as defined. But Ansible goes quite a bit further—it's also great for deploying applications (especially in tandem with tools like Jenkins), running commands on servers, and day-to-day management of a few, hundreds, or even thousands, of servers—it's an end-to-end configuration management tool. Ansible also has a great, and rapidly-growing <a href="https://github.com/ansible/ansible/blob/devel/CONTRIBUTING.md">community</a>, building it up and making it markedly better every release.

Ansible uses YAML to define configuration (<em>just like Drupal 8!</em>), and is relatively easy to pick up, especially if you already have some experience on the command line. You can read more about it in a book I'm writing, <a href="https://leanpub.com/ansible-for-devops">Ansible for DevOps</a>, and hopefully, I'll be able to tell you more about Ansible <em>in person</em> at DrupalCon Austin—I've submitted a session titled <a href="https://austin2014.drupal.org/session/devops-humans-ansible-drupal-deployment-victory">DevOps for Humans: Ansible for Drupal Deployment Victory!</a> (please leave a comment and let me know what you want to hear!).

<h2>Drupal development VM (Vagrant + Ansible)</h2>

I used to use MAMP (a simple-to-install Apache + MySQL + PHP setup for Macs) for all my development, which made adding virtual hosts to Apache relatively simple. However, there are many downsides to developing with MAMP—I could never configure things like drush, APC, the version of PHP, MySQL, or auxiliary tools like XDebug and Solr, <em>exactly</em> how I wanted or needed them.

A couple years ago, I started using virtual machines, built using <a href="http://www.vagrantup.com/">Vagrant</a> and a bunch of shell scripts, to work more like I wanted them, and more like the real servers where I run the code I'm developing. However, this setup was never very satisfactory; building the VM was always a bit hit-or-miss, because the shell scripts were a bit cumbersome and hard to make as flexible as I wanted them.

I finally had time to build a quick-and-dirty (but very simple, and much more flexible!) <a href="https://github.com/geerlingguy/drupal-dev-vm">Drupal 8 development VM</a>. Not only that—I can tweak a variable (either via the command line, or in the vars.yml file) and get Drupal 6, 7, or 8, fully installed, on a fresh new Ubuntu linux VM.

The whole process of building a fresh instance of Drupal 6, 7, or 8 takes only a few minutes, and is great for testing patches or module development.

Clone the <a href="https://github.com/geerlingguy/drupal-dev-vm">Simple Drupal Development VM</a> and modify to suit your taste—the included README file shows you how to get started.

<h2>Mac Development Playbook</h2>

Many people have started sharing their <a href="http://dotfiles.github.io/">dotfiles</a>—their system's little configuration files—as well as elaborate shell scripts to provision their own workstations. There's even a nice new Ansible-powered configuration that aims to be flexible enough to set up anyone's Mac called <a href="http://spencer.gibb.us/blog/2014/02/03/introducing-battleschool/">Battleschool</a>.

Because I just got a new Mac for work, and didn't want to do my normal "restore from Time Machine then delete the stuff I don't need", I decided to wrap as much of the initial configuration in Ansible as I could. The result? My <a href="https://github.com/geerlingguy/mac-dev-playbook">Mac Development Ansible Playbook</a>. This project is a set of playbooks which install and configure most of the software I use for my web and app development. See the README for more info.

The great thing about this setup? It took only a little bit longer to build this Ansible configuration than it did to do the configuration by hand (seriously—I did all this in less than a day!), and it takes all of 10 minutes (mostly constrained by your Internet connection) to set up a brand new Mac for my web development needs—with every little setting and app in place.

<h2>Summary</h2>

To summarize:

<ul>
<li><a href="http://www.ansible.com/">Ansible</a> rocks. It's configuration management (and more!) for normal human beings.</li>
<li>I'm writing <a href="https://leanpub.com/ansible-for-devops">a book on Ansible</a>. It'll be on sale soon... sign up to get a copy!</li>
<li>I've posted a bunch of Ansible playbooks on GitHub:
<ul>
<li><a href="https://github.com/geerlingguy/drupal-dev-vm">Simple Drupal Development VM</a></li>
<li><a href="https://github.com/geerlingguy/mac-dev-playbook">Mac Development Ansible Playbook</a></li>
<li><a href="https://github.com/geerlingguy/nodejs-dev-vm">Simple Node.js Development VM</a></li>
<li>More to come...</li>
</ul></li>
</ul>

I'm working on a bunch of other Ansible + Vagrant configurations, so follow me on <a href="https://github.com/geerlingguy">GitHub</a> and <a href="https://twitter.com/geerlingguy">Twitter</a> to see the latest; I get to do some pretty fun and crazy things in the process of writing <a href="https://leanpub.com/ansible-for-devops">Ansible for DevOps</a>, and I love sharing everything I learn!
