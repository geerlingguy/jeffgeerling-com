---
nid: 2672
title: "Poor Man's XHProf profiling of Drupal 8 Migrations and Drush commands"
slug: "poor-mans-xhprof-profiling-drupal-8-migrations-and-drush-commands"
date: 2016-07-13T17:35:03+00:00
drupal:
  nid: 2672
  path: /blog/2017/poor-mans-xhprof-profiling-drupal-8-migrations-and-drush-commands
  body_format: markdown
  redirects:
    - /blog/2016/poor-mans-xhprof-profiling-drupal-8-migrations-and-drush-commands
aliases:
  - /blog/2016/poor-mans-xhprof-profiling-drupal-8-migrations-and-drush-commands
tags:
  - drupal
  - drupal 8
  - drupal planet
  - migrate
  - migrate tools
  - performance
  - xhprof
---

On a recent project, there was a Migration run that took a very long time, and I couldn't pinpoint why; there were multiple migrations, and none of the others took very long at all (usually processing at least hundreds if not thousands of nodes per minute). In Drupal 7, if you enabled the [XHProf module](TODO), then you'd get a checkbox on the configuration page that would turn on profiling for all page requests and Drush commands.

In Drupal 8, the XHProf module was completely rewritten, and as a side effect, the Drush/CLI profiling functionality is not yet present (see: [Profile drush/CLI with XHProf in Drupal 8](https://www.drupal.org/node/2765651)).

Since I don't have the time right now to help figure out how to get things working through the official XHProf module, I decided to use a 'poor man's profiling' method to profile a Migration run:

  1. Find the Migrate module's drush command file (`migrate_tools.drush.inc`).
  2. Inject the appropriate xhprof functions in the right places to set up and save a profiling run.
  3. Run the `drush mi [migration-name]` command.
  4. Profit!

In my case, since I was using [Drupal VM](https://www.drupalvm.com/) and it's default XHProf configuration, I had to add the following PHP:

```
<?php
/**
 * @param string $migration_names
 */
function drush_migrate_tools_migrate_import($migration_names = '') {
  // Enable XHProf profiling for CPU and Memory usage.
  xhprof_enable(XHPROF_FLAGS_CPU + XHPROF_FLAGS_MEMORY);

  ... migrate drush command code here ...

  // Disable XHProf, save the run into the configured directory.
  $xhprof_data = xhprof_disable();
  $XHPROF_ROOT = "/usr/share/php";
  include_once $XHPROF_ROOT . "/xhprof_lib/utils/xhprof_lib.php";
  include_once $XHPROF_ROOT . "/xhprof_lib/utils/xhprof_runs.php";
  $xhprof_runs = new XHProfRuns_Default();
  $run_id = $xhprof_runs->save_run($xhprof_data, "xhprof_testing");
}
?>
```

The `$XHPROF_ROOT` should point to the directory where you have XHProf installed.

After doing this, and running `drush mi [migration-name]`, I looked at the Drupal VM XHProf runs page (configured by default at `http://xhprof.[drupal-vm-name]/`), and noticed the new run (the one at the top—the second one in this screenshot was from a run I did while viewing the site in the browser):

<p style="text-align: center;">{{< figure src="./xhprof-drupal-vm-dashboard.png" alt="XHProf Drupal VM Dashboard page screenshot" width="416" height="157" class="insert-image" >}}</p>

See more on the PHP.net XHProf documentation pages, most notably the [XHProf example with optional GUI](http://php.net/manual/en/xhprof.examples.php) example.
