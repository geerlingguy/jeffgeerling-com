---
nid: 2967
title: "The Kubernetes Collection for Ansible"
slug: "kubernetes-collection-ansible"
date: 2020-02-18T15:15:06+00:00
drupal:
  nid: 2967
  path: /blog/2020/kubernetes-collection-ansible
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible-test
  - community
  - github
  - k8s
  - kubernetes
  - molecule
  - open source
---

> **October 2020 Update**: This post still contains relevant information, but one update: the `community.kubernetes` collection is moving to `kubernetes.core`. Otherwise everything's the same, it's just changing names.

{{< figure src="./opera-bull-ansible.jpeg" alt="Opera-bull with Ansible bull looking on" width="650" height="458" class="insert-image" >}}

The Ansible community has long been a victim of its own success. Since I got started with Ansible in 2013, the growth in the number of Ansible modules and plugins has been astronomical. That's what happens when you build a very simple but powerful tool—easy enough for anyone to extend into any automation use case.

When I started, I remember writing in [Ansible for DevOps](https://www.ansiblefordevops.com) about 'hundreds' of modules—at the time, mostly covering Linux administration use cases. Today there are many _thousands_, covering Linux and Windows server administration, network automation, security automation, and [even stranger](https://www.youtube.com/watch?v=yF63TnaZfaY) use cases.

Jan-Piet Mens summed it up succinctly in a blog post last year, titled [I care about Ansible](https://jpmens.net/2019/06/21/i-care-about-ansible/):

> In my opinion they’re being inundated.

And he included this tweet:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hey I just met you<br>And this is crazy<br>But here&#39;s a PR<br>So merge it maybe</p>&mdash; Kelly Vaughn 🐞 (@kvlly) <a href="https://twitter.com/kvlly/status/1137360516182151168?ref_src=twsrc%5Etfw">June 8, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

This is a problem that every successful open source project has to deal with. I've written in the past about [why I close PRs](/blog/2016/why-i-close-prs-oss-project-maintainer-notes) and [why saying 'no' is important to prevent maintainer burnout](/blog/2020/saying-no-burnout-open-source-maintainer). In the Drupal community, it's a well-established fact there will always be [20,000+ open issues](https://www.drupal.org/project/drupal), including hundreds of [#drupalWTF](https://www.drupal.org/project/issues/search?issue_tags=DrupalWTF)s. Ansible, as a larger project backed by a corporate entity, sometimes doesn't have the luxury of saying 'no'. Therefore hundreds of barely- or not-at-all-maintained modules and plugins exist in the main [ansible/ansible](https://github.com/ansible/ansible) repository as a result of [drive-by contributions](https://lwn.net/Articles/688560/).

Over the past few years, the core team has worked to build 'Collections', a first-class way built into Ansible to allow modules, plugins, and roles to be packaged up and distributed separately from Ansible via Ansible Galaxy and Automation Hub. The Ansible team wrote up two posts on the [reasoning behind Collections](https://www.ansible.com/blog/the-future-of-ansible-content-delivery) and the [initial plans for the transitionary period](https://www.ansible.com/blog/thoughts-on-restructuring-the-ansible-project). In Ansible 2.10, the code for anything not deemed 'core' (which includes the majority of plugins and modules that are currently stored in the ansible/ansible repository) will be moved into separate collection repositories, with the majority moving into a 'general' collection. As time goes on, some of the more actively-maintained content in the general collection may be extracted into more specific collections.

## The Kubernetes Collection

Seeing the huge increase in Kubernetes adoption—often by teams using some automation tooling already—I decided to help organize the [Kubernetes Working Group](https://github.com/ansible/community/wiki/Kubernetes), and get all the current Kubernetes-related plugins and modules extracted into [their own, dedicated Kubernetes collection](https://github.com/ansible-collections/kubernetes).

Its only been a couple weeks, but the benefits of doing this are already apparent:

  1. The repository is separate from the ansible/ansible repository (which has 4,000+ open issues and 2,000+ open PRs), so it's easier to manage and gauge project health.
  2. The repository runs _more_ CI tests than ever before against multiple versions of Kubernetes, using `ansible-test`, Molecule, and GitHub actions, meaning the Kubernetes modules are already better-documented and will be more thoroughly tested for regressions in every release going forward.
  3. One new module (`k8s_exec`) has already been merged, after having languished in the PR queue in ansible/ansible for almost a year. Other modules and feature improvements are soon to follow.

The `k8s` modules and plugins that existed as part of the main `ansible` package in Ansible 2.9 and earlier will still be present in Ansible 2.10 if you run `pip install ansible`, but I'd recommend depending on and using the Kubernetes Collection directly, to make sure you can use the latest code as soon as it becomes available.

## Using the Kubernetes Collection

To use the collection, you first need to download it:

    ansible-galaxy collection install community.kubernetes

Then in your playbook, after the `- hosts:` definition, add a `collections:` list with `community.kubernetes` in it, e.g.:

```
---
- hosts: localhost
  gather_facts: false
  connection: local

  collections:
    - community.kubernetes

  tasks:
    - name: Ensure the myapp Namespace exists.
      k8s:
        api_version: v1
        kind: Namespace
        name: myapp
        state: present
```

If you add `community.kubernetes` to the list of `collections` in a playbook, then module invocations (like the `k8s` task in the example above) will use the module that ships with the collection. You could also type out the entire Fully Qualified Collection Namespace (FQCN) for _every_ task where you call a module (so substitute `community.kubernetes.k8s` for `k8s` in the task above), but that can get rather tedious, especially if you're updating an existing playbook that calls the modules without any namespacing.

Going even further, I recommend explicitly defining all collection dependencies in an Ansible `requirements.yml` file alongside your playbook. In that file, you can (and probably should!) specify a collection version to use, so you can test new versions of the collection before using them in production:

```
---
collections:
  - name: community.kubernetes
    version: 0.9.0
```

Then make sure to install the content from the requirements file:

    ansible-galaxy collection install -r requirements.yml

Note that you can (and often should) install collections in a project-specific path (e.g. under the current working directory), that way the collections are not shared among all your Ansible projects. I typically add the following two lines to all my Ansible projects' `ansible.cfg` file, to make sure any content that's downloaded is inside my project directory and not shared with any other playbooks:

```
[defaults]
collections_paths = ./
roles_path = ./roles
```

## Contributing to the Ansible Kubernetes Collection

We're still in the early days of moving the `k8s` content out of the main Ansible repo into the Collection repo, but it's already easier than ever to contribute Kubernetes content! The collection includes three sets of tests—all which can be run locally:

  1. Sanity tests, run via `ansible-test sanity --docker`, which check for module and documentation formatting issues, and for basic Python errors.
  2. Basic integration tests, run via `ansible-test integration --docker`, which check for underlying issues with Python libraries and the interaction with the Kubernetes API, on a local OpenShift instance.
  3. Full integration tests, run via `molecule test`, which test almost all aspects of each module in the collection, on a local [kind](https://kind.sigs.k8s.io) cluster.

You can run these tests, and even use the local environment with molecule to do development work and test bug fixes for the Collection. Read more about [Testing and Development](https://github.com/ansible-collections/kubernetes#testing-and-development) in the collection's README.

## Where do we go from here?

There are still a lot of open questions around the use of Collections on Ansible and how they'll impact contribution and overall usage. Jan-Piet Mens sums up the main risk to moving to a more [Bazaar-style](https://www.amazon.com/Cathedral-Bazaar-Musings-Accidental-Revolutionary-ebook/dp/B0026OR3LM/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=60fa60bb4edbc26529fe9555507f8900&language=en_US) model for Ansible content (versus the 'Cathedral' style in use pre-2.10)—instead of everyone moving behind one implementation of a certain feature, you may have an explosion of options. This can be good in some cases, but in the case of a new user trying to choose the best and most well-maintained content, it could make adopting Ansible more challenging.

For a project known for its ease of adoption—one of the main reasons I started using Ansible was it took one hour to get it working with my servers, whereas I gave up on Puppet and Chef after a few days messing around—keeping simplicity in mind for end-users must be a driving force behind smoothing the rough edges of Collections that will inevitably show up over the next year.

> Note: If you're interested in automating Kubernetes with Ansible, I have a great book suggestion for you—[Ansible for Kubernetes](https://www.ansibleforkubernetes.com)! I'm writing the book now, but you can already buy the book from LeanPub and get every update to the book free, forever, with no DRM, on all your devices!
