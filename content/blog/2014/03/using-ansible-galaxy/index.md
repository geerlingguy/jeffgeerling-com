---
nid: 2610
title: "Using Ansible Galaxy"
slug: "using-ansible-galaxy"
date: 2014-03-13T03:32:08+00:00
drupal:
  nid: 2610
  path: /blog/using-ansible-galaxy
  body_format: full_html
  redirects: []
tags:
  - ansible
  - ansible for devops
  - ansible galaxy
  - automation
  - infrastructure
  - roles
aliases:
  - /blog/using-ansible-galaxy
---

<blockquote><strong>2020 Update</strong>: This article is still as relevant as ever, though Galaxy now has <em>tens of thousands of roles</em> and also has 'Collections' now, which can include plugins, modules, and roles! If you want to learn the latest about all this stuff, check out my fully updated <a href="https://www.ansiblefordevops.com">Ansible for DevOps</a>, now in it's 2nd edition! It has two chapters covering roles and collections on Ansible Galaxy.</blockquote>

<p style="text-align: center;"><a href="https://galaxy.ansible.com/">{{< figure src="./ansible-galaxy.png" alt="Ansible Galaxy Logo" width="600" height="135" >}}</a></p>

<p><a href="https://galaxy.ansible.com/">Ansible Galaxy</a> was <a href="http://www.ansible.com/blog/2013/12/19/ansibleworks-galaxy-is-now-available">launched</a> just a few short months ago, and already has over 500 roles maintained by over 225 users. The idea behind Galaxy is to give greater visibility to one of Ansible's most exciting features: reusable Roles for server configuration or application installation.</p>

<p>Galaxy is still in beta, and likely will be for a while longer, but if you have Ansible 1.4.2 or later installed, you can use the <code>ansible-galaxy</code> command to get started.</p>

You may not know the power of Ansible Galaxy (or, indeed, Ansible Roles, which have been around since 1.2, and were greatly improved in 1.3+) until you've had a little taste of what it has to offer. In this post, I'd like to highlight how to get started using <code>ansible-galaxy</code> in particular, and how you can put together fully-featured servers with roles like lego blocks, and very few lines of YAML.</p>

<p>The topic of this post is greatly expanded in <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>, a book I wrote on Ansible.</p>

<h2>
<a name="getting-roles-from-galaxy" class="anchor" href="#getting-roles-from-galaxy"><span class="octicon octicon-link"></span></a>Getting roles from Galaxy</h2>

<p>One of the primary functions of the <code>ansible-galaxy</code> command is retrieving roles from the Galaxy. Roles must be downloaded before they can be used in playbooks[1].</p>

<p>I'd like to build a quick LAMP server to test some newfangled PHP script I wrote with one big 800 line function. So, I'll just do the following:</p>


```
$ ansible-galaxy install geerlingguy.apache geerlingguy.mysql geerlingguy.php
```

<p>The latest version will be downloaded if no version is specified. To specify a version, add the version after the role name[2]:</p>


```
$ ansible-galaxy install geerlingguy.apache,1.0.0 geerlingguy.mysql,1.0.0 geerlingguy.php,1.0.0
```

<h2>
<a name="a-lamp-server-in-six-lines-of-yaml" class="anchor" href="#a-lamp-server-in-seven-lines-of-yaml"><span class="octicon octicon-link"></span></a>A LAMP server in seven lines of YAML</h2>

<p>Now that we have these roles installed (Apache, MySQL, and PHP), we can quickly create a LAMP server. This example assumes you already have a CentOS-based linux VM or server booted and can connect to it or run Ansible as a provisioner via Vagrant on it:</p>

<p>1. Create an Ansible playbook named <code>lamp.yml</code> with the following contents:</p>


```
---
- hosts: all
  roles:
  - geerlingguy.mysql
  - geerlingguy.apache
  - geerlingguy.php
  - geerlingguy.php-mysql
```

<p>2. Run the playbook against a host:</p>


```
$ ansible-playbook -i path/to/custom-inventory lamp.yml
```

<p>Boom. LAMP server.</p>

<h2>
<a name="a-solr-server-in-six-lines-of-yaml" class="anchor" href="#a-solr-server-in-six-lines-of-yaml"><span class="octicon octicon-link"></span></a>A Solr server in six lines of YAML</h2>

<p>Let's grab a few more roles so we can build a Solr search server.</p>


```
$ ansible-galaxy install geerlingguy.java geerlingguy.tomcat6 geerlingguy.solr
```

<p>Then create a playbook named <code>solr.yml</code> with the following contents:</p>


```
---
- hosts: all
  roles:
    - geerlingguy.java
    - geerlingguy.tomcat6
    - geerlingguy.solr
```

<p>Boom. Solr server.</p>

