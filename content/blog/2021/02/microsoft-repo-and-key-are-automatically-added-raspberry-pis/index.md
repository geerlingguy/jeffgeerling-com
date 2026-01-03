---
nid: 3075
title: "Microsoft repo and key are automatically added to Raspberry Pis"
slug: "microsoft-repo-and-key-are-automatically-added-raspberry-pis"
date: 2021-02-17T02:52:23+00:00
drupal:
  nid: 3075
  path: /blog/2021/microsoft-repo-and-key-are-automatically-added-raspberry-pis
  body_format: markdown
  redirects: []
tags:
  - apt
  - debian
  - microsoft
  - open source
  - raspberry pi
  - video
  - vscode
---

A couple weeks ago, I noticed when running `apt-get upgrade` on one of my Pi projects that a new repository was added.

{{< figure src="./vscode-repo-added-raspberry-pi.jpg" alt="VSCode Repository added to Raspberry Pi OS automatically during apt upgrade" width="700" height="394" class="insert-image" >}}

It was a little odd, because Linux distributions don't typically 'inject' new repositories like this. And it was even stranger because this particular repository was for VSCode, from Microsoft.

The Raspberry Pi Foundation [just posted an article to their blog](https://www.raspberrypi.org/blog/visual-studio-code-comes-to-raspberry-pi/) about Visual Studio Code coming to the Raspberry Pi—but that post didn't address any of the controversy surrounding this change.

> There's also a video that goes along with this post: [Is Microsoft Spying on your Raspberry Pi?](https://www.youtube.com/watch?v=OnA_s9IBSmA)

## What Happened

In late 2020, Microsoft released a version of VSCode compatible with the Raspberry Pi.

In early February this year, the Raspberry Pi OS team added an automatic update that installs Microsoft's GPG key and a Microsoft repo source on all Raspberry Pis running Pi OS.

After the install, whenever someone on Pi OS runs `apt update`, the Pi will reach out and check Microsoft's apt server for any updates.

VSCode isn't automatically installed—at least not _yet_. And the amount of data Microsoft can get from this apt configuration is minimal (though some would argue getting the IP addresses of most Raspberry Pis connected to the Internet would be a privacy violation in itself). But that's not the main concern people have with this action.

## VSCode Concerns

First let's talk about VSCode.

{{< figure src="./vscode-telemetry-on-raspberry-pi.jpg" alt="VSCode Telemetry option on Raspberry Pi" width="700" height="394" class="insert-image" >}}

By default, it has 'telemetry' that sends out system and usage information to Microsoft if you install it. This telemetry is annoying at best, but concerning if you care about privacy. The telemetry can be disabled, but most people would rather have it be _opt-in_ versus opt-out.

Worse than that, VSCode's _source code_ is open source, but the binary you install is _not_, since it includes some extra bits that are built in by Microsoft outside of the [public source tree](https://github.com/Microsoft/vscode).

This makes VSCode non-free software, and it should be marked as such if following typical Debian packaging standards (though the Pi Foundation is under no such obligation).

## VSCode Alternatives

Many in the community pointed out that [VSCodium](https://vscodium.com) is _truly_ open source, end-to-end, and would be a worthy inclusion in the free and open source spirit. There aren't any giant corporations pushing that project, so why not include VSCodium in the default repositories and recommend people install it instead?

> I learned recently that Microsoft's licensing for VSCode extensions is restrictive to the point that many extensions are not made available separately to open source VSCodium installs, meaning many popular extensions won't work if you want to use an unencumbered version of VSCode. Go figure.

Well, I know Microsoft would love to have more inroads in 'educational computing'. VSCode on the Pi could allow them to more directly integrate Microsoft services like Azure IoT into people's projects, thus making it less appealing to use competing IoT services like those from Amazon.

I won't speculate on the relationship Microsoft has with the Raspberry Pi Foundation or Raspberry Pi Trading, but I'm guessing there is _some_ incentive for Microsoft besides just 'goodwill,' especially considering the official Raspberry Pi blog post showing how to use VSCode on the Pi was penned by a [Senior Cloud Advocate from Microsoft](https://www.linkedin.com/in/jimbobbennett/) who's involved in promoting Azure's IoT platform.

## Why so angry?

But what made people so fired up about this? It's the Raspberry Pi Foundation's right to add in software they believe will be loved by their users, right?

The problem is that many Pi users noticed a Microsoft repository being added to their Raspberry Pis unannounced, and when they followed the breadcrumbs back to the `raspberrypi-sys-mods` GitHub repository, the code that did the automatic push [wasn't even present for further auditing](https://github.com/RPi-Distro/raspberrypi-sys-mods/issues/41) until days after the repo was already installed.

What's more, when users posted their concerns to the Raspberry Pi Forums, many threads about the situation were locked or deleted.

Sure, you can just _not install VSCode_, but the apt repo is still pushed to your Pi unless you explicitly ignore it, which is hard to do if you don't know it's coming.

It didn't help when someone asked Eben Upton about the situation on Twitter. This was [his response to the situation](https://twitter.com/EbenUpton/status/1357058711873871872):

> Sorry: I can't understand why you think this was a controversial thing to do. We do things of this sort all the time without putting out a blog post about how to opt out.

I can't imagine someone like Eben, who's been in the industry for years, _not_ seeing what's controversial about something from Microsoft being automatically added to a Linux OS without any user interaction or prior warning.

Sure, Microsoft's been coming around to the open source way, slowly but surely. But Pi OS is built on Linux, and most in the Linux community aren't willing to give Microsoft a free pass. They have to earn their standing in the open source community, and pushing non-free software into educational Linux-based computers isn't the way.

{{< figure src="./force-push-non-free-repos-to-pis.jpg" alt="Force push non-free repos to all Raspberry Pis - This is not the way" width="500" height="261" class="insert-image" >}}

Finally, many people argue "you're fine with Android and Alexa collecting all your information, but not Microsoft?"

Not only is that a false equivalence, many who share these concerns _don't_ use Alexa or Android _for exactly that reason_.

## Aren't you just overblowing the situation?

There _are_ some people making a mountain out of a mole hill. I don't think the Pi Foundation has any nefarious plans here. And I don't think Microsoft is going to be injecting software in Pis anytime soon now that they have their GPG and a default repo installed everywhere. Well, _hopefully_ they won't.

Assuming the best intent, I can see the argument that VSCode is a popular code editor, it would help the Pi's outreach if it were easily available to anyone using a Raspberry Pi.

I've run a [local development survey for the Drupal community](https://www.jeffgeerling.com/blog/2020/2020-drupal-local-development-survey-results) for three years now, and it's amazing how quickly VSCode has surpassed most other editors in usage—at least for web-based projects.

From the Raspberry Pi Foundation's perspective, VSCode is a popular mainstream code editor, and making it easy to install on the Raspberry Pi is a worthy goal, if you want people to consider using a Pi as their main computer.

And it's not like the Pi Foundation is scot-free in terms of being 100% free and open source. Pis [still require a closed-source binary blob for its booting and the GPU](https://github.com/raspberrypi/firmware/issues/79), and that's been a thorn in the side of the Pi open source community for years.

As a pragmatic programmer, I understand the motivations behind this inclusion, but it does erode some of the trust I have in the Pi Foundation to be good stewards of Raspberry Pi OS.

It's not _that_ hard to teach someone the three or four terminal commands to add a third party repository to the Raspberry Pi, and I'd much rather the Pi Foundation teach people _that_, than force it on everyone:

```
wget -qO - https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
echo "deb [arch=amd64,arm64,armhf] http://packages.microsoft.com/repos/code stable main" | sudo tee -a /etc/apt/sources.list.d/vscode.list
sudo apt-get update
```

Will I still use Raspberry Pi OS? Yes, I'm using both the 32-bit and 64-bit versions for various projects.

But will this action cause me to consider [Ubuntu for Pi](https://ubuntu.com/raspberry-pi) or any of the other ARM Linux builds more often? Most definitely.

## How can you prevent this repo from being used?

Here's how to remove the installed repo and GPG key from your Raspberry Pi, if you're running Raspberry Pi OS:

```
sudo rm /etc/apt/sources.list.d/vscode.list
sudo rm /etc/apt/trusted.gpg.d/microsoft.gpg
sudo apt update
```

This _should_ be a permanent fix, since the update that forces in the repo and key should only ever run once.

## Conclusion

The Raspberry Pi Foundation's mission is education, and they've been focused on simplicity and targeting the mainstream in what they do.

Focusing solely on 'pure' free and open source software can lead to missed opportunities (and they've already distributed other proprietary apps like Minecraft and Wolfram), but this action still taints their standing as good stewards in the open source community.

I'm mixed on this decision. I'd much rather the Pi Foundation give people the knowledge of how to install VSCode (or other applications like it) by teaching them how to use apt to install it, instead of forcing a new repo for a tool that relatively few Pis will ever get installed.

And even with the forced repo install, there should've been prior warning, especially since _it was pushed to all Pis, even those running the 'lite' OS with no GUI and thus no way to run VSCode_.
