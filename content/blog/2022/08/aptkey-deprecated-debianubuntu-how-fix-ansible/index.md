---
nid: 3231
title: "apt_key deprecated in Debian/Ubuntu - how to fix in Ansible"
slug: "aptkey-deprecated-debianubuntu-how-fix-ansible"
date: 2022-08-30T15:37:04+00:00
drupal:
  nid: 3231
  path: /blog/2022/aptkey-deprecated-debianubuntu-how-fix-ansible
  body_format: markdown
  redirects:
    - /blog/2022/aptkey-usage-deprecated-debianubuntu-how-fix-ansible
aliases:
  - /blog/2022/aptkey-usage-deprecated-debianubuntu-how-fix-ansible
tags:
  - ansible
  - apt
  - debian
  - gpg
  - tutorial
  - ubuntu
---

> **2023 Update**: Ansible now has the [`ansible.builtin.deb822_repository`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/deb822_repository_module.html) module, which can add keys _and_ repositories in one task. It's a little more complex than the old way, and requires Ansible 2.15 or later. See some [common `deb822_repository` examples](https://gist.github.com/roib20/27fde10af195cee1c1f8ac5f68be7e9b) here, for example, the Jenkins tasks below can be consolidated (though the structure of the templated vars would need reworking):
> 
> ```
> - name: Add Jenkins repo using key from URL.
>   ansible.builtin.deb822_repository:
>     name: jenkins
>     types: [deb]
>     uris: "https://pkg.jenkins.io/debian-stable"
>     components: [binary]
>     signed_by: https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
>     state: present
>     enabled: true
> ```

For many packages, like Elasticsearch, Docker, or Jenkins, you need to install a trusted GPG key on your system before you can install from the official package repository.

Traditionally, you'd run a command like:

```
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
```

But if you do that in modern versions of Debian or Ubuntu, you get the following warning:

```
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
```

This way of adding apt keys still works for now (in mid-2022), but will stop working in the next major releases of Ubuntu and Debian (and derivatives). So it's better to stop the usage now. In Ansible, you would typically use the [`ansible.builtin.apt_key`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_key_module.html) module, but even that module has the following deprecation warning:

> The apt-key command has been deprecated and suggests to ‘manage keyring files in trusted.gpg.d instead’. See the Debian wiki for details. This module is kept for backwards compatiblity for systems that still use apt-key as the main way to manage apt repository keys.

So traditionally, I would use a task like the following in my Ansible roles and playbooks:

```
- name: Add Jenkins apt repository key.
  ansible.builtin.apt_key:
    url: https://pkg.jenkins.io/debian-stable/jenkins.io.key
    state: present

- name: Add Jenkins apt repository.
  ansible.builtin.apt_repository:
    repo: "deb https://pkg.jenkins.io/debian-stable binary/"
    state: present
```

The new way to do this without adding an extra `gpg --dearmor` task is to use `get_url` to download the file into the `trusted.gpg.d` folder with the `.asc` filename. Therefore the first task above can be replaced with:

```
- name: Add Jenkins apt repository key.
  ansible.builtin.get_url:
    url: "{{ jenkins_repo_key_url }}"
    dest: /etc/apt/trusted.gpg.d/jenkins.asc
    mode: '0644'
    force: true
```

See [this issue in ansible/ansible](https://github.com/ansible/ansible/issues/78063) for a little more background.
