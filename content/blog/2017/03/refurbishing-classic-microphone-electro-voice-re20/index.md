---
nid: 2746
title: "Refurbishing a classic microphone - the Electro-Voice RE20"
slug: "refurbishing-classic-microphone-electro-voice-re20"
date: 2017-03-05T16:06:01+00:00
drupal:
  nid: 2746
  path: /blog/2017/refurbishing-classic-microphone-electro-voice-re20
  body_format: markdown
  redirects:
    - /blog/2017/refurbishing-classic-microphone-electro-v
aliases:
  - /blog/2017/refurbishing-classic-microphone-electro-v
tags:
  - audio
  - electro-voice
  - electronics
  - microphone
  - re20
  - repair
  - tutorial
---

In the world of radio and professional podcasting, there are fewer than a dozen 'go-to' microphones. Each of the classics (e.g. the [Shure SM7B](TODO), the [Neumann U87](TODO), or the [EV RE20](TODO)) has it's own advantages and a few marquee users, but one mic seems to rule the roost when it comes to versatility and ability to color almost any voice with the 'talk show' sound, and that's the EV RE20. 

<p style="text-align: center;">{{< figure src="./ev-re20-classic-black-and-white-microphone_0.jpg" alt="Electro-Voice RE20 classic black and white mounted in shock mount microphone EV" width="650" height="435" class="insert-image" >}}<br>
<em>The RE20 mounted in the <a href="https://www.amazon.com/Electro-Voice-309A-Suspension-Shockmount-RE27ND/dp/B003BQ2DKK/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=1bccb641114944550a49a079b3fbfef2">309A shockmount</a>.</em></p>

The RE20 is a dynamic mic, so you can shout at it without clipping, it's a hefty metal mic, so you can bang it up a bit without too much ill effect, and it has a neat 'Variable D' feature that allows you to talk straight on or at an angle without affecting the quality of your voice too much (other mics need a lot more practice in controlling distance and direction).

I've often wanted one of my own, but couldn't justify the half-a-grand price tag. Luckily, however, I know a few people in radio (RE20s are about as common in radio studios as Toyota Camrys are on the road!), and it seems most radio engineers have a box full of crusty old RE20s that have been dropped, popped, or shaken one too many times. I did some research, and found the most common issue with older mics was that the foam deteriorated to the point where the mic capsule would be freely rattling around inside the body of the mic, and as long as the circuits were good and the voice coil intact, you could restore it to like-new condition with about $30 worth of foam!

So I took a few of the worst-of-the-worst—the ones with 30+ years of abuse from a variety of AM and FM radio announcers—and set about trying to clean, refurbish, and re-foam them. Since there aren't any other comprehensive guides on the Internet on the procedure, I thought I'd document it here, once and for all.

> Note that Electro-Voice used to offer a rebuild-and-refoam service for about $75, shipping included. I called EV before starting this project to see what they offer, and apparently the price is now $230 (plus tax), and an additional $75 to replace the outer casing.

This project isn't for the faint of heart, but if you have an old 'baby rattle' (as some engineers call these messy old RE20s), it might be worth the DIY effort.

## Servicing the RE20

For starters, I found the RE20 Service Manual (helpfully available for download on the EV website!). I looked through all the details to make sure I knew what parts went where, and how to eventually reassemble everything (the wires need to be routed through a few different parts of the mic correctly, otherwise screwing together the parts will break the connections):

<p style="text-align: center;"><a href="./RE20%20Service%20Manual.pdf">{{< figure src="./ev-re20-service-manual-cover.jpg" alt="Electro-Voice RE20 Service Manual - Cover" width="325" height="455" class="insert-image" >}}</a><br>
<em>Click image above to download.</em></p>

