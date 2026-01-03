---
nid: 2846
title: "Converting a non-Composer Drupal codebase to use Composer"
slug: "converting-non-composer-drupal-codebase-use-composer"
date: 2018-05-03T14:05:13+00:00
drupal:
  nid: 2846
  path: /blog/2019/converting-non-composer-drupal-codebase-use-composer
  body_format: markdown
  redirects:
    - /blog/2018/converting-non-composer-drupal-codebase-use-composer
aliases:
  - /blog/2018/converting-non-composer-drupal-codebase-use-composer
tags:
  - composer
  - conversion
  - drupal
  - drupal 8
  - drupal planet
  - how-to
  - php
  - tutorial
  - website
---

A question which I see quite often in response to posts like [A modern way to build and develop Drupal 8 sites, using Composer](https://www.jeffgeerling.com/blog/2018/modern-way-build-and-develop-drupal-8-sites-using-composer) is: "I want to start using Composer... but my current Drupal 8 site wasn't built with Composer. Is there an easy way to convert my codebase to use Composer?"

{{< figure src="./composer-convert-drupal-codebase.png" alt="Convert a tarball Drupal codebase to a Composer Drupal codebase" width="650" height="440" class="insert-image" >}}

Unfortunately, the answer to that is a little complicated. The problem is the switch to managing your codebase with Composer is an all-or-nothing affair... there's no middle ground where you can manage a couple modules with Composer, and core with Drush, and something else with manual downloads. (Well, _technically_ this is possible, but it would be immensely painful and error-prone, so don't try it!).

