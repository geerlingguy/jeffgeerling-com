---
nid: 2931
title: "How to add integration tests to an Ansible Collection with ansible-test"
slug: "how-add-integration-tests-ansible-collection-ansible-test"
date: 2019-08-07T21:39:25+00:00
drupal:
  nid: 2931
  path: /blog/2019/how-add-integration-tests-ansible-collection-ansible-test
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible-test
  - collections
  - testing
---

> **Note**: Ansible Collections are currently in tech preview. The details of this blog post may be outdated by the time you read this, though I will try to keep things updated if possible.

Ansible 2.8 and 2.9 introduced a new type of Ansible content, a 'Collection'. **Collections are still in tech preview state**, so things are prone to change, but one thing that the Ansible team has been working on is improving `ansible-test` to be able to test modules, plugins, and roles in Collections (previously it was only used for testing Ansible core).

`ansible-test` currently requires your Collection be in a very specific path, either:

  - Inside the current Ansible source tree (e.g. if you're developing against Ansible core)
  - Inside a specific collection heirarchy path, like `{...}/ansible_collections/{namespace}/{collection}/`

You have to make sure your collection is in that specific path—with an empty directory named `ansible_collections`, then a directory for the `namespace`, and finally a directory for the `collection` itself. I opened an issue in the Ansible issue queue asking if maybe `ansible-test` can be a little more lenient and [allow running tests in an arbitrary collection directory](https://github.com/ansible/ansible/issues/60215), since not everyone likes cloning into extremely rigid directory structures.

Once you have the collection in the right path, you can run:

    ansible-test integration --docker ubuntu1804

I always use the `--docker` option and specify a particular OS, that way I can be sure the tests are running inside a clean, ephemeral environment (and not locally in my workspace). Ansible's [official maintained container OS images for `ansible-test`](https://docs.ansible.com/ansible/latest/dev_guide/testing_integration.html#container-images) are listed in the documentation, but you can also use a custom image by specifying it directly, e.g. `ansible-test integration --docker geerlingguy/docker-ubuntu1804-ansible`

> If you're using a local image or otherwise don't want to try pulling the image from a remote repository, also pass the `--docker-no-pull` option.

## Creating an integration test

`ansible-test` also requires tests be in a specific directory structure in order for them to be picked up. You must put all test code inside a directory named `tests` in the root of your Collection (I opened a feature request to [see if the directory naming can be relaxed](https://github.com/ansible/ansible/issues/60218), too). Then integration tests go inside `tests/integration`.

You can have one or more test 'targets' (e.g. one target for each role, module, or plugin in your Collection, or one target for one kind of integration test, and another for a different kind), each one inside a `targets` directory. In my case, I'm testing the [geerlingguy.php_roles](https://github.com/geerlingguy/ansible-collection-php_roles) Collection, so I want an integration test for the `php` role, to make sure it works. I'll create the directory structure:

    tests/
      integration/
        targets/
          php/

This `php` directory will be run as a role against the test environment—as will any other directory placed inside `targets`.

> **Note**: Currently, `ansible-test` will run every role/target, in succession, against the same test environment container; so things changed by the first target would affect the second target's environment. I opened an issue asking if there could be a way to [provide a clean environment for each integration test](https://github.com/ansible/ansible/issues/60219) (something Molecule can do currently), but for now, keep this in mind as you need to do manual cleanup between roles if you want to run them all in one suite.

As with any Ansible role, the minimum requirement is a `tasks/main.yml` file, which will be run as a normal included Ansible task file. In this task file, you can do anything you normally would do with ansible, like include a role, use modules to test certain conditions, call an API, etc.

To verify your tests are working, add a task in `tasks/main.yml` like:

```
- name: Debug test.
  debug: msg="Testing 1, 2, 3."
```

Then when you run ansible-test you should get something like:

```
$ ansible-test integration --docker ubuntu1804
...
Running php_role_test integration test role

PLAY [testhost] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [testhost]

TASK [php_role_test : Debug test.] *********************************************
ok: [testhost] => {
    "msg": "Testing 1, 2, 3."
}

PLAY RECAP *********************************************************************
testhost                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

If you want the integration test to run a role in your collection, be sure to use the entire role path with namespace:

```
- include_role:
    name: geerlingguy.php_roles.php
```

> **Note**: Currently, the only way to use collection or role dependencies inside the docker test container is by installing them manually, directly inside your collection's directories, before running `ansible-test`. There is an open issue to get this resolved so collection dependencies can work correctly with `ansible-test --docker`: [Support testing collections with deps using --docker](https://github.com/ansible/ansible/issues/59563).

> **Additional Note**: Currently, the only way to test for role _idempotence_ (that is, if you run it multiple times, it only makes changes the first time, and just ensures state in follow-up runs) is to build your own checks in a `runme.sh` shell script. See the following issue for progress in making idempotence testing easier: [ansible-test idempotence tests for roles in Ansible Collections](https://github.com/ansible/ansible/issues/60226).

For right now, I'd recommend sticking with Molecule for role testing, and using `ansible-test` more for module and plugin testing. I believe the long-term goal is to make it so Molecule can (if desired) be used as a more developer-friendly frontend to the `ansible-test` tool, but a lot of these things are still moving parts, as noted in the beginning of this post.
