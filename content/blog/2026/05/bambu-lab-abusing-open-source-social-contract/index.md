---
date: '2026-05-12T09:00:00-05:00'
tags: ['bambu lab', '3d printing', 'open source', 'software', 'video', 'youtube']
title: 'Bambu Lab is abusing the open source social contract'
slug: 'bambu-lab-abusing-open-source-social-contract'
---
Last year [I said I'd probably never recommend another Bambu Lab printer again](https://www.youtube.com/watch?v=91kfolYkRNM).

I still use my P1S, but after Bambu Lab started pushing their always-connected cloud solution as the new default:

  - I blocked the printer from the Internet via my OPNsense Firewall
  - I stopped updating the firmware
  - I locked the printer into Developer mode
  - I deleted Bambu Studio and started using [OrcaSlicer](https://www.orcaslicer.com)

I had to do that to keep it under _my_ control, instead of Bambu's.

But I'm weird—I acknowledge that. I'm one of those crazy ones who likes to [own something they purchased](https://en.wikipedia.org/wiki/Right_to_property), and not have the company watch everything I do with hardware I paid for.

Bambu Lab could've left the status quo at that, and I wouldn't be writing this blog post.

But they didn't.

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/eb48MdtNaDQ' frameborder='0' allowfullscreen></iframe></div>
</div>

## What happened _this_ time?

For context: [OrcaSlicer](https://www.orcaslicer.com) is a fork of the open source project [Bambu Studio](https://github.com/bambulab/BambuStudio), which is a fork of [Prusa Slicer](https://github.com/prusa3d/PrusaSlicer), which is a fork of [slic3r](https://github.com/Slic3r/Slic3r). (They are all licensed under the [AGPLv3 open source license](https://github.com/slic3r/Slic3r/blob/master/LICENSE)).

OrcaSlicer already has to dance around Bambu's weird default setup where [every file you print goes through Bambu's servers](https://wiki.bambulab.com/en/software/bambu-connect), meaning they can see everything you ever print on your printer.

That is, unless you're like me and you run it in [Developer mode](https://wiki.bambulab.com/en/knowledge-sharing/enable-developer-mode), and completely block it from the Internet on old firmware.

Some people _are_ okay with using OrcaSlicer and printing through Bambu's cloud. It's convenient if you're on the road and want to start a print on your printer at home, without managing your own VPN.

I run my own WireGuard VPN, so I don't need that, but I understand not everyone has the resources to manage their own remote access.

Bambu saw a fork of OrcaSlicer that allowed you to use all your printer's features without having to route prints through Bambu's cloud called [OrcaSlicer-bambulab](https://github.com/jarczakpawel/OrcaSlicer-bambulab) and was like, "You know what? No. For the 0.1% of power users who want to run OrcaSlicer without the cloud delivery mechanism like we have in our AGPL-licensed Linux Bambu Studio code... no. You _have_ to use our app, and _only_ our app."

So they threatened that OrcaSlicer fork's developer with legal action for things that developer _didn't_ do. For example, they indicated the fork used an impersonation attack, despite the fork using Bambu Studio's upstream code _verbatim_.

> These are very serious public accusations.
> 
> Bambu Lab did not write to me with these specific public claims first. They also refused my request to publish the full correspondence. Instead, they published a one-sided public statement where I cannot reply directly.
> 
> In practice, this presents me to the public as someone bypassing security, impersonating their client, and creating a risk to their infrastructure. I reject that characterization.
>
> — [OrcaSlicer-bambulabs developer's response](https://github.com/jarczakpawel/OrcaSlicer-bambulab/commit/eff25adaaf5ed9906ee7eaeecf3ce64cc8a920d3#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5R13-R17)

Bambu is abusing the open source social contract, and using their legal might, to suppress a tiny number of their users[^tiny], for who knows what reason.

It seems dumb to me, because it would've been easier (and more profitable) to do nothing at all[^easier]. Instead, they [wrote a blog post blaming an individual open source developer](https://blog.bambulab.com/setting-the-record-straight-on-cloud-access-and-community/) for their own infrastructure and security problems.

> This is where the actual issue arises: the modification in question worked by injecting falsified identity metadata into network communication.
>
> In simple terms: it pretended to be the official Bambu Studio client when communicating with our servers.
> 
> — [Bambu Lab blog post](https://blog.bambulab.com/setting-the-record-straight-on-cloud-access-and-community/)

I don't think they understand open source culture. Security either, if a public user agent string is their only protection against DDoS attacks...

Instead of finding solutions to ecosystem problems and building a more secure platform, Bambu is putting devoted power users like the fork's developer on blast[^devoted].

When tensions flared last year, they wrote a [similar blog post](https://blog.bambulab.com/updates-and-third-party-integration-with-bambu-connect/) blaming community backlash on 'unfortunate misinformation'. I imagine they meant speculation from community members (like myself) frustrated the whole software ecosystem and ownership model was turned upside down post-purchase.

This year they're blaming one developer of a tiny slicer fork for the _potential_ impact he could have on their entire cloud infrastructure.

> It creates structural vulnerability. If this method were widely adopted or incorrectly configured, thousands of clients could simultaneously hit our servers while impersonating the official client. Our systems would have no way to distinguish traffic, because the requests would look identical.
>
> — [Bambu Lab blog post](https://blog.bambulab.com/setting-the-record-straight-on-cloud-access-and-community/)

I love how they frame this as a developer trying to impersonate their app, when he's literally using [the same AGPL-licensed code their Linux app uses](https://github.com/bambulab/BambuStudio/blob/master/src/slic3r/Utils/Http.cpp#L175).

I find it **doubly ironic** since their own fork [caused Bambu users' telemetry to hit _Prusa's_ servers back in 2022](https://x.com/josefprusa/status/1542259514828791811), and (to my knowledge) Prusa didn't snap back with a C&D.

They spent the rest of their blog post talking about vulnerabilities, bugs, and instabilities—as if that has anything to do with a developer using upstream code verbatim in his fork.

Maybe they could take a new approach and just not lock down their whole ecosystem in the first place.

But who am I kidding? Nothing I say, and no amount of complaining in the comments below, seems to help Bambu see the fault in their ways.

Spending a little more for a printer from another company just might do it, though.

Louis Rossmann posted a video saying [he'd pledge $10,000](https://www.youtube.com/watch?v=qLLVn6XT7v0) to help the open source dev fight Bambu's legal threats. And I'd happily chip in too, but that's only useful [if the dev wants to put himself back in Bambu's crosshairs](https://github.com/jarczakpawel/OrcaSlicer-bambulab/issues/6).

The better play might just be to skip Bambu altogether.

[^tiny]: The OrcaSlicer fork in question didn't seem to have much uptake outside of a very small subset of users prior to Bambu Lab's cease and desist order.

[^easier]: Maybe ask for the fork to not include "bambulabs" in the name, since that could be a reasonable trademark-related demand.

[^devoted]: The fork's developer mentioned "I previously helped Bambu Studio users with Linux and Wayland issues, including on Bambu Lab's own GitHub. That makes it especially absurd to me that I am now being publicly presented as someone dangerous to their infrastructure."
