---
nid: 2387
title: "Preventing Security Holes"
slug: "preventing-security-holes"
date: 2012-11-06T21:18:11+00:00
drupal:
  nid: 2387
  path: /blogs/jeff-geerling/preventing-security-holes
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - security
aliases:
  - /blogs/jeff-geerling/preventing-security-holes
---

I was recently browsing a very popular review website, when I noticed the following warnings popping up:

<p style="text-align: center;">{{< figure src="./angies-list-error.png" alt="Angie's List website errors" width="500" height="227" >}}</p>

From simply loading their web page and seeing these error messages, I could conclude:

<ol>
	<li>The website is using Drupal.</li>
	<li>The website is using memcached.</li>
	<li>The website is running on Acquia's managed hosting cloud.</li>
	<li>The website has error reporting set to print all errors to the screen.</li>
</ol>

If I were trying to break into this review site, or cause them a bad day, the information presented in this simple error message would help me quickly tailor my attacks to become much more potent than if I started from a blank slate.

<h2>Security through obscurity</h2>

I will quickly point out that security through obscurity—thinking you're more secure simply because certain information about your website is kept secret—is no security at all. However, that doesn't mean that obscurity is not an important part of your site's security.

Simply because the site above doesn't have the 'display no error messages' setting enabled on the live website, I was able to learn quite a bit about the site. I could've probably found more 'helpful' error messages had I spent a little more time investigating.

At least the site's server-status page is protected! (Many sites <a href="http://arstechnica.com/security/2012/11/misconfigured-apache-sites-expose-user-passwords-other-private-data/">leave the Apache server-status page open</a>, exposing a ton of potentially dangerous details).

Keeping certain things secret, like errors that occur on your site, the version of a particular CMS, plugin, module, or theme of your website, or status reporting information, <em>does</em> improve your site's security. It won't prevent a dedicated intruder, but it will definitely slow him down, and will likely deter less-dedicated intruders.

To contribute to the overall security of your website, you should do the following:

<ul>
	<li>Make sure server and configuration status pages are secure from outside access. If you need to expose phpinfo() or server-status, make sure only&nbsp;<em>you</em> have access.</li>
	<li>Turn off error message printing on the screen on your publicly-accessible sites. Only turn on this feature on development or testing sites. (You should still&nbsp;<em>log</em> error messages, but do this behind the scenes, using syslog or some other logging facility).</li>
	<li>Protect your server configuration, error, and log files from prying eyes; even <em>backups</em> of these files can be a security hole.</li>
</ul>

<h2>Hardening your defenses</h2>

Of course, as I mentioned above, <em>security through obscurity is no security at all</em>. Even if someone were to know every detail about your server configuration and setup, your site should still be secure. The following are some essential steps to ensuring the security of your website:

<ul>
	<li>Apply patches and updates routinely. Most systems have automatic update systems, or at least notify you when an update is available.</li>
	<li>Have an outside consultant evaluate the security of any custom code or interfaces you provide (especially for custom forms, API interaction, and file handling).</li>
	<li>Use automated tools like <a href="http://www.fail2ban.org/wiki/index.php/Main_Page">Fail2Ban</a> on your servers to make sure repeated attempts to access your servers are blocked.</li>
	<li>Know your options when it comes to spam filters and flood controls; Drupal, as an example, has a plethora of excellent modules and configuration settings to prevent certain security holes from being opened. There's even a nice <a href="http://drupal.org/project/security_review">Security Review</a> module that looks at common site configuration problems and warns you if they're incorrect.</li>
</ul>
