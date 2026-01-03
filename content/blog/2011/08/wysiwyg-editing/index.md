---
nid: 2332
title: "WYSIWYG Editing (contentEditable support) in iOS 5"
slug: "wysiwyg-editing"
date: 2011-08-27T18:28:41+00:00
drupal:
  nid: 2332
  path: /blogs/jeff-geerling/wysiwyg-editing
  body_format: full_html
  redirects: []
tags:
  - contenteditable
  - drupal
  - drupal 6
  - drupal 7
  - drupal planet
  - ios
  - ipad
  - iphone
  - tinymce
  - wysiwyg
---

I haven't seen much about this feature yet, so I figured I'd put it through its paces and share what I found. WYSIWYG editing on iOS devices is finally here! For a long time, contentEditable support has been lacking on iPads, iPhones, and iPod Touches, and it's been slightly annoying, as the only way to add richly-formatted text on these devices was doing a two-step through finding the carat characters and writing the HTML yourself.

Plus, some WYSIWYG editors (like TinyMCE) simply disabled the WYSIWYG from attaching to a textarea if it detected an iOS device. No longer, however: I've tested CKEditor (latest nightly) and TinyMCE (latest nightly), and both work perfectly (surprisingly well, in fact!) on the iPad running iOS 5 beta 6:
<p style="text-align: center;">{{< figure src="./ipad-2-wysiwyg-editing.png" alt="iPad 2 WYSIWYG TinyMCE Editing" width="575" height="431" >}}</p>
The above screenshot was taken while editing a page on a <a href="http://drupal.org/">Drupal</a> site (<a href="http://www.flocknote.com/">flockNote</a>) using the <a href="http://drupal.org/project/wysiwyg">WYSIWYG module</a> and the latest nightly build of <a href="http://www.tinymce.com/">TinyMCE</a>. You can get nightly builds under TinyMCE's 'Develop' section.

Demonstration:

Here's a video of me using TinyMCE on my iPad (it's fast, and works great!):
<p style="text-align: center;"><iframe width="640" height="390" src="http://www.youtube.com/embed/I3NQlwBOXpQ?rel=0" frameborder="0" allowfullscreen></iframe></p>


<h3>Some notes on WYSIWYG usage in iOS 5:</h3>

<ul>
	<li>To solve the problem of scrolling in WYSIWYG-enabled textareas, it looks like Apple decided to just expand the area to fit all the contents. So no scrolling whatsoever inside the body field.</li>
	<li>TinyMCE's resize widget doesn't work - it would be klunky if it did anyways, and the note above resolves any issues that would cause anyways.</li>
	<li>All the buttons I tested (image, link, bold/italic/underline, alignment, font color, style, table, etc.) worked perfectly, just as they would on a desktop computer.</li>
	<li>The only major annoyance is that the full onscreen keyboard pushes everything up, and a lot of scrolling up and down in the narrow viewport is required to format text. (However, if editing with an external keyboard, the onscreen keyboard doesn't hinder anything).</li>
	<li>The popover bubble that appears when you select text in the top couple of lines hides the WYSIWYG toolbar, so you might have to add a few carriage returns at the top of your post before making selections to the top few lines of text.</li>
</ul>

<h3>Other Wishes:</h3>

Now that iOS 5 seems to support rich text editing in the browser (a HUGE boon for online publishing in Drupal, Wordpress, Joomla, etc.), the only major flaw remaining is the inability to upload files (using the file select field). There's a workaround for this (at least, for Drupal: <a href="http://www.jeffgeerling.com/articles/web-design/post-photos-from-ipad-to-drupal">Post Photos/Images to Your Drupal Site from the iPad</a>), but it's too cumbersome. I really want to just be able to select a photo from my camera roll and attach it to a post from time to time.
