---
nid: 2969
title: "Collections signal major shift in Ansible ecosystem"
slug: "collections-signal-major-shift-ansible-ecosystem"
date: 2020-02-21T14:53:18+00:00
drupal:
  nid: 2969
  path: /blog/2020/collections-signal-major-shift-ansible-ecosystem
  body_format: markdown
  redirects:
    - /blog/2020/ansible-210-will-restructure-project-collections
aliases:
  - /blog/2020/ansible-210-will-restructure-project-collections
tags:
  - ansible
  - ansible galaxy
  - architecture
  - collections
  - community
  - open source
---

Every successful software project I've worked on reaches a point where architectural changes need to be made to ensure the project's continued success. I've been involved in the Drupal community for over a decade, and [have written about the successes and failures](/blog/2019/drupal-8-successes-and-failures) resulting from a major rearchitecture in version 8. Apple's Macintosh OS had [two](https://en.wikipedia.org/wiki/Taligent) [major](https://en.wikipedia.org/wiki/Copland_(operating_system)) failed rewrites which were ultimately scrapped as Apple moved on to Mac OS X.

It's a common theme, and because change is hard, the first response to a major shift in a software project is often negative. Distrust over the project's stewards, or anger about a voice not being heard are two common themes. Even though it has nothing to do with the change (which was being discussed 3 years ago), the [acquisition of Red Hat by IBM](https://www.redhat.com/en/about/press-releases/ibm-closes-landmark-acquisition-red-hat-34-billion-defines-open-hybrid-cloud-future) last year didn't do anything to assuage conspiracy theorists!

{{< figure src="./batteries-included-energizer-rechargeable.jpeg" alt="Rechargeable batteries included energizer" width="390" height="310" class="insert-image" >}}

With Ansible, 'batteries included' has been one of the major selling points since day one. The phrase means "everything you need to start using Ansible is included, from the moment you install it."

So when the Ansible team at Red Hat started presenting the idea of separating the 'batteries' (thousands of contributed modules) from the 'base', it was no surprise there was unrest.

In the [Ansible Collections Overview](https://github.com/ansible-collections/overview) (which was sent out to the community yesterday), some questions are answered, including the [reasons for the change](https://github.com/ansible-collections/overview#where-we-ve-come-from-and-where-we-are-going) and a [timeline](https://github.com/ansible-collections/overview#timeline) for the changes. But there are still some open questions and issues which will need to be worked out between now and Ansible 2.10's release.

I've been fortunate to be working closely with the team at Red Hat for some time, and I have been able to spend a good amount of time working with Collections, Ansible Galaxy, and the new `ansible-base` version of Ansible which has all the batteries pulled out, and I have a lot of good news to report, though I still have some concerns.

## You might only need ansible-base

One of the first things I did when I heard that Ansible would split off all the modules into separate Collections was see what essential modules are still included in the trimmed-down Ansible release. The current (in development—subject to change) version of the new 'base Ansible' is available here: [https://github.com/ansible-collection-migration/ansible-base](https://github.com/ansible-collection-migration/ansible-base), and if you want, you can uninstall Ansible on your system, and install the latest development version of ansible's base with Pip, straight from GitHub:

    pip3 install git+https://github.com/ansible/ansible

(You can then uninstall with `pip3 uninstall ansible`, and reinstall a stable version of Ansible again once you're finished testing.)

Looking through my playbooks and roles, the _majority_ of them actually work with just the minimal version of Ansible. This is good news, because it means the modules I commonly use (like `file`, `copy`, `template`, `package`, `apt`, `yum`, `command`, etc.) are all supported by the core development team, and they will never require any extra steps to make them available to my playbooks. (You can see the full list of modules that will remain in Ansible's base version under `core` in [this collection migration scenario file](https://github.com/ansible-community/collection_migration/blob/master/scenarios/nwo/ansible.yml#L78) (**note**: subject to change).

Note that there _are_ some very useful things that would be moved out of ansible-base according to this scenario, like the `yaml` callback plugin ([which I wrote about in an earlier post](/blog/2018/use-ansibles-yaml-callback-plugin-better-cli-experience)). If you only install `ansible-base`, but want something like that callback plugin, you would need to do the following:

  1. Install the `community.general` collection from Ansible Galaxy.
  2. Specify the YAML callback using the Fully Qualified Collection Namespace in your Ansible config (e.g. `community.general.yaml` instead of just `yaml`), like so:

         [defaults]
         stdout_callback = community.general.yaml

## Ansible is still batteries-included (to some extent)

[According to the FAQ](https://github.com/ansible-collections/overview#id14):

> For users of the community version of ansible, `pip install ansible` or `apt install ansible` will continue to give you a working install of Ansible including the three thousand plus modules [that were in 2.9 and earlier].

I believe the exact details of the full batteries-included Ansible 'community' distribution are still being worked out, but the idea is that any playbook that runs with Ansible 2.9 _should_ work with Ansible 2.10, with either no changes, or minimal changes (maybe adding a couple lines at the top of the playbook) required.

If you use Ansible as part of the 'Red Hat Ansible Automation Platform', then the way Ansible is packaged up and included in Ansible Tower may require some changes, but again, I think the exact details are being worked out. One major benefit to this change is that it is going to be much easier to determine what Ansible content (modules, plugins, roles, etc.) are officially supported if you use the Red Hat Ansible Automation Platform and pay for support, verses what content is maintained and supported by the wider open source community.

<p style="text-align: center;">{{< figure src="./issue-authors-per-month.png" alt="Issue authors per month in ansible/ansible repo" width="650" height="255" class="insert-image" >}}<br>
<em>Unique ansible/ansible issue authors per month; chart by <a href="https://twitter.com/Gwmngilfen">@Gwmngilfen</a>.</em>
</p>

Ansible was an outlier from most other open source projects in storing all contributed content in one giant repository. It has been a grand experiment, but ultimately a giant open source monorepo was too burdensome to maintain. Most open source software has a 'core' component (even if it ships with a number of modules or plugins), and then can be extended with code managed by others. Ansible sort-of had this functionality via roles on [Ansible Galaxy](https://galaxy.ansible.com) (since 2014), but that setup had its flaws, and most extensions went directly into the main ansible/ansible repo. Using Collections will hopefully split the code maintenance burden in a way that is more sustainable.

## There be dragons

As I mentioned at the beginning of this post, a major shift in architecture is never easy. Some projects pull it off, and some don't.

I think in Ansible's case, the worst case scenario is maintaining the status quo: a huge community of users automating infrastructure with the simple, flexible tool that is Ansible, but with much less accelerated growth (Ansible has been on a tear for a long time, and this growth has been a blessing and a curse). This shift is (at least, in the short term) more a matter of moving code around and less a matter of rearchitecting the _way it actually works_.

The best case scenario is Ansible's 'core' dev team is freed from the shackles of having to deal with thousands of issues and PRs for thousands of components they can't even test (so they can make Ansible's core software better, faster), and the community contributors are able to maintain their own subsets of modules and plugins with less friction, because there's not one giant repo and a relatively small team of people who are able to merge PRs (or worse, let them fester for months or years).

In either case, the shift to Collections exposes some of the hidden technical debt that's been lurking in the Ansible ecosystem—there are many modules in Ansible's repository that are minimally maintained (or even broken!) with nobody willing to fix them. As I've already seen with the [Kubernetes Collection](/blog/2020/kubernetes-collection-ansible), separating modules from the base repository means it's easier to build and test them, and to get people to maintain them.

I'm excited about what the future holds, but I'm still holding my breath as a shift this large requires a lot of testing and exposes many loose ends. Whether the loose ends will be tied up by the time Ansible 2.10 is released is up to all of us, so start testing, and maybe consider helping maintain some of the community modules you use!
