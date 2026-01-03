---
nid: 3070
title: "Cracks are showing in Enterprise Open Source's foundations"
slug: "cracks-are-showing-enterprise-open-sources-foundations"
date: 2021-01-28T15:32:56+00:00
drupal:
  nid: 3070
  path: /blog/2021/cracks-are-showing-enterprise-open-sources-foundations
  body_format: markdown
  redirects: []
tags:
  - centos
  - elastic
  - elasticsearch
  - foss
  - linux
  - open source
  - red hat
---

I've worked in open source my entire career<sup>1</sup>. To say that I'm worried about the impact recent events have on the open source ecosystem would be an understatement.

{{< figure src="./redhat-elasticsearch-logos.png" alt="Red Hat and Elastic logos" width="449" height="144" class="insert-image" >}}

In the past couple months:

  - Red Hat effectively killed CentOS
  - Elastic effectively killed Elasticsearch

People may rightfully refute these statements, but the statements are more complicated than you might think. Killing a project doesn't mean the project will vanish overnight, but what _has_ happened so far is two very large companies in the 'enterprise open source' space have shown the chinks in the armor of the monetization of open source software.

For many years, everyone in the industry pointed at Red Hat as the shining example of 'how to build a company around open source'.

And for the past decade, the open source Elasticsearch, Logstash, and Kibana logging ecosystem was on a tear, becoming a standard in the open source cloud stack.

