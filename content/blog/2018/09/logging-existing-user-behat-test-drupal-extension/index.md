---
nid: 2877
title: "Logging in as an existing user in a Behat test with the Drupal Extension"
slug: "logging-existing-user-behat-test-drupal-extension"
date: 2018-09-25T17:49:11+00:00
drupal:
  nid: 2877
  path: /blog/2018/logging-existing-user-behat-test-drupal-extension
  body_format: markdown
  redirects: []
tags:
  - behat
  - drupal
  - login
  - testing
---

There are some occasions when I want my Drupal Behat tests to perform some action as a user that already exists on the Drupal site. For example, I have a test install profile with some [Default Content](https://www.drupal.org/project/default_content) (users, nodes, taxonomy terms, etc.), and it already has a large set of default test data set up on the site for the benefit of developers who need to work on theming/site building.

Rather than define a ton of extra Behat steps to re-create all this test content and these test users, I just want Behat to log in as an existing user and perform actions with the pre-existing content.

Note that this might _not_ be a good idea depending on the structure or philosophy of your site's testing. As a general principle, state should be avoided—and that includes things like 'having a set of default stuff already existing before a test runs'. However, in the real world there are situations where it's a ton easier to just use the state that exists ?.

## The problem

Out of the box, the Drupal API Driver lets you create a user in a Scenario and then use that created user, like so:

```
  Scenario: Login as a user created during this scenario
    Given users:
    | name      | status |
    | Test user |      1 |
    When I am logged in as "Test user"
    Then I should see the link "Log out"
```

But if you try to log in as an existing user, e.g.:

```
  Scenario: Login as an existing user
    Given I am logged in as "Existing user"
    Then I should see the link "Log out"
```

You'll get the error:

```
Exception: No user with Existing user name is registered with the driver. in /var/www/html/vendor/drupal/drupal-extension/src/Drupal/DrupalUserManager.php:57
```

## The Solution

There are two ways you can solve this problem:

  1. You can write a bunch of steps to go to the login page, fill in a username and password, and click 'Log In', then do the rest of your scenario.
  2. You can write your own step definition, e.g. `iAmLoggedInAsUser()`.

The first option is okay, but then you have to store a password somewhere in your code (which just feels dirty, even if it's just for testing), and it's a few extra steps _every time you want to run a scenario as that user_!

For the second option, I quickly found the following issue in the Drupal Extension's issue queue: [Use drush user-login to login user](https://www.drupal.org/project/drupalextension/issues/1846828). Taking some of the examples from there, I came up with the following step definition in my FeatureContext.php file:

```
<?php
  /**
   * @Given I am logged in as user :name
   */
  public function iAmLoggedInAsUser($name) {
    $domain = $this->getMinkParameter('base_url');

    // Pass base url to drush command.
    $uli = $this->getDriver('drush')->drush('uli', [
      "--name '" . $name . "'",
      "--browser=0",
      "--uri=$domain",
    ]);

    // Trim EOL characters.
    $uli = trim($uli);

    // Log in.
    $this->getSession()->visit($uli);
  }
?>
```

Now I can write my Scenario like so:

```
  @api @javascript
  Scenario: Log in as Existing user
    Given I am logged in as user "Existing user"
    And I am on "/"
    Then I should see the link "Log out"
```

