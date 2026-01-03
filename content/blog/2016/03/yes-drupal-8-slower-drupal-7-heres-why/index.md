---
nid: 2636
title: "Yes, Drupal 8 is slower than Drupal 7 - here's why"
slug: "yes-drupal-8-slower-drupal-7-heres-why"
date: 2016-03-24T15:40:23+00:00
drupal:
  nid: 2636
  path: /blog/2019/yes-drupal-8-slower-drupal-7-heres-why
  body_format: markdown
  redirects:
    - /blog/2016/yes-drupal-8-slower-drupal-7-heres-why
aliases:
  - /blog/2016/yes-drupal-8-slower-drupal-7-heres-why
tags:
  - bigpipe
  - caching
  - drupal
  - drupal 7
  - drupal 8
  - drupal planet
  - performance
  - refreshless
  - varnish
  - xhprof
---

> **tl;dr**: Drupal 8's defaults make most Drupal sites perform _faster_ than equivalent Drupal 7 sites, so be wary of benchmarks which tell you Drupal 7 is faster based solely on installation defaults or raw PHP execution speed. Architectural changes have made Drupal's codebase slightly slower in some ways, but the same changes make the overall experience of using Drupal and browsing a Drupal 8 site _much_ faster.

When some people see reports of Drupal 8 being 'dramatically' slower than Drupal 7, they wonder why, and they also use this performance change as ammunition against some of the major architectural changes that were made during Drupal 8's development cycle.

First, I wanted to give some more concrete data behind _why_ Drupal 8 is slower (specifically, what kinds of things does Drupal 8 do that make it take longer per request than Drupal 7 on an otherwise-identical system), and also _why_ this might or might not make any difference in your choice to upgrade to Drupal 8 sooner rather than later.

## Load test benchmarks with a cluster of Raspberry Pis

