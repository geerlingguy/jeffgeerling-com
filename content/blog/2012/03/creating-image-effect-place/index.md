---
nid: 2357
title: "Creating an Image Effect to put a play button on Video thumbnails"
slug: "creating-image-effect-place"
date: 2012-03-09T05:03:20+00:00
drupal:
  nid: 2357
  path: /blogs/jeff-geerling/creating-image-effect-place
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - filters
  - gd
  - image
  - image effects
  - input formats
  - php
  - video
aliases:
  - /blogs/jeff-geerling/creating-image-effect-place
---

I had a rather interesting feature to implement on <a href="http://www.flocknote.com/">flocknote</a> lately (after doing a pretty vast redesign of the UX/UI on the site over the past month... it was refreshing to dig into PHP again!):

We want to allow insertion of YouTube and Vimeo (and potentially other) videos into 'Notes' on the site, and there are a few moving parts in this equation:

<ul>
<li>I had to create a text format filter similar to the 'Embedded media inline' module in Drupal 6 so people could simply put a 'merge tag' in their Note (like <code>[video=URL]</code>) where they want the video to appear.</li>
<li>When a user views the embedded video on the site, the video should show at a uniform width/height, and be able to play the video (basically, a merge tag the user enters should be converted to the proper embed code for the provider (in this case, an <code><iframe></code> with the proper formatting).</li>
<li>When a user sees the video in the note email, the video can't actually play since very few email clients support any kind of video embedded in an email. So, instead, the video shows as a frame with a play button on top (this is the trickiest part), and links to the video on YouTube, Vimeo, etc.</li>
</ul>

<h3>Creating my own Image Effect for a Video Play Button</h3>

What I wanted to end up with was an image that had a custom-made iOS-style play button (play icon in a circle with a translucent grey background) right in the middle (I like the simple look of videos on my iPad...):

<p style="text-align: center;">{{< figure src="./video-play-button-example-resized.png" alt="Video Play Button Example" width="300" height="225" >}}</p>

So, I decided to work with Drupal's Image Effect API and expose a new image effect, aptly named 'Video Play Button', to Drupal's simple set of 'Resize, Scale, etc.' image effects. This is a pretty simple process:
<!--break-->

<ol>
<li>Implement <a href="http://api.drupal.org/api/drupal/modules!image!image.api.php/function/hook_image_effect_info/7">hook_image_effect_info()</a> to tell Drupal about the new effect.</li>
<li>Process the image (in <code>$image->resource</code>) in the 'effect callback' that you defined in hook_image_effect_info().</li>
</ol>

In my case, I calculated the center of the image to be processed, then subtracted half the play button's width and height (respectively) from the center dimensions, and used those dimensions, along with the image handle (<code>$image->resource</code>) and the play button image (I used drupal_get_path() to get the path to my custom module directory, and put the image in 'images/play-button.png') to build the final graphic using PHP GD library's <a href="http://php.net/manual/en/function.imagecopy.php">imagecopy()</a> function.

Here's the image effect info hook implementation and callback I wrote to put the play button on top of the image:

```
<?php
/**
 * Implements hook_image_effect_info().
 */
function mymodule_image_effect_info() {
  return array(
    'mymodule_video_play_button' => array(
      'label' => t('Video Play Button'),
      'help' => t('Adds a video play button in the middle of a given image.'),
      'effect callback' => 'mymodule_video_play_button_callback',
      'dimensions passthrough' => TRUE,
    ),
  );
}

/**
 * Video Play Button image callback.
 *
 * Adds a video play button on top of a given image.
 *
 * @param $image
 *   An image object returned by image_load().
 *
 * @return
 *   TRUE on success. FALSE on failure to colorize image.
 */
function mymodule_video_play_button_callback(&$image) {
  // Make sure the imagecopymerge() function exists (in GD image library).
  if (!function_exists('imagecopymerge')) {
    watchdog('image', 'The image %image could not be processed because the imagecopymerge() function is not available in this PHP installation.', array('%file' => $image->source));
    return FALSE;
  }

  // Verify that Drupal is using the PHP GD library for image manipulations
  // since this effect depends on functions in the GD library.
  if ($image->toolkit != 'gd') {
    watchdog('image', 'Image processing failed on %path. Using non GD toolkit.', array('%path' => $image->source), WATCHDOG_ERROR);
    return FALSE;
  }

  // Calculate the proper coordinates for placing the play button in the middle.
  $destination_x = ($image->info['width'] / 2) - 35;
  $destination_y = ($image->info['height'] / 2) - 35;

  // Load the play button image.
  $play_button_image = imagecreatefrompng(drupal_get_path('module', 'mymodule') . '/images/play-button.png');
  imagealphablending($play_button_image, TRUE); // Preserve transparency.
  imagealphablending($image->resource, TRUE); // Preserve transparency.

  // Use imagecopy() to place the play button over the image.
  imagecopy(
    $image->resource, // Destination image.
    $play_button_image, // Source image.
    $destination_x, // Destination x coordinate.
    $destination_y, // Destination y coordinate.
    0, // Source x coordinate.
    0, // Source y coordinate.
    70, // Source width.
    70 // Source height.
  );

  return TRUE;
}
?>
```

...and a PSD of the play button is attached, in case someone else wants to save themselves 10 minutes' drawing in Photoshop :)

There's another great example image effect, if you want to look at more examples, in the <a href="http://drupal.org/project/examples">Examples for Developers</a> modules' image_example.module.

<h3>imagecopy() vs. imagecopymerge()</h3>

...and Photoshop Save for Web vs. PNGOut optimization...

I spent almost an hour working on a couple different problems I encountered caused partly by the fact that I was using a compressed/optimized PNG file, and partly by the fact that I was misreading the PHP.net documentation for two GD library image copy functions, <a href="http://php.net/manual/en/function.imagecopy.php">imagecopy()</a> and <a href="http://php.net/manual/en/function.imagecopymerge.php">imagecopymerge()</a>.

First of all, instead of spending a ton of time struggling with weird file dimension issues, transparency issues, etc., and thinking your code is causing the problem—even though it may—also try different image files or try exporting the image file you're manipulating/using a different way. In my case, the image I was using was run through PNGout to remove any extraneous data, but apparently too much data was removed for PHP's GD library to understand the file correctly—in my case, the file's dimensions were distorted, the alpha transparency was not respected, and the image had lines of interpolation... all because I had tried to use an optimized PNG instead of the direct 'Save for Web...' image from Photoshop.

With regard to GD image functions, imagecopy() allows you to put one image on top of another one, hopefully preserving alpha transparency, etc., while imagecopymerge() puts an image on top of the other without preserving alpha transparency, but while allowing you to set the opacity of the source image manually (from 0-100%). I was originally trying to get imagecopymerge() to put a circle 'play' button (iOS-style) on top of the video image, but I found that the function was putting a square frame with a grey background instead of the nice transparent area around the circle. Switching to imagecopy() seemed to preserve the 24-bit PNG alpha transparency better.

<a href="https://bugs.php.net/bug.php?id=23815">This bug report on php.net</a> was especially enlightening when I was researching why imagecopymerge() wasn't working for me.

<h3>Conclusion</h3>

There are a few other moving parts to this equation, like retrieving the YouTube or Vimeo video frames, building the proper markup for different displays (on-site, email, mobile, etc.), etc., that I haven't gone into here, but I figured I'd share my experience creating a custom image effect here in case someone else wants to do something similar (like put watermarks on images for a photo site, or something like that).