But since this question comes up so often, and since I have a Drupal 8 codebase that I built that _doesn't_ currently use Composer, I thought I'd record the process of converting this codebase from tarball-download-management (where I download core, then drag it into the codebase, download a module, drag it into `modules/`, etc.) to being managed with Composer. This blog post contains the step-by-step guide using the method I recommend (basically, rebuilding your codebase from scratch with modern Composer/Drupal best practices), as well as a video of the process (coming soon - will be on [my YouTube channel](https://www.youtube.com/user/geerlingguy)!).

> **Note**: There are a few tools that attempt to convert your existing Drupal codebase to a Composer-managed codebase (e.g. [composerize-drupal](https://packagist.org/packages/grasmash/composerize-drupal), or Drupal Console's [composerize](https://docs.drupalconsole.com/en/commands/composerize.html) command), but I have found them to be a little more trouble than they are worth. I recommend rebuilding the codebase from scratch, like I do in this guide.

## Getting started - taking an inventory of the codebase

The first thing you need to do is take an inventory of all the stuff that makes up your Drupal codebase. _Hopefully_ the codebase is well-organized and doesn't contain a bunch of random files thrown wily-nily throughout. And hopefully you [didn't hack core or contrib modules](https://www.drupal.org/docs/7/site-building-best-practices/never-hack-core) (though if you do, as long as you did so using patches, you'll be okay—more on that later).

I'm going to work on converting the codebase behind my [Raspberry Pi Dramble](http://www.pidramble.com) website. Admittedly, this is a very small and tidy codebase, but it's a good one to get started with. Here's what it looks like right now:

{{< figure src="./drupal-codebase-before-composer-convert.png" alt="Drupal codebase before Composer conversion" width="650" height="462" class="insert-image" >}}

> **Note**: I use Git to manage my codebase, so any changes I make can be undone if I completely break my site. If you're not using Git or some other VCS to version control your changes... you should make sure you have a backup of the current working codebase—and start using version control!

The most important parts are:

  - Drupal Core
  - Modules (`/modules`): I have one contrib module, `admin_toolbar`
  - Install profiles (`/profiles`): mine is empty
  - Themes (`/themes`): I have one custom theme, `pidramble`

For this particular site, I don't customize the `robots.txt` or `.htaccess` files, though I sometimes do for other sites. So as far as an inventory of my current codebase goes, I have:

  - Drupal Core
  - Admin Toolbar
  - `pidramble` (custom theme)
  - No modifications to core files in the docroot

Now that I know what I'm working with, I'm ready to get started switching to Composer.

## Rebuilding with Composer

I'm about to obliterate my codebase as I know it, but before doing that, I need to temporarily copy out only my _custom_ code and files (in my case, just the `pidramble` theme) into a folder somewhere else on my drive.

Next up, the scariest part of this whole process: delete _everything_ in the codebase. The easiest way to do this, and include invisible files like the .htaccess file, is to use the Terminal/CLI and in the project root directory, run the commands:

```
# First command deletes everything besides the .git directory:
find . -path ./.git -prune -o -exec rm -rf {} \; 2> /dev/null

# Second command stages the changes to your repository:
git add -A

# Third command commits the changes to your repository:
git commit -m "Remove all files and folders in preparation for Composer."
```

At this point, the codebase is looking a little barren:

{{< figure src="./drupal-codebase-empty-pre-convert.png" alt="Drupal codebase is empty before converting to Composer" width="650" height="462" class="insert-image" >}}

Now we need to rebuild it with Composer—and the first step is to set up a new codebase based on the [Composer template for Drupal projects](https://github.com/drupal-composer/drupal-project). Run the following command in your now-empty codebase directory:

```
composer create-project drupal/recommended-project new-drupal-project --no-interaction
```

After a few minutes, that command should complete, and you'll have a fresh new Composer-managed codebase at your disposal, inside the `new-drupal-project` directory! We need to move that codebase into the project root directory and delete the then-empty `new-drupal-project` directory, so run:

```
mv new-drupal-project/* ./
mv new-drupal-project/.* ./
rm -rf new-drupal-project
```

And now you should have a Drupal project codebase that looks like this:

{{< figure src="./drupal-codebase-new-drupal-composer-template.png" alt="Drupal codebase after building a new Composer Template for Drupal" width="650" height="462" class="insert-image" >}}

But wait! The old codebase had Drupal's docroot in the project root directory... where did my Drupal docroot go? The Composer template for Drupal projects places the Drupal docroot in a _subdirectory_ of the project instead of the project root—in this case, a `web/` subdirectory:

{{< figure src="./drupal-codebase-composer-template-web-subdirectory.png" alt="Drupal codebase - web docroot subdirectory from Composer Template" width="650" height="462" class="insert-image" >}}

> **Note**: You might also see a `vendor/` directory, and maybe some other directories; note that those are installed locally but won't be committed to your Git codebase—at least not by default. I'll mention a few different implications of how this works later!

There are a few good reasons for putting Drupal's actual docroot in a subdirectory:

  1. You can store other files besides the Drupal codebase in your project repository, and they won't be in a public web directory where anyone can access them by default.
  2. Composer can manage dependencies outside of the docroot, which is useful for development and ops tools (e.g. Drush), or for files which shouldn't generally be served in a public web directory.
  3. Your project can be organized a little better (e.g. you can just have a project-specific README and a few scaffold directories in the project root, instead of a ton of random-looking Drupal core files like `index.php`, `CHANGELOG.txt`, etc. which have nothing to do with your specific Drupal project).

Now that we have the base Composer project set up, it's time to add in all the things that make our site work. Before doing that, though, you should commit all the core files and Drupal project scaffolding that was just created:

```
git add -A
git commit -m "Recreate project from Composer template for Drupal projects."
```

### Adding contrib modules, themes, and profiles

For each contributed module, theme, or install profile your site uses, you need to `require` it using Composer to get it added to your codebase. For example, since I only use one contributed module, I run the following command:

```
composer require drupal/admin_toolbar:~1.0
```

Parsing this out, we are telling Composer to `require` (basically, add to our project) the `admin_toolbar` project, from the Drupal.org packagist repository. If you look on Drupal.org at the [Admin Toolbar](https://www.drupal.org/project/admin_toolbar) project page, you'll notice the latest version is something like `8.x-1.23`... so where's this weird `~1.0` version coming from? Well, Drupal's packagist repository translates versions from the traditional Drupal style (e.g. 8.x-1.0) to a Composer-compatible style. And we want the latest stable version in the 1.x series of releases, so we say `~1.0`, which tells Composer to grab whatever is the latest 1.x release. If you visit a project's release page on Drupal.org (e.g. [Admin Toolbar 8.x-1.23](https://www.drupal.org/project/admin_toolbar/releases/8.x-1.23)), there's even a handy command you can copy out to get the latest version of the module (see the 'Install with Composer' section under the download links):

{{< figure src="./install-with-composer-link-drupal-org-project-release-page.png" alt="Install with Composer on Drupal.org project release page" width="650" height="330" class="insert-image" >}}

You could also specify a specific version of a module (if you're not running the latest version currently) using `composer require drupal/admin_toolbar:1.22`. It's preferred to _not_ require specific versions of modules... but if you're used to using Drupal's update manager and upgrading one module at a time to a specific newer version, you can still work that way if you need to. But Composer makes it easier to manage updating modules without even having to use Drupal's update manager, so I opt to use a more generic version like `~1.0`.

> **Note**: If you look in the docroot after adding a contrib module, you might notice the module is now inside `modules/contrib/admin_toolbar`. In my original codebase, the module was located in the path `modules/admin_toolbar`. When you move a module to another directory like this, you need to make sure you clear all caches on your Drupal site after deploying the change, _and_ either restart your webserver or manually flush your PHP opcache/APC (otherwise there could be weird errors when PHP looks in the wrong directory for module files!).

After you run a `composer require` for each contrib project (you can also run `composer require drupal/project_one drupal/project_two etc.` if you want to add them all in one go), it's time to commit all the contrib projects to your codebase (`git add -A`, then `git commit -m "Add contrib projects to codebase."`), then move on to restoring custom modules, themes, and profiles (if you have any).

### Adding custom modules, themes, and profiles

Following the convention of having 'contrib' modules/themes/profiles in a special 'contrib' subdirectory, a lot of people (myself included) use the convention of placing all custom projects into a 'custom' subdirectory.

I have a custom theme, `pidramble`, so I created a `custom` directory inside `themes/`, and placed the `pidramble` theme directory inside there:

{{< figure src="./drupal-composer-project-pidramble-themes-custom-directory.png" alt="Drupal codebase - pidramble theme inside custom themes subdirectory" width="650" height="462" class="insert-image" >}}

For any of your custom code:

  - Place modules in `web/modules/custom/`
  - Place themes in `web/themes/custom/`
  - Place profiles in `web/profiles/custom/`

> **Note**: If you use Drupal's multisite capabilities (where you have one codebase but many websites running off of it), then site-specific custom modules, themes, and profiles can also be placed inside site-specific folders (e.g. inside `web/sites/[sitename]/modules/custom`).

### Adding libraries

Libraries are a little different, especially since right now there are a few different ways people manage third party libraries (e.g. Javascript libraries) in Drupal 8. It seems most people have settled on using [Asset Packagist](https://asset-packagist.org) to bundle up npm dependencies, but there is still active work in the Drupal community to standardize third party library management in this still-nascent world of managing Drupal sites with Composer.

If you have a bunch of libraries you need to add to your codebase, please read through these issues for some ideas for how to work with Asset Packagist:

  - [Add asset-packagist repository to Composer template for Drupal Projects](https://github.com/drupal-composer/drupal-project/pull/286)
  - [Drupal core should help make 3rd party library management not torturous](https://www.drupal.org/project/drupal/issues/2873160)
  - [Best practices for handling external libraries in Drupal 8](https://www.drupal.org/project/documentation/issues/2605130)

### Adding customizations to .htaccess, robots.txt, etc.

You might need to customize certain files that are included with Drupal core for your site—like adding exclusions to `robots.txt` or adding a redirection to `.htaccess`. If so, make sure you make those changes and commit them to your git repository. The Composer template project [recommends](https://github.com/drupal-composer/drupal-project/blob/8.x/README.md#updating-drupal-core) you do a `git diff` on any customized files any time you update Drupal core.

> **Note**: There are [more advanced ways](https://blt.readthedocs.io/en/latest/template/patches/README/#gotchas) of managing changes to these 'scaffold' files if you want take out the human review part from Drupal core updates, but they require a bit more work to make them run smoothly, or may require you to manually apply changes to your customized files whenever Drupal core updates those files in a new release.

### Adding patches to core and contrib projects

One of the best things about using the Composer template project is that it automatically sets up the [composer-patches](https://github.com/cweagans/composer-patches) project, which allows you to [apply patches directly to Drupal core and contrib projects](https://github.com/drupal-composer/drupal-project#how-can-i-apply-patches-to-downloaded-modules). This is a little more of an advanced topic, and most sites I use don't need this feature, but it's very nice to have when you _do_ need it!

## Add a local development environment

While you're revamping your codebase, why not also revamp your local development process, and add a local environment for easy testing and development of your code? In my blog post [A modern way to build and develop Drupal 8 sites, using Composer](https://www.jeffgeerling.com/blog/2018/modern-way-build-and-develop-drupal-8-sites-using-composer), I showed how easy it is to get your codebase up and running with Drupal VM's Docker container:

```
composer require --dev geerlingguy/drupal-vm-docker
docker-compose up -d
```

Then visit [http://localhost/](http://localhost/) in your browser, and you can install a new Drupal site locally using your codebase (or you can connect to the Docker container's MySQL instance and import a database from your production site for local testing—always a good idea to validate locally before you push a major change like this to production!).

{{< figure src="./drupal-vm-docker-composer-site-rebuild-local-environment.jpg" alt="Drupal VM Docker container running a new Drupal Composer template project" width="650" height="422" class="insert-image" >}}

> **Note**: The quickest way to import a production database locally with this setup is to do the following:
> 
> 1. Drop a .sql dump file into the project root (e.g. `sql-dump.sql`).
> 2. Import the database: `docker exec drupal_vm_docker bash -c "mysql drupal < /var/www/drupalvm/drupal/sql-dump.sql"`
> 3. Clear caches: `docker exec drupal_vm_docker bash -c "drush --root=/var/www/drupalvm/drupal/web cr`

## Deploying the new codebase

One major change—at least in my Raspberry Pi Dramble codebase—is the transition from having the Drupal docroot be in the project root to having the docroot be in the `web/` subdirectory. If I were to `git push` this to my production web server (which happens to be a little Raspberry Pi on my desk, in this case!), then the site would break because docroot is in a new location.

So the first step is to make sure your webserver knows to look in `project-old-location/web` for the docroot in your Apache, Nginx, etc. configuration. In my case, I updated the docroot in my Apache configuration, switching it from `/var/www/drupal` to `/var/www/drupal/web`.

Then, to deploy to production:

  1. Take a backup of your site's database and codebase (it never hurts, especially if you're about to make a major change like this!)
  2. Stop Apache/Nginx (whatever your server is running) so no web traffic is served during this docroot transition.
  3. Deploy the updated code (I used git, so did a `git pull` on my production web server).
  4. Run `composer install --no-dev` inside the project root, so the production server has all the right code in all the right places (`--no-dev` means 'don't install development tools that aren't needed in production').
  5. Start Apache or Nginx so it starts serving up the new docroot subdirectory.

One more caveat: Since you moved the docroot to a new directory, the public `files` directory might need to also be moved and/or have permissions changed so things like CSS and JS aggregation work correctly. If this is the case, make sure the `sites/default/files` directory has the correct file ownership and permissions (usually something like `www-data` and `775`), and if your `git pull` wiped out the existing files directory, make sure your restore the rest of the contents from the backup you took in step 1!

> **Note**: There are many reasons _not_ to run `composer install` on your production server—and in some cases, it might not even work! It's _best_ to 'build' your codebase for production separately, on a CI server or using a service like Circle CI, Travis CI, etc., then to deploy the built codebase to the server... but this requires another set of infrastructure management and deployment processes, so for most of my smaller projects I just have one Git codebase I pull from and run `composer install` on the production web server.
> 
> Another option is to commit _everything_ to your codebase, including your `vendor` directory, the `web/core` directory, all the contrib modules, etc. This isn't ideal, but it works and might be a better option if you can't get `composer install` working in production for one reason or another.

## Managing everything with Composer

One of the main drivers for this blog post was the questions Matthew Grasmick and I got after our session at DrupalCon Nashville 2018, [How to build a Drupal site with Composer AND keep all of your hair](https://events.drupal.org/nashville2018/sessions/how-build-drupal-site-composer-and-keep-all-your-hair). Even before then, though, I have regularly heard from people who are _interested_ in starting to use Composer, but have no clue where to start, since their current codebase is managed via tarball, or via Drush.

And this is an especially pressing issue for those using Drush, since Drush 9 doesn't even support downloading Drupal or contributed projects anymore—from the [Drush 9 documentation](http://docs.drush.org/en/master/install/):

> Drush 9 only supports one install method. It requires that your Drupal 8 site be built with Composer and Drush be listed as a dependency.

So while you _can_ continue managing your codebase using the tarball-download method for the foreseeable future, I would highly recommend you consider moving your codebase to Composer, since a lot of the tooling, tutorials, and the rest of the Drupal ecosystem is already in the middle of a move in that direction. There are growing pains, to be sure, but there are also a lot of benefits, many of which are identified in the [DrupalCon Nashville presentation](https://events.drupal.org/nashville2018/sessions/how-build-drupal-site-composer-and-keep-all-your-hair) I mentioned earlier.

Finally, once you are using Composer, make sure you _always_ run `composer install` after updating your codebase (whether it's a `git pull` on a production server, or even on your workstation when doing local development!
