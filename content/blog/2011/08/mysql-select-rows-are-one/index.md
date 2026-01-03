---
nid: 2333
title: "MySQL Select rows that are in one table but not in another"
slug: "mysql-select-rows-are-one"
date: 2011-08-29T17:11:29+00:00
drupal:
  nid: 2333
  path: /blogs/jeff-geerling/mysql-select-rows-are-one
  body_format: full_html
  redirects: []
tags:
  - database
  - left join
  - mysql
  - query
  - sql
aliases:
  - /blogs/jeff-geerling/mysql-select-rows-are-one
---

I've had to do this a couple times, and every time, I look around on Google for some good solutions, but don't find much. Basically, I have two tables of data, and I want to see if there are any rows in the first table that aren't in the second (or, conversely, I only want values that are in the first table AND the second).

To select rows in the first table that don't have any corresponding values in the second, try:

```
SELECT first.*
FROM first_table first
LEFT JOIN second_table second ON first.id = second.id
WHERE second.id IS NULL
```

Conversely, if you just want to select rows in the first table that are also in the second (but discard rows that don't have corresponding values in the second), try:

```
SELECT first.*
FROM first_table first
LEFT JOIN second_table second ON first.id = second.id
WHERE second.id IS NOT NULL
```

For my Drupal site, I needed to do something like:

```
<?php
$result = db_query("SELECT subs.*
  FROM {custom_subscriptions} subs
  LEFT JOIN {flag_content} flag ON flag.content_id = subs.content_id AND flag.uid = subs.uid
  WHERE subs.content_id = :content_id
    AND flag.content_id IS NOT NULL", array(
    ':content_id' => $content_id,
  ))->fetchAllAssoc('uid');
?>
```

Hope this helps!
