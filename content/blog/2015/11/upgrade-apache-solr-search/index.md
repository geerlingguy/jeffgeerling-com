---
nid: 2509
title: "Upgrade an Apache Solr Search index from 1.4 to 3.6 (and later versions)"
slug: "upgrade-apache-solr-search"
date: 2015-11-27T05:37:43+00:00
drupal:
  nid: 2509
  path: /blogs/jeff-geerling/upgrade-apache-solr-search
  body_format: full_html
  redirects: []
tags:
  - apache
  - drupal
  - drupal planet
  - error
  - java
  - solr
  - upgrade
aliases:
  - /blogs/jeff-geerling/upgrade-apache-solr-search
---

Recently I had to upgrade someone's Apache Solr installation from 1.4 to 5.x (the current latest version), and for the most part, a Solr upgrade is straightforward, especially if you're doing it for a Drupal site that uses the Search API or Solr Search modules, as the solr configuration files are already upgraded for you (you just need to switch them out when you do the upgrade, making any necessary customizations).

However, I ran into the following error when I tried loading the core running Apache Solr 4.x or 5.x:

```
org.apache.solr.common.SolrException:org.apache.solr.common.SolrException: org.apache.lucene.index.IndexFormatTooOldException: Format version is not supported (resource: MMapIndexInput(path="/var/solr/cores/[corename]/data/spellchecker2/_1m.cfx") [slice=_1m.fdx]): 1 (needs to be between 2 and 3). This version of Lucene only supports indexes created with release 3.0 and later.
```

To fix this, you need to upgrade your index using Solr 3.5.0 or later, then you can upgrade to 4.x, then 5.x (using each version of Solr to upgrade from the previous major version):

<ol>
<li>Run <code>locate lucene-core</code> to find your Solr installation's <code>lucene-core.jar</code> file. In my case, for 3.6.2, it was named <code>lucene-core-3.6.2.jar</code>.</li>
<li>Find the full directory path to the Solr core's data/index.</li>
<li>Stop Solr (so the index isn't being actively written to.</li>
<li>Run the command to upgrade the index: <code>java -cp /full/path/to/lucene-core-3.6.2.jar org.apache.lucene.index.IndexUpgrader -delete-prior-commits -verbose /full/path/to/data/index</code></li>
</ol>

It will take a few seconds for a small index (hundreds of records), or a bit longer for a huge index (hundreds of thousands of records), and then once it's finished, you should be able to start Solr again using the upgraded index. Rinse and repeat for each version of Solr you need to upgrade through.

If you have directories like index, spellchecker, spellchecker1, and spellchecker2 inside your <code>data</code> directory, run the command over each subdirectory to make sure all indexes are updated.

For more info, see the <a href="http://lucene.apache.org/core/4_0_0/core/org/apache/lucene/index/IndexUpgrader.html">IndexUpgrader</a> documentation, and the <a href="http://stackoverflow.com/a/29201721/100134">Stack Overflow answer</a> that instigated this post.
