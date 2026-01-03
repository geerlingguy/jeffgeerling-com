---
nid: 2447
title: "Multisite Apache Solr Search with Domain Access"
slug: "multisite-apache-solr-search"
date: 2014-02-18T21:01:49+00:00
drupal:
  nid: 2447
  path: /blogs/jeff-geerling/multisite-apache-solr-search
  body_format: full_html
  redirects: []
tags:
  - domain
  - drupal
  - drupal 7
  - drupal planet
  - multisite
  - snippets
  - solr
aliases:
  - /blogs/jeff-geerling/multisite-apache-solr-search
---

<p>Using one Apache Solr search core with more than one Drupal website isn't too difficult; you simply use a module like <a href="https://drupal.org/project/apachesolr_multisitesearch">Apache Solr Multisite Search</a>, or a technique like the one mentioned in Nick Veenhof's post, <a href="http://nickveenhof.be/blog/lets-talk-apache-solr-multisite">Let's talk Apache Solr Multisite</a>. This kind of technique can save you time (and even money!) so you can use one <a href="http://hostedapachesolr.com/">Hosted Apache Solr</a> subscription with multiple sites. The only caveat: any site using the solr core could see any other site's content (which shouldn't be a problem if you control all the sites and don't expose private data through solr).</p>

<p>There are two ways to make Apache Solr Search Integration work with <a href="https://drupal.org/project/domain">Domain Access</a> (one of which works similarly to the methods mentioned above for multisite), and which method you use depends on how your site's content is structured.</p>

<h2>Solr Search with Domain Access - Siloed Content</h2>

<p>If the content you are indexing and searching is unique per domain (just like it would be unique per multisite Drupal instance), then you can set up Domain Access to index content with a different Apache Solr hash per site, like so:</p>

<p>First, in a custom module, use <code>hook_domain_batch()</code> to tell Domain Access to add variable configuration for the <code>apachesolr_site_hash</code> variable per-domain (this requires the Domain Configuration module to be enabled, as well as, obviously, the Apache Solr module):</p>

```
```
<?php
/**
 * Implements hook_domain_batch().
 *
 * Add batch settings to Domain Configuration for Apache Solr Search.
 */
function MODULENAME_configuration_domain_batch() {
  $batch = array();
  if (function_exists('apachesolr_site_hash')) {
    $batch['apachesolr_site_hash'] = array(
      '#form' => array(
        '#title' => t('Apache Solr site hash'),
        '#type' => 'textfield',
        '#description' => t('Unique site hash for Apache Solr.'),
      ),
      '#domain_action' => 'domain_conf',
      '#permission' => 'administer site configuration',
      '#system_default' => apachesolr_site_hash(),
      '#meta_description' => t('Set Apache Solr site hash for each domain.'),
      '#variable' => 'apachesolr_site_hash',
      '#data_type' => 'string',
      '#weight' => -1,
      '#group' => t('Apache Solr'),
      '#update_all' => TRUE,
      '#module' => t('Apache Solr'),
    );
  }
  return $batch;
}
?>
```

</pre></code>

<p>Second, visit <code>/admin/structure/domain/batch/apachesolr_site_hash</code> and enter a different hash for each domain.</p>

<p>Third, use <code>hook_apachesolr_query_alter()</code> to alter solr queries to search using the site-specific hash:</p>

```
```
<?php
/**
 * Implements hook_apachesolr_query_alter().
 */
function MODULENAME_apachesolr_query_alter($query) {
  // Get the current domain.
  $domain = domain_get_domain();
  $hash = domain_conf_variable_get($domain['domain_id'], 'apachesolr_site_hash');
  // Add the current domain's apachesolr site hash to the query.
  $query->addFilter('hash', $hash);
}
?>
```

</pre></code>

<p>At this point, if you reindex all your content on all your domains, each domain will only find content specific to the domain. (This method was discussed in <a href="https://drupal.org/node/2004434">this issue</a> in Domain Access's issue queue.).</p>

<h2>Problem: Single node, multiple domains</h2>

<p>There's a major issue that I've seen a few times with this situation: what if there is a node (or many nodes) that are published to multiple domains (shared across more than one domain)? In this case, the content will show up only when searching on the domain where Solr indexing was run first. So, if a piece of content is published to domain A and domain B, but solr indexes the node on domain A, the content won't show in results for domain B, because <em>the apachesolr site hash for that content was set to domain A's hash</em>.</p>

<p>So, to avoid this issue, we can't actually use Apache Solr's site hash when indexing nodes (or at least, we can't <em>only</em> use it). Instead, we need to add an array of assigned domains for each document in Apache Solr's index, and use that array to filter search results when searching on each individual domain.</p>

<h2>Solution: Adding domain access info to the index for shared content</h2>

<p>The fix involves three parts:</p>

<p>First, when indexing a document in solr, we need to add domain information to the index so we can filter our query with it later. We'll do this with <code>hook_apachesolr_index_document_build()</code>:</p>

```
```
<?php
/**
 * Implements hook_apachesolr_index_document_build().
 */
function MODULENAME_apachesolr_index_document_build(ApacheSolrDocument $document, $entity, $entity_type, $env_id) {
  if (isset($entity->domains)) {
    foreach($entity->domains as $domain) {
      // The gid in the {domain} table is unsigned, but the domain module makes
      // it -1 for the deault domain. Also apache doesn't like it if we query
      // for domain id -1.
      if ($domain == -1) {
        $domain = 0;
      }

      // Build an apachesolr-compatible domain search index key.
      $key = array(
        'name' => 'domain_id',
        'multiple' => TRUE,
        'index_type' => 'integer',
      );
      $key = apachesolr_index_key($key);

      // Add domain key to document.
      $document->setMultiValue($key, $domain);
    }
  }
}
?>
```

</pre></code>

<p>Second, we need to filter the search query sent to Apache Solr using <code>hook_apachesolr_query_alter()</code> so it filters based on the domain where the search is being performed:</p>

```
```
<?php
/**
 * Implements hook_apachesolr_query_alter().
 */
function MODULENAME_apachesolr_query_alter($query) {
  // Add domain key to filter all queries.
  $domain = domain_get_domain();
  $query->addParam('fq', 'im_domain_id:' . $domain['domain_id']);
}
?>
```

</pre></code>

<p>Third, we need to change the 'url' passed into the search result, so it's a relative URL that will work on all your domains (by default, Apache Solr seems to use an absolute URL to the domain on which the node was indexed, meaning some links will link users off one domain to another domain!). You can do this using <code>template_preprocess_search_result()</code> in your theme (or in a custom module substituting <code>MODULENAME</code> for <code>THEMENAME</code> below):</p>

```
```
<?php
/**
 * Overrides template_preprocess_search_result().
 */
function THEMENAME_preprocess_search_result(&amp;$vars) {
  // Create a relative link to the node, so it points to the correct domain.
  $nid = $vars['result']['node']->entity_id;
  $vars['url'] = check_plain(url('node/' . $nid));
}
?>
```

</pre></code>

<p>Once all this is done, you need to reindex all your content (across all domains) before everything will start working correctly. Once that's done, you'll have multi-domain apache solr working with shared content. Nice!</p>

<p>The inspiration behind this method of making solr work well filtering content across multiple domains comes from the <a href="https://drupal.org/project/domain_solr">Domain Access Solr Facet</a> module, which doesn't yet have a Drupal 7 release, but is relatively simple, and has a <a href="https://drupal.org/node/1213296#comment-8492829">patch for the D7 port</a> in the issue queue.</p>
