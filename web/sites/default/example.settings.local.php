<?php

// @codingStandardsIgnoreFile

/**
 * @file
 * Drupal local configuration file.
 */

$config['config_split.config_split.dev']['status'] = TRUE;

# Disable unless using a reverse proxy (e.g. Nginx caching on prod).
# $settings['reverse_proxy'] = TRUE;
# $settings['reverse_proxy_addresses'] = ['server.ip.address.here'];

$settings['trusted_host_patterns'] = [
  '^www\.jeffgeerling\.com$',
  '^localhost$',
];

$settings['hash_salt'] = 'GENERATE_YOUR_OWN_HASH_SALT';

$databases['default']['default'] = [
  'database' => 'drupal',
  'username' => 'drupal',
  'password' => 'drupal',
  'prefix' => '',
  'host' => 'mysql',
  'port' => '',
  'namespace' => 'Drupal\\Core\\Database\\Driver\\mysql',
  'driver' => 'mysql',
];

$config['search_api.server.hosted_apache_solr'] = [
  'backend_config' => [
    'connector_config' => [
      'host' => 'docker.for.mac.localhost',
      'path' => '/',
      'core' => '',
      'port' => '8984',
      'username' => '1181',
      'password' => 'TODO',
    ],
  ],
];

# Disable caching for local development.
$config['system.performance']['css']['preprocess'] = FALSE;
$config['system.performance']['js']['preprocess'] = FALSE;
$settings['cache']['bins']['render'] = 'cache.backend.null';
$settings['cache']['bins']['dynamic_page_cache'] = 'cache.backend.null';
$settings['cache']['bins']['page'] = 'cache.backend.null';

# Use development.services.yml.
$settings['container_yamls'][] = DRUPAL_ROOT . '/sites/development.services.yml';

# Don't harden permissions locally, it's just annoying.
$settings['skip_permissions_hardening'] = TRUE;
