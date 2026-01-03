---
nid: 2361
title: "Using Batch API to build huge CSV files for custom exports"
slug: "using-batch-api-build-huge-csv"
date: 2012-03-18T02:36:23+00:00
drupal:
  nid: 2361
  path: /blogs/jeff-geerling/using-batch-api-build-huge-csv
  body_format: full_html
  redirects: []
tags:
  - batch api
  - batch processing
  - csv
  - download
  - drupal
  - drupal 7
  - drupal planet
  - export
aliases:
  - /blogs/jeff-geerling/using-batch-api-build-huge-csv
---

<a href="http://www.flocknote.com/">Flocknote</a> is a large web application that lets churches easily manage communications with their members via email, text message, and phone calls. Many of the core features of email marketing services like MailChimp and Constant Contact are implemented in flocknote similarly, such as list management and mass emailing (and many features like shared list/member information management, text messaging, etc. are unique to flocknote).

Until recently, few groups using flocknote didn't have subscription lists that were big enough to hit our relatively high PHP max_time_limit setting when importing and exporting subscriber data. Since we're getting bigger, though, I've started implementing Batch API all over the place so user-facing bulk operations could not only complete without resulting in a half-finished operation, but could also show the end user exactly how much has been done, and how much is left:

<p style="text-align: center;">{{< figure src="./exporting-subscribers-batch-api.png" alt="Exporting List Subscribers - Batch API CSV Export" width="500" height="165" >}}</p>

I've seen many tutorials, blog posts, and examples for using Drupal's Batch API for <em>importing</em> tons of data, but very few (actually, none) for <em>exporting</em> tons of data—and specifically, in my case, building a CSV file with tons of data for download. The closest thing I've seen is a feature request in the Webform issue queue: <a href="http://drupal.org/node/1327186">Use BatchAPI to Export very large data sets to CSV/Excel</a>.

Before I get started, I want to mention that, for many people, something like <a href="http://drupal.org/project/views_data_export">Views Data Export</a> (for getting a ton of data out of a View) or <a href="http://drupal.org/project/node_export">Node Export</a> (specifically for exporting nodes) might be exactly what you need, and save you a few hours' time working with Batch API. However, since my particular circumstance ruled out Views, and since I was exporting a bit more customized data than just nodes or users, I needed to write my own batch export functionality.

<h2>Quick Introduction to the Batch API</h2>

I'm sure most of you have encountered Drupal's awesome Batch API at some point or another. It lets your site perform a task (say, updating a few thousand nodes) while the user can see a progress bar (which is always nice for UX) without running into the dreaded PHP timeout. Sometimes increasing PHP's max_time_limit can help, but if you want things to scale, and if you want to keep your PHP configuration sane, you should instead split the large operation up into smaller chunks of work—which is what Batch API does.

In my case, I wanted to integrate the batch operation with a form that allowed users to select certain parameters for their export. There's an excellent example in the <a href="http://drupal.org/project/examples">Examples for Developers</a> module here: <a href="http://drupalcode.org/project/examples.git/blob/refs/heads/7.x-1.x:/batch_example/batch_example.module">batch_example.module</a>. I'd suggest you read through that file to get the basics of how Batch API works along with a form submission.

Basically, when you submit the form, you set a batch with <a href="http://api.drupal.org/api/drupal/includes%21form.inc/function/batch_set/7">batch_set()</a>, then kick off the batch processing using <a href="http://api.drupal.org/api/drupal/includes%21form.inc/function/batch_process/7">batch_process()</a>.

<h2>Processing the Batch: Building a CSV file</h2>

For my huge CSV file, I needed to do a couple things to make sure I (a) didn't overwrite the file each time my batch process was called, and (b) had all the right data in all the right places.

In the function <code>MYMODULE_export_list_subscribers_batch()</code> (defined as the only operation in the $batch passed to batch_set()), I process 50 subscribers at a time, getting their profile data using some helper functions. I also check (in the first part) to see if the file has been created yet (basically, if this is the first or a later pass at the process function), and if it has not, I create the file, get the column headers for this particular list using a helper function, and store the filepath in the $batch's context.

