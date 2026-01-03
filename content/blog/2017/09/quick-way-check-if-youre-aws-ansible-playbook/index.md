---
nid: 2806
title: "Quick way to check if you're in AWS in an Ansible playbook"
slug: "quick-way-check-if-youre-aws-ansible-playbook"
date: 2017-09-01T15:28:49+00:00
drupal:
  nid: 2806
  path: /blog/2017/quick-way-check-if-youre-aws-ansible-playbook
  body_format: markdown
  redirects: []
tags:
  - amazon
  - ansible
  - aws
  - set_fact
  - tutorial
  - uri
---

For many of my AWS-specific Ansible playbooks, I need to have some operations (e.g. AWS inspector agent, or special information lookups) run when the playbook is run inside AWS, but not run if it's being run on a local test VM or in my CI environment.

In the past, I would set up a global playbook variable like `aws_environment: False`, and set it manually to `True` when running the playbook against live AWS EC2 instances. But managing vars like `aws_environment` can get tiresome because if you forget to set it to the correct value, a playbook run can fail.

So instead, I'm now using the existence of AWS' internal instance metadata URL as a check for whether the playbook is being run inside AWS:

```
- hosts: all

  pre_tasks:
    - name: Check if inside AWS.
      uri:
        url: http://169.254.169.254/latest/meta-data
        timeout: 2
      register: aws_uri_check
      failed_when: False

    - set_fact:
        is_aws_environment: "{{ aws_uri_check.status == 200 }}"
```

That way, I can use `when: is_aws_environment` as the condition for any AWS-specific tasks, e.g.:

```
  tasks:
    - include: aws-inspector.yml
      when: is_aws_environment
```

It's possible the `http://169.254.169.254/latest/meta-data` may return a `200` inside other infrastructure environments, but it doesn't seem to do so in DigitalOcean, Linode, or other hosting environments I currently use, so this is a bit safer than relying on an instance hostname (which I know many people do).
