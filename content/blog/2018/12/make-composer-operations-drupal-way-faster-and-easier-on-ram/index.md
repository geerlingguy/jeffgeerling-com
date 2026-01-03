---
nid: 2902
title: "Make composer operations with Drupal way faster and easier on RAM"
slug: "make-composer-operations-drupal-way-faster-and-easier-on-ram"
date: 2018-12-31T15:42:22+00:00
drupal:
  nid: 2902
  path: /blog/2018/make-composer-operations-drupal-way-faster-and-easier-on-ram
  body_format: markdown
  redirects: []
tags:
  - composer
  - drupal
  - drupal 8
  - drupal planet
  - optimization
  - performance
  - tutorial
---

> **tl;dr**: Run `composer require zaporylie/composer-drupal-optimizations:^1.0` in your Drupal codebase to halve Composer's RAM usage and make operations like `require` and `update` 3-4x faster.

A few weeks ago, I noticed Drupal VM's PHP 5.6 automated test suite started failing on the step that runs `composer require drupal/drush`. (**PSA**: [PHP 5.6 is officially dead](http://php.net/eol.php). Don't use it anymore. If you're still using it, upgrade to a supported version ASAP!). This was the error message I was getting from Travis CI:

```
PHP Fatal error:  Allowed memory size of 2147483648 bytes exhausted (tried to allocate 32 bytes) in phar:///usr/bin/composer/src/Composer/DependencyResolver/RuleWatchNode.php on line 40
```

I ran the test suite locally, and didn't have the same issue (locally I have PHP's CLI memory limit set to `-1` so it never runs out of RAM unless I do insane-crazy things.

So then I ran the same test but with PHP's `memory_limit` set to `2G`—yeah, that's two _gigabytes_ of RAM—and it failed! So I ran the command again using Composer's `--profile` option and `-vv` to see exactly what was happening:

```
# Run PHP 5.6 in a container.
$ docker run --rm -it drupaldocker/php-dev:5.6-cli /bin/bash
# php -v      
PHP 5.6.36 (cli) (built: Jun 20 2018 23:33:51) 

# composer create-project drupal-composer/drupal-project:8.x-dev composer-test --prefer-dist --no-interaction

# Install Devel module.
# cd composer-test
# composer require drupal/devel:^1.2 -vv --profile
Do not run Composer as root/super user! See https://getcomposer.org/root for details
[126.7MB/5.04s] ./composer.json has been updated
[129.6MB/6.08s] > pre-update-cmd: DrupalProject\composer\ScriptHandler::checkComposerVersion
[131.5MB/6.10s] Loading composer repositories with package information
[131.9MB/6.52s] Updating dependencies (including require-dev)
[2054.4MB/58.32s] Dependency resolution completed in 3.713 seconds
[2054.9MB/61.89s] Analyzed 18867 packages to resolve dependencies
[2054.9MB/61.89s] Analyzed 1577311 rules to resolve dependencies
[2056.9MB/62.68s] Dependency resolution completed in 0.002 seconds
[2055.5MB/62.69s] Package operations: 1 install, 0 updates, 0 removals
[2055.5MB/62.69s] Installs: drupal/devel:1.2.0
[2055.5MB/62.70s] Patching is disabled. Skipping.
[2055.5MB/62.80s]   - Installing drupal/devel (1.2.0): [2055.6MB/62.83s] [2055.6MB/63.02s] Downloading (0%)[2055.6MB/63.02s]                   [2[2055.6MB/63.04s] Downloading (5%)[2[2055.6MB/63.06s] Downloading (15%)[[2055.7MB/63.08s] Downloading (30%)[[2055.7MB/63.10s] Downloading (40%)[[2055.8MB/63.12s] Downloading (55%)[[2055.8MB/63.14s] Downloading (65%)[[2055.9MB/63.15s] Downloading (75%)[[2055.9MB/63.15s] Downloading (80%)[[2055.9MB/63.17s] Downloading (90%)[[2056.0MB/63.18s] Downloading (100%)[2055.5MB/63.19s] 
[2055.5MB/63.19s]  Extracting archive[2055.6MB/63.57s]     REASON: Required by the root package: Install command rule (install drupal/devel 1.x-dev|install drupal/devel 1.2.0)
[2055.6MB/63.57s] 
[2055.6MB/63.57s] No patches found for drupal/devel.
[731.5MB/71.30s] Writing lock file
[731.5MB/71.30s] Generating autoload files
[731.8MB/73.01s] > post-update-cmd: DrupalProject\composer\ScriptHandler::createRequiredFiles
[731.6MB/78.82s] Memory usage: 731.61MB (peak: 2057.24MB), time: 78.82s
```

So... when it started looking through Drupal's full stack of dependencies—some 18,867 packages and 1,577,311 rules—it gobbled up over 2 GB of RAM. No wonder it failed when `memory_limit` was `2G`!

That seems pretty insane, so I started digging a bit more, and found that the PHP 7.1 and 7.2 builds were _not_ failing; they peaked around 1.2 GB of RAM usage (yet another reason you should be running PHP 7.x—it uses way less RAM for so many different operations!).

Then I found a really neat package which had some outlandish promises: [composer-drupal-optimizations](https://github.com/zaporylie/composer-drupal-optimizations) mentioned in the README:

> Before: 876 MB RAM, 17s; After: 250 MB RAM, 5s

I went ahead and added the package to a fresh new Drupal project with:

    composer require zaporylie/composer-drupal-optimizations:^1.0

(Note that this operations still uses the same huge amount of memory and time, because the package to optimize things is being installed!)

And then I ran all the tests on PHP 5.6, 7.1, and 7.2 again. Instead of spelling out the gory details (they're all documented in [this issue in the Drupal VM issue queue](https://github.com/geerlingguy/drupal-vm/issues/1875)), here is a table of the amazing results:

<table>
  <tr>
    <th>PHP Version</th>
    <th>Before</th>
    <th>After</th>
    <th>Difference</th>
  </tr>
  <tr>
    <td>5.6</td>
    <td>2057.24 MB</td>
    <td>540.02 MB</td>
    <td>-1.5 GB</td>
  </tr>
  <tr>
    <td>7.1</td>
    <td>1124.52 MB</td>
    <td>426.64 MB</td>
    <td>-800 MB</td>
  </tr>
  <tr>
    <td>7.2</td>
    <td>1190.94 MB</td>
    <td>423.93 MB</td>
    <td>-767 MB</td>
  </tr>
</table>

You don't have to be on ancient-and-unsupported PHP 5.6 to benefit from the speedup afforded by ignoring unused/really old Symfony packages!

## Next Steps

You should immediately add this package to your Drupal site (if you're using Composer to manage it) if you run Drupal 8.5 or later. And if you use a newer version of Acquia BLT, [you're already covered](https://github.com/acquia/blt/pull/3121)! I'm hoping this package will be added upstream to `drupal-project` as well ([there's sort-of an issue for that](https://github.com/drupal-composer/drupal-project/issues/414)), and maybe even something could be done on the Drupal level.

Requiring over 1 GB of RAM to do even a simple `composer require` for a barebones Drupal site is kind-of insane, IMO.
