---
nid: 2309
title: "Gitting Started with New Drupal.org VCS"
slug: "gitting-started-new-drupalorg"
date: 2011-02-25T15:11:50+00:00
drupal:
  nid: 2309
  path: /blogs/jeff-geerling/gitting-started-new-drupalorg
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - git
aliases:
  - /blogs/jeff-geerling/gitting-started-new-drupalorg
---

This is half for my own reference, because I have a few other computers I still need to set up, and I don't want to keep referring back to drupal.org docs to get everything ready for Git.

In case you've been under a rock lately, drupal.org was down for a while yesterday, while a team of dedicated Drupal peeps spent a few hours migrating everything in drupal.org's version control system (which was running CVS) to Git. Git is an excellent tool for version control, and I've been using it for a few months for my personal projects (most recently, I've started using <a href="/blogs/jeff-geerling/prepping-git-drupalorg-need">Tower</a> on my Mac to make Git easier).

Without further ado, here are the steps/links you need to 'git' started with Git on drupal.org:

<ol>
	<li><strong>Update your profile</strong> - you should <a href="http://drupal.org/node/1027094">add your computer's public SSH key</a>, agree to drupal's Git guidelines (edit your profile to see that), and make sure you <a href="http://drupal.org/node/1022156">set your git config settings</a> on your computer to use the same username/email you use in your drupal.org profile.</li>
	<li><strong><a href="https://try.github.io/levels/1/challenges/1">Learn Git</a></strong>&nbsp;- Then <a href="http://gitimmersion.com/">learn more Git</a>. Then&nbsp;<a href="http://progit.org/">learn a whole lotta Git</a>.</li>
	<li><strong>Clone a drupal project</strong>, and <a href="http://drupal.org/node/1054616">create a patch</a>.</li>
</ol>

Read the entire <a href="http://drupal.org/documentation/git">Git handbook on drupal.org</a> for more details. But, basically, you can now do things like add and remove files, create and merge branches, and more, with much less pain than you could yesterday.
