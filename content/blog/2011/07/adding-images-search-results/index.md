---
nid: 2344
title: "Adding Images to Search Results (Drupal Search)"
slug: "adding-images-search-results"
date: 2011-07-02T17:44:03+00:00
drupal:
  nid: 2344
  path: /blogs/jeff-geerling/adding-images-search-results
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 6
  - drupal 7
  - drupal planet
  - results
  - search
  - solr
  - templates
aliases:
  - /blogs/jeff-geerling/adding-images-search-results
---

For a while (earlier in my Drupal career), I was avoiding adding imagefield-attached images to nodes that appeared in my search results, because I remember the first time I tried doing so, I was still quite confused by the way drupal handled search results theming.

Well, after another crack at it, I finally have a nice, performant way of displaying images from nodes added via imagefields (or in drupal 7, image fields) inline with search results, and it didn't require much work at all!

<p style="text-align: center;"><a href="http://www.lolsaints.com/search/apachesolr_search/flies">{{< figure src="./lolsaints-image-search-result.png" alt="Images in Search Results" width="528" height="434" >}}</a></p>

The image above shows inline images for <a href="http://www.lolsaints.com/">LOLSaints.com</a>, a site which uses <a href="http://www.jeffgeerling.com/services/hosted-solr-search">Midwestern Mac's Hosted Apache Solr search service</a> to return results quickly and allows faceting, etc. using the excellent <a href="http://drupal.org/project/apachesolr">Apache Solr Search Integration</a> module. But the technique I'm using works equally well with built-in (but slower) Drupal core search module's results.

<h3>Step 1 - Preprocess the search result to get the image data</h3>

The first thing you'll need to do is add something along the lines of the following into your theme's template.php file (if there's no template.php file in your current theme, add your own, and just paste in what's below). Change the 'THEMENAME' text to your theme's name:</p>

```
<?php
/**
 * Process variables for search-result.tpl.php.
 *
 * @see search-result.tpl.php
 */
function THEMENAME_preprocess_search_result(&$variables) {
  // Add node object to result, so we can display imagefield images in results.
  $n = node_load($variables['result']['node']->nid);
  $n && ($variables['node'] = $n);
}
?>
```

This code basically grabs the node id (nid) of the node being displayed, loads the full node object, and sends the node object over to your search result template, which we'll modify next... (note: if you're displaying tons of nodes per page in your search results, this can be a little taxing. I usually limit it to 10-15 results per page).

<h3>Step 2 - Modify search-result.tpl.php to display the image</h3>

Next, find the 'search-result.tpl.php' file in drupal core (located in core's modules/search folder), make a copy named exactly the same inside your theme's folder (or inside a 'templates' folder in your theme's folder), and add something like the following wherever you'd like the picture to show up (for my example, I was using an imagefield named 'field_article_image').

```
<code>
<?php if (isset($node->field_article_image[0]['filepath'])): ?>
```

  <span class="search-image"><code>
<?php print theme('imagecache', 'search-thumb', $node->field_article_image[0]['filepath']); ?>
</code></span>

```
<?php endif; ?>
```

</code>

For Drupal 6, you can print the image using imagecache at whatever size you want using something like the theme() function I used above. I'll leave it up to the reader to implement the proper theme function for image styles in Drupal 7 :-)
