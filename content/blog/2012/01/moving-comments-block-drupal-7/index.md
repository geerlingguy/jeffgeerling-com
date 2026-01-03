---
nid: 2392
title: "Moving Comments into a Block - Drupal 7"
slug: "moving-comments-block-drupal-7"
date: 2012-01-04T20:04:55+00:00
drupal:
  nid: 2392
  path: /blogs/jeff-geerling/moving-comments-block-drupal-7
  body_format: full_html
  redirects: []
tags:
  - blocks
  - comments
  - drupal
  - drupal 7
  - drupal planet
  - php
  - snippets
aliases:
  - /blogs/jeff-geerling/moving-comments-block-drupal-7
---

[<strong>Note</strong>: It looks like there's a new module, as of January 2013, <a href="http://drupal.org/project/node_comment_block">Node Comment Block</a>, which uses the technique outlined below to move comments into a block.]

Most of the time, Drupal's convention of printing comments and the comment form inside the node template (node.tpl.php) is desirable, and doesn't cause any headaches.

However, I've had a few cases where I wanted to either put comments and the comment form in another place on the page, and in the most recent case, I <a href="http://drupal.stackexchange.com/questions/18880/">asked around</a> to see what people recommended for moving comments out of the normal rendering method. I found a few mentions of using Panels, and also noticed the <a href="http://drupal.org/project/commentsblock">Commentsblock</a> module that does something like this using Views.

However, I just wanted to grab the normal comment information, and stick it directly into a block, and put that block somewhere else. I didn't want Views' overhead, or to have to re-theme and tweak things in Views, since I already have a firm grasp of comment rendering and form theming with the core comment display.

So, I set out to do something similar to <a href="http://drupal.org/node/122240#comment-707961">this comment on drupal.org</a> (which was also suggested by Jimajamma on Drupal Answers).

First, I had to hide the comments from the normal rendering pipeline in node.tpl.php, which involved using template_preprocess_node() to set 'comment' to 0, and a check in node.tpl.php to make sure <code>$content['comments']</code> would only be rendered if $comment evaluated to TRUE:

```
<?php
function THEMENAME_preprocess_node(&$variables) {
  // For note nodes, disable comments in the node template.
  if ($variables['type'] == 'note') {
    $variables['comment'] = 0;
  }
}
?>
```

Then, I simply built a block in my custom module, and used the magic of comment_node_page_additions() to render the comments and comment form, just as they would render under the node, except in my own, spiffy comment block:

```
<?php
/**
 * Implements hook_node_view().
 */
function MODULENAME_node_view($node, $view_mode) {
  global $node_comments;

  // Store node comments in global variable so we can put them in a block.
  if ($node->type == 'note' && isset($node->content['comments'])) {
    $node_comments = $node->content['comments'];
  }
}

/**
 * Implements hook_block_info().
 */
function MODULENAME_block_info() {
  $blocks['note_comments'] = array(
    'info' => t('Note Comments'),
    'cache' => DRUPAL_NO_CACHE,
  );
  return $blocks;
}

/**
 * Implements hook_block_view().
 */
function MODULENAME_block_view($delta = '') {
  global $user;
  global $node_comments;
  $block = array();
  if ($delta == 'note_comments') {
    // Get the active menu object.
    if ($node = menu_get_object()) {
      // Make sure user is viewing a note.
      if ($node->type == 'note') {
        $block['content'] = '';
        // Set the title of the block.
        $block['subject'] = NULL;
        // Render the comments and comment form (access checks, etc. are done
        // by comment_node_page_additions()).
        $block['content'] .= drupal_render($node_comments);
      }
    }
  }
  return $block;
}
?>
```

Then, after a quick trip to the <code>Configure > Blocks</code> page, where I assigned my block to a region, I had a slick comments block that I could render anywhere!
