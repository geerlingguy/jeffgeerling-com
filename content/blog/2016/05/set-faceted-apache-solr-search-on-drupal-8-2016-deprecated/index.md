---
nid: 2645
title: "Set up faceted Apache Solr search on Drupal 8 (2016 - deprecated)"
slug: "set-faceted-apache-solr-search-on-drupal-8-2016-deprecated"
date: 2016-05-03T15:32:26+00:00
drupal:
  nid: 2645
  path: /blog/2016/set-faceted-apache-solr-search-on-drupal-8-2016-deprecated
  body_format: markdown
  redirects:
    - /blog/2016/set-faceted-apache-solr-search-page-on-drupal-8-search-api-solr-and-facets
aliases:
  - /blog/2016/set-faceted-apache-solr-search-page-on-drupal-8-search-api-solr-and-facets
tags:
  - drupal
  - drupal 8
  - drupal planet
  - facets
  - search
  - search api
  - solr
  - tutorial
---

> **Note**: A _lot_ has changed in Drupal 8 and the Search API module ecosystem since this post was written in May 2016... I wrote a new blog post for [Faceted Solr Search in Drupal 8](//www.jeffgeerling.com/blog/2016/setting-faceted-apache-solr-search-drupal-8), so please read that if you're just getting started. I'm leaving this up as a historical reference, as the general process and architecture are the same, but many details are different.

In Drupal 8, [Search API Solr](https://www.drupal.org/project/search_api_solr) is the consolidated successor to both the Apache Solr Search and Search API Solr modules in Drupal 7. I thought I'd document the process of setting up the module on a Drupal 8 site, connecting to an Apache Solr search server, and configuring a search index and search results page with search facets, since the process has changed slightly from Drupal 7.

## Install the Drupal modules

In Drupal 8, since Composer is now a de-facto standard for including external PHP libraries, the Search API Solr module doesn't actually include the Solarium code in the module's repository. So you can't just download the module off Drupal.org, drag it into your codebase, and enable it. You have to first ensure all the module's dependencies are installed via Composer. There are two ways that I recommend for doing this (both are documented in the module's issue: [Keep Solarium managed via composer and improve documentation](https://www.drupal.org/node/2661698)):

  1. Run the following commands in the root directory of your site's codebase:
    1. `composer config repositories.drupal composer https://packagist.drupal-composer.org`
    2. `composer require "drupal/search_api_solr 8.1.x-dev"` (or `8.1.0-alpha3` for the latest stable alpha release)
  2. Install [Composer Manager](https://www.drupal.org/project/composer_manager) and [follow Composer Manager's installation instructions](https://www.drupal.org/node/2405811) to let it download module dependencies (after having downloaded search_api_solr into your codebase via Drush or manually).

Basically, you need to make sure [Search API](https://www.drupal.org/project/search_api), [Search API Solr](https://www.drupal.org/project/search_api_solr), and [Facets](https://www.drupal.org/project/facets) (formerly _Facet API_) are in your codebase before you can install them on the Extend page:

<p style="text-align: center;">{{< figure src="./install-solr-search-api-facets-modules-drupal-8.png" alt="Install Facets, Search API, and Solr Search modules in Drupal 8" width="435" height="278" class="insert-image" >}}</p>

Install those three modules on your site (either on the 'Extend' page, or via Drush with `drush en [module_name]`), and if you don't need the redundant core search functionality (you probably don't!), uninstall the Search module.

## Connect to your Solr server

Visit the Search API configuration page (`/admin/config/search/search-api`, or Configuration > Search and metadata > Search API in the menu), and click 'Add Server'. Add a server with the following configuration (assuming you're running this on a local instance of [Drupal VM](http://www.drupalvm.com/), which easily installs and configures Solr for you):

  - **Server name**: `Local Solr Server` (don't use `localhost` until <a href="https://www.drupal.org/node/2643788">this issue</a> is resolved!)
  - **Backend**: `Solr` (should be the only option at this point)
  - **HTTP protocol**: `http`
  - **Solr host**: `localhost`
  - **Solr port**: `8983`
  - **Solr path**: `/solr`
  - **Solr core**: `collection1` (this Solr search index/core is set up for you if you use Drupal VM and [uncomment the example post-provision script for Solr](https://github.com/geerlingguy/drupal-vm/blob/master/example.config.yml#L231))
  - **Basic HTTP authentication**: (make sure this is blank)
  - **Advanced**: These options are up to you. Leave the version override and HTTP method set to their automatic defaults.

Click 'Save', and the server should be saved. Hopefully under **Server Connection** on the page that you're taken to, you see the message _The Solr server could be reached._ This means the server is set up correctly, and you can move on to creating a search index on the server.

## Create a search index

Back on the Search API configuration page, click 'Add Index'. For the example, we'll create an index with only Article content, with the following configuration:

  - **Index name**: `Articles`
  - **Data sources**: `Content`
    - **What should be indexed?**: `None except those selected`
    - **Bundles**: `Article`
    - **Languages**: `English`
  - **Server**: `Local Solr Server`

Make sure the index is enabled (there's a checkbox for it), and click 'Save'. By default, Search API will index all article content that currently exists immediately (or none, if none exists at this point).

If you don't have any article content yet, create a few articles with a title, body, and some tags. Now that you have content, make sure it's indexed by running cron (either use `drush cron` or run it via the Reports > Status report page). Check the index page at `/admin/config/search/search-api/index/articles` to make sure articles are in the index:

<p style="text-align: center;">{{< figure src="./search-api-article-index-status.png" alt="Search API Article index status Drupal 8" width="600" height="274" class="insert-image" >}}</p>

### Add fields to the index

Before you can search for content in the index, you need to make sure all the fields you're interested in searching are available in Solr. You need to go to the 'Fields' tab for the index, and click the 'Add fields' button to add fields from the content type to this index:

<p style="text-align: center;">{{< figure src="./add-fields-search-index-article-search-api.png" alt="Search API Article index add fields to index Drupal 8" width="500" height="360" class="insert-image" >}}</p>

Under the 'Content' section, I chose to add the following fields:

  - ID
  - UUID
  - Content Type
  - Title
  - Authored by > User > Name
  - Authored on
  - URL alias > Path alias
  - Body
  - Tags

> Note: As of May 2016, the UI for adding fields feels slightly jarring. There's an open issue to improve the field management UI in Search API: [AJAXify and generally improve the new Fields UI](https://www.drupal.org/node/2641388).

Click 'Done' once finished adding fields, then make sure all the fields you added are present under 'Content' back on the field overview page. (Later, when you're going further into index customization and optimization, you'll spend a bit more time on this page and in this process of refining the fields, their boost, their types, etc.)

### Add processors to the index

The last step in setting up the search index is the addition of 'processors', which allow the index to be more flexible and work exactly how we want it for a fulltext 'fuzzy' search as well as for faceted search results. Go to the 'Processors' tab for the Articles index, and check the following checkboxes:

  - Aggregated fields
  - Highlight
  - Ignore case
  - Node status
  - Tokenizer
  - Transliteration

Then, to give ourselves the ability to search with one search box on multiple fields (e.g. title, body, and tags), at the bottom of the page click 'Add new Field' in the 'Aggregated fields' configuration (note this might currently drop you into a different vertical tab once clicked—switch back to the Aggregated fields tab if so), and then call the new field 'Fulltext Article search'. Check Body, Tags, URL alias, Title, and Authored by.

Click 'Save' at the bottom of the form to save all changes. The search index will need to be updated so all the processors can have an effect, but before doing that, go back to the 'Fields' configuration for the Article search index, and switch the new aggregated field from type 'String' to 'Fulltext':

<p style="text-align: center;">{{< figure src="./aggregated-search-field-string-to-fulltext.png" alt="Use type Fulltext for aggregated field in Search API Article index" width="600" height="176" class="insert-image" >}}</p>

Click 'Save changes', then go back to the search index View page and click the 'Index now' button (or use cron to reindex everything).

## Configure a search page and search facets

Now we come to the final and most important part of this process: creating a search page where users can search through your articles using a full-text, faceted search powered by Solr. Create a new View (visit `/admin/structure/views` and click 'Add new view'), and name the view 'Article search'. For the view's general settings:

  - **Show**: `Index Articles`
  - **Page**: Create a page (checked)
    - **Page title**: `Article search`
    - **Path**: `search/articles`
    - **Display format**: `Unformatted list` of `Rendered entity`

Click 'Save and edit' to configure the view. Now we will configure the search index view to our liking:

  1. Click the 'Settings' for the Rendered entity (Format > Show), and switch from the Default view mode to Teaser.
  2. Click the 'Add' button under Filter criteria, and add the "Fulltext Article search" aggregate field we added earlier.
  3. Check the 'Expose this filter to visitors' button, and change the label to 'Search', then Apply the changes.
  4. Save the view, then visit `/search/articles`.

Test out your new search page, and make sure you can search any part of any of the aggregated text fields.

> Note: If you want to be able to search _parts_ of words (e.g. word stems like 'other' match instances of 'another'), then you have to do that in your Solr schema, using Solr's `EdgeNGramFilterFactory`; see this documentation from Hosted Apache Solr: [Enable partial word match keyword searching with EdgeNGramFilterFactory
](https://hostedapachesolr.com/node/621).

### Add search facets

Now that we have the general search page set up, let's add a few facets to allow users to more easily drill down into their search results. Go to the Facets admin page (`/admin/config/search/facets` or Configuration > Search and metadata > Facets), and click 'Add facet' to add two different facets:

  1. A 'Publish date' facet:
    1. **Facet name**: `Publish date`
    2. **Facet name for URLs**: `published`
    3. **Facet source**: `Article search > Page`
    4. **Facet field**: `Authored on`
    5. **Weight**: `0`
  2. A 'Tags' facet:
    1. **Facet name**: `Tags`
    2. **Facet name for URLs**: `tags`
    3. **Facet source**: `Article search > Page`
    4. **Facet field**: `Tags`
    5. **Weight**: `0`

For the facet display settings, leave the defaults for now (you can customize the facet display and advanced behavior later), and click 'Save' to save the facet. For the 'Tags' facet, edit the display and check the 'Translate taxonomy terms' checkbox so the term name (and not the term ID) is displayed.

Go to the Block layout page (`/admin/structure/block`) to place the two new facet blocks you just created into the Left sidebar (or wherever in the theme you'd like them to be visible), and save the updated block layout.

## Profit!

Now, if you visit the `/search/articles` page, you should see a faceted fulltext Apache Solr-powered search page, and from here you can customize anything as much or as little as you need!

<p style="text-align: center;">{{< figure src="./fulltext-search-facets-drupal-8-search-api-solr.png" alt="Search API Solr Drupal 8 faceted fulltext Apache Solr search page" width="650" height="477" class="insert-image" >}}</p>

Note that there are a few bits and pieces of the UI and functionality that are still being worked out between Search API, Search API Solr, Facets, and other addon modules that extend these base modules' functionality. Some features that many rely upon in Drupal 7's Solr/search ecosystem, like 'pretty paths' for Facets (e.g. `/search/articles/tag1/tag2` instead of `/search/articles?taxonomy=tid1&taxonomy_2=tid2`) are not yet available in Drupal 8, though there are some early ports (e.g. [a Facet pretty paths port](https://www.drupal.org/node/2677728)) for many of these modules in the search ecosystem.

I was pleasantly surprised how robust and complete the core search functionality already is in Drupal 8; with Drupal 8.1.0 just released, and more and more companies beginning to move to Drupal 8 as their core platform, I think we'll see more of these addon modules make their way to a stable release.
