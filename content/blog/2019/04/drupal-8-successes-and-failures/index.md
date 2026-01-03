---
nid: 2916
title: "Drupal 8 successes and failures"
slug: "drupal-8-successes-and-failures"
date: 2019-04-08T21:33:31+00:00
drupal:
  nid: 2916
  path: /blog/2019/drupal-8-successes-and-failures
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal 8
  - drupal planet
  - migrate
  - open source
  - upgrade
---

Thoughts about Drupal 8, Drupal 7, Backdrop, the Drupal Community, DrupalCon's meteoric price increases, DrupalCamps, and the future of the framework/CMS/enterprise experience engine that is Drupal have been bubbling up in the back of my mind for, well, years now.

I am almost always an optimist about the future, and Drupal 8 promised (and usually _delivered_) on many things:

  - Vastly improved content administration
  - Views in core, and even better than ever
  - Media in core
  - Layouts in core
  - Modern programming paradigms (fewer #DrupalWTFs)
  - 'Getting off the island' and becoming more of a normal PHP application (kinda the opposite of something like Wordpress)

But one thing that has always been annoying, and now is probably to the state of alarming, for some, is the fact that Drupal 8 adoption has still not hit a level of growth which will put it ahead of Drupal 7 adoption any time soon.

This fact has been beaten to death, so you can read [more about that elsewhere](https://www.metaltoad.com/blog/sluggish-drupal-8-adoption-lags-even-d6), or see the [current usage graph here](https://www.drupal.org/project/usage/drupal) and yes, not every site reports back to Drupal.org, so those numbers are not perfect... but it's the best data we have to work with.

So people are asking questions:

  - Should I stick with D7 LTS support for years and years, and re-platform on something else if I ever get the budget?
  - Should I upgrade to Drupal 8 now (or soon) since Drupal 8 to 9 will supposedly be a painless upgrade?
  - When will [insert critical module like Rules here] be ready for Drupal 8?
  - Is Drupal dead?
  - With 'ambitious digital experiences' being the new market Drupal targets, should I still build [insert any kind of non-enterprise type of website here] on it?

And the main driver for _this_ post, in particular, was the following tweet by @webchick (Angie Byron), who coincidentally is probably the main reason I dove headfirst into the Drupal community many years ago after she mentored me through my first core patch (hi Angie!):

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Time for my semi-annual pre-<a href="https://twitter.com/hashtag/DrupalCon?src=hash&amp;ref_src=twsrc%5Etfw">#DrupalCon</a> informal poll: If you&#39;re still on <a href="https://twitter.com/hashtag/Drupal?src=hash&amp;ref_src=twsrc%5Etfw">#Drupal</a> 7 and haven&#39;t moved to 8 yet, what&#39;s holding you back? (Please RT.)</p>&mdash; webchick (@webchick) <a href="https://twitter.com/webchick/status/1113139464849592320?ref_src=twsrc%5Etfw">April 2, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

I won't answer all the questions above—there are a lot of nuances to each that I could not possibly answer in a blog post—but I do want to jot down a number of areas where I have seen pain (and usually experienced on my own) and which are still holding back widespread adoption of Drupal 8 by those who used to default to Drupal for 'all the things'.

## Drupal 8 Failures

> Caveat to those who read on—you may think I'm trying to disparage Drupal through the rest of this post. I'm not. I'm exposing the dark side of a major open source project's decision to radically re-architect it's core software on an entirely new foundation. It's helpful to know these things so we can figure out ways to avoid hitting all the _same_ pain points in the future, and also as a sort of 'call to action' in case anyone reading this thinks they can push some initiative forward in one area or another (it's no coincidence I'm finishing this post on the flight to DrupalCon Seattle!).

### The web has changed

So... a lot of people mention that because more people build custom Node.js-based single page apps using the MEAN stack, or now do hip and trendy 'full stack development', and Drupal is some old monolith, Drupal has been left in the dust. I don't buy that argument, because otherwise we'd see similar attrition in pretty much all the other PHP CMS communities... and we don't.

Sure, there are use cases where someone would consider _either_ Drupal _or_ a hip trendy decoupled web framework backend. But Drupal 8 is actually a really good choice for those who build decoupled architectures using JSON:API, or GraphQL, or whatever other fancy decoupled framework and need a reliable content backend. To be honest, though, it seems that those who do 'decoupled' with Drupal are often people who started with Drupal (or something like it), and then get _into_ the decoupled game. And that's a pretty small slice of the market. Drupal is a hard sell if you have a team of non-PHP developers (whether they do Node, Ruby, Python, Go, or whatever) and are looking into decoupled or otherwise buzzwordy architectures.

### Migrations instead of Updates for modules

With Drupal 4, 5, 6, and 7, modules could define upgrade paths from one major version to the next through Drupal's normal update.php mechanism, and while the entire update mechanism was a very Drupal-centric oddity, it worked. And most modules would, as part of the general upgrade process, write an update path so those using the Drupal 6 version would have all that module's configuration make its way to Drupal 7, as long as they were running the latest and greatest Drupal 6 module version when they upgraded.

Things became a bit harder in Drupal 8, because of two things:

  1. New API architecture often required full module rewrites.
  1. The traditional update.php process was abandoned for major version upgrades (see: [Drupal 7 sites can no longer be upgraded to Drupal 8 with update.php](https://www.drupal.org/node/2186315)).

And these two problems kind of fed into each other—not only did module authors had to often rewrite (or at least radically alter) large swaths of code to support the new Drupal 8 APIs, but they also had to scrap any hook_update() upgrade implementation they may have worked on once that change record was published. I'm not speaking in the hypothetical here; this is _exactly_ what happened with the Honeypot module. In fact, I still have not had time to work on writing a [module migration for Honeypot for Drupal 8](https://www.drupal.org/project/honeypot/issues/2401647), even though I had a fully working and tested upgrade path using the old update.php method [years ago](https://www.drupal.org/project/honeypot/issues/2401407).

For a simpler module like Honeypot, this isn't a major issue, because site builders can reconfigure Honeypot pretty quickly. But for more complex modules that are _not_ in core, like Rules, XML Sitemaps, Google Analytics, etc., there are a ton of configuration options, and without a reliable configuration upgrade path, site owners literally have to re-do all the original configuration work they did when they built out their current Drupal site. Even if the module has the exact same features and functionality. Sometimes one little checkbox buried in the third page of a module's settings is the difference between some site feature working correctly or not—and when you have hundreds or thousands of said checkboxes to check on the new site... the upgrade becomes a much more risky proposition.

There is an open issue in the Drupal project issue queue to help improve this situation, but we're far from the end game here: [[Meta] Better support for D7 -> D8 contrib migrate](https://www.drupal.org/project/ideas/issues/2906878).

### Composer is still not a first-class citizen... but is often necessary

One of the largest 'get off the island' tasks the Drupal community checked off early was 'start using Composer for dependency management'. However, Drupal is... weird. You can't resolve two decades worth of architectural assumptions and dependency cruft in one major release.

Especially since until Drupal 8, it was not even really possible (except if you were willing to do some _really_ wacky stuff) to manage a Drupal codebase using Composer.

I've spilled enough ink on these pages over the years over Composer and Drupal 8 ([2019](/blog/2019/how-i-upgrade-drupal-8-sites-exported-config-and-composer), [2018](/blog/2018/converting-non-composer-drupal-codebase-use-composer), [2018-2](/blog/2018/updating-drupalcore-composer-drupal-core-doesnt-update), [2017](/blog/2017/composer-bof-drupalcon-baltimore), [2017-2](/blog/2017/tips-managing-drupal-8-projects-composer), [2017-3](/blog/2017/composer-and-drupal-are-still-strange-bedfellows), etc.), and most of my older postings still highlight current problems in using Drupal and Composer together.

There's a massive initiative to make things better: [[META] Improve Drupal's use of Composer](https://www.drupal.org/project/drupal/issues/2002304). It will still take time, and maybe even cause a little more strife in the end, as some more old Drupalisms may need to be put to rest. But having one standard way to build and maintain Drupal codebases will be better in the end, because right now it can be quite messy, especially for those who downloaded Drupal as a tarball and use no CI system.

### OOP and Symfony are the future

Along the same theme as the previous topic, Drupal rearchitected most of the foundational bits of code (the menu routing system, the HTTP request system, the Block system, the Entity system—pretty much everything except maybe Forms API) on top of Symfony, a very robust and widely-used PHP Framework.

But this meant that large swaths of Drupal experience were thrown out the window. A 'Block' was still a 'Block'... but the way they are built changed from weird-but-conventional Drupal hooks to using 'Plugins'. And menus used to be defined in a hook, but now there are sometimes multiple new YAML files you have to add to a module to get Drupal's menu system to pick up a new menu item—and you have to know how to wire up a menu item to a route, and what a route is, etc. In the past many of these things were kind of papered over by Drupal's simple-but-good-enough menu system, but now you have to be more _formal_ about everything.

Speaking of which, a solid understanding of OOP-style programming is basically required in Drupal 8, whereas weekend hackers could kind of cobble together things in Drupal <= 7 using some hooks and copied-and-pasted code from Stack Exchange. Debugging—for those not used to a full-fledged debugger—is also a lot different. Simple `print()` statements or `dsm()` don't always cut it anymore. And debugging things on the frontend—well, I'll get to that soon.

The overarching issue is that the Drupal community was sold on the idea that moving Drupal to Symfony would pull in thousands of other PHP developers who would flock to Drupal once it started using a more modern code architecture. That promise really never panned out, as if anything, it seems _harder_ to find solid senior-level Drupal engineers nowadays (at least in my experience—am I wrong here?).

Some Drupal developers who are not classically-trained (like me! I never took a comp sci class in my life) chose to expand their knowledge and grow with Drupal 8's new architecture. Others chose more familiar pastures and either moved on to some other PHP-based CMS or switched to some other ecosystem. I don't blame them, not at all; it's a tough decision you have to make to balance your career desires and opportunities, and everyone has to make their own decision.

In any case, the new architecture has more complexity than the old; and because of this, it's almost a necessity to adopt the following:

  - Use an IDE like PHPStorm, or lots of plugins with other editors, to be able to code efficiently across sometimes multiple files.
  - Integrate some sort of linting framework lest you hit deprecated code and weird syntax issues.
  - Have a CI/build process because a modern Drupal site can't usually be managed and run in one Git codebase and branch, checked out on a production server.

### Themes have to be rebuilt

Along with all the other changes, Drupal's theme system was _completely_ swapped out—it went from using the unholy monster that was PHPTemplate to a clean, new, standard system from Symfony, Twig. I'm one of the first to admit that this was probably one of the best and most necessary architecture changes in Drupal. The theme system was dangerous, messy, and difficult to work with on the best days.

But this is in many cases the straw that breaks the camel's back. In addition to the revamped architecture, new required build processes, and upgrade difficulties, almost every Drupal site has to _completely rewrite_ its theme. And for many of the Drupal 7 sites I've built and worked on, this is probably where the majority of the effort would need to happen.

Try as we might (as a general web development community), the number of sites using a strict frontend design system where the design is decoupled from the theme itself, and can evolve and be migrated from one system to another, is _vanishingly_ small. In 99% of the sites I've seen, very little of the frontend code from Drupal 7 could be quickly moved to Drupal 8. Maybe a few theme and form hooks, and a few CSS files, but the theme is usually very deep and complex, and most organizations use an upgrade as an opportunity to sink another chunk of money into refreshing their site's themes anyways.

But at least with Drupal 5 to 6 or 6 to 7, that was a _choice_, and you could upgrade the underlying system without also upgrading the theme. In Drupal 8, you kind of have to rebuild your theme or build an entirely new theme.

### Custom code requires a comprehensive rewrite

I admit that I am guilty of running two Drupal 7 sites with a very large amount of custom code. [Hosted Apache Solr](https://hostedapachesolr.com) and [Server Check.in](https://servercheck.in) are both currently running on Drupal 7 (well, the frontend parts at least), and I have tens of thousands of lines of custom code which integrates with backend APIs (using things like Drupal's Entity API, Form API, Block API, Queue API, etc.).

Some of this code will not need to be rewritten completely (thankfully!), but there is enough that I will have to schedule a substantial chunk of time—which I could devote to features, bugfixes, or improving the platform in other ways—to upgrade to Drupal 8 (or 9) when the time comes.

There is always technical debt associated with custom code. And I always try to manage that by adding separate Behat tests which test the frontend functionality in as generic a way as possible (that way I can at least upgrade against a set of critical feature tests). But I'm not alone in facing this problem. Thousands of project managers (some of whom have precious little budget to work with) have to decide whether to allocate time and money to a Drupal site rebuild. The more custom code, the more difficult the decision.

### Multisite is... interesting

One of the few _huge_ differentiators between Drupal and most other CMSes has always been the ability to run 'multisite' installations. That is, you have one codebase, maybe even on one server, and you can run many Drupal websites (each with its own database, set of modules, unique files directory, theme, etc.).

Many multisite detractors are quick to point out that this is kind of an abomination and is architecturally impure. However, the site you're reading right now (assuming I haven't yet upgraded it to something else) is actually a multisite—I run six different Drupal 7 sites off one codebase, and there's no way I could've justified building each of these sites in Drupal _at all_ if I wasn't able to build _one_ build pipeline, one production server, and one development workflow that literally does all six sites. The dollar cost alone from running 1 Drupal production server to 6 prevents me from even considering it (most of these sites are maintained by me _gratis_).

There are a _lot_ of massive Drupal multisite installations, especially in education and non-profits, where the cost benefit of not having to manage tens or hundreds (or in some cases _thousands_) of Drupal codebases, CI workflows, and many more production servers (since you can no longer share PHP's opcache between sites, besides some other things) necessitates multisite installation.

Here's the rub: Multisite architecture is kind of in conflict with some of the core ways Composer works. So trying to manage a modern Drupal 8 codebase with Composer and having the ability to have different copies/versions of different modules inside the codebase is... not quite _impossible_, but can be very close to that. Especially if you are not a Composer whiz.

Yes, yes, there are a thousand other arguments against multisite... but the fact is, there are a number of organizations—usually some of the orgs with hundreds or thousands of the sites that show up in the Drupal project usage statistics—who are holding off upgrading to Drupal 8 because multisite is harder, and [the future of multisite is still fuzzy](https://www.drupal.org/project/drupal/issues/3004496).

## Conclusion

Drupal 8 was a radical re-architecture of a widely-used CMS platform. Many developers made their careers through the Drupal 6 and 7 development lifecycle, and were sideswiped by what happened when Drupal 8 was released. There's no doubt Drupal 8 has a great feature set, a thoroughly-tested core codebase, is excellent as a general site-building tool, and is primed for the building great (and 'ambitious') digital experiences.

But do I recommend Drupal 8 in all the same kinds of situations where I used to recommend Drupal 7 in the past? Definitely not.

Drupal 8 is a very different framework and platform than Drupal 6 or 7 was. There are some massive benefits, like the fact that it is easier to use modern programming paradigms, dependency management tools, and site architecture. And these benefits are _massive_ for new site builds or migrations from outside the Drupal ecosystem _into_ Drupal. But there are many tradeoffs for older Drupal sites; many users (and developers) have been left with a dilemma as they face re-building an entire site, in light of the fact that upgrades are more time-consuming and difficult than they had been in the past.

> It may be noted that many of the more 'ambitious' Drupal 6 sites also needed a full migration to Drupal 7 and couldn't be directly upgraded—but for the long tail of smaller sites which usually used core modules and a smattering of contrib modules, and had little if any custom code, the upgrade.php process worked quite well, and resulted in hundreds of thousands of site upgrades that I don't believe we will see with Drupal 7 to Drupal 8.

_Architecturally_, almost every major change that resulted in the Drupal 8 we know and love (and sometimes shake our fists at!) is sound. But when taken as a whole, I do not begrudge the project managers who have to decide if and when to upgrade to Drupal 8—or sit tight on Drupal 7 LTS, or move to Backdrop, or re-platform to some other system.

**I am still optimistic about Drupal's future**, especially as the plan seems to be to _not_ make such a massive set of architecture changes in a major version again, but instead to upgrade subsystems here and there through point releases. But I think the usage pattern and value proposition for Drupal has changed. I definitely think there are classes of websites that are more ideally situated on some other platform now, and I also think there will be a large set of organizations willing to stick it out on Drupal 7 LTS for as long as there is some form of commercial support available.

But I think the moral of Drupal's saga is if you revamp many major portions of an ecosystem's architecture in one release, you have to accept the attrition that comes with such a refactoring. The radical alternative is to kind of stick your head in the sand like Wordpress seems to be doing (with regard to modern best practices and the PHP community), but I'm not sure if I like that solution much, either ?.
