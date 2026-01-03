---
nid: 2839
title: "Drupal, the Fastest - Improving the evaluator experience"
slug: "drupal-fastest-improving-evaluator-experience"
date: 2018-04-13T18:48:43+00:00
drupal:
  nid: 2839
  path: /blog/2018/drupal-fastest-improving-evaluator-experience
  body_format: markdown
  redirects: []
tags:
  - ddev
  - docksal
  - drupal
  - drupal planet
  - drupal vm
  - drupalcon
  - environment
  - lando
  - local development
  - simplytest
---

At DrupalCon Nashville 2018, I became deeply interested in the realm of first-time Drupal experiences, specifically around technical evaluation, and how people would get their feet wet with Drupal. There were two great BoFs related to the topic which I attended, and which I hope will bear some fruits over the next year in making Drupal easier for newcomers:

  - [Improving Drupal's Evaluator experience](https://events.drupal.org/nashville2018/bofs/improving-drupals-evalutator-experience)
  - [An official Drupal local development environment?](https://events.drupal.org/nashville2018/bofs/official-drupal-local-develop-environment)

There are a number of different tools people can use to run a new Drupal installation, but documentation and ease of use for beginners is all over the place. The intention of this project is to highlight the most stable, simple, and popular ways to get a Drupal site installed and running for testing or site building, and measure a few benchmarks to help determine which one(s) might be best for Drupal newcomers.

For reference, here's a spreadsheet I maintain of all the community-maintained [local Drupal development environment tools](https://docs.google.com/spreadsheets/d/11LWo_ks9TUoZIYJW0voXwogawohqAbOFv_dcBlAVs2E/edit?usp=drive_web&ouid=107078709110443510384) I've heard of.

Throughout the week at DrupalCon, I've been adding automated scripts to build new Drupal environments, seeing what makes different development tools like Lando, Drupal VM, Docksal, DDEV, SimplyTest.me, and even _Drupal core_ (using code from the active issue <a href="https://www.drupal.org/project/drupal/issues/2911319">Provide a single command to install and run Drupal</a>) tick. And now I've compiled some benchmark data to help give an overview of what's involved with the different tools, for someone who's never used the tool (or Drupal) before.

> All the code for these benchmarks is available under an open source license in the [Drupal, the Fastest](https://github.com/geerlingguy/drupal-the-fastest) project on GitHub.

## Time to Drupal

One of my favorite metrics is "time to Drupal": basically, how long does it take, at minimum, for someone who just discovered a new tool to install a new Drupal website and have it running (front page accessible via the browser) locally?

{{< figure src="./drupal-evaluator-time-to-drupal.png" alt="Time to Drupal - how long it takes different development environments to go from nothing to running Drupal" width="650" height="283" class="insert-image" >}}

The new `drupal quick-start` command that will be _included with Drupal core_ once [this patch](https://www.drupal.org/project/drupal/issues/2911319) is merged is _by far_ the fastest way to go from "I don't have any local Drupal environment" to "I'm running Drupal and can start playing around with a fresh new site." And being that it's included with Drupal core (and doesn't even require something like Drush to run), I think it will become the most widely used way to quickly test out and even build simple Drupal sites, just because it's easy and fast!

But the `drupal quick-start` environment doesn't have much in the way of extra tools, like an email catching system (to prevent your local environment from accidentally sending emails to people), a debugger (like XDebug), a code profiler (like Blackfire or Tideways), etc. So most people, once they get into more advanced usage, would prefer a more fully-featured local environment.

There's an obvious trend in this graph: Docker-based environments are generally faster to get up and running than a Vagrant-based environment like Drupal VM, mostly because the Docker environments use pre-compiled/pre-installed Docker images, instead of installing and configuring everything (like PHP, MySQL, and the like) inside an empty VirtualBox VM.

Now, 'time to Drupal' isn't the only metric you should care about—there are some good reasons people may choose something like Drupal VM over a Docker-based tool—but it is helpful to know that some tools are more than _twice_ as fast as others when it comes to getting Drupal up and running.

## Required Dependencies

Another important aspect of choosing one of these tools is realizing what you will need to have installed on your Computer to make that tool work. All options require you to have _something_ installed, whether it be just PHP and Composer, or a virtualization environment like VirtualBox or Docker.

{{< figure src="./drupal-evaluator-required-dependencies.png" alt="How many dependencies are required per development environment" width="650" height="290" class="insert-image" >}}

Almost all Drupal local development environment tools are settling on either requiring Docker CE, or requiring Vagrant and VirtualBox. The two exceptions here are:

  1. SimplyTest.me runs in the cloud, so it doesn't require _any_ dependencies locally. But you can't run the site you create in SimplyTest.me locally either, so that's kind of a moot point!
  1. Drupal's `quick-start` command requires PHP and Composer, which in some sense are less heavyweight to install locally (than Docker or VirtualBox)—but in another sense can be a little more brittle (e.g. you can only easily install and one version of PHP at a time—a limitation you can bypass easily by having multiple PHP Docker or VM environments).

Overall, though, the number of required dependencies shouldn't turn you off from any one of these tools, unless there are corporate policies that restrict you from installing certain software on your workstation. Docker, VirtualBox, PHP, Composer, Git and the like are pretty common tools for any developer to have running and updated on their computer.

## Number of setup steps

While the raw number of steps involved in setting up a local environment is not a perfect proxy for _how complex it is to use_, it can be frustrating when it takes many commands just to get a new thing working. Consider, for example, most Node.js projects: you usually `install` or `git clone` a project, then run `npm install`, and `npm start`. The fewer steps involved, the less can go wrong!

{{< figure src="./drupal-evaluator-setup-step-count.png" alt="How many steps are involved in the setup of a Drupal development tool" width="650" height="289" class="insert-image" >}}

The number of individual steps required for each environment varies pretty wildly, and some tools are a little easier to start using than others; whereas Drupal VM relies only on `vagrant`, and doesn't require any custom command line utility or setup to get started, tools like Lando (`lando`), Docksal (`fin`), and DDEV (`ddev`) each require a couple extra steps to first add a CLI helper utility, then to initialize the overall Docker-based environment—_then_ your project runs inside the environment.

In reality, the tradeoff is that since Docker doesn't include as many frills and plugins as something like Vagrant, Docker-based environments usually require some form of wrapper or helper tool to make managing multiple environments easier (setting up DNS, hostnames, http proxy containers and the like).

## Summary

In the end, these particular benchmarks don't paint a perfect picture of why any individual developer should choose one local development environment over another. All the environments tested have their strengths and weaknesses, and it's best to try one or two of the popular tools before you settle on one for your project.

But I'm most excited for the [new `drupal quick-start` command](https://www.drupal.org/project/drupal/issues/2911319) that is going to be in core soon—it will make it a lot faster and easier to do something like clone drupal and test a core patch or new module locally within a minute or two, tops! It's not a feature-filled local development environment, but it's _fast_, it only requires people have PHP (and maybe Composer or Git) installed, and it works great on Mac, Windows (7, 8, or 10!), and Linux.
