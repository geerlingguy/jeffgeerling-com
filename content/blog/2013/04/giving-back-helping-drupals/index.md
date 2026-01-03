---
nid: 2401
title: "Giving Back - Helping with Drupal's Issue Queues"
slug: "giving-back-helping-drupals"
date: 2013-04-22T18:54:44+00:00
drupal:
  nid: 2401
  path: /blogs/jeff-geerling/giving-back-helping-drupals
  body_format: full_html
  redirects: []
tags:
  - contribute
  - drupal
  - drupal planet
  - open source
  - presentations
aliases:
  - /blogs/jeff-geerling/giving-back-helping-drupals
---

Below is a video and some notes from my presentation "Giving Back - Helping with Drupal's Issue Queues", which I gave to the St. Louis Drupal group at the <a href="http://groups.drupal.org/node/293683">April 17 meetup</a>. Please post any feedback or additional resources/suggestions in the comments below or on YouTube.

<p style="text-align: center;"><iframe width="640" height="360" src="http://www.youtube.com/embed/8VKp7RBPOOY" frameborder="0" allowfullscreen></iframe></p>

<ul>
<li><p>Note: This presentation roughly coincides with the Drupal Ladder lesson, <a href="http://drupalladder.org/lesson/1d498fa2-d3e4-5754-9160-757d219e8032">Getting started in the issue queue</a>.</p></li>
<li><p>We&#8217;ll look at three different ways you can help contribute to Drupal&#8217;s success in the issue queues.</p></li>
<li>Cleaning up an issue queue, testing and reviewing a patch, and writing your own patch.</li>
</ul>

<h2>Clean up an issue queue</h2>

<p>Reference: <a href="http://drupal.org/node/383956">Helping maintainers in the issue queue</a></p>

<ul>
<li>Many module maintainers, and Drupal core contributors, appreciate any help they can get in making sure their issue queues are not overflowing with support requests and duplicate or related bug reports.</li>
<li>As long as you remember to not step on anyone&#8217;s toes, you can be a huge help to module maintainers especially.</li>
<li>Let&#8217;s hop into a queue and take a look:
<ul>
<li><a href="http://drupal.org/project/issues/privatemsg?categories=All">Privatemsg issue queue</a></li>
<li>&#8220;How to add a class to the messages link in the user menu?&#8221;</li>
<li>See: <code>theme_menu_link</code>, <code>menu_attributes</code> module</li>
</ul></li>
</ul>

<h2>Testing and reviewing a patch</h2>

<p>Reference: <a href="http://drupal.org/project/issues/drupal?status=8&amp;categories=bug&amp;version=7.x">Issues for Drupal 7 core - patches for bugs</a></p>

<ul>
<li>Let&#8217;s find a simple patch to review for Drupal 7. (I would do Drupal 8, but right now things are in flux so much that almost any patch older than a week is almost guaranteed to not work right).</li>
<li>Go to &#8216;Advanced Search&#8217; in the core issue queue.</li>
<li>Enter &#8216;Novice&#8217;.</li>
<li>Find: <a href="http://drupal.org/node/1038356">Labels in tables need some left padding</a>
<ul>
<li>Apply patch on Drupal core on simplytest.me</li>
<li>Edit Article content type, make new textfield with unlimited values.</li>
<li>Create article with Garland theme, and with Seven theme.</li>
</ul></li>
<li>Summarize what happened in a new comment on the issue (David_Rothstein is correct that it looks funny in Garland, but it does make the text look better in Seven).</li>
<li>Post screenshots for reference.</li>
</ul>

<h2>Writing your own patch</h2>

<p>Reference: <a href="http://drupal.org/project/issues/advanced_help">Issues for Advanced help</a>
Reference: <a href="http://drupal.org/node/1901746">Advanced Help: Allow more space for the up text</a></p>

<ul>
<li>There are many issues around Drupal.org where someone&#8217;s reported a bug or laid out a quick fix for something, but there&#8217;s no patch.</li>
<li>You can take their bug report and turn it into an actionable patch.</li>
<li>Let&#8217;s do that with this issue for the Advanced Help module (see reference above).</li>
<li>&#8230;</li>
<li>In the future, instead of just posting a bug report, you can post a patch which fixes the bug!
<ul>
<li>These kinds of issues are far and away the most helpful and appreciated by module maintainers.</li>
<li>But any kind of good bug report or well-thought-out feature request is also helpful!</li>
</ul></li>
</ul>

<h2>More Resources</h2>

<ul>
<li><a href="http://drupal.org/new-contributors">New contributor tasks</a></li>
<li><a href="http://drupalladder.org/lesson/1d498fa2-d3e4-5754-9160-757d219e8032">Getting started in the issue queue</a></li>
<li><a href="http://drupal.org/node/1427826">Please help: Issue Summaries</a></li>
<li><a href="http://julian.granger-bevan.me/blog/websites/how-to-start-contributing-in-drupalorg-issue-queues">How to start contributing in Drupal.org issue queues</a></li>
</ul>
