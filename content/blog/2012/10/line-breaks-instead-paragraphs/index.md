---
nid: 2382
title: "Line breaks instead of Paragraphs in TinyMCE (by default)"
slug: "line-breaks-instead-paragraphs"
date: 2012-10-01T16:43:22+00:00
drupal:
  nid: 2382
  path: /blogs/jeff-geerling/line-breaks-instead-paragraphs
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - tinymce
  - wysiwyg
aliases:
  - /blogs/jeff-geerling/line-breaks-instead-paragraphs
---

Most people who have grown up on the web, and have used Wysiwyg utilities online, or newer text editors/word processing applications are used to having a simple 'return' create a new paragraph, with (on average) one extra line of empty space between the new paragraph and the one before it.

However, a lot of people like having the 'return' key just go down one line. There are a few ways this is possible in most Wysiwygs:

<ul>
<li>You can change the block style from 'Paragraph' (which creates <code><p></code> tags around new lines of text) to 'div' (which creates <code><div></code> tags around new lines of text).</li>
<li>You can press Shift + Return when you want to just go down one line (using a <code><br /></code> tag instead of a <code><p></code> tag).</li>
</ul>

I use the second method when I'm using a Wysiwyg, as I like using paragraphs (which are semantic for text, and which allow for better CSS styling than a monolithic block of text with linebreaks). I also rarely use a Wysiwyg editor, so it's not really an issue for me anyways ;-)

But, some people ask me if they can set up TinyMCE to use line breaks instead of paragraph returns by <em>default</em>, so they don't have to hit Shift + Return all the time (instead, they hit 'Enter Enter'... more keystrokes, but whatever floats their boat!).

Well, as it turns out, TinyMCE <em>does</em> have a setting for this, called <a href="http://www.tinymce.com/wiki.php/TinyMCE_FAQ#TinyMCE_produce_P_elements_on_enter.2Freturn_instead_of_BR_elements.3F"><code>forced_root_block</code></a>. And Drupal's Wysiwyg module allows you to pass along this setting to TinyMCE when TinyMCE is loaded on a page, using <code>hook_wysiwyg_editor_settings_alter()</code> like so (in a custom module):

```
<?php
/**
 * Implements hook_wysiwyg_editor_settings_alter().
 *
 * Sets defaults for TinyMCE editor on startup.
 */
function custom_wysiwyg_editor_settings_alter(&$settings, $context) {
  if ($context['profile']->editor == 'tinymce') {
    // Force linebreaks instead of paragraph returns.
    $settings['forced_root_block'] = FALSE;
  }
}
?>
```

