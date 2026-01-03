---
nid: 2364
title: "Views: Show \"Showing X-X of X results\" (page and result counter) in Drupal 7"
slug: "views-show-showing-x-x-x"
date: 2011-06-13T20:39:37+00:00
drupal:
  nid: 2364
  path: /blogs/jeff-geerling/views-show-showing-x-x-x
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - pager
  - views
aliases:
  - /blogs/jeff-geerling/views-show-showing-x-x-x
---

[<strong>Update</strong>: Views 3.x has a really nifty plugin feature called 'Results summary' that you can simply add to the header or footer of your view, and use your own text with placeholders, to do everything I outline in the post below, without a line of code. Add a results summary instead of using hook_views_pre_render() or a Views PHP field.]

I needed to display a page/item counter on a view on one of my Drupal 7 sites, using Views 7.x-3.x. This counter would display at the bottom of the view, just above the pager, and needed to display the current number of results being displayed, along with the total number of results.

Views provides all this data right inside the $views object, so all I needed to do was add the following PHP snippet (including the <code><code>
<?php ?>
</code></code> delimiters) to a 'Global: PHP' textarea in my view's footer:

```
<?php
$from = ($view->query->pager->current_page * $view->query->pager->options['items_per_page']) + 1;
$to = $from + count($view->result) - 1;
$total = $view->total_rows;
print '<div class="views-result-count">';
if ($total <= $to) {
  // If there's no pager, just print the total.
  print $total . ' results.';
} else {
  // Otherwise, show "Showing X - X of XX results."
  print 'Showing ' . $from . ' - ' . $to . ' of '. $total . ' results.';
}
print '</div>';
?>
```

This prints the total number of results when there is just one page of results, and prints the range which the user is currently viewing, with the total number of results, when the user is browsing through pages using the view's pager.

You can use this code to print the pager/result counts wherever you can access the $view object (in a .tpl.php file, in the header or footer, or in a views render hook.

<strong>Edit</strong>: To make this live better in version control, and to avoid having to enable the PHP filter on your site, you can add the following code inside a custom module (which hooks into views and adds the count to the bottom of the view (switch 'attachment_after' to 'attachment_before' to show the count at the top of the view):

```
<?php
/**
  * Implements hook_views_pre_render().
  */
function MYMODULE_views_pre_render(&$view) {
  dpm($view);
  if ($view->name == 'MY_VIEW_NAME_HERE') {
    $output = '';
    $from = ($view->query->pager->current_page * $view->query->pager->options['items_per_page']) + 1;
    $to = $from + count($view->result) - 1;
    $total = $view->total_rows;
    $output .= '<div class="views-result-count">';
    if ($total <= $to) {
      // If there's no pager, just print the total.
      $output .= $total . ' results.';
    } else {
      // Otherwise, show "Showing X - X of XX results."
      $output .= 'Showing ' . $from . ' - ' . $to . ' of '. $total . ' results.';
    }
    $output .= '</div>';
    $view->attachment_after = $output;
  }
}
?>
```

