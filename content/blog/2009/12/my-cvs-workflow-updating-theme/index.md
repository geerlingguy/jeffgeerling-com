---
nid: 2262
title: "My CVS Workflow for Updating a Theme on drupal.org"
slug: "my-cvs-workflow-updating-theme"
date: 2009-12-03T23:31:42+00:00
drupal:
  nid: 2262
  path: /blogs/geerlingguy/my-cvs-workflow-updating-theme
  body_format: full_html
  redirects: []
tags:
  - cvs
  - drupal
  - terminal
  - theming
aliases:
  - /blogs/geerlingguy/my-cvs-workflow-updating-theme
---

<p>{{< figure src="./cvs-ugh.png" alt="Drupal CVS &lt;ugh&gt; Druplicon Frown" width="293" height="190" class="noborder" >}}From time to time, I've had to update my airyblue project in CVS (<a href="http://drupal.org/project/airyblue">Airy Blue</a> is a light, airy, Zen subtheme listed on Drupal.org's Themes section). It's always a bother, and I always end up spending about 20 minutes figuring out how to check out the module to my local computer (I use three of them, so even if I have it set up on one, I need to get it going on another sometimes), then another 20 figuring out how to commit my changes, tag a release, etc.</p>
<p>So, this post might be titled &quot;How to Maintain a Theme on Drupal.org if You're Confounded by the <a href="http://drupal.org/node/262432">CVS Guide for Theme Maintainers</a>, and you are on a computer on which you haven't checked out your module yet.&quot;</p>
<p>Logging in, Setting up CVSROOT</p>
<ol>
    <li>Open up Terminal (on a Mac) and navigate (<code>cd</code>) to your CVS folder.</li>
    <li>Enter <code>export CVSROOT=:pserver:&lt;username&gt;@cvs.drupal.org:/cvs/drupal-contrib</code><br />
    (This will set your CVS 'root' to the right directory. Enter your username where it says &lt;username&gt;).</li>
    <li>Enter <code>cvs login</code> to login, and type in your CVS password when prompted.</li>
    <li>Type in <code>cvs checkout -l contributions/themes</code></li>
    <li>Type in <code>cvs checkout -d contributions/themes/&lt;themename&gt; contributions/themes/&lt;themename&gt;</code></li>
</ol>
<p>After you do this, you should have the latest version of your module checked out into your local folder. Now, edit the files however you'd like, and test them locally to be sure your changes are correct. Next you have to commit your changes (<em>don't do this yet if you've added or removed any files or folders*</em>):</p>
<ol>
    <li>In the same Terminal window, type in <code>cvs commit -m &quot;Explanation of changes.&quot;</code></li>
    <li>Finally, you have to tag your release before you can go to the project page on drupal.org and create a new release of your theme. Type in <code>cvs tag DRUPAL-6--1-1</code> (or whatever tag you need - in my case, it was DRUPAL-6--1-5 for 6.x-1.5).</li>
</ol>
<p>Now, go back to your project page on drupal.org, and click the 'Add new release' link under the Download section. In the release notes, you should reference all the issues you addressed in this release cycle, by typing them in as follows: [#552912] (the number should be replaced by issue's number as seen on drupal.org).</p>
<p>*If you added or removed any files, you will need to tell the CVS server what you did:</p>
<ol>
    <li>For a new directory, type in <code>cvs add &lt;directory&gt;</code></li>
    <li>And to get all the files inside that directory added, type in <code>cvs add &lt;directory&gt;/*</code></li>
    <li>To remove a file or directory, type in <code>cvs remove &lt;filename&gt;</code> or <code>cvs remove &lt;directory&gt;</code></li>
</ol>
