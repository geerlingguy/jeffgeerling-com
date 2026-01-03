---
nid: 2989
title: "Install Drupal Coder and PHP CodeSniffer to your Drupal project to lint PHP code"
slug: "install-drupal-coder-and-php-codesniffer-your-drupal-project-lint-php-code"
date: 2020-04-07T18:55:21+00:00
drupal:
  nid: 2989
  path: /blog/2020/install-drupal-coder-and-php-codesniffer-your-drupal-project-lint-php-code
  body_format: markdown
  redirects: []
tags:
  - ci
  - coder
  - composer
  - development
  - drupal
  - drupal 8
  - drupal planet
  - lint
  - php
  - sniff
---

In the [official Coder Sniffer install guide](https://www.drupal.org/docs/8/modules/code-review-module/installing-coder-sniffer) on Drupal.org, it recommends installing Coder and the Drupal code sniffs globally using the command:

    composer global require drupal/coder

I don't particularly like doing that, because I try to encapsulate all project requirements _within that project_, especially since I'm often working on numerous projects, some on different versions of PHP or Drupal, and installing things globally can cause things to break.

So instead, I've done the following ([see this issue](https://github.com/geerlingguy/jeffgeerling-com/issues/49)) for my new JeffGeerling.com Drupal 8 site codebase (in case you haven't seen, I'm [live-streaming the entire migration process!](https://www.jeffgeerling.com/blog/2020/migrating-jeffgeerlingcom-drupal-7-drupal-8-how-video-series)):

  1. Install the [Coder module](https://www.drupal.org/project/coder) as a dev requirement, along with the [Composer installer for PHP_CodeSniffer coding standards](https://github.com/Dealerdirect/phpcodesniffer-composer-installer): `composer require --dev drupal/coder dealerdirect/phpcodesniffer-composer-installer`
  2. Verify the installation is working: `./vendor/bin/phpcs -i` (should list `Drupal` and `DrupalPractice` in its output).

Once it's working, you can start using `phpcs` which was installed into the `vendor/bin` directory:

```
./vendor/bin/phpcs \
  --standard="Drupal,DrupalPractice" -n \
  --extensions="php,module,inc,install,test,profile,theme" \
  web/themes/jeffgeerling \
  web/modules/custom
```

{{< figure src="./coding-standards-github-actions.png" alt="GitHub Actions - PHPCS coding standards Coder review for Drupal" width="650" height="373" class="insert-image" >}}

I also added a build stage to my site's GitHub Actions CI workflow which runs `phpcs` using the above command, to make sure my code is always _up to snuff_. You can see my [phpcs GitHub Actions configuration here](https://github.com/geerlingguy/jeffgeerling-com/blob/6db3e1486a0ebc177bc25ed7c1eda36eccfb3fe4/.github/workflows/ci.yml#L13-L37).

Happy coding!
