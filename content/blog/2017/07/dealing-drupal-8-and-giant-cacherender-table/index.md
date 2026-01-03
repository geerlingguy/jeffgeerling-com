---
nid: 2795
title: "Dealing with Drupal 8 and a giant cache_render table"
slug: "dealing-drupal-8-and-giant-cacherender-table"
date: 2017-07-17T18:19:45+00:00
drupal:
  nid: 2795
  path: /blog/2017/dealing-drupal-8-and-giant-cacherender-table
  body_format: markdown
  redirects: []
tags:
  - cache
  - drupal
  - drupal 8
  - drupal planet
  - memcached
  - mysql
  - redis
---

There are a number of scenarios in Drupal 8 where you might notice your MySQL database size starts growing _incredibly fast_, even if you're not adding any content. Most often, in my experience, the problem stems from a exponentially-increasing-in-size `cache_render` table. I've had enough private conversations about this issue that I figure I'd write this blog post to cover common scenarios, as well as short and long-term fixes if you run into this issue.

Consider the following scenarios I've seen where a `cache_render` table increased to 10, 50, 100 GB or more:

  - A Search API search page with five facets; each facet has 5-10 links to narrow the search down.
  - A views page with a few taxonomy filters with dozens of options.
  - A views block with a couple filters that allow sorting and narrowing options.

In all three cases, the problem is that the one page (e.g. `/search`) can have hundreds, thousands, millions, or even _billions_ of possible variations (e.g. `/search?value=test`, `/search?value=another%20test`, etc.). So the problem is that _every single variation_ produces a row in the `render_cache` table—whether that cached entry is accessed once, ever, or a million times a day. And there's no process that cleans up the `cache_render` table, so it just grows and grows. Especially when crawlers start crawling the page and following every combination of every link!

This isn't a problem that only affects large sites with millions of nodes, either—all it takes is a few hundred taxonomy terms, nodes, etc., and you will likely encounter the problem.

## So, what's the fix?

First of all, you should follow the Drupal 8 core issue [Database cache bins allow unlimited growth: cache DB tables of gigabytes!](https://www.drupal.org/node/2526150)—that's the best place to testing patches which should resolve the issue more permanently.

After that, here are some ways to fix the issue, in order from the most immediate/quick to the most correct and long-lasting (but possibly more difficult to implement):

  - For an immediate fix, run `drush cr` or click 'Clear all caches' in the admin UI at Configuration > Development > Performance. This will nuke the `cache_render` table immediately. _Note: This could take a while if you have a giant table! It's recommended to use `drush` if possible since a timeout is less likely._
  - For a short-term band-aid to prevent it from happening again, add a cron job that runs `drush cr` at least once a day or week, during a low-traffic period. This is kind of like cleaning up your room by detonating it with TNT, but hey, it works!
  - For a better band-aid, consider using the [Slushi cache](https://www.drupal.org/project/slushi_cache) module, which basically limits the growth of the `cache_render` and `cache_dynamic_page_cache ` tables.
  - For the best fix long-term (and worthwhile to do for better performance regardless of whether you have this problem!), you should use [Redis](https://www.drupal.org/project/redis) or [Memcache](https://www.drupal.org/project/memcache) as your site's cache backend. Unlike the MySQL database, these in-memory caches are usually a bit faster, and are designed to be able to discard old cache entries more intelligently.

And for a bit more detail about debugging this problem (to verify it's the root cause of site issues), check out Acquia's helpful help document, [Managing Large Cache Render tables in Drupal 8](https://docs.acquia.com/article/managing-large-cache-render-tables-drupal-8).

The Drupal.org issue linked earlier in this post will hopefully have a better long-term fix for the many users who are limited to using MySQL, but that's little consolation if your site is offline right now due to the database filling up it's disk space, or backups failing because the database is just too large! In those cases, use one of the bandaids above and determine whether using Redis or Memcache is a possibility.
