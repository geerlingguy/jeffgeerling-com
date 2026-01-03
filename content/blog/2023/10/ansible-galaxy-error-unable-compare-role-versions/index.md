---
nid: 3319
title: "Ansible Galaxy error 'Unable to compare role versions'"
slug: "ansible-galaxy-error-unable-compare-role-versions"
date: 2023-10-24T23:08:26+00:00
drupal:
  nid: 3319
  path: /blog/2023/ansible-galaxy-error-unable-compare-role-versions
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible galaxy
  - ansible-galaxy
  - bugs
  - open source
  - roles
---

Ansible Galaxy was recently updated to the 'Next Generation' ([Galaxy-NG](https://github.com/ansible/galaxy_ng/)) codebase.

There are some growing pains, as a lot of Galaxy NG was built up around Collections, and Ansible role support was written into the codebase over the past year or so, after it became obvious Galaxy roles would not be deprecated.

Unfortunately, one of the major issues right now—which I'm seeing pop up in many places—is an error that occurs upon installation of Galaxy roles for any playbook (e.g. when you run `ansible-galaxy install` to download a role), for any role that has had a new version released in the past few weeks.

You wind up with an error like:

```
[WARNING]: - geerlingguy.pip was NOT installed successfully: Unable to compare
role versions (1.0.0, 1.1.0, 1.2.0, 1.2.1, 1.2.2, 1.3.0, 2.0.0, 2.1.0, 2.2.0,
master) to determine the most recent version due to incompatible version
formats. Please contact the role author to resolve versioning conflicts, or
specify an explicit role version to install.
ERROR! - you can use --ignore-errors to skip failed roles and finish processing the list.
```

The problem is the code that imports new role versions in Galaxy NG currently grabs the HEAD branch name and imports that as a tag... which leads to an impossible comparison between version strings and a text string—leading to the above error message.

A fix is being worked on here: [Revamp legacyrole versions](https://github.com/ansible/galaxy_ng/pull/1946), and I opened up an issue on the Ansible Community Forum here: [Role import from GitHub results in “master” release, not the tag release, breaking installs](https://forum.ansible.com/t/role-import-from-github-results-in-master-release-not-the-tag-release-breaking-installs/).

Until fixed on Ansible Galaxy, the only way to get Ansible to install the role correctly is to specify the role's GitHub repository and a specific version in your `requirements.yml` file like so:

```
---
roles:
  - name: geerlingguy.pip
    src: https://github.com/geerlingguy/ansible-role-pip.git
    version: 3.0.0
```

Then run `ansible-galaxy role install -r requirements.yml`.

There's a forum topic tracking some of the other complaints about Galaxy NG, and it seems most of them center around role support, and how it is a bit, shall we say, 'broken' at launch: [The new Galaxy is completely broken](https://forum.ansible.com/t/the-new-galaxy-is-completely-broken/1518).

I do hope the team can get some of the more egregious bugs worked out (and I have faith they will). I think some of the community outcry validates my push a year or two ago for role support to _not_ be called 'legacy' or 'deprecated'—so many of us in the community still use Galaxy almost exclusively for roles, and collections still don't enhance role-based playbook use in a meaningful way—at least IMHO.
