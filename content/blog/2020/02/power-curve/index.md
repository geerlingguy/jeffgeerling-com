---
nid: 2813
title: "The power curve"
slug: "power-curve"
date: 2020-02-12T16:25:06+00:00
drupal:
  nid: 2813
  path: /blog/2020/power-curve
  body_format: markdown
  redirects:
    - /blog/2017/professional-software-development-and-power-curve
    - /blog/2019/power-curve
aliases:
  - /blog/2017/professional-software-development-and-power-curve
  - /blog/2019/power-curve
tags:
  - books
  - development
  - essay
  - gene kranz
  - power curve
  - software
  - space
---

Besides being a software developer and photographer, I take a deep interest in spaceflight and love reading about the history and development of air- and spacecraft, with a special focus on early space program development.

A few books I've read in the past couple years have gone beyond being interesting just for their historic content—they gave me a lot of ideas to reflect on in relation to my approach to software development, especially what I'd term 'professional' software development (vs. hacking something together for fun, or churning out brochureware sites or cookie-cutter apps).

One book in particular, [Failure is Not an Option](https://www.amazon.com/Failure-Not-Option-Mission-Control/dp/1439148813/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=876eabeb823748e3532481ddd835d0ef) (by Gene Kranz, director of Mission Control during NASA's early days into the Apollo era), illustrates high-performing teams operating well under pressure and with high stakes.

Thanks to efficiencies in computing power and available abstractions, software engineering today is on a scale the earliest software developers could only dream of. And yet, if we look at some of the greatest challenges the practitioners of this field encounter... it's not all that different from the past, or from other industries.

## The _power curve_

Kranz's book mentions the idea of the _power curve_ a few times:

> I had no problems and felt comfortable with the mechanics. But I had a long way to go before I would have that sense of "being ahead of the airplane" or "ahead of the power curve" as pilots put it—having the experience to anticipate what could happen rather than just reacting to what was happening at the moment.

I liken it to the feeling a race car driver gets, knowing the limits of his own body, the machine he's in, the grip of the tires, the stickiness of the tarmac, and the precise power output of his engine, the temperature of the engine and the brakes—a true professional optimizes for all of these aspects and is able to keep control—but only just _barely_. He's riding the power curve right up to the edge, but not going too far, lest his race end in a crash.

A good modern example rally car driver Ken Block. In a 2017 video, he can be seen playing with and continuously pushing the edge of the limits of his machine, the _Hoonicorn V2_:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Hg6L_7qLIEQ" frameborder='0' allowfullscreen></iframe></div>

<p style="text-align: center;"><a href="https://www.youtube.com/watch?v=Hg6L_7qLIEQ">Ken Block’s Climbkhana: Pikes Peak Featuring the Hoonicorn V2</a></p>

Similarly, I remember the feeling of finally mastering the [hockey stop](https://en.wikipedia.org/wiki/Hockey_stop) after a hundred crashes into the the wall of an ice rink. Or being able to use [countersteer](https://en.wikipedia.org/wiki/Countersteering) with my dirt bike to perform fast-but-controlled turns with one wheel sliding out from behind.

Building software, I sometimes notice a similar feeling—that of being so attuned to a bug, to a new feature in development, or to some performance tuning parameters—that I can in a way anticipate what will happen. And just like with a pilot pulling off a spectacular maneuver at 9 Gs, I feel the adrenaline rush from being one step ahead of my code.

It's not just [flow state](https://en.wikipedia.org/wiki/Flow_(psychology)), though flow state is a prerequisite to this feeling. It's when I hold a complete segment of code or an entire architecture in my internal 'state', and can feel out any of the logical progressions. Instead of having to adjust, run a build, adjust, run a build again, I can quickly explore many scenarios in my head. This is amped up to the extreme when I'm debugging a time-sensitive problem, like a performance issue or outage in production, or during a major load test, pentest, or cutover.

On a deeper level, it's being able to keep an even keel amidst a lot of projects, or amidst personal and work problems. I don't know if there are any genetic, biological, or even emotional reasons for it, but there are times when it's easier to jump in and out of tasks, or to manage multiple competing priorities with aplomb.

## The _power curve_ and software teams

The idea of the _power curve_ can be applied to software development teams as well. I've seen development teams mired in a depressing spiral of broken builds, missed deadlines, and technical debt. And I've seen development teams who seem to see the world with rose-colored glasses, delivering on time, delighting stakeholders, under-promising and over-delivering. And they have a great time doing it!

These teams stay ahead of the power curve _as a unit_. There's a baseline requirement for technical competence in all the roles—project management, development, quality assurance. But you don't need a bunch of '10x developers' to build a great team. And it has nothing to do with whether the team is in close physical proximity. I've seen these teams perform in situations where no two people are in the same timezone, and I've seen these teams working together in a cubicle farm.

What are some practical examples of a team that consistently pushes its power curve?

  - They use a well-defined but flexible process (e.g. Agile + scrum + some bits of waterfall) to turn business requirements into shipping features, and then have a well-defined workflow for estimating, building, testing, and shipping the features.
  - They do not allow work to enter their workflow unless it is part of the above process.
  - The PM/architect-level team members act as real-world firewalls, blocking or redirecting requests from outside that don't fit into their project's scope.
  - There is no hierarchy (at least, not in the traditional sense). Anyone can and does mention risks, anyone can speak directly with anyone else on the team at any time.
  - Egos are (usually) checked at the door. Team members are both humble and open with respect to implementation ideas, delivery promises, and RCAs. (Though members of high-performing teams are usually pretty proud of their individual contributions, it isn't the same kind of stubborn pride that rejects healthy debate.)
  - Technical debt is a well-managed asset; new features and optimizations which introduce tech debt are wisely chosen, and there is a plan for maintenance of the debt (rather than letting it spiral out of control).
  - Team members don't think in terms of the next week or month, they think in a timeline of years. (This helps especially with tech debt management.)
  - Team members don't waste time being 'architecturenauts'—they build small and efficient, but with an eye towards the future. They use proof-of-concept implementations to tease out major features or changes to critical components before committing to a major body of work.
  - They measure past performance and use it as a metric for future work, quickly rejecting requirements that cannot be reliably estimated. Software estimation is hard, _but it is not impossible_.
  - They do not compare their performance metrics to other teams' metrics. They understand that every team is unique and there is no magical comparison metric that can measure inter-team performance (e.g. commit count, lines of code added, lines of code removed, unit or functional test coverage, or bugs reported vs. features added).
  - They rarely think about any of the above—at least not consciously. These traits come _naturally_ to the team.

When a team consistently delivers, it can be frustrating to outsiders who have trouble doing the same. Especially since, as a team becomes more cohesive, the power curve is continually stretched, so the team seems deliver better results, faster!

> _Aside_: As someone who has worked with both agency-style short-lived teams and longer single-project teams, one downside to the agency style is that right after discovering their power curve, the team disbands and individuals form other teams. It's hard to strike a balance between breaking up cohesive teams and making individuals feel stuck in a particular project, but agencies have a hard time building high-performing teams when they think of work on a quarterly basis!

I'm not the first person to mention most of these ideas—or probably any of them—but I think the differentiation between _professional_ and amateur/hobbyist developers is the ability to _fly by the seat of their pants_ and push their work and their team right up to the edge of the power curve, but back off and push back on extra work or distractions before they're out of their depth.

Nothing above is meant to be disparaging—you can work as a professional (in the sense of knowing your power curve) for some projects, and a hobbyist for other projects. As an example, I don't often hit flow state or push my limits when I'm fixing bugs on my open source projects. A lot of time, you just have to push through mundane tasks. And even the most high-performing teams aren't always pushing the envelope (even Ken Block stopped at Pike Peak's summit for some R&R at the gift shop!); managing toil and technical debt is usually a challenge no matter what the project.

If you don't feel you've been 'ahead of the power curve', but instead a project is out of control and you're getting depressed about it, you might be aiming a little too high (your power curve might not be quite where you think it is!), or you might be taking on too much work. Just like when a pilot pushes experimental aircraft too high or too fast and loses control, you have to work within your limits, and know when to pull back on the throttle.