For a hobby project of mine, the [Raspberry Pi Dramble](http://www.pidramble.com/), I like to benchmark every small change I make to the infrastructure—I poke and prod to see how it affects load capacity (how many requests per second can be served without errors), per-page load performance (how many milliseconds before the page is delivered), and availability (how many requests are served correctly and completely).

I've compiled these benchmarks from time to time on the [Dramble - Drupal Benchmarks](http://www.pidramble.com/wiki/benchmarks/drupal) page, and I also did a much more detailed blog post on the matter (especially comparing PHP 5.6 to 7.0 to HHVM): [Benchmarking PHP 7 vs HHVM - Drupal and Wordpress](/blogs/jeff-geerling/benchmarking-drupal-8-php-7-vs-hhvm).

The most recent result paints a pretty sad picture if you're blindly comparing Drupal 8's standard configuration with Drupal 7's (with anonymous page caching enabled<sup>1</sup>):

<p style="text-align: center;">{{< figure src="./drupal-8-vs-drupal-7-standard-profile-performance.png" alt="Drupal 8 vs Drupal 7 standard profile performance on home page load - anonymous vs authenticated" width="533" height="426" >}}</p>

These particular benchmarks highlight the maximum load capacity with 100% availability that the cluster of five (incredibly slow, in comparison to most modern servers) Raspberry Pis. Chances are you'll get more capacity just spinning up an instance of [Drupal VM](http://www.drupalvm.com/) on your own laptop! But the fact of the matter is: Drupal 7, both when loading pages for anonymous and authenticated users, in a very bare (no custom modules, no content) scenario, is much faster than Drupal 8. But _why?_

## XHProf page profiling with Drupal 7 and Drupal 8

With Drupal VM, it's very easy to [profile code with XHProf](http://docs.drupalvm.com/en/latest/extras/xhprof/), so I spun up one VM for Drupal 8, then shut that one down and spun up an identical environment for Drupal 7 (both using PHP 5.6 and Apache 2.4), and ran an XHProf analysis on the home page, standard profile, anonymous user, with anonymous page cache enabled, on the first page load (e.g. when Drupal stores its anonymous cache copy).

Subsequent page loads use even less of Drupal's critical code path, and it would be helpful to also analyze what's happening there, but for this post I'll focus on the first anonymous page request to the home page.

Compare, first, the zoomed out callgraph image for Drupal 7 (126ms, 13,406 function calls, 3.7 MB memory) vs Drupal 8 (371ms, 41,863 function calls, 11.1 MB memory):

<p style="text-align: center;">{{< figure src="./xhprof-callgraph-anonymous-drupal-7-vs-8.jpg" alt="Drupal 7 vs Drupal 8 - Anonymous request to standard profile home page - XHProf call graph comparison" width="458" height="351" >}}<br />
<em>Call graphs for <a href="https://www.dropbox.com/s/jo80g21qzaf336t/xhprof-callgraph-drupal-7-home-anonymous-standard-profile.png?dl=0">Drupal 7</a> (left) vs <a href="https://www.dropbox.com/s/rllmr7q9rq59ady/xhprof-callgraph-drupal-8-home-anonymous-standard-profile.png?dl=0">Drupal 8</a> (right) - click the links to download full size</em></p>

Callgraphs allow you to visualize the flow of the code from function to function, and to easily identify areas of the code that are 'hotspots', which either take a long time to run or are called many, many times.

Just glancing at the callgraphs, you can see the difference in the way the page is rendered. In Drupal 7, Drupal's homegrown request routing/menu system efficiently chooses the proper menu callback, and most of the time is spent in regular expressions (that 'preg_grep' red box) during theming and rendering the page.

In Drupal 8, there is a bit of extra time spent routing the request to the proper handler, notifying subscribers of the current request and response flow<sup>2</sup>, with similar amounts of time as Drupal 7 are spent theming and rendering the page. On top of that, since Drupal 8 has been architected in a more OOP way, especially with the splitting out of functionality into discrete PHP files, more time is spent scanning file data on each page load—this can be mitigated in some circumstances by disabling opcache's stat of each file on each page load, but even then, there is a lot of time spent in `file_exists`, `Composer\Autoload\ClassLoader::findFileWithExtension`, `is_file`, and `filemtime`.

In both cases, one of the most time-consuming tasks is retrieving data from the database; in Drupal 8, the front page took about 29ms grabbing data from MySQL, in Drupal 7, about 26ms—close enough to be practically the same. In most _real-world_ scenarios, database access is a much larger portion of the page load, so the total page render times in real world usage are often a bit closer between Drupal 7 and Drupal 8. But even there, Drupal 8 adds in a tiny bit of extra time for its more flexible (and thus expensive) entity loading.

So Drupal 8's hot/minimal code path is verifiably slower than Drupal 7 in many small ways, due to additional function calls and object instantiation for Symfony integration, notification handling (on top of some remaining Drupal 7-style hooks) and time spent rummaging through the highly individual-file-per-class-heavy codebase. But does this matter _for you_? Thats can be a difficult question to answer.

> You can download the full .xhprof reports below; if you want to view them in XHProf and generate your own callgraphs, you can do so by placing them in your XHProf output directory without the `.txt` extension:
> 
>   - [drupal7-56eb23846cf23.Drupal.xhprof.txt](./drupal7-56eb23846cf23.Drupal.xhprof.txt)
>   - [drupal8-56eb2134b8978.Drupal.xhprof.txt](./drupal8-56eb2134b8978.Drupal.xhprof.txt)

## Drupal 8 changes - more than just the architecture

Most Drupal 7 site builders feel quite at home in Drupal 8, especially considering many of the features that are baked into Drupal 8 core were the most popular components of many Drupal 7 sites—Views, Wysiwyg, entity relationships, etc. Already, just adding those modules (which are used on many if not most Drupal 7 sites) to a standard Drupal 7 site evens the playing field by a large margin, at least for uncached requests:

<p style="text-align: center;">{{< figure src="./drupal-7-vs-drupal-8-performance-with-modules.png" alt="Drupal 7 vs Drupal 8 with D8 core modules included in Drupal 7" width="535" height="384" >}}<br />
<em>Drupal 7 and Drupal 8 authenticated requests are much more even when including all of D8's core functionality</em></p>

It's rare to see a Drupal 7 site with less than ten or fifteen contributed modules; many sites have dozens—or even hundreds—of contributed modules that power the various admin and end-user-facing features that make a Drupal 7 site work well. Using real-world sites as examples, rather than clean-room Drupal installs, benchmarks between _functionally similar_ Drupal 7 and Drupal 8 sites are often much closer (like the one above); though Drupal 7 still takes the raw performance crown per-page-request.

> For the above D7 + D8 core module test, I ran the following drush command to get (most of) the modules that are in D8 core, enabled via the standard install profile: `drush en -y autoupload backbone bean breakpoints ckeditor date date_popup_authored edit email entityreference entity_translation file_entity filter_html_image_secure jquery_update link magic module_filter navbar phone picture resp_img save_draft strongarm transliteration underscore uuid variable views`

So, Drupal 8 is slightly slower than a Drupal 7 site with a comparable suite of modules... _excluding_ many of the amazing new features like Twig templating, built-in Wysiwyg and file upload integration, a better responsive design for everything, more accessibility baked in, and huge multilingual improvements—what else in Drupal 8 makes the raw PHP performance tradeoff worth it?

## Easier and more robust caching for anonymous users

<p style="text-align: center;">{{< figure src="./varnish-cache-hit.png" alt="Varnish cache hit in Drupal 8" width="311" height="92" >}}</p>

What's the best way to speed up any kind of dynamic CMS? To bypass it completely, using something like Varnish, Nginx caching, or a CDN acting as a caching or 'reverse' proxy like Fastly, CloudFlare or Akamai. In Drupal 7, all of these options were available, and could be made to work fairly easily. However, the elephant in the room was always _how do you keep content fresh_?

The problem was Drupal couldn't pass along any information with pages that were cached to help upstream reverse proxies to _intelligently_ cache the documents. You'd end up with dozens or custom configured rules and a concoction of modules like [Expire](https://www.drupal.org/project/expire), [Purge](https://www.drupal.org/project/purge), and/or [Varnish](https://www.drupal.org/project/varnish), and then you'd still have people who publish content on your site asking why their changes aren't visible on page XYZ.

In Drupal 8, [cache tags](https://www.drupal.org/developing/api/8/cache/tags) are built into core and passed along with every page request. Cache tags allow reverse proxies to attach a little extra metadata to every page on the site (this doesn't need to be passed along to the client, since it's only for cacheability purposes), and then Drupal can intelligently say "expire any page where `node:118292` appears". Then Varnish could add a ban rule that will mark any view, content listing, block, or other node where `node:118292` appears as needing to be refreshed from the backend.

Instead of setting extremely short TTLs (time to live) for content, meaning more requests to Drupal (and thus a slower average response time), you will be free to set TTLs much longer—for some sites, you could even set the cache TTL to days, weeks or longer, so Drupal is only really ever touched when new content is added or specific content is updated.

I wrote a [very detailed article on how you can use cache tags with Varnish and the Purge module in Drupal 8](/blog/2016/use-drupal-8-cache-tags-varnish-and-purge); you can also more easily use Drupal 8 with CloudFlare, Fastly, and other CDNs and reverse proxies; for simple cases, you can use Drupal 8 with CloudFlare's free plan, like I did with my [Raspberry Pi Dramble](/blog/2016/configuring-cloudflare-drupal-8-protect-pi-dramble). Paid plans allow you to integrate more deeply and use cache tags effectively.

## Faster for authenticated users and slow-loading content

If you need to support many logged in users (e.g. a community site/forum, or a site with many content editors), you know how difficult it is to optimize Drupal 6 or 7 for authenticated users; the [Authcache](https://www.drupal.org/project/authcache) module and techniques like [Edge-Side Includes](https://en.wikipedia.org/wiki/Edge_Side_Includes) have been the most widely-adopted solutions, but if, like me, you've ever had to implement these tools on complex sites, you know that they are hard to configure correctly, and in some cases can cause _slower_ performance while simultaneously making the site's caching layers _harder_ to debug. Authenticated user caching is a tricky thing to get right!

In Drupal 8, because of the comprehensive cacheability metadata available for content and configuration, a new [Dynamic Page Cache](https://www.drupal.org/documentation/modules/dynamic_page_cache) module is included in core. It works basically the same as the normal anonymous user page cache, but it uses [auto-placeholdering](https://www.drupal.org/developing/api/8/render/arrays/cacheability/auto-placeholdering) to patch in the dynamic and uncacheable parts of the cached page. For many sites, this will make authenticated page requests an _order of magnitude_ faster (and thus more scalable) in Drupal 8 than in Drupal 7, even though the raw Drupal performance is slightly slower.

That's well and good... but the end user still doesn't see the rendered page until Drupal is completely finished rendering the page and placing content inside the placeholders. _Right?_ Well, Drupal 8.1 adds a new and amazing experimental feature modeled after [Facebook's "BigPipe" tech](https://www.facebook.com/notes/facebook-engineering/bigpipe-pipelining-web-pages-for-high-performance/389414033919):

<p style="text-align: center;">{{< figure src="./bigpipe-demo-one.gif" alt="BigPipe demonstration in an animated gif" width="640" height="360" >}}<br />
<em>BigPipe demo - click the above gif to play it again.</em></p>

The image above illustrates how BigPipe can help even slow-to-render pages deliver usable content to the browser very quickly. If you have a block in a sidebar that pulls in some data from an external service, or only one tiny user-specific block (like a "Welcome, Jeff!" widget with a profile picture) that takes a half second or longer to render, Drupal can now serve the majority of a page _immediately_, then send the slower content when it's ready.

To the end user, it's a night-and-day difference; users can start interacting with the page very quickly, and content seamlessly loads into other parts of the page as it is delivered. Read more about [BigPipe in Drupal](https://www.drupal.org/documentation/modules/big_pipe)—it's currently labeled as an 'experimental' module in Drupal 8.1, and I'm currently [poking and prodding BigPipe with Drupal VM](https://github.com/geerlingguy/drupal-vm/issues/527).

Also, in case you're wondering, here's a great overview of [the difference between ESI and BigPipe](http://stackoverflow.com/a/16115263/100134).

There are a few caveats with BigPipe—depending on your infrastructure's configuration, you may need to make some changes so BigPipe can stream the page correctly to the end user. Read [BigPipe environment requirements](https://www.drupal.org/documentation/modules/big_pipe/environment) for more information.

## Only the beginning of what's possible

Drupal 8's architecture also allows for other innovative ways of increasing overall performance. One trend on the upswing is **decoupled Drupal**, where all or parts of the front-end of the site (the parts of the website your users see) are actually rendered via javascript either on a server, or on the client (or a mix of both). These decoupled sites have the potential to make more seamless browsing experiences, and can also make some types of sites perform _much_ faster.

> Caveat: Before decoupling, have a read through Dries Buytaert's recent (and very insightful) blog post: [How should you decouple Drupal?](http://buytaert.net/how-should-you-decouple-drupal)

In Drupal 7, building a fully decoupled site was extremely difficult, as everything would need to work around the fact that Drupal < 8 was built mainly for generating HTML pages. Drupal 8's approach is to generate generic "responses". The default is to generate an HTML page... but it's much easier to generate JSON, XML, or other types of responses. And things like cacheability metadata are also flexible enough to work with any kind of response, so you can have a full-cacheable decoupled Drupal site if you want, without even having to install extra modules or hack around Drupal's rendering system, like you did in Drupal 7.

<p style="text-align: center;"><video width="420" height="525" controls="controls"><source src="https://www.drupal.org/files/issues/Turbolinks%20quick%20PoC%2060fps.mp4" type="video/mp4" /></video><br />
<a href="https://www.drupal.org/files/issues/Turbolinks%20quick%20PoC%2060fps.mp4">Click here to download the video</a> if it won't play above.</p>

Another recent development is the [RefreshLess](https://www.drupal.org/project/refreshless) module, which uses javascript and the [HTML5 history API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to make any Drupal 8 site behave more like a one page app—if you click on a link, the page remains in place, but the URL updates, and the parts of the page that are different are swapped out seamlessly, using the cacheability data that's _already_ baked into Drupal 8, powering all the other awesome new caching tools!

On top of _all that_, we're still very early in Drupal 8's release cycle. Since Drupal is using semantic versioning for releases, new features and improvements can be added to minor releases (e.g. 8.1, 8.2, etc.), meaning as we see more of what's possible with BigPipe, Dynamic page cache, etc., we'll make even more improvements—maybe to the point where even the tiniest Drupal 8 page request is close to Drupal 7 in terms of raw PHP execution speed!

What are _your_ thoughts and experiences with Drupal 8 performance so far?

<hr />

<sup>1</sup> Drupal 7's standard profile _doesn't enable the anonymous page cache_ out of the box. You have to enable it manually on the Performance configuration page. This is one area where Drupal 8's initial _out of the box_ experience is actually _faster_ than Drupal 7. Additionally, Drupal 7's anonymous page cache was much less intelligent than Drupal 8's (any content update or comment posting in Drupal 7 resulted in the entire page cache emptying), meaning content updates and page caching in general are much less painful in Drupal 8.

<sup>2</sup> One of the biggest contributors to the slower request routing performance is Drupal 8's use of Symfony components for matching routes, notifying subscribers, etc. [chx's comment](https://www.drupal.org/node/1606794#comment-6534466) on the far-reaching nature of this change was prescient; much of Drupal's basic menu handling and access control had to be adapted to the new (less efficient, but more structured) Symfony-based routing system.
