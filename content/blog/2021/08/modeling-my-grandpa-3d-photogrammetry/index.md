---
nid: 3100
title: "Modeling my Grandpa with 3D Photogrammetry"
slug: "modeling-my-grandpa-3d-photogrammetry"
date: 2021-08-25T14:10:36+00:00
drupal:
  nid: 3100
  path: /blog/2021/modeling-my-grandpa-3d-photogrammetry
  body_format: markdown
  redirects:
    - /blog/2021/highly-accurate-3d-model-my-grandpa-using-photogrammetry
    - /blog/2021/modeling-my-grandpa-highly-accurate-3d-photogrammetry
aliases:
  - /blog/2021/highly-accurate-3d-model-my-grandpa-using-photogrammetry
  - /blog/2021/modeling-my-grandpa-highly-accurate-3d-photogrammetry
tags:
  - 3d
  - 3d printing
  - photogrammetry
  - photography
  - video
  - youtube
---

Today I released a video about how—and why—I 3D Printed my Grandpa and put him on my bottle of ketchup. [Watch it here](https://www.youtube.com/watch?v=7-om1dxKbN4).

I sculpted a bust of my Grandpa in high school, gave it to my grandparents, got it back after he died and my Grandma moved out of her house (I wrote a [tribute to my 'Grandpa Charlie'](/blog/2014/grandpa-charlie)), and I kept on moving it around my office because I didn't have room for it:

<p style="text-align: center;">
{{< figure src="./grandpa-bust-terracotta-jeff-geerling-original.jpeg" alt="Grandpa bust - terracotta by Jeff Geerling in 2001 - original statue" width="480" height="463" class="insert-image" >}}<br>
<em>Grandpa by Jeff Geerling, terracotta, 2001.</em></p>

I decided it had to go, but asked my extended family if anyone wanted the statue (thinking it would be sad to destroy it). One enterprising cousin suggested he could 'copy' the statue in smaller form using **photogrammetry**:

  - I'd take many pictures of the statue
  - He'd convert it into a 3D model using software algorithms
  - He'd print a smaller (and _much lighter_) copy of the bust for any takers

The video above goes into more detail about the entire journey, but in this blog post I wanted to give some detail about the photogrammetry process itself.

{{< figure src="./jeff-looks-at-3d-printed-grandpa-ketchup-bottle.jpg" alt="Jeff Geerling looks at Grandpa 3D Printed Ketchup Bottle Topper" width="578" height="325" class="insert-image" >}}

Coming into it, it seemed like some form of magic. And after generating a highly-detailed 3D model from a physical object with nothing but my camera and my laptop, it still feels like magic. But at least it's highly deterministic magic that can be grasped.

## Taking Pictures

Any Photogrammetry adventure begins with capturing photographs of a 3D object.

In my case, the object was a bust of my Grandpa, which weighed 16 lbs (7.26 kg) and was about 1 foot (30 cm) wide.

I could've set the bust on a surface and walked around taking pictures of it, relying on software to 'clean things up' for me.

But as a programmer, I know _garbage in equals garbage out_, and the cleaner the images, and the more precisely they are taken, the less work I'll have to do later cleaning up artifacts or touching up an imprecise model—at least that's my theory.

So I built a rotating turntable out of two round pieces of wood and a [lazy susan bearing](https://amzn.to/34c5Be1):

{{< figure src="./turntable-assemble.gif" alt="Assembling turntable or lazy susan using drill" width="347" height="220" class="insert-image" >}}

I set it up with a pure white background (a sheet of posterboard), and measured out 10° increments on a piece of tape I put on the DIY lazy susan, so I could rotate it precisely.

Finally, I took a series of 148 pictures, from four elevations:

{{< figure src="./grandpa-bust-spinning.gif" alt="Grandpa bust spinning - photogrammetry" width="480" height="320" class="insert-image" >}}

I pulled those pictures into the computer, tweaked the exposure a bit so the white background was blown out a tiny bit (pure white), and had a set of 24 megapixel JPEGs ready for the photogrammetry process—over 3.5 billion pixels of data to work with!

## First Attempts (Failures)

Since I have a Mac (a 2019 16" Macbook Pro with an i9 processor at the time), I don't have any Nvidia CUDA cores at my disposal (locally, at least). And it seems some of the more GUI-driven photogrammetry programs (which often require CUDA cores) are Windows-only.

But I eventually found the free and cross-platform app [Regard3D](http://www.regard3d.org), and I followed the official [tutorial](http://www.regard3d.org/index.php/documentation/tutorial). I was able to get a result, but the resulting 3D mesh was really messy:

{{< figure src="./regard3d-grandpa-spin.gif" alt="Grandpa Regard3D blobby goo model" width="415" height="325" class="insert-image" >}}

You could see my Grandpa, but he seemed to be frozen in a bed of goo. It would've required a lot of work in Meshmixer to get a faithful reproduction of the original bust.

I sent my cousin the same set of pictures, but was also having trouble getting a good initial model.

## Second Attempt: COLMAP + OpenMVS

Finally, I found [this blog post on COLMAP + OpenMVS](https://peterfalkingham.com/2018/04/01/colmap-openmvs-scripts-updated/) from Dr. Peter L. Falkingham. He wrote a `.bat` script that uses the two open source tools (on Windows, at least) to generate a 3D model from a set of images.

I needed to install COLMAP and OpenMVS, and luckily, I _also_ found an excellent Instructable by joecooning, [Free Photogrammetry on Mac OS: From Photos to 3D Models](https://www.instructables.com/Free-Photogrammetry-on-Mac-OS-From-Photos-to-3D-Mo/), and followed his instructions to install them:

### Install COLMAP

Download the latest `COLMAP-dev-mac-no-cuda.zip` file from the [COLMAP GitHub releases page](https://github.com/colmap/colmap/releases), expand it, and place COLMAP in the Applications folder.

### Install OpenMVS

  1. Install OpenMVS' dependencies [with Homebrew](https://docs.brew.sh/Installation): `brew install boost eigen opencv cgal ceres-solver`.
  2. [Install CMake](https://cmake.org/install/).
  3. [Install XCode](https://developer.apple.com/xcode/).
  4. Clone the VCG Library: `git clone https://github.com/cdcseacave/VCG.git vcglib`
  5. Clone OpenMVS: `git clone https://github.com/cdcseacave/openMVS.git`
  6. Create a separate build directory to build OpenMVS: `mkdir openMVS_build && cd openMVS_build`
  7. Build OpenMVS: `cmake . ../openMVS -DCMAKE_BUILD_TYPE=Release -DVCG_ROOT="`pwd`/vcglib" -G "Xcode"`
  8. Use xcodebuild to compile the app: `xcodebuild -configuration Release`

### Run `photogrammetry.sh`

Use [this shell script](https://gist.github.com/geerlingguy/7049523be6bbd3e7af3e9251a14b052b) (embedded below) to run the photogrammetry process inside a directory full of images of the object you wish to turn into a 3D model:

<script src="https://gist.github.com/geerlingguy/7049523be6bbd3e7af3e9251a14b052b.js"></script>

After running the script, the new 'model' directory should contain a `.jpg` texture map image, a `.mtl` (material settings) file, and an `.obj` (3D object) file.

I imported the `.obj` file in the free [Meshmixer](https://www.meshmixer.com) app, and WOW, it was pretty much dead-on... besides the fact that the object was upside-down:

{{< figure src="./colmap-openmvs-grandpa-spin.gif" alt="COLMAP OpenMVS grandpa object imported into MeshMixer" width="415" height="325" class="insert-image" >}}

## The Final Result

So I spent a bit of time cleaning up the bottom edges in Meshmixer, and doing a 'plane cut' to slice off the bottom and discard all the artifacts from the lazy susan/turntable. Then I made the object a solid (this isn't _strictly_ necessary for 3D printing, but it's easier to work with in my case) and exported it.

It looks pretty amazing, even capturing some of the tiny details that the naked eye would likely miss at a glance!

{{< figure src="./final-grandpa-meshmixer.gif" alt="Final Grandpa statue in Meshmixer from COLMAP and OpenMVS" width="453" height="407" class="insert-image" >}}

Here's one brief clip of a 3D print I made of this model (generated with [Octolapse and my Nikon D700](https://github.com/geerlingguy/3d-printing#octolapse-and-nikon-d700)):

{{< figure src="./3d-print-octolapse-tiny-grandpa-white.gif" alt="Octolapse timelapse of 3D Printing my Grandpa in white PLA with clock in background" width="225" height="210" class="insert-image" >}}

To see a ton more detail about the story behind this bust, and the different designs I made for my family, please [watch the video](https://www.youtube.com/watch?v=7-om1dxKbN4).
