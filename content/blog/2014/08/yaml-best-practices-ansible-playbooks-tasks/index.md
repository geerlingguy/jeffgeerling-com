---
nid: 2607
title: "YAML best practices for Ansible playbooks - tasks"
slug: "yaml-best-practices-ansible-playbooks-tasks"
date: 2014-08-28T20:23:41+00:00
drupal:
  nid: 2607
  path: /blog/yaml-best-practices-ansible-playbooks-tasks
  body_format: full_html
  redirects: []
tags:
  - ansible
  - ansible for devops
  - syntax
  - yaml
aliases:
  - /blog/yaml-best-practices-ansible-playbooks-tasks
   - /blog/yaml-best-practices-ansible-playbooks-tasks
---

<p>This post is a follow-up to a recent <a href="https://groups.google.com/forum/#!topic/ansible-project/GfJBkzuTTNM">discussion about YAML formatting for complex Ansible playbook tasks</a> on the Ansible Project mailing list, and will also be appearing as part of Appendix B: Ansible Best Practices and Conventions in my <a href="http://www.ansiblefordevops.com/">Ansible for DevOps book</a> on LeanPub.</p>

<h2>
<a name="user-content-yaml-a-simple-configuration-language" class="anchor" href="#yaml-a-simple-configuration-language" aria-hidden="true"><span class="octicon octicon-link"></span></a>YAML, a simple configuration language</h2>

<p>YAML's usage for describing configuration has been increasing rapidly in the past few years, and with the introduction of SaltStack and Ansible, YAML finally made its way into the server configuration management realm as a first class citizen.</p>

<p>YAML is a pretty simple language; it is a human-readable, machine-parsable syntax that allows for complex nested object, list, and array structures, so it is a great fit for a configuration management tool. Consider the following method of defining a list (or 'collection') of widgets:</p>


```
widget:
  - foo
  - bar
  - fizz
```

<p>This would translate into Python (using the <code>PyYAML</code> library employed by Ansible) as the following:</p>


```
translated_yaml = {'widget': ['foo', 'bar', 'fizz']}
```

<p>And what about a structured list/map in YAML?</p>


```
widget:
  foo: 12
  bar: 13
```

<p>The Python that would result:</p>


```
translated_yaml = {'widget': {'foo': 12, 'bar': 13}}
```

<p>A few things to note with both of the above examples:</p>

<ul>
<li>YAML will try to determine the type of an item automatically. So <code>foo</code> in the first example would be translated as a string, <code>true</code> or <code>false</code> would be a boolean, and <code>123</code> would be an integer. This post doesn't attempt to go further with this exploration, but realize that you might want to explicitly declare strings with quotes (<code>''</code> or <code>""</code>) to minimize surprises.</li>
<li>Whitespace matters! YAML uses spaces (literal space characters—<em>not</em> tabs) to define structure (mappings, array lists, etc.), so set your editor to use spaces for tabs. You can technically use either a tab or a space to delimit parameters (like <code>apt: name=foo state=installed</code>—you can use either a tab or a space between parameters), but it's generally preferred to use spaces everywhere, to minimize errors and display irregularities across editors and platforms.</li>
<li>YAML syntax is robust and well-documented. Read through the official <a href="http://www.yaml.org/spec/1.2/spec.html">YAML Specification</a> and/or the <a href="http://pyyaml.org/wiki/PyYAMLDocumentation">PyYAMLDocumentation</a> to dig deeper.</li>
</ul><h2>
<a name="user-content-a-basic-ansible-playbook" class="anchor" href="#a-basic-ansible-playbook" aria-hidden="true"><span class="octicon octicon-link"></span></a>A basic Ansible playbook</h2>

<p>To use Ansible, you only need to know minimal YAML structure. Consider the following simple playbook:</p>


```
---
# My Ansible playbook.
- hosts: all

  tasks:
    - name: Install foo.
      apt: pkg=foo state=installed
```

