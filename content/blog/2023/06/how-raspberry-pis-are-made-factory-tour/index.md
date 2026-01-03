---
nid: 3287
title: "How Raspberry Pis are made (Factory Tour)"
slug: "how-raspberry-pis-are-made-factory-tour"
date: 2023-06-08T14:00:34+00:00
drupal:
  nid: 3287
  path: /blog/2023/how-raspberry-pis-are-made-factory-tour
  body_format: markdown
  redirects:
    - /blog/2023/how-raspberry-pis-are-made
aliases:
  - /blog/2023/how-raspberry-pis-are-made
tags:
  - factory
  - manufacturing
  - pi 4
  - raspberry pi
  - sony
  - tour
  - video
---

This blog post is one of the few instances where, no matter how much you prefer reading to watching a video... you're going to want to [watch the video](https://www.youtube.com/watch?v=k2C4lbbIH0c).

The day after I [interviewed Eben Upton, co-founder of Raspberry Pi](https://www.youtube.com/watch?v=-_aL9V0JsQQ), I went to the Sony UK Technology Centre in Pencoed, Wales to tour the factory where almost every Raspberry Pi has been made—_50,000,000_ of them (as of this month!).

{{< figure src="./10%20jeff%20pi%20milestones.jpeg" alt="Jeff - Raspberry Pi Milestones in Sony Technology Centre" width="700" height="467" class="insert-image" >}}

I got to snap a picture with the milestone Pis:

  - 1 million on September 30, 2013
  - 5 million on September 23, 2015
  - 10 million on September 8, 2016

And it looks like they're set to hit the 50 million milestone any day now. In a strange turn of events, it doesn't look like it'll land in September this time!

{{< figure src="./raspberrypi-sales-cumulative-2012-2023-jeffg-watermark.png" alt="Raspberry Pi sales chart - cumulative, SBC only, 2012-2023" width="700" height="326" class="insert-image" >}}

Data sources: [2012-2018](https://raspberrytips.com/raspberry-pi-history/), [2019](https://www.zdnet.com/article/raspberry-pi-now-weve-sold-30-million/), [2022](https://www.cam.ac.uk/stories/raspberrypi)

That milestone would've arrived a year or two ago had the Pi not been supply-constrained. Seeing that data makes me wonder whether the ramp will still be accelerating once they can make enough Pis to meet demand! (Also, this figure only includes Raspberry Pi SBCs—not the Pico or any other Pi products like cameras, keyboards, etc.).

On the factory floor—where they were making Pi Zero, Pi 3 model B+, Pi 4 model B, Compute Module 4, and Compute Module 4S at the time—the Pi's start as a set of blank PCBs with copper pads, and the first stop is the automated screen printing machine where solder paste is applied with a squeegee. In the picture below, Andrew Puntan (one of our guides, working at the factory for over two _decades_!) holds up the Pi 3 B+ stencil, and you can see me and Gordon Hollingworth admiring it's shiny surface:

{{< figure src="./03%20andrew%20holds%20pcb%20stencil.jpeg" alt="Andrew Puntan holds solder screen for Pi 3 B while Jeff Geerling and Gordon Hollingworth look on" width="700" height="467" class="insert-image" >}}

After the solder paste is applied, the PCB heads through the pick and place line. Between the solder application and the final baking, that line is part of Sony's Surface Mount Technology (SMT) department:

{{< figure src="./04%20pcbs%20with%20paste.jpeg" alt="Pi PCBs with Solder Paste" width="700" height="467" class="insert-image" >}}

Again, [watch the video](https://www.youtube.com/watch?v=k2C4lbbIH0c) if you're into this stuff... there's no way to convey the raw power of an industrial-scale pick-and-place machine in a still image.

{{< figure src="./07%20pick%20and%20place%20reels%202.jpeg" alt="BCM2711 on pick and place component reel" width="700" height="467" class="insert-image" >}}

But while I was there, I noticed they only had a few reels of the BCM2711 SoC that's the heart of every Pi 4—that's their current bottleneck. When they run out of the reel holding those shiny metal squares in the middle, they have to halt production. And sadly, that happens a lot, even though people are clamoring for Pis still, years into its production cycle.

I noticed at various points through the line, there were inspection stations, where a machine would take hundreds (maybe thousands?) of pictures of each Pi, and a computer would flag any component that was shifted even a _fraction_ of a millimeter, or any pad that didn't look like it was set _just so_:

{{< figure src="./09%20inspection%203d%20machine.jpeg" alt="Inspection in 3D on Sony's production line" width="700" height="467" class="insert-image" >}}

This particular display showed a neat 3D view, and you could watch as someone either remotely passed the board, or someone on the line would come and grab the board, make a notation, and put the board in a special hopper for closer inspection. That happened very infrequently while I was there, but there were a few.

After the surface mount line came one of the more visually impressive parts of the production line: the cluster of ABB robots:

{{< figure src="./11%20abb%20robot%20through-hole.jpeg" alt="ABB robot placing through-hole components" width="700" height="467" class="insert-image" >}}

These robots employ a distinctive 'wiggle' as they place Ethernet jacks, USB ports, GPIO pins, and the PoE header pins on the board. But they're not perfect—they get most of the way there, but they don't complete _every_ piece on the board—and sometimes one of the components isn't quite flat on the board.

{{< figure src="./14%20human%20through-hole%20cleanup.jpeg" alt="Human at end of robot through-hole placement line" width="700" height="467" class="insert-image" >}}

That's why there's a human at the end of this line, to finish off the through-hole placement, and give one final inspection before the selective soldering process finishes off the boards.

{{< figure src="./15%20pi%20baking%20preheat%20selective%20solder.jpeg" alt="Raspberry Pis baking in toaster oven" width="700" height="467" class="insert-image" >}}

At this point, the Pi pauses for a number of seconds over a 'toaster oven' style heating element, which warms the board, then _really_ turns up the heat (to something over 100°C), before it dips into a solder bath, finalizing the through-hole component installation. The video shows this process better—it's hard to show a single frame that conveys this process well.

{{< figure src="./molten-metal-solder-bath-selective-solder.jpeg" alt="Molten metal in the solder bath for Raspberry Pi 4 production line" width="700" height="467" class="insert-image" >}}

That's molten metal flowing in all those channels; a pump forces it against the underside of the board in a pattern that matches where all the through-hole components are located.

A process that _does_ come across in one frame is the complex maze of test jigs, with their 'bed of nails' upon which every Pi that goes through the line rests.

{{< figure src="./16%20pi%20bed%20of%20nails%20test%20jig.jpeg" alt="Bed of nails Raspberry Pi test jig" width="700" height="467" class="insert-image" >}}

Each jig actually has _another_ Raspberry Pi, which runs tons of automated tests against the Pi under test, ensuring every part of the Pi works perfectly. It's fascinating standing back and watching the many rows of test machines, with robots on tracks distributing Pis to different test jigs.

{{< figure src="./raspberry-pi-test-jigs-factory.jpg" alt="Raspberry Pi test jig farm in factory" width="700" height="394" class="insert-image" >}}

Then you can walk around to the back side and watch another set of robots fetching the Pis as they complete their tests, and then quickly shuffle them back to the conveyor.

The final conveyor heads down to the packing line. This part of the process was revamped and fully automated in the past couple years, and it uses some lessons learned from food packaging—the boxes are flat when they enter, and this pops them off a stack one at a time, then glues and bends into place most of the box structure in one fluid motion:

{{< figure src="./17%20packing%20flat%20containers.jpeg" alt="Box hopper" width="700" height="467" class="insert-image" >}}

A couple more stops and a manual, quick start guide, and the Pi are dropped in. Finally, a few simple bits of metal finish off the box folding process using the pressure of the box itself as its pushed down the line:

{{< figure src="./20%20packing%20glue%20and%20fold.jpeg" alt="Packing machine - glue and fold" width="700" height="467" class="insert-image" >}}

I feel like a broken record at this point... but [watch the video](https://www.youtube.com/watch?v=k2C4lbbIH0c), no photos will do it justice.

The final bit of the line is a machine that counts the boxes. 15 at once, it vacuums them up, then places them neatly into a shipping box:

{{< figure src="./21%20packing%20vac%20picker%20upper.jpeg" alt="Vacuum Pi lifter upper packing box" width="700" height="467" class="insert-image" >}}

Before this box was taped up, I was allowed to hold up one of the thousands of Pis made that day—though I had to replace it quickly, since every Pi being made right now is already accounted for _somewhere_ and needed to ship out soon!

{{< figure src="./jeff-hold-raspberry-pi-4-factory-production-line.jpg" alt="Jeff Geerling holds a Raspberry Pi on the production line at Sony UK" width="700" height="394" class="insert-image" >}}

Now, [go watch the video](https://www.youtube.com/watch?v=k2C4lbbIH0c).
