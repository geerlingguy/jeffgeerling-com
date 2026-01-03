---
nid: 2365
title: "Finding an Image's width/height dimensions using JavaScript"
slug: "finding-images-widthheight"
date: 2012-04-18T19:55:41+00:00
drupal:
  nid: 2365
  path: /blogs/jeff-geerling/finding-images-widthheight
  body_format: full_html
  redirects: []
tags:
  - code
  - image
  - javascript
  - jquery
  - properties
  - snippets
aliases:
  - /blogs/jeff-geerling/finding-images-widthheight
---

For a complex Drupal node form I've been working on for flocknote, I have a relatively complicated image switching functionality that lets people change an imagefield on the node (either when creating a new one or editing an existing node), and once the imagefield is changed, some custom jQuery code will grab that image and display it in the form, for a very WYSWIYG-like experience (the node looks almost exactly the same when editing/adding as it does once the user saves the node).

One problem is that images can be arbitrarily high (though they're resized to 600px wide), and I can't easily get the height of the image through any traditional means. If I were grabbing an already-saved imagefield image, I could throw the image height into the JS settings for the page. However, getting a dynamically-added image's height/width values is surprisingly tricky using JavaScript, at least if you take a look around the web and try using many people's suggestions (which work great if the image was already loaded with the page's content, but not if the image is dynamically added, or if the image hasn't yet loaded on the page.

The advantage of using the code below, which uses the onload method to make sure the image has been loaded before it retrieves the image's dimensions, works with remote images, already-loaded images, and dynamically-added images, which may not be loaded by the time your jQuery/Javascript is run. (Of course, it uses a tad bit more memory, and might take a tad bit extra time to reload the image, but it's a fine tradeoff for a node add/edit page, where content editors are okay with an extra half second).

Many other methods of getting image dimensions either work only with certain browsers (like naturalHeight/naturalWidth), and/or don't work in many cases (using .width() and .height() or clientWidth/clientHeight won't work if the image isn't fully loaded, and won't always get the dimension you're expecting).

So, here it is!

```
var theImage = new Image();
theImage.src="http://www.example.com/testImage.jpg";
theImage.onload = function() {
  console.log(theImage.height);
  console.log(theImage.width);
};
```

Basically, we create a new Image, then set an onload function to get the image's height and width variables. You could also do other things inside the onload function (I actually change a variable and call another function in there on the node form I'm using this on). I've only tested this with Chrome, Safari and FireFox, but I think it should work fine in newer versions of IE as well.
