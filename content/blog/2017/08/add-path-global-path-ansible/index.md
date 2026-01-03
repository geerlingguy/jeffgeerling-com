---
nid: 2799
title: "Add a path to the global $PATH with Ansible"
slug: "add-path-global-path-ansible"
date: 2017-08-11T03:42:40+00:00
drupal:
  nid: 2799
  path: /blog/2017/add-path-global-path-ansible
  body_format: markdown
  redirects: []
tags:
  - ansible
  - copy
  - linux
  - path
  - profile
---

When building certain roles or playbooks, I often need to add a new directory to the global system-wide `$PATH` so automation tools, users, or scripts will be able to find other scripts or binaries they need to run. Just today I did this yet again for my [`geerlingguy.ruby` Ansible role](https://github.com/geerlingguy/ansible-role-ruby), and I thought I should document how I do it here—mostly so I have an easy searchable reference for it the next time I have to do this and want a copy-paste example!

```
    - name: Add another bin dir to system-wide $PATH.
      copy:
        dest: /etc/profile.d/custom-path.sh
        content: 'PATH=$PATH:{{ my_custom_path_var }}'
```

In this case, `my_custom_path_var` would refer to the path you want added to the system-wide `$PATH`. Now, on next login, you should see your custom path when you `echo $PATH`!
