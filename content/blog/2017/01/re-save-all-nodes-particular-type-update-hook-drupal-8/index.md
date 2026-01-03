---
nid: 2734
title: "Re-save all nodes of a particular type in an update hook in Drupal 8"
slug: "re-save-all-nodes-particular-type-update-hook-drupal-8"
date: 2017-01-16T22:33:32+00:00
drupal:
  nid: 2734
  path: /blog/2017/re-save-all-nodes-particular-type-update-hook-drupal-8
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
---

I recently needed to re-save all the nodes of a particular content type (after I had added some fields and default configuration) as part of a Drupal 8 site update and deployment. I could go in after deploying the new code and configuration, and manually re-save all content using the built-in bulk operation available on the `/admin/content` page, but that would not be ideal, because there would be a period of time where the content isn't updated on the live site—plus, manual processes are fragile and prone to failure, so I avoid them at all costs.

In my Drupal 8 module, called `custom`, I added the following update hook, inside `custom.install`:

```
<?php
// Add this line at the top of the .install file.
use Drupal\node\Entity\Node;

/**
 * Re-save all Article content.
 */
function custom_update_8002() {
  // Get an array of all 'article' node ids.
  $article_nids = \Drupal::entityQuery('node')
    ->condition('type', 'article')
    ->execute();

  // Load all the articles.
  $articles = Node::loadMultiple($article_nids);
  foreach ($articles as $article) {
    $article->save();
  }
}
?>
```

Though Drupal 8's configuration management system allows almost any config changes to be made without update hooks nowadays... I find I still need to use update hooks on many sites to deploy updates that affect the way a theme or a view displays content on the site (especially when adding new fields to existing content types).