<p>I think you might get the point. Now, I could've easily left out the <code>java</code> and <code>tomcat6</code> roles, since they'll be automatically picked up during installation of the <code>geerlingguy.solr</code> role. Additionally, each of these roles has a good deal of customizability in the form of variables. And obviously, you'll need to do more configuration (like securing the server, setting up user accounts, etc.), but I'm even working on flexible roles for <em>that</em>, too, like my <a href="https://galaxy.ansible.com/list#/roles/451">firewall</a> role for any Linux OS using iptables.</p>

<p>The roles' pages on the Ansible Galaxy website highlight the available variables for setting things like what version of Solr to install, where to install it, etc. (for example: <a href="https://galaxy.ansible.com/list#/roles/445">geerlingguy.solr Galaxy page</a>).</p>

<p>I've been abstracting all my playbooks for the infrastructure I manage into distinct application-related roles, and doing so has allowed me to have a set of around 30 roles (most of which have been uploaded to Galaxy: <a href="https://galaxy.ansible.com/geerlingguy/">geerlingguy's roles on Ansible Galaxy</a>) I can use to build a <em>very</em> wide variety of servers. Instead of having to maintain lengthy playbooks unique to each server, I can just build a list of the required roles, and a few variables that set up the servers with the proper versions and paths. Each server is defined in a few simple lines of YAML.</p>

<p>As I said... Boom!</p>

<h2>
<a name="other-helpful-galaxy-commands" class="anchor" href="#other-helpful-galaxy-commands"><span class="octicon octicon-link"></span></a>Other Helpful Galaxy commands</h2>

<p>Some other helpful <code>ansible-galaxy</code> commands you might use from time to time:</p>

<ul>
<li>
<code>ansible-galaxy list</code> displays a list of installed roles, with version numbers</li>
<li>
<code>ansible-galaxy remove [role]</code> removes an installed role</li>
<li>
<code>ansible-galaxy info</code> (hmm... not sure what this does?)</li>
<li>
<code>ansible-galaxy init</code> can be used to create a role template suitable for submission to Ansible Galaxy</li>
</ul><p>Additionally, you can configure the default path where Ansible roles will be downloaded by editing your <code>ansible.cfg</code> configuration file (normally located in <code>/etc/ansible/ansible.cfg</code>), and setting a <code>roles_path</code> in the <code>[defaults]</code> section.</p>

<h2>
<a name="room-for-improvements" class="anchor" href="#room-for-improvements"><span class="octicon octicon-link"></span></a>Room for improvements</h2>

<p>Even with all the great utility Ansible Galaxy provides, there are a few things I think could be improved:</p>

<ol>
<li>For contributors, some parts of the process aren't immediately obvious, like whether roles on Galaxy will automatically refresh (and if so, how often) when changes are pushed to GitHub.</li>
<li>When searching for roles, it's currently impossible to filter results by distro or OS version; if you have a CentOS server, and most of the results are for Ubuntu, it can make the process of finding a role to use difficult.</li>
<li>The <code>ansible-galaxy</code> command's documentation isn't incredibly obvious or clear, but it's been improving :)</li>
<li>There is currently no way to simply update a role (to my knowledge); you'd have to remove the role then download a new copy with the proper version.</li>
</ol><p>All of these complaints are borderline trivial, and since Galaxy is still in beta status, I expect they'll be worked out in due time (indeed, I hope to help with the process!).</p>

<p>All in all, I'm very impressed with Ansible Galaxy as it exists today, and I hope you can start using it to accelerate your infrastructure development! If nothing else, spinning up quick servers to try out new apps or other packages listed in Galaxy can be an enlightening process.</p>

<p><em>If you'd like to learn how Ansible can help you manage your infrastructure, and are either new to Ansible or already using Ansible, you can purchase my book, Ansible for DevOps, on <a href="https://leanpub.com/ansible-for-devops">LeanPub</a>, <a href="http://www.amazon.com/Ansible-DevOps-Server-configuration-management-ebook/dp/B016G55NOU/">Amazon</a>, or <a href="https://itunes.apple.com/us/book/ansible-for-devops/id1050383787?ls=1&mt=11">iTunes</a></em>.</p>

<p>[1] Note that, as of this writing, downloading a single role will not necessarily download all its dependencies (though a <code>--no-deps</code> option seems to imply this would be the expected behavior). Nor will running a playbook referencing an external role automatically download the role. You will need to run <code>ansible-galaxy install</code> for each role you need.</p>

<p>[2] There's no way (at least not that I know of) to get the master/HEAD release from GitHub after a version has been tagged. I tried <code>master</code>, <code>HEAD</code>, and <code>head</code>, but those resulted in errors. It would be awesome if we could specify head, or even a specific commit, when downloading roles. Versions cover more than 99% of use-cases, though, so I'm not going to complain loudly :)</p>
