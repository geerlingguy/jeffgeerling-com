---
nid: 2879
title: "Testing your Ansible roles with Molecule"
slug: "testing-your-ansible-roles-molecule"
date: 2018-10-25T15:10:11+00:00
drupal:
  nid: 2879
  path: /blog/2018/testing-your-ansible-roles-molecule
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible lint
  - ci
  - code quality
  - lint
  - molecule
  - testing
  - travis ci
---

After the announcement on September 26 that [Ansible will be adopting molecule and ansible-lint](https://groups.google.com/forum/#!topic/ansible-project/ehrb6AEptzA) as official 'Ansible by Red Hat' projects, I started moving more of my public Ansible projects over to Molecule-based tests instead of using the [homegrown Docker-based Ansible testing rig](/blog/2018/how-i-test-ansible-configuration-on-7-different-oses-docker) I'd been using for a few years.

{{< figure src="./molecule-sticker.jpg" alt="Molecule sticker in front of AnsibleFest 2018 Sticker" width="650" height="421" class="insert-image" >}}

There was also a bit of motivation from readers of [Ansible for DevOps](https://www.ansiblefordevops.com), many of whom have asked for a new section on Molecule specifically!

In this blog post, I'll walk you through how to use Molecule, and how I converted all my existing roles (which were using a different testing system) to use Molecule and Ansible Lint-based tests.

## Installing Molecule

Assuming you have `pip` installed, Installing Molecule is quite easy:

    pip install molecule

Check if it's working:

    $ molecule --version
    molecule, version 2.19.0

## Initializing a new role with Molecule

Before we start integrating Molecule into an _existing_ role, let's take a look at the 'happy path'—using Molecule itself to `init` a new role:

    molecule init role geerlingguy.example -d docker

This command uses `ansible-galaxy` behind the scenes to generate a new Ansible role, then it injects a `molecule` directory in the role, and sets it up to run builds and test runs in a `docker` environment. Inside the Molecule directory is a `default` directory, indicating the `default` test scenario. It contains the following:

    $ cd geerlingguy.example/molecule/default/ && ls
    Dockerfile.j2
    INSTALL.rst
    molecule.yml
    playbook.yml
    tests

Here's a quick rundown of what all these files are:

  - `Dockerfile.j2`: This is the Dockerfile used to build the Docker container used as a test environment for your role. You can customize it to your heart's content, and you can even use your own Docker image instead of building the container from scratch every time—I'll cover how to do that later though. The key is this makes sure important dependencies like Python, `sudo`, and Bash are available inside the build/test environment.
  - `INSTALL.rst`: Contains instructions for installing required dependencies for running `molecule` tests.
  - `molecule.yml`: Tells molecule everything it needs to know about your testing: what OS to use, how to lint your role, how to test your role, etc. We'll cover a little more on this later.
  - `playbook.yml`: This is the playbook Molecule uses to test your role. For simpler roles, you can usually leave it as-is (it will just run your role and nothing else). But for more complex roles, you might need to do some additional setup, or run other roles prior to running your role.
  - `tests/`: This directory contains a basic [Testinfra](https://testinfra.readthedocs.io/en/latest/) test, which you can expand on if you want to run additional verification of your build environment state _after_ Ansible's done its thing.

You can customize and/or remove pretty much everything. In many of my roles, I use a custom pre-made Docker image which already has Python and Ansible, so I removed the `Dockerfile.j2` template, and updated the `image` in my `molecule.yml` to point to [my public Docker Hub images](https://hub.docker.com/u/geerlingguy/). You can also use environment variables anywhere inside the `molecule.yml` file, so you could have an environment variable like `MOLECULE_IMAGE` and specify a different OS base image whenever you do a test run, without adding additional scenarios (besides `default`).

I also use Ansible itself (usually the `uri`, `assert`, and `fail` modules mostly) to do functional tests after the `playbook.yml` runs, so I delete the `tests/` directory, and Molecule automatically detects there are no `test infra` tests to run.

### Running your first Molecule test

Your new example role doesn't have anything exciting in it yet, but it should—at this point—pass all tests with flying colors! So let's let Molecule do its thing:

    $ cd ../../
    $ molecule test
    ...
    --> Validating schema /Users/jgeerling/Downloads/geerlingguy.example/molecule/default/molecule.yml.
    Validation completed successfully.
    --> Test matrix
        
    └── default
        ├── lint
        ├── destroy
        ├── dependency
        ├── syntax
        ├── create
        ├── prepare
        ├── converge
        ├── idempotence
        ├── side_effect
        ├── verify
        └── destroy

    --> Executing Yamllint on files found in /Users/jgeerling/Downloads/geerlingguy.example/...
    Lint completed successfully.
    --> Action: 'syntax'
        playbook: /Users/jgeerling/Downloads/geerlingguy.example/molecule/default/playbook.yml        
    --> Action: 'converge'
    --> Action: 'idempotence'
    Idempotence completed successfully.
    ...

After a couple minutes, Molecule runs through all the testing steps: linting, checking playbook syntax, building the Docker environment, running the playbook in the Docker environment, running the playbook again to verify idempotence, then cleaning up after itself.

This is great! You can work on the role, and then whenever you want, run `molecule test` and verify everything still passes.

But what about development? Molecule is actually great for that too!

## Role development with Molecule

I used to use [this Ansible role testing 'shim' script](https://gist.github.com/geerlingguy/73ef1e5ee45d8694570f334be385e181) to do lightweight development of my roles, but it was a little bit of a hassle using it, and I didn't have a quick "build me a local environment to work in and leave it running" mode, without setting some extra environment variables.

With Molecule, any time you want to bring up a local environment and start running your role, you just run `molecule converge`. And since you can use Molecule with VirtualBox, Docker, or even AWS EC2 instances, you can have your role run inside any type of virtual environment you need! (Sometimes it can be hard to test certain types of applications or automation inside of a Docker container).

So my new process for developing a role (either a new one, or when fixing or improving an existing role) is:

    molecule init role geerlingguy.example -d docker
    molecule converge
    <do some work on the role>
    molecule converge
    <see that some changes didn't work>
    molecule converge
    <see everything working well, commit my changes>
    molecule converge
    <idempotence check - make sure Ansible doesn't report any changes on a second run>
    molecule destroy

It's a lot more fun and painless to work on my roles when I can _very_ quickly get a local development environment up and running, and easily re-run my role against that environment over and over. The faster I can make that feedback cycle (make a change, see if it worked, make another change...), the more—and higher quality—work I can get done.

The `converge` command is even faster after the first time it's run, as the container already exists and doesn't have to be created again.

Also, when I get a build failure notification from Travis CI, I can just `cd` into the role directory, run `molecule test`, and quickly see if the problem can be replicated locally. I used to have to set a few environment variables (which I would always forget) to reproduce the failing test locally, but now I have a more efficient—and easy to install, via `pip install molecule`—option.

## Configure Molecule

If you've been working through the examples in this blog post, you'll notice Molecule puts out a lot of notices about skipped steps, like:

```
--> Action: 'dependency'
Skipping, missing the requirements file.
--> Scenario: 'default'
--> Action: 'create'
Skipping, instances already created.
--> Scenario: 'default'
--> Action: 'prepare'
Skipping, prepare playbook not configured.
```

What if you want to customize the order of tasks run when you run `molecule test`? Or if you need to remove a step (e.g. for some very specialized use cases, you don't want to verify idempotence—the playbook is supposed to make a change on every run)?

The order of `scenario`s (in Molecule's terms) can be modified, along with just about everything else, in the `molecule.yml` file.

For the example above, since we don't need to install any dependencies or run a preparatory playbook, we can take those out by adding the following configuration, under the `scenario` top level configuration. Here's the default set of scenarios as of Molecule 2.19:

```
scenario:
  name: default
  test_sequence:
    - lint
    - destroy
    - dependency
    - syntax
    - create
    - prepare
    - converge
    - idempotence
    - side_effect
    - verify
    - destroy
```

Since we don't need certain steps, we can comment out:

  - `dependency`: If this role required other roles, we could add a `requirements.yml` file in the `default` scenario directory, and Molecule would install them in this step. But we don't have any requirements for this role.
  - `prepare`: You can create a `prepare.yml` playbook in the `default` scenario directory and have Molecule run it during the `prepare` step, but we don't need one for this role.
  - `side_effect`: You can create a `side_effect.yml` playbook in the `default` scenario directory and have Molecule run it during the `prepare` step, but we don't need one for this role.

So now our `scenario` definition looks like:

```
scenario:
  name: default
  test_sequence:
    - lint
    - destroy
    # - dependency
    - syntax
    - create
    # - prepare
    - converge
    - idempotence
    # - side_effect
    - verify
    - destroy
```

And if we run `molecule test`, we won't see all the notices about skipped actions, because they're not in the `test_sequence`.

There are many other things you can configure in `molecule.yml`; in fact, pretty much every setting and option in Molecule is configurable or overridable. See the [Molecule configuration documentation](https://molecule.readthedocs.io/en/latest/configuration.html) for all the gory details.

## Use pre-built Docker images with Molecule

Speaking of things you can configure in `molecule.yml`—if you want to speed up your test runs (especially in ephemeral CI environments), you can swap out the default Docker build configuration for your own Docker image, and tell Molecule you've already configured the image with Ansible.

And wouldn't you know, I already maintain a number of base Docker images with Ansible pre-installed, for most popular Linux distributions:

  - [Ubuntu 18.04](https://hub.docker.com/r/geerlingguy/docker-ubuntu1804-ansible/)
  - [Ubuntu 16.04](https://hub.docker.com/r/geerlingguy/docker-ubuntu1604-ansible/)
  - [Ubuntu 14.04](https://hub.docker.com/r/geerlingguy/docker-ubuntu1404-ansible/)
  - [CentOS 7](https://hub.docker.com/r/geerlingguy/docker-centos7-ansible/)
  - [CentOS 6](https://hub.docker.com/r/geerlingguy/docker-centos6-ansible/)
  - [Debian 9](https://hub.docker.com/r/geerlingguy/docker-debian9-ansible/)
  - [Debian 8](https://hub.docker.com/r/geerlingguy/docker-debian8-ansible/)
  - [Fedora 29](https://hub.docker.com/r/geerlingguy/docker-fedora29-ansible/)
  - [Fedora 27](https://hub.docker.com/r/geerlingguy/docker-fedora27-ansible/)

All of the above base images have not only Ansible, but also systemd (or sysvinit in older Ubuntu and CentOS releases), so you can test `service` management, and pretty much anything you'd be able to test in a full-fledged virtual machine.

To use those images, I customize my `molecule.yml` file's `platforms` configuration a bit:

```
platforms:
  - name: instance
    image: "geerlingguy/docker-${MOLECULE_DISTRO:-centos7}-ansible:latest"
    command: ${MOLECULE_DOCKER_COMMAND:-""}
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:ro
    privileged: true
    pre_build_image: true
```

Many of the options, like `volumes`, `command`, `image`, and `privileged` are passed through exactly like you'd expect from a Docker Compose file, or in the Ansible docker_container module's parameters. The special `pre_build_image` option, when set to `true`, means that the image you're using already has Ansible inside, so Molecule doesn't need to waste time building it if the image doesn't exist locally.

You might also notice my use of variables like `${MOLECULE_DISTRO:-centos7}`; Molecule conveniently supports environment variables inside the `molecule.yml` file, and you can even provide defaults like I have with the `:-centos7` syntax (this means that if `MOLECULE_DISTRO` is an empty string or not set, it will default to `centos7`).

So when I run `molecule` commands, I can run them with whatever OS I like, for example:

    MOLECULE_DISTRO=ubuntu1804 molecule test

This will run the test suite inside an Ubuntu 18.04 environment. If I don't set `MOLECULE_DISTRO`, it will run inside a CentOS 7 environment.

I also use use `volumes` to mount `/sys/fs/cgroup` inside the image, and set the `--privileged` flag, because without these, `systemd` won't run correctly inside the container. If your Ansible roles aren't managing services using `systemd`, you might not need to use those options (even if you use my Docker images); many Ansible playbooks and roles work just fine without the elevated Docker container privileges.

You don't _have_ to use your own pre-built images (or mine), but if you have the tests run in Travis CI or any other environments where Docker images are not persistent (heck, I run `docker system prune --all` on my local workstation all the time!), it's much faster to use pre-built images. Plus you can have images which simulate a more full VM-like experience.

If you use VirtualBox, EC2, or some other platform, then the amount of time and effort required to maintain a custom image might negate the minimal performance gain from pre-building the images; but at least the option is out there. Oh, and I have plenty of Vagrant base image builds for VirtualBox (built automatically with Packer and Ansible) you could use to get started (e.g. [packer-ubuntu-1804](https://github.com/geerlingguy/packer-ubuntu-1804))!

## Integrating Molecule into Travis CI

The holy grail, at least for me, is reproducing my entire [multi-os testing platform](/blog/2018/how-i-test-ansible-configuration-on-7-different-oses-docker) I've built up over the years using Molecule instead of some cobbled-together shell scripts. One reason I am able to maintain nearly 100 popular Ansible roles on Ansible Galaxy (and lots of other projects besides) is the fact that all the common usage scenarios are thoroughly and automatically tested—not only on every pull request and commit, but also on a weekly cron schedule—via Travis CI.

I won't go into the full details of how I switched from my old setup to Molecule in Travis CI, but I will offer a couple examples you can look at to see how I did it, and managed to make a maintainable test setup for multiple operating systems and playbook test cases using Molecule and Travis CI:

  - [`geerlingguy.kibana`](https://github.com/geerlingguy/ansible-role-kibana) ([Travis CI build](https://travis-ci.org/geerlingguy/ansible-role-kibana)) - This is one of the simpler test cases; it just tests on two distros, the latest version of Ubuntu and CentOS, and runs [one playbook](https://github.com/geerlingguy/ansible-role-kibana/blob/master/molecule/default/playbook.yml) which installs Kibana then makes sure it's reachable.
  - [`geerlingguy.jenkins`](https://github.com/geerlingguy/ansible-role-jenkins) ([Travis CI build](https://travis-ci.org/geerlingguy/ansible-role-jenkins)) - This is one of my most complicated roles, therefore it has much a more complex array of tests. Not only is it tested against four different distros, there are also five separate test playbooks used to test various common use cases and configurable options.

In the Jenkins role (and many others), I specify a different `MOLECULE_PLAYBOOK` for the `converge` playbook. Some people may prefer an entirely different molecule `scenario` (besides the `default` scenario) for different test cases, but in my case, I set the `converge` playbook name (`provisioner.playbooks.converge` in the `molecule.yml`) to an environment variable so I can use a different playbook per scenario:

```
provisioner:
  name: ansible
  lint:
    name: ansible-lint
  playbooks:
    converge: ${MOLECULE_PLAYBOOK:-playbook.yml}
```

In all my roles, I use [Travis CI's build matrix](https://docs.travis-ci.com/user/customizing-the-build/#build-matrix) feature to perform each distro/playbook combination test in a separate build container, running in parallel with the other tests. It would take 7x longer to run all the Jenkins tests in series, and I hate waiting to see if a pull request will break anything in my role!

## Dive Deeper into Ansible role and playbook testing

You can find out even more about Molecule, Travis CI, Docker integration, and other testing topics in my book, [Ansible for DevOps](https://www.ansiblefordevops.com).
