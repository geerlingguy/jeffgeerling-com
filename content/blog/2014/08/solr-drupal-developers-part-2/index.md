---
nid: 2526
title: "Solr for Drupal Developers, Part 2: Solr and Drupal, A History"
slug: "solr-drupal-developers-part-2"
date: 2014-08-21T13:40:28+00:00
drupal:
  nid: 2526
  path: /blogs/jeff-geerling/solr-drupal-developers-part-2
  body_format: full_html
  redirects: []
tags:
  - apache
  - drupal
  - drupal planet
  - search
  - search api
  - series
  - solr
  - tutorial
---

<em>Posts in this series:</em>

<ul>
<li><a href="http://www.jeffgeerling.com/blogs/jeff-geerling/solr-drupal-developers-part-1">Part 1: Intro to Apache Solr</a></li>
<li><strong>Part 2: Solr and Drupal, A History</strong></li>
<li><a href="http://www.jeffgeerling.com/blogs/jeff-geerling/solr-drupal-developers-part-3">Part 3: Testing Solr locally</a></li>
</ul>

<p>Drupal has included basic site search functionality since its first public release. Search administration was added in Drupal 2.0.0 in 2001, and search quality, relevance, and customization was improved dramatically throughout the Drupal 4.x series, especially in Drupal 4.7.0. Drupal's built-in search provides decent database-backed search, but offers a minimal set of features, and slows down dramatically as the size of a Drupal site grows beyond thousands of nodes.</p>

<p>In the mid-2000s, when most custom search solutions were relatively niche products, and the <a href="http://www.google.com/enterprise/search/products/gsa.html">Google Search Appliance</a> dominated the field of large-scale custom search, Yonik Seeley started working on Solr for CNet Networks. Solr was designed to work with Lucene, and offered fast indexing, extremely fast search, and as time went on, other helpful features like distributed search and geospatial search. Once the project was open-sourced and released under the Apache Software Foundation's umbrella in 2006, the search engine became one of the most popular engines for customized and more performant site search.</p>

<blockquote>
<p>As an aside, I am writing this series of blog posts from the perspective of a Drupal developer who has worked with large-scale, highly customized Solr search for Mercy (<a href="http://www.mercy.net/search/doctor/John?address=St.%20Louis%2C%20MO&amp;distance=50&amp;latlon%5Blat%5D=38.6270025&amp;latlon%5Blon%5D=-90.1994042">example</a>), and with a variety of small-to-medium sites who are using <a href="https://hostedapachesolr.com/">Hosted Apache Solr</a>, a service I've been running as part of Midwestern Mac since early 2011.</p>
</blockquote>

<h2>
<a name="user-content-timeline-of-apache-solr-and-drupal-solr-integration" class="anchor" href="#timeline-of-apache-solr-and-drupal-solr-integration" aria-hidden="true"><span class="octicon octicon-link"></span></a>Timeline of Apache Solr and Drupal Solr Integration</h2>

<iframe src="http://cdn.knightlab.com/libs/timeline/latest/embed/index.html?source=0Aj1MYMiETXzXdGhhOFd5QXdKNGhQa0Nyck9YbGVYb3c&font=DroidSerif-DroidSans&maptype=toner&lang=en&height=400" width='100%' height='400' frameborder='0' style="margin-top: 1em;"></iframe>

<p><em>If you can't view the timeline, please click through and read this article on the website directly.</em></p>

<h2>
<a name="user-content-a-brief-history-of-apache-solr-search-and-search-api-solr" class="anchor" href="#a-brief-history-of-apache-solr-search-and-search-api-solr" aria-hidden="true"><span class="octicon octicon-link"></span></a>A brief history of Apache Solr Search and Search API Solr</h2>

<p>Only two years after Apache Solr was released, the <a href="https://www.drupal.org/project/apachesolr">Apache Solr Search</a> module was created. Originally, the module was written for Drupal 5.x, but it has been actively maintained for many years and was ported to Drupal 6 and 7, with some major rewrites and modifications to keep the module up to date, easy to use, and integrated with all of Apache Solr's new features over time. As Solr gained popularity, many Drupal sites started switching from using core search or heavily customized Views to using Apache Solr.</p>

