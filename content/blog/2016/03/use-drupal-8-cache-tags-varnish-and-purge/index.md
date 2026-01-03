---
nid: 2638
title: "Use Drupal 8 Cache Tags with Varnish and Purge"
slug: "use-drupal-8-cache-tags-varnish-and-purge"
date: 2016-03-22T16:52:45+00:00
drupal:
  nid: 2638
  path: /blog/2016/use-drupal-8-cache-tags-varnish-and-purge
  body_format: markdown
  redirects: []
tags:
  - cache
  - cache expiration
  - cache tags
  - drupal
  - drupal 8
  - drupal planet
  - performance
  - purge
  - varnish
  - varnishadm
  - varnishlog
---

<p style="text-align: center;">{{< figure src="./varnish-cache-hit.png" alt="Varnish cache hit in Drupal 8" width="311" height="92" >}}</p>

Over the past few months, I've been reading about BigPipe, Cache Tags, Dynamic Page Cache, and all the other amazing-sounding new features for performance in Drupal 8. I'm working on a blog post that more comprehensively compares and contrasts Drupal 8's performance with Drupal 7, but that's a topic for another day. In this post, I'll focus on [cache tags in Drupal 8](https://www.drupal.org/developing/api/8/cache/tags), and particularly their use with [Varnish](https://www.varnish-cache.org/) to make cached content expiration much easier than it ever was in Drupal 7.

## Purging and Banning

Varnish and Drupal have long had a fortuitous relationship; Drupal is a flexible CMS that takes a good deal of time (relatively speaking) to generate a web page. Varnish is an HTTP reverse proxy that excels at sending a cached web page extremely quickly—and scaling up to thousands or more requests per second even on a relatively slow server. For many Drupal sites, using Varnish to make the site hundreds or thousands of times faster is a no-brainer.

But there's an [adage in programming](http://martinfowler.com/bliki/TwoHardThings.html) that's always held true:

> There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.

Cache invalidation is rightly positioned as the first of those two (three!) hard things. Anyone who's set up a complex Drupal 7 site with dozens of views, panels pages, panelizer layouts, content types, and configured Cache expiration, Purge, Acquia Purge, Varnish, cron and Drush knows what I'm talking about. There are seemingly always cases where someone edits a piece of content then complains that it's not updating in various places on the site.

The traditional answer has been to reduce the TTL for the caching; some sites I've seen only cache content for 30 seconds, or at most 15 minutes, because it's easier than accounting for every page where a certain type of content or menu will change the rendered output.

In Varnish, PURGE requests have been the de-facto way to deal with this problem for years, but it can be a complex task to purge all the right URLs... and there could be hundreds or thousands of URLs to purge, meaning Drupal (in combination with Purge/Acquia Purge) would need to churn through a massive queue of purge requests to send to Varnish.

Drupal 8 adds in a ton of _cacheability metadata_ to all rendered pages, which is aggregated from all the elements used to build that page. Is there a search block on the page? There will be a `config:block.block.bartik_search` cache tag added to the page. Is the main menu on the page? There will be a `config:system.menu.main` cache tag, and so on.

Adding this data to every page allows us to do _intelligent cache invalidation_. Instead of us having to tell Varnish which particular URLs need to be invalidated, when we update anything in the main menu, we can tell Varnish "invalidate all pages that have the `config:system.menu.main` cache tag, using a BAN instead of a PURGE. If you're running Varnish 4.x, all you need to do is add some changes to your VCL to support this functionality, then configure the [Purge](https://www.drupal.org/project/purge) and [Generic HTTP Purger](https://www.drupal.org/project/purge_purger_http) modules in Drupal.

Whereas Varnish would process PURGE requests immediately, dropping cached pages matching the PURGE URL, Varnish can more intelligently match BAN requests using regular expressions and other techniques against any cached content. You have to tell Varnish exactly what to do, however, so there are some changes required in your VCL.

## Varnish VCL Changes

