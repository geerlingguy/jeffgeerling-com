---
nid: 2431
title: "Migrating style and script tags from node bodies into Code per Node"
slug: "migrating-style-and-script"
date: 2013-10-01T17:35:52+00:00
drupal:
  nid: 2431
  path: /blogs/jeff-geerling/migrating-style-and-script
  body_format: full_html
  redirects: []
tags:
  - code per node
  - css
  - drupal
  - drupal planet
  - javascript
  - migrate
  - stylesheets
aliases:
  - /blogs/jeff-geerling/migrating-style-and-script
---

For a recent project, I needed to migrate anything inside `<script>` and `<style>` tags that were embedded with other content inside the body field of Drupal 6 nodes into separate Code per Node-provided fields for Javascript and CSS. (<a href="https://drupal.org/project/cpn">Code per Node</a> is a handy module that lets content authors easily manage CSS/JS per node/block, and saves the styles and scripts to the filesystem for inclusion when the node is rendered—<a href="http://www.lullabot.com/blog/article/module-monday-code-node">read more about CPN goodness here</a>).

The key is to get all the styles and scripts into a string (separately), then pass that data into an array in the format:

```
<?php
$node->cpn = array(
  'css' => '<string of CSS without <style> tags goes here>',
  'js' => '<string of Javascript without <script> tags goes here>',
);
?>
```

Then you can save your node with <code>node_save()</code>, and the CSS/JS will be stored via Code per Node.

For a migration using the <a href="https://drupal.org/project/migrate">Migrate</a> module, the easiest way to do this (in my opinion) is to implement the <code>prepare()</code> method, and put the JS/CSS into your node's cpn variable through a helper function, like so:

First, put implement the <code>prepare()</code> method in your migration class:

```
<?php
  /**
   * Make changes to the entity immediately before it is saved.
   */
  public function prepare($entity, $row) {
    // Process the body and move <script> and <style> tags to Code per Node.
    if (isset($entity->body[$entity->language][0])) {
      $processed_info = custom_process_body_for_cpn($entity->body[$entity->language][0]['value']);
      $entity->body[$entity->language][0]['value'] = $processed_info['body'];
      $entity->cpn = $processed_info['cpn'];
    }
  }
?>
```

Then, add a helper function like the following in your migrate module's .module file (assuming your migrate module is named 'custom'):

```
<code>
<?php
/**
 * Break out style and script tags in body content into a Code per Node array.
 *
 * This function uses regular expressions to grab the content inside <script>
 * and <style> tags inside the given body HTML, then put them into separate keys
 * in an array that can be set as $node->cpn for a node before saving, which
 * will store the scripts and styles in the appropriate fields for the Code per
 * Node module.
 *
 * Why regex? I originally tried using PHP's DOMDocument to process the HTML,
 * but besides being overly verbose with error messages on all but the most
 * pristine markup, DOMDocument processed tags poorly; if there were multiple
 * script tags, or cases where script tags were inside certain other tags, only
 * one or two of the matches would work. Yuck.
 *
 * Regex is evil, but in this case necessary.
 *
 * @param string $body
 *   HTML string that could potentially contain script and style tags.
 *
 * @return array
 *   Array with the following elements:
 *     cpn: array with 'js' and 'css' keys containing corresponding strings.
 *     body: same as the body passed in, but without any script or style tags.
 */
function custom_process_body_for_cpn($body) {
  $cpn = array('js' => '', 'css' => '');

  // Search for script and style tags.
  $tags = array(
    'script' => 'js',
    'style' => 'css',
  );
  foreach ($tags as $tag => $type) {
    // Use a regular expression to match the tag and grab the text inside.
    preg_match_all("/<$tag.*?>
</code>(.*?)<\/$tag>/is", $body, $matches, PREG_SET_ORDER);
    if (!empty($matches)) {
      foreach ($matches as $match_set) {
        // Remove the first item in the set (it still has the matched tags).
        unset($match_set[0]);
        // Loop through the matches.
        foreach ($match_set as $match) {
          $match = trim($match);
          // Some tags, like script tags for embedded videos, are empty, and
          // shouldn't be removed, so check to make sure there's a value.
          if (!empty($match)) {
            // Remove the text from the body.
            $body = preg_replace("/<$tag.*?>(.*?)<\/$tag>/is", '', $body);
            // Add the tag contents to the cpn array.
            $cpn[$type] .= $match . "\r\n\r\n";
          }
        }
      }
    }
  }

  // Return the updated body and CPN array.
  return array(
    'cpn' => $cpn,
    'body' => $body,
  );
}
?>
```

If you were using another solution like the <a href="https://drupal.org/project/css">CSS module</a> in Drupal 6, and need to migrate to Code per Node, your processing will be a little different, and you might need to do some work in your migration class' <code>prepareRow()</code> method instead. The main thing is to get the CSS/Javascript into the <code>$node->cpn</code> array, then save the node. The Code per Node module will do the rest.
