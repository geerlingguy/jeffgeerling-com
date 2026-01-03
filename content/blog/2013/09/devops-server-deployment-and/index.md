---
nid: 2428
title: "DevOps, Server Deployment and Configuration Management"
slug: "devops-server-deployment-and"
date: 2013-09-19T13:01:35+00:00
drupal:
  nid: 2428
  path: /blogs/jeff-geerling/devops-server-deployment-and
  body_format: full_html
  redirects: []
tags:
  - ansible
  - chef
  - configuration management
  - deployment
  - devops
  - puppet
  - saltstack
  - servers
---

For the past few years, as the number of servers I manage has increased from a few to many, and the services I operate have required more flexibility in terms of adding and removing similarly-configured servers for different purposes, I've been testing different deployment and configuration management tools.

Many developers who are also sysadmins have progressed much the same way as I have, beginning by building everything by hand without documenting the process, then documenting the build with text files, and ultimately scripting builds with bash scripts. However, none of these techniques allow fast provisioning, continuous configuration management, or the flexibility required to make constantly-evolving applications adapt to the requirements of the day.

In recent years, 'DevOps' (better integration of development and operations) has become a hot buzzword and mantra of companies espousing agile development methodologies.

<h2 id="a-very-brief-and-woefully-inadequate-philosophy-of-devops">A Very Brief (and woefully inadequate) Philosophy of DevOps</h2>

<p style="text-align: center;">{{< figure src="./devops-define-roles.jpg" alt="Devops - fire meme" width="400" height="299" >}}
<em>Source: <a href="http://devops.com/2013/02/11/defining-the-dev-and-the-ops-roles-in-devops/">DevOps.com</a></p>

