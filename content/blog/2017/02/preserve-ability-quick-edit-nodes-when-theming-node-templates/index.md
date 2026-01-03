---
nid: 2744
title: "Preserve the ability to Quick Edit nodes when theming node templates!"
slug: "preserve-ability-quick-edit-nodes-when-theming-node-templates"
date: 2017-02-09T20:49:52+00:00
drupal:
  nid: 2744
  path: /blog/2017/preserve-ability-quick-edit-nodes-when-theming-node-templates
  body_format: markdown
  redirects: []
tags:
  - contextual
  - drupal 8
  - drupal planet
  - javascript
  - quick edit
  - theming
  - twig
---

...aka, avoid the annoying Javascript error below:

```
drupal.js:67
TypeError: undefined is not an object (evaluating 'entityElement
      .get(0)
      .getAttribute')
```

Many themers working on Drupal 8 sites have Contextual menus and Quick Edit enabled (they're present in the Standard Drupal install profile, as well as popular profiles like Acquia's Lightning), and at some point during theme development, they notice that there are random and unhelpful fatal javascript errors—but they only appear for logged in administrators.

Eventually, they may realize that disabling the Contextual links module fixes the issue, so they do so and move along. Unfortunately, this means that content admins (who tend to _love_ things like contextual links—at least when they work) and up not being able to hover over content to edit it.

There are two ways you can make things better without entirely disabling these handy modules:

  1. Apply the patch from this Drupal.org issue: [contextual.js and quickedit.js should fail gracefully, with useful error messages, when Twig templates forget to print attributes](https://www.drupal.org/node/2551373).
  2. Make sure you _always_ include `attributes` somewhere in the wrapping class in all node templates, as well as `{{ title_prefix }}` and `{{ title_suffix }}`. If you don't, the contextual links module won't be able to inject the proper classes it needs to add the contextual link. And until the above patch hits Drupal core, any page where your template is used and a user with permission to use Contextual links visits, Javascript on that page will break!

As one quick example, I was working on a node template for a bootstrap theme, and it looked something like:

```
  <div class="col-md-6">
    <h2 class="lead">{{ label }}</h2>
    <p class="small">{{ node.getCreatedTime() | date("F d, Y") }}</p>
    <div class="body">
      {{ content.body }}
    </div>
    {{ content|without('body') }}
  </div>
```

To fix this so the contextual link displays to the right of the title, I modified the template as in number 2 above, to look like:

```
<div{{ attributes }}>
  <div class="col-md-6">
    {{ title_prefix }}
    <h2 class="lead">{{ label }}</h2>
    {{ title_suffix }}
    <p class="small">{{ node.getCreatedTime() | date("F d, Y") }}</p>
    <div class="body">
      {{ content.body }}
    </div>
    {{ content|without('body') }}
  </div>
</div>
```

Now, I get the handy little contextual link widget, and I can happily go about editing nodes within the context of the page I'm on (instead of digging through the admin content listings for the node!):

{{< figure src="./quick-edit-contextual-link-node-drupal-8-twig.png" alt="Quick edit contextual link in Drupal 8" width="349" height="148" class="insert-image" >}}

Note also the `{{ content|without('body') }}`—it's always important to render the entire {{ content }} element somewhere (even `without()` all the other fields on the node) so that cache tags bubble correctly—see a related core issue I opened a week or so ago: [Bubbling cache tag metadata when rendering nodes in preprocess functions is difficult](https://www.drupal.org/node/2848158).
