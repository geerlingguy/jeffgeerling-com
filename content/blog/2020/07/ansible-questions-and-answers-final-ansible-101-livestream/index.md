---
nid: 3024
title: "Ansible Questions and Answers from the final Ansible 101 livestream"
slug: "ansible-questions-and-answers-final-ansible-101-livestream"
date: 2020-07-02T22:02:01+00:00
drupal:
  nid: 3024
  path: /blog/2020/ansible-questions-and-answers-final-ansible-101-livestream
  body_format: markdown
  redirects: []
tags:
  - ansible
  - livestream
  - questions
  - video
  - youtube
---

Over the past four months, I live-streamed a series of episodes covering all the basics of using Ansible for infrastructure automation in my [Ansible 101 series on YouTube](/blog/2020/ansible-101-jeff-geerling-youtube-streaming-series).

In the last episode of the series, I asked viewers to send in questions that I could answer on the final live stream, and there were many great questions sent in. Some of those questions and my answers are posted below, and you can also view the entire episode in the embedded video below:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/sb5XYD3BLMA" frameborder='0' allowfullscreen></iframe></div>

## Matias

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1020s">View this Q&A in the livestream</a>

> How do you organize your Ansible tasks? What are the best practices for Ansible?

_Jeff_: This may sound like a cop-out, but check out Appendix B in [Ansible for DevOps](https://www.ansiblefordevops.com). It covers what I consider some best practices that will help you on your journey. Also look over episodes 3-6, as those deal with basic playbook organization. Typically, I try to keep my task files under 100 lines, and if I have more than one or two Pythonic statements in my conditions, I work on moving those into Ansible plugins (like the test plugin I built in episode 13!).

## Adam

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1180s">View this Q&A in the livestream</a>

> How do you bootstrap a computer with Ansible? I do it two ways currently:
>
>   1. Use Kickstart to put a key and user on the computer
>   2. I initially connect with root in my playbook to create the Ansible user

_Jeff_: There are so many ways to do it. I'm like you; there are some cases (like when bootstrapping servers for my [Hosted Apache Solr](https://hostedapachesolr.com) service) when I connect with root in an initial play, then after that play runs, the next play switches and uses the Ansible management user set up in the initial play. I also build many servers using pre-made images using Packer, and for these I try to always use kickstart for the initialization, then configure everything else with Ansible. See my [packer-boxes](https://github.com/geerlingguy/packer-boxes) repo for some examples.

I typically prefer doing the latter: pre-building AMIs and container images with Ansible so I don't have to manage all the initialization details on my first connection.

## Dwayne

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1368s">View this Q&A in the livestream</a>

> Will you be creating a Mastering Ansible book and doing another live stream for that?
> You mentioned you're working on 'Ansible for Kubernetes'. Is it full K8s or K3s?

_Jeff_: I probably won't be creating any book at the 'mastering' level, mostly because I think when you get to that level with a tool like Ansible, you should really be focused on 'mastering' one particular aspect. There are many different parts to Ansible, like Windows, Networking, Security, Cloud, and containers, and I feel like I know some parts better than others. So I'd more likely work on books and videos that go deeper on _certain topics_, but I feel like my [Ansible for DevOps](https://www.ansiblefordevops.com) book is the best broad-topic coverage I can do for Ansible itself.

I am currently writing [Ansible for Kubernetes](https://www.ansibleforkubernetes.com), and it's about half complete. It covers all of Kubernetes (full K8s, installed and run many different ways), and I will likely also touch on or even cover some of K3s and the differences between distributions like OpenShift/OKD, microk8s, and K3s in the book.

## Joshua

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1496s">View this Q&A in the livestream</a>

> What's the best place for Ansible variables? `ansible.cfg` or an `inventory` file?

_Jeff_: The answer is _it depends_. I tend to have an `ansible.cfg` in all my playbook repositories, so sometimes if it's something that I want to apply to all things, I'll drop it there. But I usually need more control over which hosts or groups the variable applies to, so I put variables in inventory most of the time.

## Gowtham

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1604s">View this Q&A in the livestream</a>

> What's the best way to run ansible in CI/CD (e.g. in Docker containers)? Any gotchas?

_Jeff_: I maintain a large number of Docker images with Ansible inside (see [ansible.jeffgeerling.com](https://ansible.jeffgeerling.com)). I use these for testing with Molecule for almost all my Ansible projects (for example, see my [Apache role's Molecule configuration](https://github.com/geerlingguy/ansible-role-apache/tree/master/molecule/default). It's trivial to install Ansible in your own Docker images, since most environments have Python available and you just need to install `pip3`, then `pip3 install ansible`.

## Dave

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1754s">View this Q&A in the livestream</a>

> If you have a mix of CentOS, Ubuntu, and Windows servers, would you maintain separate repositories for Linux vs. Windows? Or one single repo, inventory, etc.?

_Jeff_: That's a good question. I think it comes down to the applications you manage. If you have one heterogenous system, one monorepo would be nice. But if you have tons of different servers doing different things, only loosely related, I would stick with different repos for different types of machines. But I'd still consider using a central inventory system, and there are many out there, like Device42, Solarwinds, etc.

## Judd

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1888s">View this Q&A in the livestream</a>

> What is your opinion on ownership of operations in Ansible for systems that rely on each other? Example: Postgres database server that services multiple independently-managed systems.

_Jeff_: Good question. I try to make sure that my software is installed and configured by more generic Ansible content, like my [Postgres role](https://galaxy.ansible.com/geerlingguy/postgresql). And if a particular server or cluster would need specific configuration for one or more applications, I would break that out into a separate role or put the logic for it in a different part of the play.

That way my application-based roles, like my Postgres role, can stay generic and reusable across all my Postgres installations, but the logic that determines what runs on a particular cluster can stay separate and specialized.

## Namasivayam

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2031s">View this Q&A in the livestream</a>

> As a teacher, we have students set up servers inside a NAT on VMware Workstation, then we want to check them using Ansible playbooks, but we don't yet want them to see the playbooks we use to check their work.
>
> Could we use something like SSH port forwarding to a central shared server that their workstation and the school network could see?

_Jeff_: Good question. I'm not as familiar with VMware as I haven't used it in a while, but I do believe there's a way to get it configured to set up port forwarding, and then your central network server that runs the playbooks could point to the individual machine's IP and SSH port. This could create a bit of a security risk, assuming the students might not have hardened their installs perfectly! You may also be able to set up some sort of SSH proxying for this, but it's something you'd have to experiment with a bit to get it set up correctly.

## David

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2138s">View this Q&A in the livestream</a>

> How do you deal with isolated servers in a DMZ that don't have Internet access? Tower has 'isolated nodes', but that feature's not available to AWX. We currently have a server inside the DMZ act as the orchestrator, pulling playbooks from git.

_Jeff_: That's typically what I do as well. You either have to build a system that can access servers through a bastion somehow, or you have to have a server inside the DMZ that can access those servers to manage them and access the Ansible playbooks to be run on them. You can also use `ansible-pull` mode on the individual machines, assuming they could pull from a git repository hosted inside the DMZ.

## Martin

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2188s">View this Q&A in the livestream</a>

> Can you talk about tasks based on facts? Like if you have a couple hosts, and want to deploy an app to the host with the most free RAM?

_Jeff_: I have a solution for this particular problem below, but I have to warn you, when doing dynamic things like this in Ansible, there are some types of automation that would be better left to a more purpose-built scheduling system, like Kubernetes. If you used the playbook below and didn't design it in a way that took into account where an application was already deployed, you could end up with multiple application instances running in your servers!

I have an example playbook that could work with a modified version of the [sortbysubkey plugin mentioned in this Stack Overflow answer](https://stackoverflow.com/a/51865113/100134):

```
---
- hosts: all
  gather_facts: true

  tasks:
    - name: Find host with most available memory.
      set_fact:
        id_max_host: "{{ hostvars | sortbysubkey('ansible_memfree_mb' | int) | last }}"

    - name: Get the hostname
      set_fact:
        host_with_the_most: "{{ hostvars[id_max_host] }}"

    - debug:
        var: host_with_the_most['ansible_hostname']

    - block:
        # Do things like deploy an app in here.
      delegate_to: "{{ host_with_the_most['ansible_hostname'] }}"
```

You could test this playbook locally against a few servers set up by, for example, my [orchestration](https://github.com/geerlingguy/ansible-for-devops/tree/master/orchestration) multi-node example in the Ansible for DevOps repository.

The main thing to keep in mind is that if you want to use some value derived from facts gathered from _all_ your servers, you'll need to use `set_fact` to set the derived value in your playbook so the variable is applied to all your servers. Then, you can use `delegate_to` to delegate a task to a specific server.

## Shih

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2410s">View this Q&A in the livestream</a>

> Would you recommend insstalling AWX in a Kubernetes cluster? Should it be in a dedicated cluster?

_Jeff_: Yes and no. Currently you can get Tower installed in OpenShift or Kubernetes using the [official Tower OpenShift installer](https://releases.ansible.com/ansible-tower/setup_openshift/), so if you want to do it, that's the best way. But for AWX, the easiest way to do it is to use the [AWX Operator](https://github.com/ansible/awx-operator). Note that this project is a fork from my original [Tower Operator](https://github.com/geerlingguy/tower-operator) and was recently moved into Ansible's GitHub organization, but is not supported under a Red Hat support contract.

## Daniel

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2570s">View this Q&A in the livestream</a>

> What are some cases you might have seen Ansible used when it shouldn't have been used?

_Jeff_: Two good examples are my [ansible-requirements-updater](https://github.com/geerlingguy/ansible-requirements-updater), which would likely be better off as a Python script or Go application, since it's mostly 'programming by template', which is kind of an Ansible anti-pattern. I also [sometimes use Ansible to generate HTML](https://github.com/geerlingguy/ansible.jeffgeerling.com/blob/master/scripts/generate-ansible-test-container-list.yml), and there are definitely a thousand better ways to do that.

But in the end, I like to think that a working solution is better than no solution, so if using Ansible automated away some formerly manual, labor-intense process, it's a net win. But if you find yourself spending more time writing Python and Jinja statements in a playbook, either some things should be moved into plugins or modules, or you might be using Ansible in a way that's not the most useful.

## Simon

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2705s">View this Q&A in the livestream</a>

> I can control Linux hosts via SSH with Ansible through multiple bastion hosts. Can you give an example of how I can chain SSH or configure WinRM to jump through multiple Linux bastion hosts?

_Jeff_: You'll need to ask someone else, unfortunately; I have only really managed Windows hosts running OpenSSH (e.g. in [Ansible 101 Episode 14 on Windows](https://www.youtube.com/watch?v=N7tgLVCXup4)), and WinRM is not something I have really dealt with.

## Hans

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2751s">View this Q&A in the livestream</a>

> How can you make Molecule faster for multiple-host scenarios (e.g. with Vagrant)?
> How do you properly create and remove admin users with ssh key access?
> What's the best practice for running different roles on different hosts in one playbook?

_Jeff_:

  1. I noticed this blog post, published just a few days ago: [Testing Ansible Roles for Multiple Hosts or Clusters with Molecule](https://medium.com/swlh/testing-ansible-roles-for-multiple-hosts-or-clusters-with-molecule-e4e67a2d0d83). It's well-written, and covers testing on multiple hosts using Molecule and Docker, which may be a little faster (especially for initialization) than testing with Vagrant.
  2. For an example of how I normally do this, see my public [`geerlingguy.github-users`](https://galaxy.ansible.com/geerlingguy/github-users/) role. That role allows the easy addition and removal of user accounts based on GitHub accounts, but my private roles that do this for my own infrastructure are built in an extremely similar fashion.
  3. The best way to apply different roles to different hosts in one playbook is to use multiple plays. I highlighted one specific example of this in my [Raspberry Pi cluster series episode 3, covering installation of K3s with `k3s-ansible`](https://youtu.be/N4bfNefjBSw?t=702). You can see the playbook with three different plays [here](https://github.com/rancher/k3s-ansible/blob/master/site.yml). Also, if you need to apply a role to a specific host or group of hosts inline in a play's tasks, you can use `include_role` along with `delegate_to`, but that can get a little bit messy.

## Claudio

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3156s">View this Q&A in the livestream</a>

> What are best practices for organizing playbooks for:
>
>   1. dev/stage/prod environments
>   2. selective task execution (e.g. tags, blocks)

_Jeff_: Check out [this part of Episode 6](https://www.jeffgeerling.com/watch?v=JFweg2dUvqM&t=1293s). I like to make the same playbook work for dev/stage/prod without changes, using inventory variables to differentiate between them. Sometimes I have to add a conditional include or a role that configures something special for a non-prod environment though. But I always use a non-prod environment to test major changes (even if it's just local or local + CI)!

## Robert

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3323s">View this Q&A in the livestream</a>

> For a fairly complex playbook, involving many files, how does one visualize what the playbook is going to do, especially if you didn't write it yourself?

_Jeff_: Great question. There are two tools I know of that you can use to visualize playbooks:

  - Built into Ansible, you can use `--list-tasks` to get a broad overview of the playbook: `ansible-playbook --list-tasks playbook.yml`
  - You can also use the [Ansible Playbook Grapher](https://github.com/haidaraM/ansible-playbook-grapher) to generate a graphical representation of plays. For more on this, see the blog post [Visualizing with Ansible Playbook Grapher](https://blog.networktocode.com/post/visualizing-ansible-plays-and-tasks/).

Both methods are good for an overview, but you can't really know the details or know exactly which tasks will run, or in what exact order, without looking at the code or running the playbook itself.

You could also run a playbook in `--check` mode, but not every playbook (or even module!) is built in a way that would work properly in check mode, so be careful doing that with a playbook you don't know that well!

## Seb

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3511s">View this Q&A in the livestream</a>

> How would you configure a connection to a host when you have to SSH tunnel through multiple other machines with various usernames, passwords, and keys?

_Jeff_: You got me there. I'm fairly certain this is possible, but you have to make sure your SSH configuration is all correct, then make sure your Ansible inventory is set up properly. Check out [this SO question](https://stackoverflow.com/q/53966782/100134) for some hints.

## Gurudatta

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3572s">View this Q&A in the livestream</a>

> How do you append values to specific files, for example, revision, IP address, hostname in a specific file for multiple hosts?

_Jeff_: This is something that should be possible with basic Jinja templating, for example:

```
---
- hosts: localhost
  gather_facts: false
  connection: local

  tasks:
    - file:
        path: "test-{{ inventory_hostname }}"
        state: touch
```

This playbook, when run with `ansible-playbook -i 'localhost,' main.yml`, would result in a file being written in the current directory with the name `test-localhost`.

## Eddie

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3644s">View this Q&A in the livestream</a>

> How do you display and parse output properly when the debug module is enabled?

_Jeff_: Let's assume you have a playbook like the following:

```
---
- hosts: localhost
  gather_facts: false
  connection: local

  tasks:
    - debug:
        var: hostvars['localhost']['ansible_version']
```

If you run the playbook with the command `ansible-playbook -i 'localhost,' eddie-debug-output.yml`, you'll get the output:

```
TASK [debug] *****************************************************
ok: [localhost] => {
    "hostvars['localhost']['ansible_version']": {
        "full": "2.9.10",
        "major": 2,
        "minor": 9,
        "revision": 10,
        "string": "2.9.10"
    }
}
```

The output is a little hard to parse because it's kind of an inline JSON format. You can change the way Ansible outputs data to the screen by specifying a different [callback plugin](https://docs.ansible.com/ansible/latest/plugins/callback.html). I like to use `yaml` but you could also use something like `minimal` to have slightly less noise to sort through.

To get the output in the second code block below, I used the `yaml` plugin, which I configured in my `ansible.cfg` file:

```
[defaults]
nocows = True
stdout_callback = yaml
```

```
TASK [debug] *****************************************************
ok: [localhost] => 
  hostvars['localhost']['ansible_version']:
    full: 2.9.10
    major: 2
    minor: 9
    revision: 10
    string: 2.9.10
```

This looks a lot nicer, and copying out the `hostvars` section makes it easy to read and manage the data being output, since it's just YAML.

You can also check out Ansible's [Playbook Debugger](https://docs.ansible.com/ansible/latest/user_guide/playbooks_debugger.html), which may be helpful in getting deeper into debug output for tasks giving you trouble.

## Samuel

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3755s">View this Q&A in the livestream</a>

> You have previously stated that you were predominantly a PHP developer still are. How did you pivot into Python, Ansible, and K8s?
Will you be doing an Ansible for Kubernetes series?

_Jeff_: You're correct, I started out doing web development in the early 2000s, and one of my early projects led me to using Drupal for a media site (for podcasting and broadcasting video). I learned PHP mostly as a side effect of choosing Drupal then needing to build additional custom functionality, and then learned a lot more over the years as I worked on other PHP-based projects.

I started learning Linux server administration and bash scripting as I needed to focus more on getting my web applications to run better and become more scalable, and then as some of my projects scaled to multiple servers, I needed to automate things. That started out as a mess of bash scripts, and eventually led me to Ansible. And in the first few years using Ansible, I knew very little Python; only as much as I picked up writing some Python scripts to control Raspberry Pi projects and build a couple small Flask apps.

Now I know a lot more Python, but still wouldn't call myself a seasoned Python developer. But I usually pick up tools based on a need, then learn the underlying tech stack and languages as I need to do so. (The same goes for Kubernetes and the Go language!).

I am most definitely considering an Ansible for Kubernetes or Kubernetes 101 series on my YouTube channel, so [subscribe to my channel](https://www.youtube.com/c/JeffGeerling) so you don't miss out!

## Carlos

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3905s">View this Q&A in the livestream</a>

> What's the best way to get started with contributing to Ansible's codebase?

_Jeff_: The best way is to look in the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html), and more specifically, the 'How can I help?' section. There are many ways to contribute, and not all of them involve submitting code and patches! I got my start building playbooks and sharing some knowledge of Ansible with my co-workers. Then I started helping with local meetups and wrote my book. And it all kind of ballooned from there.

## Alex

> Can you install AWX or Tower on a Raspberry Pi 4?

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3991s">View this Q&A in the livestream</a>

_Jeff_: Good question. In the past the main limitation was that AWX required many gigabytes of RAM to run, and no Pi had that available. The Pi 4 model B changed that, though, and is now available in 4 and 8 GB versions. The current AWX Docker images are not built for `arm64` yet, though, but there's an issue in the AWX repository exploring [AWX ARM64 Support](https://github.com/ansible/awx/issues/7051) that you should follow.

This would be really cool to see happen, because Apple's going to be moving to 64-bit ARM chips too, and the same images would work there. I just did a video on that topic and what I think it means for the wider ARM ecosystem: [What does Apple Silicon mean for the Raspberry Pi and ARM64?](https://www.youtube.com/watch?v=DMUofMagmfc)

## Bruno

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4160s">View this Q&A in the livestream</a>

> How do you integrate Ansible into GitLab CI/CD (or other tools)? Are there any best practices or practical experiences you can share? Do you keep separate dev/test/prod environments? Do you use pipelines for automated testing?

_Jeff_: There is a lot to unpack there! I actually used Ansible with GitLab CI in a previous project to build a large scale static site hosting system inside Kubernetes. The way it worked was Ansible managed the GitLab installation and Kubernetes cluster itself, and inside the GitLab CI job's Docker image, Ansible was installed and moved files into place and configured the built image with Apache 2, then GitLab pushed the new image and triggered a Deployment update in Kubernetes.

I mentioned earlier for any project that affects a business' bottom line, I do use separate dev/stage/prod environments, but for some personal projects, I have a local environment where I do the bulk of my development and testing, then I push to CI (which rebuilds local and runs tests on it), then I deploy the changes to production.

I use many different systems for testing, like Travis CI, GitHub Actions, GitLab CI, and Jenkins, and highly recommend that you at least cover the basics of my [Ansible Testing Spectrum](https://www.youtube.com/watch?v=FaXVZ60o8L8&t=1155s), which I covered in episode 7.

## Srinath

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4303s">View this Q&A in the livestream</a>

> When should you use 'block' and what are some use cases for it? Any practical examples?

_Jeff_: In episode 12, [one of the 'real-world' playbooks I highlighted](https://youtu.be/_QZr4xKhir4?t=1167) was my Midwestern Mac playbook that deploys the Drupal codebase that runs my personal website, [www.jeffgeerling.com](https://www.jeffgeerling.com). I have a `block` named `Drupal 8 post-deploy tasks.` in that example; if you watch the video you can see that the block was used to be able to run a number of tasks inline with one set of conditions applied to it. You may also use blocks when you want to have a set of tasks run with a recoverable failure or rollback, using the `block-rescue-always` pattern of exception handling.

## Razvan

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4357s">View this Q&A in the livestream</a>

> How do you build your own Ansible module?

_Jeff_: That's not something I've covered in Ansible 101, mostly because I think you can be very productive with Ansible without knowing any Python at all, and to illustrate that, my first four years using Ansible I never wrote an Ansible module!

But there is a brief introduction to [building a Test Plugin](https://www.youtube.com/watch?v=nyXDR4RG4A8&t=1201s) in episode 13, so please watch that. And check out the official [Ansible module development: getting started](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html#developing-modules-general) guide.
