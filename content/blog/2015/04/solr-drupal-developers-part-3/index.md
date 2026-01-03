---
nid: 2521
title: "Solr for Drupal Developers, Part 3: Testing Solr locally"
slug: "solr-drupal-developers-part-3"
date: 2015-04-09T03:05:55+00:00
drupal:
  nid: 2521
  path: /blogs/jeff-geerling/solr-drupal-developers-part-3
  body_format: full_html
  redirects: []
tags:
  - apache
  - drupal
  - drupal 7
  - drupal planet
  - search
  - search api
  - series
  - solr
  - tutorial
---

<em>Posts in this series:</em>

<ul>
<li><a href="http://www.jeffgeerling.com/blogs/jeff-geerling/solr-drupal-developers-part-1">Part 1: Intro to Apache Solr</a></li>
<li><a href="http://www.jeffgeerling.com/blogs/jeff-geerling/solr-drupal-developers-part-2">Part 2: Solr and Drupal, A History</a></li>
<li><strong>Part 3: Testing Solr locally</strong></li>
</ul>

<p>In earlier <em>Solr for Drupal Developers</em> posts, you learned about Apache Solr and it's history in and integration with Drupal. In this post, I'm going to walk you through a quick guide to getting Apache Solr running on your local workstation so you can test it out with a Drupal site you're working on.</p>

<p>The guide below is for those using Mac or Linux workstations, but if you're using Windows (or even if you run Mac or Linux), you can use <a href="http://www.drupalvm.com/">Drupal VM</a> instead, which optionally installs Apache Solr alongside Drupal.</p>

<blockquote>
<p>As an aside, I am writing this series of blog posts from the perspective of a Drupal developer who has worked with large-scale, highly customized Solr search for Mercy (<a href="http://www.mercy.net/search/doctor/John?address=St.%20Louis%2C%20MO&amp;distance=50&amp;latlon%5Blat%5D=38.6270025&amp;latlon%5Blon%5D=-90.1994042">example</a>), and with a variety of small-to-medium sites who are using <a href="https://hostedapachesolr.com/">Hosted Apache Solr</a>, a service I've been running as part of Midwestern Mac since early 2011.</p>
</blockquote>
<h2>
<a id="user-content-installing-apache-solr-in-a-virtual-machine" class="anchor" href="#installing-apache-solr-in-a-virtual-machine" aria-hidden="true"><span class="octicon octicon-link"></span></a>Installing Apache Solr in a Virtual Machine</h2>

<p>Apache Solr can be run directly from any computer that has Java 1.7 or later, so technically you could run it on any modern Mac, Windows, or Linux workstation natively. But to keep your local workstation cleaner, and to save time and hassle (especially if you don't want to kludge your computer with a Java runtime!), this guide will show you how to set up an Apache Solr virtual machine using Vagrant, VirtualBox, and Ansible.</p>

<p>Let's get started:</p>

<ol>
<li>Clone the <a href="https://github.com/geerlingguy/ansible-vagrant-examples">ansible-vagrant-examples</a> project from GitHub (you can also <a href="https://github.com/geerlingguy/ansible-vagrant-examples/archive/master.zip">download ansible-vagrant-examples</a> directly).</li>
<li>Change directory in Terminal to the <code>/solr</code> subdirectory, and follow the instructions in the Solr example's README for installing Vagrant, VirtualBox, and Ansible, then follow the rest of the instructions for building that example (e.g. <code>vagrant up</code>).</li>
<li>At this point, if you visit <code>http://192.168.33.44:8983/solr</code> in your browser, you <em>should</em> see the Apache Solr admin interface:
{{< figure src="./apache-solr-admin-dashboard-4-10.png" alt="Apache Solr Administration Dashboard - 4.10" width="600" height="350" >}}</li>
<li>The next step is to point your local Drupal installation (assuming you have a Drupal site running locally) at this Solr instance and make sure it can connect. We're using the <a href="https://www.drupal.org/project/apachesolr">Apache Solr Search</a> module in this example, but <a href="https://www.drupal.org/project/search_api_solr">Search API Solr Search</a> setup is similar.
<ol>
<li>Visit <code>/admin/config/search/apachesolr/settings</code>, and click 'Add search environment'.</li>
<li>Enter <code>http://192.168.33.44:8983/solr/collection1</code> (this is the default search core that Apache Solr includes out of the box) for 'Solr server URL', check the checkbox to make this the default environment, add a description (e.g. 'Local Solr server'), and click 'Save':
{{< figure src="./apache-solr-drupal-configuration-page.png" alt="Drupal Apache Solr module search environment configuration form" width="550" height="430" >}}</li>
<li>After saving the new environment, the next page should show the environment with a green-colored background. That means your Drupal site can connect to the Solr server.</li>
</ol></li>
<li>After Drupal is able to connect, you need to add the Drupal module's Solr configuration files to the search core you'll be using. This takes a few steps, but will ensure all your Drupal content is indexed by Solr correctly.
<ol>
<li>Change directory in Terminal to the <code>/solr</code> directory (where you ran <code>vagrant up</code> earlier), and run <code>vagrant ssh</code> to log into the Solr VM.</li>
<li>While logged into the VM, enter the following commands:
<ol>
<li>
<code>curl http://ftp.drupal.org/files/projects/apachesolr-7.x-1.x-dev.tar.gz | tar -xz</code> (download the Apache Solr module into the current directory).</li>
<li>
<code>sudo cp -r apachesolr/solr-conf/solr-4.x/* /var/solr/collection1/conf/</code> (copy the Apache Solr module configuration into the default Solr core).</li>
<li>
<code>sudo chown -R solr:solr /var/solr/collection1/conf/*</code> (fix permissions for the copied files).</li>
<li>
<code>sudo service solr restart</code> (restart Apache Solr so the configuration is updated).</li>
</ol>
<li>Once this is complete, go back to the Apache Solr search settings page (<code>/admin/config/search/apachesolr/settings</code>), and click on the 'Index' configuration in your local solr server row. You should see something like <code>drupal-4.3-solr-4.x</code> for the 'Schema', meaning the Drupal module <code>schema.xml</code> has been picked up successfully.</li>
</ol>
</li>
</ol>

<p>At this point, you should be able to index your site content into Apache Solr (scroll down and check some content types you want to index), and start playing around with Apache Solr search!</p>

<p>The best first steps are to look around in all the Apache Solr configuration pages, test indexing your entire site, then work on setting up search pages and maybe even install the <a href="https://www.drupal.org/project/facetapi">Facet API</a> module to configure some search facets. In very little time, you should be able to make your site search as user-friendly and speedy as Amazon, Newegg, etc.</p>

<h2>
<a id="user-content-further-reading" class="anchor" href="#further-reading" aria-hidden="true"><span class="octicon octicon-link"></span></a>Further Reading</h2>

<ul>
<li>Drupal.org has excellent step-by-step documentation for <a href="https://www.drupal.org/node/1053074">installing and configuring a Solr server</a> on many different platforms (assuming you don't want to use the <a href="https://galaxy.ansible.com/list#/roles/445"><code>geerlingguy.solr</code></a> Ansible role to set up Solr for you on Redhat, CentOS, Ubuntu or Debian!).</li>
<li>Drupal.org also has <a href="https://www.drupal.org/node/1053102">Tips and suggestions for module customization</a>.</li>
<li>Check out Nick Veenhof's excellent presentation, <a href="http://www.slideshare.net/nickvh/apache-solr-search-course-drupal-7-acquia">Intro to search in Drupal 7</a>, on Slideshare.</li>
</ul>
