---
nid: 2755
title: "Drupal's Contrib floodgates are open, PAReview your projects in Drupal VM!"
slug: "drupals-contrib-floodgates-are-open-pareview-your-projects-drupal-vm"
date: 2017-03-14T19:25:33+00:00
drupal:
  nid: 2755
  path: /blog/2017/drupals-contrib-floodgates-are-open-pareview-your-projects-drupal-vm
  body_format: markdown
  redirects: []
tags:
  - code quality
  - code review
  - community
  - contributions
  - drupal
  - drupal planet
  - drupal vm
  - open source
---

Last week, the proverbial floodgates were opened when Drupal.org finally opened access to any registered user to create a 'full' Drupal.org project (theme, module, or profile). See the [Project Applications Process Revamp](https://www.drupal.org/node/2666584) issue on Drupal.org for more details.

<p style="text-align: center;">{{< figure src="./drupal-org-modules-landing-page.png" alt="Drupal.org modules page" width="650" height="469" class="insert-image" >}}<br>
<em>You can now contribute full Drupal projects even if you're new to the community!</em></p>

Some people weren't comfortable with this change, but it makes onboarding new Drupal contributors more painless and rewarding experience. In the past, when projects got stuck in a Project Application Review hell, it could take months to years before a new Drupal contrib project would be granted access to the exclusive 'full project' club! One of the sad byproducts of that process was the fact that so few contrib themes seem to have been created in the past year or so (compared to the Drupal 6 and 7 release cycle, parts of which still allowed anyone access to full projects).

Whether it's a net benefit for the community or whether there are dragons lurking in this new process, only time will tell. _I_ think it will be a huge boon towards contrib health, especially since full projects are much easier to download, evaluate, test, fix, and work with than sandbox projects—and security coverage is still possible through the existing PAR process. I know that if I had hit tons of roadblocks the first time I tried submitting a theme I just spent many hours building, I would've just given up on submitting any Drupal contrib at that point. Other ecosystems (Wordpress plugins, NPM modules, Packagist libraries, etc.) don't have such a high bar for entry; and they don't offer automatic security support either!

In any case, one of the best things to come out of the entire PAR situation is a neat script/project, [PAReview.sh](https://www.drupal.org/project/pareviewsh), that runs any Drupal module through a gauntlet of tests, checking for code quality, typos, etc. And you can run it on your own modules, easily—whether they're on Drupal.org, GitHub, or locally, on your filesystem!

Traditionally, you had two options for running PAReview.sh on your module:

  1. You could use the extremely handy online [pareview.sh](https://pareview.sh) website to test any publicly-accessible Git project repository. (But this didn't work for local or private projects, or for really quick iterative fixes.)
  2. You could spend some time installing all the script's dependencies as outlined [in the installation docs](https://github.com/klausi/pareviewsh#intallation). (But this can take a while, and assumes you're on Ubuntu — some of the instructions take some time to get right on a Mac or other Linux distros.)

At [Pieter De Clercq](https://github.com/PieterDC)'s suggestion, though, I added out-of-the-box support for PAReview.sh to Drupal VM (see issue: [Feature Idea: PAReview.sh as installed extra](https://github.com/geerlingguy/drupal-vm/issues/1197).

## Enabling PAReview.sh on Drupal VM

The setup is very simple, and works the same on macOS, Linux, or Windows (anywhere Drupal VM runs!):

  1. Download [Drupal VM](https://www.drupalvm.com).
  2. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
  3. Create a `config.yml` file inside the Drupal VM directory, and put in the following contents:

        post_provision_scripts:
          - "../examples/scripts/pareview.sh"
        
        composer_global_packages:
          - { name: hirak/prestissimo, release: '^0.3' }
          - { name: drupal/coder, release: '^8.2' }
        
        nodejs_version: "6.x"
        nodejs_npm_global_packages:
          - name: eslint

  4. Open a Terminal and `cd` into the Drupal VM directory, and run `vagrant up`.

> Note: For an even speedier build (if you're just using Drupal VM to test out a module or three), you can add the following to `config.yml` to make sure only the required dependencies are installed, and to prevent a full Drupal 8 site from being built (if you don't need it):
> 
>     installed_extras: []
>     extra_packages: []
>     drupal_build_composer_project: false
>     drupal_install_site: false
>     configure_drush_aliases: false

A new Drupal VM instance should be built within 5-10 minutes (depending on your computer's speed), with PAReview.sh configured inside.

## Using PAReview.sh on Drupal VM

{{< figure src="./drupal-vm-pareview-sh-honeypot-review.png" alt="Drupal VM pareview.sh script after vagrant ssh" width="650" height="382" class="insert-image" >}}

In the Drupal VM directory (still in the Terminal), run `vagrant ssh` to log into the VM. Then run the `pareview.sh` script on a Drupal.org module just to ensure it's working:

    pareview.sh http://git.drupal.org/project/honeypot.git

This should output some messages, and maybe even a few errors (hey, no maintainer is perfect!), and then drop you back to the command line.

You can also run the script against any local project. If you drop a module named `my_custom_module` into the same directory as the Vagrantfile, you can see it inside the VM in the `/vagrant` folder, so you can run the script against your custom module like so:

    pareview.sh /vagrant/my_custom_module

[See the PAReview.sh documentation](https://github.com/klausi/pareviewsh#usage-running-in-a-shell) for more usage examples and notes, and go make your modules perfect!

## Conclusion

Special thanks to Pieter De Clercq ([PieterDC](https://www.drupal.org/u/pieterdc)) for the inspiration for this new feature, to Klaus Purer ([klausi](https://www.drupal.org/u/klausi)) for the amazing work on PAReview.sh, and also to Patrick Drotleff ([patrickd](https://www.drupal.org/u/patrickd)) for maintaining the free online version.
