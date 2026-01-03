---
nid: 2769
title: "Composer and Drupal are still strange bedfellows"
slug: "composer-and-drupal-are-still-strange-bedfellows"
date: 2017-05-04T02:31:29+00:00
drupal:
  nid: 2769
  path: /blog/2017/composer-and-drupal-are-still-strange-bedfellows
  body_format: markdown
  redirects: []
tags:
  - baltimore
  - composer
  - drupal
  - drupal planet
  - drupalcon
  - open source
  - php
---

More and more sites are being built in Drupal 8 (over 160,000 as of DrupalCon Baltimore 2017!). As developers determine best practices for Drupal 8 site builds and deployment, they need to come to terms with Composer. In one of the most visible signs that Drupal is 'off the island', many modules are now requiring developers to have at least a fundamental grasp of Composer and dependency management.

But even more than that, many developers now use Composer in place of manual dependency management or a simpler tools like Drush Make files.

With these major changes comes some growing pains. Seeing these pains on a daily basis, I wrote [Tips for Managing Drupal 8 projects with Composer](https://www.jeffgeerling.com/blog/2017/tips-managing-drupal-8-projects-composer) to highlight some best practices and tricks for making Composer more powerful and helpful.

But many developers still wrestle with Composer, and mourn the fact that deployments aren't as simple as dragging zip files and tarballs around between servers, or checking everything into a Git repository and doing a `git push`. For example:

  - If I manage my codebase with Composer and follow Composer's own recommendation—[don't commit dependencies in my vendor directory](https://getcomposer.org/doc/faqs/should-i-commit-the-dependencies-in-my-vendor-directory.md), what's the best way to actually deploy my codebase? Should I run `composer install` on my production web server? What about shared hosting where I might not have command line access at all?
  - Many modules (like [Webform](https://www.drupal.org/project/webform)) require dependencies to be installed in a `libraries` folder in the docroot. How can I add front end dependencies via Composer in custom locations outside of the `vendor` directory?

And on and on.

<p style="text-align: center;"><a href="https://www.flickr.com/photos/comprock/33483313043/in/pool-drupalconbaltimore2017/">{{< figure src="./drupalcon-baltimore-2017-keynote-wide.jpg" alt="DrupalCon Baltimore 2017 - participants sitting and waiting to see the opening Keynote" width="650" height="249" class="insert-image" >}}</a><br>
<em>Over 3,000 community members attended DrupalCon Baltimore 2017.</em><br>
<em>(Photo by Michael Cannon)</em></p>

During a BoF I led at DrupalCon Baltimore 2017 ([Managing Drupal sites with Composer](https://events.drupal.org/baltimore2017/bofs/managing-drupal-sites-composer)), we identified over 20 common pain points people are having with Composer, and for many of them, we discussed ways to overcome the problems. However, there are still a few open questions, or problems which could be solved in a number of different ways (some better than others).

I've taken all my notes from the BoF, and organized them into a series of problems (questions) and answers below. Please leave follow-up comments below this post if you have any other thoughts or ideas, or if something is not clear yet!

> Note: I want to make it clear I'm not against using Composer—quite the contrary, I've been using Composer for other PHP projects for years, and I'm glad Drupal's finally on board! But Drupal, with all it's legacy and complexity, does require some special treatment for edge cases, as evidenced by the breadth of problems listed below!

## Common Problems and Solutions with Drupal + Composer

Contents:

<ul>
<li><a href="#1">How do I deploy a Drupal codebase if the `vendor` directory isn't in the codebase?</a></li>
<li><a href="#2">I need to put a library (e.g. CKEditor for Webform) in the `libraries` directory, and not in `vendor`. Is this even possible with Composer?</a></li>
<li><a href="#3">One frontend library I need to add to my site (for a module, not a theme) is not on Packagist. How can I `composer require` it without it being on Packagist?</a></li>
<li><a href="#4">What's the best way to start building the codebase for a new Drupal 8 website?</a></li>
<li><a href="#5">If I have a multisite installation, how can I put certain modules in one `sites/site-a/modules` directory, and others in another `sites/site-b/modules` directory?</a></li>
<li><a href="#6">Using the command line to install modules is a lot to ask. Isn't there some sort of UI I could use?</a></li>
<li><a href="#7">What happens if there are dependencies required by two modules or core and a module, and there's a conflict with version requirements?</a></li>
<li><a href="#8">How can I include libraries and shared modules that I made for my own sites (they're not on Packagist)?</a></li>
<li><a href="#9">I have a Drush make file for my site. Can I easily convert this to a `composer.json` file?</a></li>
<li><a href="#10">I set up my Drupal 8 site by downloading archives from Drupal.org and copying them into the codebase. How can I convert my codebase to use a `composer.json` file?</a></li>
<li><a href="#11">What is the difference between `^` and `~` in version requirements, and should I use one over the other?</a></li>
<li><a href="#12">When I run `composer update` a lot of weird things happen and everything is updated, even if I don't want it to be updated. Is there a way I can just update one module at a time?</a></li>
<li><a href="#13">When I run `composer install` on my production server, it runs out of memory. How can I avoid this issue?</a></li>
<li><a href="#14">For security reasons, I need to verify that the code I'm running in production wasn't hacked or modified. How can I do this if I'm using Composer to manage my dependencies?</a></li>
<li><a href="#15">I totally screwed up some of the dependencies on my site while I was tinkering with them. Is there any way to 'nuke' all the things in my codebase that Composer manages so I can do a fresh `composer install` and get them back into the correct state (short of deleting my entire codebase and re-cloning my site locally)?</a></li>
<li><a href="#16">My team constantly battles with `composer.lock` file merge conflicts. How can we avoid this painful experience?</a></li>
<li><a href="#17">Do you have any other tips for making Composer use easier and more delightful?</a></li>
</ul>

<a name="1"></a>

### How do I deploy a Drupal codebase if the `vendor` directory isn't in the codebase?

This was one of the most discussed issues. Basically: If it's best to not commit the `vendor` directory to my Git repository, and I deploy my Git repository to my production server... how do I run my site in production?

In the old days, we used to commit every file for every module, theme, and library—custom or contributed—to our website's codebase. Then, we could just `git push` the codebase to the production web server, and be done with it. But nowadays, there are two different ways you can _not_ commit everything and still run a codebase on production:

  1. **Using Deployment Artifacts**: [Acquia's BLT project](https://github.com/acquia/blt) is the best example of this—instead of cloning your source code repository to the production server, BLT uses an intermediary (either a developer locally, or in a CI environment like Travis CI or Jenkins) to 'build' the codebase, and then commit the 'build' (the artifact to be deployed, containing _all_ code, including core, contrib modules, libraries, etc.) to a special branch or a separate repository entirely. Then you deploy this artifact to production.
  2. **Run `composer install` on Prod**: This is often a simpler solution, as you can still use the tried-and-true 'git push to prod' method, then run `composer install` in place, and all the new dependencies will be installed.

The second method may seem simpler and more efficient at first, but _there be dragons_. Not only is it likely that Composer (which is quite the RAM-hungry monster) will run out of memory, leaving a half-built copy of your codebase, it's also difficult to manage the more complicated deployment steps and synchronization required to make this work well.

The first method is the most stable production deployment option, but it requires either two separate Git repositories, or some other mechanism of storing the deployment artifact, and it requires an additional manual step or a CI system to actually build the deployment artifact.

Some hosting providers like Acquia are building new systems like [Acquia Cloud CD](https://www.acquia.com/products-services/acquia-cloud-cd) to make the deployment artifact process more streamlined. But in either case (`composer install` on prod or deployment artifacts), there are tradeoffs.

<a name="2"></a>

### I need to put a library (e.g. CKEditor for Webform) in the `libraries` directory, and not in `vendor`. Is this even possible with Composer?

Using the [composer/installers](http://composer.github.io/installers/) package, you can set specific paths for certain `type`s of packages, and you can even set specific directories per-package _as long as the package has a `type` and requires `composer/installers`_.

The last bit is the part that makes this a little difficult. Let's take two examples:

First, if you want to install all the Drupal modules (`type` of `drupal-module`) into your codebase in `docroot/modules/contrib`. Tell Composer by setting paths in the `extra` section of `composer.json`:

    "extra": {
        "installer-paths": {
            "docroot/core": [
                "type:drupal-core"
            ],
            "docroot/modules/contrib/{$name}": [
                "type:drupal-module"
            ],
            "docroot/themes/contrib/{$name}": [
                "type:drupal-theme"
            ],
            "docroot/libraries/{$name}": [
                "type:drupal-library"
            ],
        },
    }

Now, lets say you've installed the Webform module, which requires the [geocomplete](https://github.com/ubilabs/geocomplete) library be placed inside your site's `libraries` directory.

Since geocomplete isn't available through Packagist (and doesn't have `type: 'drupal-library'`), we can't easily tell Composer to put that particular library somewhere outside of `vendor`.

Currently, there are three ways to work around this issue, and all of them are slightly hacky (in my opinion):

  1. Add the [Composer Installers Extender](https://github.com/oomphinc/composer-installers-extender) plugin, which allows you to set a custom install path _per-dependency_.
  2. Add the library as a custom repository in your `composer.json` file's `repositories` section:

      "repositories": {
          "drupal": {
              "type": "composer",
              "url": "https://packages.drupal.org/8"
          },
          "fontawesome-iconpicker": {
              "type": "package",
              "package": {
                  "name": "itsjavi/fontawesome-iconpicker",
                  "version": "v1.3.0",
                  "type": "drupal-library",
                  "extra": {
                      "installer-name": "fontawesome-iconpicker"
                  },
                  "dist": {
                      "url": "https://github.com/itsjavi/fontawesome-iconpicker/archive/1.3.0.zip",
                      "type": "zip"
                  },
                  "require": {
                      "composer/installers": "~1.0"
                  }
              }
          }
      }

  3. Attach a script to one of Composer's 'hooks' to move the library at the end of the `composer install` process. See the [Composer Scripts](https://getcomposer.org/doc/articles/scripts.md) documentation for more info and examples.

After the BoF, I opened a core issue, [Drupal core should help make 3rd party library management not torturous](https://www.drupal.org/node/2873160), and basically asked if it might be possible for Drupal core to solve the problem using something like the third option, but using a class or library that was provided by core and available to all contributed and custom Drupal projects (instead of each codebase solving the problem in some one-off way).

The workarounds are all a bit burdensome, even after you have a few site builds under your belt. Hopefully this situation improves over time (note that a similar issue, [Best practices for handling external libraries in Drupal 8](https://www.drupal.org/node/2605130), has been open since late 2015).

<a name="3"></a>

### One frontend library I need to add to my site (for a module, not a theme) is not on Packagist. How can I `composer require` it without it being on Packagist?

There are two ways you can add packages that might exist on frontend packaging sites, but not Packagist:

  1. Use [Asset Packagist](https://asset-packagist.org) to require Bower or NPM packages (even if they're not on Packagist).
  2. Either get the upstream package maintainer to add a `composer.json` file to the package repo and submit it to Packagist, or fork the repository and add your fork to Packagist.

The former option is my preferred method, though I've had to do the second option in a pinch a couple times. The best long-term solution is to try to get the upstream library added to Packagist, so you don't have any extra maintenance burden.

<a name="4"></a>

### What's the best way to start building the codebase for a new Drupal 8 website?

The community seems to have settled on using a starter template like the [Composer template for Drupal projects](https://github.com/drupal-composer/drupal-project). In the beginning, some people did a `require drupal/core` to kick off a new Drupal codebase... but doing that can lead to some pain further down the road (for various reasons).

When you start with the Composer template, or something like Acquia's BLT, you have more flexibility in deploying your site, storing things in different places in your repository, and a more stable upgrade path.

See the documentation on Drupal.org for more info: [Using Composer to manage Drupal site dependencies](https://www.drupal.org/docs/develop/using-composer/using-composer-to-manage-drupal-site-dependencies).

<a name="5"></a>

### If I have a multisite installation, how can I put certain modules in one `sites/site-a/modules` directory, and others in another `sites/site-b/modules` directory?

You're in luck! Just like we can do with libraries (see the earlier question above), we can use the [composer/installers](http://composer.github.io/installers/) package to define a specific directory _per-dependency_ (as long as the dependencies—e.g. modules or themes—have a `type` assigned):

    "extra": {
        "installer-paths": {
            "sites/example.com/modules/{$name}": ["drupal/module"]
        }
    }

<a name="6"></a>

### Using the command line to install modules is a lot to ask. Isn't there some sort of UI I could use?

You're in luck again! Matt Glaman built a fancy UI, [Conductor](https://github.com/mglaman/conductor), to use with Composer (he's asked for feedback on GitHub of how he can make it even better). Additionally, some IDEs have support for basic functionality (e.g. [Composer PHP Support](https://marketplace.eclipse.org/content/composer-php-support) for Eclipse, or the [Sublime Text Composer plugin](https://github.com/francodacosta/composer-sublime)).

And finally, _There's a core issue for that™_: [Do not leave non-experts behind: do not require Composer unless a GUI is also included](https://www.drupal.org/node/2845379).

Just like with Git, though, it pays dividends to know how to use Composer on the command line.

<a name="7"></a>

### What happens if there are dependencies required by two modules or core and a module, and there's a conflict with version requirements?

This... is a hard problem to solve. As Drupal has moved to a more semver-style release cadence (8.x.0 releases can include major new features, and could drop experimental modules), there are times when a core dependency and a contributed module or install profile dependency might conflict (e.g. core requires version 1.3.2 or later, and an install profile you're using requires version 1.2.9 but nothing later than 1.2).

In these cases, the best option is likely to get the non-core packages (e.g. contrib modules, profiles, themes, etc.) to align with Drupal core. When two different modules or other contrib libraries conflict, the best option is to work it out between the two modules in their issue queues, or to manually override one of the dependency definitions.

This is a hard problem to solve, and best practices here are still being discussed.

<a name="8"></a>

### How can I include libraries and shared modules that I made for my own sites (they're not on Packagist)?

Many people have private modules or themes they use on multiple Drupal codebases, where they want to maintain the module or theme separately from the individual sites. In these situations, there are two options:

  1. You can add additional `repositories` in your `composer.json` file, one for each of these custom libraries, then you can `composer require` them just like any other dependency.
  2. If you have many of these dependencies, you could set up a [private Packagist](https://packagist.com). This option is probably best for large organizations that have specific security requirements and a number of custom libraries and packages.

See related documentation in the Composer docs: [Handling private packages](https://getcomposer.org/doc/articles/handling-private-packages-with-satis.md).

<a name="9"></a>

### I have a Drush make file for my site. Can I easily convert this to a `composer.json` file?

Well, there's the [Drush makefile to composer.json converter tool](https://github.com/jpstacey/drush-m2c), but other than that, it might be easiest to regenerate your site from scratch using something like the [Composer template for Drupal projects](https://github.com/drupal-composer/drupal-project).

Note that if you built your site by hand using .zip or .tar.gz downloads, you can use Drush to at least generate a makefile (see [`drush make-generate`](https://drushcommands.com/drush-8x/make/make-generate/)).

<a name="10"></a>

### I set up my Drupal 8 site by downloading archives from Drupal.org and copying them into the codebase. How can I convert my codebase to use a `composer.json` file?

See the above question—you can't easily go straight from custom codebase to Composer-managed, but you can use [`drush make-generate`](https://drushcommands.com/drush-8x/make/make-generate/) to generate a Drush Make file; and from there you can convert to a Composer-based project.

<a name="11"></a>

### What is the difference between `^` and `~` in version requirements, and should I use one over the other?

Put simply:

  - `~`: `~8.3` won't go to 8.4.0
  - `^`: `^8.3` will go to 8.4.x, 8.5.x, etc. to 8.9xxx

Both operators tell Composer 'use at least this version or higher', but the `~` says "stay within the same minor release (8.3.x)", while the `^` says "stay within the same major release (all releases up to, but not including, 9.0.0)".

There's some good discussion about standards in core here: [Prefer carat over tilde in composer.json](https://www.drupal.org/node/2769841), and as with most other things, you should also read through the [official Composer documentation](https://getcomposer.org/doc/articles/versions.md#tilde) for a more canonical answer.

As long as you trust a module or library's maintainers to follow semver standards and not break backwards compatibility within a major release, it's best to use the `^` to indicate required minimum versions (e.g. `composer require drupal/honeypot ^1.0.0`.

<a name="12"></a>

### When I run `composer update` a lot of weird things happen and everything is updated, even if I don't want it to be updated. Is there a way I can just update one module at a time?

Yes! In fact, in real world usage, you'd rarely run `composer update` alone.

To just update one module or library at a time, you should run the command (e.g. for Honeypot):

    composer update drupal/honeypot --with-dependencies

When you add those arguments, you are telling Composer:

  - _Only_ update Honeypot
  - Check if Honeypot has any dependencies that also need updating
  - Don't update anything else!

This is generally safer than running `composer update` alone, which will look at all the modules, themes, etc. on your site and update them. _Technically_ speaking, if we lived in an ideal world where patch and minor releases never broke anything, `composer update` would be perfectly safe, even if it updated every module on your site.

But we live in the real world, and despite the best efforts of module maintainers, many bugfix and patch releases end up breaking something. So better safe updating one thing at a time, then committing that update (so you can verify exactly where something went wrong in the case of failure).

<a name="13"></a>

### When I run `composer install` on my production server, it runs out of memory. How can I avoid this issue?

Short answer: don't use Composer on your production server. Build a deployment artifact instead (on a non-production server), then deploy the artifact to production.

More realistic answer: If you _have_ to use Composer in production (e.g. you deploy your codebase then run `composer install` as part of your deployment process), you might need to bump up your command line PHP `memory_limit`. See Composer's [troubleshooting guide for memory limit errors](https://getcomposer.org/doc/articles/troubleshooting.md#memory-limit-errors).

Another realistic answer if you don't want to use CI or some other means of building your production codebase: commit `vendor` directories and all depdendencies to your codebase. This isn't necessarily the most technically pure way of doing things. But it's definitely not the worst thing you could do—it's akin to how must people managed Drupal sites before Drupal 8.

<a name="14"></a>

### For security reasons, I need to verify that the code I'm running in production wasn't hacked or modified. How can I do this if I'm using Composer to manage my dependencies?

If you commit all your code to a Git repository (including dependencies), you can easily do a `git diff` on the production codebase to see if any files have been hacked. But if you're constantly using `composer install` to install dependencies, you need to be able to verify that you're getting the right code in two places:

  1. When you or anyone else runs `composer install`.
  2. When the code is deployed to production.

In the first case, you should always make sure you're using `https` endpoints; Composer will validate certificates when communicating with secure channels. If you use `http` repositories, there's no protection against [man-in-the-middle attacks](https://www.owasp.org/index.php/Man-in-the-middle_attack).

To verify your production code, the best solution is to not run composer commands on production. Instead, use a CI tool (like Travis CI, Jenkins, CircleCI, etc.) to build your codebase, then commit your codebase to an artifact repository (or a separate branch on your main repository), then deploy _that_ code to production. That way, you preserve the ability to do a `git diff` on your production codebase.

<a name="15"></a>

### I totally screwed up some of the dependencies on my site while I was tinkering with them. Is there any way to 'nuke' all the things in my codebase that Composer manages so I can do a fresh `composer install` and get them back into the correct state (short of deleting my entire codebase and re-cloning my site locally)?

This can be tricky—with a Drupal site, Composer might be managing code inside `vendor/`, `modules/`, `libraries/`, `profiles/`, `themes/`, and possibly other places too! The best way to 'nuke' all the dependencies Composer downloaded and start fresh with a `composer install` is to run:

    git clean -fdx .

This command tells Git: **f**orce delete all files and **d**irectories in the current directory that aren't being tracked by Git, including files not tracked because of .gitignore (**x**).

Then run `composer install` to get back all the dependencies in their correct state.

<a name="16"></a>

### My team constantly battles with `composer.lock` file merge conflicts. How can we avoid this painful experience?

The two strategies that were discussed at the BoF for avoiding merge conflicts are:

  - Have one dedicated dependency manager on the team—e.g. only one person/role who runs `composer require *`, `composer remove *`, `composer update *` etc. Typically this would be a senior or lead developer who is communicating with the other members of the team and can unblock them.
  - Have one dedicated 'sweeper'—a person whose job it is to deal with merge conflicts.

If push comes to shove, and you _have_ to deal with a merge conflict (or if you're the dedicated conflict resolver), one tip for successfully merging is to accept all the `composer.json` changes, but clear out all the `composer.lock` changes that were conflicting, then run `composer update none` (or `composer update lock`... it's not obvious if there's a difference). This will update the `lock` file based on your current `composer.json` and make sure the file hashes and timestamps are all in sync.

<a name="17"></a>

### Do you have any other tips for making Composer use easier and more delightful?

I'm glad you asked! I was thinking you'd keep asking the hard questions. Here are some of the other miscellaneous Composer tips that were mentioned during the DrupalCon BoF:

  - Don't run Composer in prod! (I think this was mentioned at least five times in the BoF). Instead, either commit `vendor` to codebase, or use CI to commit `vendor` and create a 'deployment artifact' that is deployed to production.
  - Use the [Composer Merge Plugin](https://github.com/wikimedia/composer-merge-plugin) to mix custom module `composer.json` files into one root repository.
  - Don't use `composer create-project drupal/drupal` when setting up Drupal. Use `drupal-composer/drupal-project` instead, as it follows more of the Composer best practices for managing a Drupal 8 codebase.
  - Don't run `composer update` unless you really know what you're doing. Use `composer update [package] --with-dependencies` instead.
  - Commit the `composer.lock` file for individual sites and deployed projects. But _don't_ commit the `.lock` file to contributed modules or modules shared among multiple sites.

## Conclusion

As I alluded to in this post's title, there are still some growing pains as the Drupal community more comprehensively adopts Composer and structured dependency management in general.

One thing that's clear: developers who need to include external libraries and code have a _much_ easier time in Drupal 8 than they did in past versions.

But with that benefit comes some downside: site builders and sysadmins tasked with deploying Drupal 8 securely and efficiently will have to adapt to some new tools and techniques if they want to avoid [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell).
