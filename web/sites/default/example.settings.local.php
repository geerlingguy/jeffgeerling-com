<?php

// @codingStandardsIgnoreFile

/**
 * @file
 * Drupal local configuration file.
 */

$settings['hash_salt'] = 'GENERATE_YOUR_OWN_HASH_SALT';

$databases['default']['default'] = [
  'database' => 'drupal',
  'username' => 'drupal',
  'password' => 'drupal',
  'prefix' => '',
  'host' => '127.0.0.1',
  'port' => '',
  'namespace' => 'Drupal\\Core\\Database\\Driver\\mysql',
  'driver' => 'mysql',
];

$databases['migrate']['default'] = [
  'database' => 'drupal',
  'username' => 'drupal',
  'password' => 'drupal',
  'prefix' => '',
  'host' => 'docker.for.mac.localhost',
  'port' => '3307',
  'namespace' => 'Drupal\\Core\\Database\\Driver\\mysql',
  'driver' => 'mysql',
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
