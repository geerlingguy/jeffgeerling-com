---
nid: 2899
title: "Hosted Apache Solr now supports Drupal Search API 8.x-2.x, Solr 7.x"
slug: "hosted-apache-solr-now-supports-drupal-search-api-8x-2x-solr-7x"
date: 2018-12-19T16:50:13+00:00
drupal:
  nid: 2899
  path: /blog/2018/hosted-apache-solr-now-supports-drupal-search-api-8x-2x-solr-7x
  body_format: markdown
  redirects: []
tags:
  - docker
  - drupal
  - drupal 8
  - drupal planet
  - hosted apache solr
  - open source
  - search api
  - solr
---

Earlier this year, I completely [revamped Hosted Apache Solr's architecture](https://www.jeffgeerling.com/blog/2018/hosted-apache-solrs-revamped-docker-based-architecture), making it more resilient, more scalable, and better able to support having different Solr versions and configurations per customer.

Today I'm happy to officially announce support for Solr 7.x (in addition to 4.x). This means that no matter what version of Drupal you're on (6, 7, or 8), and no matter what Solr module/version you use (Apache Solr Search or Search API Solr 1.x or 2.x branches), Hosted Apache Solr is optimized for your Drupal search!

{{< figure src="./solr-version-selection-hosted-apache-solr.png" alt="Hosted Apache Solr - version selection" width="650" height="244" class="insert-image" >}}

This post isn't just a marketing post, though—I am also officially announcing that the actual Docker container images used to run your search cores are free and open source, and available for anyone to use (yes, even if you don't pay for a Hosted Apache Solr subscription!). I maintain a variety of Solr versions, from 3.6.x (I still use it to support some annoyingly-outdated Magento 1.x sites which only work with 3.6.x) to 7.x and everything in between, and there are instructions for using the Solr containers with your own projects (even in production if you'd like!) in the source code repository:

  - [`geerlingguy/solr`](https://hub.docker.com/r/geerlingguy/solr/) - Docker container tagged with many different Solr versions.
  - [Solr Container project on GitHub](https://github.com/geerlingguy/solr-container) - The source code used to build all the Solr version Docker images.

You can add a subscription to supercharge your Drupal site's search—no matter what version you want—over at [hostedapachesolr.com](https://hostedapachesolr.com).

(Aside: Within the first quarter of 2018, we will also add support for changing Solr versions at-will!)
