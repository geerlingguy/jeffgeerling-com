---
nid: 2732
title: "Can't upload more than 20 files using Media Image Entities in Drupal 8?"
slug: "cant-upload-more-20-files-using-media-image-entities-drupal-8"
date: 2017-01-14T21:56:55+00:00
drupal:
  nid: 2732
  path: /blog/2017/cant-upload-more-20-files-using-media-image-entities-drupal-8
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
  - image
  - media
  - php
  - upload
---

After [migrating an older Drupal 6 site with 20,000 media items to Drupal 8](//www.jeffgeerling.com/blog/2016/migrating-20000-images-audio-clips-and-video-clips-drupal-8), I found a strange problem with image uploads. On the Drupal site, using Image FUpload and Adobe Flash, I could upload up to 99 images in one go. On the new Drupal 8 site, I was only able to upload 20 images, even though I didn't see an error message or any other indication that the rest of the images I had selected through the Media Image upload form were not successfully added.

I could choose 21, 40, or 500 images, but only 20 were ever added to an album at any time.

There were no apparent warnings on the screen, so I just assumed there was some random bug in the Media Image Entity or Media module suite that limited uploads to 20 files at a time.

But due to an unrelated error, I glanced at the PHP logs one day, and noticed the following error message:

```
[Fri Dec 23 22:05:53.403709 2016] [:error] [pid 29341] [client ip.address.here:41316] PHP Warning:  Maximum number of allowable file uploads has been exceeded in Unknown on line 0, referer: https://example.com/entity-browser/modal/image_browser?uuid=b6e0c064758fc25f517d276e265585959f18361a&original_path=/node/add/gallery
```

Quite enlightening!

So looking at the [PHP docs for file uploads](http://php.net/manual/en/ini.core.php#ini.sect.file-uploads), it seems the default limit is 20 files. That's a bit low for a photo sharing site, so I decided to lift that limit to 250 for the benefit of family members who are a bit trigger-happy when taking pictures!

I edited `php.ini` and set the following directive:

    max_file_uploads = 250

And now I can upload to my heart's content, without manually batching uploads in groups of 20!
