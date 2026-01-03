---
nid: 2933
title: "How to add integration tests to an Ansible collection with Molecule"
slug: "how-add-integration-tests-ansible-collection-molecule"
date: 2019-08-20T13:16:41+00:00
drupal:
  nid: 2933
  path: /blog/2019/how-add-integration-tests-ansible-collection-molecule
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible-test
  - collections
  - molecule
  - testing
---

> **Note**: Ansible Collections are currently in tech preview. The details of this blog post may be outdated by the time you read this, though I will try to keep things updated if possible.

Ansible 2.8 and 2.9 introduced a new type of Ansible content, a 'Collection'. **Collections are still in tech preview state**, so things are prone to change.

Ansible Collections must be in a very specific path, like `{...}/ansible_collections/{namespace}/{collection}/`

You have to make sure your collection is in that specific path—with an empty directory named `ansible_collections`, then a directory for the `namespace`, and finally a directory for the `collection` itself. I opened an issue in the Ansible issue queue asking if `ansible-test` can [allow running tests in an arbitrary collection directory](https://github.com/ansible/ansible/issues/60215), and for Molecule itself, there's more of a 'meta' issue, [Molecule and Ansible Collections](https://github.com/ansible/molecule/issues/2165).

> Note: Some of the features in this blog post require Ansible 2.9, which was released in October 2019. Please make sure you're running Ansible 2.9 or later for full collection support.

## Creating a new Collection

Currently, Molecule doesn't know much about collections, so you should not use the `molecule init` command to create a collection (that only creates roles currently).

Instead, you should use the `ansible-galaxy` command to create a collection (ideally, inside the directory `~/.ansible/collections/ansible_collections/` so Ansible can pick it up automatically):

    $ ansible-galaxy collection init geerlingguy.testing

Ansible creates the collection in the directory `./geerlingguy/testing`, so change into that directory:

    $ cd geerlingguy/testing
    $ ls
    README.md  docs       galaxy.yml plugins    roles

The `galaxy.yml` file contains important metadata used by the Ansible Galaxy importer, so you should make sure all the information inside is correct (it comes with a bunch of helpful comments). Other than that, you have an empty scaffold of a collection, ready for development.

## Adding a basic module

Create a `modules` directory inside `plugins`:

    $ mkdir plugins/modules

Create a module named `my_test.py` in the new modules directory:

    $ touch plugins/modules/my_test.py

And then paste the contents of the [example module](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html#starting-a-new-module) in the Ansible module development documentation into this file.

At this point, your Collection includes an Ansible module called `my_test`, which can be used in an Ansible playbook like:

```
---
- hosts: all

  collections:
  - geerlingguy.testing

  tasks:
  - name: Test the my_test module.
    my_test:
      name: 'hello'
      new: true
    register: testout
  - name: Debug the my_test module's output
    debug:
      msg: '{{ testout }}'
```

Next, we want to be able to both test this module (e.g. for a Continuous Integration (CI) workflow), and have a clean local development environment where we can quickly test changes or bug fixes for this module. Molecule provides both!

## Adding Molecule to the Collection

> Note: If you don't have molecule installed already, run `pip install molecule docker` to install it and the python library for Docker.

Molecule doesn't support `init` for collections yet, but it does allow you to add a Molecule configuration to an existing role or collection, using `molecule init scenario`. So we want to add a default testing scenario to our testing project. Run the following command in the collection project root directory:

    $ molecule init scenario --scenario-name default

(The `--scenario-name` is not strictly required if you're adding the `default` scenario, but I like adding it for completeness.)

Now you should have a `.yamllint` file and `molecule/` directory in your collection. What happens if we run `molecule test` right now?

    $ molecule test
    ...
    An error occurred during the test sequence action: 'lint'. Cleaning up.

Oops! You can quickly fix those errors in the `galaxy.yml` file (I opened an issue to see if we can make the default file pass yamllint: [ansible-galaxy collection init generates galaxy.yml that fails YAMLlint](https://github.com/ansible/ansible/issues/60909), too). There will also be errors with the default Testinfra tests inside `molecule/default/tests`, so go ahead and delete that directory too. Now try testing again:

```
$ molecule test
--> Scenario: 'default'
--> Action: 'converge'
    
    PLAY [Converge] ****************************************************************
    
    TASK [Gathering Facts] *********************************************************
    ok: [instance]
    
    PLAY RECAP *********************************************************************
    instance                   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
    
--> Scenario: 'default'
--> Action: 'idempotence'
Idempotence completed successfully.
...
```

Yay, the test was successful! So you now have an isolated test environment, and you can also use it for live development, by running `molecule converge`, it will run through all the same steps, but stop after the `converge` action, at which point you can make changes to your collection or the Converge play, and then run `molecule converge` again (and again) until you're done with your development work.

## Testing the `geerlingguy.testing.my_test` module

The `molecule test` command worked... but so far it's not really testing anything (besides a basic linting of the collection's YAML files). We should merge the tests from the example playbook earlier in this post with the 'Converge' playbook that molecule added, so now the `molecule/default/playbook.yml` playbook should look like:

```
---
- name: Converge
  hosts: all

  collections:
  - geerlingguy.testing

  tasks:
  - name: Test the my_test module.
    my_test:
      name: 'hello'
      new: true
    register: testout

  - name: Debug the my_test module's output
    debug:
      msg: '{{ testout }}'
```

This time, after you run `molecule converge`, you should see:

```
--> Scenario: 'default'
--> Action: 'converge'
    
    PLAY [Converge] ****************************************************************
    
    TASK [Gathering Facts] *********************************************************
    ok: [instance]
    
    TASK [Test the my_test module.] ************************************************
    changed: [instance]
    
    TASK [Debug the my_test module's output] ***************************************
    ok: [instance] => {
        "msg": {
            "changed": true, 
            "failed": false, 
            "message": "goodbye", 
            "original_message": "hello"
        }
    }
    
    PLAY RECAP *********************************************************************
    instance                   : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Excellent! Now, to take it a step further, we'll use Ansible's `assert` module to verify the my_test module is performing as expected. Change the last task in the molecule `playbook.yml` to:

```
  - name: Validate the my_test module's output
    assert:
      that:
        - testout.original_message == 'hello'
        - testout.message == 'goodbye'
```

After you run `molecule converge` again, you should see:

```
    TASK [Validate the my_test module's output] ************************************
    ok: [instance] => {
        "changed": false, 
        "msg": "All assertions passed"
    }
```

Great! At this point, you could continue doing development work on your custom module (or other roles and plugins in the collection), you can add scenarios to your molecule configuration, and you can develop and test locally to your heart's content!

## Running Molecule in CI

Locally, everything seems to work great! But what about a Continuous Integration (CI) environment like Travis CI, Circle CI, or Jenkins? In these environments, you'd typically do a `git clone` (or the CI tool does it for you) into a 'workspace'. The problem is, Ansible requires a strict directory path format and location for collections. Because of this, we need to do do two things:

### Moving things around

The first step is to move the checked out collection project into a folder Ansible can use for your collection. For my [k8s collection](https://github.com/geerlingguy/ansible-collection-k8s), I have the following defined in my Travisfile:

```
env:
  global:
    - COLLECTION_NAMESPACE: geerlingguy
    - COLLECTION_NAME: k8s

before_script:
  # Move the collection into the required path.
  - cd ../
  - mkdir -p ansible_collections/$COLLECTION_NAMESPACE
  - mv ansible-collection-$COLLECTION_NAME ansible_collections/$COLLECTION_NAMESPACE/$COLLECTION_NAME
  - cd ansible_collections/$COLLECTION_NAMESPACE/$COLLECTION_NAME
```

This changes the working directory _out of_ the checked out collection project, then creates the required collection pathing, and moves the collection into the properly-named directory (`ansible_collections/geerlingguy/k8s`).

Once that's done, Molecule also needs to set the environment properly so Ansible playbooks it runs pick up the collections. So in the project's `molecule.yml`, I added:

```
provisioner:
  ...
  env:
    ANSIBLE_COLLECTIONS_PATHS: "/home/travis/build/geerlingguy:~/.ansible/collections"
```

This adds the path to the Travis CI `$HOME` directory where I created that `ansible_collections` folder structure. Now, Ansible can easily pick up the collection for use in Molecule tests.

## Final optimizations

If you don't want to waste a ton of CPU cycles building and rebuilding the test environment Docker container, I'd also recommend nixing the default Docker image that Molecule supplies, and instead using one of your own (or one of mine :).

Change the `platforms` section in `molecule.yml` to something like the following:

```
platforms:
  - name: instance
    image: geerlingguy/docker-centos7-ansible:latest
    privileged: true
    pre_build_image: true
```

Then delete the 'Dockerfile' that was created by Molecule. Now your uncached builds should all be a slight bit faster!
