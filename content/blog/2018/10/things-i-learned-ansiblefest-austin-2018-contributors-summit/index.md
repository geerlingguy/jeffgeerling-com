---
nid: 2880
title: "Things I learned at the AnsibleFest Austin 2018 Contributor's Summit"
slug: "things-i-learned-ansiblefest-austin-2018-contributors-summit"
date: 2018-10-01T22:13:59+00:00
drupal:
  nid: 2880
  path: /blog/2018/things-i-learned-ansiblefest-austin-2018-contributors-summit
  body_format: markdown
  redirects:
    - /blog/2018/things-i-learned-ansiblefest-2018-contributors-summit
aliases:
  - /blog/2018/things-i-learned-ansiblefest-2018-contributors-summit
tags:
  - ansible
  - ansiblefest
  - community
  - contributions
---

AnsibleFest Austin 2018 is about to get started (with a huge party tonight, then a keynote to kick off two full days of sessions tomorrow), and the day before and after the 'Fest marks the [6th "Contributor's Summit"](https://groups.google.com/forum/#!topic/ansible-devel/ivrpVbLya8g), a "working session with the core team and key contributors to discuss important issues affecting the Ansible community".

{{< figure src="./ansiblefest-2018-austin-contributor-summit.jpg" alt="AnsibleFest 2018 Austin Contributors Summit" width="650" height="433" class="insert-image" >}}

As with most conference-related events, the best part of the day is getting to meet with and talk to people you work with online, but there are also usually lots of little tidbits discussed during the sessions which aren't yet widely known. Some of the most exciting things I learned today include:

  - [Ansible 2.7](https://docs.ansible.com/ansible/devel/roadmap/ROADMAP_2_7.html) is coming this week! It includes:
    - A new `reboot` module (I blogged about [rebooting servers with Ansible](/blog/2018/reboot-and-wait-reboot-complete-ansible-playbook) previously)
    - A new AWS EKS module for managing EKS clusters.
    - Ansible Roles can be run ad-hoc! For example: `ansible all -m include_role -a name=geerlingguy.nginx`
  - [Ansible Pulp](https://github.com/pulp/pulp_ansible) can help with air-gapped Ansible Galaxy usage, local caching, that kind of thing.
  - [Mazer](https://github.com/ansible/mazer) and Ansible Galaxy 'Collections', which is a new way you will be able to package roles + plugins + modules in a project
    - Mazer would also host artifacts, and not be tied to GitHub tags for releases (which means Ansible Galaxy can guarantee that once a release is built, it will be the same forever).
    - Mazer-based content should also allow for things like `mazer update` to be able to update dependencies.
    - Mazer-based content would also follow [semantic versioning](https://semver.org), so eventually you could follow specific version targets, etc.
  - [Molecule](https://molecule.readthedocs.io/) has been adopted by Ansible and will soon be moved under Ansible's GitHub namespace.
    - Inspired by [test-kitchen](https://docs.chef.io/kitchen.html) for Chef, it's a test and development framework for CI
    - Simple guide (once you have a molecule-driven role): `molecule create`, hack on feature, submit PR
    - 'Scenarios' allow you to test role in various use cases
  - Ansible Galaxy will soon incorporate 'quality scores', at least partially driven by [this list of ansible lint rules for Galaxy](https://github.com/ansible/galaxy-lint-rules).
    - I opened an issue questioning the application of one of the proposed rules: [LineTooLongRule - how to deal with it?](https://github.com/ansible/galaxy-lint-rules/issues/4)
    - TODO: How do you run `molecule lint` incorporating these rules?
  - Red Hat is building some [Linux System Roles](https://linux-system-roles.github.io/), which are are a collection of Ansible roles officially maintained by Red Hat to work with Linux subsystems, especially across distros like RHEL 6, RHEL 7, Fedora.
    - It was mentioned that they may accept contributions to extend roles to work with other Linux distros as well; but currently targeting Red Hat.
    - Stable roles started shipping in RHEL 7.4.

There's another full day of the Summit on Thursday, but I will only be able to make a few of those sessions. Both tomorrow _and_ Wednesday I'll be presenting the session [Making your playbooks maintainable, flexible, and scalable](https://www.ansible.com/blog/make-your-ansible-playbooks-flexible-maintainable-and-scalable) (link is to preview of the session on the official Ansible Blog); as soon as possible I'll share the slides and video from the session here!
