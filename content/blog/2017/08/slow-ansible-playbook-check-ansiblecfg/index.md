---
nid: 2801
title: "Slow Ansible playbook? Check ansible.cfg!"
slug: "slow-ansible-playbook-check-ansiblecfg"
date: 2017-08-20T04:00:26+00:00
drupal:
  nid: 2801
  path: /blog/2017/slow-ansible-playbook-check-ansiblecfg
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible.cfg
  - configuration
  - performance
  - playbooks
  - tuning
---

Today while I was running a particularly large Ansible playbook about the 15th time in a row, I was wondering why _this_ playbook seemed to run quite a bit slower than most other playbooks, even though I was managing a server that was in the same datacenter as most of my other infrastructure.

I have had `pipelining = True` in my system `/etc/ansible/ansible.cfg` for ages, and initially wondered why the individual tasks were so delayed—even when doing something like running three `lineinfile` tasks on one config file. The only major difference in this slow playbook's configuration was that I had a local `ansible.cfg` file in the playbook, to override my global `roles_path` (I wanted the specific role versions for this playbook to be managed and stored local to the playbook).

So, my curiosity led me to a more thorough reading of [Ansible's configuration documentation](http://docs.ansible.com/ansible/latest/intro_configuration.html), specifically a section talking about Ansible configuration file precedence:

> Changes can be made and used in a configuration file which will be processed in the following order:
> 
>   - ANSIBLE_CONFIG (an environment variable)
>   - ansible.cfg (in the current directory)
>   - .ansible.cfg (in the home directory)
>   - /etc/ansible/ansible.cfg
> 
> Ansible will process the above list and use the first file found. Settings in files are not merged.

Then it hit me—unlike `vars_include` and `include` module behavior within an Ansible playbook, Ansible _configuration_ files (the ones that tell Ansible how to connect, how to optimize things over SSH, etc.) are _not_ merged. Instead, Ansible uses the above hierarchy to choose one file, then it will use configuration overrides **from that file and no others**.

So even though I had the following in my global configuration file:

    [ssh_connection]
    pipelining = True
    control_path = /tmp/ansible-ssh-%%h-%%p-%%r

The settings weren't applying to Ansible when I was running this large Ansible playbook, because it had its own `ansible.cfg`.

I copied and pasted my `[ssh_connection]` settings into the playbook's local `ansible.cfg`, and—well, the results speak for themselves:

|Pipelining enabled|Time to complete|
|--------|--------|
|No|03:28|
|Yes|01:42|

So, two takeaways:

  - Unless it breaks your configuration, **you should always set `pipelining = True` in `ansible.cfg`**
  - If you add a custom `ansible.cfg` in a project/playbook, make sure you add in all the configuration you need—global overrides (e.g. in `/etc/ansible/ansible.cfg`) are not merged!

It looks like there's a related ticket that's been open for some time: [Merge ansible config files](https://github.com/ansible/ansible/issues/17914), and even better—it looks like there's been some movement towards an implementation!
