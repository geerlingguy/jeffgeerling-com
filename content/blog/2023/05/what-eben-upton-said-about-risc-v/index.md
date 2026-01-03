---
nid: 3285
title: "What Eben Upton said about RISC-V"
slug: "what-eben-upton-said-about-risc-v"
date: 2023-05-18T14:04:35+00:00
drupal:
  nid: 3285
  path: /blog/2023/what-eben-upton-said-about-risc-v
  body_format: markdown
  redirects: []
tags:
  - arm
  - eben upton
  - interviews
  - raspberry pi
  - risc-v
  - sbc
  - video
  - youtube
---

Earlier this month, I was able to discuss with Eben Upton (co-founder of Raspberry Pi) the role RISC-V could play in Raspberry Pi's future (among other things—[watch the full interview here](https://www.youtube.com/watch?v=-_aL9V0JsQQ)).

{{< figure src="./eben-upton-with-jeff-geerling.jpeg" alt="Eben Upton with Jeff Geerling" width="700" height="425" class="insert-image" >}}

To sum it up: Raspberry Pi is [currently a 'Strategic Member' of RISC-V International](https://riscv.org/members/), and they are working on multiple custom silicon designs—we've already seen their RP3A0 SiP chip and the RP2040, and they surely have more in the pipeline. Eben said currently there are no plans to move the Raspberry Pi SBC to RISC-V due to the lack of high-performance 'A-class' cores, but "never say never" when it comes to RISC-V architecture finding its way into a future Pi microcontroller.

{{< figure src="./eben-upton-talking-jeff-geerling-interview.jpg" alt="Eben Upton Raspberry Pi interview with Jeff Geerling" width="700" height="394" class="insert-image" >}}

> I tend to get flamed a little bit for saying this, but people will say, "Ah, but on GitHub, you can find this excellent core that is much more performant than anything I make."
> 
> But there really is a shortage of good, licensable high-performance [RISC-V] cores.

Indeed, any of the current crop of RISC-V SBCs perform about as well as the previous-generation Pi 3 model B. There are some higher-end designs, and companies like SiFive are building exciting hardware.

But as I mentioned in my [review of the StarFive VisionFive 2 SBC](/blog/2023/risc-v-business-testing-starfives-visionfive-2-sbc), the board's performance is generally worse than a Pi 3 B+, and even IO performance is slower; the PCIe Gen 2 bus ran slower than the comparable bus on a Compute Module 4 (250 MB/sec compared to 410 MB/sec).

{{< figure src="./eben-upton-talks-to-jeff-geerling-raspberry-pi-interview.jpg" alt="Eben Upton and Jeff Geerling at Raspberry Pi headquarters" width="700" height="394" class="insert-image" >}}

> Even the Arm world is pretty immature compared to the Intel world. The RISC-V world is immature compared to the Arm world. That can be overcome—and Arm overcame it, not completely, but to a sufficient degree. I'm sure RISC-V can do that, but it's going to take years.
> 
> There's a still a lack of maturity in the software stacks—in particular, bits of the Linux userland are not well optimized at the moment for RISC-V architectures.

In my testing of the VisionFive 2, I did experience the growing pains trying to compile and run software within Linux. It's not a _horrible_ experience (and certainly better today than a year ago!), but it did feel a lot like 'using Arm in 2013'; lots of software just won't compile yet, or needs a lot of hand-holding to run. And standardization is... not yet there.

Eben did mention a bright spot: 'M-class' cores for microcontrollers in particular:

> I do think there are opportunities for people to go build RISC-V microcontrollers. Would we do it, I don't know. I mean, the Arm value proposition is really strong, right? It's a really strong community. And it's not expensive to play.
> 
> Never say never. I think 'microcontroller' is more plausible than 'A-class'. A-class may become plausible in a few years, but M-class is definitely feasible and I definitely wouldn't commit to _not_ do it.

{{< figure src="./ian-cutress-jeff-geerling-london-uk.jpeg" alt="Ian Cutress - TechTechPotato with Jeff Geerling in London, UK" width="700" height="394" class="insert-image" >}}

This jives with my conversation with Ian Cutress (of [TechTechPotato](https://www.youtube.com/techtechpotato) and [More than Moore](https://morethanmoore.substack.com) fame):

> [Ian] One of the things RISC-V has right now issues with is standardization. The whole point about RISC-V is that it's this open source ecosystem where anybody can add anything. Now, if anybody can add anything, it means everybody doesn't support everybody else. So there has to be that next level of standardization.
>
> Arm already has that. Arm also has [SystemReady Certifications]. You know, server CPUs have to be [SystemReady SR] in order to support all sorts of Linux and different sorts of things. RISC-V is getting there, just not yet.
>
> So I wouldn't say Raspberry Pi would pivot to RISC-V. If they were to go down that route, it would be the add-on.

And I also asked Ian if he thinks RISC-V will prove an existential threat to Arm in the next decade.

> [Ian] RISC-V has a lot of potential, but it really does require the standards bodies getting on top of what the larger ecosystem wants. And if what the larger ecosystem wants right now is embedded IoT-type cores and designs, that's what they'll focus on until somebody starts saying, "Can we have a processor for a small board computer," or [asks] for something a bit more desktop-y, or something a bit more enterprise-y.

These opinions align with the sentiment I see repeated time and again; architecture is great. Clean-sheet designs are great. But as [this great Chips and Cheese article points out](https://chipsandcheese.com/2021/07/13/arm-or-x86-isa-doesnt-matter/): _Implementation matters, not ISA_.

Put another way, the entire ecosystem matters more than just chip architecture. Arm is not inherently better or more power efficient than X86 (though that is sometimes the case in individual chip designs). RISC-V is not inherently better, simpler, or easier to adopt than Arm, despite coming on the scene more recently.

These opinions all coming from those in the West, however, may discount some other geopolitical reasons for choosing RISC-V designs. That's a topic left untouched in my UK conversations.

You can watch my entire interview with Eben Upton on YouTube:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/-_aL9V0JsQQ" frameborder="0" allowfullscreen=""></iframe></div>
</div>
