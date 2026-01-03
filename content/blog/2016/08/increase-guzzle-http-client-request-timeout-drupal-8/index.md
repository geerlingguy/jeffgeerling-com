---
nid: 2686
title: "Increase the Guzzle HTTP Client request timeout in Drupal 8"
slug: "increase-guzzle-http-client-request-timeout-drupal-8"
date: 2016-08-18T16:56:42+00:00
drupal:
  nid: 2686
  path: /blog/2016/increase-guzzle-http-client-request-timeout-drupal-8
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
  - guzzle
  - http
  - settings.php
  - timeout
---

During some migration operations on a Drupal 8 site, I needed to make an HTTP request that took > 30 seconds to return all the data... and when I ran the migration, I'd end up with exceptions like:

```
Migration failed with source plugin exception: Error message: cURL error 28: Operation timed out after 29992 milliseconds with 2031262 out of 2262702 bytes received (see http://curl.haxx.se/libcurl/c/libcurl-errors.html).
```

The solution, it turns out, is pretty simple! Drupal's [`\Drupal\Core\Http\ClientFactory`](https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Http%21ClientFactory.php/class/ClientFactory/8.2.x) is the default way that plugins like Migrate's HTTP fetching plugin get a Guzzle client to make HTTP requests (though you could swap things out if you want via `services.yml`), and in the code for that factory, there's a line after the defaults (where the `'timeout' => 30` is defined) like:


```
<code>
<?php
$config = NestedArray::mergeDeep($default_config, Settings::get('http_client_config', []), $config);
?>
</code>
```

Seeing that, I know at a glance that Drupal is pulling any `http_client_config` configuration overrides from settings.php and applying them to the Guzzle Clients that this factory creates. Therefore, I can add the following to my site's `settings.php` to set the default timeout to `60` seconds instead of the default `30`:


```
<code>
<?php
/**
 * HTTP Client config.
 */
$settings['http_client_config']['timeout'] = 60;
?>
</code>
```

Pretty simple! You can override any of the other settings this way too, like the `proxy` settings (there's an example in the default settings.php file), `headers`, and whether to `verify` certificates for https requests.
