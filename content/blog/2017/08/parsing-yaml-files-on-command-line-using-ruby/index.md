---
nid: 2798
title: "Parsing YAML files on the command line using Ruby"
slug: "parsing-yaml-files-on-command-line-using-ruby"
date: 2017-08-03T16:01:39+00:00
drupal:
  nid: 2798
  path: /blog/2017/parsing-yaml-files-on-command-line-using-ruby
  body_format: markdown
  redirects: []
tags:
  - bash
  - ruby
  - script
  - stack overflow
  - yaml
---

I have been working on an infrastructure project that uses YAML files for all inventory and configuration management, and for the most part, if you're using tools like Ansible, CloudFormation, etc., then you don't ever have to worry about the actual parsing of a YAML file, and keys and values in the file are readily accessible since these tools parse them and get them into a readable structure for you.

But there's often little bits of glue code, or infrastructure build/cleanup jobs, where you need to grab one specific value out of a YAML file, and all you have readily available is bash. Luckily for me, I also have Ruby available in the particular environment where I needed to parse the YAML file, so doing this was as easy as:

  1. Defining a little bit of Ruby code which would load the YAML file, then grab a value out of it.
  2. Running that Ruby code using `ruby -e` (`-e` for 'evaluate this code), operating on the contents of a YAML file.

And here's how that looked, in my case:

    RUBY_YAML_PARSE="inventory = YAML::load(STDIN.read); puts inventory['${environment}']['key']"
    image=$(cat inventory.yml | ruby -ryaml -e "$RUBY_YAML_PARSE")

If I had a YAML file like this:

```
dev:
  key: value
prod:
  key: value2
```

Then the script would parse out `value` if the `environment` is set to `dev`, or `value2` if the `environment` is set to `prod`.

Pretty handy! I found this solution in [this Stack Overflow answer](https://stackoverflow.com/a/9243599/100134), and other answers in that thread had some interesting ways of doing it natively in bash (without requiring a language interpreter present on the server, like Ruby, PHP, or Python). But using a library like Ruby's [yaml library](https://ruby-doc.org/stdlib-1.9.3/libdoc/yaml/rdoc/YAML.html) means a lot of weird edge cases are covered that might trip up a custom YAML interpreter!
