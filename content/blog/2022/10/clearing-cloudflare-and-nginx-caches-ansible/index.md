---
nid: 3241
title: "Clearing Cloudflare and Nginx caches with Ansible"
slug: "clearing-cloudflare-and-nginx-caches-ansible"
date: 2022-10-05T17:35:54+00:00
drupal:
  nid: 3241
  path: /blog/2022/clearing-cloudflare-and-nginx-caches-ansible
  body_format: markdown
  redirects: []
tags:
  - ansible
  - cache
  - cache expiration
  - cloudflare
  - devops
  - drupal
  - nginx
  - purge
  - varnish
---

Since being DDoS continuously earlier this year, I've set up extra caching in front of my site. Originally I just had Nginx's proxy cache, but that topped out around 100 Mbps of continuous bandwidth and maybe 5-10,000 requests per second on my little DigitalOcean VPS.

So then I added Cloudflare's proxy caching service on top, and now I've been able to handle months with 5-10 TB of traffic (with multiple spikes of hundreds of mbps per second).

That's great, but caching comes with a tradeoff—any time I post a new article, update an old one, or a post receives a comment, it can take anywhere between 10-30 minutes before that change is reflected for end users.

I used to use Varnish, and with Varnish, you could configure cache purges directly from Drupal, so if any operation occurred that would invalidate cached content, Drupal could easily purge just that content from Varnish's cache.

Nginx—at least the open source/community version—doesn't have fine grained cache purge controls. So my process is basically, "nuke `/var/cache/nginx` and reload the Nginx service." But I don't want this Drupal website to have the permission to touch that folder or manage services running on the server. This isn't Wordpress we're dealing with, where that kind of cowboy coding is commonplace!

And for Cloudflare, it's easy enough to whip up some code in Drupal to call out to Cloudflare's [`purge_cache` API endpoint](https://api.cloudflare.com/#zone-purge-files-by-url). But instead of doing that, I wanted one proverbial 'button' to press to clear out both Nginx _and_ Cloudflare at the same time.

And so, it's Ansible to the rescue!

Using the playbook below, I can run it, and within a few seconds, have all the caches updated worldwide, so my shiny new/updated content is ready for everyone to see.

<script src="https://gist.github.com/geerlingguy/0e3423ba23f21d1f184b09cbc8a8391d.js"></script>

I haven't yet wired this to Drupal, though, so there's still one manual process involved (hitting 'go' on the playbook). I might never wire it up, because I don't particularly like giving web applications access to backend systems if I can avoid it.

For more details, check out the [original GitHub issue](https://github.com/geerlingguy/jeffgeerling-com/issues/150) where I implemented this playbook for my website.
