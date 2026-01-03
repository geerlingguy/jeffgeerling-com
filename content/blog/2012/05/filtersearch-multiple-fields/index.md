---
nid: 2374
title: "Filter/Search on multiple fields with Views 3.x"
slug: "filtersearch-multiple-fields"
date: 2012-05-15T15:13:34+00:00
drupal:
  nid: 2374
  path: /blogs/jeff-geerling/filtersearch-multiple-fields
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - filters
  - search
  - snippets
  - views
---

[<strong>Update</strong>: As of <a href="http://drupal.org/node/1742778">Views 7.x-3.4</a>, you can now use the new "Global: Combine fields filter" to combine fields for an exposed search. Just add the fields you want to search to the view's Fields section, then add a 'Global: Combine fields filter' and select all the fields you want to search. Simple as that!]

<hr />

A common need I run into with a ton of Drupal sites and Views is searching/filtering content based on multiple fields. For example, a lot of people would like to search for content using either the Title or the Body for a particular content type.

There are two primary solutions offered for this situation, but they both have downsides or are overly complex, in my opinion:

<ul>
	<li>Use the <a href="http://drupal.org/project/computed_field">Computed Field</a> module to create yet another field stored in the database, combining the two (or more) fields you want to search, then expose a filter for that field instead of both of the individual fields. (I don't like this because it duplicates content/storage, and involves an extra module to do so).</li>
	<li>Use the <a href="http://drupal.org/project/views_filters_populate">Views Filters Populate</a> to invisibly populate a second field that you've added to a views OR group (using Views OR in Views 2.x, or the built-in AND/OR functionality in Views 3.x). (This module is slightly limited in that you can only work with strings, and again, it involves an extra module).</li>
</ul>

Instead of using an extra module, I simply do the following to achieve a multi-field search:

<ol>
	<li>Add an and/or group to the filters in Views 3.x (next to 'Filter criteria', click the 'Add' drop down and choose 'and/or, rearrange').</li>
	<li>Put the main field you'd like to search into the new filter group (in my case, the Title field), and set the new group to OR.</li>
	<li>Implement&nbsp;hook_views_query_alter() in a custom module. In the query alter, you'll simply get the keyword parameter, and add a join and where clause (if you want to join to another table, like the 'body' data table). The code I'm using in this particular instance is below:</li>
</ol>

```
<?php
/**
 * Implements hook_views_query_alter().
 *
 * Allow users to search the in the 'help' view by title OR body.
 */
function custom_views_query_alter(&$view, &$query) {
  // Only do anything when using the 'help' view.
  if ($view->name == 'help') {
    // Get the keyword used for the search.
    $keyword = isset($_GET['title']) ? $_GET['title'] : '';

    // Add a new LEFT JOIN and WHERE clause for the help node body.
    $join = new views_join();
    $join->construct('field_data_body', 'node', 'nid', 'entity_id');
    $query->table_queue['node__field_data_body'] = array(
      'table' => 'field_data_body',
      'num' => 1,
      'alias' => 'node__field_data_body',
      'join' => $join,
      'relationship' => 'node',
    );
    // The first parameter selects the 'AND/OR' group this WHERE will be added to.
    // In this case, we add it to the second group (the first one is an AND group for
    // 'status = published' and 'type = help').
    $query->add_where(2, 'node__field_data_body.body_value', '%' . $keyword . '%', 'LIKE');
  }
}
?>
```

The documentation for a views_join() and add_where() are somewhat vague, but basically, the code above only runs on the 'help' view, it gets the keyword from the URL parameters (works with or without AJAX-enabled views), then adds a join from the node table (where the 'Title' is) to the field_data_body table (where the content is), and adds a 'where' clause to the new 'OR' group we created in steps 1-2 above.

If you want to dig deeper into the query, just use the Devel module's dpm() function to show the $query object (<code>dpm($query);</code>).

(Note: This illustrates a pretty simple two-field search. I've used the same technique to search on more fields, just adding more where clauses, and making sure there are joins to all the tables where I'm searching... in one example, I searched a list of users by their username, real name (fields), phone number (a field), or email address).
