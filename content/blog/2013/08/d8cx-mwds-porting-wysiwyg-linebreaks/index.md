---
nid: 2421
title: "D8CX at MWDS - Porting Wysiwyg Linebreaks to Drupal 8"
slug: "d8cx-mwds-porting-wysiwyg-linebreaks"
date: 2013-08-17T18:58:41+00:00
drupal:
  nid: 2421
  path: /blogs/jeff-geerling/d8cx-mwds-porting-wysiwyg-linebreaks
  body_format: full_html
  redirects: []
tags:
  - core
  - development
  - drupal
  - drupal 8
  - drupal planet
  - mwds
---

I have been at the <a href="https://groups.drupal.org/node/300808">Midwest Drupal Summit</a> for the past few days, focusing on <a href="https://drupal.org/search/site/%2523D8CX?f[0]=ss_meta_type%3Amodule">#D8CX</a> and reducing Drupal 8's technical debt (at least, a tiny bit of it!).

<h2>Wysiwyg Linebreaks</h2>

My main goal at the conference was to port the <a href="https://drupal.org/project/wysiwyg_linebreaks">Wysiwyg Linebreaks</a> module to Drupal 8. I originally built the module for Drupal 6 while helping the <a href="http://archstl.org/">Archdiocese of St. Louis</a> migrate almost 50 separate Joomla-based websites into one organic-groups-driven Drupal site. Their legacy content used linebreaks (rather than markup like <code><p></code> and <code><br /></code> tags) for paragraphs of text, and when we originally enabled Wysiwyg with TinyMCE, the editor ran all the text together in one big paragraph. The Wysiwyg Linebreaks module fixes that problem by running some JavaScript that adds the required tags when an editor is attached to a textarea, and (optionally) removes the tags when the editor is detached.

The Drupal 6 and Drupal 7 versions of the module depended on the <a href="https://drupal.org/project/WYSIWYG">Wysiwyg</a> module, and worked with many different editors—however, the way the linebreaks plugin was added was slightly clunky, and required a little bit of a hack to work well (see <a href="https://drupal.org/node/1050340">Let cross-editor plugins be button-less (aka 'extensions')</a>).

For Drupal 8, the module simply defines an editor plugin without a button (no hacks!), and integrates with CKEditor's API (See change notice: <a href="https://drupal.org/node/1911646">CKEditor module added: WYSIWYG in core!</a>).

This is the second contrib module I've ported (the first being <a href="https://drupal.org/project/honeypot">Honeypot</a>), and the process is relatively straightforward. The nicest thing about Drupal 8's refined architecture is that, for modules like Wysiwyg Linebreaks, you don't need to have much, if any, procedural code inside .module and .inc files. For Wysiwyg Linebreaks, there's just the JavaScript plugin code inside <code>/js/linebreaks/linebreaks.js</code>, and a CKEditor plugin definition inside <code>/lib/Drupal/wysiwyg_linebreaks/Plugin/CKEditorPlugin/Linebreaks.php</code>. Very clean!

To anyone else working on a CKEditor plugin or integration with the new Drupal 8 Editor module: The API for dealing with editors, or with CKEditor in particular, is very simple but powerful—see the 'API' section on <a href="https://drupal.org/node/1911614">this change notice for the Editor module</a>, and the 'Provide additional CKEditor plugins' section on <a href="https://drupal.org/node/1911646">this change notice for CKEditor</a>.

One more note: I was made aware of the issue <a href="https://drupal.org/node/1933916">How do we want to facilitate enabling of CKEditor for sites upgraded from Drupal 7 to Drupal 8?</a> just after I finished committing the last fixes for the D8 version of Wysiwyg Linebreaks. This module solves the problem of legacy content that uses the <code>autop</code> filter ("Convert line breaks into HTML (i.e. <code><br></code> and <code><p></code>)") quite nicely—enable it, and content will look/function as it always has, with or without CKEditor enabled.

<h2>MWDS at Palantir's HQ</h2>

<p style="text-align: center;">{{< figure src="./bacon-donuts.jpg" alt="Bacon Donuts" width="400" height="245" >}}
<em>Bacon Donuts at #MWDS – Palantir, you know us too well...</p>

This was the first year I've attended the Midwest Drupal Summit at Palantir's HQ in Chicago, IL, and it was a great experience! Besides working on <a href="https://drupal.org/node/1917702">porting Wysiwyg Linebreaks</a> and cleaning up Honeypot to work with Drupal 8 head, I worked on:

<ul>
<li><a href="https://drupal.org/node/1356276">Make install profiles inheritable</a></li>
<li><a href="https://drupal.org/node/2067881">Search is missing from block admin UI after installation</a></li>
<li><a href="https://drupal.org/node/2067323">Don't show empty vertical tabs area if all vertical tabs are hidden</a></li>
</ul>

I was also able to meet and talk to some really awesome Drupal developers—many from Chicago and the surrounding areas, but also a bunch of people who I've met at past DrupalCons and was happy to say hello to again. Palantir provided a great atmosphere, and some amazing food (bacon donuts, good pizza, tasty sandwiches, schwarma, etc.), and even some fun games (though I was unable to stay long enough to enjoy them during the summit).

I learned a lot about Drupal 8's architecture—plugins, controllers and routes especially—and I'm excited about the things this new architecture will afford when building and migrating Drupal modules and sites (like easier/faster testing and more code portability!). While there have been legitimate gripes about the release timeline and API changes for Drupal 8, developers have a tendency to focus too much on what's missing and broken (negatives) during the current core development phase (remember D7's release cycle?), and not on the more positive meta-level view—Drupal 8 has a vastly-improved admin UI, responsive design throughout, first-class HTML5 support, a great template system, a very flexible plugin system, more sane APIs for dealing with entities and fields, etc.

We made good progress in moving Drupal 8 forward during the summit, but there's still a ways to go... And you can help! See: <a href="http://xjm.drupalgardens.com/blog/technical-debt-drupal-8-or-when-will-it-be-ready">Technical debt in Drupal 8 (or, when will it be ready?)</a> and help push out the first beta release!
