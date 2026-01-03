---
nid: 2895
title: "Testing the 'Add user' and 'Edit account' forms in Drupal 8 with Behat"
slug: "testing-add-user-and-edit-account-forms-drupal-8-behat"
date: 2018-12-03T22:20:48+00:00
drupal:
  nid: 2895
  path: /blog/2018/testing-add-user-and-edit-account-forms-drupal-8-behat
  body_format: markdown
  redirects: []
tags:
  - behat
  - drupal
  - drupal 8
  - drupal planet
  - featurecontext
  - testing
---

On a recent project, I needed to add some behavioral tests to cover the functionality of the [Password Policy](https://www.drupal.org/project/password_policy) module. I seem to be a sucker for pain, because often I choose to test the things it seems there's no documentation on—like testing the functionality of the partially-Javascript-powered password fields on the user account forms.

In this case, I was presented with two challenges:

  - I needed to run one scenario where a user edits his/her _own_ password, and must follow the site's configured password policy.
  - I needed to run another scenario where an admin creates a new user account, and must follow the site's configured password policy for the _created_ user's password.

So I came up with the following scenarios:

```
@password
Feature: Password Policy
  In order to verify that password policies are working
  As a user
  I should not be able to use a password
  Unless it meets the minimum site password policy constraints

  @api @authenticated
  Scenario: Users must meet password policy constraints
    Given users:
    | name                 | status | uid    | mail                             | pass         |
    | test.password.policy |      1 | 999999 | test.password.policy@example.com | fEzHZ3ru9pce |
    When I am logged in as user "test.password.policy"
    And I am on "/user/999999/edit"
    And I fill in "edit-current-pass" with "fEzHZ3ru9pce"
    And I fill in "edit-pass-pass1" with "abc123"
    And I fill in "edit-pass-pass2" with "abc123"
    And I press "edit-submit"
    Then I should see "The password does not satisfy the password policies."
    And I should see "Fail - Password length must be at least 12 characters."

  @api @authenticated @javascript
  Scenario: Password policy constraints are enforced when creating new users
    Given I am logged in as user "administrator_account"
    When I am on "/admin/people/create"
    And I fill in "mail" with "test.create.user@example.com"
    And I fill in "name" with "test.create.user"
    And I fill in "edit-pass-pass1" with "test.create.userABC123"
    And I fill in "edit-pass-pass2" with "test.create.userABC123"
    And I pause for "1" seconds
    And I press "edit-submit"
    Then I should see "The password does not satisfy the password policies."
```

Now, there are a couple annoying/special things I'm doing here:

  - For the first scenario, I had trouble making it work without specifying the uid of the new user, because I needed to get to the user edit page (`user/[id]/edit`), but for some reason trying a step like `And I click "Edit"` was not working for me.
  - The first scenario doesn't seem to have any trouble with the process of clicking submit then seeing the password policy validation error message—hold onto that thought for a second.
  - The second scenario uses `@javascript` to indicate this test should be run in a browser environment with javascript running. Apparently this means there is some tiny amount of delay between the time the 'edit-pass-passX' fields are filled in and the drupal password validation javascript does whatever it does—any time I would submit without a pause, I would get the error `"The specified passwords do not match."` _Infuriating!_

To resolve the third problem listed above, I added a custom step definition to my project's `FeatureContext`:

```
  /**
   * @When I pause for :seconds seconds
   */
  public function iPauseForSeconds($seconds) {
    sleep($seconds);
  }
```

And the way I finally figured out that it was a timing issue was because I stuck in a [Behat breakpoint](https://www.metaltoad.com/blog/what-i-learned-today-drupal-behat-breakpoints) (e.g. `And I break`) in different points in the scenario, and found it would work if I paused between tasks.

Sometimes testing can be a bit infuriating :P

I'm guessing there are a few slightly-better ways to get this done, but it works for me, and a 1s pause two times in my test suite isn't so bad.
