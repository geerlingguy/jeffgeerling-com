---
nid: 2355
title: "Using apachebench (ab) with Drupal 7 to load test site with authenticated users"
slug: "using-apachebench-ab-drupal-7"
date: 2011-12-24T06:36:29+00:00
drupal:
  nid: 2355
  path: /blogs/jeff-geerling/using-apachebench-ab-drupal-7
  body_format: full_html
  redirects: []
tags:
  - ab
  - cli
  - drupal
  - drupal 7
  - drupal planet
  - performance
  - php
  - scalability
  - snippets
---

<a href="http://httpd.apache.org/docs/2.0/programs/ab.html">apachebench</a> is an excellent performance and load-testing tool for any website, and Drupal-based sites are no exception. A lot of Drupal sites, though, need to be measured not only under heavy anonymous traffic load (users who aren't logged in), but also under heavy authenticated-user load.

Drupal.org has some good <a href="http://drupal.org/node/659974">tips for ab testing</a>, but the details for using ab's '-C' option (notice the capital C... C is for Cookie) are lacking. Basically, if you pass the -C option with a valid session ID/cookie, Drupal will send ab the page as if ab were authenticated.

Instead of constantly going into the database and looking up session IDs and such nonsense, I have a simple script, which is quite revised from the <a href="http://2bits.com/articles/using-apachebench-benchmarking-logged-users-automated-approach.html">2008-era script originally from 2bits that worked with Drupal 5</a>, which will give you the proper ab commands for stress-testing your Drupal site under authenticated user load. Simply copy the attached script (source pasted below) to your site's docroot, and run the command from the command line as follows:

```
# [PATH_TO_SCRIPT] [HTTP_HOST] [URL_TO_TEST] [#_SESSIONS] [#_REQUESTS]
$ /path/to/drupal/root/ab-testing-cli.php www.example.com http://www.example.com/node/1 2 10
```

You'll get back the command to paste into the cli in order to test the URL you provided as an authenticated user. (Note: The sessions table needs to be populated for this to work, so someone (or a few someones) will need to have logged in during the past few hours/days for this to work correctly).

Here's the full code (file attached to bottom of post):

```
<?php
/**
 * @file
 *
 * Script to generate ab tests for logged in users using sessions from database.
 * This script is based on an older script by 2bits for load testing Drupal 5,
 * located at: http://goo.gl/4pfku
 *
 * Place this script into the webroot of your Drupal site.
 *
 * Usage (from command line):
 *   # [PATH_TO_SCRIPT] [HTTP_HOST] [URL_TO_TEST] [#_SESSIONS] [#_REQUESTS]
 *   $ php /path/to/drupal/root/ab-testing-cli.php example.com http://www.example.com/ 2 200
 *
 * After the script runs, it will output a list of commands for you to use to
 * test your website as a logged-in user.
 */

// Set the variable below to your Drupal root (on the server).
$drupal_root = '/path/to/drupal/root/';

// If arguments not supplied properly, warn user.
if ($argc != 5) {
  $prog = basename($argv[0]);
  print "Usage: $prog host url concurrency num_requests\n";
  exit(1);
}

// Get the arguments for ab.
$url = $argv[2];
$number_concurrency = $argv[3];
$number_requests = $argv[4];

// Set this directory to your drupal root directory.
chdir($drupal_root);

// Set up required variables to help Drupal bootstrap the correct site.
$_SERVER['HTTP_HOST'] = $argv[1];
$_SERVER['PHP_SELF'] = basename(__file__);
$_SERVER['REMOTE_ADDR'] = '127.0.0.1';
define('DRUPAL_ROOT', getcwd());

// Boostrap Drupal.
require_once('./includes/bootstrap.inc');
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);

// Get as many sessions as the user calls for.
$results = db_query_range("SELECT sid FROM {sessions} WHERE uid > 1", 0, $number_concurrency)->fetchAll();

// Loop through the results and print the proper ab command for each session.
foreach ($results as $result) {
  $cookie = session_name() . '=' . $result->sid;
  print "ab -c 1 -n $number_requests -C $cookie $url\n";
}
?>
```

