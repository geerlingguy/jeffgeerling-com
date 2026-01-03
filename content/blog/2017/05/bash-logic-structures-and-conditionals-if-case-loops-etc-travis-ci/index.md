---
nid: 2775
title: "Bash logic structures and conditionals (if, case, loops, etc.) in Travis CI"
slug: "bash-logic-structures-and-conditionals-if-case-loops-etc-travis-ci"
date: 2017-05-17T03:29:47+00:00
drupal:
  nid: 2775
  path: /blog/2017/bash-logic-structures-and-conditionals-if-case-loops-etc-travis-ci
  body_format: markdown
  redirects:
    - /blog/2017/complex-bash-logic-structures-if-case-etc-travis-ci
    - /blog/2017/complex-bash-logic-structures-if-case-loops-etc-travis-ci
aliases:
  - /blog/2017/complex-bash-logic-structures-if-case-etc-travis-ci
  - /blog/2017/complex-bash-logic-structures-if-case-loops-etc-travis-ci
tags:
  - ansible
  - bash
  - docker
  - php
  - shell
  - travis ci
  - yaml
---

Travis CI's documentation often mentions the fact that it can call out to shell scripts in your repository, and recommends anything more complicated than a command or two (maybe including a pipe or something) be placed in a separate shell script.

But there are times when it's a lot more convenient to just keep the Travis CI-specific logic inside my repositories' `.travis.yml` file.

As it turns out, YAML is well-suited to, basically, inlining shell scripts. YAML's [literal scalar indicator](http://yaml.org/spec/current.html#|%20literal%20style/) (a pipe, or `|`) allows you to indicate a block of content where newlines should be preserved, though whitespace before and after the line will be trimmed.

So if you have a statement like:

```
if [ "${variable}" == "something" ]; then
  do_something_here
fi
```

You can represent that in YAML via:

```
- |
  if [ "${variable}" == "something" ]; then
    do_something_here
  fi
```

Note that every line after the `- |` must be indented one more level (e.g. 2 spaces further).

So, in some of my `.travis.yml` files, I have logic that determines whether certain bits of code should run in certain environmental conditions (some of my projects run a large matrix of builds since I sometimes support 7 operating systems and sometimes multiple build processes in each!):

```
  # Check the status of PHP-FPM.
  - |
    if [ "${playbook}" == "test.yml" ]; then
      case "${distro}" in
        "centos7"|"fedora24")
          docker exec --tty ${container_id} env TERM=xterm systemctl --no-pager status php-fpm status
          docker exec --tty ${container_id} env TERM=xterm systemctl --no-pager status php-fpm status | grep -qF "fpm.service; enabled"
          ;;
        "debian8"|"ubuntu1604")
          docker exec --tty ${container_id} env TERM=xterm systemctl --no-pager status php${php_version}-fpm status
          docker exec --tty ${container_id} env TERM=xterm systemctl --no-pager status php${php_version}-fpm status | grep -qF "fpm.service; enabled"
          ;;
      esac
    fi
```

The above example was taken from my [Ansible role for PHP's `.travis.yml` file](https://github.com/geerlingguy/ansible-role-php/blob/3.4.5/.travis.yml#L55-L68).

I could technically do these things in one super-long line... but that's just sloppy. And if this started getting any more complex, it would be a good candidate for extracting into a separate shell script, as Travis' documentation suggests.
