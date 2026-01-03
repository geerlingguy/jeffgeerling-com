---
nid: 2785
title: "Changing a deeply-nested dict variable in an Ansible playbook"
slug: "changing-deeply-nested-dict-variable-ansible-playbook"
date: 2017-06-19T16:37:03+00:00
drupal:
  nid: 2785
  path: /blog/2017/changing-deeply-nested-dict-variable-ansible-playbook
  body_format: markdown
  redirects: []
tags:
  - ansible
  - dict
  - irc
  - jinja2
  - python
  - tutorial
  - yaml
---

I recently had to build an Ansible playbook that takes in a massive inventory structure (read from a YAML file), modifies a specific key in that file, then dumps the file back to disk. There are some other ways that may be more efficient standalone (e.g. using a separate Python/PHP/Ruby/etc. script and a good YAML library), but since I had to do a number of other things in this Ansible playbook, I thought it would keep it simple if I could also modify the key inside the playbook.

I was scratching my head for a while, because while I knew that I could use the `dict | combine()` filter to merge two dicts together (this is a feature that was introduced in Ansible 2.0), I hadn't done so for a deeply-nested dict.

After banging my head on a test playbook for a while, I finally resorted to the #ansible IRC room and asked if anyone else knew how to do it. I posted [this Pastebin demo playbook](https://pastebin.com/vm2bN5Lt), and within a few minutes, both [halberom](https://github.com/halberom) and [sivel](https://github.com/sivel) responded with some ideas. Sivel suggested I structure the object correctly inside the `combine()` filter, and also helped me do everything in one task using the `combine()` filter's `recursive=True` option (see [docs on the `combine()` filter](http://docs.ansible.com/ansible/playbooks_filters.html#combining-hashes-dictionaries) for more details).

So in the end, I had a demonstration playbook like:

```
---
- hosts: localhost
  connection: local
  gather_facts: no

  vars:
    animals:
      mammals:
        humans:
          eyes: many-colored
          legs: two
      birds:
        cardinals:
          eyes: black
          feathers: blue # <-- I want to change this to 'red'.

  tasks:
    - name: Change animals.birds.cardinals.feathers to "red".
      set_fact:
        animals: "{{ animals|combine({'birds': {'cardinals': {'feathers': 'red'}}}, recursive=True) }}"

    - name: Echo the updated animals var to the screen.
      debug: var=animals
```

From that point, it was just a matter of writing the updated vars structure to a `.yml` file, which is as easy as:

```
- name: Write the updated animals dict to a YAML file.
  template:
    src: animals.yml.j2
    dest: /path/to/animals.yml
```

Then, inside the template `animals.yml.j2`:

```
---
animals:
  {{ animals | to_nice_yaml(width=80, indent=2) | indent(2) }}
```

After running the complete playbook, I ended up with an updated `animals.yml` YAML file formatted like:

```
---
animals:
  birds:
    cardinals:
      eyes: black
      feathers: red
  mammals:
    humans:
      eyes: many-colored
      legs: two
```

(Note that when you use Ansible, or really any tool, for automatically generating a YAML file, you might not get as much control over things like whitespace, comments, etc.)

I've attached an example playbook (which reads in `animals.yml`, modifies a nested dict variable, then writes out the updated file) to this blog post: Download [animals-ansible-change-nested-dict-example.zip](./animals-ansible-change-nested-dict-example.zip) and try it for yourself!
