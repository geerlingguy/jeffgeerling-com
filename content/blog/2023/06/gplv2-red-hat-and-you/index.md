---
nid: 3295
title: "GPLv2, Red Hat, and You"
slug: "gplv2-red-hat-and-you"
date: 2023-06-29T00:04:36+00:00
drupal:
  nid: 3295
  path: /blog/2023/gplv2-red-hat-and-you
  body_format: markdown
  redirects: []
tags:
  - gplv2
  - law
  - license
  - linux
  - open source
  - red hat
---

(See update at the bottom of this post)

One of the interesting outcomes of the Red Hat situation:

Distribution of [GPLv2](https://opensource.org/license/gpl-2-0/)-licensed code requires no restrictions be placed on downstream users rights to use and redistribute the code (whether they obtained it freely or paid for access):

> Each time you redistribute the Program (or any work based on the Program), the recipient automatically receives a license from the original licensor to copy, distribute or modify the Program subject to these terms and conditions. **You may not impose any further restrictions on the recipients exercise of the rights granted herein**.

Does threatening retaliation (account suspension) for sharing code count as a 'restriction' on exercising a user's rights?

So far I've heard from three corporate open source licensing experts the answer is no.

According to them, the [EULA](https://www.redhat.com/licenses/Appendix_1_Global_English_20230309.pdf) only deals with an account-holder's ability to acquire services from Red Hat (a contract).

> **Unauthorized Use of Subscription Services**. Any unauthorized use of the Subscription Services is a material breach of the Agreement.
>
> Unauthorized use of the Subscription Services includes: [...] (d) using Subscription Services in connection with any redistribution of Software

The corporate license experts I talked to said the threat of termination of a subscription would not trigger the 'no restrictions' clause of the GPLv2, which deals with a _copyright_, not a contract.

I... disagree in principle (for what that's worth, lol) and think a lot about "interference, coercion, or intimidation", something surrounded by some [legal precedent](https://www.law.cornell.edu/uscode/text/42/3617), admittedly not in the software space, and only really dealing with discriminatory topics like real estate sales. But it seems there is some case law (ironically, dealing with SCO and IBM) on the topic.

As for whether Red Hat would enforce that agreement and cancel someone's subscription for sharing the source code, here's what Mike McGrath [had to say](https://podcast.asknoahshow.com/343) (at approximately 50:30):

> If they [downstreams] continue to use their subscription, I think that they would find they'd have difficulties with that, but, I don't really know what else to say about it.

I think it's insane Red Hat, of all companies, is the one triggering this thought process.

## Update 2023-07-01

It was pointed out on Reddit the terms also include in Section 1.4 the following:

> This Agreement establishes the rights and obligations associated with Subscription Services and is not intended to limit your rights to software code under the terms of an open source license.

From my reading, this would negate the earlier clause, and it seems that Red Hat's EULA is not technically in opposition to the GPLv2 license, which applies only at the time of Red Hat providing the source code, and doesn't widen it's scope to any ongoing relationship (the Red Hat subscription).

Somewhat ironically, IBM's own ['Open Source - Open Enterprise' page](https://www.ibm.com/opensource/enterprise/) states (under section 5):

> Note that if there is an End User License Agreement (EULA) or other terms required to download the software, it is not open source and those terms would have to be reviewed further."

Maybe they were on to something.
