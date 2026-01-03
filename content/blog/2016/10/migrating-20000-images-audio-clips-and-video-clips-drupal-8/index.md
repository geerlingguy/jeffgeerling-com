---
nid: 2701
title: "Migrating 20,000 images, audio clips, and video clips into Drupal 8"
slug: "migrating-20000-images-audio-clips-and-video-clips-drupal-8"
date: 2016-10-04T17:09:23+00:00
drupal:
  nid: 2701
  path: /blog/2016/migrating-20000-images-audio-clips-and-video-clips-drupal-8
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 6
  - drupal 8
  - drupal planet
  - file
  - files
  - media
  - migrate
  - migration
---

> **tl;dr**: If you want to skip the 'how-to' part and explanation, check out the [`pix_migrate` example Drupal 8 migration module](https://github.com/geerlingguy/drupal-8-example-pix_migrate) on GitHub.

For a couple years, I wanted to work on my first personal site migration into Drupal 8, for the last Drupal 6 site I had running on my servers. I've run a family photo/audio/video sharing website since 2009, and through the years it has accumulated hundreds of galleries, and over 20,000 media items.

<p style="text-align: center;">{{< figure src="./family-photos-and-events-website-display.jpg" alt="Family Photos and Events website display - desktop and mobile" width="500" height="357" class="insert-image" >}}<br>
<em>The home page of the Drupal 8 photo sharing website.</em></p>

I did a lot of work to get the Drupal 6 site as optimized and efficient as possible, but after official support for Drupal 6 was over, the writing was on the wall. I was fortunate to have a few days of time when I could rebuild the site in Drupal 8, work on a migration, and build a new theme for the site (fully responsive, with retina/responsive images, modern HTML5 media embeds, etc.!). I already wrote a couple other posts detailing parts of the site build and launch:

  - [Change the displayed username in Drupal 8 ala Realname](//www.jeffgeerling.com/blog/2016/change-displayed-username-drupal-8-ala-realname)
  - [How to get your server's emails through Gmail's spam filter with Exim](//www.jeffgeerling.com/blog/2016/how-get-your-servers-emails-through-gmails-spam-filter-exim)

And this will be the third post with some takeaways/lessons from the site build. I mostly write these as retrospectives for myself, since I'll likely be building another five or ten migrations for personal Drupal projects, and it's easier to refer back to a detailed blog post than to some old source code. Hopefully it helps some other people as well!

## Why I _Didn't_ Use Core's 'Migrate Drupal'

Migrate Drupal is a built-in migration path for Drupal 8 that allows some Drupal 6 or 7 sites to be migrated/upgraded to Drupal 8 entirely via the UI. You just tell the migration where your old database is located, click 'Next' a few times, then wait for the migration to complete. Easy, right?

As it turns out, there are still a lot of things that _aren't_ upgraded, like most file attachments, Views, and of course any module data for modules that haven't been ported to Drupal 8 yet (even for those that are, many don't have migration paths yet).

The module is still in 'experimental' status, and for good reason—for now, unless you have a _very_ simple blog or brochure-style Drupal 6 or 7 site, it's a good idea to spin up a local Drupal 8 site (might I suggest [Drupal VM](https://www.drupalvm.com/)?) and test your migration to see how things go before you commit fully to the Drupal 8 upgrade process.

## Building Custom Migrations

Since Migrate Drupal was out, I decided to build my own individual migrations, migrating all the core entities out of Drupal 6 and into Drupal 8. Since this was an SQL/database-based migration, almost everything I needed was baked into Drupal core. I also added a few contributed modules to assist with migrations:

  - **[Migrate Plus](https://www.drupal.org/project/migrate_plus)** - Adds a few conveniences to the migration pipeline, and also includes the best (and most up-to-date) migration example modules.
  - **[Migrate Tools](https://www.drupal.org/project/migrate_tools)** - Provides all the drush commands to make working with Migrate through a CLI possible.

Other than that, before working on any migration, I had to rebuild the structure of the website in Drupal 8 anew. For me, this is actually a fun process, as I can rebuild the content architecture from scratch, and ditch or tweak a lot of the little things (like extra fields or features) that I found were not needed from the Drupal 6 site.

One of my features of Drupal 8 is the fact that almost everything you need for any given content type is baked into core. Besides adding a number of media-related modules (see the official [Drupal 8 Media Guide](https://www.gitbook.com/book/drupal-media/drupal8-guide/details) for more) to support image, video, and audio entities (which are related to nodes), I only added a few contrib modules to add user registration spam prevention ([Honeypot](https://www.drupal.org/project/honeypot), a nicer [Admin Toolbar](https://www.drupal.org/project/admin_toolbar), and a helpful bundle of Twig extensions via [Twig Tweak](https://www.drupal.org/project/twig_tweak) that helped make theming (especially embedding views) easier.

Here's a high-level overview of the content architecture that drives the site:

<p style="text-align: center;">{{< figure src="./gallery-website-content-architecture.png" alt="Drupal image gallery website content architecture diagram" width="600" height="255" class="insert-image" >}}</p>

Or in text form (with a chain of dependencies):

  - **Users** (since all content belongs to a particular User).
  - **Files** (in Drupal, all files should be imported first, so they can be attached to entities later).
  - **Names** (this is a taxonomy, with a bunch of names that can be attached to photos (either via keyword match or manually tagging images).
  - **Images** (a Media Entity, which can have one User reference, one File reference, and one or more Name references).
  - **Galleries** (a Content Type, which can have one User reference, and one Image reference).

Once the site's structure was built out, and the basic administrative and end-user UX was working (this is important to make it easier to evaluate how the migration's working), I started building the custom migrations to get all the Drupal 6 data into Drupal 8.

## Getting Things in Order

Because Images depend on Users, Files, and Names, I had to set up the migrations so they would always run in the right order. It's hard to import an Image when you don't have the File that goes along with it, or the User that created the Image! Also, Galleries depend on Images, so I had to make sure they were imported last.

Knowing the content structure of the new site, and having the database of the old site already set up (I added both databases in the site's `settings.php` file like so:

```
<?php
/**
 * Database settings.
 */
$databases['default']['default'] = array (
  'database' => 'pix_site',
  'username' => 'pix_site',
  'password' => 'supersecurepassword',
  'prefix' => '',
  'host' => '127.0.0.1',
  'port' => '3306',
  'namespace' => 'Drupal\\Core\\Database\\Driver\\mysql',
  'driver' => 'mysql',
);
$databases['migrate']['default'] = array(
  'database' => 'pix_site_old',
  'username' => 'pix_site_old',
  'password' => 'supersecurepassword',
  'prefix' => '',
  'host' => '127.0.0.1',
  'port' => '3306',
  'namespace' => 'Drupal\\Core\\Database\\Driver\\mysql',
  'driver' => 'mysql',
);
?>
```

I decided to name my custom migration module `pix_migrate`, so I created a directory with that name, with an info file `pix_migrate.info.yml` that describes the module and its dependencies:

```
name: Pix Migrate
type: module
description: 'Migrations for media gallery site Drupal 6 to Drupal 8 upgrade.'
package: custom
version: '8.0'
core: '8.x'
dependencies:
  - migrate_plus
```

Once I had that structure set up, I could go to the Extend page or use Drush to enable the module: `drush en -y pix_migrate`; this would also enable all the other required Migrate modules, and at this point, I was ready to start developing the individual migrations!

### Aside: Developing and Debugging Migrations

During the course of building a migration, it's important to be able to quickly test mappings, custom import plugins, performance etc. To that end, here are a few of the techniques you can use to make migration development easier:

  - First things first: for every module that generates configuration, the module should also clean up after itself. For a Migration-related module, that means adding a `hook_install()` implementation in the module's .install file. See [this `hook_uninstall()` example](https://gist.github.com/geerlingguy/66b19e5e5450f069abe992d5e804842e) for details.
  - When you test something that relies on configuration in your module's 'install' directory (as we'll see Migrations do), you'll find it necessary to reload that configuration frequently. While you could uninstall and reinstall your module to reload the configuration (`drush pmu -y pix_migrate && drush en -y pix_migrate`), this is a little inefficient. Instead, you can:
  - Use one of the following modules to allow the quick refresh/reload/re-sync of configuration from your module's install directory (note that there are currently a number of solutions to this generic problem of 'how do I update config from my modules?'; it will be some time before the community gravitates towards one particular solution):
    - [Configuration Development](https://www.drupal.org/project/config_devel) module
    - [Configuration Update Manager](https://www.drupal.org/project/config_update) module
  - When _running_ migrations, there are some really helpful Drush commands provided by the Migrate Tools module, along with some flags that can help make the process go more smoothly:
    - When running a migration with `drush migrate-import` (`drush mi`), use `--limit=X` (where X is an integer) to just import _X_ items (instead of the full set). (Note that [there's currently a bug](https://www.drupal.org/node/2730081) that make multiple runs with `--limit` not work like you'd expect.)
    - When running a migration with `drush migrate-import`, use `--feedback=X` (where X is an integer) to show a status message after every _X_ items has been imported.
    - If a migration errors out or seems to get stuck, use `drush migrate-stop`, then `drush migrate-status` to see if the migration kicks back to 'Idle'. If it gets stuck on 'Stopping', and you're sure the Migration's not doing anything anymore (check CPU status), then you can use `drush migrate-reset-status` to reset the status to 'Idle'.
  - If a migration seems to be very slow, you can [use XHProf to profile Migrations via Drush](/blog/2016/poor-mans-xhprof-profiling-drupal-8-migrations-and-drush-commands), and hopefully figure out what's causing the slowness.

### Migration module file structure

As stated earlier, we have a folder with an .info.yml file, but here's the entire structure we'll be setting up in the course of adding migrations via configuration:

```
pix_migrate/
  config/
    install/
      [migrations go here, e.g. migrate_plus.migration.[migration-name].yml]
    src/
      Plugin/
        migrate/
          source/
            [Source plugins go here]
  pix_migrate.info.yml
  pix_migrate.install
```

## Our first migration: Users

> Note: ALL the code mentioned in this post is located in the GitHub repository [TODO](TODO). This is the module that I used to do all my imports, using Drupal 8.1.x.

Most of the time, the first migration you'll need to work on is the User migration—getting all the users who authored content into the new system. Since most other migrations depend on the authors being imported already, I usually choose to build this migration first. It also tends to be one of the easiest migrations, since Users _usually_ don't have to be related to other kinds of content.

I'll name all the migrations using the pattern `pix_[migration_name]` for the machine name, and 'Pix [Migration Name]' for the label. Starting with the User migration, here's how I defined the migration itself, in the file `pix_migrate/config/install/migrate_plus.migration.pix_user.yml`:

```
id: pix_user
migration_group: pix
migration_tags: {}
label: 'Pix User'

source:
  plugin: pix_user

destination:
  plugin: 'entity:user'

process:
  name: name
  pass: pass
  mail: mail
  init: init
  status: status
  created: created
  access: access
  login: login
  timezone: timezone_name
  roles:
    plugin: default_value
    default_value: 1

migration_dependencies: {}

dependencies:
  module:
    - pix_migrate
```

Note that all migration configurations follow the basic pattern:

```
# Meta info, like id, group, label, tags.

source:
  # Source definition or plugin.

destination:
  # Destination definition or plugin.

process:
  # Field mappings.

# migration_dependencies and dependencies.
```

For more documentation on the structure of the migration itself, please read through the example modules included with the [Migrate Plus](https://www.drupal.org/project/migrate_plus) module.

For the User migration, the configuration is telling Drupal, basically:

  1. Use the `pix_user` Migration source plugin (we'll create that later).
  2. Save `user` entities (using the `entity:user` Migration destination plugin).
  3. Map fields to each other (e.g. `name` to `name`, `mail` to `mail`, etc.).
  4. This migration requires the `pix_migrate` module, but doesn't require any other migrations to be run before it.

We could've used a different source plugin (e.g. the `csv` or `xml` plugin) if we were importing from different data sources, but since we are importing from an SQL database, we need to do define our own plugin (don't worry, it's just like Drupal 7 Migrations, but even simpler!), so we'll create that inside `pix_migrate/src/Plugin/migrate/source/PixUser.php`:

```
<?php

namespace Drupal\pix_migrate\Plugin\migrate\source;

use Drupal\migrate\Plugin\migrate\source\SqlBase;
use Drupal\migrate\Row;

/**
 * Source plugin for Pix site user accounts.
 *
 * @MigrateSource(
 *   id = "pix_user"
 * )
 */
class PixUser extends SqlBase {

  /**
   * {@inheritdoc}
   */
  public function query() {
    return $this->select('users')
      ->fields('users', array_keys($this->fields()))
      ->condition('uid', 0, '>')
      ->condition('uid', 1, '<>');
  }

  /**
   * {@inheritdoc}
   */
  public function fields() {
    $fields = [
      'uid' => $this->t('User ID'),
      'name' => $this->t('Username'),
      'pass' => $this->t('Password'),
      'mail' => $this->t('Email address'),
      'created' => $this->t('Account created date UNIX timestamp'),
      'access' => $this->t('Last access UNIX timestamp'),
      'login' => $this->t('Last login UNIX timestamp'),
      'status' => $this->t('Blocked/Allowed'),
      'timezone' => $this->t('Timeone offset'),
      'init' => $this->t('Initial email address used at registration'),
      'timezone_name' => $this->t('Timezone name'),
    ];

    return $fields;
  }

  /**
   * {@inheritdoc}
   */
  public function getIds() {
    return [
      'uid' => [
        'type' => 'integer',
      ],
    ];
  }

}
?>
```

In the plugin, we extend the [SqlBase](https://api.drupal.org/api/drupal/core!modules!migrate!src!Plugin!migrate!source!SqlBase.php/class/SqlBase/8.2.x) class, and only have to implement three methods:

  1. [`query()`](https://api.drupal.org/api/drupal/core%21modules%21migrate%21src%21Plugin%21migrate%21source%21SqlBase.php/function/SqlBase%3A%3Aquery/8.2.x): The query that is used to get rows for this migration.
  2. [`fields()`](https://api.drupal.org/api/drupal/core%21modules%21migrate%21src%21Plugin%21MigrateSourceInterface.php/function/MigrateSourceInterface%3A%3Afields/8.2.x): The available fields from the source data (you should explicitly list every field from which you need to get data).
  3. [`getIds()`](https://api.drupal.org/api/drupal/core%21modules%21migrate%21src%21Plugin%21MigrateSourceInterface.php/function/MigrateSourceInterface%3A%3AgetIds/8.2.x): Which source field (or fields) are the unique identifiers per row of source data.

There are other methods you can add to do extra work, or to preprocess data (e.g. `prepareRow()`), but you only _have_ to implement these three for a database-based migration.

The User migration is pretty simple, and I'm not going to go into details here—check out the examples in the Migrate Plus module for that—but I will step through a couple other bits of the other migrations that warrant further explanation.

## Second migration: Files

The File migration needs to migrate managed files from Drupal 6 to core file entities in Drupal 8; these file entities can then be referenced by 'Image' Media Entities later. The file migration is defined thusly, in `pix_migrate/config/install/migrate_plus.migration.pix_file.yml`:

```
id: pix_file
[...]
source:
  plugin: pix_file

destination:
  plugin: 'entity:file'
  source_base_path: https://www.example.com/
  source_path_property: filepath
  urlencode: true
  destination_path_property: uri

process:
  fid: fid
  filename: filename
  uri: filepath
  uid:
    -
      plugin: migration
      migration: pix_user
      source: uid
      no_stub: true
    -
      plugin: default_value
      default_value: 1
[...]
```

The important and unique parts are in the `destination` and `process` section, and I'll go through them here:

First, for the `entity:file` source plugin, you need to define a few more properties to make sure the migration succeeds. `source_base_path` allows you to set a base path for the files—in my case, I needed to add the URL to the site so Migrate would fetch the files over HTTP. You could also set a local filesystem path or any other base path that's accessible to the server running the migration. I used `urlencode: true` to make sure special characters and spaces were encoded (otherwise some file paths would fail). Then I told the plugin to use the `filepath` from the source to migrate files into the `uri` in the destination (this is a change from Drupal 6 to Drupal 8 in the way Drupal refers to file locations).

Then, for the `process`, some of the fields were easy/straight mappings (File ID, name, and path—which is morphed using the rules I set in the `destination` settings mentioned previously). But for the `uid`, I had to do a little special formatting. Instead of just a straight mapping, I defined _two_ processors—one the `migration` plugin, which allows me to define a migration from which a mapping should be used (the `pix_user` migration from earlier), and the other the `default_value` plugin.

In my case, I didn't import the user with uid of 1 during the `pix_user` migration, so I have to tell Migrate first, "don't stub out a user for missing users", then "for any files that don't have a user mapped from the old site, set a `default_value` of uid 1.

For the `PixFile.php` plugin definition (which defines the `pix_file` source plugin), I needed to do a tiny bit of extra work to get the filepath working with references in Drupal 8:

```
<?php
  /**
   * {@inheritdoc}
   */
  public function prepareRow(Row $row) {
    // Update filepath to remove public:// directory portion.
    $original_path = $row->getSourceProperty('filepath');
    $new_path = str_replace('sites/default/files/', 'public://', $original_path);
    $row->setSourceProperty('filepath', $new_path);

    return parent::prepareRow($row);
  }
?>
```

If I didn't do this, the files would show up and get referenced properly for Image media entities, but image thumbnails and other image styles wouldn't be generated (they'd show a 404 error). Note that if your old site's files directory is in a site-specific folder (e.g. `sites/example.com/files/`), you would need to replace the path using that pattern instead of `sites/default/files`.

## Third migration: Names

This is perhaps the simplest of all the migrations—please see the code in the [pix_migrate repository on GitHub](https://github.com/geerlingguy/drupal-8-example-pix_migrate). It's self-explanatory, and doesn't depend on any other migrations.

## Fourth migration: Image entities referencing files and names

The Image media entity migration is where the rubber meets the road; it has to migrate all the image node content from Drupal 6 into Drupal 8, while maintaining a file reference to the correct file, an author reference to the correct user, and name references to all relevant terms in the Names taxonomy.

First, let's look at the migration definition:

```
id: pix_image
[...]
source:
  plugin: pix_image

destination:
  plugin: 'entity:media'

process:
  bundle:
    plugin: default_value
    default_value: image
  name: title
  uid:
    -
      plugin: migration
      migration: pix_user
      source: uid
      no_stub: true
    -
      plugin: default_value
      default_value: 1
  'field_description/value': body
  'field_description/summary': teaser
  'field_description/format':
    plugin: default_value
    default_value: basic_html
  field_names:
    plugin: migration
    migration: pix_name
    source: names
  status: status
  created: created
  changed: changed
  'field_image/target_id':
    plugin: migration
    migration: pix_file
    source: field_gallery_image_fid

migration_dependencies:
  required:
    - pix_user
    - pix_file
    - pix_name
[...]
```

There's a bit to unpack here:

  - We're going to use a `pix_image` migrate source plugin to tell Migrate about source data, which we'll define later in `PixImage.php`.
  - We're importing Images as media entities, so we set the destination plugin to `entity:media`.
  - We want to save _Image_ media entities, so we have to define the `bundle` (in `process`) with a `default_value` of `image`
  - The `uid` needs to be set up just like with the `pix_file` migration, referring to the earlier `pix_user` migration mapping, but defaulting to uid 1 if there's no user migrated.
  - `field_description` is a complex field, with multiple possible values to map; so we can map each value independently (e.g. `field_description/value` gets mapped to the `body` text in Drupal 6, and `field_description/format` gets a default value of `basic_html`.
  - `field_names`, like `uid`, needs to refer to the `pix_name` migration for term ID mappings.
  - `field_image/target_id` needs to refer to the `pix_file` migration for file ID mappings.
  - This migration can't be run until Users, Names, and Files have been migrated, so we can _explicitly_ define that dependency in the `migration_dependencies` section. Set this way, Migrate won't allow this Image migration to be run until all the dependent migrations are complete.

There is also a little extra work that's necessary in the `pix_image` Migrate source plugin to get the body, summary, and Names term IDs from the source (I chose to do it this way instead of trying to get the `::query()` method to do all the necessary joins, just because it was a little easier with the weird database structure in Drupal 6):

```
<?php
  /**
   * {@inheritdoc}
   */
  public function prepareRow(Row $row) {
    // Get Node revision body and teaser/summary value.
    $revision_data = $this->select('node_revisions')
      ->fields('node_revisions', ['body', 'teaser'])
      ->condition('nid', $row->getSourceProperty('nid'), '=')
      ->condition('vid', $row->getSourceProperty('vid'), '=')
      ->execute()
      ->fetchAll();
    $row->setSourceProperty('body', $revision_data[0]['body']);
    $row->setSourceProperty('teaser', $revision_data[0]['teaser']);

    // Get names for this row.
    $name_tids = $this->select('term_node')
      ->fields('term_node', ['tid'])
      ->condition('nid', $row->getSourceProperty('nid'), '=')
      ->condition('vid', $row->getSourceProperty('vid'), '=')
      ->execute()
      ->fetchCol();
    $row->setSourceProperty('names', $name_tids);

    return parent::prepareRow($row);
  }
?>
```

## Final migration: Galleries referencing images

The fifth and final migration puts everything together. Since we changed a little of the content architecture from Drupal 6 to Drupal 8, there's a tiny bit of extra work that goes into getting each Gallery's images related to it correctly. In Drupal 6, the images each referenced a gallery node. In Drupal 8, each Gallery has a `field_images` field that holds the references to Image media entities.

So we can still map the images the same way as other fields are mapped in the migration configuration:

```
[...]
process:
  [...]
  field_images:
    plugin: migration
    migration: pix_image
    source: images
[...]
```

But to get the `images` field definition correct, we need to populate that field with an array of Image IDs from the Drupal 6 site in the `pix_gallery` source plugin:

```
<?php
  /**
   * {@inheritdoc}
   */
  public function prepareRow(Row $row) {
    [...]
    // Get a list of all the image nids that referenced this gallery.
    $image_nids = $this->select('content_type_photo', 'photo')
      ->fields('photo', ['nid'])
      ->condition('field_gallery_nid', $row->getSourceProperty('nid'), '=')
      ->execute()
      ->fetchCol();
    $row->setSourceProperty('images', $image_nids);

    return parent::prepareRow($row);
  }
?>
```

This query basically grabs all the old 'photo' node IDs from Drupal 6 that had references to the currently-being-imported `gallery` node ID, then spits that out as an array of node IDs. Migrate then uses that array (stored in the `images` field) to map old image nodes to new image media entities in Drupal 8.

## Conclusion

I often think migrations are full of magic... and sometimes they do seem that way, especially when they work on the first try and migrate a few thousand items at once! But when you dig into them, you find that beneath one simple line of abstraction (e.g. `title: title` for a field mapping), there is a lot of grunt work that Migrate module does to get the source data reliably and _repeatably_ into your fancy new Drupal 8 site.

This blog post is a little more rough than what I normally would write, and less 'tutorial-y', but I figure that most developers are like me—we learn by doing, but need to see _real-world_, _working_ examples before the light bulb goes off sometimes. Hopefully I've helped with _something_ through the course of writing this post.

Note that the migrations themselves took me a couple days to set up and debug, and I probably read through 10 other earlier blog posts, every line of certain classes' code, and all the documentation on Drupal.org pertaining to migrations in Drupal 8. Hopefully as time goes on and more examples are published, that aspect of migration development becomes less necessary :)