I create a temporary file, which will automatically get cleaned out by the system after a while, because I just need the file to persist for a short while, until the user has downloaded the generated file (to get the filepath, I use <code>file_directory_temp()</code> and create a file with a list-specific file name.

On each pass of the batch process operation, I add in 50 more subscribers to the file (using <code>fopen()</code>, with the 'a' flag, so it adds on to the end of the file), and then store the current location of the file in the batch's context.

Code speaks louder than words, though, so here's the main batch operation function in all its glory (a few details are missing, but the relevant parts are all there):

```
<?php
/**
 * Batch operation to export list subscribers.
 */
function MYMODULE_export_list_subscribers_batch($list_id, $option, &$context) {
  // Start working on a set of results.
  $limit = 50;
  $context['finished'] = 0;

  // Create the CSV file with the appropriate column headers for this
  // list/network if it hasn't been created yet, and store the file path and
  // field data in the $context for later retrieval.
  if (!isset($context['sandbox']['file'])) {
    $list = node_load($list_id);

    // Get field names for this list/network. (I use a helper function here).
    $field_labels = array(
      'Member ID',
      'First Name',
      'Last Name',
      'Email Address',
      'Phone Number',
      'Created',
      'Last Updated',
      'etc...',
    );

    // Create the file and print the labels in the header row.
    $filename = 'list_' . $list_id . '_subscriber_export.csv';
    $file_path = file_directory_temp() . '/' . $filename;
    $handle = fopen($file_path, 'w'); // Create the file.
    fputcsv($handle, $field_labels); // Write the labels to the header row.
    fclose($handle);

    // Store file path, fields, subscribers, and network in $context.
    $context['sandbox']['file'] = $file_path;
    $context['sandbox']['fields'] = $fields;
    $context['sandbox']['subscribers'] = MYMODULE_retrieve_list_subscribers($list->nid, TRUE);
    $context['sandbox']['subscribers_total'] = count($context['sandbox']['subscribers']) - 1;

    // Store some values in the results array for processing when finshed.
    $context['results']['filename'] = $filename;
    $context['results']['file'] = $file_path;
    $context['results']['list_id'] = $list_id;
  }

  // Accounting.
  if (!isset($context['results']['count'])) {
    $context['results']['count'] = 0;
  }

  // Open the file for writing ('a' puts pointer at end of file).
  $handle = fopen($context['sandbox']['file'], 'a');

  // Loop until we hit the batch limit.
  for ($i = 0; $i < $limit; $i++) {
    $number_remaining = count($context['sandbox']['subscribers']) - 1;

    if ($number_remaining) {
      $uid = $context['sandbox']['subscribers'][$context['results']['count']];
      // I use a helper function to get the data for each subscriber.
      $subscriber_data = MYMODULE_retrieve_account_data_for_export($uid, $context['sandbox']['fields'], $context['sandbox']['network']);
      fputcsv($handle, $subscriber_data);

      // Remove the uid from $context.
      unset($context['sandbox']['subscribers'][$context['results']['count']]);

      // Increment the counter.
      $context['results']['count']++;
      $context['finished'] = $context['results']['count'] / $context['sandbox']['subscribers_total'];
    }
    // If there are no subscribers remaining, we're finished.
    else {
      $context['finished'] = 1;
      break;
    }
  }

  // Close the file.
  fclose($handle);

  // Show message updating user on how many subscribers have been exported.
  $context['message'] = t('Exported @count of @total subscribers.', array(
    '@count' => $context['results']['count'],
    '@total' => $context['sandbox']['subscribers_total'],
  ));
}
?>
```

There are a few things I can do to further optimize this, if need be; for example, I could probably run through the subscriber list in a better way, besides storing the whole thing (a bunch of integers) in an array, which doesn't scale infinitely. But those are micro-optimizations that I'll worry about if/when they become a problem.

<h2>Finishing the Batch: Delivering the CSV file</h2>

Because I want to deliver a .csv file download to the end-user, and not just display a simple message like 'Congratulations! We built your CSV file... but you have to click here to download it!', I decided to actually have the batch operation set CSV file download path in the user's session data, and then redirect to my own page for the end of the batch operation (to do this, I pass in the final path to <code>batch_process()</code> when I call it in the form submit function).

Here's the 'finished' function for the batch, where I simply set a message, and set a couple session variables that will be used later:

```
<?php
/**
 * Finish the export.
 */
function MYMODULE_export_list_subscribers_finished($success, $results, $operations) {
  // The 'success' parameter means no fatal PHP errors were detected. All
  // other error management should be handled using 'results'.
  if ($success) {
    $message = format_plural($results['count'], 'One subscriber exported.', '@count subscribers exported.');
  }
  else {
    $message = t('There were errors during the export of this list.');
  }
  drupal_set_message($message, 'warning');

  // Set some session variables for the redirect to the file download page.
  $_SESSION['csv_download_file'] = $results['file'];
  $_SESSION['csv_download_filename'] = $results['filename'];
}
?>
```

Here's the page building function for the path that I have the user go to at the end of the batch operation (after the _finished function is called above)—this page's path redirect is set by passing it into batch_process() as a simple string, way back in the form submit function:

```
<?php
/**
 * Interim download step for downloading CSV file.
 */
function MYMODULE_download_csv_file_interim($list_id) {
  global $base_url;

  if (empty($_SESSION['csv_download_filename']) || empty($_SESSION['csv_download_file'])) {
    return t('Please visit your list subscribers page to begin a list download.');
  }

  $list = node_load($list_id);

  // Redirect to the download file.
  $redirect = base_path() . 'path/to/download/csv/' . $list_id;
  drupal_add_js('setTimeout(function() { window.location.href = "' . $redirect . '"; }, 2000);', 'inline');

  $download_link = l(t('click here to download the file'), 'path/to/download/csv/' . $list_id);
  $output = '<p>' . t('Your subscriber list is now ready for download. The download should begin automatically. If it does not begin downloading within 5 seconds, please !download_link.', array('!download_link' => $download_link)) . '</p>';
  $output .= '<p>' . l(t("&#8592; Back to %list subscribers", array('%list' => $list->title)), 'node/' . $list_id . '/subscribers', array('html' => TRUE)) . '</p>';
  return $output;
}
?>
```

I used JavaScript/setTimeout() on this page, and redirected to another path that actually delivers the CSV file to the end user, because otherwise, most browsers will block the download (without user intervention), or go to the downloaded file and show a blank white page. Here's the code that's used to deliver the actual CSV file at the redirect path defined above:

```
<?php
/**
 * Download a list subscriber CSV file.
 */
function MYMODULE_download_csv_file($list_id) {
  // For added security, make sure the beginning of the path is the same as that
  // returned by file_directory_temp() (to prevent users from gaining access to
  // arbitrary files on the server).
  if (strpos($_SESSION['csv_download_file'], file_directory_temp()) !== 0) {
    return 'Access denied.';
  }

  // Add HTTP headers for CSV file download.
  drupal_add_http_header('Content-Type', 'text/csv; utf-8');
  drupal_add_http_header('Content-Disposition', 'attachment; filename=' . $_SESSION['csv_download_filename'], TRUE);

  // Allow caching, otherwise IE users can't dl over SSL (see issue #294).
  drupal_add_http_header('Cache-Control', 'max-age=300; must-revalidate');

  // Read the file to the output buffer and exit.
  readfile($_SESSION['csv_download_file']);
  exit;
}
?>
```

There are other ways to simply deliver a CSV file, but this seems to work the best for the widest variety of browsers. Setting the Cache-Control header is necessary to allow IE users to download files over SSL (due to caching settings and file path persistence in Windows/IE). Chrome, FireFox and Safari work fine without it...

<h2>Conclusion</h2>

I hope this example has helped you figure out how to use Batch API for more than just importing; it's a little more involved to build a file or something else using Batch API than to just do something that doesn't require extra steps afterwards. But with this example, hopefully you can start flexing Batch API's muscles to do a bit more for you!

If possible, I would always try using <a href="http://drupal.org/project/views_data_export">Views Data Export</a>, as it's so much simpler to integrate with my custom data sets, and Views is really fast and easy to implement. But in this case, I had to pull in access-controlled data from user profile fields, from Profile2 profile fields specific to each list, and from some other data sources, all into one CSV file, and this just wasn't going to happen with Views.

I've tested this Batch processing with up to 50,000 users, and it takes a few minutes to generate the resulting ~5MB file. It's much nicer to see that the file is being built over time (the way it is now) than to have to wait while the page is loading (with no feedback), and then get a WSOD because the page timed out after about 10,000 subscribers.
