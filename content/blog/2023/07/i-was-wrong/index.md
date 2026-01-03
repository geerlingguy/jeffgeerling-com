---
nid: 3296
title: "I was wrong"
slug: "i-was-wrong"
date: 2023-07-02T17:22:14+00:00
drupal:
  nid: 3296
  path: /blog/2023/i-was-wrong
  body_format: markdown
  redirects: []
tags:
  - eula
  - gplv2
  - licensing
  - open source
  - red hat
---

...about Red Hat's EULA and its enforceability according to the license terms of the GPLv2. (Specifically in reference to my [blog post last Wednesday](/blog/2023/gplv2-red-hat-and-you)).

And for that, I apologize.

Basically, the GPLv2 says there can be "no restrictions" placed on any use of the source code provided to any user of the software with its license.

Red Hat's EULA says that Red Hat reserves the right to terminate your business relationship (the Red Hat Subscription) if you redistribute the source code.

This doesn't restrict your right to share the source code that has been previously provided, since you are still free to do so.

It doesn't make sense _logically_, and certainly not _ethically_ (I don't think _anyone_ could argue this is in the spirit of the GPLv2 license), but _legally_, logic and ethics sometimes take a back seat to _interpretation_.

> Update: I still think a court case could go either way given enough money and good lawyers, but apparently IBM's lawyers don't, otherwise they wouldn't have written the EULA.

This realization does nothing to affect my view of Red Hat's decisions concerning CentOS and the subsequent reversal of the promise to deliver cleaned SRPMs to git.centos.org.

But after discussing it (usually while being a bit impatient, sorry about that!) with a number of folks in the community (and a couple corporate open source laywers who were extremely kind to reach out directly), I am happy to admit I'm smarter today than I was last week, when it comes to GPLv2 and EULAs.

Nico's comment on [my last post](/blog/2023/gplv2-red-hat-and-you), especially, sums up the issue well:

> There can be no license violation because the contract also says that any open source license supersedes the terms of the agreement. For example the prohibition to share source might not apply to AGPL software, because of the requirement to offer modified source over the network. So if anything someone whose support contract is cancelled could sue and ask for the contract to be reinstated according to the GPL. But I am skeptical that it would succeed, the lawyers know both copyleft licensing and contract law better than you and I.

I previously mentioned that in this entire debacle, there are no winners.

I was also wrong about that. Somehow, lawyers, they always come out ahead.
