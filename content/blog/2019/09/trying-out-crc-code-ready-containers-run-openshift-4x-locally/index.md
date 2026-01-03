---
nid: 2935
title: "Trying out CRC (Code Ready Containers) to run OpenShift 4.x locally"
slug: "trying-out-crc-code-ready-containers-run-openshift-4x-locally"
date: 2019-09-05T20:34:43+00:00
drupal:
  nid: 2935
  path: /blog/2019/trying-out-crc-code-ready-containers-run-openshift-4x-locally
  body_format: markdown
  redirects: []
tags:
  - crc
  - hyperkit
  - k8s
  - kubernetes
  - mac
  - openshift
  - redhat
---

I've been working a bit with Red Hat lately, and one of the products that has intrigued me is their OpenShift Kubernetes platform; it's kind of like Kubernetes, but made to be more palatable and UI-driven... at least that's my initial take after taking it for a spin both using [Minishift](https://github.com/minishift/minishift) (which works with OpenShift 3.x), and [CRC](https://github.com/code-ready/crc) (which works with OpenShift 4.x).

Because it took me a bit of time to figure out a few details in testing things with OpenShift 4.1 and CRC, I thought I'd write up a blog post detailing my learning process. It might help someone else who wants to get things going locally!

## CRC System Requirements

First things first, you need a decent workstation to run OpenShift 4. The minimum requirements are 4 vCPUs, 8 GB RAM, and 35 GB disk space. And even with that, I constantly saw HyperKit (the VM backend CRC uses) consuming 100-200% CPU and 12+ GB of RAM (sheesh!).

## Installing CRC

Before you can use CRC, you must have a Red Hat Developer account. Sign up on the [Red Hat Developers Registration site](https://developers.redhat.com/register). You can then visit the [CRC install page on cloud.redhat.com](https://cloud.redhat.com/openshift/install/crc/installer-provisioned) to view the [CRC Getting Started Guide](https://code-ready.github.io/crc/), download the platform-specific `crc` binary, and copy your 'pull secret' (which is required during setup).

After you download the `crc` binary and place it somewhere in your `$PATH`, you have to run the following commands:

    $ crc setup
    $ crc start

`crc setup` creates a `~/.crc` directory, and `crc start` will prompt you for your pull secret (which you _must_ get from your account on cloud.redhat.com at the bottom of the [CRC Installer page](https://cloud.redhat.com/openshift/install/crc/installer-provisioned).

Note that during `crc setup`, I had a big scary warning pop up on my Mac about the binary code signature being changed (this is from a malware detection system built into Little Snitch):

{{< figure src="./crc-has-been-modified-terminal.png" alt="CRC has been modified terminal warning" width="650" height="297" class="insert-image" >}}

I clicked 'Accept Modification', as the modification is part of CRC's install process... but hopefully that's something that could be avoided in future versions of CRC!

After a few minutes, `crc start` prints out some cluster information, like:

```
INFO Starting OpenShift cluster ... [waiting 3m]
INFO To access the cluster using 'oc', run 'eval $(crc oc-env) && oc login -u kubeadmin -p [redacted] https://api.crc.testing:6443'
INFO Access the OpenShift web-console here: https://console-openshift-console.apps-crc.testing
INFO Login to the console with user: kubeadmin, password: [redacted]
CodeReady Containers instance is running
```

If you open the web console ([https://console-openshift-console.apps-crc.testing](https://console-openshift-console.apps-crc.testing)), you'll need to accept the self-signed certificate... then you'll be redirected to another local URL, and you'll need to accept _another_ self-signed certificate. But once that's done you should arrive at a login screen:

{{< figure src="./crc-cluster-login-resized.png" alt="CRC Login screen" width="650" height="458" class="insert-image" >}}

Click on the `kube:admin` option, then log in using the credentials output by `crc start`. Note that if you get an error the first time you click on the `kube:admin` option, try again in a minute or two; the cluster still might be initializing.

Now you should arrive at the OpenShift dashboard:

{{< figure src="./openshift-crc-dashboard-projects-list.png" alt="CRC OpenShift dashboard project list" width="650" height="458" class="insert-image" >}}

## Running an application on OpenShift locally

One nice thing about OpenShift is that you can manage most everything via the UI, if you desire (assuming the user you are logged in as has the RBAC rights to do so); you can also inspect all the raw resources (either in OpenShift's layout or as YAML in an in-browser editor) pretty easily.

Since I fancy myself a PHP developer, I decided to deploy an example CakePHP application (never used CakePHP before, though):

  1. I created a project with name `php-test` and display name 'PHP Test'.
  1. On the Project Status page, I chose to browse the application catalog to find something to deploy.
  1. I scrolled down to PHP, clicked it, and chose 'Create Application'.
  1. I named it `php-test`, left all the defaults (except for checking the 'create route' checkbox to create a public URL), and clicked the 'Try Sample' button to test out the example repo (which happens to be a [demo CakePHP app](https://github.com/sclorg/cakephp-ex.git)).
  1. I waited

With this application, it requires some time to pull the base image, run a container to pull the source, run another container to build the project (using PHP's package manager, Composer), and finally run the final container so the PHP test Pod is ready to start responding to HTTP requests.

You can monitor the progress of the build by clicking on the DeploymentConfig (DC) 'php-test', and then inspecting the 'Resources':

{{< figure src="./project-status-php-test-crc-openshift.png" alt="CRC Openshift project application resource build progress monitoring" width="650" height="458" class="insert-image" >}}

It took a few minutes for the build process to complete (there's a lot to download, apparently!), but once that was done, I could visit http://php-test-php-test.apps-crc.testing/ and see the running application:

{{< figure src="./crc-openshift-cakephp-demo-application.png" alt="CRC OpenShift demo CakePHP application" width="650" height="458" class="insert-image" >}}

It's interesting, I've never seen 'Routes' in K8s nomenclature (I'm used to 'Ingress'), but it seems to be about the same, just with some extra decoration for some OpenShift-specific features. I could also manually add a Kubernetes Ingress resource that allowed me to direct a domain (e.g. `http://php.test/`) to the php-test service running in the `php-test` namespace.

## Managing the cluster

After you're finished, you can run `crc stop` to stop the cluster, and `crc delete` to completely delete it. `crc start` then generates a new cluster (or restarts a stopped cluster).

## Getting the CRC VM IP address

I wanted to get the IP address of the HyperKit VM, too, so I could access exposed services (either by NodePort or Ingress via DNS), and there are three quick ways to do that:

  1. In the OpenShift UI, go to Compute > Nodes, and look at the 'Internal IP' under 'Node Addresses'.
  1. Run `crc ip`.
  1. Ping the console URL (e.g. `ping console-openshift-console.apps-crc.testing`).
