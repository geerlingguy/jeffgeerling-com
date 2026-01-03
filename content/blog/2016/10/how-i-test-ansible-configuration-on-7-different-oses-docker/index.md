---
nid: 2704
title: "How I test Ansible configuration on 7 different OSes with Docker"
slug: "how-i-test-ansible-configuration-on-7-different-oses-docker"
date: 2016-10-05T02:52:44+00:00
drupal:
  nid: 2704
  path: /blog/2019/how-i-test-ansible-configuration-on-7-different-oses-docker
  body_format: markdown
  redirects:
    - /blog/2016/how-i-test-ansible-configuration-on-7-different-oses-docker
    - /blog/2018/how-i-test-ansible-configuration-on-7-different-oses-docker
aliases:
  - /blog/2016/how-i-test-ansible-configuration-on-7-different-oses-docker
  - /blog/2018/how-i-test-ansible-configuration-on-7-different-oses-docker
tags:
  - ansible
  - ansible for devops
  - automation
  - devops
  - docker
  - github
  - testing
  - travis ci
---

> The following post is an excerpt from chapter 11 in my book [Ansible for DevOps](https://www.ansiblefordevops.com/). The example used is an [Ansible role that installs Java](https://galaxy.ansible.com/geerlingguy/java/)—since the role is supposed to work across CentOS 6 and 7, Fedora 24, Ubuntu 12.04, 14.04, and 16.04, and Debian 8, I use Docker to run an end-to-end functional test on each of those Linux distributions. See an [example test run in Travis CI](https://travis-ci.org/geerlingguy/ansible-role-java/builds/162633043), and the [Travis file that describes the build](https://github.com/geerlingguy/ansible-role-java/blob/1.7.0/.travis.yml).
> 
> Note: I do the same thing currently (as of 2019), but now I'm using Molecule to tie everything together; see [Testing your Ansible roles with Molecule](/blog/2018/testing-your-ansible-roles-molecule).

<p style="text-align: center;"><a href="https://travis-ci.org/geerlingguy/ansible-role-java/builds/162633043">{{< figure src="./ansible-role-java-travis-docker-test-result.png" alt="Ansible Java role - Travis CI Docker-based test results" width="650" height="384" class="insert-image" >}}</a></p>

Automated testing using a continuous integration tool like Travis CI (which is free for public projects and integrated very well with GitHub) allows you to run tests against Ansible playbooks or roles you have hosted on GitHub with every commit.

There are four main things to test when building and maintaining Ansible playbooks or roles:

  1. The playbook or role's syntax (are all the .yml files formatted correctly?).
  2. Whether the playbook or role will run through all the included tasks without failing.
  3. The playbook or role's idempotence (if run again, it should not make any changes!).
  4. The playbook or role's success (does the role do what it should be doing?).

The most important part is #4—the _functional_ test—because what's the point of a playbook or role if it doesn't do what you want it to do (e.g. start a web server, configure a database, deploy an app, etc.)?

For the purposes of this example, we're going to make the following assumptions:

  - You are testing an Ansible role (though this process applies just as well to testing an entire playbook).
  - Your role's repository is hosted on GitHub.
  - You are using Travis CI and it's enabled for your role's repository.

Note that you can apply the test setup detailed here to almost any SCM and CI tool (e.g. GitLab, Jenkins, Circle, etc.), with minor variations.

## Testing on multiple OSes with Docker

Travis CI provides a VM in which you can run your tests. You can choose between a few flavors of Linux or macOS, but there's not a lot of flexibility in terms of _infrastructure_ testing, and Travis bakes in a lot of software by default (e.g. Ruby, Python, etc.).

Because we want to test our Ansible roles in as clean an environment as possible, we have two options:

  1. Choose from one of the few Travis default OS environments and try to clean out all the existing software installs before running our tests.
  2. Build our own clean test environments inside Travis using Docker containers and run tests in containers.

Historically, the first solution was easier to implement, but recent improvements in Travis's Docker support makes the second solution a better choice.

Because multi-OS, clean-slate tests are important to us, we will do the following for each test:

  1. Start a fresh, minimal OS container for each OS our role supports.
  2. Run our role inside the container (and then test idempotence and functionality).

For many of my roles and playbooks, I support the following OSes, therefore I maintain images on Docker Hub for the explicit purpose of testing Ansible roles and playbooks:

  - [CentOS 6](https://hub.docker.com/r/geerlingguy/docker-centos6-ansible/)
  - [CentOS 7](https://hub.docker.com/r/geerlingguy/docker-centos7-ansible/)
  - [Fedora 24](https://hub.docker.com/r/geerlingguy/docker-fedora24-ansible/)
  - [Debian 8](https://hub.docker.com/r/geerlingguy/docker-debian8-ansible/)
  - [Ubuntu 12.04](https://hub.docker.com/r/geerlingguy/docker-ubuntu1204-ansible/)
  - [Ubuntu 14.04](https://hub.docker.com/r/geerlingguy/docker-ubuntu1404-ansible/)
  - [Ubuntu 16.04](https://hub.docker.com/r/geerlingguy/docker-ubuntu1604-ansible/)

The rest of this section will demonstrate how to test an example Ansible role against all these OSes with one simple Travis configuration file.

## Setting up the test

Create a new 'tests' directory in your role or project directory, and create a test playbook inside:

    # Directory structure:
    my_role/
      tests/
        test.yml <-- the test playbook

Inside `test.yml`, add:

    ---
    - hosts: all
    
      roles:
        - role_under_test

In this playbook we tell Ansible to run our role on all hosts; since the playbook will run inside a Docker container with the option `--connection=local`, this basically means "run it on localhost". You can add `vars`, `vars_files`, `pre_tasks`, etc. if you need to adjust anything or prep the environment before your role runs, but I try to avoid overriding pre-packaged defaults, since they should ideally work across all environments—including barebones test environments.

The next step is to add a `.travis.yml` file to your role so Travis CI knows how to run your tests. Add the file to the root level of your role, and add the following scaffolding:

    ---
    # We need sudo for some of the Docker commands.
    sudo: required
    
    env:
      # Provide a list of OSes we want to use for testing.
    
    # Tell Travis to start Docker when it brings up an environment.
    services:
      - docker
    
    before_install:
      # Pull the image from Docker Hub for the OS under test.
    
    script:
      # Start the container from the image and perform tests.
    
    notifications:
      # Notify Ansible Galaxy when a role builds successfully.

This is a fairly standard Travis file layout, and if you want to dive deeper into how Travis works, read through the guide [Customizing the Build](https://docs.travis-ci.com/user/customizing-the-build). Next, we need to fill in each section of the file, starting with the parts that control the Docker container lifecycle.

## Building Docker containers in Travis

The first thing we need to do is decide on which OSes we'd like to test. For my [`geerlingguy.java`](https://galaxy.ansible.com/geerlingguy/java/) role, I support CentOS, Fedora, Debian, and Ubuntu, so at a minimum I want to support the latest LTS release of each, and for CentOS and Ubuntu, the previous LTS release as well:

    env:
      - distro: centos7
      - distro: centos6
      - distro: fedora24
      - distro: ubuntu1604
      - distro: ubuntu1404
      - distro: debian8

One other thing that needs to be configured per-OS is the init system. Because we're dealing with OSes that have a mixture of `systemd` and `sysv` init systems, we have to specify in Travis' environment the path to the init system to use, and any extra options that we need to pass to the `docker run` command to get the image in the right state for Ansible testing. So we'll add two variables for each distribution, `init` and `run_opts`:

    env:
      - distro: centos7
        init: /usr/lib/systemd/systemd
        run_opts: "--privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:ro"
      - distro: centos6
        init: /sbin/init
        run_opts: ""
      - distro: fedora24
        init: /usr/lib/systemd/systemd
        run_opts: "--privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:ro"
      - distro: ubuntu1604
        init: /lib/systemd/systemd
        run_opts: "--privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:ro"
      - distro: ubuntu1404
        init: /sbin/init
        run_opts: ""
      - distro: debian8
        init: /lib/systemd/systemd
        run_opts: "--privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:ro"

> Why use an `init` system in Docker? With Docker, it's preferable to either run apps directly (as 'PID 1') inside the container, or use a tool like Yelp's [dumb-init](https://github.com/Yelp/dumb-init) as a wrapper for your app. For our purposes, we're testing an Ansible role or playbook that could be run inside a container, but is also likely used on full VMs or bare-metal servers, where there will be a real init system controlling multiple internal processes. We want to emulate the real servers as closely as possible, therefore we set up a full init system (`systemd` or `sysv`) according to the OS.

Now that we've defined the OS distributions we want to test, and what init system we want Docker to call, we can manage the Docker container's lifecycle—we need to `pull` the image, `run` the image with our options, `exec` some commands to test our project, then `stop` the container once finished. Here's the basic structure, starting with the `before_install` step:

    before_install:
      # Pull container from Docker Hub.
      - 'docker pull geerlingguy/docker-${distro}-ansible:latest'
    
    script:
      # Create a random file to store the container ID.
      - container_id=$(mktemp)
    
      # Run container detached, with our role mounted inside.
      - 'docker run --detach --volume="${PWD}":/etc/ansible/roles/role_under_test:ro ${run_opts} geerlingguy/docker-${distro}-ansible:latest "${init}" > "${container_id}"'
    
      # TODO - Test the Ansible role.

Let's run through these initial commands that set up our OS environment:

  - `docker pull` (in `before_install`): This pulls down the appropriate OS image from Docker Hub with Ansible baked in. Note that `docker run` automatically pulls any images that don't already exist, but it's a best practice to always pull images prior to running them, in case the image is cached and there's a newer version.
  - `container_id=$(mktemp)`: We need a file to store the container ID so we can perform operations on it later; we could also name the container, but we treat containers (like infrastructure) like cattle, not pets. So no names.
  - `docker run`: This command starts a new container, with the Ansible role mounted inside (as a `--volume`), and uses the `run_opts` and `init` system described earlier in the `env:` section, then saves the container ID (which is output by Docker) into the temporary file we created in the previous step.

At this point, we have a Docker container running, and we can perform actions inside the container using `docker exec` just like we would if we were logged into a VM with the same OS.

For example, if you wanted to check up on disk space inside the container (assuming the `df` utility is present), you could run the command:

    script:
      ...
      - 'docker exec "$(cat ${container_id})" df -h'

You can also run the command with `--tty`, which will allocate a pseudo-TTY, allowing things like colors to be passed through to Travis for prettier output.

> Note: In Docker < 1.13, you have to set the `TERM` environment variable when using `docker exec` with the `--tty` option, like: `docker exec --tty "$(cat ${container_id})" env TERM=xterm df -h` (see: [exec does not set TERM env when -t passed](https://github.com/docker/docker/issues/9299)). Also note that some older sysvinit scripts, when run through Ansible's `service` module, can cause strange issues when run inside a Docker container (see: [service hangs the whole playbook](https://github.com/ansible/ansible-modules-core/issues/2459#issuecomment-246880847).

Now that we have a Docker container running (one for each of the distributions listed in the `env` configuration), we can start running some tests on our Ansible role or playbook.

## Testing the role's syntax

This is the easiest test; `ansible-playbook` has a built in command to check a playbook's syntax (including all the included files and roles), and return `0` if there are no problems, or an error code and some output if there were any syntax issues.

    ansible-playbook /etc/ansible/roles/role_under_test/test.yml --syntax-check

Add this as a command in the `script` section of `.travis.yml`:

    script:
      # Check the role/playbook's syntax.
      - >
        docker exec --tty "$(cat ${container_id})" env TERM=xterm
        ansible-playbook /etc/ansible/roles/role_under_test/tests/test.yml
        --syntax-check

If there are any syntax errors, Travis will fail the build and output the errors in the log.

## Role success - first run

The next aspect to check is whether the role runs correctly or fails on its first run. Add this after the `--syntax-check` test:

    # Run the role/playbook with ansible-playbook.
    - >
      docker exec --tty "$(cat ${container_id})" env TERM=xterm
      ansible-playbook /etc/ansible/roles/role_under_test/tests/test.yml

Ansible returns a non-zero exit code if the playbook run fails, so Travis will know whether the command succeeded or failed.

## Role idempotence

Another important test is the idempotence test—does the role change anything if it runs a second time? It should not, since all tasks you perform via Ansible should be idempotent (ensuring a static/unchanging configuration on subsequent runs with the same settings).

    # Run the role/playbook again, checking to make sure it's idempotent.
    - idempotence=$(mktemp)
    - >
      docker exec "$(cat ${container_id})"
      ansible-playbook /etc/ansible/roles/role_under_test/tests/test.yml
      | tee -a ${idempotence}
    - >
      tail ${idempotence}
      | grep -q 'changed=0.*failed=0'
      && (echo 'Idempotence test: pass' && exit 0)
      || (echo 'Idempotence test: fail' && exit 1)

This command runs the exact same command as before, but pipes the results into another temporary file (using `tee`, which pipes the output to the console and the file), and then the next command reads the output and checks to make sure 'changed' and 'failed' both report `0`. If there were no changes or failures, the idempotence test passes (and Travis sees the `0` exit and is happy). If there were any changes or failures, the test fails (and Travis sees the `1` exit and reports a build failure).

## Role success - final result

The last thing I check is whether the role actually did what it was supposed to do. If it configured a web server, is the server responding on port 80 or 443 without any errors? If it configured a command line application, does the application work when invoked, and do the things it's supposed to do?

    # Ensure Java is installed.
    - 'docker exec --tty "$(cat ${container_id})" env TERM=xterm which java'

In this example, a simple test of whether or not `java` is installed is used as a functional test of the role. In other cases, I might run the command `curl http://localhost:3000/` (to check if an app is responding on a particular port), or some other command that verifies an application is installed and running correctly.

Taking this a step further, you could even run a deployed application or service's own automated tests after Ansible is finished with the deployment, thus testing your infrastructure and application in one go—but we're getting ahead of ourselves here... that's a topic for later!

## Some notes about Travis CI

There are a few things you need to know about Travis CI, especially if you're testing Ansible, which will rely heavily on the VM environment inside which it is running:

  - **Docker Environment**: The default Docker installation runs on a particular Docker engine version, which may or may not be the latest stable release. Read through Travis' documentation for more: [Using Docker in Builds](https://docs.travis-ci.com/user/docker/).
  - **Networking/Disk/Memory**: Travis CI continously shifts the VM specs you're using, so don't assume you'll have X amount of RAM, disk space, or network capacity. Add commands like `cat /proc/cpuinfo`, `cat /proc/meminfo`, `free -m`, etc. in the `.travis.yml` `before_install` section if you need to figure out the resources available in your VM.

See much more information about the VM environment on the [Travis CI Build Environment page](http://docs.travis-ci.com/user/ci-environment/).

## Real-world examples

This style of testing is integrated into many of the `geerlingguy.*` roles on Ansible Galaxy; here are a few example roles using Travis CI integration in the way outlined above:

  - [https://github.com/geerlingguy/ansible-role-java](https://github.com/geerlingguy/ansible-role-java)
  - [https://github.com/geerlingguy/ansible-role-apache](https://github.com/geerlingguy/ansible-role-apache)
  - [https://github.com/geerlingguy/ansible-role-mysql](https://github.com/geerlingguy/ansible-role-mysql)

I'd like to give special thanks to Bert Van Vreckem, who helped me to get the initial versions of this Docker-based test workflow working on GitHub; he wrote a bit about the process on his blog, too: [Testing Ansible roles with Travis-CI: Multi-platform tests](http://bertvv.github.io/notes-to-self/2015/12/13/testing-ansible-roles-with-travis-ci-part-2-multi-platform-tests/).

## Other server and role testing tools

There are also a number of other projects which abstract the testing process a little further than the above approach; some allowing more control and easier use outside of the Travis CI environment, others focused more on Ansible roles in particular:

  - [serverspec](http://serverspec.org/) - A generalized server validation tool.
  - [molecule](https://github.com/metacloud/molecule) - A generalized solution for testing Ansible roles in any environment.
  - [goss](https://github.com/aelsabbahy/goss) - Another generalized server validation tool.
  - [rolespec](https://github.com/nickjj/rolespec) - A library for testing Ansible roles on Travis or locally.

Each of the options has some benefits and drawbacks; you should check them all out and find out which one works best in your workflow and skill-set.
