---
nid: 2869
title: "How to focus stack a set of images in Photoshop"
slug: "how-focus-stack-set-images-photoshop"
date: 2018-09-04T15:02:52+00:00
drupal:
  nid: 2869
  path: /blog/2018/how-focus-stack-set-images-photoshop
  body_format: markdown
  redirects: []
tags:
  - 105mm
  - focus
  - focus stacking
  - how-to
  - macro
  - nikon
  - photography
  - photoshop
  - tutorial
---

I recently rented a [Nikon 105mm VR Macro lens](https://www.amazon.com/Nikon-AF-S-Micro-NIKKOR-105mm-IF-ED/dp/B000EOSHGQ/ref=as_li_ss_tl?ie=UTF8&qid=1536072134&sr=8-1&keywords=105mm+vr&dpID=51gb9e-VESL&preST=_SX300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=0e627447b4117b2118b2210590b9b38c&language=en_US) for a weekend, and wanted to experiment with different types of macro photography.

One of the things I was most interested in was _focus stacking_. See, there's a problem with macro photography in that you're dealing with a depth of field measured in millimeters when reproducing images at a 1:1 ratio, even stopped down to f/8 or f/11. And, wanting to avoid diffraction at higher apertures, there's no way to take a straight-out-of-camera picture of a 3D object that's sharp from front to back.

(There's also a video version of this post, embedded below)

<div class="yt-embed"><style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/pinYVZxBF2Q" frameborder='0' allowfullscreen></iframe></div></div>

One frequent subject of my close-up photography is the Raspberry Pi single board computer. You can see the problem when taking just one photo:

{{< figure src="./raspberry-pi-depth-of-field-example.jpg" alt="Raspberry Pi at f/5.6 - blurred foreground and background" width="650" height="434" class="insert-image" >}}

The blurred out foreground and background can be a nice effect, if that's what you're going for... but if you wanted to have a clear representation of the entire product—say, for a catalog or for scientific purposes—this is not it. This image was taken at f/5.6 and 1/25 second exposure at ISO 800 (using available light).

## Taking pictures for a focus stack image

So, to combat this problem, we'll create a 'stack' of images, with the area in focus overlapping from frame to frame. At f/5.6, that area in focus is about 0.8 cm deep, so I set my camera in manual focus and exposure mode, locked it down on a tripod, and focused just on the front edge:

{{< figure src="./raspberry-pi-focus-stack-front-edge.jpg" alt="Raspberry Pi focus stack first image focused on front edge" width="650" height="434" class="insert-image" >}}

Next, I manually adjusted focus _just_ beyond, on the HDMI port and second group of circuits:

{{< figure src="./raspberry-pi-focus-stack-second.jpg" alt="Raspberry Pi focus stack second image focused on hdmi and circuits" width="650" height="434" class="insert-image" >}}

And so on and so forth, until I focused just on the back edge of the board (the metal USB ports):

{{< figure src="./raspberry-pi-focus-stack-last.jpg" alt="Raspberry Pi focus stack last image focused on USB ports" width="650" height="434" class="insert-image" >}}

Now that I have a set of 7 photos with overlapping areas in focus, I can import them and complete the post-processing in Photoshop. (Note that I usually tweak exposure and white balance in Lightroom or Photos before I export a set of JPEGs for Photoshop work).

## Simple focus stacking in Photoshop

  1. In Photoshop, go to File > Scripts > Load files into Stack...
  2. Select the photos you just imported, then before creating the stack, check the 'Attempt to automatically align source images' checkbox.
  3. After Photoshop creates the image with all the layers, use Shift to select all the layers in the Layers palette.
  4. Go to Edit > Auto-Blend Layers...
  5. Make sure the 'Stack' option is selected, and click OK.

After a minute or so (depending on the resolution and number of images you have in the stack), Photoshop will show you the end result, which in my case looks like the following:

{{< figure src="./raspberry-pi-focus-stack-macro-nikon-105mm.jpg" alt="Raspberry Pi focus stack final Photoshop post-processed image" width="650" height="434" class="insert-image" >}}

> Note: There are many situations where this kind of focus stacking will _not_ produce perfect results. In some cases, especially with more complicated plant life, you may need to spend a bit of time adjusting the masks on each of the layers before you can get an image that's acceptably sharp and without strange blur artifacts due to overlapping objects (e.g. a leaf that goes in front of and behind a vine).
