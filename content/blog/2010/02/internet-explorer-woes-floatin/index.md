---
nid: 1860
title: "Internet Explorer Woes: Floating a Span using jQuery - Order Matters!"
slug: "internet-explorer-woes-floatin"
date: 2010-02-25T21:48:50+00:00
drupal:
  nid: 1860
  path: /blog/2010/internet-explorer-woes-floatin
  body_format: full_html
  redirects: []
tags:
  - bugs
  - css
  - floating
  - internet explorer
  - jquery
  - span
---

<p>
	I spent the greater part of two hours trying to debug an Internet Explorer bug today. Basically, I wanted to get an image that I uploaded to have a caption applied through jQuery. I used the Image Caption module for Drupal to do this, and set it to grab the &#39;alt&#39; text in a &lt;span&gt; underneath the image, and wrap both the image and caption inside another &lt;span&gt;, which would grab the float/alignment for the image, and use that to float it left or right (or neither).</p>
<p>
	Well, in Internet Explorer 6 and 7, the image would appear on its own line, as a block-level element. I tried everything short of throwing my computer against a wall to get this to work, but was unsuccessful. I finally went for broke and tried some thing so dumb that it couldn&#39;t possibly work&mdash;but it did.</p>
<p>
	I changed the order of the inline css properties in the script so the float would be applied before the &quot;display: block&quot; value. Bingo, IE works great!</p>
<p>
	Some things that I have to do to get things to work in Explorer... I hate you, Microsoft!!</p>
<p>
	You can view a page with the aforementioned image caption here: <a href="http://archstl.org/archstl/post/featured-st-louis-review-christian-marriage">Featured in the St. Louis Review: Christian Marriage</a>.</p>