But Red Hat was bought out by IBM in 2019, and after taking over the community CentOS project (which happened in 2014, well before the acquisition), they basically neutered it by [ending the decade-long support cycle](https://www.redhat.com/en/blog/centos-stream-building-innovative-future-enterprise-linux) it was previously known and loved for.

And Elastic [switched from the Apache 2 license to a non-free software license for Elasticsearch](https://www.elastic.co/blog/licensing-change) just a couple weeks ago.

## Video Version of the Post

I also have a video version of this post (in case you're more visually inclined):

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/_0tIQlQhr00" frameborder='0' allowfullscreen></iframe></div>

## Red Hat and CentOS

When Red Hat took over the CentOS project back in 2014, there was a [mixed, but mostly positive](https://redmonk.com/dberkholz/2014/01/10/red-hats-centos-acquisition-good-for-both-sides-but-ware-the-jabberwock/) reaction. The CentOS maintainers were sometimes having a hard time keeping up with upstream changes in Red Hat Enterprise Linux (RHEL), and major releases like version 7 and 8 were challenging due to the required architecture changes.

So Red Hat's willingness to come in and backstop CentOS was generally a good thing—for a time.

Last month, Red Hat dropped a bombshell: CentOS users who had started adopting CentOS 8 and expected support for stable releases until the end of the 2020s would get [just one year of support](https://www.theregister.com/2021/01/26/killing_centos/).

They would need to switch to 'CentOS Stream', a kind of a 'stable beta' version of RHEL that's more stable than Fedora, but less stable than Enterprise Linux. Or they'd have to give up CentOS entirely.

This angered a lot of people, _admittedly_ most of whom have been building on the free version of CentOS without contributing much if anything back to the project for years (but that's part of the whole 'free software' thing—there will be freeloaders).

But it also angered a lot of people like me, who don't really use CentOS much, except to test other FOSS software on multiple distributions, and used CentOS as a 1:1 proxy for Red Hat Enterprise Linux.

Red Hat [extended a small olive branch](https://www.redhat.com/en/blog/new-year-new-red-hat-enterprise-linux-programs-easier-ways-access-rhel) in the form of less restrictive licensing for developers like me, but it's still not clear how much work I'll have to do if I want to do things like CI testing in containers without having to manage subscriptions and access keys. Those kinds of things may lead to me killing all support for Red Hat flavors of Linux in many of my own open source projects.

So I guess... Debian and Ubuntu for the win?

Anyways, there's more nuance to the entire debacle, but the main thing this points to is the fact that while increasing revenue via licensing might not be the _only_ motive Red Hat had in this move, it was certainly a major factor. And the downfall of Scientific Linux and CentOS makes those who've built their careers or companies around Red Hat compatibility without paying the subscription fees nervous.

Many are waiting to see if up-and-coming [Rocky Linux](https://rockylinux.org)—which aims to be a perfect replacement for CentOS—is going to be released soon, with the same stability they grew to expect from CentOS.

## Elastic and Elasticsearch

Now on to Elastic and Elasticsearch: There's again so much happening that I can't possibly cover it all in one post, but the basic story goes like this:

Elasticsearch was created under the Apache License version 2.0. It's grown to be an essential open source cloud infrastructure component, and I've seen it used everywhere.

Seeing its popularity, and the complexity of deploying and maintaining Elasticsearch clusters, Amazon Web Services (or AWS) decided to [package up its own hosted Elasticsearch offering](https://aws.amazon.com/blogs/aws/new-amazon-elasticsearch-service/).

Well, Elastic, the [venture-capital-backed company](https://www.crunchbase.com/organization/elasticsearch) at the helm of the open source project, didn't like that, because the way they were monetizing their development, and showing growth to their investors, was by charging for their own hosted Elasticsearch offering.

So AWS was directly competing with Elastic, but not taking the same responsibility for the open source project or investing in it as heavily as Elastic was.

This creates a problem inherent to many popular open source packages—when a cloud computing behemoth like Google, AWS, or Microsoft decides to wrap up your free software in a hosted offering, and profits from it, how do you deal with that?

Well, Elastic dealt with it by [switching to a new license](https://www.elastic.co/blog/licensing-change), which many in the FOSS, or Free and Open Source Software Community, have decried as not being truly open source.

The [SSPL](https://en.wikipedia.org/wiki/Server_Side_Public_License), or Server Side Public License, is touted as a GPL version 3 derivative license. It's similar, but has a major restriction, stating you can't build a hosted service without also releasing all the code you used to build _that service_.

But the Fedora community has [publicly stated](https://fedoraproject.org/wiki/Licensing/SSPL) that "to consider the SSPL to be 'Free' or 'Open Source' causes a shadow to be cast across all other licenses in the FOSS ecosystem."

And the Open Source Initiative dubbed the license "fauxpen" in their article [The SSPL is Not an Open Source License](https://opensource.org/node/1099). They said "it's deception, plain and simple, to claim that the software has all the benefits and promises of open source when it does not."

So what did Amazon do in response? They [forked Elasticsearch](https://aws.amazon.com/blogs/opensource/stepping-up-for-a-truly-open-source-elasticsearch/). Something well within their rights, since they're forking the last truly open source version.

It will be interesting to see how the communities around these two now separate projects diverge.

## Conclusion

So like I said, this post can't do justice to the nuance of the situation. And it's not as simple as "[IBM|Red Hat] is bad", or "leeches are bad for open source", or "giant AWS is forking little Elastic's project." There's a lot more to it, and I encourage you to read more about the news.

But I know for me, it brings up some challenging questions:

First, how can we make sure developers who build open source software are compensated for their work in a just way? And how can we hold both giant corporations _and_ billion-dollar venture-backed startups accountable for riding the coattails of free and open source software without giving back proportionately?

Second, how can I mitigate against software and services I use and love changing licenses and causing headaches? One way is to become more restrictive in licensing, choosing only [copyleft licenses](http://copyfree.org/policy/copyleft) that were originally created to offer more protections to individuals than corporations.

Third, if I want to earn a living or build a company around open source, what are my options? We all used to point to Red Hat as the paragon of open source, but it seems like that company—for all the great things they have done and are _still_ doing in open source communities—has begun travelling down the path of sales over source code.

The more corporate-friendly open source has become, the more power has been ceded to giant mega corporations. And who's to blame? Well, sadly, after some deep introspection, I have to admit maybe I'm a part of the problem!

Anyways, these events are causing a lot of developers to second guess their dismissal of the open source 'licensing weirdos' who always yell about the importance of choosing the right license. But maybe they're onto something. Maybe blindly adopting permissive open source licenses to invite more corporate ownership _isn't_ the right answer.

---

<sup>1</sup> _The definition of 'open source' I'm using loosely in this sentence is inclusive of both FOSS and OSS licensed software. About half the projects I've made a living with have been GPLv2 or v3, the other half Apache or MIT. You can go down a deep rabbit hole arguing with pedants over what is meant by the term 'open source'._