<ul>
<li>The first line above denotes the beginning of some YAML—anything above that line shouldn't be parsed as YAML (but I wouldn't rely on all YAML parsers being so smart... so I generally leave YAML in <code>.yml</code> and add documentation as comments inline with the YAML).</li>
<li>The second line is a comment. Comments start with <code>#</code> and can use multiple lines (as long as each line starts with <code>#</code>).</li>
<li>The third line begins a list; in this case, a list of plays Ansible should run. Generally, playbooks only affect one set of hosts (in this case, <code>all</code> hosts defined in available/given inventories), but you can add additional plays by starting another new <code>- hosts: [group]</code> section or including another playbook with another play.</li>
<li>For the first (and in this playbook, only) grouping of hosts, we define a list of tasks. The first task uses the <code>apt</code> module to install the <code>foo</code> package on a Debian-based system.</li>
</ul><p>All well and good, right? Well, as you get deeper into Ansible and start defining more complex configuration, you might start seeing tasks like the following:</p>


```
- name: Copy Phergie shell script into place.
  template: src=templates/phergie.sh.j2 dest=/home/{{ phergie_user }}/phergie.sh owner={{ phergie_user }} group={{ phergie_user }} mode=755
```

<p>The one-line syntax (which uses Ansible-specific <code>key=value</code> shorthand for defining parameters) has some very positive attributes:</p>

<ul>
<li>Typical tasks (like installations and copies) are compact and readable (<code>apt: pkg=apache2 state=installed</code> is just about as simple as <code>apt-get install -y apache2</code>; in this way, an Ansible playbook feels very much like a shell script).</li>
<li>Playbooks can be more compact, and more configuration can be displayed on one screen.</li>
<li>Ansible's official documentation follows this format, and many existing roles and playbooks use one line for all parameters.</li>
</ul><p>However, as highlighted in the above example, there are a few issues with this <code>key=value</code> syntax, namely you have to:</p>

<ul>
<li>Have a pretty large/widescreen monitor (able to display at least 120 characters comfortably)</li>
<li>Use a source control UI that displays output in a very wide display (e.g. <em>not</em> GitHub, GitLab, Gogs, etc.)</li>
<li>Read left-to-right</li>
<li>Have a diff viewer that easily highlights inter-line differences</li>
<li>Not worry about variable types being converted to strings in some situations</li>
</ul><p>I argue that the shorthand syntax falls apart for more complicated, shared playbooks (especially roles), and I have a few ideas to help you make tasks more readable, better for version control software and diffing.</p>

<h2>
<a name="user-content-methods-for-formatting-ansible-tasks-in-yaml" class="anchor" href="#methods-for-formatting-ansible-tasks-in-yaml" aria-hidden="true"><span class="octicon octicon-link"></span></a>Methods for formatting Ansible tasks in YAML</h2>

<p>Following a discussion over on the Ansible Project Google Group on <a href="https://groups.google.com/forum/#!topic/ansible-project/GfJBkzuTTNM">YAML formatting best practices</a>, and also the maintenance of dozens of roles and playbooks, I've finally settled on a few basic guidelines for my playbook tasks, and generally prefer using a multiline syntax rather than shorthand for more complex tasks.</p>

<h3>
<a name="user-content-simple-straightforward-tasks---shorthandone-line-" class="anchor" href="#simple-straightforward-tasks---shorthandone-line-" aria-hidden="true"><span class="octicon octicon-link"></span></a>Simple, straightforward tasks - shorthand/one-line (<code>=</code>)</h3>

<p>For simpler tasks, I usually stick to the shorthand syntax, using <code>key=value</code> parameters.</p>


```
- name: Install Nginx.
  yum: pkg=nginx state=installed
```

<p>For any situation where an equivalent shell command would roughtly match what I'm writing in the YAML, I prefer this method, since it's immediately obvious what's happening, and it's highly unlikely any of the parameters (like <code>state=installed</code>) will change frequently during development.</p>

<h3>
<a name="user-content-complex-or-3-parameter-tasks---structured-map-" class="anchor" href="#complex-or-3-parameter-tasks---structured-map-" aria-hidden="true"><span class="octicon octicon-link"></span></a>Complex or 3+ parameter tasks - structured map (<code>:</code>)</h3>

