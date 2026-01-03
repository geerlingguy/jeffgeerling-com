---
nid: 2414
title: "Boost Expire module being deprecated; how to switch to Cache Expiration"
slug: "boost-expire-module-being"
date: 2013-06-27T03:41:00+00:00
drupal:
  nid: 2414
  path: /blogs/jeff-geerling/boost-expire-module-being
  body_format: full_html
  redirects: []
tags:
  - boost
  - boost expire
  - cache
  - cache expiration
  - caching
  - drupal
  - drupal 7
  - drupal planet
  - performance
---

{{< figure src="./Boost.png" alt="Boost" width="220" height="329" >}}I'm a huge fan of <a href="https://drupal.org/project/boost">Boost</a> for Drupal; the module generates static HTML pages for nodes and other pages on your Drupal site so Apache can serve anonymous visitors the static pages without touching PHP or Drupal, thus allowing a normal web server (especially on cheaper shared hosting) to serve thousands instead of tens of visitors per second (or worse!).

For Drupal 7, though, Boost was rewritten and substantially simplified. This was great in that it made Boost more stable, faster, and easier to configure, but it also meant that the integrated cache expiration functionality was dumbed down and didn't really exist at all for a long time. I wrote the <a href="https://drupal.org/project/boost_expire">Boost Expire</a> module to make it easy for sites using Boost to have the static HTML cache cleared when someone created, updated, or deleted a node or comment, among other things.

However, the <a href="https://drupal.org/project/expire">Cache Expiration</a> module has finally gotten solid Boost module integration (through <code>hook_cache_expire()</code>) in version 7.x-2.x, and <strong>the time has come for all users of Boost Expire to switch to the more robust and flexible Cache Expiration module</strong> (see <a href="https://drupal.org/node/2029269">issue</a>). Here's how to do it:

<ol>
<li>Disable and uninstall the Boost Expire module (then delete it, if you wish).</li>
<li>Download and enable the Cache Expiration module (make sure Boost is still enabled).</li>
<li>Visit the Cache Expiration configuration page (<code>admin/config/development/performance/expire</code>), and set the following options:<ul>
  <li><strong>Module status</strong>: select 'External expiration' to enable cache expiration for the Boost module.</li>
  <li><strong>Node expiration</strong>: check all three checkboxes under Node actions, and make sure the 'Node page' checkbox is checked below.</li>
  <li><strong>Comment expiration</strong>: check all five checkboxes under Comment actions, and make sure the 'Comment page' and 'Comment's node page' checkboxes are checked below.</li>
</ul></li>
</ol>

For the visually inclined, see the screenshots in <a href="https://drupal.org/node/1592774#comment-7583865">this comment</a>.

I'd like to thank the 750+ users of Boost Expire for helping me make it a great and robust stopgap solution until Cache Expiration 'cached' up (heh) with Boost in D7, and the author of and contributors to both Boost and Cache Expiration for making some great and powerful tools to make Drupal sites fly!

If you're interested in some other ways to make your Drupal site faster, check out the article <a href="http://www.jeffgeerling.com/articles/web-design/2010/drupal-performance-white-paper">Drupal Performance White Paper</a> (still in development) on my personal website.
