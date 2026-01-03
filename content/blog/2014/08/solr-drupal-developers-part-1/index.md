---
nid: 2522
title: "Solr for Drupal Developers, Part 1: Intro to Apache Solr"
slug: "solr-drupal-developers-part-1"
date: 2014-08-11T18:42:50+00:00
drupal:
  nid: 2522
  path: /blogs/jeff-geerling/solr-drupal-developers-part-1
  body_format: full_html
  redirects: []
tags:
  - apache
  - drupal
  - drupal planet
  - search
  - series
  - solr
  - tutorial
aliases:
  - /blogs/jeff-geerling/solr-drupal-developers-part-1
---

<em>Posts in this series:</em>

<ul>
<li><strong>Part 1: Intro to Apache Solr</strong></li>
<li><a href="http://www.jeffgeerling.com/blogs/jeff-geerling/solr-drupal-developers-part-2">Part 2: Solr and Drupal, A History</a></li>
<li><a href="http://www.jeffgeerling.com/blogs/jeff-geerling/solr-drupal-developers-part-3">Part 3: Testing Solr locally</a></li>
</ul>

<p>It's common knowledge in the Drupal community that <a href="http://lucene.apache.org/solr/">Apache Solr</a> (and other text-optimized search engines like <a href="http://www.elasticsearch.org/">Elasticsearch</a>) blow database-backed search out of the water in terms of speed, relevance, and functionality. But most developers don't really know <em>why</em>, or just <em>how much</em> an engine like Solr can help them.</p>

<p>I'm going to be writing a series of blog posts on Apache Solr and Drupal, and while some parts of the series will be very Drupal-centric, I hope I'll be able to illuminate why Solr itself (and other search engines like it) are so effective, and why you should be using them instead of simple database-backed search (like Drupal core's Search module uses by default), even for small sites where search isn't a primary feature.</p>

<blockquote>
<p>As an aside, I am writing this series of blog posts from the perspective of a Drupal developer who has worked with large-scale, highly customized Solr search for Mercy (<a href="http://www.mercy.net/search/doctor/John?address=St.%20Louis%2C%20MO&amp;distance=50&amp;latlon%5Blat%5D=38.6270025&amp;latlon%5Blon%5D=-90.1994042">example</a>), and with a variety of small-to-medium sites who are using <a href="https://hostedapachesolr.com/">Hosted Apache Solr</a>, a service I've been running as part of Midwestern Mac since early 2011.</p>
</blockquote>

<h2>
<a name="user-content-why-not-database" class="anchor" href="#why-not-database" aria-hidden="true"><span class="octicon octicon-link"></span></a>Why not Database?</h2>

<p>Apache Solr's wiki leads off it's <a href="http://wiki.apache.org/solr/WhyUseSolr">Why Use Solr</a> page with the following:</p>

<blockquote>
<p>If your use case requires a person to type words into a search box, you want a text search engine like Solr.</p>
</blockquote>

<p>At a basic level, databases are optimized for storing and retrieiving bits of data, usually either a record at a time, or in batches. And <em>relational</em> databases like MySQL, MariaDB, PostgreSQL, and SQLite are set up in such a way that data is stored in various tables and fields, rather than in one large bucket per record.</p>

<p>In Drupal, a typical node entity will have a title in the <code>node</code> table, a body in the <code>field_data_body</code> table, maybe an image with a description in another table, an author whose name is in the <code>users</code> table, etc. Usually, you want to allow users of your site to enter a keyword in a search box and search through all the data stored across <em>all</em> those fields.</p>

<p>Drupal's Search module avoids making ugly and slow search queries by building an <em>index</em> of all the search terms on the site, and storing that index inside a <em>separate</em> database table, which is then used to map keywords to entities that match those keywords. Drupal's venerable <em>Views</em> module will even enable you to bypass the search indexing and search directly in multiple tables for a certain keyword.</p>

<p>So what's the downside to database-backed search? Mainly, performance. Databases are built to be efficient query engines—provide a specific set of parameters, and the database returns a specific set of data. Most databases are not optimized for arbitrary string-based search. Queries where you use <code>LIKE '%keyword%'</code> are not that well optimized, and will be slow—especially if the query is being used across multiple <code>JOIN</code>ed tables! And even if you use the Search module or some other method of pre-indexing all the keyword data, relational databases will still be less efficient (and require much more work on a developer's part) for arbitrary text searches.</p>

<p>If you're simply building lists of data based on very specific parameters (especially where the conditions for your query all utilize speedy indexes in the database), a relational database like MySQL will be highly effective. But usually, for search, you don't just have a couple options and maybe a custom sort—you have a keyword field (primarily), and end users have high expectations that they'll find what they're looking for by simply entering a few keywords and clicking 'Search'.</p>

<h2>
<a name="user-content-why-solr" class="anchor" href="#why-solr" aria-hidden="true"><span class="octicon octicon-link"></span></a>Why Solr?</h2>

<p>What makes Solr different? Well, Solr is optimized <em>specifically</em> for text-based search. The <a href="http://lucene.apache.org/">Lucene</a> text search engine that runs behind Apache Solr is built to be incredibly efficient and also offers some other really useful tools for searching. Apache Solr adds some cool features on top of Lucene, like:</p>

