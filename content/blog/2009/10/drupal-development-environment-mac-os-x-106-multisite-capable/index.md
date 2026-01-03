---
nid: 2258
title: "Drupal Development Environment on Mac OS X 10.6 - Multisite Capable"
slug: "drupal-development-environment-mac-os-x-106-multisite-capable"
date: 2009-10-28T08:43:28+00:00
drupal:
  nid: 2258
  path: /blogs/geerlingguy/drupal-development-environment-mac-os-x-106-multisite-capable
  body_format: full_html
  redirects: []
tags:
  - apache
  - development
  - drupal
  - hosts
  - mac
---

<p>I've begun working a lot more with Drupal multisites, as doing so saves a lot of time in certain situations (usually, when you have a large group of sites that use the same kinds of Drupal modules, but need to have separate databases and front-end information.</p>
<p>One problem I've finally overcome is the use of actual domain host names for development (i.e. typing in dev.example.com instead of localhost to get to a site). This is important when doing multisite work, as it lets you use Drupal's built-in multisite capabilities without having to hack your way around using the http://localhost/ url.</p>
<p>Here's what I did to use dev.example.com to access a dev.example.com multisite in a Drupal installation using MAMP (the dev.example.com folder is located within Drupal's /sites/ folder):</p>
<ol>
    <li>Edit MAMP/Apache's httpd.conf file - it's located at <code>/Applications/MAMP/conf/apache/httpd.conf</code>
    <ol>
        <li>Put in the following at the end of the file:<br />
        <pre>
&lt;virtualhost&gt;
  DocumentRoot /Applications/MAMP/htdocs
  ServerName dev.example.com
&lt;/virtualhost&gt;</pre>
        </li>
    </ol>
    </li>
    <li>Restart Apache (in MAMP, click stop servers, then start servers).</li>
    <li>Open up Terminal (in Applications &gt; Utilities), and type in $ sudo nano /private/etc/hosts
    <ol>
        <li>Type in your password if requested</li>
    </ol>
    </li>
    <li>In the hosts file, add a new line after the line that reads <code>127.0.0.1         localhost</code>:
    <ul>
        <li><code>127.0.0.1         dev.example.com</code></li>
    </ul>
    </li>
    <li>Save the file by pressing Control+O (this writes the file) and then Return when it says 'File Name to Write:', then press Control+X to exit nano.</li>
    <li>Now, flush Mac OS X's DNS cache by typing:
    <ul>
        <li><code>sudo dscacheutil -flushcache</code></li>
    </ul>
    </li>
</ol>
<p>Now, if you are behind a proxy server (i.e. if you have the Network settings in System Preferences set to use a proxy server for Web traffic), you will need to also add your dev.example.com entry to the 'Bypass proxies for these domains' field (localhost/127.0.0.1 should already be present here).</p>
<p>Next time you visit http://dev.example.com/ in your web browser, Drupal should point you to the appropriate multisite folder on your local Mac!</p>
