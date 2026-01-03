---
nid: 3121
title: "How to Export a 2D illustration of a 3D model in OpenSCAD"
slug: "how-export-2d-illustration-3d-model-openscad"
date: 2021-08-05T22:44:47+00:00
drupal:
  nid: 3121
  path: /blog/2021/how-export-2d-illustration-3d-model-openscad
  body_format: markdown
  redirects: []
tags:
  - 3d printing
  - design
  - export
  - model
  - openscad
  - pdf
---

I've been getting into [OpenSCAD](https://openscad.org) lately—I'd rather wrestle with a text-based 3D modeling application for more dimensional models than fight with lockups of Fusion 360!

One thing I wanted to do recently was model a sheet-metal object that would be cut from a flat piece of sheet metal, then folded into its final form using a brake. Before 3D printing the final design, or cutting metal, I wanted to 'dry fit' my design to make sure my measurements were correct.

The idea was to print a to-scale line drawing of the part on my laser printer, cut it out, fold it, and check to make sure everything lined up correctly.

Some online utilities took an STL file and turned it into a PNG, but they weren't great and most wouldn't output a PNG with the exact dimensions as the model (they printed too big or too small).

Here was my model:

{{< figure src="./tripod-adapter-plate-3d.jpg" alt="3D Model for Mounting Plate in OpenSCAD" width="700" height="395" class="insert-image" >}}

If I tried exporting a PDF or SVG of the model (File > Export > Export as PDF...), it understandably didn't know what to do:

{{< figure src="./error-openscad-not-a-2d-object.png" alt="Error in OpenSCAD - object is not a 2D object" width="438" height="239" class="insert-image" >}}

To get something exportable, I just added `projection()` at the top of my model to turn the top-down view into a 2D projection, then Rendered the object. Now it shows up as a 2D plane drawing:

{{< figure src="./tripod-adapter-plate-2d.jpg" alt="2D projection of 3D object in OpenSCAD" width="700" height="395" class="insert-image" >}}

And now the 'Export as PDF...' option (as well as the other 2D options like SVG) works great, allowing me to save a to-scale PDF suitable for reference or printing:

{{< figure src="./2d-pdf-of-openscad-3d-object.png" alt="2D PDF output of OpenSCAD 3D model projection" width="794" height="570" class="insert-image" >}}

I decided to put up this blog post in the hopes it might help someone else doing the same thing. My DDG searches weren't quite coming up with anything besides a few old GitHub issues.

Now I'm thinking of how much easier many of my Illustrator drawings would be if I just programmed them in OpenSCAD...
