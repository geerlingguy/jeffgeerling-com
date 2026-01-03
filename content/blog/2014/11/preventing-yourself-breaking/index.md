---
nid: 2470
title: "Preventing yourself from accidentally breaking production with Drush"
slug: "preventing-yourself-breaking"
date: 2014-11-06T18:51:28+00:00
drupal:
  nid: 2470
  path: /blogs/jeff-geerling/preventing-yourself-breaking
  body_format: full_html
  redirects: []
tags:
  - bash
  - command line
  - dotfiles
  - drupal
  - drupal planet
  - drush
  - shell
---

For all the sites I maintain, I have at least a local and production environment. Some projects warrant a dev, qa, etc. as well, but for the purposes of this post, let's just assume you often run drush commands on local or development environments during development, and eventually run a similar command on production during a deployment.

What happens if, at some point, you are churning through some Drush commands, using aliases (e.g. <code>drush @site.local break-all-the-things</code> to break things for testing), and you accidentally enter <code>@site.prod</code> instead of <code>@site.local</code>? Or what if you were doing something potentially disastrous, like deleting a database table locally so you can test a module install file, using <code>drush sqlq</code> to run a query?

```
$ drush @site.prod break-all-the-things -y
Everything is broken!                                    [sadpanda]
```

Most potentially-devastating drush commands will ask for confirmation (which could be overridden with a <code>-y</code> in the command), but I like having an extra layer of protection to make sure I don't do something dumb. If you use Bash for your shell session, you can put the following into your .profile or .bash_profile, and Bash will warn you whenever the string <code>.prod</code> is in one of your commands:

```
prod_command_trap () {
  if [[ $BASH_COMMAND == *.prod* ]]
  then
    read -p "Are you sure you want to run this command on prod [Y/n]? " -n 1 -r
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "\nRunning command \"$BASH_COMMAND\" \n"
    else
      echo -e "\nCommand was not run.\n"
      return 1
    fi
  fi
}
shopt -s extdebug
trap prod_command_trap DEBUG
```

Now if I accidentally run a command on production I get a warning/confirmation before the command is run:

```
$ drush @site.prod break-all-the-things -y
Are you sure you want to run this command on prod [Y/n]?
```

This code, as well as other aliases and configuration I use to help my command-line usage more efficient, is also viewable in my <a href="https://github.com/geerlingguy/dotfiles">Dotfiles</a> repository on GitHub.
