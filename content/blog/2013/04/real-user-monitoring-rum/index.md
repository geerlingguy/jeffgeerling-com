---
nid: 2400
title: "Real User Monitoring (RUM) with Pingdom and Drupal"
slug: "real-user-monitoring-rum"
date: 2013-04-11T14:33:48+00:00
drupal:
  nid: 2400
  path: /blogs/jeff-geerling/real-user-monitoring-rum
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - monitoring
  - performance
  - pingdom
  - real user monitoring
  - rum
aliases:
  - /blogs/jeff-geerling/real-user-monitoring-rum
---

<strong>Edit:</strong> There's a module for that™ now: <a href="http://drupal.org/project/pingdom_rum">Pingdom RUM</a>. The information below is for historical context only. Use the module instead, since it makes this a heck of a lot simpler.

<hr />

<a href="http://royal.pingdom.com/2013/04/11/pingdom-announces-real-user-monitoring-press-release/">Pingdom</a> just announced that their Real User Monitoring service is now available for all Pingdom accounts—including monitoring on one site for free accounts!

This is a great opportunity for you to start making page-specific measurements of page load performance on your Drupal site.

To get started, log into your Pingdom account (or create one, if you don't have one already), then click on the "RUM" tab. Add a site for Real User Monitoring, and then Pingdom will give you a `<script>` tag, which you then need to insert into the markup on your Drupal site's pages.

The easiest way to do this is to use <code>drupal_add_html_head()</code> within the <a href="http://api.drupal.org/api/drupal/modules!system!system.api.php/function/hook_page_alter/7">page_alter hook</a> (in your theme's template.php, or in a custom module):

```
<?php
/**
 * Implements hook_page_alter().
 */
function THEMENAME_page_alter($page) {
  // Add Pingdom RUM code.
  $pingdom_rum = array(
    '#type' => 'html_tag',
    '#tag' => 'script',
    '#attributes' => array(
      'type' => 'application/javascript',
    ),
    '#value' => '[SCRIPT TAG CONTENT HERE]',
  );
  drupal_add_html_head($pingdom_rum, 'pingdom_rum');
}
?>
```

Replace THEMENAME with your module or theme name, and [SCRIPT TAG CONTENT HERE] with the content of the pingdom script tag (excluding the two `<script>` tags at the beginning and end).

Once you've done this, go back to Pingdom, and you can view page load times in real-time:

<p style="text-align: center;">{{< figure src="./pingdom-rum-monitoring-graph.png" alt="Pingdom RUM monitoring graph" width="425" height="166" >}}</p>

Pretty nifty!

<strong>Note</strong>: If you're looking for a great website monitoring service that's a bit simpler and cheaper than something like Pingdom (which we love!), check out <a href="https://servercheck.in/">Server Check.in</a> :)
