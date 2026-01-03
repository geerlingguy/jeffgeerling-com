---
nid: 2523
title: "Checklist for Setting up a CentOS 6 LAMP Server"
slug: "checklist-setting-centos-lamp"
date: 2012-09-19T20:47:12+00:00
drupal:
  nid: 2523
  path: /blogs/jeff-geerling/checklist-setting-centos-lamp
  body_format: full_html
  redirects: []
tags:
  - config
  - lamp
  - linode
  - server
  - tutorial
---

I have to set up a new LAMP server for different clients here and there, but not with enough frequency to warrant using a particular scripted solution or 'stack' from a particular hosting company. Plus, I like to have a portable solution that is flexible to the needs (and constraints) of a client's website.

<blockquote>
<strong>Note on hosting providers</strong>: For hosting, I've used a <em>very wide</em> variety of hosts. I typically use and recommend <a href="http://www.hotdrupal.com/drupal-vps-plans">Hot Drupal VPSes</a> or <a href="http://www.linode.com/?r=dca78b4b11124cbcb5aee9b46c3055ca6379018a">Linode VPSes</a> [affiliate link] running CentOS for a good LAMP server. Shared servers are only good for nonessential or low-traffic sites, but they are a bit cheaper and easier to use for simpler needs!
</blockquote>

So, here's a typical step-by-step process for how I set up a CentOS 6 (similar process for CentOS 5) server for LAMP (Linux, Apache, MySQL, and PHP), often for low-to-moderate Drupal sites (one or many):

<ol>
	<li>Set the server's hostname (<a href="http://library.linode.com/getting-started#sph_setting-the-hostname">guide</a>).</li>
	<li>Set the server's timezone (<a href="http://library.linode.com/getting-started#sph_setting-the-timezone">guide</a>).</li>
	<li>Install any existing updates using yum update (<a href="http://library.linode.com/getting-started#sph_installing-software-updates">guide</a>).</li>
	<li>Security: Add a non-root admin user, disable SSH password and root login (<a href="http://library.linode.com/securing-your-server">guide</a>).</li>
	<li>Create a firewall for the server (<a href="http://library.linode.com/securing-your-server#sph_creating-a-firewall">guide</a>).</li>
	<li>Enable the REMI/EPEL repos (<a href="http://www.rackspace.com/knowledge_center/article/installing-rhel-epel-repo-on-centos-5x-or-6x">guide</a>) (<em>for more recent versions of PHP, MySQL, Apache, etc.</em>).</li>
	<li>Security: Install Fail2Ban (<a href="http://centoshelp.org/security/fail2ban/">guide</a>).</li>
	<li>Insall Apache, MySQL, and PHP (<a href="http://library.linode.com/lamp-guides/centos-6">guide</a>).</li>
<ol>
	<li>Drupal also requires php-gd and php-xml</li>
	<li>Some configuration variables you might want to change:</li>
<ol>
	<li><code>/etc/my.cnf</code>: <code>max_allowed_packet</code> (for non-trival database imports, you want this to be bigger).</li>
	<li><code>/etc/httpd/conf/httpd.conf</code>: Apache settings.</li>
	<li><code>/etc/php.ini</code>: <code>memory_limit</code>, <code>upload_max_filesize</code>, at least</li>
</ol>

</ol>
	<li>Install and configure APC for PHP opcode caching (<a href="http://2bits.com/articles/installing-php-apc-gnulinux-centos-5.html">guide</a>).</li>
	<li>Install and configure Munin for server monitoring (<a href="http://articles.slicehost.com/2010/3/12/installing-munin-on-centos">guide</a>).</li>
	<li>Install git (<code>$ sudo yum install git</code> since you have the REMI/EPEL repos).</li>
	<li>Install drush (<a href="http://openspring.net/tip/how-to-install-drush-serverwide-in-less-than-one-minute">guide</a>).</li>
</ol>

After you've completed all these steps, go ahead and configure Apache's VirtualHosts however you'd like (I typically create a special user for all the sites I run on that server, and include a 'vhosts.conf' file from the user's home directory in Apache's httpd.conf file). Then point a domain name to the server and see if everything's working for you!