Since it was obvious that the foam was the primary issue with the mics I had been entrusted, I looked around online and found that I could purchase the individual foam parts direct from Full Compass, an online audio distributor (there may be other sources, but Full Compass had a decent price and was quick to ship):

  - [Internal pop filter](http://www.fullcompass.com/prod/272935-Telex-F01U110421)
  - [Windscreen / surround foam](http://www.fullcompass.com/prod/272958-Telex-F01U264975)
  - [Rear internal foam pad](http://www.fullcompass.com/prod/272964-Telex-F01U153540)

I ordered the foam and waited a few days for the shipment. While I was waiting, I realized the head of the mic was retained by a _very_ tiny hex screw... which I didn't have. So I made sure I also acquired all the tools that would be needed for the rebuild—most I had on hand, but check to make sure you have everything in the list below before attempting a re-foam!

## Tools Required

  - [0.035" hex key](https://www.amazon.com/Bondhus-12101-Wrench-ProGuard-Finish/dp/B001HWCO22/ref=as_li_ss_tl?s=hi&ie=UTF8&qid=1488681869&sr=1-1&keywords=0.035+hex&linkCode=ll1&tag=mmjjg-20&linkId=ad35513c6c60b83775d1671acc5ed6e9) (note—this is _way_ smaller than most standard size hex kits include)
  - [9/64" hex key](https://www.amazon.com/Bondhus-12108-Wrench-ProGuard-Finish/dp/B002JG9L0I/ref=as_li_ss_tl?ie=UTF8&qid=1488682123&sr=8-6&keywords=9/64+hex&linkCode=ll1&tag=mmjjg-20&linkId=dca17fdd9bad799fc77985624a3b2d5b) (note—I actually used a T20 Torx bit instead, as I didn't have a 9/64" hex bit)
  - [1/8" flat head (slotted) screwdriver + #1 phillips screwdriver](https://www.amazon.com/Topzone-Pcs-inch-Mini-Screwdriver/dp/B0195TNSQO/ref=as_li_ss_tl?s=hi&ie=UTF8&qid=1488682180&sr=1-2&keywords=1/8%22+flat&linkCode=ll1&tag=mmjjg-20&linkId=851eff0c0fe3b5f5c1f7bfdb5185fdf1)
  - [Needle-nose pliers](https://www.amazon.com/Stanley-84-096-5-Inch-Needle-Plier/dp/B0001IW50Y/ref=as_li_ss_tl?s=hi&ie=UTF8&qid=1488682264&sr=1-1&keywords=needle-nose&linkCode=ll1&tag=mmjjg-20&linkId=384a464a1ed06851014e25926b1f4bb9)
  - [6" Cotton swabs](https://www.amazon.com/gp/product/B01H6C26RE/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=e2af837d452550a1b12b451e3519bef0) (for cleaning the grill mesh and details)
  - 91% Isopropyl alcohol (for cleaning)
  - [Soldering iron](https://www.amazon.com/Weller-SP80NUS-Heavy-Soldering-Black/dp/B00B3SG796/ref=as_li_ss_tl?s=hi&ie=UTF8&qid=1488581876&sr=1-24&keywords=soldering+iron&linkCode=ll1&tag=mmjjg-20&linkId=bec16c1c9807710d91d725b53bf73b33) (or a nice fancy [temperature-controlled soldering station](https://www.amazon.com/gp/product/B000BRC2XU/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=9d05fbe8542e85c4657d11144365cc14)
  - (Optional) [Solder wick](https://www.amazon.com/NTE-Electronics-SW02-10-No-Clean-Solder/dp/B0195UVWJ8/ref=as_li_ss_tl?s=hi&ie=UTF8&qid=1488581834&sr=1-6&keywords=solder+wick&linkCode=ll1&tag=mmjjg-20&linkId=a8cbb47b5f322470ff311846c399c749)

Other than these supplies, you should probably prepare a work surface and make sure you have something laid on top of it to collect all the icky foam bits that will drop out of the microphone (some dried out, some gooey) during the course of the teardown.

## Step-by-Step Pictoral Guide

{{< figure src="./ev-re20-head-hex-screw.jpg" alt="Electro-Voice RE20 remove head with hex screw" width="650" height="430" class="insert-image" >}}

There's a tiny 0.035" hex screw in the head of the microphone. You need to back this out at least a few turns (but don't need to pull out the screw all the way!).

{{< figure src="./ev-re20-mic-capsule-front-top.jpg" alt="Electro-Voice RE20 front of mic capsule" width="650" height="430" class="insert-image" >}}

Unscrew the head of the microphone by hand; you'll find the foam pop filter inside (unless it's completely disintegrated!, and once the head is off, you should also see the front of the mic capsule. Don't be alarmed if there's a bit of foam that falls out as well!

> Note: Be careful not to touch the front of the mic capsule; even when cleaning, be gentle in that area—the voice coil is exposed under a fine mesh filter, and you can even see (if you look closely) the finely-wound copper wire that picks up your voice. If it gets damaged, the mic capsule is toast, and you'll have a pretty dull-sounding paperweight. Only touch the mic capsule on the sides, never the top.

Now we need to get to work on the _bottom_ of the mic. First, you need to unscrew the reverse-threaded screw holding the male XLR connector in place. Loosen it ('lefty loosey'), but realize that loosening it will actually sink the screw _deeper_ into the mic body. I used a 1/8" flat precision screwdriver, along with needle-nose pliers around the barrel of the screwdriver to give a little extra torque.

{{< figure src="./ev-re20-pull-out-xlr-connector.jpg" alt="Electro-Voice RE20 pull out XLR connector with needle-nose pliers" width="650" height="430" class="insert-image" >}}

After making sure the retaining screw is sunk in all the way, you need to slide out the male XLR connector. This is probably the most nerve-wracking portion of the mic rebuild, because on most RE20s, the connector is fixed in place with a little paste (colored red on my mic), which could be brittle, sealing the connector in the end. I had to use needle nose pliers, and work the connector back and forth a bit to get it to break loose. There's a good chance, if you're using a lot of force, that you'll end up breaking one of the leads on the inside. Don't worry—you'll have to do some soldering later anyways!

{{< figure src="./ev-re20-foam-dust-falling-out.jpg" alt="Electro-Voice RE20 foam coming out of mesh screen rattling" width="650" height="430" class="insert-image" >}}

You'll probably start accumulating a good deal of disgusting disintegrated foam dust at this point—I kept tossing out sheets of packing paper that I was using to cover my work surface throughout the rebuild. This stuff is even nastier than regular old foam because you _know_ it contains the spittle and DNA of all the talent who used it over the years!

{{< figure src="./ev-re20-hex-screw-retaining-base.jpg" alt="Electro-Voice RE20 hex screw retaining mic base" width="650" height="395" class="insert-image" >}}

{{< figure src="./ev-re20-t20-star-bit-hex-screw.jpg" alt="Electro-Voice RE20 hex screw removed with Torx T20 bit" width="650" height="442" class="insert-image" >}}

Use an 9/64" hex key (I ended up using a T20 torx bit because I'm missing my 9/64" hex key!) to unscrew the screw retaining the bottom end of the mic. Use a flashlight to find it—it's pretty dark inside the end of the mic!

{{< figure src="./ev-re20-remove-base.jpg" alt="Electro-Voice RE20 remove base of mic with tape and plumber wrench" width="650" height="430" class="insert-image" >}}

Carefully pull off the bottom part of the mic. Since mine was on tight, I tried breaking it loose with my plumbing pliers...

{{< figure src="./ev-re-20-patina-stripped-pliers.jpg" alt="Electro-Voice RE20 stripped part of finish with pliers" width="650" height="428" class="insert-image" >}}

...and ended up stripping a little of the finish off in the process! Ah well, adds to the patina.

{{< figure src="./ev-re20-tri-wing-aluminum-screw-adapter-grounding.jpg" alt="Electro-Voice RE20 tri-wing aluminum screw adapter in mic base" width="650" height="430" class="insert-image" >}}

Next up, there are three phillips screws retaining the plastic mic circuit assembly. Unscrew the screws with a #1 Phillips-head screwdriver, then unwind the copper ground wire from the post that's integrated into this tri-wing metal piece. This metal adapter is basically a bridge that allows the bottom retaining hex bolt to hold firmly against the rest of the mic.

{{< figure src="./ev-re20-wires-inside-mic-circuit-housing-area.jpg" alt="Electro-Voice RE20 wires inside mic housing in base circuit" width="650" height="421" class="insert-image" >}}

After the metal retaining clip is out of the way, you need to slide off the (hopefully) loose heat shrink wrapping the purple and black wires, and make sure the copper ground wire is also free. These wires need to be able to extend into the body of the mic as they're connected to the capsule—which will need to slide out the other end of the mic body soon!

{{< figure src="./ev-re20-mic-capsule-free-of-body.jpg" alt="Electro-Voice RE20 mic capsule free from the body with disgusting foam" width="650" height="430" class="insert-image" >}}

Now that the wires are free, carefully (and slowly) slide the large mic capsule out the other end of the body of the mic. You'll need to pull a little, then feed the three wires (copper, purple, black) through the little hole in the plastic circuit housing, then pull more, then feed, etc. until the mic capsule is free from the body casing.

This is the step where it's apparent _just how badly the foam has decayed_. Compare the few bits of foam here to the new foam sleeve later in this post—the old stuff is nasty, and almost completely deteriorated! In the future, it is probably a good idea to re-foam the mic every 5 or 10 years at the most. Or just use it 'till it rattles again then throw it away!

{{< figure src="./ev-re20-mic-barrel-empty-with-wires.jpg" alt="Electro-Voice RE20 mic capsule empty with wires inside" width="650" height="430" class="insert-image" >}}

If you look down the now-empty mic barrel, you'll see the three little wires exit through a nasty foam-encrusted hole in the plastic circuit housing.

{{< figure src="./ev-re20-comparison-new-foam-old-nasty-foam.jpg" alt="Electro-Voice RE20 mic capsule next to new foam" width="650" height="430" class="insert-image" >}}

Here's a picture of the new foam we'll be installing later. Notice how it's not in tiny flecks of nasty gooey mess? That's how the old foam looked when the mic was new!

{{< figure src="./ev-re20-circuit-housing-pried-loose.jpg" alt="Electro-Voice RE20 mic circuit with wires" width="650" height="430" class="insert-image" >}}

At this point, you need to unsolder the purple and black wires from the plastic circuit housing, so the mic capsule can be _completely_ removed from the body of the mic. (If you have trouble unseating the plastic circuit housing, use patience and a tiny flat-head screwdriver to pry opposite sides until it budges—it's just a friction fit).

{{< figure src="./ev-re20-soldering.jpg" alt="Electro-Voice RE20 - soldering iron to remove leads" width="650" height="430" class="insert-image" >}}

{{< figure src="./ev-re20-soldering-point.jpg" alt="Electro-Voice RE20 - soldering iron to remove leads 2" width="650" height="452" class="insert-image" >}}

Yikes, my old Radio-Shack soldering iron makes an appearance! I usually use my nicer [Weller soldering station](https://www.amazon.com/gp/product/B000BRC2XU/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=2775c882be3c889925bd9217d631106b), but I needed a quick iron to remove these bits, and was far away from my workshop when I was rebuilding this mic. Any old soldering iron will do, as long as you have a small tip. [Solder wick](https://www.amazon.com/NTE-Electronics-SW02-10-No-Clean-Solder/dp/B0195UVWJ8/ref=as_li_ss_tl?s=hi&ie=UTF8&qid=1488581834&sr=1-6&keywords=solder+wick&linkCode=ll1&tag=mmjjg-20&linkId=a8cbb47b5f322470ff311846c399c749) isn't strictly required, but it's easier to wick away the old solder and then use new clean solder on the posts later.

{{< figure src="./ev-re20-circuit-crud-foam.jpg" alt="Electro-Voice RE20 goop on circuit plastic housing" width="650" height="398" class="insert-image" >}}

After you wiggle the wires out through the tiny hole in the circuit housing, you can pull it out, and see the full extent of the decayed foam. Some will remain permanently 'gooed' onto the plastic, even after repeated cleanings. Luckily, we'll put in some brand new foam to make sure the last remnants of goop don't fall out when you shake the mic in the future!

{{< figure src="./ev-re20-foam-crud-inside-body.jpg" alt="Electro-Voice RE20 foam goo stuck inside barrel of mic" width="650" height="430" class="insert-image" >}}

And with the mic capsule and plastic circuit housing removed, you can finally look down the empty barrel of the mic and see even more foam stuck to everything! Luckily, with everything removed, cleaning it out once and for all is finally possible.

And... IT'S CLEANUP TIME! Finally, after all this teardown, you can start rebuilding and reassembling everything.

{{< figure src="./ev-re20-head-of-mic-dented-mesh-filter.jpg" alt="Electro-Voice RE20 head of mic dented mesh" width="650" height="430" class="insert-image" >}}

First things first, let's take care of the dent in the front mesh screen of the mic. I held it in my hand, and bashed the inside with the blunt rubber end of my screwdriver until the mesh looked pretty close to the original shape.

{{< figure src="./ev-re20-head-not-dented-anymore-still-dirty.jpg" alt="Electro-Voice RE20 head of mic not dented but still pretty dirty" width="650" height="430" class="insert-image" >}}

Ahh... much better!

{{< figure src="./ev-re20-foam-goop-and-toothbrush.jpg" alt="Electro-Voice RE20 foam goop after a good tooth brushing" width="650" height="430" class="insert-image" >}}

You might be forgiven for throwing up a little after cleaning the grill—this picture was taken after cleaning all the parts with just a dry toothbrush. **Be _very_ careful to not touch the head of the mic capsule, and use caution around any connections on the capsule itself!**

{{< figure src="./ev-re20-before-cleaning.jpg" alt="Electro-Voice RE20 Nasty old mic mesh grill" width="650" height="430" class="insert-image" >}}

{{< figure src="./ev-re20-after-cleaning.jpg" alt="Electro-Voice RE20 mic mesh grill cleaned with cotton swab" width="650" height="430" class="insert-image" >}}

You can see what a massive difference you can make just scrubbing the mic mesh grill with a few dozen cotton swabs and rubbing alcohol does. There's at least three decades worth of grit and grime in there, and using a toothbrush doused in alcohol, as well as a ton of long cotton swabs, I was able to get it restored to something resembling metal. Patience is key here—if you want to ever touch the thing without fear of getting sick, you gotta get into every little nook and cranny.

{{< figure src="./ev-re20-new-foam-ready-to-go.jpg" alt="Electro-Voice RE20 new foam windscreen" width="650" height="433" class="insert-image" >}}

The new foam is ready to go! The internal pop filter slides into the head of the mic quite easily, but you'll need to spend a bit more time getting the rest of the foam in place.

{{< figure src="./ev-re20-wires-through-long-foam-sleeve.jpg" alt="Electro-Voice RE20 wires on foam mic capsule sleeve" width="650" height="411" class="insert-image" >}}

Wrap the copper ground wire around the other two wires coming from the mic capsule, and carefully work them through the little opening in the large foam sleeve, while you slide the mic capsule into the sleeve. Yet again—be careful to only touch the sides, and not the top, of the mic capsule!

{{< figure src="./ev-re20-mic-in-foam-squish.jpg" alt="Electro-Voice RE20 mic capsule in squished foam" width="650" height="430" class="insert-image" >}}

In terms of delicate operations... this one isn't. You have to slowly but slightly-forcefully squish the foam-jacketed mic capsule into the body of the mic until it's all the way in. In the end, the foam should be squishing just a tiny bit out the sides, and the capsule should stand about .5 cm above the end of the mic body.

{{< figure src="./ev-re20-foam-in-other-end.jpg" alt="Electro-Voice RE20 foam in end of mic body" width="650" height="415" class="insert-image" >}}

After the capsule-and-foam-sleeve assembly is seated in the body, thread the 'rear internal foam pad' over the wires into the circular opening in the body.

{{< figure src="./ev-re20-resolder-wires.jpg" alt="Electro-Voice RE20 re-soldering wires from mic capsule" width="650" height="430" class="insert-image" >}}

Thread the purple, black, and copper wires through the opening in the plastic circuit body. This can be tricky, so take your time and use a tiny needle-nose pliers or a tiny screwdriver to thread it through. Then, re-solder the black and purple wires to the posts where they were originally soldered. Be careful to not get the posts too hot with the soldering iron—it seems they're only held to the rest of the plastic circuit holder via solder as well, and they can pop right off!

{{< figure src="./ev-re20-tri-wing-metal-adapter-screwed-in.jpg" alt="Electro-Voice RE20 tri-wing metal adapter screwed back in" width="650" height="430" class="insert-image" >}}

Mind the cables while you reposition the tri-wing aluminum screw plate over the plastic housing. Also, be careful when re-inserting the plastic housing in the mic body to make sure the EQ switch seats correctly in its slot. Unlike in the picture above, you should also screw one of the three machine screws _through_ the grounding wire lead, so it's grounded with the metal adapter (like it was prior to disassembly).

{{< figure src="./ev-re20-body-of-mic-repaired.jpg" alt="Electro-Voice RE20 body of mic after foam repair" width="650" height="430" class="insert-image" >}}

At this point, I also screwed on the head of the mic, just to provide a little extra protection to the front of the mic capsule. Even without the tail end and XLR connector, this thing is looking ten times better than before!

{{< figure src="./ev-re20-xlr-adapter-end-holes-remount.jpg" alt="Electro-Voice RE20 end XLR sleeve adapter cables" width="650" height="430" class="insert-image" >}}

The last step is also a bit tricky, especially if you snapped a couple of connections accidentally like I did. The stranded signal wires (red and green) are something like 24 or 26 gauge, and if they're old and brittle, they'll be very hard (if not impossible) to re-strip and reuse. Therefore, in my case, I pulled out some solid wire I normally use for Raspberry Pi and Arduino projects (I didn't have any stranded available—it would be a better fit here), and cut the same lengths as the existing wire, and stripped back about 0.5 cm of insulation. I soldered the ends to the plastic circuit assembly, then carefully threaded both wires through the hole just off the center of the bottom casing (this is a bit tricky with my 22 gauge wire!), and prepared to make the final solder joint, to the male XLR connector.

{{< figure src="./ev-re20-solder-xlr-connection-green-red.jpg" alt="Electro-Voice RE20 soldered female XLR connector" width="650" height="422" class="insert-image" >}}

I soldered the green and red wires to the proper pins on the male XLR connector, then carefully re-inserted it in the proper orientation into the barrel of the end of the mic (it only fits one way, orienting the key on the connector towards the index inside the barrel).

Push in the connector until you can see the flat-head screw through the hole in the side, then 'tighten' the screw (this will back out the reverse-threaded screw so the connector is fixed in place). Finally...

{{< figure src="./ev-re20-rebuilt-plugged-in.jpg" alt="Electro-Voice RE20 rebuilt and plugged into XLR cable" width="650" height="430" class="insert-image" >}}

SUCCESS! In this picture, the RE20 is plugged into my computer via a [Behringer U-Phoria UMC202HD](https://www.amazon.com/Behringer-UMC202HD-BEHRINGER-U-PHORIA/dp/B00QHURUBE/ref=as_li_ss_tl?ie=UTF8&qid=1488689033&sr=8-2&keywords=behringer+u-phoria&linkCode=ll1&tag=mmjjg-20&linkId=5ec02fc5b473c23c3a08ce544594d6a7) USB audio interface, and I tested it by recording samples into Sound Studio on my Mac:

{{< figure src="./sound-studio-recording-re20.jpg" alt="Sound Studio recording RE20 Electro-Voice RE320" width="650" height="385" class="insert-image" >}}

I tweaked the levels for this mic (plugged into the right channel of the U-Phoria) and another known-good RE20 (plugged into the left channel of the U-Phoria), and then did some test recordings in Sound Studio, and found that the levels and fullness of the sound were just as before, if slightly improved by having a continuous ring of foam holding the capsule in place!

## More Resources and Inspiration

I'm indebted to a ton of different forum topics and random tidbits I've read from audio engineers and DIY enthusiasts, in addition to helpful advice from [my dad](https://www.linkedin.com/in/josephgeerling/). Here are some of the posts where I found bits of information helpful in my journey towards repairing some old RE20s instead of buying new and dumping the old ones:

  - [GroupDIY post on RE20 replacement foam sources](https://groupdiy.com/index.php?topic=42371.0)
  - [Tape Op Message Board topic on replacing the RE20 foam](http://messageboard.tapeop.com/viewtopic.php?t=81171) (includes a great walkthrough and detailed pictures!)
  - [Gearslutz topic on RE20 foam replacement](https://www.gearslutz.com/board/so-much-gear-so-little-time/371862-diy-re20-filter-replacement-step-step-photos.html) (more pictures, though a bit blurry/low-res)
  - [RE20 Service Manual](http://www.electrovoice.com/downloadfile.php?i=971882)

Of course, if you read through this entire post and decided this kind of project isn't for you (especially considering a used RE20 might never sound as good as new even after full foam replacement!), you can always buy a new copy of the [Electro-Voice RE20 microphone](https://www.amazon.com/Electro-Voice-RE-20-Cardioid-Microphone/dp/B000Z7LLQ0/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=79bfbb602d4dd9069a574c4a219c907b) for a bit over $400 on Amazon! And if that's a bit too rich for your taste, the [RE320](https://www.amazon.com/EV-RE320-Variable-D-Instrument-Microphone/dp/B00KCN83VI/ref=as_li_ss_tl?ie=UTF8&qid=1488689426&sr=8-1&keywords=re320&linkCode=ll1&tag=mmjjg-20&linkId=8fe4837585746934a8cc23368f286996) has almost the same signature sound for about $120 less.
