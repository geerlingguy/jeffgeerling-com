---
nid: 2366
title: "PSR-0 PSR-1 PSR-2, Drupal, and You!"
slug: "psr-0-psr-1-psr-2-drupal-and"
date: 2012-06-04T18:59:14+00:00
drupal:
  nid: 2366
  path: /blogs/jeff-geerling/psr-0-psr-1-psr-2-drupal-and
  body_format: filtered_html
  redirects: []
tags:
  - community
  - drupal
  - drupal 8
  - drupal planet
  - php
  - php-fig
  - psr
  - standards
---

For the past couple years, discussions about 'PSR-0', PHP standards, and some sort of framework standardizations have been popping up here and there. It wasn't until a bunch of 'PSR-0 Interoperability' patches started popping up in the Drupal core issue queues that I decided to take a closer look at PSR. (The latest? <a href="https://github.com/php-fig/fig-standards/tree/master/accepted">PSR-1 (Basic Coding Standard) and PSR-2 (Coding Style Guide)</a> have been accepted).

There's a great <a href="http://paul-m-jones.com/archives/2420">FAQ</a> that was just posted by Paul M. Jones <a href="http://paul-m-jones.com/archives/2420">explaining the PHP-FIG (PHP Frameworks Interoperability Group)</a>, which will give a little backstory to the group and its purpose. Drupal is a member of this group, with <a href="http://drupal.org/user/26398">Crell</a> (Larry Garfield) representing Drupal's vote for standards guidelines. You can see group members and discussions in the <a href="https://groups.google.com/forum/#!forum/php-standards">PHP Standards Working Group</a> Google Group, and you can follow along with proposed and ratified group standards in the <a href="https://github.com/php-fig">php-fig GitHub repository</a>.

A lot of the larger PHP frameworks, CMSes and developer communities are represented, but—importantly—this group does not intend to represent PHP as a whole (that's probably the main reason it's now called the 'Framework Interoperability Group' instead of the 'PHP Standards Working Group'). Rather, it represents the mainstream PHP developer, and countless professional PHP developers working with and for the projects in the group. The main premise is that there are many large development groups working with PHP, and it would be helpful if these large groups could use a common set of coding standards, naming standards, and the like when developing their projects so things like the fruitful relationship between Symfony and Drupal can flourish (we're already seeing positive results here in the Drupal community!).

Drupal has already <a href="http://drupal.org/node/1479568">converted core subsystems to the PSR-0 standard</a> for Drupal 8, and there is a <a href="http://drupal.org/node/1320394">PSR-0 compatible class loader in core</a>.

Having set standards that many organizations follow (such as PSR-0, PSR-1, etc.) also helps unify PHP development and bring it to a higher level; many others have (often rightfully) criticized the PHP language and developers for being fragmented, inconsistent and amateurish. I'm going to adopt PSR standards in my own PHP side projects (heck, most of my code already conforms, so it's not a big deal to me), and I'm glad many organizations are working towards adopting the standards as well. It will let our community spend more time working on making better end results and useful classes than arguing over whitespace, bracket placement, and control structure formatting (to name a few things...).

There's another great article on Pádraic Brady's blog titled <a href="http://blog.astrumfutura.com/2012/06/the-framework-interoperability-group-fig-openness-accountability-and-community-involvement-in-php-standards/">The Framework Interoperability Group (FIG): Openness, Accountability and Community Involvement in PHP Standards</a>.
