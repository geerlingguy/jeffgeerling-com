---
nid: 2623
title: "Blog post id enumeration can lead to unwanted information disclosure"
slug: "blog-post-id-enumeration-can-lead-unwanted-information-disclosure"
date: 2016-02-29T03:05:28+00:00
drupal:
  nid: 2623
  path: /blog/2016/blog-post-id-enumeration-can-lead-unwanted-information-disclosure
  body_format: markdown
  redirects: []
tags:
  - blogs
  - disclosure
  - drupal
  - drupal planet
  - information
  - raspberry pi
  - security
  - wordpress
---

With the rampant speculation there will be a new Raspberry Pi model released next week, I was wondering if the official Raspberry Pi blog might reveal anything of interest; they just posted a [Four Years of Pi](https://www.raspberrypi.org/blog/four-years-of-pi/) blog post on the 26th, which highlighted the past four years, and mentioned the excitement surrounding 4th anniversary of Pi sales, coming up on February 29th, 2016.

Glancing at the blog's source, I noticed it looks like a Wordpress blog (using [httpie](https://github.com/jkbrzt/httpie) on the cli):

```
$ http https://www.raspberrypi.org/blog/four-years-of-pi/ | grep generator
<meta name="generator" content="WordPress 4.4.2" />
```

Having set up a few WP sites in the past, I knew there was a simple way to load content by its ID, using a URL in the form:

```
https://www.example.org/?p=[post-id-here]
```

Trying this on the RPi blog, I put in the post ID of the latest blog post, which is set as a class on the `<body>` tag: `postid-20167`: [https://www.raspberrypi.org/?p=20167](https://www.raspberrypi.org/?p=20167)

This URL redirects to the pretty URL (yay for good SEO, at least :), so this means if I can put in other IDs, and get back valid pages (or just valid redirects), I can start _enumerating_ the post IDs and seeing what I can find. Checking a few other IDs gets some interesting images, a few 404s with no redirects... and eventually, a 404 _after_ a redirect, with a fairly large spoiler (well, not so large if you're following Raspberry Pi news almost anywhere this weekend!).

```
$ http head https://www.raspberrypi.org/?p=[redacted]
HTTP/1.1 301 Moved Permanently
Location: https://www.raspberrypi.org/[redacted]
```

If I load the 'Location' URL, I get:

```
$ http head https://www.raspberrypi.org/[redacted]
HTTP/1.1 404 Not Found
```

So... for SEO purposes, it's best to either drop the `?p=[id]` format, or redirect it to the pretty URL. However, for information security, this redirect should _only_ happen if the content is published, because it can lead (like we see here) to information disclosure.

Other CMSes like Drupal and Joomla (or most any other CMS/custom CMS I've seen) can also suffer from the same enumeration problem, and I know at least for Drupal, there are tools like [Username Enumeration Prevention](https://www.drupal.org/project/username_enumeration_prevention) for usernames and [m4032404](https://drupal.org/project/m4032404) for other content. Another way to work around this particular problem is to stage content in a non-production environment, and only have the content exist in production at all once it's published.

Note that enumeration by ID (posts, users, etc.) is not necessarily considered a security vulnerability (and it's really not... it's not like someone can hack your site using this attack). But it can lead to unwanted information leakage.
