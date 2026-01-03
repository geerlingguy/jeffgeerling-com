---
nid: 2679
title: "Changing the font for one character in a string on a Drupal site"
slug: "changing-font-one-character-string-on-drupal-site"
date: 2016-08-05T16:11:31+00:00
drupal:
  nid: 2679
  path: /blog/2016/changing-font-one-character-string-on-drupal-site
  body_format: markdown
  redirects: []
tags:
  - design
  - drupal
  - fonts
  - javascript
  - performance
---

File this under the "it's a very bad idea, but sometimes absolutely necessary" category: I was working on a site that wanted to use a particular font for headlines throughout the site, but the client detested one particular character (an ampersand), and requested any time that character were to occur in the page title, it would be swapped out for a different font.

If at all possible, you should avoid doing what I'm about to describe—but in the off chance you need to have an automated way to scan a string of text and change the font family for one particular character, this is what to do:

First, you need to create a special CSS class that you can apply to the individual character, so in your theme's CSS, add something like:

```
# This style already existed, but had the ugly &.
h1 {
  font-family: "NormalFont", Helvetica, Arial, sans-serif;
}

# This is the style we'll apply to & characters.
.ampersand-character {
  font-family: "MuchNicerFontForAmpersands", Helvetica, Arial, sans-serif;
}
```

Then, add a JS file like the following to your theme (in Drupal 8, you'll need to add it to your `themename.libraries.yml` file to apply it globally), in my case as a file in my theme folder `js/character-replacer.js`:

```
/**
 * @file
 * Character replacer.
 */

(function ($, Drupal, drupalSettings) {

  Drupal.behaviors.characterReplacer = {

    attach: function (context) {
      this.ampersandSpanWrap($("h1"));
    },

    ampersandSpanWrap: function (element) {
      var letters = element.html().split("");
      var text = "";

      for (var i in letters) {
        if (letters[i] == "&") {
          text += '<span class="ampersand-character">&</span>';
        }
        else {
          text += letters[i];
        }
      }
      $(element).html(text);
    }

  };

})(jQuery, Drupal, drupalSettings);
```

Measuring the performance of this little function, it takes around .9 ms per `<h1>` element (average ~30 characters) on a 2013 MacBook Air with a mobile i7 processor on FireFox, Chrome, or Safari. You could technically apply this to all sorts of text strings on your site, but use it sparingly, because it will definitely impact front-end performance—especially on slower mobile devices!

This also causes a very brief repaint of the page as the `<span>`s are inserted and the font face is swapped out by the browser, so keep that in mind!
