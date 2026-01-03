---
nid: 2745
title: "YAML formatting and Drupal 8 - making things readable"
slug: "yaml-formatting-and-drupal-8-making-things-readable"
date: 2017-02-10T21:01:45+00:00
drupal:
  nid: 2745
  path: /blog/2017/yaml-formatting-and-drupal-8-making-things-readable
  body_format: markdown
  redirects: []
tags:
  - configuration management
  - drupal
  - drupal 8
  - drupal planet
  - syntax
  - theming
  - yaml
---

As someone who loves [YAML syntax](http://www.yaml.org/) (so much more pleasant to work with than JSON!), I wanted to jot down a few notes about syntax formatting for the benefit of Drupal 8 developers everywhere.

I often see copy/pasted YAML examples like the following:

```
object:
  child-object: {key: value, key2: {key: value}}
```

This is perfectly valid YAML. And technically [any JSON is valid YAML too](http://www.yaml.org/spec/1.2/spec.html#id2759572). That's part of what makes YAML so powerful—it's easy to translate between JSON and YAML, but YAML is way more readable!

So instead of using YAML like that, you can make the structure and relationships so much more apparent by formatting it like so:

```
object:
  child-object:
    key: value
    key2:
      key: value
```

This format makes it much more apparent that both `key` and `key2` are part of `child-object`, and the last `key: value` is part of `key2`.

In terms of Drupal, I see the confusing `{ }` syntax used quite often in themes and library declarations. Take, for instance, a library declaration that adds in some attributes to an included JS file:

```
https://some-api.com/?key=APIKEY&signed_in=true: {type: external, attributes: { defer: true, async: true} }
```

That's difficult to read at a glance—and if you have longer key or value names, it gets even worse!

Instead, use the structured syntax for a more pleasant experience (and easier `git diff` ability):

```
https://some-api.com/?key=APIKEY&signed_in=true:
  type: external
  attributes:
    defer: true
    async: true
```

You really only need to use the `{ }` syntax for objects if you're defining an empty object (one without any keys or subelements):

```
# Objects.
normal-object:
  key: value
empty-object: { }

# Arrays.
normal-array:
  - item
empty-array: [ ]
```

I've worked with a _lot_ of YAML in the past few years, especially in my work writing [Ansible for DevOps](https://www.ansiblefordevops.com). It's a great structured language, and the primary purpose is to make structured data easy to read and edit (way, way simpler than JSON, especially considering you won't need to worry about commas and such!)—so go ahead and use that structure to your advantage!
