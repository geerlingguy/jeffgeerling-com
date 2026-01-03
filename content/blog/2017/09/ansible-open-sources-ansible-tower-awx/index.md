---
nid: 2808
title: "Ansible open sources Ansible Tower with AWX"
slug: "ansible-open-sources-ansible-tower-awx"
date: 2017-09-07T16:51:55+00:00
drupal:
  nid: 2808
  path: /blog/2017/ansible-open-sources-ansible-tower-awx
  body_format: markdown
  redirects:
    - /blog/2017/ansible-open-sources-ansible
aliases:
  - /blog/2017/ansible-open-sources-ansible
tags:
  - ansible
  - ansible for devops
  - ansible tower
  - awx
---

Ever since Red Hat acquired Ansible, I and many others have anticipated whether or when [Ansible Tower](https://www.ansible.com/tower) would be open sourced. Ansible Tower is one of the nicest automation tools I've used... but since I haven't been on a project with the budget to support the Tower licensing fees, I have only used it for testing small-scale projects.

I wrote a guide for [Automating your Automation with Ansible Tower](/blog/automating-your-automation-ansible-tower), and it's both on the web and in Chapter 11 of [Ansible for DevOps](https://www.ansiblefordevops.com), and in the guide, I wrote:

> For smaller teams, especially when everyone on the team is well-versed in how to use Ansible, YAML syntax, and follows security best practices with playbooks and variables files, using the CLI can be a sustainable approach... Ansible Tower provides a great mechanism for team-based Ansible usage.

There are a lot of companies (mine included!) using Jenkins as a substitute for Ansible Tower, and this can work pretty well, but Jenkins doesn't integrate deeply with all Ansible's powerful inventory management, secret management, and playbook management. Tower also supports a lot more flexible authentication and role-based playbook permissions model which makes it a perfect fit for team-based playbook management.

To be clear though, _Ansible Tower_ itself will still be a licensed product offering from Red Hat, but the _code that builds Ansible Tower releases_ is open sourced, and is available in the [AWX Project](https://github.com/ansible/awx). According to the [AWX Project FAQ](https://www.ansible.com/awx-project-faq), the best way to think of this open source model is in the analogy Fedora is to Red Hat Enterprise Linux as AWX is to Ansible Tower:

> AWX is designed to be a frequently released, fast-moving project where all new development happens.
> 
> Ansible Tower is produced by taking selected releases of AWX, hardening them for long-term supportability, and making them available to customers as the Ansible Tower offering.
> 
> This is a tested and trusted method of software development for Red Hat, which follows a similar model to Fedora and Red Hat Enterprise Linux.

I'm excited to see the code behind Tower has finally been open sourced via [AWX](https://github.com/ansible/awx), and I hope to start using it for a few services like [Hosted Apache Solr](https://hostedapachesolr.com) shortly. I'll be updating my book's chapter on Ansible Tower and AWX as soon as I'm able—and if you [buy the book on LeanPub](https://leanpub.com/ansible-for-devops), you'll get that updated content for free, as soon as I finish writing it!

## Getting started with AWX

**tl;dr**: Run the two commands below to run my AWX Docker images, then access http://localhost/ after your CPU calms down, and enter username `admin` and password `password`:

```
curl -O https://raw.githubusercontent.com/geerlingguy/awx-container/master/docker-compose.yml
docker-compose up -d
```

{{< figure src="./awx-shell-script-install.jpg" alt="Install AWX using a script Ansible" width="600" height="304" class="insert-image" >}}

If Docker's not your thing, I'm also maintaining an AWX example in my [Ansible Vagrant Examples](https://github.com/geerlingguy/ansible-vagrant-examples) GitHub repository. Read through [the AWX example README file](https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/awx) for instructions in getting everything set up, and follow the project's issue tracker for further development of the example (I'm working to make it run in more environments, more easily!).

> I'm also building an [Ansible AWX role on Ansible Galaxy](https://galaxy.ansible.com/geerlingguy/awx/) (which is used by the Vagrant example); it's still in a pretty early stage, but should work okay. I'll hopefully get time to optimize it more in the coming weeks!

After you install it, you'll be greeted by this angry potato:

{{< figure src="./awx-login-screen-default.jpg" alt="Ansible AWX login screen angry potato" width="650" height="470" class="insert-image" >}}

Log in with the credentials `admin` and `password`.

## What's up with the name 'AWX'?

Originally, Ansible Tower was called "AWX" — see [this old blog post](https://www.ansible.com/blog/2013/08/05/supercharge-ansible-with-ansibleworks-awx-1-2) from 2013. And apparently that was kind of a short-hand for 'AnsibleWorks', [the original name of the company](https://www.ansible.com/blog/2013/03/04/introducing-ansibleworks) that became Ansible, that became Ansible by Red Hat. Straight from the horse's mouth:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Loosely &quot;ansibleworks&quot;. But nothing really.</p>&mdash; Michael DeHaan (@laserllama) <a href="https://twitter.com/laserllama/status/905849835236020224">September 7, 2017</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

## Ansible for DevOps discounted during AnsibleFest

Right now, [Ansible for DevOps is 25% off in celebration of AnsibleFest](http://leanpub.com/ansible-for-devops/c/2I2Wgy6kiEFS), so pick up a copy today and supercharge your automation with Ansible!