Borrowing from the well-documented [FOSHttpCache](http://foshttpcache.readthedocs.org/en/stable/varnish-configuration.html#tagging) VCL example, you need to make the following changes in your Varnish VCL (see the [full set of changes](https://github.com/geerlingguy/drupal-vm/pull/525/files) that were made to Drupal VM's VCL template):

Inside of `vcl_recv`, you need to add some logic to handle incoming BAN requests:

```
sub vcl_recv {
    ...
    # Only allow BAN requests from IP addresses in the 'purge' ACL.
    if (req.method == "BAN") {
        # Same ACL check as above:
        if (!client.ip ~ purge) {
            return (synth(403, "Not allowed."));
        }

        # Logic for the ban, using the Purge-Cache-Tags header. For more info
        # see https://github.com/geerlingguy/drupal-vm/issues/397.
        if (req.http.Purge-Cache-Tags) {
            ban("obj.http.Purge-Cache-Tags ~ " + req.http.Purge-Cache-Tags);
        }
        else {
            return (synth(403, "Purge-Cache-Tags header missing."));
        }

        # Throw a synthetic page so the request won't go to the backend.
        return (synth(200, "Ban added."));
    }
}
```

The above code basically inspects BAN requests (e.g. `curl -X BAN http://127.0.0.1:81/ -H "Purge-Cache-Tags: node:1"`), then passes along a new `ban()` if the request comes from the acl `purge` list, and if the `Purge-Cache-Tags` header is present. In this case, the ban is set using a regex search inside stored cached object's `obj.http.Purge-Cache-Tags` property. Using this property (on `obj` instead of `req`) allows Varnish's _ban lurker_ to clean up ban requests more efficiently, so you don't end up with thousands (or millions) of stale ban entries. Read more about Varnish's [ban lurker](http://info.varnish-software.com/blog/ban-lurker).

Inside of `vcl_backend_response`, you can add a couple extra headers to help the ban lurker (and, potentially, allow you to make more flexible ban logic should you choose to do so):

```
 sub vcl_backend_response {
    # Set ban-lurker friendly custom headers.
    set beresp.http.X-Url = bereq.url;
    set beresp.http.X-Host = bereq.http.host;
    ...
}
```

Then, especially for production sites, you should make sure Varnish doesn't pass along all the extra headers needed to make Cache Tags work (unless you want to see them for debugging purposes) inside `vcl_deliver`:

```
sub vcl_deliver {
    # Remove ban-lurker friendly custom headers when delivering to client.
    unset resp.http.X-Url;
    unset resp.http.X-Host;
    unset resp.http.Purge-Cache-Tags;
    ...
}
```

At this point, if you add these changes to your site's VCL and restart Varnish, Varnish will be ready to handle cache tags and expire content more efficiently with Drupal 8.

## Drupal Purge configuration

First of all, so that external caches like Varnish know they are safe to cache content, you need to set a value for the 'Page cache maximum age' on the Performance page (`admin/config/development/performance`). You can configure Varnish or other reverse proxies _under your control_ to cache for as long or short a period of time as you want, but a good rule-of-thumb default is 15 minutes—even with cache tags, clients cache pages based on this value until the user manually refreshes the page:

<p style="text-align: center;">{{< figure src="./1-set-page-cache-max-age.png" alt="Set page cache maximum age" width="427" height="211" class="insert-image" >}}</p>

Now we need to make sure Drupal does two things:

  1. Send the `Purge-Cache-Tags` header with every request, containing a space-separated list of all the page's cache tags.
  2. Send a BAN request with the appropriate cache tags whenever content or configuration is updated that should expire pages with the associated cache tags.

Both of these can be achieved quickly and easily by enabling and configuring the [Purge](https://www.drupal.org/project/purge) and [Generic HTTP Purger](https://www.drupal.org/project/purge_purger_http) modules. I used `drush en -y purge purge_purger_http` to install the modules on my Drupal 8 site running inside [Drupal VM](http://www.drupalvm.com/).

Purge automatically sets the `http.response.debug_cacheability_headers` property to `true` via it's `purge.services.yml`, so Step 1 above is taken care of. (Note that if your site uses it's own `services.yml` file, the `http.response.debug_cacheability_headers` setting defined in _that_ file will override Purge's settings—so make sure it's set to `true` if you define settings via `services.yml` on your site!)

> Note that you currently (as of March 2016) need to use the -dev release of Purge until 8.x-3.0-beta4 or later, as it sets the `Purge-Cache-Tags` header properly.

For step 2, you need to add a 'purger' that will send the appropriate BAN requests using purge_purger_http: visit the Purge configuration page, `admin/config/development/performance/purge`, then follow the steps below:

  1. Add a new purger by clicking the 'Add Purger' button:
    {{< figure src="./2-add-purger.png" alt="Add Purger" width="574" height="457" class="insert-image" >}}
  2. Choose 'HTTP Purger' and click 'Add':
    {{< figure src="./3-http-purger.png" alt="HTTP Purger" width="650" height="210" class="insert-image" >}}
  3. Configure the Purger's name ("Varnish Purger"), Type ("Tag"), and Request settings (defaults for Drupal VM are hostname `127.0.0.1`, port `81`, path `/`, method `BAN`, and scheme `http`):
    {{< figure src="./4-http-purger-request.png" alt="Configure HTTP purger request settings" width="650" height="528" class="insert-image" >}}
  4. Configure the Purger's headers (add one header `Purge-Cache-Tags` with the value `[invalidation:expression]`):
    {{< figure src="./5-http-purger-header-cache-tags.png" alt="Configure HTTP purger header settings" width="650" height="502" class="insert-image" >}}<br />**Note: Don't use the header in the screenshot—use `Purge-Cache-Tags`!**

## Testing cache tags

Now that you have an updated VCL and a working Purger, you should be able to do the following:

  1. Send a request for a page and refresh a few times to make sure Varnish is caching it:

```
$ curl -s --head http://drupalvm.dev:81/about | grep X-Varnish
X-Varnish: 98316 65632
X-Varnish-Cache: HIT
```

  2. Edit that page, and save the edit.
  3. Run `drush p-queue-work` to process the purger queue:

```
$ drush @drupalvm.drupalvm.dev p-queue-work
Processed 5 objects...
```

  4. Send another request to the same page and verify that Varnish has a cache MISS:

```
$ curl -s --head http://drupalvm.dev:81/about | grep X-Varnish
X-Varnish: 47
X-Varnish-Cache: MISS
```

  5. After the next request, you should start getting a HIT again:

```
$ curl -s --head http://drupalvm.dev:81/about | grep X-Varnish
X-Varnish: 50 48
X-Varnish-Cache: HIT
```

You can also use Varnish's built in tools like [varnishadm](https://www.varnish-cache.org/docs/3.0/reference/varnishadm.html) and [varnishlog](https://www.varnish-cache.org/docs/3.0/reference/varnishlog.html) to verify what's happening. Run these commands from the Varnish server itself:

```
# Watch the detailed log of all Varnish requests.
$ varnishlog
[wall of text]

# Check the current list of Varnish bans.
$ varnishadm
varnish> ban.list
200        
Present bans:
1458593353.734311     6    obj.http.Purge-Cache-Tags ~ block_view

# Check the current parameters.
varnish> param.show
...
ban_dups                   on [bool] (default)
ban_lurker_age             60.000 [seconds] (default)
ban_lurker_batch           1000 (default)
ban_lurker_sleep           0.010 [seconds] (default)
...
```

If you're interested in going a little deeper into general Varnish debugging, read my earlier post, [Debugging Varnish VCL configuration files](/blogs/jeff-geerling/debugging-varnish-vcl).

## Other notes and further reading

I spent a few days exploring cache tags, and how they work with Varnish, Fastly, CloudFlare, and other services with Drupal 8, as part of [adding cache tag support to Drupal VM](https://github.com/geerlingguy/drupal-vm/issues/397). Here are some other notes and links to further reading so you can go as deep as you want into cache tags in Drupal 8:

  - If you're building custom Drupal modules or renderable arrays, make sure you add cacheability metadata so all the cache tag magic _just works_ on your site! See the official documentation for [Cacheability of render arrays](https://www.drupal.org/developing/api/8/render/arrays/cacheability).
  - The [Varnish](https://www.drupal.org/project/varnish) module is actively being [ported to Drupal 8](https://www.drupal.org/node/2365949), and could offer an alternative option for using cache tags with Drupal 8 and Varnish.
  - Read the official Varnish documentation on [Cache Invalidation](http://book.varnish-software.com/4.0/chapters/Cache_Invalidation.html#purge-vs-bans-vs-hashtwo-vs-cache-misses), especially regarding the effectiveness and performance of using Bans vs Purges vs Hashtwo vs. Cache misses.
  - There's an ongoing meta issue to [profile and rationalize cache tags](https://www.drupal.org/node/2241377) in Drupal 8, and the conversation there has a lot of good information about cache tag usage in the wild, caveats with header payload size and hashing, etc.
  - As mentioned earlier, if you have a `services.yml` file for your site, make sure you set `http.response.debug_cacheability_headers: true` inside (see note [here](https://github.com/geerlingguy/drupal-vm/issues/397#issuecomment-199860436)).
  - Read more about [Varnish bans](https://www.varnish-cache.org/docs/trunk/users-guide/purging.html#bans)
  - Read more about [Drupal 8 cache tags](https://www.drupal.org/developing/api/8/cache/tags)
  - Read a case study of cache tags (with Fastly) dramatically [speeding up a large Drupal 8 site](http://www.md-systems.ch/en/blog/2015-10/successful-relaunch-of-letemps-ch).
  - Be careful with your ban logic in the VCL; you need to avoid using regexes on `req` to allow the ban lurker to efficiently process bans (see [Why do my bans pile up?](https://www.varnish-cache.org/forum/topic/1128)).
  - If you find Drupal 8's `cache_tags` database table is growing very large, please check out the issue [Garbage collection for cache tag invalidations](https://www.drupal.org/node/2250033). For now, you can safely truncate that table from time to time if needed.
