---
nid: 2864
title: "Fixing Jenkins CLI 'ERROR: anonymous is missing the Overall/Read permission'"
slug: "fixing-jenkins-cli-error-anonymous-missing-overallread-permission"
date: 2018-08-27T14:53:31+00:00
drupal:
  nid: 2864
  path: /blog/2018/fixing-jenkins-cli-error-anonymous-missing-overallread-permission
  body_format: markdown
  redirects: []
tags:
  - authentication
  - automation
  - cli
  - jenkins
  - password
---

For the past decade or so, I've been working to automate as much of a Jenkins server build process as possible. There are a few 'hacky' bits to doing so, like managing some Jenkins XML files (or if you really want to go crazy, storing your entire $JENKINS_HOME somewhere in a source control repository!).

One of the most annoying things about automating Jenkins is using the `jenkins-cli.jar` file to interact with Jenkins on the CLI. It doesn't come with any automated solution for authenticating with Jenkins, and is meant for running either on the same server where Jenkins is running, or really anywhere that has SSH access. I generally don't like putting any Jenkins bits (including the CLI tool) on servers outside the actual Jenkins instance itself, so I've traditionally used the `--username` and `--password` method of authenticating with `jenkins-cli`.

However, it seems those CLI flags were deprecated and removed at some point in the past few months (maybe around 2.130 or so?), and now I get the following error when running CLI commands that way:

```
ERROR: anonymous is missing the Overall/Read permission
```

So, looking into the [Jenkins CLI docs](https://jenkins.io/doc/book/managing/cli/), it mentions the preferred method of auth is to set up an SSH Public Key in your Jenkins user account, then referencing that with the CLI like:

```
java -jar /opt/jenkins-cli.jar -s "http://localhost:8080" -i path/to/key.rsa who-am-i
```

Digging down deeper into the CLI jarfile options, I found that the username/password combo is still usable with the `-auth` option:

```
java -jar /opt/jenkins-cli.jar -s "http://localhost:8080" -auth username:password who-am-i
```

The docs do state you should use your Jenkins user token if possible, but it's much harder to automate the user setup and token retrieval, than to use a username and password setup by automated build scripts.
