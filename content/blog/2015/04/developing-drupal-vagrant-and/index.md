---
nid: 2493
title: "Developing for Drupal with Vagrant and VMs"
slug: "developing-drupal-vagrant-and"
date: 2015-04-29T14:21:36+00:00
drupal:
  nid: 2493
  path: /blogs/jeff-geerling/developing-drupal-vagrant-and
  body_format: full_html
  redirects: []
tags:
  - development
  - drupal
  - drupal planet
  - drupal vm
  - vagrant
  - virtualbox
  - virtualization
  - vmware
---

<p>Many blog posts have outlined the <a href="http://www.mediacurrent.com/blog/better-local-development-vagrant">benefits of using VMs</a> (Virtual Machines) for local Drupal development instead of either using native PHP and Apache, or a bundled environment like MAMP, XAMPP, or Acquia Dev Desktop. The advantages of using virtualization (usually managed by Vagrant) are numerous, but in certain cases, you can make a good argument for sticking with the traditional solutions.</p>

<p>If you'd like to take the dive and start using virtualized development environments, or if you're already using Vagrant and VirtualBox or some other VM environment (e.g. VMWare Fusion or Parallels Desktop), how do you optimize local development, and which pre-bundled Drupal development VM will be best for <em>you</em> and <em>your team</em>?</p>

<h2>
<a id="user-content-criteria-for-the-perfect-local-development-environment" class="anchor" href="#criteria-for-the-perfect-local-development-environment" aria-hidden="true"><span class="octicon octicon-link"></span></a>Criteria for the Perfect Local Development Environment</h2>

<p>These are the criteria I use when judging solutions for local Drupal development (whether virtualized or traditional):</p>

<ul>
<li>Should be <strong>simple</strong> and easy to set up</li>
<li>Should be <strong>fast</strong> by default</li>
<li>Should be <strong>flexible</strong>:

<ul>
<li>Should work with multiple providers; VirtualBox is free, but VMWare can be much faster!</li>
<li>Should allow configuration of the PHP version.</li>
<li>Should work with your preferred development workflow (e.g. drush, makefiles, manual database sync, etc.)</li>
<li>Should prevent filesystem friction (e.g. permissions issues, slow file access speeds, etc.)</li>
<li>Shouldn't have hardcoded defaults</li>
</ul>
</li>
<li>Should be <strong>complete</strong>:

<ul>
<li>Should work without requiring a bunch of extra plugins or 3rd party tools</li>
<li>No extra languages or libraries should be required (why install Ruby gems, npm modules, etc. unless you need them for your particular project?)</li>
</ul>
</li>
<li>Should be Free and Open Source</li>
<li>Should include all the tools you need, but allow you to disable whatever you don't need (e.g. XHProf, Apache Solr, etc.)</li>
<li>Should work on Windows, Mac, and Linux with minimal or no adjustment</li>
<li>Should be deployable to production (so your local dev environment matches prod <em>exactly</em>)</li>
</ul>

<p>A lot of these points may have more or less importance to a particular team or individual developer. If you're a die-hard Mac user and don't ever work with any developers on Windows or Linux, you don't need to worry about Windows support. But some of these points apply to everyone, like being <em>fast</em>, <em>simple</em>, and <em>flexible</em>.</p>

<p>If you're looking for a way to improve team-based Drupal development, all these bullet points apply. If your entire team is going to standardize on something, you should standardize on something that gives everyone the standard layout that's required, but the flexibility to work with each developer's environment and preferred development tools.</p>

<h2>
<a id="user-content-announcing-drupal-vm" class="anchor" href="#announcing-drupal-vm" aria-hidden="true"><span class="octicon octicon-link"></span></a>Announcing Drupal VM</h2>

<p>I built <a href="http://www.drupalvm.com/">Drupal VM</a> over the past two years for my local Drupal development needs, and continue to improve it so it meets all the above criteria.</p>

<p>Drupal VM is a local development environment that works with a variety of Drupal site development workflows with minimal friction. Whether a site is built via drush makefiles, uses a 'codebase-in-a-git-repo' approach, or is built with install profiles and drush commands, it works with Drupal VM. Drupal VM also includes all the tools I need in my day-to-day development, and even installs helpful software like Apache Solr, Memcache, and MailHog.</p>

<p>Another common scenario I have as a contrib module maintainer and core contributor is my need for a quick, fresh Drupal environment where I can run Drupal 8, 7 or 6 HEAD and hack on core or one of my contrib modules (like <a href="https://www.drupal.org/project/honeypot">Honeypot</a>). Drupal VM is preconfigured to install a fresh copy of Drupal 8 for local hacking, but it's easy to configure it to run whatever Drupal site and configuration you like!</p>

<p>Since Drupal VM has been helpful to other developers, I've made it more flexible, built a simple marketing page (at <a href="http://www.drupalvm.com/">www.drupalvm.com</a>), and polished up the documentation on the <a href="https://github.com/geerlingguy/drupal-vm/wiki">Drupal VM Wiki</a>. I'm continuing to improve Drupal VM as I get time, adding features like:</p>

