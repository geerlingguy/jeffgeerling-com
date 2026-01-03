---
nid: 2929
title: "A Drupal Operator for Kubernetes with the Ansible Operator SDK"
slug: "drupal-operator-kubernetes-ansible-operator-sdk"
date: 2019-08-09T15:20:05+00:00
drupal:
  nid: 2929
  path: /blog/2019/drupal-operator-kubernetes-ansible-operator-sdk
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible for kubernetes
  - drupal
  - drupal planet
  - k8s
  - kubernetes
  - operator
---

Kubernetes is taking over the world of infrastructure management, at least for larger-scale operations, and best practices have started to solidify. One of those best practices is the cultivation of [Custom Resource Definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (CRDs) to describe your applications in a Kubernetes-native way, and [Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) to manage your the Custom Resources running on your Kubernetes clusters.

In the Drupal community, Kubernetes uptake has been somewhat slow, but is on the rise. Just like with Docker adoption for local development, the tooling and documentation has been slowly percolating. For example, [Tess Flynn from TEN7](https://ten7.com/blog/post/episode-062-2019-flyover-camp-tess-flynn) has been <s>boldly going where no one has gone before</s> (oops, wrong scifi series!) using the Force to promote Drupal usage in a Kubernetes environment.

I've also moved my [Raspberry Pi Dramble](https://www.pidramble.com) (a cluster of Raspberry Pi computers running a Drupal 8 site) from a standard LAMP stack cluster to Kubernetes, and I've been blogging about that journey here and there, even taking the Dramble on a tour, presenting [Everything I know about Kubernetes I learned from a cluster of Raspberry Pis](https://www.youtube.com/watch?v=QbdLO-IKFzc).

But so far, all the Drupal organizations using Kubernetes are 'out there', doing their own thing, often using a more traditional approach to the management of Drupal containers in a Kubernetes cluster.

In mid-2018, after some informal meetings at DrupalCon and between various interested parties online, a few of the kind folks at Drud Technologies (behind DDEV) helped form the [sig-drupal Drupal on Kubernetes Special Interest Group](https://github.com/drud/sig-drupal). We sometimes chat in the #kubernetes in the [Drupal Slack](https://www.drupal.org/slack), and there are biweekly meetings on Wednesdays.

One of the things that a few different members of the community have been working on (mostly informally, for now) is a Drupal Operator for Kubernetes.

## I'm Jeff, I'll be your operator

{{< figure src="./tank-operator-matrix.jpg" alt="Tank being the operator in the Matrix" width="650" height="275" class="insert-image" >}}

First, even if you've been using Kubernetes for a while, you might not know much about Operators. You might use one to manage something that you copied and pasted into your cluster for logging, metrics, or a service mesh component, but what _is_ an Operator, and why would you be interested in making your _own_?

And, to me, the million dollar question is: will you need to know Go to write an Operator? After all, most things in the Kubernetes ecosystem seem to be Go-based...

Well, first, an Operator is a Kubernetes 'controller' that watches over specific Custom Resources (which follow your Custom Resource Definition), and makes sure the Custom Resources are configured and running as they should be, based on the Custom Resource `metadata` and `spec`.

So if you want a widget with a fizz equal to buzz:

```
     ---
     apiVersion: widget.example.com/v1alpha1
     kind: Widget
     metadata:
       name: my-special-widget
     spec:
       fizz: buzz
```

Then it is the responsibility of the _operator_ to make it so. It could do that in a variety of ways. You could write some Go to interact with the Kubernetes API and run the proper containers with the proper configuration (be that a ConfigMap with a Deployment, or a StatefulSet, or whatever it needs to be).

So your Operator might say "ah, the `fizz` for `my-special-widget` is currently set to `foo`, but it should be `buzz`. Now I will change that `foo` to a `buzz`, update my application's database schema to reflect the change, and notify some external service of the `fizz` change."

Once the change is made, the Operator goes back into its ever-watchful state, waiting for another change, and also ensuring the Custom Resource it's watching is running as it should be (with the help of the Kubernetes API).

When you _delete_ the Custom Resource, the Operator can even take a final backup of your special widget, and maybe notify an external service that your special widget is no longer very special.

### Ansible Operator SDK

There are a number of different ways you can build and maintain Operators; many of them require you (and anyone you ever want to help maintain the operator) to program in Go. Go is a great programming language, and it's not very hard to learn. But it is usually not the same programming language you use for the applications you regularly develop, so it would be nice to have an alternative option besides learning an entire new programming language.

That's where [Ansible Operator SDK](https://github.com/operator-framework/operator-sdk/blob/master/doc/ansible/user-guide.md) comes in! (See also: the full [developer guide](https://github.com/operator-framework/operator-sdk/blob/master/doc/ansible/dev/developer_guide.md).)

Ansible has had great support for managing Kubernetes cluster resources for some time, mostly via its `k8s` and `k8s_facts` modules. For example, in an Ansible playbook, you can add or modify a Kubernetes resource with the following:

```
---
- name: Create a Service object from an inline definition
  k8s:
    state: present
    definition:
      apiVersion: v1
      kind: Service
      metadata:
        name: mysite
        namespace: mysite
        labels:
          app: mysite
          service: drupal
      spec:
        selector:
          app: mysite
          service: drupal
        ports:
        - protocol: TCP
          targetPort: 80
          name: port-80-tcp
          port: 80
```

You can also use powerful Jinja2 templating and Ansible variables along with separate Kubernetes YAML files to manage cluster resources. And Ansible can go much further, because you have thousands of other modules which can be used to integrate external services (e.g. you can have the same Ansible operator playbook [manage an external AWS RDS/Aurora database cluster](https://docs.ansible.com/ansible/latest/modules/rds_module.html), [interact with a chat client like Slack](https://docs.ansible.com/ansible/latest/modules/slack_module.html), and [update your website monitoring service](https://docs.ansible.com/ansible/latest/modules/pingdom_module.html), all with very easy-to-define syntax.

## Drupal Operator, built with the Operator SDK

To explore how Ansible Operator SDK can make managing a Drupal Operator easy, I forked Thom Toogood's [original PoC Drupal Operator](https://github.com/thom8/drupal-operator), then rebuilt it with the latest version of the Operator SDK. My fork of the [Drupal Operator](https://github.com/geerlingguy/drupal-operator) is currently structured to run a Drupal site with a codebase like the one in the [official Docker library image for Drupal](https://hub.docker.com/_/drupal/), but that is subject to change, because the way that image is built is not (IMHO) the way you should build a modern best-practices Drupal site codebase (for more on that, see my [Drupal for Kubernetes](https://github.com/geerlingguy/drupal-for-kubernetes) project!).

If you have a Kubernetes cluster running (you can get one quickly by [Installing minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) and running `minikube start`), it's easy to get started:

  1. Deploy Drupal Operator into your cluster:

         kubectl apply -f https://raw.githubusercontent.com/geerlingguy/drupal-operator/master/deploy/drupal-operator.yaml

  2. Create a file named `my-drupal-site.yml` with the following contents:

         ---
         apiVersion: drupal.drupal.org/v1alpha1
         kind: Drupal
         metadata:
           name: my-drupal-site
           namespace: default
         spec:
           drupal_image: 'drupal:8.7-apache'
           # You should generate your own hash salt, e.g. `Crypt::randomBytesBase64(55)`.
           drupal_hash_salt: 'provide hash_salt here'
           drupal_trusted_host_patterns: 'provide trusted_host_patterns here'
           files_pvc_size: 1Gi
           manage_database: true
           database_image: mariadb:10
           database_pvc_size: 1Gi

  3. Use `kubectl` to create the site in your cluster:

         kubectl apply -f my-drupal-site.yml

You should now have a Drupal site running inside the cluster, accessible via a `NodePort` on any of your Kubernetes servers' IP address (use `kubectl get service my-drupal-site` to see details). In the future, this Drupal Operator will also [support Ingress](https://github.com/geerlingguy/drupal-operator/issues/8) (instead of access via NodePort), among many other features.

Since the Operator uses a Persistent Volume (PV) for the Database and Drupal files directory, you can upgrade container image versions (to run the latest version of Drupal core) without losing your Drupal site data. Currently, upgrading the site or performing other types of site maintenance is done manually via the web interface (e.g. via /update.php), but eventually the Operator will [manage many site maintenance tasks automatically via Drush](https://github.com/geerlingguy/drupal-operator/issues/6).

### Building your own Operator

This Drupal Operator is still a 'proof of concept', and will likely see many changes over the next year or two before it is more of a stable solution for running your sites in production.

But that doesn't mean you shouldn't start building your _own_ Operators to manage your Kubernetes resources right now! You can build your own operator quickly and easily with the Operator SDK and ansible-operator following the [Operator SDK Quick Start](https://github.com/operator-framework/operator-sdk#quick-start) guide. My directions assume you're using a Mac:

  1. [Install Operator SDK CLI](https://github.com/operator-framework/operator-sdk/blob/master/doc/user/install-operator-sdk.md): `brew install operator-sdk`
  1. Activate Go's module mode: `export GO111MODULE=on`
  1. Create the new Operator: `operator-sdk new my-app --api-version=myapp.example.com/v1alpha1 --kind=MyApp --type=ansible`
  1. Change into the Operator directory and try testing the basic components using Molecule:
     1. `pip install docker molecule openshift` (if you don't already have these installed)
     1. `molecule test -s test-local`
  1. Those tests should pass, and at this point you have a barebones, but working, Operator.

> Note: If you want to be able to create MyApp instances in any namespace in your cluster, you should make sure the Operator is cluster-scoped (see the [Operator scope](https://github.com/operator-framework/operator-sdk/blob/master/doc/operator-scope.md) documentation). Otherwise the Operator can only be deployed and used in one particular namespace at a time. This could be desirable in some scenarios.

At this point, I would commit all the files to a newly-initialized Git repository for the Operator project (`git init && git add -A && git commit -m "Initial commit."`), then start working on making the Operator do exactly what I want.

I plan on writing more on Operators and Kubernetes cluster management in my upcoming book, [Ansible for Kubernetes](https://www.ansibleforkubernetes.com). You can [sign up to be notified](https://leanpub.com/ansible-for-kubernetes) when the book is released on LeanPub.
