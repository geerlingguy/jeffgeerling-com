---
nid: 2642
title: "Migrate a custom JSON feed in Drupal 8 with Migrate Source JSON"
slug: "migrate-custom-json-feed-drupal-8-migrate-source-json"
date: 2016-04-28T02:21:04+00:00
drupal:
  nid: 2642
  path: /blog/2016/migrate-custom-json-feed-drupal-8-migrate-source-json
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
  - json
  - migrate
  - migrate tools
  - tutorial
---

> **June 2016 Update:** Times change fast! Already, the `migrate_source_json` module mentioned in the post has been (mostly) merged directly into the `migrate_plus` module, so if you're building a new migration now, you should use the `migrate_plus` JSON plugin if at all possible. See Mike Ryan's blog post [Drupal 8 plugins for XML and JSON migrations](http://virtuoso-performance.com/blog/mikeryan/drupal-8-plugins-for-xml-and-json-migrations) for more info.

Recently I needed to migrate a small set of content into a Drupal 8 site from a JSON feed, and since documentation for this particular scenario is slightly thin, I decided I'd post the entire process here.

I was given a JSON feed available over the public URL `http://www.example.com/api/products.json` which looked something like:

```
{
  "upcs" : [ "11111", "22222" ],
  "products" : [ {
    "upc" : "11111",
    "name" : "Widget",
    "description" : "Helpful for many things.",
    "price" : "14.99"
  }, {
    "upc" : "22222",
    "name" : "Sprocket",
    "description" : "Helpful for things needing sprockets.",
    "price" : "8.99"
  } ]
}
```

I first created a new 'Product' content type inside Drupal, with the Title field label changed to 'Name', and with additional fields for UPC, Description, and Price. Then I needed to migrate all the data in the JSON feed into Drupal, in the `product` content type.

> Note: at the time of this writing, Drupal 8.1.0 had just been released, and many of the migrate ecosystem of modules (still labeled [experimental](https://www.drupal.org/core/experimental) in Drupal core) require specific or dev versions to work correctly with Drupal 8.1.x's version of the Migrate module.

## Required modules

Drupal core includes the base 'Migrate' module, but you'll need to download and enable all the following modules to create JSON migrations:

  - Migrate (in core)
  - [Migrate Plus](https://www.drupal.org/project/migrate_plus) 8.x-2.x
  - [Migrate Tools](https://www.drupal.org/project/migrate_tools) 8.x-2.x
  - [Migrate Source JSON](https://www.drupal.org/project/migrate_source_json) 8.x-1.x (currently, requires [this patch](https://www.drupal.org/node/2694591) for Drupal 8.1.x+ compatibility)

After enabling those modules, you should be able to use the standard Drush commands provided by Migrate Tools to view information about migrations (`migrate-status`), run a migration (`migrate-import [migration]`), rollback a migration (`migrate-rollback [migration]`), etc.

The next step is creating your own custom migration by adding custom migration configuration via a module:

## Create a Custom Migration Module

In Drupal 8, instead of creating a special migration class for each migration, registering the migrations in an info hook, etc., you can just create a migration configuration YAML file inside `config/install` (or, technically, `config/optional` if you're including the migration config inside a module that does a bunch of other things and may or may not be used with the Migration module enabled), then when your module is installed, the migration configuration is read into the active configuration store.

The first step in creating a custom migration module in Drupal 8 is to create an folder (in this case, `migrate_custom_product`), and then create an info file with the module information, named `migrate_custom_product.info.yml`, with the following contents:

```
type: module
name: Migrate Custom Product
description: 'Custom product migration.'
package: Migration
core: 8.x
dependencies:
  - migrate_plus
  - migrate_source_json
```

Next, we need to create a migration configuration file, so inside `migrate_custom_product/config/install`, add a file titled `migrate_plus.migration.product.yml` (I'm going to call the migration `product` to keep things simple). Inside this file, define the entire JSON migration (don't worry, I'll go through each part of this configuration in detail later!):

```
# Migration configuration for products.
id: product
label: Product
migration_group: Products
migration_dependencies: {}

source:
  plugin: json_source
  path: http://www.example.com/api/products.json
  headers:
    Accept: 'application/json'
  identifier: upc
  identifierDepth: 0
  fields:
    - upc
    - name
    - description
    - price

destination:
  plugin: entity:node

process:
  type:
    plugin: default_value
    default_value: product

  title: name
  field_upc: upc
  field_description: description
  field_price: price

  sticky:
    plugin: default_value
    default_value: 0
  uid:
    plugin: default_value
    default_value: 0
```

The first section defines the migration machine name (`id`), human-readable `label`, group, and dependencies. You don't need to separately define the group outside of the `migration_group` defined here, though you might want to if you have many related migrations that need the same general configuration (see the migrate_example module included in Migrate Plus for more).

```
source:
  plugin: json_source
  path: http://www.example.com/api/products.json
  headers:
    Accept: 'application/json'
  identifier: upc
  identifierDepth: 1
  fields:
    - upc
    - title
    - description
    - price
```

The `source` section defines the migration source and provides extra data to help the source plugin know what information to retrieve, how it's formatted, etc. In this case, it's a very simple feed, and we don't need to do any special transformation to the data, so we can just give a list of fields to bring across into the Drupal Product content type.

The most important parts here are the `path` (which tells the JSON source plugin where to go to get the data), the `identifier` (the unique ID that should be used to match content in Drupal to content in the feed), and the `identifierDepth` (the level in the feed's hierarchy where the identifier is located).

```
destination:
  plugin: entity:node
```

Next we tell Migrate the data should be saved to a node entity (you could also define a destination of `entity:taxonomy`, `entity:user`, etc.).

```
process:
  type:
    plugin: default_value
    default_value: product

  title: name
  field_upc: upc
  field_description: description
  field_price: price

  sticky:
    plugin: default_value
    default_value: 0
  uid:
    plugin: default_value
    default_value: 0
```

Inside the `process` configuration, we'll tell Migrate which specific node type to migrate content into (in this case, `product`), then we'll give a simple field mapping between the Drupal field name (e.g. `title`) and the name of the field in the JSON feed's individual record (`name`). For certain properties, like a node's `sticky` status, or the `uid`, you can provide a default using the `default_value` plugin.

## Enabling the module, running a migration

Once the module is ready, go to the module page or use Drush to enable it, then use `migrate-status` to make sure the Product migration configuration was picked up by Migrate:

```
$ drush migrate-status
 Group: Products  Status  Total  Imported  Unprocessed  Last imported
 product          Idle    2      0         2
```

Use `migrate-import` to kick off the product migration:

```
$ drush migrate-import product
Processed 2 items (2 created, 0 updated, 0 failed, 0 ignored) - done with 'product'           [status]
```

You can then check under the content administration page to see if the products were migrated successfully:

<p style="text-align: center;">{{< figure src="./migrate-success-product-json.png" alt="Drupal 8 content admin - successful product JSON migration" width="604" height="263" class="insert-image" >}}</p>

If the products appear here, you're done! But you'll probably need to do some extra data transformation using a custom JSONReader to transform the data from the JSON feed into your custom content type. That's another topic for another day! You can also update all the migrated products with `migrate-import --update product`, or rollback the migration with `migrate-rollback product`.

> Note: Currently, the Migrate UI at `/admin/structure/migrate` is broken in Drupal 8.1.x, so using Drush is the only way to inspect and interact with migrations; even with a working UI, it's generally best to use Drush to inspect, run, roll back, and otherwise interact with migrations.

## Reinstalling the configuration for testing

Since the configuration you define inside your module's `config/install` directory is only read into the active configuration store at the time when you enable the module, you will need to re-import this configuration frequently while developing the migration. There are two ways you can do this. You could use some code like the following in your custom product migration's `migrate_custom_product.install` file:

```
<?php
/**
 * Implements hook_uninstall().
 */
function migrate_custom_product_uninstall() {
  db_query("DELETE FROM {config} WHERE name LIKE 'migrate.migration.custom_product%'");
  drupal_flush_all_caches();
}
?>
```

...or you can use the [Configuration Development](https://www.drupal.org/project/config_devel) module to easily re-import the configuration continuously or on-demand. The latter option is recommended, and is also the most efficient when dealing with more than just a single migration's configuration. I have a feeling `config_devel` will be a common module in a Drupal 8 developer's tool belt.

## Diving Deeper

Some of the inspiration for this post was found in [this more fully-featured example JSON migration module](https://github.com/heddn/d8_json_migrate), which was referenced in the issue [Include JSON example in the module](https://www.drupal.org/node/2626016) on Drupal.org. You should also make sure to read through the [Migrate API in Drupal 8](https://www.drupal.org/node/2127611) documentation.

[Download the source code of the custom product migration module example used in this blog post](./migrate_product.zip).
