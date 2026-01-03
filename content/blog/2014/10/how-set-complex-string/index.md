---
nid: 2469
title: "How to set complex string variables with Drush vset"
slug: "how-set-complex-string"
date: 2014-10-30T18:26:06+00:00
drupal:
  nid: 2469
  path: /blogs/jeff-geerling/how-set-complex-string
  body_format: full_html
  redirects: []
tags:
  - cli
  - drupal
  - drupal planet
  - drush
  - variables
---

I recently ran into an issue where <code>drush vset</code> was not setting a string variable (in this case, a time period that would be used in <code>strtotime()</code>) correctly:

```
# Didn't work:
$ drush vset custom_past_time '-1 day'
Unknown options: --0, --w, --e, --k.  See `drush help variable-set`      [error]
for available options. To suppress this error, add the option
--strict=0.
```

Using the <code>--strict=0</code> option resulted in the variable being set to a value of <code>"1"</code>.

After scratching my head a bit, trying different ways of escaping the string value, using single and double quotes, etc., I finally realized I could just use <code>variable_set()</code> with drush's <code>php-eval</code> command (shortcut <code>ev</code>):

```
# Success!
$ drush ev "variable_set('custom_past_time', '-1 day');"
$ drush vget custom_past_time
custom_past_time: '-1 day'
```

This worked perfectly and allowed me to go make sure my time was successfully set to one day in the past.
