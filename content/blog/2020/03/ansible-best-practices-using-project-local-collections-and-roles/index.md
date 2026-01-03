---
nid: 2974
title: "Ansible best practices: using project-local collections and roles"
slug: "ansible-best-practices-using-project-local-collections-and-roles"
date: 2020-03-02T18:20:57+00:00
drupal:
  nid: 2974
  path: /blog/2020/ansible-best-practices-using-project-local-collections-and-roles
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible galaxy
  - best practices
  - collections
  - roles
---

> **Note for Tower/AWX users**: Currently, Tower requires role and collection requirements to be split out into different files; see [Tower: Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ansible-galaxy-support). Hopefully Tower will be able to support the requirements layout I outline in this post soon!

Since collections will be a major new part of every Ansible user's experience in the coming months, I thought I'd write a little about what I consider an Ansible best practice: that is, always using project-relative collection and role paths, so you can have multiple independent Ansible projects that track their own dependencies according to the needs of the project.

Early on in my Ansible usage, I would use a global roles path, and install all the roles I used (whether private or on Ansible Galaxy) into that path, and I would rarely have a playbook or project-specific role or use a different playbook-local version of the role.

Over time, I found that many playbooks benefitted from having all role dependencies managed independently. That meant adding a `requirements.yml` file for that playbook, (usually, but not always) defining each role's version or Git commit hash, and adding an `ansible.cfg` file in the playbook project's root directory so Ansible would know to _only_ load roles from that playbook's roles directory.

With collections, I'm expanding that best practice, and generally recommend against installing collections into a global location (like the default, which is `~/.ansible/collections` or `/usr/share/ansible/collections`).

For any new project I start, I add a `ansible.cfg` with the following (at minimum):

```
[defaults]

# Chick-Fil-A would like a word...
nocows = True

# Installs collections into [current dir]/ansible_collections/namespace/collection_name
collections_paths = ./

# Installs roles into [current dir]/roles/namespace.rolename
roles_path = ./roles
```

Then I manage all my playbook's dependencies in a `requirements.yml` file like this one:

```
---
roles:
  - name: geerlingguy.java
    version: 1.9.7

collections:
  - name: community.kubernetes
    version: 0.9.0
```

Assuming [this PR](https://github.com/ansible/ansible/pull/67843) is merged prior to Ansible 2.10's release, you can then install all the playbook project's dependencies with:

    ansible-galaxy install -r requirements.yml

Then your playbooks will use the correct requirements, and won't affect any other playbooks and Ansible projects.

This also optimizes things because instead of Ansible having to scan through the likely hundreds (thousands?) of role and collection directories that I would need to have in global paths to support the hundreds of projects I work with, it only needs to scan the few that are required for the given project I'm working on.

A final major benefit is you can then commit the roles and collections to your project code repository, and then the dependencies are _part of the deployable project_, which gives two major benefits:

  1. Other people (e.g. coworkers, or even CI systems) which work with the project would necessarily have the same revision as everyone else as part of the project VCS, and updates to any dependencies would be checked in via source control.
  2. You could still run the playbook if GitHub, Ansible Galaxy, or any other system required to download the dependencies were offline, since you wouldn't need to run `ansible-galaxy` at all (except to update dependencies when you want to do so).
