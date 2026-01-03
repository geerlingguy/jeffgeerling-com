---
nid: 2587
title: "Easily manage Apache VirtualHosts with Ansible and Jinja2"
slug: "apache-virtualhosts-with-ansible-and-jinja2"
date: 2013-12-16T04:16:11+00:00
drupal:
  nid: 2587
  path: /blog/apache-virtualhosts-with-ansible-and-jinja2
  body_format: full_html
  redirects:
    - /blog/easily-manage-multiple-apache-virtualhost
    - /blog/easily-manage-apache-virtualhosts-ansible-and
aliases:
  - /blog/easily-manage-multiple-apache-virtualhost
  - /blog/easily-manage-apache-virtualhosts-ansible-and
tags:
  - ansible
  - ansible for devops
  - apache
  - automation
  - infrastructure
  - jinja2
  - virtualhosts
---

Server Check.in's entire infrastructure is managed via <a href="http://www.ansibleworks.com/">Ansible</a>, which has helped tremendously as the service has grown from one to many servers.

<p style="text-align: center;">{{< figure src="./ansible-borg-cow.jpg" alt="Ansible Borg Cow" width="400" height="292" >}}<br />
<a href="http://cowsay.morecode.org/">cowsay</a> and Ansible were <a href="https://coderwall.com/p/uzy0yw">made for each other</a>.</p>

One pain point with running Apache servers that host more than one website (using <a href="http://httpd.apache.org/docs/2.2/vhosts/name-based.html">name-based virtual hosts</a>) is that the virtual host configuration files quickly get unwieldy, as you have to define the entire <code><VirtualHost /></code> for every domain you have on the server, and besides Apache's <a href="https://httpd.apache.org/docs/trunk/mod/mod_macro.html">mod_macro</a>, there's no easy way to define a simple structured array of information and have the vhost definitions built from that.

In my case, for ease of generic local development, I have one Vagrant/Ansible profile that installs MySQL, Apache, PHP, Node.js, and a few other tools for local development, and I originally included a barebones <code>vhosts.conf</code> file that was included by the main <code>httpd.conf</code> file Apache used.

The file looked something like this:

```
NameVirtualHost *:80

<VirtualHost *:80>
  ServerName www.domain.tld
  DocumentRoot /www/domain
  [more rules...]
</VirtualHost>

<VirtualHost *:80>
  ServerName www.otherdomain.tld
  DocumentRoot /www/otherdomain
  [more rules...] 
</VirtualHost>

[more definitions here...]
```

However, this file grows over time into an unmanageable mess, as I've had more than 20 vhosts at times. (Aside: I could avoid this mess by working on sites individually with different Vagrant/Ansible profiles per instance, but when I'm doing generic work on a normal LAMP stack, I like having one main VM that has all the tools installed (mostly so I don't have to keep booting and halting VMs and loading up my small SSD with a bunch of VMs)).

Ansible and it's built-in integration with the <a href="http://jinja.pocoo.org/docs/">Jinja2</a> templating system makes managing virtual hosts (and other files where you might have a lot of repeated boilerplate with different variables) simple.

As a simple example (without many options for the virtual hosts), here's all I had to do to make Ansible and Jinja do the heavy lifting for me:

<strong>1. Add <code>.j2</code> to the end of my <code>vhosts.conf</code> file to indicate that it's a Jinja2 template.</strong>

<strong>2. Modify the vhosts.conf.j2 template so instead of listing all the virtual hosts, it just has one definition inside a <code>for</code> loop</strong>, like so:

```
NameVirtualHost *:80

{% for vhost in apache_vhosts %}
<VirtualHost *:80>
  ServerName {{ vhost.servername }}
  DocumentRoot {{ vhost.documentroot }}
{% if vhost.serveradmin is defined %}
  ServerAdmin {{ vhost.serveradmin }}
{% endif %}
  <Directory "{{ vhost.documentroot }}">
    AllowOverride All
    Options -Indexes FollowSymLinks
    Order allow,deny
    Allow from all
  </Directory>
</VirtualHost>

{% endfor %}
```

(The extra space before the endfor is to allow for a space between each vhost entry, and the if clause is indented as such to prevent the following line from being indented an extra space).

<strong>3. Define the <code>apache_vhosts</code> variable inside your playbook, or via an included playbook, or via any other supported Ansible variable definition method</strong>, for example:

```
vars:
  apache_vhosts:
    - {servername: "www.domain.tld", documentroot: "/www/domain"}
    - {servername: "www.otherdomain.tld", documentroot: "/www/otherdomain", serveradmin: "webmaster@otherdomain.tld"}
```

I've taken to using Ansible for even the simplest of server configurations, even for one-off servers (like a master monitoring server), as it not only codifies every bit of configuration, it also makes changes, additions, and redeployments so much easier and faster!

I tried my hand at Puppet and Chef, and thought about using SaltStack for a while, but Ansible has been so much easier to grok (not to mention deploy—there's no extra software to install on my servers!), and can do everything I've thrown at it so far. Expect more on how Server Check.in is using Ansible in the future!
