---
nid: 2367
title: "My Simple, but Nerve-Calming, drush Update Workflow"
slug: "my-simple-nerve-calming-drush"
date: 2011-01-04T16:50:58+00:00
drupal:
  nid: 2367
  path: /blogs/jeff-geerling/my-simple-nerve-calming-drush
  body_format: filtered_html
  redirects: []
tags:
  - development
  - drupal
  - drupal planet
  - drush
  - workflow
aliases:
  - /blogs/jeff-geerling/my-simple-nerve-calming-drush
---

<p>Just posted for my own reference - here's my workflow for updating a D6 (probably also D7) website using drush. Comprehensive information about all drush commands can be found on the http://drush.ws/ website. If you're not yet drinking the drush kool-aid, you need to—if you use a Linux server, of course.</p>

<ol>
<li>Visit admin/reports/updates page on your site, read through any relevant release notes for required updates (to check if there are special requirements for said update).</li>
<li><code>$ drush @site pm-updatecode <module1_shortname> <module2_shortname></code> (add all modules to be updated)</li>
<li><code>$ drush @site updatedb</code> (updates the site database - update.php)</li>
<li><code>$ drush @site cc all</code> (clears all caches on the site)</li>
</ol>

<p>The reason I do this manually, instead of running something like <code>pm-update</code> or <code>pm-updatecode</code> is that I like the granularity and security of doing all the updates discretely—especially when I'm updating a larger site, where I like to know exactly what's happening when I update.</p>

<p>For Drupal core updates, at least in D6, I always copy the files in by hand (even though drush can handle this), because I just don't trust Drush with that operation—especially if I have other files included in my root directory for other purposes. (Plus, using git, this is a breeze. When I used SVN or CVS, it was a major pain, due to all the 'CVS' or '.svn' directories that had to be maintained).</p>

<p>After finishing the drush process, I do a <code>$ git add .</code>, <code>$ git add -u</code>, then <code>$ git commit -am "Updated <modulename1>, <modulename2>, etc."</code> (after testing the site thoroughly, of course). Then I push the changes to production, do an <code>updatedb</code> on that server, and breathe a sigh of relief when everything's working perfectly.</p>

<p>Anyone have a better idea for leveraging drush for updates? One thing I wish I could do is maintain patches when doing drush updates on a module, instead of having to re-download and apply the patch.</p>