Servers, like instances of applications, should be managed via version-controlled configuration, and should be disposable (a common war cry: <a href="http://chadfowler.com/blog/2013/06/23/immutable-deployments/">Trash Your Servers and Burn Your Code</a>. If a server blows up, or if another few application servers are needed, they should be able to be provisioned or decommissioned in minutes, not hours (much less days or weeks!), and should be able to be provisioned and decommissioned automatically, without human intervention.

Using 'cloud' platforms with APIs for server management (like Amazon Web Services, VMWare vCloud, Rackspace, or Digital Ocean), a configuration management tool (like one of those mentioned below) can interact with the service to add, update, and remove servers. Additionally, individual developers should be able to perform their own server provisioning and management (at least in non-production environments).

DevOps also aims to reduce the friction between development teams and operations teams. Typically, if a deployment goes bad, or an application server falls over, the next few days are spent playing the blame game, trying to figure out who was at fault for the outage. If both the developers and operations personnel work together on server management and infrastructure, everybody shares the responsibility of SLAs and responsiveness.

<h2 id="configuration-management-and-deployment-tools">Configuration Management and Deployment Tools</h2>

The three tools below are the three that I see mentioned most often. I'd like to summarize a few characteristics of each, and a couple things that might sway you towards using one over the other. I've used all three, to a greater or lesser extent, and like aspects of each—but I don't have a universal preference of one over the other. Each one is a good fit in certain circumstances.

<strong><a href="http://www.opscode.com/chef/">Chef</a></strong> (by Opscode)
<ul>
<li>Uses plain-vanilla Ruby for configuration.</li>
<li>Built with Ruby.</li>
<li>Can be run via central server, or on local configured host with chef-solo.</li>
<li>Cookbook controls configuration.</li>
<li>Requires extra software installed on each individual managed server.</li>
</ul>

<strong>Short description</strong>: A ruby-based configuration management and server deployment tool. You define the configuration you want (as a 'cookbook'), and then deploy the configuration to a central chef server. Chef nodes (individual servers) then get the latest configuration changes and update themselves to match. Deploying new servers is as simple as building a basic server, installing chef, and pointing the server at the central chef server.

<strong><a href="http://puppetlabs.com/">Puppet</a></strong> (by Puppet Labs)
<ul>
<li>Uses Ruby + DSL for defining configuration.</li>
<li>Built with Ruby.</li>
<li>Needs a central 'puppet master' server to run (normally).</li>
<li>Manifest file controls configuration.</li>
<li>Requires extra software installed on each individual managed server.</li>
</ul>

<strong>Short description</strong>: Another ruby-based configuration management and server deployment tool. Puppet is very similar to Chef, but the syntax is a little different, since Puppet uses Ruby + a custom domain-specific language set (DSL), and some of the terminology is different. ('Puppet master' instead of 'central chef server', 'manifest' instead of 'cookbook', etc.). Puppet seems to be slightly more enterprise-y than Chef, in my eyes, but I haven't used it enough to judge it well.

<strong><a href="http://www.ansibleworks.com/">Ansible</a></strong> (by AnsibleWorks)
<ul>
<li>Uses YAML files for defining configuration.</li>
<li>Built with Python.</li>
<li>Run deployments and commands straight from your workstation ('push' deployment).</li>
<li>Playbooks define configuration.</li>
<li>Doesn't require extra software to be installed on individual servers.</li>
</ul>

<strong>Short description</strong>: Configuration is done in YAML, and deployments and changes use SSH, but can be orchestrated across many servers at once. Terminology is again different than other solutions ('playbooks' instead of 'cookbooks', etc.). By default, instead of individual servers polling for new configuration/updates, you push changes from a central location (your workstation). Ansible is usually easier to get up and running quickly (especially for smaller teams/server groups), but requires a little more responsibility from individual developers, who should have a good understanding of network security and SSH in general.

There are a few other interesting tools out there (like <strong><a href="http://saltstack.com/community.html">SaltStack</a></strong>, which is similar to Ansible but uses ZeroMQ instead of SSH for transport, meaning widespread deployments can be faster, but it takes a little more to set it up), but these three are the ones I've seen mentioned most often, and am testing for controlling my own infrastructure (currently seven servers, mostly LAMP-style or Node.js application servers).

One other question that is often asked, especially by people who are used to writing complex shell scripts to do deployments for a specific platform: <a href="http://serverfault.com/a/504089/15673">Why use Chef/Puppet over shell scripts?</a> - click the link for some good reasons.

<h2 id="local-provisioning-vagrant-and-virtualbox">Local Provisioning - Vagrant and VirtualBox</h2>

The three tools above were created to manage anywhere from a few to hundreds or thousands of servers (either virtual or physical), but they can also be used with local virtual machines, like those created through <a href="https://www.virtualbox.org/">VirtualBox</a> or another VM application. You can use them with <a href="http://www.vagrantup.com/">Vagrant</a> to easily build and destroy local sandbox VMs on your computer (or on certain services).

I built a Vagrant profile for local development that encapsulates the configuration of one of my live production servers and lets me easily deploy and rebuild instances of the server on my local computer for development and testing. I originally built the profile using shell scripts written specifically for CentOS/RHEL, but I'm working on rebuilding the profile using each of the tools above, just to see which one fits my workflow/mindset the best. So far I'm liking Ansible a lot, since I don't have too many servers to manage, and don't have a large team of developers to coordinate.

Vagrant has excellent documentation (complete with detailed examples to get you started) for <a href="http://docs.vagrantup.com/v2/provisioning/index.html">using different provisioning tools</a> to deploy new servers.

<h2 id="concluding-notes">Concluding Notes</h2>

As the number of servers managed by organizations has risen dramatically, and web applications have relied on multiple servers to serve ever-diversified needs, it has become increasingly important to automate the management of servers and infrastructure. Waiting hours or days for server provisioning interferes with development velocity, and it is not good practice to rely on a server administrator's memory or a text file with instructions to configure new servers.

Using configuration management tools like those listed above, and ensuring that servers are provisioned similarly in all environments ensures a more stable and reliable application. Additionally, it ensures that every stakeholder, from an individual developer to the end user, gets a similar experience while using an application.

More good reading:
<ul>
<li><a href="http://www.opsschool.org/en/latest/config_management.html">Configuration Management 101</a>.</li>
<li><a href="http://jjasghar.github.io/blog/2013/06/26/ansible-vs-chef-vs-puppet/">Ansible vs Chef vs Puppet</a></li>
<li><a href="http://devopsu.com/books/taste-test-puppet-chef-salt-stack-ansible.html">Taste Test: Puppet - Chef - Salt - Ansible</a></li>
<li><a href="http://devopsu.com/blog/ansible-vs-shell-scripts/">Shell Scripts vs. Ansible: Fight!</a></li>
</ul>