<p>Seeing this trend, hosted solutions for Solr search were built specifically for Drupal sites. Some of these solutions included Acquia's <a href="http://www.acquia.com/products-services/acquia-search">Acquia Search</a> (<a href="http://www.acquia.com/blog/hosted-solr-site-search-drupal-way">2008</a>), Midwestern Mac's <a href="https://hostedapachesolr.com/">Hosted Apache Solr</a> (<a href="http://www.jeffgeerling.com/blogs/jeff-geerling/hosted-apache-solr-drupal">2011</a>), and Pantheon's <a href="http://helpdesk.getpantheon.com/customer/portal/articles/361249-apache-solr-on-pantheon">Apache Solr service</a>. Acquia, seeing the need for more stability and development in Drupal's Solr integration module, began sponsoring the development of the Apache Solr Search module in April of 2009 (<a href="https://web.archive.org/web/20090517090942/http://drupal.org/project/apacheSolr">wayback machine</a>).</p>

<p>Search API came on the scene after Drupal 7 was released in 2011. Search API promised to be a rethink of search in Drupal. Instead of tying to a particular search technology, a search framework (with modular plugins for indexing, searching, facets, etc.) was written to plug into the Drupal database, Apache Solr, or whatever other systems a Drupal site could integrate with. The Search API Solr module was released shortly thereafter, and both Search API and Search API Solr were written exclusively for Drupal 7.</p>

<p>Both Solr integration solutions—Apache Solr Search and Search API Solr—have been actively developed, and both modules offer a very similar set of features. This led to a few issues during reign of Drupal 7 (still the current version as of this writing):</p>

<ul>
<li>Many site builders wonder: Which module should I use?</li>
<li>Switching site search between the two modules (for example, if you find a feature in one that is not in the other) can be troublesome.</li>
<li>Does corporate sponsorship of one module over the other cause any issues in enterprise adoption, new feature development, or community involvement?</li>
</ul><p>These problems have run their course over the past few years, and cause much confusion. Some add-on modules, like Facet API (which allows you to build facets for your search results), have been abstracted and generalized enough to be used with either search solution, but there are dozens of modules, and hundreds of blog posts, tutorials, and documentation pages written specifically for one module or the other. For Drupal 6 users, there is only one choice (since Search API Solr is only available for Drupal 7), but for Drupal 7 users, this has been a major issue.</p>

<p>Hosted Apache Solr's solr module usage statistics reveal the community's split over the two modules: 46% of the sites using Hosted Apache Solr use the Apache Solr Search module, while 54% of the sites use Search API Solr.</p>

<p>So, is Drupal's Solr community destined to be divided for eternity? Luckily, no! There are many positive trends in the current Solr module development cycle, and some great news regarding Drupal 8.</p>

<h2>
<a name="user-content-uniting-forces" class="anchor" href="#uniting-forces" aria-hidden="true"><span class="octicon octicon-link"></span></a>Uniting Forces</h2>

<p>Already for Drupal 7, the pain of switching between the two modules (or supporting both, as Hosted Apache Solr does) is greatly reduced by the fact that both modules started using a unified set of Apache Solr configuration files (like schema.xml, solrconfig.xml, etc.) as of mid-2012 (see the <a href="https://www.drupal.org/sandbox/cpliakas/1600962">Apache Solr Common Configurations</a> sandbox project).</p>

<p>Additionally, development of add-on modules like Facet API and the like has been generalized so the features can be used <em>today</em> with either search solution with minimal effort.</p>

<h3>
<a name="user-content-a-brighter-future" class="anchor" href="#a-brighter-future" aria-hidden="true"><span class="octicon octicon-link"></span></a>A Brighter Future</h3>

<p>There's still the problem of two separate modules, two separate sets of APIs, and a divided community effort between the two modules. When Drupal 8 rolls around, that division will be no more! In a 2013 blog post, <a href="http://www.acquia.com/blog/battleplan-search-solr-drupal-8">Nick Veenhof announced</a> that the maintainers of Search API and Apache Solr Search would be working together on a new version of Search API for Drupal 8.</p>

<p>The effort is already underway, as the <a href="http://www.acquia.com/blog/search-api-drupal-8-sprint-june-2014">first Drupal 8 Search API code sprint</a> was held this past June in Belgium, after a successful funding campaign on Drupalfund.us.</p>

<p>The future of Solr and Drupal is bright! Even as other search engines like Elasticsearch are beginning to see more adoption, Apache Solr (which has seen hundreds of new features and greater stability throughout it's 4.x release series) continues to gain momentum as one of the best text search solutions for Drupal sites.</p>
