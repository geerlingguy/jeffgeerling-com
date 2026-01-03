---
nid: 3110
title: "Allowing Ansible playbooks to work with new user groups on first run"
slug: "allowing-ansible-playbooks-work-new-user-groups-on-first-run"
date: 2021-06-14T15:42:37+00:00
drupal:
  nid: 3110
  path: /blog/2021/allowing-ansible-playbooks-work-new-user-groups-on-first-run
  body_format: markdown
  redirects: []
tags:
  - ansible
  - devops
  - docker
  - idempotence
  - playbook
  - reset_connection
---

For a long time, I've had some Ansible playbooks—most notably ones that would install Docker then start some Docker containers—where I had to split them in two parts, or at least run them twice, because they relied on the control user having a new group assigned for some later tasks.

The problem is, Ansible would connect over SSH to a server, and use that connection for subsequent tasks. If you add a group to the user (e.g. `docker`), then keep running more tasks, that new group assignment won't be picked up until the SSH connection is reset (similar to how if you're logged in, you'd have to log out and log back in to see your new `groups`).

The easy fix for this? Add a `reset_connection` meta task in your play to force Ansible to drop its persistent SSH connection and reconnect to the server:

```
- name: Ensure pi user is added to the docker group.
  ansible.builtin.user:
    name: pi
    groups: docker
    append: true

# reset_connection doesn't support conditionals.
- name: Reset connection so docker group is picked up.
  meta: reset_connection
```

That example was taken from my Raspberry Pi Internet monitoring playbook, and was added as part of the issue [Use 'meta: reset_connection` if Docker pi user group changes](https://github.com/geerlingguy/internet-pi/issues/5). See [commit](https://github.com/geerlingguy/internet-pi/commit/c1f4b7beca6f3f796775e6c4b56777fa9d5b1c88).

Unfortunately, you can't add `when` conditionals to the `reset_connection` meta task... so it will always reset the connection on every playbook run. But it's a small price to pay to have a playbook that always works on the first run!
