---
nid: 2827
title: "Drupal VM 4.8 and Drush 9.0.0 - Some major changes"
slug: "drupal-vm-48-and-drush-900-some-major-changes"
date: 2018-01-30T22:34:10+00:00
drupal:
  nid: 2827
  path: /blog/2018/drupal-vm-48-and-drush-900-some-major-changes
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - drush
  - drush 9
  - php
---

> **tl;dr**: [Drupal VM 4.8.0](https://github.com/geerlingguy/drupal-vm/releases/tag/4.8.0) was just released, and it uses Drush 9 and Drush Launcher to usher in a new era of Drush integration!

Drush has been Drupal's stable sidekick for many years; even as Drupal core has seen major architectural changes from versions 4 to 5, 5 to 6, 6 to 7, and 7 to 8, Drush itself has continued to maintain an extremely stable core set of APIs and integrations for pretty much all the time I've been using it.

<p style="text-align: center;"><a href="http://www.drush.org">{{< figure src="./drush-website-homepage.jpg" alt="Drush.org homepage" width="650" height="460" class="insert-image" >}}</a><br><em>New Drush version, new Drush website!</em></p>

But as time has gone on, and the "getting off the island" philosophy has swept across much of the PHP world, Drush has jumped on that train for a major overhaul in Drush 9. It's now based on a number of smaller PHP libraries to provide things like CLI integration, command annotations, etc., and just like Drupal 8, the architecture behind the scenes has changed dramatically, while end-user changes have been (somewhat) minimal. All the old standby's like `drush cr` and `drush site-install` remain and work as well as ever.

But things like using `hook_drush_command()` to register a new Drush command are radically altered—now you create annotated `DrushCommands` (see [Porting Commands to Drush 9](https://weitzman.github.io/blog/port-to-drush9)). And global Drush aliases work a bit differently (I'll get to that soon). And even the way you install Drush for system-wide use is much different—rather than installing a global copy of Drush (e.g. via a .phar file), you now install [Drush Launcher](https://github.com/drush-ops/drush-launcher), and it detects and uses a site-local install of Drush (or a fallback version of Drush if you have one configured).

This blog post isn't about the why's of all the Drush 9 changes; it's an explanation of how this affects Drupal VM, and how your workflow might (or might not!) be impacted by the Drush integration changes happening in Drupal VM 4.8.

## Composer is king

If you haven't already, **it's time to move your Drupal sites over to using Composer** to manage the codebase. There are so many reasons why this is a good idea (or in some cases the _only_ way to get a working Drupal codebase), and one of them is the ease of integrating Drush with your Drupal site. Basically, installing Drush is as easy as `composer require drush/drush`, and then (if you have Drush Launcher installed), you can run `drush [command]` while you're in your project's directory and Drush will 'just work'.

## Drush aliases and Drupal VM

Note that with Drupal VM, how you use Drush is affected by whether you're inside or outside the VM. If you're inside the VM (e.g. `vagrant ssh` or inside the Docker container), then you just use `drush [command]`. If you're outside the VM, you need to use a Drush alias to make sure Drush connects to the VM via SSH, then runs the command correctly inside.

Drupal VM configures Drush aliases for you, for any hosts you have defined in `apache_vhosts` (or `nginx_vhosts` if that's your thing), and as an example, with all the default configuration, there's a global Drush alias `@drupalvm.drupalvm` defined, which you can use outside the VM (in your project folder) like `drush @drupalvm.drupalvm cr`. The aliases are configured similarly inside the VM (so you can use the same alias), but without the SSH connection details.

Drupal VM defines these aliases in new Drush alias YAML files, inside `~/.drush/sites/drupalvm.site.yml`. Note that Drush won't pick up custom global alias files like `drupalvm.site.yml` unless you also configure the new Drush config file to look in global paths. Drupal VM helpfully creates the config file if you don't already have one at `~/.drush/drush.yml`:

```
drush:
  paths:
    alias-path:
      - '${env.home}/.drush/sites'
```

If you always work _inside_ Drupal VM, there aren't many substantial changes you need to worry about. But if you work _outside_, on your host, then you'll have to make a decision on whether you want to stick to Drush 8 or move on to Drush Launcher and 'the new way of using Drush'.

> **Note**: You can disable Drupal VM's alias generation _entirely_ by setting `configure_drush_aliases: false` in your Drupal VM `config.yml`. I recommend you do this if you have more than one site in your VM (e.g. multisite or multiple codebases), or if you have any other specialized use case. Manually managing your Drush aliases is usually the best choice, and the automatic alias generation is more of a convenience to help you get started.

### Sticking with Drush 8 on your host

Currently, if you run `brew install drush` (on a Mac), Homebrew will install a global version of Drush 8.1.15 in your $PATH so when you run `drush` you'll be able to access the full power of Drush locally, whenever and wherever you want. You could also install Drush via Composer globally (`composer global require drush/drush`) and use it the same way, or even download a Drush 8 .phar file locally and run it to use Drush.

If you use Drush 8, Drupal VM still saves the old-style Drush aliases in the global Drush alias path, and everything should still work the same (even if your actual Drupal _project_ you're working on uses Drush 9!).

Sticking with Drush 8 for now might be a safe option for the short term, as small bugs are worked out and Drush 9 gets more stable, but you won't benefit from running the latest and greatest version, or from using Drush Launcher, which enables a few other niceties when using Drush for multiple Drupal projects.

### Using Drush Launcher on your host

Drush Launcher is basically a small wrapper that is triggered when you run `drush`. It looks if you're inside a Drupal project directory, then finds if there's a local version of Drush installed with the project. If so, it uses that version of Drush, configured _for each Drupal project you work on_. If not, it helps you:

```
$ drush
The Drush launcher could not find a Drupal site to operate on. Please do *one* of the following:
  - Navigate to any where within your Drupal project and try again.
  - Add --root=/path/to/drupal so Drush knows where your site is located.
```

I installed Drush Launcher via Homebrew on my Mac: `brew install drush-launcher` (after a `brew uninstall --force drush` to uninstall old Drush versions). See [other Drush Launcher installation options here](https://github.com/drush-ops/drush-launcher#installation---phar).

Now, what if you want the best of _both_ worlds? That is, if you want to use the project-local version and configuration for Drush for any Drupal project that you have Drush installed within, but you _also_ want to fall back to Drush 8.1.15 (or some other version) for any other sites where you might not yet have the codebase set up with Composer?

Drush Launcher has a convenient [fallback option](https://github.com/drush-ops/drush-launcher#fallback) for this. To use it:

  - Install a version of Drush somewhere (e.g. `composer global require drush/drush:~8.0` to install it to `~/.composer/vendor/bin/drush`)
  - Run the `drush` command with `--fallback=~/.composer/vendor/bin/drush`

Before, running `drush` in a directory outside a project root triggers the Drush Launcher and results in the following:

```
$ drush --version
Drush Launcher Version: 0.5.0
The Drush launcher could not find a Drupal site to operate on. Please do *one* of the following:
  - Navigate to any where within your Drupal project and try again.
  - Add --root=/path/to/drupal so Drush knows where your site is located.
```

After, using the fallback version results in the following:

```
$ drush --fallback=~/.composer/vendor/bin/drush --version
Drush Launcher Version: 0.5.0
 Drush Version   :  8.1.15
```

For convenience, instead of passing the `--fallback` option any time you're using Drush outside a Composer-based Drupal project directory, you can set the environment variable `DRUSH_LAUNCHER_FALLBACK`, for example in your `.bash_profile`:

```
export DRUSH_LAUNCHER_FALLBACK=~/.composer/vendor/bin/drush
```

## Drush, y u no make?

Another change that might not be immediately apparent to old-time Drupalists is the [removal of Drush make support in Drush 9](https://github.com/drush-ops/drush/issues/2528). You can no longer run `drush make site.make.yml` to build a Drupal codebase from a Drush make file, unless you stick to Drush 8. Lucky for you, Drush includes built-in support for _converting_ a makefile to a composer.json file: `drush make-convert example.make --format=composer  > composer.json`.

Drupal VM continues to support using Drush make files _for now_ (see updated documentation: [Building your codebase » Using a Drush Make file](http://docs.drupalvm.com/en/latest/deployment/drush-make/)), but Drupal VM's support for Drush make file builds [will be removed](https://github.com/geerlingguy/drupal-vm/issues/1674) at some point in the future. If you use a make file to build your Drupal codebase and want Drupal VM to build it, follow the directions in the documentation to ensure Drush 8 is installed inside Drupal VM instead of the Drush Launcher.

## Drush vs. Drupal Console

Drush and Drupal Console do a lot of the same things (allow CLI interaction with a Drupal site, allow site installation via the command line, aid in Drupal automation, make code generation easier...), and I'm often asked which project someone should use. I often have to answer 'both', because some Drupal contributed modules integrate only with Drush, others integrate only with Console, and yet others ([like Webform](https://twitter.com/jrockowitz/status/957310885059551233)) somehow manage to integrate with both.

There have been faltering efforts in the past to find ways to unify the two tools (e.g. read through [Drupal Console and Drush collaboration efforts](https://drupalconsole.com/articles/drupal-console-and-drush-collaboration-efforts) from April 2016), but it seems the most effective path forward is to collaborate on the underlying PHP libraries and CLI architecture. Both tools now use Symfony Console components at the base, and both support many of the same kind of command structures (though there are small differences between the two). Both tools perform similarly, and both are (IMO) about as easy to set up and integrate into your workflows.

However, Drush has the edge when it comes to name recognition, long-term maintenance history, familiarity, and stability (though we'll have to see if that track record holds through the major changes that come with the Drush 9 rewrite!), and therefore I usually prefer Drush first, Drupal Console second. For someone coming from Laravel, Symfony, or another PHP sub-community, Console may be more immediately familiar, though, and I hold nothing against you if you prefer Console over Drush ✌️.

Drupal VM will continue to support _both_ as `installed_extras` for now (though it's usually better for you to manage Drush and/or Console as dependencies of your Drupal projects via Composer!).

## Further reading

There are a few Drupal VM issues you can follow (or read for a historical overview of the situation) if you want more background on all the above changes:

  - [Upgrade Drupal VM to use Drush Launcher / drush role 3.0.0 version](https://github.com/geerlingguy/drupal-vm/issues/1672)
  - [Drush 9 cannot SSH into DrupalVM](https://github.com/geerlingguy/drupal-vm/issues/1595)
  - [Remove Drush make support](https://github.com/geerlingguy/drupal-vm/issues/1674)

<em>Thanks especially to Moshe Weitzman and Greg Anderson for some help getting Drupal VM's reworked Drush 9 integration working correctly.</em>
