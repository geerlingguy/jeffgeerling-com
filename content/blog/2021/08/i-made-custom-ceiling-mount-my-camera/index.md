---
nid: 3124
title: "I made a custom ceiling mount for my camera"
slug: "i-made-custom-ceiling-mount-my-camera"
date: 2021-08-18T14:00:20+00:00
drupal:
  nid: 3124
  path: /blog/2021/i-made-custom-ceiling-mount-my-camera
  body_format: markdown
  redirects: []
tags:
  - camera
  - design
  - made
  - makerspace
  - metal
  - mount
  - openscad
  - saint louis
  - youtube
---

I shoot the 'A-roll' for my YouTube videos with a [Sony a6000](https://amzn.to/3m8UzAD) and a small [Glide Gear TMP 75 smartphone teleprompter](https://amzn.to/37NyXBs):

{{< figure src="./tripod-setup-teleprompter-a6000-sony-jeff-geerling.jpg" alt="Tripod setup with teleprompter and Sony a6000" width="600" height="338" class="insert-image" >}}

Until recently, I had these mounted on a tripod just off the back corner of my desk:

{{< figure src="./tripod-in-the-way-office-youtube.jpg" alt="Tripod in the way" width="600" height="338" class="insert-image" >}}

Some people mount semi-permanent camera rigs on a pole on their desks ([example](https://www.youtube.com/watch?v=xrWpkZix_sI)), but my adjustable-height desk (by UPLIFT) is not rock solid, so sometimes when I'm typing or accidentally bump the desk, anything mounted to the desktop wobbles.

For lights, monitors, etc., a little wobble isn't a problem. But even with image stabilization in my camera, the wobble becomes noticeable if I have the camera physically attached to my desk.

So I've been using a tripod. Only problem is my little 12' x 12' office is _not_ set up to be a YouTube studio. I [built it in 2014](/blog/2014/basement-home-office-build), and at the time video production was not even on my radar.

## Idea: TV Ceiling Mount

I stopped looking at dedicated camera mounting arms and truss systems once I realized they'd cost at least a couple hundred dollars—and the low end of the price range includes the weaker systems that I wouldn't trust with my $1000 camera rig!

Having mounted many TVs before, I realized TV ceiling mounts are cheap, sturdy, and available darn near everywhere. I bought [this VideoSecu ceiling TV mount](https://amzn.to/3xPNHud) for $37, and decided there _must_ be a way I could hack together some sort of rigid mounting plate for it, with a platform for the camera and a tripod screw underneath.

Here's what the base of the mount looks like without the VESA mounting adapter plate attached:

{{< figure src="./videosecu-ceiling-mount-plate-bottom.jpg" alt="The bottom mounting bracket for the VideoSecu ceiling TV mount" width="407" height="298" class="insert-image" >}}

## Can I 3D Print it?

I initially considered a fully-3D-printed mount, with a lot of support material and a large amount of infill. I've [dialed in my 3D printing setup](https://github.com/geerlingguy/3d-printing) now, and am confident I could get a good print. But I just won't trust a 5 pound camera rig on a plastic printed part.

I knew metal was the best option, but I didn't know how I'd make a bracket thick enough with the tools I had.

I have a small sheet metal folding tool and some aviation snips, but I can only use that on relatively thin metal—16 gauge, or about 1.5mm. I would need at least 3mm if I wanted to be confident in the strength of my bracket.

## Designing the part in OpenSCAD

I used a sheet of paper and made up a template for what I wanted the final plate to look like:

{{< figure src="./paper-template-mounting-bracket.jpeg" alt="Paper template of ceiling mounting camera plate" width="575" height="432" class="insert-image" >}}

I wanted a lot of adjustability, so I decided:

  - The tripod screw would be in a long channel, so the camera could be mounted closer or further from the ceiling mount pole—essential for potential upgrades to a larger teleprompter or camera in the future.
  - The mounting screws would have an arc so the whole mount could be tilted forward or backward, allowing many axes of adjustability once everything's mounted up.

I decided to use [OpenSCAD](https://openscad.org) to do the modeling, since it's open source and it lends itself to quick designs for simple parts like this.

After a couple hours, I was satisfied I had captured the dimensions for the plate:

{{< figure src="./openscad-model-of-plate.jpg" alt="OpenSCAD - design of camera mounting plate" width="576" height="324" class="insert-image" >}}

I also opened it up in Meshmixer to quickly plane cut the part and 'bend' it virtually so I could see what the final part would look like—assuming I found a way to bend 3mm steel!

{{< figure src="./final-3d-part-meshmixed.jpg" alt="Meshmixer final 3D part" width="501" height="271" class="insert-image" >}}

Since I have a 3D printer, I decided to print the final result for a dry-fit, and it fit great:

{{< figure src="./3d-printed-bracket-on-mount.jpg" alt="3D printed bracket on mount" width="399" height="233" class="insert-image" >}}

But it was _definitely_ not sturdy enough for a camera rig!

## Getting it MADE

At this point, I was exploring the possibility of buying a brake rated for 3mm steel, but found the options (at least for quality equipment I'd be able to use for years) too expensive to justify. I also didn't have a solution for cutting the steel that didn't involve a lot of painful abuse of my power tools meant more for woodworking.

So I asked on Twitter, and [Sam Wronski](https://twitter.com/runewake2/status/1418440462545801220) pointed me to [MADE](https://madestl.com), a local makerspace in St. Louis—I had no clue we had anything like it, besides [Arch Reactor](https://archreactor.org)!

{{< figure src="./made-stl-sign.jpg" alt="MADE STL Sign" width="510" height="287" class="insert-image" >}}

When I looked at their [equipment list](http://madestl.com/equipment/), I spotted the two machines I needed:

  1. A waterjet capable of cutting any flat shape out of darn near any material.
  2. Industrial-sized brakes capable of bending any of the sheet steel I could imagine using.

To use the machines, I'd need to take a training _and_ become a member, but I wanted to get this done quickly so I could get the tripod off my office floor, so I opted for a special service they offer called [Custom MADE](https://madestl.com/customMADE/).

My project was so simple it's almost a joke compared to the elaborate projects they often take on, but it is really nice to be able to take an idea and project description, pay someone a little money, and have a working part within a short time.

And so that's what I did, and I have a whole video about the process on my YouTube channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/x-NmktQ9nBE" frameborder='0' allowfullscreen></iframe></div>
</div>

After the part was made, I tapped a 1/4"-20 hole in it with my humble little [Irwin set](https://amzn.to/3iWaP68), and put in a tripod screw from my [SmallRig tripod screw kit](https://amzn.to/3z18bkY).

I mounted the bracket on the arm, and mounted the camera and teleprompter to it. At the same time, I also mounted my microphone (a [Sennheiser MKE 600](https://amzn.to/3y64ZU5) shotgun) to the pole using a [Manfrotto Super Clamp](https://amzn.to/3g7q4qQ) and [Articulated Arm](https://amzn.to/37QRXyV), and now my entire recording setup is up in the air, out of the way, ready at a moment's notice:

{{< figure src="./final-camera-ceiling-mount-rig-with-mic.jpeg" alt="Final camera rig with shotgun mic ceiling mounted" width="600" height="450" class="insert-image" >}}

The 3D bracket file and OpenSCAD source are on [Thingiverse](https://www.thingiverse.com/thing:4934969), so anyone else who might want to build a similar ceiling-mounted camera rig could do so... though you'd need to access a waterjet and metal brake if you want to make it out of sturdy metal!
