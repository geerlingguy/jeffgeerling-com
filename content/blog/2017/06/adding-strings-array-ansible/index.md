---
nid: 2783
title: "Adding strings to an array in Ansible"
slug: "adding-strings-array-ansible"
date: 2017-06-16T17:05:29+00:00
drupal:
  nid: 2783
  path: /blog/2017/adding-strings-array-ansible
  body_format: markdown
  redirects: []
tags:
  - ansible
  - aws
  - ec2
  - loop
  - tutorial
  - variables
---

From time to time, I need to dynamically build a list of strings (or a list of other things) using Ansible's `set_fact` module.

Since `set_fact` is a module like any other, you can use a `with_items` loop to loop over an existing list, and pull out a value from that list to add to another list.

For example, today I needed to retrieve a list of all the AWS EC2 security groups in a region, then loop through them, building a list of all the security group names. Here's the playbook I used:

```
- hosts: localhost
  connection: local
  gather_facts: no

  vars:
    ec2_security_group_names: []

  tasks:
    - name: Get security groups from EC2.
      ec2_group_facts:
        region: us-east-1
        filters:
          "tag:myapp": "example"
      register: ec2_security_groups

    - name: Build a list of all the security group names.
      set_fact:
        ec2_security_group_names: "{{ ec2_security_group_names }} + [ '{{ item.group_name }}' ]"
      with_items: "{{ ec2_security_groups.security_groups }}"

    - name: Print the security group names to the console.
      debug: var=ec2_security_group_names
```

Before building the `ec2_security_group_names` list, I made sure to set it as an empty list in `vars` (`ec2_security_group_names: []`). That way the first time the loop adds a `group_name`, it has something to add to (an empty list)!

When run, you get something like:

```
TASK [debug] ***********************************************************************************************************
ok: [localhost] => {
    "changed": false, 
    "ec2_security_group_names": [
        "security-group-1", 
        "security-group-2", 
        "security-group-3", 
    ]
}
```