<ul>
<li>Efficient and fast search indexing.</li>
<li>Simple search sorting on any field.</li>
<li>Search ranking based on some simple rules (over which you have complete control).</li>
<li>Multiple-index searching.</li>
<li>Features like facets, text highlighting, grouping, and document indexing (PDF, Word, etc.).</li>
<li>Geospatial search (searching based on location).</li>
</ul><p>Some of these things may seem a little obtuse, and it's likely that you don't need every one of these features on your site, but it's nice to know that Solr is flexible enough to allow you to do almost anything you want with your site search.</p>

<p>These general ideas are great, but in order to really understand what benefits Solr offers, let's look at what happens with a basic search in Apache Solr.</p>

<h2>
<a name="user-content-simple-explanation-of-how-solr-performs-a-search" class="anchor" href="#simple-explanation-of-how-solr-performs-a-search" aria-hidden="true"><span class="octicon octicon-link"></span></a>Simple Explanation of how Solr performs a search</h2>

<p>This is a very basic overview, leaving out many technical details, but I hope it will help you understand what's going on behind the scenes at a basic level.</p>

<p>When searching with a database-backed search, the database says, "give me a few keywords, and I'll find exact matches for those words," and it only covers a few very specific bits of data (like title, body, and author). Searching with Solr is more nuanced, flexible, and powerful.</p>

<h3>
<a name="user-content-step-1---indexing-search-data" class="anchor" href="#step-1---indexing-search-data" aria-hidden="true"><span class="octicon octicon-link"></span></a>Step 1 - Indexing search data</h3>

<p>First, when Solr builds an index of all the content on your site, it gathers all the content's data—each entity's title, body, tags, and any other textual information related to the entity. While reading through all this textual information, Solr does some neat things, like:</p>

<ul>
<li>Stemming: taking a word like "baseballs" and adding in 'word stems' like "baseball".</li>
<li>Stop Word filtering: Removing words with little search relevance like "a", "the", "of", etc.</li>
<li>Normalization: Converting special characters to simpler forms (like ü to u and ê to e so search can work more intuitively).</li>
<li>Synonym expansion: Adding synonyms to words, so the words "doctor" and "practitioner" could be equivalent in a search, even if only one word appears in the content.</li>
</ul><p>These functions are collectively known as <a href="http://lucene.apache.org/core/4_9_0/core/org/apache/lucene/analysis/package-summary.html#package_description"><em>tokenization</em></a>, and are actually performed by Lucene, the engine running under Solr. You don't need to know what all this means right now, but basically, if your content has the word "baseball" in it, and a user searches for "baseballs" or "stickball", the "baseball" result will be returned.</p>

<h3>
<a name="user-content-step-2---searching-with-keywords" class="anchor" href="#step-2---searching-with-keywords" aria-hidden="true"><span class="octicon octicon-link"></span></a>Step 2 - Searching with keywords</h3>

<p>Second, when someone enters keywords to perform a search, Solr does a few things before it starts the actual search. We'll take the example below and run through what happens:</p>


```
Baseball hall of fame
```

<p>The first thing Solr does is splits the search into groupings: first the entire string, then all but one word in every combination, then all but two words in every combination, and so on, until it gets to individual words. Just like with indexing, Solr will even take individual words like "hall" and split that word out into "halls", "hall", etc. (basically any kind of related term/plural/singular/etc.).</p>

<p>So now, at this point, your above search looks kind of like you actually searched for:</p>

<p>"baseball hall of fame"
"baseball hall"
"baseball fame"
"baseballs"
"halls"
...
"baseball"</p>

<p>I've skipped many derivatives for clarity, but basically Solr does a little work on the entered keywords to make sure you're going to get results that are relavant for the terms you entered.</p>

<h3>
<a name="user-content-step-3---executing-the-search" class="anchor" href="#step-3---executing-the-search" aria-hidden="true"><span class="octicon octicon-link"></span></a>Step 3 - Executing the search</h3>

<p>Finally, the search engine takes every one of the parsed keywords, and scores them against every piece of content in the index. Each piece of content then gets a score (higher for the number of possible matches, zero if no terms were matched). Then your search result shows all those results, ranked by how relevant they are to the current search.</p>

<p>If you had an entity with the title "Baseball Hall of Fame", it's likely that would be the top result. But some other content may match on parts or combinations of the keywords, so they'll <em>also</em> show up in the search.</p>

<p>If you know better than the search engine, and only want results that <em>exactly match</em> your search, you can enclose your keywords in quotes, so you would <em>only</em> get results with the exact string <code>baseball hall of fame</code>, and nothing that mentions 'hall of fame' or 'baseball' independently.</p>

<p>Solr also adds in a few nifty features when it returns the search results (or lack thereof); it will give back spelling suggestions, which are based on whether any words in the search index are very close matches to the words or phrase you entered in the keywords, and it will also highlight the matched words or word parts in the actual search result.</p>

<h2>
<a name="user-content-summary" class="anchor" href="#summary" aria-hidden="true"><span class="octicon octicon-link"></span></a>Summary</h2>

<p>In a nutshell, this post explained how Apache Solr works by indexing, tokenizing, and searching your content. If you read through the entire post, you even have a basic understanding of <a href="https://en.wikipedia.org/wiki/Levenshtein_distance">Levenshtein distance</a>, <a href="https://en.wikipedia.org/wiki/Approximate_string_matching">approximate string matching</a>, and <a href="https://en.wikipedia.org/wiki/Concept_Search">concept search</a>, and can get started building your own Google :)</p>

<p>I'll be diving much more deeply into Apache Solr as time allows, highlighting especially the past, present, and future of Apache Solr and Drupal, as well as ways you can make Apache Solr integrate more seamlessly and effectively with your site, perform better, and do exactly what you want it to do.</p>
