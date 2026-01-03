---
nid: 2674
title: "Migrating Link fields with multiple properties with Drupal 8"
slug: "migrating-link-fields-multiple-properties-drupal-8"
date: 2016-07-18T17:11:26+00:00
drupal:
  nid: 2674
  path: /blog/2016/migrating-link-fields-multiple-properties-drupal-8
  body_format: markdown
  redirects:
    - /blog/2016/migrating-fields-multiple-properties-drupal-8
aliases:
  - /blog/2016/migrating-fields-multiple-properties-drupal-8
tags:
  - drupal
  - drupal 8
  - drupal planet
  - links
  - migrate
---

Today I needed to migrate a URL/Link into a Drupal 8 site, and I was scratching my head over how to migrate it so there were distinct values for the URL (the actual link) and the Label (the 'title' that displays to end users and is clickable). Drupal 8's Link field type allows you to set a URL in addition to an optional (or required) label, but by default, if you just migrate the URL, the label will be blank.

I first set up the migration config like so:

```
...
process:
  field_url: source_url
```

And `source_url` was defined in the migration's `source.fields` configuration.

In my case, the source data didn't have a label, but I wanted to set a default label so the Drupal 8 site could display that as the clickable link (instead of an ugly long URL). To do that, it's similar to migrating a formatted text field, where you can migrate individual components of the field using the syntax `[field_name]/[component]`. In a Link field's case, it looks like:

```
...
process:
  'field_url/uri': source_url
  'field_url/title':
    plugin: default_value
    default_value: 'Click here!'
```

A lot easier than I was expecting—I didn't have to do anything in `PrepareRow` or even write my own plugin! I found that the parameters were `uri` and `title` by digging into the Link module's field `propertyDefinitions`, which lists a `uri`, `title`, and `options` (the definition is in [`Drupal\link\Plugin\Field\FieldType`](https://api.drupal.org/api/drupal/core!modules!link!src!Plugin!Field!FieldType!LinkItem.php/class/LinkItem/8.2.x).

Special thanks to [Richard Allen](https://www.drupal.org/u/richard.c.allen2386) for cluing me into this after I was looking for documentation to no avail (he pointed out that Link fields are probably just like the core Body field, which is migrated [like so](https://gist.github.com/allgood2386/d58702d1ba18f8233e2774f092265f75#file-gistfile1-txt-L16-L19), with `body/value`, `body/format`, etc.). He also mentioned that pinging people in the #drupal-migrate IRC channel is usually a helpful way to get help at this point in the game!
