---
nid: 2940
title: "Notes from the AnsibleFest Atlanta 2019 Ansible Contributor Summit"
slug: "notes-ansiblefest-atlanta-2019-ansible-contributor-summit"
date: 2019-09-24T14:13:42+00:00
drupal:
  nid: 2940
  path: /blog/2019/notes-ansiblefest-atlanta-2019-ansible-contributor-summit
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansiblefest
  - community
  - contributions
---

This is the third Ansible Contributor Summit I've attended, and the one with by far the most attendees. Contributor Summit is an Ansible community-focused day spent giving Ansible contributors updates on the current status and direction of the Ansible project, as well as an open mic to give feedback to the Ansible core team and other Ansible component teams.

As I have [in the past](/blog/2018/things-i-learned-ansiblefest-austin-2018-contributors-summit), I thought I'd jot down a few notes from the Summit, with things I learned during the day, for the benefit of those who couldn't attend remotely, or don't have the time to watch all the meeting recordings ([see a recap here](https://github.com/ansible/community/issues/449)).

## Ansible Community Data

Greg Sutcliffe ([Gwmngilfen](https://twitter.com/gwmngilfen?lang=en)), a data scientist at Red Hat, presented a number of interesting graphs and charts exploring Ansible community activity. John Barker ([gundalow](https://twitter.com/the_gundalow?lang=en)) mentioned that the ansible/ansible project on GitHub is the #7 most active Git repository on all of GitHub—millions of repos.

The first graph showed a large number of contributors who have interacted with or reviewed more than 15 PRs, and highlighted the 'network' of communications and code reviews in ansible/ansible.

Next we explored a tool Greg built in R to explore the relationship of [open issues vs. interest in and usage of Ansible modules](https://stats.eng.ansible.com/apps/triage/). This graph showed some outliers, like the vmware_guest module, which have a huge number of open issues but seemingly little docs traffic and public repos using it.

{{< figure src="./new-contributor-merge-time.png" alt="New Contributor Merge time graph" width="650" height="264" class="insert-image" >}}

He also showed [per-label merge-time data](https://stats.eng.ansible.com/apps/mergetimes/), and one interesting graph showed the mean time to merge a PR labeled 'new_contributor' was predicted (based on current open and closed PRs) to be _3000 days_. This brings up an interesting question: how can Ansible make new contributors more confident their work will be reviewed and accepted in a more timely fashion?

There was also an [Ansible meetup health graphing app](https://stats.eng.ansible.com/apps/meetups/), which includes a combination map of Meetups + Contributor locations, which is not a perfect representation (since not every contributor on GitHub includes a valid and up-to-date location). An interesting observation from this data is the fact there are countries like Spain with a large amount of contributions, but no Meetup groups. Maybe these places would be good targets for community expansion!

### Resources

  - [Ansible Engineering Stats](https://stats.eng.ansible.com/apps/)
  - [Greg Sutcliffe's website](https://emeraldreverie.org/)

## Ansible Collections (Dylan Silva)

Dylan Silva ([thaumos](https://twitter.com/thaumos?lang=en)) spoke about Ansible Collections, which is the headline new feature going live (out of tech preview) Ansible in 2.9, and will have a large impact on the wider Ansible community.

A number of people in the room knew about Collections, and a small but respectable number of people had actually worked with collections before (during the tech preview).

On the roadmap: Making the `ansible-galaxy collection` command more useful (e.g. adding `provides` to see what's in it).

Some of the contributor summit's initial questions about Collections:

  - _How will we account for Ansible Collection content usage vs what's in Ansible core?_ Greg and the core team will work on making sure the data points (e.g. the statistics shown earlier) will incorporate a wider swath of Ansible content (e.g. Collections).
  - _Will there still be a distribution of Ansible that's 'batteries included'?_ Ansible Galaxy will be the main way to use Collections _a la carte_ ("gotta collect 'em all!"), and in the next session Dylan will run through how things will be broken out by working groups. One advantage to the way Collections work is a Collection can be developed and released independently of the core Ansible release process.
  - _Once something is moved from ansible/ansible into a Collection, will it be removed from ansible/ansible immediately?_ That's a little bit up in the air; right now the idea is that content would be removed in one or two releases. But this is still something under discussion, especially since we want to give people enough time to migrate their playbooks and learn about Collections.
  - _Is anybody scared of Collections?_ Yes.

And later in the day, there was more time for Q&As:

  - _What is the timeline for more role support in Collections, e.g. role dependencies, better role support in testing, etc._ The first focus for Collections is plugins and modules (because major Ansible contribution and support issues currently revolve around them). Collections can include roles currently, but the initial focus has not been on role usage.
  - _How will users know when a module they're using is moving to a Collection?_ In Ansible 2.9, there's no mechanism to throw a Deprecation Warning if someone uses a module which is moved into a Collection. Hopefully this mechanism will exist in 2.10 so users will know when to make the switch.
  - _Is the AWX/Tower team on board with Collections?_ Collections are a big thing for Tower, definitely supported. There will be sessions both in the afternoon and during AnsibleFest proper which discuss Tower support for Collections.

### Core / Community Split

The current idea is there will be one GitHub repository for all community collections (multiple collections in one repository), to help split the management of community content from ansible/ansible and keep it maintainable.

Long term, this repository could be split up; it's generally preferred to have on repository per Collection.

Ansible 2.10 will not contain any _new_ community plugins or modules; they would instead go into this new GitHub repository.

Individual working group community leads will likely be given more rights to this new community collections repository, and Ansibot will likely be involved to some extent. Everything in this collection will be under the Ansible namespace (in GitHub and on Galaxy), but will be identified as 'community' content.

Some of the contributor summit's questions surrounding the community Collections split:

  - _For partners and other orgs, can they start developing outside of GitHub?_ Yes; one of the nice things about Collections is the fact that they are released as tarballs, so the source repository can be elsewhere (not just GitHub).
  - _How will open source licensing affect Collection content?_ Collections will allow for different licenses to be used with different content. There are open questions about the implications.
  - _What will be the release cycle, process, and documentation for Community Collections?_ This is still TBD. It will likely be released _more frequently_ than Ansible Core. For other Collections it will be up to the maintainer.
    - Documentation from Community Collections will flow back into Ansible's core documentation ([docs.ansible.com](https://docs.ansible.com)).
    - At some point, Galaxy will also display documentation for Collections (all Collections).
    - Alicia Cozine ([acozine](https://github.com/acozine)) mentioned that any documentation that _does_ move would be redirected from the core docs site.
    - The migration will _not_ be considered complete until all the documentation issues are resolved.
  - _What happens with modules like AWS modules, which rely on central libraries, where some are core and some are community?_ (Dylan did a little dance) The AWS modules are a special case, and things will likely evolve a bit as modules are moved out of core.

One thing that's a core focus is to ensure playbooks don't have to be rewritten to be Collection-aware for some amount of time. This is a major concern from the community, and we want to avoid rework. For the forseeable future, there will be a way to get a 'batteries included' version of Ansible.

Collections are namespaced, and the directory structure (inside `$ANSIBLE_COLLECTIONS_PATHS`) always has an `ansible_collections` subdirectory. The reason for this is the Python namespacing standard—all Collection modules are able to interoperate with all the Python community tooling.

## Ansible Galaxy (Chris Housenecht)

  - Galaxy 3.x was released in May 2019.
  - Major focus was support for the first iteration of Ansible Collections (there are currently 65 published collections).
  - Focus will be going back to community Galaxy development again soon, as well as the Collections workflow.
  - Concerns:
    - Roles have been pushed down in search results, which is a bit annoying, since roles are currently the most mature community content available for Ansible.
    - How can we make the UI for collection discovery as useful as it is for roles?

## `ansible-test` (Dylan Silva)

  - `ansible-test` is the main tool used in core testing (focused on modules and plugins).
  - A lot of effort will be spent on getting `ansible-test`, `ansible-lint`, and `molecule` to a good place.
    - `ansible-test` has had a lot of polish in the 2.9 release, so please check it out and see what can be improved.

## Ansible Community Breakout

### Community Collections Discussion

In the past, Ansible did try a module split, with `ansible-modules-core` and `ansible-modules-extras`, but after a lot of missteps, that split was undone and everything went back into `ansible/ansible`.

For this 'Collections split', there is still active discussion around the exact methods and timeline. We spent some time discussing pros and cons of moving things into one massive 'community collections' repository, vs. the other extreme of moving every single sub-directory (e.g. `aws`, `mysql`, etc.) into its own separate repository.

One difficulty of slowly moving modules out of Ansible core is that so many modules currently in core depend on module libraries that would require a strange and difficult-to-maintain dependency tree.

### ansible/ansible Backlog Management

The backlog has been growing at an increasing rate over time (see [this interactive graph](http://dash.tannerjc.net/graph)), and the core team can't keep up with the rate of open issues. Triage can deal with ~10 per meeting. PR-focused full day meetings can deal with maybe ~60 in a day.

Moving things out into Collections may alleviate some of this load, or may not. We may also see about having the Ansible bot auto-close issues after X days (see issue: [auto-close "rotten" issues per fejta-bot k8s example](https://github.com/ansible/ansibullbot/issues/1011)).

Using the current data and projections, it is estimated at least 6 more full-time core developers would be needed just to tread water with the current rate of opened issues and PRs in ansible/ansible.
