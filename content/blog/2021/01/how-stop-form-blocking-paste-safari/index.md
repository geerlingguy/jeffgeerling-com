---
nid: 3067
title: "How to stop a form from blocking paste in Safari"
slug: "how-stop-form-blocking-paste-safari"
date: 2021-01-18T15:16:06+00:00
drupal:
  nid: 3067
  path: /blog/2021/how-stop-form-blocking-paste-safari
  body_format: markdown
  redirects: []
tags:
  - console
  - forms
  - javascript
  - paste
  - safari
  - security
---

This is a quick blog post, mostly for my own reference.

I finally got sick of a certain government website thinking that preventing pasting passwords into certain forms was some sort of security feature, so I am documenting my workaround in Safari for stupid forms written by compliance-minded folks (the same who think that expiring passwords every 30 days leads to any kind of better security).

In Safari, select Develop > Show Javascript Console (or press ⌥⌘C, that's Option + Command + 'C')<sup>1</sup>.

Paste the following into the console and press 'Enter':

```
var allowPaste = function(e){
  e.stopImmediatePropagation();
  return true;
};
document.addEventListener('paste', allowPaste, true);
```

Now you can paste to your heart's content.

<sup>1</sup> If you don’t see the Develop menu in the menu bar, choose Safari > Preferences, click Advanced, then select “Show Develop menu in menu bar.”
