---
nid: 2323
title: "Programmatically Adding or Removing a User or Node Reference from a Node (D7 / References)"
slug: "programmatically-adding-or"
date: 2011-06-16T17:51:45+00:00
drupal:
  nid: 2323
  path: /blogs/jeff-geerling/programmatically-adding-or
  body_format: full_html
  redirects: []
tags:
  - code
  - drupal
  - drupal 7
  - drupal planet
  - php
  - references
aliases:
  - /blogs/jeff-geerling/programmatically-adding-or
---

The References module in Drupal 7 allows for easy creation and removal of user and node references through Drupal's interface. However, programmatically adding and removing these references is a little more difficult.

You basically have to load the node which has the reference in it, edit the reference field (in my example, the reference field can have an unlimited number of references), add or remove the user ID (or node ID if you're chaging a node reference), and save the node.

Let's look at the example of simply adding a user reference to a node:

```
<?php
  // Load the node you'd like to edit.
  $node = node_load($nid);
  // Add the user ID you'd like to add to this node reference.
  $node->field_node_user_references[$node->language][] = array('uid' => $uid);
  // Save the node.
  node_save($node);
?>
```

It takes a little more effort to remove a user reference (or node reference) from a node. For this, since I have to do it for a few different fields on a node, I've written a helper function that removes a given $uid from the array of user references on a given node.

Code first, explanation after:

```
<?php
/**
 * Helper function to remove an user reference by value.
 */
function _MYMODULE_remove_user_reference_by_uid($reference_field_lang_array, $uid = '', $preserve_keys = FALSE) {
  // Since we have a multi-value user reference field, we need to check each value.
  foreach($reference_field_lang_array as $key => $value) {
    if ($value['uid'] == $uid) {
      // If the user ID is found in the array, unset that value.
      unset($reference_field_lang_array[$key]);
    }
  }
  // Run this through array_values() so the array index (0, 1, 2, etc.) is reset.
  return array_values($reference_field_lang_array);
}
?>
```

To call this function and actually remove a given user from the user reference field, we'll do something like the following:

```
<?php
  // Load the node you'd like to edit.
  $node = node_load($nid);
  // Use our helper function to remove the given user id from the references field.
  $list->field_node_user_references[$list->language] = _fn_networks_remove_user_reference_by_uid($node->field_node_user_references[$list->language], $uid);
  // Save the node.
  node_save($node);
?>
```

It's slightly convoluted, sure, but it really helps if you, like me, need to build an alternate interface for allowing, say, list administrators to quickly add or remove a user reference from a list. In my case, I use this feature to let list administrators for a site toggle list subscribers from being able to add posts to a given list.

Adding and removing node references would be about the same, but you would use whatever field name you have for your node reference.

P.S. The <a href="http://drupal.org/project/relation">Relation</a> module for Drupal 7 looks like it might someday replace references, but for now, it's not nearly as supported/simple to use... at least in my book!
