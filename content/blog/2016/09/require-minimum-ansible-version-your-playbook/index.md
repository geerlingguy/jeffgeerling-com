---
nid: 2698
title: "Require a minimum Ansible version in your Playbook"
slug: "require-minimum-ansible-version-your-playbook"
date: 2016-09-29T01:51:17+00:00
drupal:
  nid: 2698
  path: /blog/2018/require-minimum-ansible-version-your-playbook
  body_format: markdown
  redirects:
    - /blog/2016/require-minimum-ansible-version-your-playbook
aliases:
  - /blog/2016/require-minimum-ansible-version-your-playbook
tags:
  - ansible
  - assert
  - drupal vm
  - tutorial
  - version
---

It's helpful to be able to enforce a minimum required Ansible version in Ansible playbooks. Ansible [Roles](http://docs.ansible.com/ansible/playbooks_roles.html) have long been able to specify a minimum Ansible version—but only for Ansible Galaxy and `ansible-galaxy`-related dependency management.

I've found more and more that users who installed Ansible further in the past (in the 1.7.x or 1.8.x era) are now using some of my newer projects that require Ansible 2.0 (there are [so many nice new shiny things!](/blog/2016/whats-new-ansible-2-and-ansible-galaxy-2-presentation)), and they're running into errors like:

```
ERROR: [DEPRECATED]: include + with_items is a removed deprecated feature.  Please update your playbooks.
Ansible failed to complete successfully. Any error output should be
visible above. Please fix these errors and try again.
```

The problem, as it turns out, is that these users are running a version < 2.0, but it's not very obvious based on that error message!

Luckily, Ansible has the helpful `assert` module, and Ansible also provides a global `ansible_version` dict with the full version string, major and minor versions, etc.—see this output for the var from the `debug` module in a simple test playbook:

```
"ansible_version": {
    "full": "2.1.1.0", 
    "major": 2, 
    "minor": 1, 
    "revision": 1, 
    "string": "2.1.1.0"
}
```

Using these two tools, we are able to build a task in our playbook that will check that the version of Ansible being used to run the playbook meets a minimum (or even exact) requirement.

In [Drupal VM](https://www.drupalvm.com/)'s case, I added the task below as the first task in my playbook's `pre_tasks`:

```
---
- hosts: all
  pre_tasks:
    - name: Verify Ansible meets Drupal VM's version requirements.
      assert:
        that: "ansible_version.full is version_compare('2.1', '>=')"
        msg: >
          "You must update Ansible to at least 2.1 to use this version of Drupal VM."
```

Now, if a user runs Drupal VM's playbook with an outdated version of Ansible, they'll get the following warning:

```
TASK [Verify Ansible meets Drupal VM's version requirements.] ******************
fatal: [drupalvm]: FAILED! => {"assertion": "ansible_version.full is version_compare('2.1', '>=')", "changed": false, "evaluated_to": false, "failed": true, "msg": "\"You must update Ansible to at least 2.1 to use this version of Drupal VM.\"\n"}
```

This is a much more helpful debug message than other 'xyz module failed' messages. Unfortunately, there are still cases (like the one mentioned in this post originally) where this task won't help, because the playbook _itself_ won't be run (since the older version of Ansible can't even parse the full YAML structure correctly).

So for those cases, it would be nice if Ansible provided a built-in mechanism (maybe in a project `ansible.cfg` file) to specify a minimum required Ansible version, like what [Vagrant does](https://www.vagrantup.com/docs/vagrantfile/vagrant_version.html). You can technically write a callback plugin to do the version check, but this seems like overkill to me. See these three issues for further information:

  - [Allow playbooks to require a specific version of Ansible](https://github.com/ansible/ansible/issues/4357) (ansible project - closed issue)
  - [Introduce an ansible_version dict as runner variable](https://github.com/ansible/ansible/pull/6619) (ansible project - merged PR)
  - [Require minimum version of Ansible](https://github.com/geerlingguy/drupal-vm/issues/908) (drupal-vm project - fixed issue)
