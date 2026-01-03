---
nid: 2550
title: "Set up a hierarchical taxonomy term Facet using Facet API with Search API Solr"
slug: "set-hierarchical-taxonomy-term-facet-using-facet-api-search-api-solr"
date: 2016-02-04T17:28:55+00:00
drupal:
  nid: 2550
  path: /blog/2016/set-hierarchical-taxonomy-term-facet-using-facet-api-search-api-solr
  body_format: markdown
  redirects:
    - /blog/2016/set-heirarchical-taxonomy-term-facet-using-facet-api-search-api-solr
aliases:
  - /blog/2016/set-heirarchical-taxonomy-term-facet-using-facet-api-search-api-solr
tags:
  - drupal
  - drupal 7
  - drupal planet
  - facets
  - search api
  - taxonomy
---

I wanted to document this here just because it took me a little while to get all the bits working just right so I could have a hierarchical taxonomy display inside a Facet API search facet, rather than a flat display of only the taxonomy terms directly related to the nodes in the current search.

Basically, I had a search facet on a search page that allowed users to filter search results by a taxonomy term, and I wanted it to show the taxonomy's hierarchy:

<p style="text-align: center;">{{< figure src="./flat-to-hierarchical-taxonomy-facet-drupal.png" alt="Flat taxonomy to hierarchical taxonomy display using Search API Solr and Facet API in Drupal 7" >}}</p>

To do this, you need to do two main things:

  1. Make sure your taxonomy field is being indexed with taxonomy hierarchy data intact.
  2. Set up the Facet API facet for this taxonomy term so it will display the full hierarchy.

Let's first start by making sure the taxonomy information is being indexed (refer to the image below):

<p style="text-align: center;">{{< figure src="./search-api-solr-index-filters-hierarchical-taxonomy.png" alt="Search API Solr index Filters configuration for hierarchical taxonomy" >}}</p>

  1. In Search API's configuration, edit the Filters for the search index you're using (e.g. `/admin/config/search/search_api/index/[index]/workflow`).
    1. Make sure the 'Index hierarchy' checkbox is checked.
    2. In the 'Index hierarchy' Callback settings (which appear after you check the box in step 1), scroll down and make sure you select 'Parent terms' and 'All parent terms' under the Taxonomy type you need to display hierarchically.
  2. Save the Filters configuration, then reindex all the content on your site (otherwise Solr won't have the updated hierarchy information).

Next, we need to edit the Facet API facet for this taxonomy:

  1. Go to the taxonomy Facet's configuration page (e.g. `/admin/config/search/facetapi/search_api%40[index]/block/field_release/edit`).
  2. Check the 'Expand hierarchy' checkbox under 'Display settings' (near the top of the form).
  3. Set 'Treat parent items as individual facet items' to 'No'.
  4. Set 'Flatten hierarchy' to 'No'.
  5. Set 'Minimum facet count' to 0 (to show all terms in the taxonomy).

After you've done that (make sure you reindexed your content!), you should have a nice hierarchical facet display.
