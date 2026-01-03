---
nid: 2973
title: "Automatically building and publishing Ansible Galaxy Collections"
slug: "automatically-building-and-publishing-ansible-galaxy-collections"
date: 2020-02-28T17:08:53+00:00
drupal:
  nid: 2973
  path: /blog/2020/automatically-building-and-publishing-ansible-galaxy-collections
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible galaxy
  - ci
  - collections
  - development
  - galaxy
  - travis ci
---

I maintain [a large number of Ansible Galaxy roles](https://galaxy.ansible.com/geerlingguy), and publish hundreds of new releases every year. If the process weren't fully automated, there would be no way I could keep up with it. For Galaxy roles, the process of tagging and publishing a new release is very simple, because Ansible Galaxy ties the role strongly to GitHub's release system. All that's needed is a webhook in your `.travis.yml` file (if using Travis CI):

```
notifications:
  webhooks: https://galaxy.ansible.com/api/v1/notifications/
```

For _collections_, Ansible Galaxy actually hosts an artifact—a .tar.gz file containing the collection contents. This offers some benefits that I won't get into here, but also a challenge: someone has to build and upload that artifact... and that takes more than one or two lines added to a `.travis.yml` file.

Until recently, I had been publishing collection releases manually. The process went something like:

  1. Update `galaxy.yml` manually, making sure the "version" key has the tag I'm planning on pushing.
  2. Push all changes, make sure tests are passing.
  3. Tag a new release (e.g. `1.2.3`), and push it to GitHub.
  4. Run `ansible-galaxy collection build` to build the release artifact (a `.tar.gz` file) in the collection directory.
  5. Make sure the file `~/.ansible/galaxy_token` has my Ansible Galaxy token (for authentication).
  6. Run `ansible-galaxy collection publish ./geerlingguy-php_roles-1.2.3.tar.gz` in the collection directory.

After all that, a new release is ready. Compare that to what I'm used to doing for roles:

    git tag 1.2.3
    git push --tags

The collections process is a lot more involved, to be sure!

## Automating the collection release process

I wanted the workflow to be the same for collections, so I've built a small Ansible [deploy.yml playbook](https://gist.github.com/geerlingguy/fba1809a649acf462b69b3687da8930b) that handles the process for me, and is run only on `tag` builds in Travis CI (other CI systems like GitHub Actions are similar—you would just need to call this playbook in a different place, and only on `tag` builds).

<script src="https://gist.github.com/geerlingguy/fba1809a649acf462b69b3687da8930b.js"></script>

The playbook does the following:

  1. Writes the value of `ANSIBLE_GALAXY_TOKEN` to `~/.ansible/galaxy_token` (the entire pre_tasks section could be dropped if [this Ansible issue is fixed](https://github.com/ansible/ansible/issues/67862).
  2. Writes the `galaxy.yml` file with the new git tag.
  3. Builds the collection artifact.
  4. Publishes the collection artifact.

In my `.travis.yml` file, I added the following to ensure this `deploy.yml` playbook is _only_ run on tag builds:

```
deploy:
  provider: script
  script: ansible-playbook -i 'localhost,' scripts/deploy.yml -e "tag=$TRAVIS_TAG"
  'on':
    tags: true
```

Note that `$TRAVIS_TAG` contains the current tag being built (e.g. `1.2.3`).

You could use this playbook in CI, or if you're going to manually push up a new collection artifact version, it could be used to make that process a little less prone to error.
