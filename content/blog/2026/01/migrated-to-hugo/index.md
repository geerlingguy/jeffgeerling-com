---
date: '2026-01-03T13:00:00-06:00'
title: 'JeffGeerling.com has been Migrated to Hugo'
tags: ['migration', 'hugo', 'drupal', 'drupal-planet', 'blog', 'go', 'migrate', 'history']
slug: 'migrated-to-hugo'
---
Since 2009, this website has [run on Drupal](/blog/2009/moved-drupal-hello-drupal). Starting with Drupal 6, and progressing through major site upgrades and migrations to 7, 8, 9, and 10, I used the site as a way to dogfood the same CMS (Content Management System) I used in my day job for _over a decade_.

{{< figure
  src="./jeffgeerling-old-drupal.png"
  alt="JeffGeerling.com - Old Drupal site"
  width="700"
  height="auto"
  class="insert-image"
>}}

But as time progressed—especially after completing a [grueling upgrade from Drupal 7 to 8](/blog/2020/migrating-jeffgeerlingcom-drupal-8-live)—my enthusiasm for maintaining what's now a more enterprise-focused [Digital Experience Platform](https://www.acquia.com/blog/what-digital-experience-platform-dxp) or 'DXP' for a personal blog has waned.

Not to mention, the blog is a passion project. I use it as a scratchpad for thoughts, and deeper dives for [my YouTube videos](https://www.youtube.com/c/JeffGeerling). Time spent maintaining a complex CMS is time I can't spend actually _writing_ (not to mention time spent on everything else in life!).

## Why Hugo?

I've moved other hobby sites to static hosting. For older sites I don't actively update, I [scrape and mothball](/blogs/jeff-geerling/drupal-on-mothballs-convert-static-html) them. But for sites I wanted to keep active, I converted them to [Jekyll](https://jekyllrb.com) or [Hugo](https://gohugo.io), both of which are competent and full-featured modern SSGs (Static Site Generators).

Jekyll is perfect for the static sites I host for free on GitHub Pages, like the [Raspberry Pi PCIe Database](https://pipci.jeffgeerling.com) or [Project MINI RACK](https://mini-rack.jeffgeerling.com), but I'm not a Ruby programmer, so I like Hugo for anything I run on my _own_ infrastructure (like [Geerling Engineering](https://www.geerlingengineering.com)). It's simpler to set up and a little faster.

## Housekeeping

Anyway, I've been working on the migration in [this GitHub issue](https://github.com/geerlingguy/jeffgeerling-com/issues/158), and there are bound to be mistakes, broken image references, and probably some old URLs that just go _poof_!

{{< figure
  src="./jeffgeerling-new-hugo.png"
  alt="JeffGeerling.com - New Hugo site"
  width="700"
  height="auto"
  class="insert-image"
>}}

I try to keep everything where it is, or add redirects. But with 20 years of baggage and 3500+ posts (many of those were individual photos converted into 'blog' nodes in a prior upgrade... oops!), it's hard to run a perfect migration.

## Markdown Workflow

I've been writing all my posts in Markdown [since 2020](https://github.com/geerlingguy/jeffgeerling-com/issues/13), and even before that, was drafting them in Markdown in Sublime Text, then exporting that to HTML via [MarkdownPreview](https://facelessuser.github.io/MarkdownPreview/).

So having a tool (Hugo) that uses Markdown natively is a breath of fresh air.

Beyond that, I've grown fond of 'sticking to the defaults' over the years. On my initial Drupal 6 site, I installed something like 30 modules (plugins in Drupal parlance), but almost all of those modules bit me in one way or another as I upgraded to Drupal 7, 8, 9, or 10...

Honestly, upgrading from 8 to 9 to 10 was easier than 6 to 7 and 7 to 8, simply because I had stripped my site down to the basics.

_However_, in so doing, I also made my content authoring experience a bit horrid:

  1. Write a blog post on my computer in a Markdown file
  2. Create new unpublished Drupal blog post
  3. Paste the Markdown content into the body and add a title
  4. Individually upload each picture
  5. Put cursor where each picture goes in the content, scroll down to the uploaded picture, click 'Insert' to insert the preformatted `<img>` markup, and rinse-and-repeat for all images (sometimes up to 25-30 per post!).
  6. Clear out the 'Authored on' field to make sure the date would update when I publish the post
  7. Toggle the 'Published' option and save the node
  8. Run an Ansible playbook to drop Drupal caches, Nginx caches, and trigger a Cloudflare purge of the relevant URLs ([ongoing DDoSes since 2022](https://www.jeffgeerling.com/blog/2022/three-ddos-attacks-on-my-personal-website) caused me to _really_ lock down my caching)...

It was a _lot_. Just to publish a blog post—and none of that helped with writing or being creative, it was just a bunch of work.

_Yes_, I could automate each step in Drupal. There are even modules for Drupal, like [Scheduler](https://www.drupal.org/project/scheduler) for scheduling posts and updating publish dates, and [Cloudflare](https://www.drupal.org/project/cloudflare) for purging CDN cache... but you know what? I used to use those modules, but after four Drupal upgrade cycles, I was burned out on managing patches for months, years, or _indefinitely_ since some of the modules took that long to have a stable release for [current Drupal version].

And don't get me started on having to rebuild entire content authoring workflows (e.g. WYSIWYG editors, media management, and content fields) every time a major Drupal version was released! That specific type of churn, thankfully, is not _as_ bad these days, but it was _really_ bad prior to Drupal 10 or so.

For _Hugo_, since my workflow already started with a Markdown file... the whole process is done after step 1, basically.

To publish, I guess I _do_ have to update the `date` in my post's frontmatter, and change `draft` to `false`, but that's about it. `hugo && git commit -m "Updated post." && git push` and the blog is up to date!

And for maintenance, don't get me started on managing Composer, Drush, PHP, MariaDB, Nginx, Cloudflare, etc. — for an enterprise website, with multiple content workflows, dozens or hundreds of users with RBAC, etc., sure, it's fine. But for a blog where I just want to _write_ and _publish_, it has been wearing me down for the past few years.

## TODOs

Comments will be missing site-wide initially, as I've chosen to tackle a [self-hosted static site commenting system](https://github.com/geerlingguy/jeffgeerling-com/issues/167) in a 'phase two'. I love having comments enabled, despite the moderation overhead, and don't think blogging is the same without them.

I also loved having integrated site search, since I use my blog as a project journal, referencing it often. The Drupal site was integrated into an Apache Solr search instance I also ran as part of [Hosted Apache Solr](https://hostedapachesolr.com)... which I sunset years ago at this point. So I'll have to decide [how I want to implement search within Hugo](https://github.com/geerlingguy/jeffgeerling-com/issues/168).
