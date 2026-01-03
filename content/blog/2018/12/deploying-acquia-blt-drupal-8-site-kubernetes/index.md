---
nid: 2897
title: "Deploying an Acquia BLT Drupal 8 site to Kubernetes"
slug: "deploying-acquia-blt-drupal-8-site-kubernetes"
date: 2018-12-19T22:28:41+00:00
drupal:
  nid: 2897
  path: /blog/2018/deploying-acquia-blt-drupal-8-site-kubernetes
  body_format: markdown
  redirects: []
tags:
  - acquia
  - blt
  - docker
  - drupal
  - drupal 8
  - drupal planet
  - kubernetes
---

{{< figure src="./blt-to-kubernetes-drupal.png" alt="BLT to Kubernetes" width="249" height="76" class="insert-image" >}}

Wait... what? If you're reading the title of this post, and are familiar with [Acquia BLT](https://blt.readthedocs.io/), you might be wondering:

  - Why are you using Acquia BLT with a project that's not running in Acquia Cloud?
  - You can deploy a project built with Acquia BLT to Kubernetes?
  - Don't you, like, have to use Docker instead of Drupal VM? And aren't you [Jeff Geerling] the maintainer of Drupal VM?

Well, the answers are pretty simple:

  - Acquia BLT is not just for Acquia Cloud sites; it is a great way to kickstart and supercharge any large-scale Drupal 8 site. It has built-in testing integration with PHPUnit and Behat. It has default configurations and packages to help make complex Drupal sites easier to maintain and deploy. And it's not directly tied to Acquia Cloud, so you can use it with any kind of hosting!
  - Yes, Acquia BLT is a great tool to use for building and deploying Drupal to Kubernetes!
  - Why, yes! And while I use, maintain, and love Drupal VM—even for this particular project, for the main local dev environment—it is just not economical to deploy and maintain a highly-scalable production environment using something like Drupal VM... not to mention it would make Kubernetes barf!

Anyways, I figured I'd jump right in and document how I'm doing this, and not get too deep into the whys.

## Generating a build artifact using only Docker

The first problem: BLT has built-in tooling to deploy new code to environments in traditional cloud environments, in a separate Git repository. This works great for hosting in Acquia Cloud, Pantheon, or other similar environments, but if you need to deploy your BLT site into a container-only environment like Kubernetes, you need to generate a BLT deployment artifact, then get that into a deployable Docker container.

Along that theme, my first goal was to make it so I could build the deployment artifact in a perfectly clean environment—no PHP, no Composer, no Node.js, no _nothing_ except for Docker. So I built a shell script that does the following:

  1. Starts a build container (uses the [PHP 7.2 CLI Docker image](https://hub.docker.com/_/php/) from Docker Hub).
  2. Installs the required dependencies for PHP.
  3. Installs Node.js.
  4. Installs Composer.
  5. Runs `blt artifact:build` to build a deployment artifact in the `deploy/` directory.
  6. Deletes the build container.

Here's the script:

<script src="https://gist.github.com/geerlingguy/85b816ed7aff378ea2700b82ebde81c8.js"></script>

All you need is to be in a BLT project directory, and run `./blt-artifactory`. Now, I could optimize this build process further by building my own image which already has everything set up so I can just run `blt artifact:build`, but for now I'm a little lazy and don't want to maintain that. Maybe I will at some point. That would cut out 3-5 minutes from the build process.

## Building a Docker container with the build artifact

So after we have a deployment artifact in the `deploy/` directory, we need to stick that into a Docker container and then push that container into a Docker registry so we can use it as the `Image` in a Kubernetes Deployment for Drupal.

Here's the Dockerfile I am using to do that:

<script src="https://gist.github.com/geerlingguy/5998fe7cd13520498df0578b9ba366ea.js"></script>

I put that Dockerfile into my BLT project root, and run `docker build -t my/site-name .` to build the Docker image. Note that this Dockerfile is meant to build from a PHP container image which already has all the required PHP extensions for your project. In my case, I have a preconfigured PHP base image (based off `php:7.2-apache-stretch`) which installs extensions like `gd`, `pdo_mysql`, `simplexml`, `zip`, `opcache`, etc.

Once I have the `my/site-name` image, I tag it appropriately and—in this case—push it up to a repository I have set up in [AWS ECR](https://aws.amazon.com/ecr/). It's best to have a private Docker registry running somewhere for your projects, because you wouldn't want to push your site's production Docker image to a public registry like Docker Hub!

## Running Drupal in Kubernetes

Now that I have a Docker image available in AWS ECR, and assuming I have a Kubernetes cluster running inside AWS EKS (though you could be using any kind of Kubernetes cluster—you'd just have to configure it to be able to pull images from whatever private Docker registry you're using), I can create a set of namespaced manifests in Kubernetes for my Drupal 8 site.

For this site, it doesn't need anything fancy—no Solr, no Redis or Memcached, no Varnish—it just needs a horizontally-scalable Drupal deployment, a MySQL deployment, and ingress so people can reach it from the Internet.

Unfortunately for this blog post, I will not dive into the details of the process of getting this _particular_ site running inside Kubernetes, but the process and Kubernetes manifests used for doing so is extremely similar to the ones I am building and maintaining for my [Raspberry Pi Dramble](http://www.pidramble.com) project. _What's that?_, you ask? Well, it's a cluster of Raspberry Pis running Drupal on top of Kubernetes!

If you want to find out more about _that_, please attend my session at DrupalCon Seattle in April 2019, [Everything I know about Kubernetes I learned from a cluster of Raspberry Pis](https://events.drupal.org/seattle2019/sessions/everything-i-know-about-kubernetes-i-learned-cluster-raspberry-pis) (or view the video/slides after the fact).
