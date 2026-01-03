---
nid: 2731
title: "Testing redirections using Behat and the Behat Drupal Extension"
slug: "testing-redirections-using-behat-and-behat-drupal-extension"
date: 2017-01-13T18:33:22+00:00
drupal:
  nid: 2731
  path: /blog/2017/testing-redirections-using-behat-and-behat-drupal-extension
  body_format: markdown
  redirects: []
tags:
  - behat
  - blt
  - drupal
  - drupal 8
  - drupal planet
  - goutte
  - redirect
  - testing
---

One project I'm working on needed a Behat test added to test whether a particular redirection works properly. Basically, I wanted to test for the following:

  1. An anonymous user accesses a file at a URL like `http://www.example.com/pictures/test.jpg`
  2. The anonymous user is redirected to the path `http://www.example.com/sites/default/files/pictures/test.jpg`

Since the site uses Apache, I added the actual redirect to the site's `.htaccess` file in the docroot, using the following Rewrite configuration:

```
<IfModule mod_rewrite.c>
  RewriteEngine on

  # Rewrite requests for /profile_images to public files directory location.
  RewriteRule ^ pictures/(.*)$ /sites/default/files/pictures/$1 [L,NC,R=301]
</IfModule>
```

Testing with `curl --head`, I could see that the proper headers were set—`Location` was set to the correct redirected URL, and the response gave a `301`. So now I had to add the Behat test.

First, I created a .feature file to contain Redirection tests for my project (since it uses [Acquia's BLT](https://github.com/acquia/blt), I placed the file in `tests/behat/features` so it would automatically get picked up when running `blt tests:behat`):

```
Feature: Redirects
  In order to verify that redirects are working
  As a user
  I should be able to load a URL
  And I should be redirected to another URL

  # Note: Can't use "When I visit 'path'" because it expects a 200.
  @mink:goutte
  Scenario: Test a Picture redirect.
    Given I am not logged in
    When I do not follow redirects
      And I am on "/pictures/xyz.jpg"
    Then I am redirected to "/sites/default/files/pictures/xyz.jpg"
```

There are a couple unique aspects of this feature file which are worth highlighting:

  1. Testing redirects requires the GoutteDriver, so I've tagged the scenario (@mink:goutte) to indicate this requirement—see notes on the page [behat: 
intercepting the redirection with behat and mink](http://docs.behat.org/en/v2.5/cookbook/intercepting_the_redirections.html).
  2. I had to add the line `When I do not follow redirects` to make sure I can intercept the browser and tell it to _not_ follow redirects automatically. By default, it will follow redirects on the `And I am on [path]` line, and that would make my ability to test the actual redirection impossible.
  3. The `Then I am redirected to [path]` line is where the magic happens. I had to write a custom [Behat step definition](http://behat.org/en/latest/user_guide/context/definitions.html) to teach Behat how to test the redirection.

If I ran the test at this point, it would fail on the `When I do not follow redirects` line, because Behat doesn't yet know how to _not_ follow redirects. So I need to teach it by adding two step definitions to my FeatureContext class. Here's the class in it's entirety:

```
<?php
<?php

namespace Drupal;

use Drupal\DrupalExtension\Context\RawDrupalContext;
use Behat\Behat\Context\SnippetAcceptingContext;

// Needed for assert* functions from PHPUnit.
require_once '../../../../vendor/phpunit/phpunit/src/Framework/Assert/Functions.php';

/**
 * FeatureContext class defines custom step definitions for Behat.
 */
class FeatureContext extends RawDrupalContext implements SnippetAcceptingContext {

  /**
   * @When /^I do not follow redirects$/
   */
  public function iDoNotFollowRedirects() {
    $this->getSession()->getDriver()->getClient()->followRedirects(false);
  }

  /**
   * @Then /^I (?:am|should be) redirected to "([^"]*)"$/
   */
  public function iAmRedirectedTo($actualPath) {
    $headers = $this->getSession()->getResponseHeaders();
    assertTrue(isset($headers['Location'][0]));

    $redirectComponents = parse_url($headers['Location'][0]);
    assertEquals($redirectComponents['path'], $actualPath);
  }

}
?>
```

Notes for the customized `FeatureContext`:

  1. I had to require PHPUnit's functions to be able to `assert` certain things in the redirect test step definition, so I've manually loaded that file with `require_once`.
  2. `iDoNotFollowRedirects()` allows me to disable Goutte's automatic redirect handling.
  3. `iAmRedirectedTo()` is where the magic happens:
    1. The response headers for the original request are retrieved.
    2. The `Location` URL is extracted from those headers.
    3. The path (sans protocol/domain/port) is extracted.
    4. I assert that the path from the `Location` header matches the path that is being tested.

Now, when I run the test on my local environment (which runs Apache, so the .htaccess redirect is used), I get the following result:

```
1 scenario (1 passed)
4 steps (4 passed)
0m11.24s (31.16Mb)
```

Unfortunately, I then realized that the tests in our CI environment are currently using Drush's embedded PHP webserver, which doesn't support/use Apache `.htaccess` files. Therefore I'll either have to set up the CI environment using Apache instead of Drush, or use some other means of testing for the proper redirection (e.g. using PHPUnit to verify the right syntax appears inside the `.htaccess` file directly).
