---
nid: 2602
title: "New features in Ansible 2.0: Blocks"
slug: "new-features-ansible-20-blocks"
date: 2015-09-12T02:51:16+00:00
drupal:
  nid: 2602
  path: /blog/new-features-ansible-20-blocks
  body_format: full_html
  redirects: []
tags:
  - ansible
  - blocks
aliases:
  - /blog/new-features-ansible-20-blocks
---

<blockquote>
The following is an excerpt from Chapter 5 of <a href="http://ansiblefordevops.com/">Ansible for DevOps</a>, a book on Ansible by Jeff Geerling.
</blockquote>

<p>Introduced in Ansible 2.0.0 (still in active development, currently in alpha), Blocks allow you to group related tasks together and apply particular task parameters on the block level. They also allow you to handle errors inside the blocks in a way similar to most programming languages' exception handling.</p>

<p>Here's an example playbook that uses blocks with <code>when</code> to run group of tasks specific to one platform without <code>when</code> parameters on each task:</p>

```
---
- hosts: web
  tasks:
    # Install and configure Apache on RedHat/CentOS hosts.
    - block:
        - yum: name=httpd state=installed
        - template: src=httpd.conf.j2 dest=/etc/httpd/conf/httpd.conf
        - service: name=httpd state=started enabled=yes
      when: ansible_os_family == 'RedHat'
      sudo: yes

    # Install and configure Apache on Debian/Ubuntu hosts.
    - block:
        - apt: name=apache2 state=installed
        - template: src=httpd.conf.j2 dest=/etc/apache2/apache2.conf
        - service: name=apache2 state=started enabled=yes
      when: ansible_os_family == 'Debian'
      sudo: yes
```

<p>If you want to perform a series of tasks with one set of task parameters (e.g. <code>with_items</code>, <code>when</code>, or <code>sudo</code>) applied, blocks are quite handy.</p>

<p>Blocks are also useful if you want to be able to gracefully handle failures in certain tasks. There might be a task that connects your app to a monitoring service that's not essential for a deployment to succeed, so it would be better to gracefully handle a failure than to bail out of the entire deployment!</p>

<p>Here's how to use a block to gracefully handle task failures:</p>

```
tasks:
  - block:
      - name: Shell script to connect the app to a monitoring service.
        script: monitoring-connect.sh
    rescue:
      - name: This will only run in case of an error in the block.
        debug: msg="There was an error in the block."
    always:
      - name: This will always run, no matter what.
        debug: msg="This always executes."
```

<p>Tasks inside the <code>block</code> will be run first. If there is a failure in any task in <code>block</code>, tasks inside <code>rescue</code> will be run. The tasks inside <code>always</code> will always be run, whether or not there were failures in either <code>block</code> or <code>rescue</code>.</p>

<p>Blocks can be very helpful for building reliable playbooks, but just like exceptions in programming languages, <code>block</code>/<code>rescue</code>/<code>always</code> failure handling can overcomplicate things. If it's easier to maintain idempotency using <code>failed_when</code> per-task to define acceptable failure conditions, or to structure your playbook in a different way, it may not be necessary to use <code>block</code>/<code>rescue</code>/<code>always</code>.</p>

<p>Read more about Blocks on the <a href="http://docs.ansible.com/ansible/playbooks_blocks.html">official Blocks documentation page</a>.</p>

<p><em>Read Ansible for DevOps, available on LeanPub:</em></p>

<iframe width="160" height="400" src="https://leanpub.com/ansible-for-devops/embed" frameborder="0" allowtransparency="true"></iframe>
