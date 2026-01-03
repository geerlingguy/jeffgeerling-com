---
nid: 2371
title: "PHP: Calculating Monthly/Yearly Billing Dates - Same day next month"
slug: "php-calculating-monthly"
date: 2011-07-07T16:06:00+00:00
drupal:
  nid: 2371
  path: /blogs/jeff-geerling/php-calculating-monthly
  body_format: full_html
  redirects: []
tags:
  - billing
  - date
  - functions
  - mktime
  - php
  - recurring
aliases:
  - /blogs/jeff-geerling/php-calculating-monthly
---

On a recent project, I needed to generate the timestamp for the 'same day, next month' for billing purposes. This can be tough in some circumstances, like when a user signs up on the 31st of August. What happens in September, when there are 30 days? If I were to simply try something like <code>strtotime('+1 month')</code>, I would get back the first day of October rather than September 30th. Same problem happens when someone hits February (oh my! only 28 days there... sometimes 29).

After looking through a bunch of different forums, Stack Overflow, etc., and finding that most people simply pro-rated the current month and billed people on the 1st (which is a valid option), I decided to write my own function that calculates the same day, next month, and simply gives the last day of the next month if the next month doesn't have as many days as this month.

It's pretty much self-documenting. It could probably be reworked to be a little faster, but I had to do this pretty quickly, and it's pretty robust imo:

```
<?php
/**
 * Function to calculate the same day one month in the future.
 *
 * This is necessary because some months don't have 29, 30, or 31 days. If the
 * next month doesn't have as many days as this month, the anniversary will be
 * moved up to the last day of the next month.
 *
 * @param $start_date (optional)
 *   UNIX timestamp of the date from which you'd like to start. If not given,
 *   will default to current time.
 *
 * @return $timestamp
 *   UNIX timestamp of the same day or last day of next month.
 */
function jjg_calculate_next_month($start_date = FALSE) {
  if ($start_date) {
    $now = $start_date; // Use supplied start date.
  } else {
    $now = time(); // Use current time.
  }

  // Get the current month (as integer).
  $current_month = date('n', $now);

  // If the we're in Dec (12), set current month to Jan (1), add 1 to year.
  if ($current_month == 12) {
    $next_month = 1;
    $plus_one_month = mktime(0, 0, 0, 1, date('d', $now), date('Y', $now) + 1);
  }
  // Otherwise, add a month to the next month and calculate the date.
  else {
    $next_month = $current_month + 1;
    $plus_one_month = mktime(0, 0, 0, date('m', $now) + 1, date('d', $now), date('Y', $now));
  }

  $i = 1;
  // Go back a day at a time until we get the last day next month.
  while (date('n', $plus_one_month) != $next_month) {
    $plus_one_month = mktime(0, 0, 0, date('m', $now) + 1, date('d', $now) - $i, date('Y', $now));
    $i++;
  }

  return $plus_one_month;
?>
```

What do you think? Any other ways to accomplish this task? (Note: I had to support PHP < 5.3, so I couldn't use some of the fancier new DateTime methods...).

[Edit: A similar function, to return the same day next year. For this function, the only special date, really, is February 29th. If you calculate from that date, March 1st of the following year will be returned. Not a huge deal for my site.]

```
<?php
/**
 * Function to calculate the same day one year in the future.
 *
 * @param $start_date (optional)
 *   UNIX timestamp of the date from which you'd like to start. If not given,
 *   will default to current time.
 *
 * @return $timestamp
 *   UNIX timestamp of the same day or last day of next month.
 */
function jjg_calculate_next_year($start_date = FALSE) {
  if ($start_date) {
    $now = $start_date; // Use supplied start date.
  } else {
    $now = time(); // Use current time.
  }
  $month = date('m', $now);
  $day = date('d', $now);
  $year = date('Y', $now) + 1;
  $plus_one_year = strtotime("$year-$month-$day"); // Use ISO 8601 standard.
  return $plus_one_year;
}
?>
```

