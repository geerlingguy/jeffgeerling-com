---
nid: 2328
title: "All the Hubbub About Drupal 7"
slug: "all-hubbub-about-drupal-7"
date: 2011-08-11T16:26:02+00:00
drupal:
  nid: 2328
  path: /blogs/jeff-geerling/all-hubbub-about-drupal-7
  body_format: full_html
  redirects: []
tags:
  - community
  - development
  - drupal
  - drupal 7
  - drupal planet
  - drupalwtf
  - open source
aliases:
  - /blogs/jeff-geerling/all-hubbub-about-drupal-7
---

Drupal 7. <em>Is it ready?</em>

That seems to be the general question in the air over the past few weeks <a href="http://poplarware.com/news/drupal-7-ready-not">discussed</a> <a href="http://davidherron.com/content/drupals-complexity-turning-people-hurm">by</a> <a href="http://benbuckman.net/drupal-excessive-complexity">many</a> in the community. There's a problem with this question, though... I think many people look at their particular use cases, determine Drupal 7 to not (yet) be a good fit, then declare all things Drupal 7 to be lacking.

Really, though, are things so bad? I've seen hundreds of sites on Drupal Gardens that are beautiful and functional. I've upgraded two of my simpler Drupal 6 sites to Drupal 7. I've built a total of fifteen Drupal 7 sites—some serving more than 10,000 visitors a day, others serving a hundred or two (and almost all on <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/drupal-7-front-end-performance">shared hosting</a>!)—and am working on three others. So, for me, the question 'Is Drupal 7 ready for prime-time?' doesn't make sense. It's already there (I haven't started a new project on Drupal 6 for six months now).

Sure, there are a few rough edges in Drupal 7, and some of the APIs can be confusing and/or complex, mostly because of incomplete or missing documentation... but those things are easy to fix, and require more developers to start using the APIs and fleshing out the APIs.

<h3>Drupal Contrib</h3>

Contributed modules are one of Drupal's greatest strengths, and yes, there are many areas where improvement is needed—but is this any different than Drupal 6? I remember many Drupal modules for D6 that didn't have stable releases until one or two years after D6's launch. They were still perfectly usable except for one or two minor problems, but that's the nature of software—there are always bugs and missing features, and that's not going to change.

In Drupal 7, there are a lot of modules stuck in beta-land, and a few major modules that simple don't have a D7 release, but have many active contributors posting D7-upgrade patches to issue queues. We need to get more module maintainers to commit these patches so people have an upgrade path—bugs and all—from D6 to D7. It's amazing how much more quickly things get stable once there's a 7.x-dev release... and then once that -dev release spawns an alpha or beta.

Take a look at a few of the patches I've tested and/or created as a result of one recent project:

<ul>
	<li><a href="http://drupal.org/node/1160738#comment-4629800">Getting 'Undefined index: join field in flag_views_data_alter()' when clearing caches</a>&nbsp;(Flag module)</li>
	<li><a href="http://drupal.org/node/1223380#comment-4754008">Needs to implement hook_user_delete()</a> (Flag module)</li>
	<li><a href="http://drupal.org/node/714884#comment-4560274">DrupalStream::stream_stat is not implemented!</a> (Input stream module)</li>
	<li><a href="http://drupal.org/node/1177148#comment-4575386">Uninitialized string offset: 0 in form_process_tableselect()</a> (Queue UI module)</li>
	<li><a href="http://drupal.org/node/1007844#comment-4469312">Fix for undefined warnings on Schema page</a> (Schema module)</li>
</ul>

None of the issues for which I require a patch are actually major bugs—usually just missing empty() checks, or a little bug with the way certain values are set or checked. And this is how it is with almost every D7 project I've tried. There are one or two tiny bugs that just require someone spending 5-10 minutes to resolve them. The problem seems to me to be missing module maintainers—most of these patches affect 1-5 lines of code, and should be committed immediately. But they sit in the queues without being touched.

BUT, this doesn't mean you should abandon D7. On the contrary: Drupal 7 is the most advanced, helpful, and awesome Drupal release in history. Some of the new core features—fields, Queue API, more advanced Cron hooks, form #states, etc.—are utterly awesome, and have saved <em>this</em> developer hours of frustration.

<h3>Complexity Breeds Contempt</h3>

I've seen arguments that Drupal core is becoming too complex, or too vast for individual developers (or smaller shops) to grok. However, I believe that (a) this is only partially true, and (b) this is necessary. First, it's only partially true because I consider myself at least vaguely familiar with most parts of the API, after working on one large site with D7. There is plenty of documentation about most things (enough to get you started, at least), and for the rest, a solid hour of Googling will get you the rest of the way.

I also believe that the complexity and size of the codebase is necessary for Drupal, because Drupal is not Wordpress. Drupal is not set up to be utterly simple and focused on one or two use-cases, and good only for the '80%'. Drupal is able to be good for the 95%, and solves complex issues with panache.

If you're setting up a website with three main pages and a blog, use Wordpress. It's that simple. If you want to build a really simple and fast web app that does one thing well, there are other frameworks well-suited to that task. If you want to build a complex website that ties into five different APIs, sends out thousands of emails a day, has a built-in store of some sort, pulls in content from around the web, lets you visulize your content in many different ways, integrates with mobile apps and platforms, lets you migrate all your live data into the new site and <em>also</em> has a blog... Drupal may just be for you! (Case in point: <a href="http://www.flocknote.com/">flockNote</a>, which is 100% Drupal 7-powered).

<h3>The Drop is Always Moving</h3>

There are a lot of things happening in the Drupal universe. The new <a href="http://groups.drupal.org/node/166704">gates</a>&nbsp;being used to determine what gets into Drupal 8 core are a very good idea, and will hopefully help reduce the amount of time-consuming tasks Drupal core developers need to focus on. The new <a href="http://drupal.org/community-initiatives/drupal-core">initiatives</a>&nbsp;are helping certain portions of the community come together and focus on resolving a few complex problems more systematically than happened in Drupal 7's cycle. Acquia and other larger Drupal companies are beginning to pick up more enterprise-class site projects, and Drupal's exposure to the mainstream web is hitting stride.

What does this mean? <a href="http://drupal.org/node/65922">The Drop is Always Moving</a>. There are always a bunch of <a href="http://twitter.com/#!/search/%23drupalwtf">#drupalwtf</a>'s getting in the way, but Drupal will continue to grow and morph into a new beast. You need to keep moving with the Drop. From Drupal release to Drupal release, you will hit a lot of obstacles. But working through those obstacles and continuing your march forward will help thousands of developers who will follow in your footsteps. So, onward we go!
