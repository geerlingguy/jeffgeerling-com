---
nid: 3374
title: "Import unsupported camera RAW files into Apple Photos"
slug: "import-unsupported-camera-raw-files-apple-photos"
date: 2024-05-13T02:59:58+00:00
drupal:
  nid: 3374
  path: /blog/2024/import-unsupported-camera-raw-files-apple-photos
  body_format: markdown
  redirects:
    - /blog/2024/how-add-sony-a7c-ii-raw-files-apple-photos
    - /blog/2024/how-import-unsupported-camera-raw-files-apple-photos
aliases:
  - /blog/2024/how-add-sony-a7c-ii-raw-files-apple-photos
  - /blog/2024/how-import-unsupported-camera-raw-files-apple-photos
tags:
  - adobe
  - apple
  - camera
  - conversion
  - dng
  - mac
  - photography
  - photos
  - raw
---

Many years ago, I decided to [migrate my photo library from Apple's now-defunct Aperture to Photos](/blog/2017/i-made-switch-aperture-photos), so I could take advantage of Apple's iCloud Photo Library (don't worry, I still have three full complete local backups, plus a separate cloud backup besides Apple's iCloud originals).

One pain point is RAW support. As camera manufacturers add new models, their proprietary RAW codecs are updated, and software vendors like Apple, Adobe, and Microsoft have to update photo editing tools to work with the new camera models.

I don't envy them this task, but as Photos was Apple's official successor to Aperture (a pale shadow to be sure, but it has its merits as a semi-decent library organizer), they've _generally_ done well supporting new camera models. The compatibility list for [macOS Sonoma, iPadOS 17, and iOS 17](https://support.apple.com/en-us/105094) is a testament to that effort.

However, Apple's been slower and slower adding new cameras to that list. It can take 6+ months after a camera's release before it's supported. If you use one of the new-but-unsupported camera models and shoot RAW, your photo library ends up looking a bit hodgepodge:

{{< figure src="./apple-photos-unsupported-raw-camera.jpg" alt="Apple Photos - pictures not appearing in library" width="700" height="auto" class="insert-image" >}}

In contrast, Adobe's been [consistent and quick in supporting new cameras](https://helpx.adobe.com/camera-raw/kb/camera-raw-plug-supported-cameras.html) from all the major manufacturers, sometimes less than a week after launch.

One solution (besides waiting indefinitely for Apple to add support) is to shoot in JPEG or use other tools (like the manufacturer's usually-weak official camera apps) to convert RAW files to JPEGs so Photos can see them. That's far from ideal, as RAW gives so much more post-processing and archival flexibility.

Some people resort to [tweaking the RAW file metadata with ExifTool](https://zekeweeks.com/2023/10/05/raw-file-support-workaround-for-sony-a7c-ii/) to make Apple's apps _think_ the files are from the A7C (v1), which allows them to be processed—though at a cost of tainting the metadata for those photos (what if you also have an A7C and wish to distinguish the files from each other at some point?).

I don't like that solution, but I was made aware of a nicer solution by [mecobutnot on Twitter/X](https://twitter.com/mecobutnot/status/1789712432971026772): use Adobe's free [Adobe DNG Converter](https://helpx.adobe.com/camera-raw/using/adobe-dng-converter.html) to convert the proprietary RAW files to Digital NeGatives (.dng), which are easy for Photos to read just the same as supported RAW files!

  1. Download and install [Adobe DNG Converter](https://helpx.adobe.com/camera-raw/using/adobe-dng-converter.html)
  2. Open DNG Converter and select the folder containing your A7C II's RAW image files
  3. Convert all the files to `.dng`
  4. Import all the converted `.dng` files into your Photos library

{{< figure src="./adobe-dng-converter.jpg" alt="Adobe DNG Digital Negative Converter" width="500" height="auto" class="insert-image" >}}

Bingo! Photos can now display the photos, scan them for faces, object, and text, and you can make adjustments or crops to the photos directly in your library.