<p>For more complex tasks, like the longer <code>template</code> example above, I prefer the following format:</p>


```
- name: Copy Phergie shell script into place.
  template:
    src: "templates/phergie.sh.j2"
    dest: "/home/{{ phergie_user }}/phergie.sh"
    owner: "{{ phergie_user }}"
    group: "{{ phergie_user }}"
    mode: 0755
```

<p>A few notes on this syntax:</p>

<ul>
<li>The structure is all valid YAML, using the structured list/map syntax mentioned in the beginning of this post.</li>
<li>Strings, booleans, integers, octals, etc. are all preserved (instead of being converted to strings).</li>
<li>Each parameter <em>must</em> be on its own line, so you can't chain together <code>mode: 0755, owner: root, user: root</code> to save space.</li>
<li>YAML syntax highlighting works slightly better for this format than <code>key=value</code>, since each key will be highlighted, and values will be displayed as constants, strings, etc.</li>
</ul>

<h3>
<a name="user-content-a-passable-hybrid-approach---folded-scalars-" class="anchor" href="#a-passable-hybrid-approach---folded-scalars-" aria-hidden="true"><span class="octicon octicon-link"></span></a>A passable hybrid approach - folded scalars (<code>></code>)</h3>

<p>Another approach that's often used in the wild (I use it in many of my own work) is using the terse <code>key=value</code> parameter syntax as in Ansible's documentation, but splitting values over multiple lines using YAML's folded scalar syntax:</p>


```
- name: Copy Phergie shell script into place.
  template: >
    src=templates/phergie.sh.j2
    dest=/home/{{ phergie_user }}/phergie.sh
    owner={{ phergie_user }} group={{ phergie_user }} mode=755
```

<p>In YAML, the <code>></code> character denotes a <em>folded scalar</em>, where every line that follows (as long as it's indented further than the first line) will be joined with the line above by a space. So the above YAML and the original <code>template</code> example will function exactly the same.</p>

<p>This syntax allows arbitrary splitting of lines on parameters, but it also doesn't preserve numeric, boolean, and other non-string types for values.</p>

<p>I have started to phase out this approach in my own work (and will be changing older examples in my book, <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>) in favor of the structure map style above. The only place where I can see the folded scalar approach being more helpful is for certain uses of the <code>command</code> and <code>shell</code> modules, where you need to pass in extra options:</p>


```
- name: Install Drupal.
  command: >
    drush si -y
    --site-name="{{ drupal_site_name }}"
    --account-name=admin
    --account-pass={{ drupal_admin_pass }}
    --db-url=mysql://root@localhost/{{ domain }}
    chdir={{ drupal_core_path }}
    creates={{ drupal_core_path }}/sites/default/settings.php
```

<p>Typically, if you can find a way to run a command without having to use <code>creates</code> and <code>chdir</code>, or very long commands (which are arguably unreadable either in single <em>or</em> multiline format!), it's better to do that instead of this monstrosity.</p>

<p>But sometimes the above is as good as you can do to keep unweildy tasks sane.</p>

<h2>
<a name="user-content-summary" class="anchor" href="#summary" aria-hidden="true"><span class="octicon octicon-link"></span></a>Summary</h2>

<p>As I <a href="https://groups.google.com/d/msg/ansible-project/GfJBkzuTTNM/RsoLu4P4JHgJ">mentioned</a> in the mailing list, one of Ansible's strengths is its flexibility; any one of the above methods of task definition is equally valid and functional. I have chosen to use the shorthand syntax for simpler tasks, and structured maps for more complex tasks, since they feel more maintainable and readable to my eye.</p>

<p>If you prefer to use a different syntax or conventions, that's not <em>wrong</em>. As with most programming and technical things, being <em>consistent</em> is more important than following a particular set of rules, especially if that set of rules isn't universally agreed upon.</p>

<p>I would encourage the use of one of these styles as a general rule, though, and also communicate as much to the people who will be working with you on your playbooks. Nothing's worse than debugging a complicated role and having to visually parse through three different YAML styles!</p>
