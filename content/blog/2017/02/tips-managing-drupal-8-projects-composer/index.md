---
nid: 2742
title: "Tips for Managing Drupal 8 projects with Composer"
slug: "tips-managing-drupal-8-projects-composer"
date: 2017-02-13T18:12:44+00:00
drupal:
  nid: 2742
  path: /blog/2017/tips-managing-drupal-8-projects-composer
  body_format: markdown
  redirects: []
tags:
  - composer
  - dependency management
  - drupal
  - drupal 8
  - drupal planet
  - packagist
---

It's been over a year since Drupal 8.0.0 was released, and the entire ecosystem has improved vastly between that version's release and the start of the 8.3.0-alpha releases (which [just happened](https://www.drupal.org/project/drupal/releases/8.3.0-alpha1) a couple weeks ago).

One area that's seen a vast improvement in documentation and best practices—yet still has a ways to go—is Composer-based project management.

Along with a thousand other 'get off the island' initiatives, the Drupal community has started to take dependency management more seriously, by integrating with the wider PHP ecosystem and maintaining a [separate Drupal.org packagist](https://www.drupal.org/node/2718229) for Drupal modules, themes, and other projects.

At a basic level, Drupal ships with a starter `composer.json` file that you can use if you're building simpler Drupal sites to manage modules and other dependencies. Then there are projects like the [Composer template for Drupal projects](https://github.com/drupal-composer/drupal-project) (which [Drupal VM](https://www.drupalvm.com) uses by default to build new D8 sites) and Acquia's [BLT](https://github.com/acquia/blt) which integrate much more deeply with Composer-based tools and libraries to allow easier patching, custom pathing, and extra library support.

One thing I've found lacking in my journey towards dependency management nirvana is a list of all the little tips and tricks that make managing a Drupal 8 project entirely via Composer easier. Therefore I'm going to post some of the common (and uncommon) things I do below, and keep this list updated over time as best practices evolve.

## Adding a new module

In the days of old, you would either download a module from Drupal.org directly, and drag it into your codebase. Or, if you were command line savvy, you'd fire up [Drush](http://www.drush.org/) and do a `drush dl modulename`. Then came Drush Makefiles, which allowed you to specify module version constraints and didn't require the entire module codebase to exist inside your codebase (yay for smaller repositories and repeatable deployments and site rebuilds!).

But with Composer, and especially with the way many (if not most) Drupal 8 modules integrate with required libraries (e.g. TODO Solarium/Solr/link to issue in search api solr module queue), it's easier and more correct to use `composer require` to add a new module.

Drupal.org modules don't quite follow semantic versioning, but the way release versioning works out with the Drupal.org packagist endpoint, you should generally be able to specify a version like "give me any version 8.x-1.0 or later, and I'll be happy".

Therefore, the proper syntax for requiring a module this way (so that when you run `composer update drupal/modulename` later, it will update to the latest stable 8.x-1.x release) is:

    composer require drupal/modulename:^1.0

This says "add modulename to my codebase, and download version 1.0 or whatever is the latest release in the 8.x-1.x release series (including alpha/beta releases, if there hasn't been a stable release yet).

> **Note on version constraints**: Two of the most-commonly-used version constraints I see are `~` (tilde) and `^` (caret). Both are similar in that they tell Composer: 'use this version but update to a newer version in the series', but the tilde is a bit more strict in keeping to the same minor release, while the caret allows for any new version up to the next major release. See this article for more details: [Tilde and caret version constraints in Composer](https://blog.madewithlove.be/post/tilde-and-caret-constraints/). See this Drupal core issue for discussion on why the caret is often preferred in Drupal projects: [Prefer carat over tilde in composer.json](https://www.drupal.org/node/2769841).

## Updating modules

Early on in my Composer adventures, I did the reasonable thing to update my site—I ran `composer update`, waited a while for everything to be updated, then I committed the updated `composer.json` and `composer.lock` files and was on my merry way. Unfortunately, doing this is kind of like cleaning a dirty blue dress shirt by washing it in a bucket of bleach—sure, the stain will be removed, but you'll also affect the rest of your shirt!

If you are meticulous about your dependencies, and lock in certain ones that are finicky at specific versions (e.g. `composer require drupal/modulename:1.2`) or at a specific git commit hash (`composer require drupal/modulename:dev-1.x#dfa710e`), then `composer update` is manageable.

But if you're managing a project with many moving parts using more than a dozen contributed modules... be cautious when considering running `composer update` without specifying specific modules to update!

Instead, what I recommend is a more cautious approach:

  1. See what modules need updating.
  2. Update those modules specifically using `composer update drupal/modulename --with-dependencies`.

If you had required the module using a release series like `drupal/modulename:^1.0`, then Composer will update that module—and _only_ that module—to the latest tagged release in the 8.x-1.x branch. And adding `--with-dependencies` will ensure that any libraries the module depends on are updated as well (e.g. if you update the Search API Solr module, the Solarium dependency will also be updated).

> Another quick tip: In addition to Drupal core's `update` module functionality and `drush pm-updatestatus`, you can use Composer's built-in mechanism to quickly scan for outdated dependencies. Just use `composer outdated`. This will show you if Drupal core, contrib modules, or any other dependencies are outdated.

## Removing modules

This one is pretty easy. To remove a module you're no longer using (be sure it's uninstalled first!):

    composer remove drupal/modulename

Older versions of Composer required a flag to also remove module dependencies that aren't otherwise required, but modern versions will remove the module and all it's dependencies from your composer.json, composer.lock, and the local filesystem.

## Requiring -dev releases at specific commits

From time to time (especially before modules are stable or have a 1.0 final release), it's necessary to grab a module at a specific Git commit. You can do this pretty simply by specifying the `dev-[branch]#[commit-hash]` version constraint. For example, to get the Honeypot module at it's latest Git commit (as of the time of this writing):

    composer require drupal/honeypot:dev-1.x#dfa710e

Be careful doing this, though—if at all possible, try to require a stable version, then if necessary, add a patch or two from the Drupal.org issue queues to get the functionality or fixes you need. Relying on specific dev releases is one way your project's [technical debt](https://en.wikipedia.org/wiki/Technical_debt) increases over time, since you can no longer cleanly `composer update` that module.

## Regenerating your `.lock` file

Raise your hand if you've ever seen the following after resolving merge conflicts from two branches that both added a module or otherwise modified the `composer.lock` file:

```
$ composer validate
./composer.json is valid, but with a few warnings
See https://getcomposer.org/doc/04-schema.md for details on the schema
The lock file is not up to date with the latest changes in composer.json, it is recommended that you run `composer update`.
```

Since I work on a few projects with multiple developers, I run into this on almost a daily basis. Until recently, I would find a module, then run a `composer update drupal/modulename`. Now, I just found that I can quickly regenerate the lockfile without updating or requiring anything, by running:

    composer update nothing

Note that some people on Twitter mentioned there's a `composer update --lock` command that does a similar thing. [The docs](https://getcomposer.org/doc/03-cli.md#update) say "Only updates the lock file hash to suppress warning about the lock file being out of date." — but I've had success with `nothing`, so I'm sticking with it for now until someone proves `--lock` is better.

## Development dependencies

There are often components of your project that you need when doing _development_ work, but you don't need on production. For example, Devel, XHProf, and Stage File Proxy are helpful to have on your local environment, but if you don't _need_ them in production, you should exclude them from your codebase entirely (not only for minor performance reasons and keeping your build artifacts smaller—non-installed modules _can_ still be a security risk if they have vulnerabilities).

Composer lets you track 'dev dependencies' (using [require-dev](https://getcomposer.org/doc/04-schema.md#require-dev) instead of `require`) that are installed by default, but can be excluded when building the final deployable codebase (by passing `--no-dev` when running `composer install` or `composer update`).

One concrete example is the inclusion of the Drupal VM codebase in a Drupal project. This VM configuration is intended _only_ for local development, and shouldn't be deployed to production servers. When adding Drupal VM to a project, you should run:

    composer require --dev geerlingguy/drupal-vm:^4.0

This will add `geerlingguy/drupal-vm` to a `require-dev` section in your `composer.json` file, and then you can easily choose to _not_ include that project in the deployed codebase.

## Commiting your `.lock` file

The [Composer documentation on the lock file](https://getcomposer.org/doc/01-basic-usage.md#composer-lock-the-lock-file) bolds the line:

> **Commit your application's `composer.lock` (along with `composer.json`) into version control.

For good reason—one of the best features of any package manager is the ability to 'lock in' a set of dependencies at a particular version or commit hash, so every copy of the codebase can be completely identical (assuming people haven't gone around `git --force push`ing changes to the libraries you use!), even if you don't include any of the code in your project.

Ideally, a project would just include a `composer.json` file, a `composer.lock` file, and any custom code (and config files). Everything else would be downloaded and 'filled in' by Composer. The lock file makes this possible.

## Patching modules

Acquia's [BLT](https://github.com/acquia/blt) the [`composer-patches`](https://github.com/cweagans/composer-patches) project, which is what it says on the tin: "Simple patches plugin for Composer."

Use is fairly simple: first, `composer require cweagans/composer-patches:^1.0`, then add a `patches` section to the `extra` section of your `composer.json` file:

```
    "extra": {
        "patches": {
            "acquia/lightning": {
                "New LightningExtension subcontexts do not autoload": "https://www.drupal.org/files/issues/2836258-3-lightning-extension-autoload.patch"
            },
            "drupal/core": {
                "Exposed date view filter fix": "https://www.drupal.org/files/issues/2369119-145_0.patch"
            }
    }
```

Once you've added a patch, you might wonder how to get Composer to apply the patch and update `composer.lock` while still maintaining the same version you currently have (instead of running `composer update drupal/module` which may or may not update/change versions of the module).

The safest way is to run `composer update none` (a handy trick yet again!), which allows Composer to delete the module in question (or core), then download the same version anew, and apply the specified patch.

## Other Tips and Tricks?

Do you know any other helpful Composer tricks or things to watch out for? Please post them in the comments below!

See related: [Composer and Drupal are still strange bedfellows](/blog/2017/composer-and-drupal-are-still-strange-bedfellows).
