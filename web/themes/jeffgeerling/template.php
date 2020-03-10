<?php

/**
 * @file
 * Theme customizations for Jeff Geerling's website.
 */

/**
 * Implements hook_page_alter().
 */
function jeffgeerling_page_alter($page) {
  // Add meta tag for viewport, for easier responsive theme design.
  $viewport = array(
    '#type' => 'html_tag',
    '#tag' => 'meta',
    '#attributes' => array(
      'name' => 'viewport',
      'content' => 'width=device-width, initial-scale=1',
    ),
  );
  drupal_add_html_head($viewport, 'viewport');
}

/**
 * Implements template_preprocess_html().
 */
function jeffgeerling_preprocess_html(&$variables) {
  if (drupal_is_front_page()) {
    $variables['head_title'] = t('Jeff Geerling - Author and Software Developer in St. Louis, MO');
  }
}

/**
 * Implements template_preprocess_page().
 */
function jeffgeerling_preprocess_page(&$variables) {
  if (drupal_is_front_page()) {
    drupal_add_css(drupal_get_path('theme', 'jeffgeerling') . '/css/front.css');
  }

  if (isset($variables['node'])) {
    // Resumé page customizations.
    if ($variables['node']->nid == 1) {
      drupal_add_css(drupal_get_path('theme', 'jeffgeerling') . '/css/resume.css');
      drupal_add_css(drupal_get_path('theme', 'jeffgeerling') . '/css/resume-print.css', array('media' => 'print'));
      drupal_add_js(drupal_get_path('theme', 'jeffgeerling') . '/js/resume.js');
    }
    // Project page customizations.
    elseif ($variables['node']->type == 'project') {
      drupal_add_css(drupal_get_path('theme', 'jeffgeerling') . '/css/project.css');
    }
    elseif ($variables['node']->type == 'blog_post') {
      drupal_add_css(drupal_get_path('theme', 'jeffgeerling') . '/css/blog.css');
    }
  }

  // Add project CSS to project view.
  $arg0 = arg(0);
  if ($arg0 == 'projects') {
    drupal_add_css(drupal_get_path('theme', 'jeffgeerling') . '/css/project.css');
  }
  elseif ($arg0 == 'blog' || $arg0 == 'comment') {
    drupal_add_css(drupal_get_path('theme', 'jeffgeerling') . '/css/blog.css');
  }
  elseif ($arg0 == 'search') {
    drupal_add_css(drupal_get_path('theme', 'jeffgeerling') . '/css/search.css');
  }

  // Remove breadcrumbs on non-admin pages.
  if (arg(0) != 'admin') {
    drupal_set_breadcrumb(array());
  }
}

/**
 * Implements template_preprocess_node().
 */
function jeffgeerling_preprocess_node(&$variables) {
  // Update 'submitted by' text.
  $variables['submitted'] = t('@date', array('@date' => $variables['date']));

  // Make the 'node_bottom' region available.
  if ($blocks = block_get_blocks_by_region('node_bottom')) {
    $variables['region']['node_bottom'] = $blocks;
  }
  else {
    $variables['region']['node_bottom'] = array();
  }
}

/**
 * Implements template_preprocess_comment().
 */
function jeffgeerling_preprocess_comment(&$variables) {
  $comment = $variables['elements']['#comment'];

  // Build the date.
  $variables['created'] = format_interval(REQUEST_TIME - $comment->created, 1);

  // Build the permalink.
  $uri = entity_uri('comment', $comment);
  $uri['options'] += array('attributes' => array(
    'class' => 'permalink',
    'rel' => 'bookmark',
  ));
  $variables['time_ago_link'] = l(
    t('@time ago', array('@time' => $variables['created'])),
    $uri['path'],
    $uri['options']
  );

  // Build the 'submitted by' text.
  $variables['submitted'] = t('!author – !time_ago', array(
    '!author' => $variables['author'],
    '!time_ago' => $variables['time_ago_link'],
  ));
}

/**
 * Implements template_preprocess_search_result().
 */
function jeffgeerling_preprocess_search_result(&$variables) {
  $variables['info'] = format_date($variables['result']['date'], 'custom', 'F j, Y');
}

/**
 * Implements template_preprocess_search_api_page_result().
 */
function jeffgeerling_preprocess_search_api_page_result(&$variables) {
  $variables['info'] = format_date($variables['item']->created, 'custom', 'F j, Y');
}
