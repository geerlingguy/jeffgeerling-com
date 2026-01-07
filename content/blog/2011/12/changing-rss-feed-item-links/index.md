---
nid: 2351
title: "Changing RSS Feed item links (and other data) in Drupal 7"
slug: "changing-rss-feed-item-links"
date: 2011-12-14T01:58:46+00:00
drupal:
  nid: 2351
  path: /blogs/jeff-geerling/changing-rss-feed-item-links
  body_format: full_html
  redirects: []
tags:
  - display
  - drupal
  - drupal 7
  - drupal planet
  - hook_node_view
  - node
  - rss
  - snippets
aliases:
  - /blogs/jeff-geerling/changing-rss-feed-item-links
---

You can do a lot of great things with field display in Drupal 7's 'manage display' tab for a content type. You can control the order and label position of each field attached to a node type in that tab for Full node displays, Teasers, and RSS displays (or other displays you set up).

However, there's no way to change certain aspects of a node's display inside an RSS Feed, such as the 'creator' tag, the 'link' tag, or the 'title' tag. For a <a href="http://catholicnewslive.com/">news aggregation site</a> I run, I wanted to modify the <code><link></code> tag when displaying 'story' nodes, and make the link tag give an absolute URL to the original source instead of to my drupal site (so, instead of http://www.mysite.com/node/12, it would go to http://www.example.com/original-story-url).

A lot of blogs also use this kind of format for reposted blog items (such as <a href="http://daringfireball.net/">Daring Fireball</a>), so users go straight to the source when they click on the title of an item in their RSS reader of choice. My method below can be modified to conditionally change a link if a field has a value (say, a 'RSS absolute URL' field or something like that).

For Drupal 6, some people had suggested using <a href="http://drupal.org/project/views_rss">Views RSS</a> for this purpose (it would let me manage a Views-provided feed display with fields instead of using Drupal's built-in node/teaser display), but this module doesn't have a stable D7 release, and it won't help me change things for Drupal's built in feeds.

For Drupal 7, all you need to do is implement <a href="http://api.drupal.org/api/drupal/modules--node--node.api.php/function/hook_node_view/7">hook_node_view()</a> in a custom module, and change the <code>$node->link</code> value to whatever you want:

```
<?php
/**
 * Implements hook_node_view().
 *
 * For story nodes in RSS feeds, use field_story_url for link element.
 */
function custom_node_view($node, $view_mode, $langcode) {
  if ($node->type == 'story' && $view_mode == 'rss') {
    $node->link = $node->field_story_url[$node->language][0]['url'];
  }
}
?>
```

Easy peasy. If you want to conditionally change the feed item <code><link></code> (say, only change the link value if <code>$field_story_url</code> has a value), change the line to:

```
<?php
    $node->link = (empty($node->field_story_url)) ? $node->link : $node->field_story_url[$node->language][0]['url'];
?>
```

You can also change things like <code>$node->title</code> to change what's in the RSS feed's <code><title></code> tag.
