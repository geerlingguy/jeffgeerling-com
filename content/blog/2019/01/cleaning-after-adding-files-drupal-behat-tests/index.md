---
nid: 2904
title: "Cleaning up after adding files in Drupal Behat tests"
slug: "cleaning-after-adding-files-drupal-behat-tests"
date: 2019-01-11T19:51:41+00:00
drupal:
  nid: 2904
  path: /blog/2019/cleaning-after-adding-files-drupal-behat-tests
  body_format: markdown
  redirects: []
tags:
  - behat
  - drupal
  - drupal planet
  - php
  - testing
  - tutorial
---

I've been going kind of crazy covering a particular Drupal site I'm building in Behat tests—testing every bit of core functionality on the site. In this particular case, a feature I'm testing allows users to upload arbitrary files to an SFTP server, then Drupal shows those filenames in a streamlined UI.

I needed to be able to test the user action of "I'm a user, I upload a file to this directory, then I see the file listed in a certain place on the site."

These files are _not_ managed by Drupal (e.g. they're not file field uploads), but if they _were_, I'd invest some time in resolving this issue in the drupalextension project: ["When I attach the file" and Drupal temporary files](https://github.com/jhedstrom/drupalextension/issues/355).

Since they are just random files dropped on the filesystem, I needed to:

  1. Create a new step definition
  2. Track files that are created using that step definition
  3. Add code to make sure files that were created are cleaned up

If I just added a new step definition in my `FeatureContext` which creates the new files, then subsequent test runs on the same machine would likely fail, because the test files I created are still present.

Luckily, Behat has a mechanism that allows me to track created resources and clean up after the scenario runs (even if it fails), and those in Drupal-land may be familiar with the naming convention—they're called [hooks](http://docs.behat.org/en/v2.5/guides/3.hooks.html).

In this case, I want to add an `@AfterScenario` hook which runs after any scenario that creates a file, but I'm getting a little ahead of myself here.

## Create a new step definition

Whenever I want to create a new step definition, I start by writing out the step as I want it, in my feature file:

    When I add file "test.txt" to the "example" folder

Now I run the scenario using Behat, and Behat is nice enough to generate the stub function I need to add to my `FeatureContext` in it's output:

```
--- Drupal\FeatureContext has missing steps. Define them with these snippets:

    /**
     * @When I add file :arg1 to the :arg2 folder
     */
    public function iAddFileToTheFolder($arg1, $arg2)
    {
        throw new PendingException();
    }
```

I copy that code out, drop it into my `FeatureContext`, then change things to do what I want:

```
  /**
   * @When I add file :file_name to the :folder_name folder
   */
  public function iAddFileToTheFolder($file_name, $folder_name) {
    $file_path = '/some/system/directory/' . $folder_name . '/' . $file_name;
    $file = fopen($file_path, 'w');
    fwrite($file, '');
    fclose($file);
  }
```

Yay, a working Behat test step! If I run it, it passes, and the file is dropped into that folder.

But if I run it again, the file was already there and the rest of my tests may also be affected by this rogue testing file.

So next step is I need to track the files I create, and make sure they are cleaned up in an `@AfterScenario`.

## Track files created during test steps

At the top of my `FeatureContext`, I added:

```
  /**
   * Keep track of files added by tests so they can be cleaned up.
   *
   * @var array
   */
  public $files = [];
```

This array tracks a list of file paths, quite simply.

And then inside my test step, at the end of the function, I can add any file that is created to that array:

```
  /**
   * @When I add file :file_name to the :folder_name folder
   */
  public function iAddFileToTheFolder($file_name, $folder_name) {
    $file_path = '/some/system/directory/' . $folder_name . '/' . $file_name;
    $file = fopen($file_path, 'w');
    fwrite($file, '');
    fclose($file);
    $this->files[] = $file_path;
  }
```

That's great, but next we need to add an `@AfterScenario` hook to clean up the files.

## Make sure the created files are cleaned up

At the end of my feature context, I'll add a `cleanUpFiles()` function:

```
  /**
   * Cleans up files after every scenario.
   *
   * @AfterScenario @file
   */
  public function cleanUpFiles($event) {
    // Delete each file in the array.
    foreach ($this->files as $file_path) {
      unlink($file_path);
    }

    // Reset the files array.
    $this->files = [];
  }
```

This `@AfterScenario` is tagged with `@file`, so any scenario where I want the files to be tracked and cleaned up, I just need to add the `@file` tag, like so:

```
@myfeature
Feature: MyFeature

  @api @authenticated @javascript @file
  Scenario: Show changed files in selection form using Git on Site page.
    Given I am logged in as a user with the "file_manager" role
    When I am on "/directory/example"
    Then I should see the text "There are no files present in the example folder."
    And I should not see the text "test.txt"
    When I add file "test.txt" to the "example" folder
    And I am on "/directory/example"
    Then I should see the text "text.txt"
```

And that is how you do it. Now no matter whether I create one file or a thousand, any scenario tagged with `@file` will get all its generated test files cleaned up afterwards!
