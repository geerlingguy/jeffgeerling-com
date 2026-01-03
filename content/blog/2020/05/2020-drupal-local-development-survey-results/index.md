---
nid: 2999
title: "2020 Drupal Local Development Survey Results"
slug: "2020-drupal-local-development-survey-results"
date: 2020-05-08T14:29:55+00:00
drupal:
  nid: 2999
  path: /blog/2020/2020-drupal-local-development-survey-results
  body_format: markdown
  redirects: []
tags:
  - appearances
  - cms philly
  - drupal
  - drupal planet
  - local development
  - statistics
  - survey
---

> **tl;dr**: [Video from CMS Philly presentation](https://www.youtube.com/watch?v=q4NiyOAn6RI), [Slides from the presentation](https://www.slideshare.net/geerlingguy/2020-drupal-local-development-tools-survey-cms-philly), and scroll down to see graphs of particular interest to Drupal developers.

On May 1st, [Chris Urban](https://twitter.com/_urban_) and I presented [2020 Developer Tool Survey Results](https://cmsphilly.org/talks/2020-developer-tool-survey-results) at CMS Philly. For the past few years, we've run an annual Drupal Dev Tool Survey ([2019](/blog/2020/2019-drupal-local-development-survey-updated-results), [2018](https://www.midcamp.org/2018/topic-proposal/local-dev-environments-dummies)) and presented the results at DrupalCon and some local Drupal Camps.

Since DrupalCon went virtual this year, and Chris was helping make CMS Philly virtual, he suggested I join him at that conference and reveal the results at this session.

This blog post summarizes the main results relevant to Drupal _developers_ like me, who might want to know what other tools and techniques are currently popular for Drupal development.

> Note that these 2019 numbers, as well as in the rest of the numbers from the rest of the comparison graphs below, are adjusted to scale to the same number of responses given this year. We saw a 44% decrease in total responses this year (from ~1100 to ~600), likely in part due to the survey's timing—it was released right before a certain 2020 global event started taking over the airwaves.
>
> In _this_ blog post, I limit graphs to the top 6-10 results in the interest of more readable graphs. You can find more data in the presentation and slides linked earlier in this post.

First of all, it's important to know the kind of geographical diversity represented in the survey respondents:

{{< figure src="./2020-location.png" alt="2020 Local Development Survey Location Results" width="650" height="444" class="insert-image" >}}

This year we had a bit of a larger representation from North America, at the expense of responses from Europe.

One of the graphs I'm most interested in compares the popularity of different local development environments for Drupal:

{{< figure src="./2020-dev-environments-results.png" alt="2020 Local Development Environment Results" width="650" height="528" class="insert-image" >}}

One quick note: Acquia BLT can use one of Drupal VM, Lando, or Dev Desktop as its backend, so the absolute numbers here may not reflect reality _exactly_, but they are a good representation of relative popularity.

What's most interesting to me is the year-over-year differences; Lando and Docksal have accelerated their growth, DDEV has jumped up four spots, and Drupal VM, Dev Desktop, Vagrant, and Homebrew (most of the 'non-Docker' solutions) have put on the brakes.

It seems that by next year, we may see the overwhelming majority of Drupal developers using Docker-based local development environments.

The next graph shows the relative popularity of different local IDEs or code editors. As in prior years, PHPStorm rules the roost, and other tools fall off in popularity pretty quickly. If you use PHPStorm, VS Code, Sublime Text, or Vim, you're with the majority of developers:

{{< figure src="./2020-code-dev-editor-tools.png" alt="2020 Local Development Survey Code Editor Results" width="650" height="509" class="insert-image" >}}

There are some other graphs Chris and I covered comparing code editors to region, OS type, and Drupal project type, which can provide some interesting data giving clues to why some people may choose one editor over another (e.g. more of the Linux users use Vim, Emacs, or other free and open source editors). Again, see the presentation and slides linked from earlier in this post for all the details!

Chris and I discussed adding a _new_ question to the survey this year:

> Where are you hosting your production Drupal sites? (Select up to 3)

The results are interesting:

{{< figure src="./2020-drupal-hosting-providers.png" alt="2020 Local Development Survey Drupal Hosting Results" width="650" height="413" class="insert-image" >}}

And as with the other results, some of the relationships between team size and region can reveal interesting facts about the Drupal ecosystem. Since this was the first year we asked this question, we can't offer any historical comparison or trends, but one thing is clear: outside of having your customer manage their own hosting environment (which could also be one of the other listed providers—we don't know), the overwhelming majority of Drupal sites are hosted either on Acquia or Pantheon.

(Again, please note that there is a long tail of data including providers with < 17 respondents, but those are not included in this post for brevity.)

You can view the entire video of the presentation on Drupaldelphia's YouTube Channel:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/q4NiyOAn6RI" frameborder='0' allowfullscreen></iframe></div>

Chris and I will hopefully be at it again next year. Until then:

{{< figure src="./chris-urban-jeff-geerling-drupalcon-seattle-2019.jpeg" alt="Chris Urban and Jeff Geerling at DrupalCon Seattle 2019" width="650" height="434" class="insert-image" >}}
