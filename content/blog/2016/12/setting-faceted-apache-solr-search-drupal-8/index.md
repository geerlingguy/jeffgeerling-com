---
nid: 2723
title: "Setting up Faceted Apache Solr search in Drupal 8"
slug: "setting-faceted-apache-solr-search-drupal-8"
date: 2016-12-30T04:34:07+00:00
drupal:
  nid: 2723
  path: /blog/2018/setting-faceted-apache-solr-search-drupal-8
  body_format: markdown
  redirects:
    - /solr-d8
    - /blog/2016/setting-faceted-apache-solr-search-drupal-8
    - /blog/2017/setting-faceted-apache-solr-search-drupal-8
aliases:
  - /solr-d8
  - /blog/2016/setting-faceted-apache-solr-search-drupal-8
  - /blog/2017/setting-faceted-apache-solr-search-drupal-8
tags:
  - drupal
  - drupal 8
  - drupal planet
  - facets
  - search
  - search api
  - solr
  - tutorial
  - video
  - youtube
---

> Note: Extra special thanks to [Doug Vann](http://www.dougvann.com) for providing motivation to finally post this blog post!

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/J8Rt6HSzrqY" frameborder='0' allowfullscreen></iframe></div>

Early in 2016, when the Search API and Solr-related modules for Drupal 8 were in early alpha status, I wrote the blog post [Set up a faceted Apache Solr search page on Drupal 8 with Search API Solr and Facets](//www.jeffgeerling.com/blog/2016/set-faceted-apache-solr-search-page-on-drupal-8-search-api-solr-and-facets).

That post was helpful during the painful months when Solr search in Drupal 8 was still in a very rough state, but a _lot_ has changed since then, and Solr-based search in Drupal 8 is in a much more stable (and easy-to-configure) place today, so I thought I'd finally write a _new_ post to show how simple it is to build faceted Solr search in Drupal 8, almost a year later.

## Build a local development environment with Apache Solr

These days I always build and maintain Drupal sites locally using Drupal VM; doing this allows me to set up a development environment exactly how I like it, and doing things like adding Apache Solr is trivial. So for this walkthrough, I'll start from square one, and show you how to start with absolutely nothing, and build faceted search on a new Drupal 8 site, using Drupal VM and a Composer file:

Download [Drupal VM](https://www.drupalvm.com) and follow the [Quick Start Guide](https://github.com/geerlingguy/drupal-vm#quick-start-guide), then add the following `config.yml` inside the Drupal VM folder to ensure Apache Solr is installed:

    ---
    # Make sure Apache Solr is installed inside the VM.
    installed_extras:
      - drush
      - mailhog
      - solr
    
    # Configure Solr for the Search API module.
    post_provision_scripts:
      - "../examples/scripts/configure-solr.sh"
    
    # Use custom drupal.composer.json to build and install site.
    drupal_build_composer: true
    drupal_build_composer_project: false
    drupal_core_path: "{{ drupal_composer_install_dir }}/docroot"
    drupal_composer_dependencies:
      - "drupal/devel:1.x-dev"
      - "drupal/search_api:^1.0"
      - "drupal/search_api_solr:^1.0"
      - "drupal/facets:^1.0"

We're going to use Drupal VM's [Composer integration](http://docs.drupalvm.com/en/latest/deployment/composer/#using-composerjson) to generate a Drupal site that has a Composer-based Drupal install in the synced folder path (by default, in a `drupal` subdirectory inside the Drupal VM folder).

The `drupal_composer_dependencies` variable tells Drupal VM to `composer require` the modules necessary to get [Search API Solr](https://www.drupal.org/project/search_api_solr) and [Facets](https://www.drupal.org/project/facets). The `post_provision_scripts` script is included with Drupal VM, and will configure the version of Apache Solr installed with Drupal VM appropriately for use with the Search API Solr module.

Copy the `example.drupal.composer.json` to `drupal.composer.json`, then run `vagrant up` to build the local development environment and download all the Drupal code required to get started with search.

> Note: If you are setting search up on an existing site or don't want to use Drupal VM, download and install the Search API, Search API Solr, and Facets modules manually, and make sure you have Apache Solr running and a search core configured with the latest Search API Solr module version's configuration.

## Install the modules

If you want to install the modules via Drupal's UI:

  1. Go to `http://drupalvm.dev/`, then log in as the administrator (default username and password is `admin`/`admin`).
  2. Go to the Extend page (`/admin/modules`), and enable "Search API", "Facets", "Solr search", and "Solr Search Defaults".

<p style="text-align: center">{{< figure src="./search-api-related-modules-d8.png" alt="Enable Search API Solr and Facet modules in Drupal 8 UI" width="650" height="332" class="insert-image" >}}</p>

If you want to install the modules via Drush:

  1. Run `drush @drupalvm.drupalvm.dev en -y facets search_api search_api_so
lr search_api_solr_defaults`

You should also _uninstall_ the core 'Search' module if it's installed—it is not required for Search API or Facets, and will continue to store extra junk in your site's database if it is installed.

## Configure the Solr server

Visit the Search API configuration page, and edit the default Solr Server, making the following changes:

  - Change 'Solr core' to `collection1` (default is `d8`).

> **Note**: The latest versions of Drupal VM no longer require this step, as the default Solr core's name is set to `d8` automatically (see [this PR](https://github.com/geerlingguy/drupal-vm/pull/1134)).

<p style="text-align: center">{{< figure src="./update-core-to-collection1.png" alt="Search API Solr search core configuration" width="455" height="293" class="insert-image" >}}</p>

At this point, on the server's status page (`/admin/config/search/search-api/server/default_solr_server`), you should see a message "The Solr server could be reached" and "The Solr core could be accessed":

<p style="text-align: center">{{< figure src="./solr-server-connection-details.png" alt="Apache Solr server connection details in Search API configuration" width="650" height="193" class="insert-image" >}}</p>

Once this is done, uninstall the Solr Search Defaults module (`drush @drupalvm.drupalvm.dev pmu -y search_api_solr_defaults`); this module is no longer required after initial install, as the configuration for your Solr server is now part of the site's active configuration store and won't be deleted.

## Configure the Solr index

The Solr Search Defaults module creates a default content index containing all published nodes on the website. In our case, that means all Basic pages and Articles would be included.

You don't need to change anything in the index configuration, but if you want to have a poke around and see how it's set up and what options you have in terms of the data source, fields, or processors, visit `/admin/config/search/search-api/index/default_solr_index/edit`.

## Add default content (if you don't have any)

Assuming you built this site using Drupal VM, it's likely the site is barren, with no content whatsoever to be indexed. To fix that, you can use the Devel module's handy companion, Devel generate:

  1. Enable Devel generate: `drush @drupalvm.drupalvm.dev en -y devel_generate`
  2. Generate dummy content: `drush @drupalvm.drupalvm.dev generate-content 100`
    - _Note: At the time of this writing, the Drush command didn't result in generated content. Use the UI at `/admin/config/development/generate/content` if the Drush command isn't generating content._

Now you have a bunch of nodes you can index and search!

## Confirm Search indexing is working

It's best to let your production Solr servers wait a couple minutes before freshly-indexed content are made available to search; this way searches are a little more performant as Solr can batch its update operations. But for local development it's nice to have the index be up-to-date as quickly as possible for testing purposes, so Drupal VM's configuration tells Solr to update it's search index immediately after Drupal sends any content.

So, if you generated content with Devel generate, then visit the Index status page for the default search index (`/admin/config/search/search-api/index/default_solr_index`), you should see all the content on the site indexed:

<p style="text-align: center">{{< figure src="./indexed-content-100-percent-search-api.png" alt="100 percent of content indexed in Search API" width="650" height="277" class="insert-image" >}}</p>

If you're working on an existing site, or if all the content _isn't_ yet indexed for some reason, you can manually index all content by clicking the 'Index now' button and waiting for the operation to complete.

> Note that indexing speed can vary depending on the complexity of your site. If you have a site with many complex node types and hundreds of thousands or millions of nodes, you'll need to use more efficient methods for indexing, or else you'll be waiting months for all your content to be searchable!

## Make a Faceted Solr Search View

The Solr Search Defaults module creates an example Views-based search page, which you can access at `/solr-search/content`. It should already be functional, since your content is indexed in Solr (try it out!):

<p style="text-align: center">{{< figure src="./search-functional-demo-page.png" alt="Function Search Content page with Search API Solr in Drupal 8" width="480" height="308" class="insert-image" >}}</p>

For many sites, this kind of general keyword-based site search is all that you'd ever need. But we'll spruce it up a bit and make it more functional by changing the path and adding a Content Type Facet.

First, modify the view by visiting `/admin/structure/views/view/solr_search_content`:

  1. Change the Title to 'Search' (instead of 'Search Content').
  2. Change the Path to '/search' (instead of '/solr-search/content').
  3. Click 'Save'.

Second, create a Content Type facet by visiting `/admin/config/search/facets`:

  1. Click 'Add facet'.
  2. Choose the 'View Solr search content, display Page' Facet source (this is the view you just edited).
  3. Select 'Content type (type)' for the Facet's Field.
  4. Name the facet 'Search Facet - Content type' (this will help with placing a block later).
  5. Click 'Save'.
  6. On the Facet edit page:
    1. Check the box to 'Show the amount of results'.
    2. Check the 'List item label' checkbox (this will make the facet show 'Basic page' instead of 'page'—the label instead of the machine name for each item).
    3. Click 'Save'.

The facet is now ready to be placed in your theme so it will appear when the Search view is rendered. Visit the Block layout configuration page (`/admin/structure/block`), and click 'Place block' in the region where you want the facet to appear. In my theme, I chose the 'Sidebar first' region.

Find 'Search Facet - Content type' (the Facet you just created) and click 'Place block'. Then set the block title to something like 'Filter by Type', and click 'Save block'. You don't need to set specific visibility constraints for the block because the Facet is set to not display at all if there aren't search results on the page that require it to be shown.

Click 'Save blocks' on the Block layout page, and then visit your sitewide search page at `/search`:

<p style="text-align: center">{{< figure src="./search-page-with-facet.png" alt="Solr Search page with a basic preconfigured Facet in Drupal 8" width="500" height="230" class="insert-image" >}}</p>

If you perform a search, then you'll notice the facet's result counts will adjust accordingly:

<p style="text-align: center">{{< figure src="./facet-count-for-keyword-search-api-d8.png" alt="Facets with result count for Drupal 8 Search API keyword search page" width="650" height="305" class="insert-image" >}}</p>

At this point, you should have a fully operational Faceted Solr search on your Drupal 8 site. From here, you can customize the search page further, work on outputting different results (maybe a content teaser instead of the full rendered content?), and add more facets (date, author, taxonomy term, etc.) to make the search work exactly as you'd like!

## Next steps

If your hosting provider doesn't provide an Apache Solr search core for your site to use, you might want to consider using [Hosted Apache Solr](https://hostedapachesolr.com) to host your site's Solr search core; it uses a similar setup to what's used in Drupal VM, and I can vouch for it, since I run the service :)

Note that the Search API modules are still in beta as of this blog post; minor details may result in differences from the screenshots and instructions above.