<ul>
<li>Ability to choose between Nginx and Apache for the webserver.</li>
<li>Ability to deploy to DigitalOcean, Linode, or AWS with the same (but security-hardened) configuration as your local environment.</li>
<li>Ability to add Varnish or Nginx as a reverse-proxy cache.</li>
</ul>

<p>Drupal VM has also been a fun project to work on while writing <a href="http://ansiblefordevops.com/">Ansible for DevOps</a>. My work on Drupal VM allows me to flex some Ansible muscle and work on a large number of Ansible Galaxy roles (like <a href="https://galaxy.ansible.com/list#/roles/432"><code>geerlingguy.php</code></a> and <a href="https://galaxy.ansible.com/list#/roles/445"><code>geerlingguy.solr</code></a>) that are used by Drupal VM—in addition to hundreds of other projects not related to Drupal!</p>

<h2>
<a id="user-content-a-vm-for-everyone" class="anchor" href="#a-vm-for-everyone" aria-hidden="true"><span class="octicon octicon-link"></span></a>A VM for Everyone</h2>

<p>Drupal VM is my weapon of choice... but there are many great projects with similar features:</p>

<ul>
<li>
<a href="http://www.drupalvm.com">Drupal VM</a> (Vagrant + Ansible)</li>
<li>
<a href="https://www.drupal.org/project/vdd">Vagrant Drupal Development</a> (Vagrant + Chef)</li>
<li>
<a href="https://github.com/hashbangcode/vlad">Vlad</a> (Vagrant + Ansible)</li>
<li>
<a href="http://www.vampd.io/">Vampd</a> (Vagrant + Chef)</li>
<li>
<a href="https://github.com/eaton/vagrant-chef-dlamp">Vagrant Chef Dlamp</a> (Vagrant + Chef)</li>
<li>
<a href="http://www.kalamuna.com/products/kalabox/">Kalabox</a> (Vagrant + Containers)</li>
<li>
<a href="https://github.com/gman29/varying-drupal-vagrants">Varying Drupal Vagrants</a> (Vagrant + Shell Scripts)</li>
<li>
<a href="https://www.drupal.org/project/vm">Virtual Machine</a> (Vagrant + Puppet)</li>
<li>
<a href="https://github.com/NBCUTechnology/pubstack">Pubstack</a> (Vagrant + Ansible)</li>
<li>
<a href="https://www.drupal.org/project/aegir_up">Aegir-up</a> (Vagrant + Aegir)</li>
<li>
<a href="http://phansible.com/">Phansible</a> or <a href="https://puphpet.com/">PuPHPet</a> (build-your-own VM, not Drupal-specific)</li>
<li>Others listed in the issue <a href="https://www.drupal.org/node/2232049">Get Vagrant D8 VM ready for Drupal 8 mentoring</a>
</li>
</ul>

<p>Alternatively, if you know how to use Puppet, Chef, Ansible, or SaltStack, and want to fork and develop your own alternative dev environment, or build one on your own, that's always an option! Especially if you have a highly specialized production environment, it may be best to reflect that environment with a more specialized local development environment.</p>

<h2>
<a id="user-content-on-docker-and-lxclxc-container-based-environments" class="anchor" href="#on-docker-and-lxclxc-container-based-environments" aria-hidden="true"><span class="octicon octicon-link"></span></a>On Docker and LXC/LXC (Container-based environments)</h2>

<p>Before I wrap up, I wanted to also specifically call out some projects like <a href="http://drocker.io/">Drocker</a> and the next-generation Drupal.org testbot infrastructure project, <a href="https://www.drupal.org/project/drupalci_testbot">DrupalCI</a>, both of which are using Docker containers for local development. Containerized development environments offer many of the same benefits of virtualization, but can be faster to build and rebuild, and easier to maintain.</p>

<p>Container-based infrastructure is likely going to become standard in the next 5-10 years (much like VM-based infrastructure has become standard in the past 5-10 years)—whether with Docker or some other standard format/methodology (a container's just a container!).</p>

<p>Many hosting platforms use a container-everywhere approach, like:</p>

<ul>
<li>Platform.sh</li>
<li>Pantheon</li>
<li>Google Container Engine</li>
<li>Amazon EC2 Container Service</li>
</ul>

<p>However, I caution that container-based development has it's own complexities, especially in production—especially with more complicated web applications like Drupal. I also caution against blindly running other people's pre-built container images in production; you should build them and manage them on your own (just like I build and manage my own VM images using Packer, e.g. <a href="https://github.com/geerlingguy/packer-ubuntu-1404">packer-ubuntu-1404</a>).</p>

<h2>
<a id="user-content-in-summary" class="anchor" href="#in-summary" aria-hidden="true"><span class="octicon octicon-link"></span></a>In Summary</h2>

<p>In short, I've been working on <a href="http://www.drupalvm.com/">Drupal VM</a> for the past couple years, and I've made it flexible enough for the variety of Drupal sites I work on. I hope it's flexible enough for your development needs, and if not, <a href="https://github.com/geerlingguy/drupal-vm/issues">open an issue</a> and I'll see what I can do!</p>
