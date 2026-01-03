---
nid: 2440
title: "Responsive design > mobile sites"
slug: "responsive-design-mobile-sites"
date: 2013-12-04T14:17:01+00:00
drupal:
  nid: 2440
  path: /blogs/jeff-geerling/responsive-design-mobile-sites
  body_format: full_html
  redirects: []
tags:
  - design
  - mobile
  - responsive
  - usability
  - ux
---

There are individuals and companies who still believe it would be in their best interest to maintain a 'desktop' version of their website, and a completely or mostly-separate 'mobile' version of their site, and this belief (especially in the corporate arena) was strengthened by a recent (2012) report by the Nielsen Norman Group, <a href="http://www.nngroup.com/articles/mobile-site-vs-full-site/">Mobile Site vs. Full Site</a>, which recommended a separate mobile site with stripped-down features and different design. The idea of having a mobile-optimized design is good—but not with the cost of making it a stripped-down version of your 'full' site, as Nielsen seems to recommend.

<p style="text-align: center;">{{< figure src="./mobile-pnc-site.png" alt="Mobile PNC Website" width="141" height="250" >}}</p>

There are many problems with having separate versions of the website, especially as we near a point where many sites are accessed more on mobile devices (tablets, smartphones), and less on traditional desktop computers:

<ul>
	<li><strong>Mobile is not Mobile</strong>: Many tablets and very-large-screened smartphones are grouped in with other 'mobile' devices, and served an embarrassingly-broken design if you redirect them to a mobile version of your site. Additionally, if you assume that mobile users are out and about and are always in a hurry, so don't care that they're not getting your full site, you're wrong—most smartphone and tablet users spend more time browsing the web on their 'mobile' devices while at home than on their old PCs.</li>
	<li><strong>Mobile users want everything</strong>: The biggest gripe smartphone and tablet users have (and the reason they'll leave your site in an instant) is that your site doesn't let them do what they wanted to do, and know they could've done on your desktop site. They don't only want to search your company's locations and read your blog—they want to do everything they can do on their desktops. Don't just hide half (or more!) of your site's content from half your user base—there's no excuse.</li>
	<li><strong>You will be penalized</strong>: Unless your mobile site is a 1:1 content match for your desktop site, <a href="http://googlewebmastercentral.blogspot.com/2013/12/smartphone-crawl-errors-in-webmaster.html">Google is going to start penalizing you in search results</a>. It's easier to maintain a responsive design than to ensure that you have two entire websites running with the exact same content and URL structure*.</li>
	<li><strong>'Mobile' is the future</strong>: Almost every site that has a separate 'mobile' version treats that version as the outcast. Redesigns are done to the desktop version of the site, and much later to the mobile version—if ever. If you're ignoring the entire smartphone/tablet market in your design, you're ignoring an ever-increasing audience, and your site will be irrelevant in a few years. Especially <a href="http://gigaom.com/2013/12/02/black-friday-shopping-by-the-numbers-mobile-optimized-sites-win/">if your site is a retail site</a>, you lose if you don't consider your mobile device users as first-class citizens.</li>
</ul>

It's time to consider <a href="http://www.lukew.com/ff/entry.asp?933">mobile-first design</a>: focus on what the user wants, not on what marketing thinks looks pretty on their old desktop PCs. Focus on the content, and the simplicity of your site's user experience, not on how many JS widgets and massive navigation structures you can fit on one page.

Scale&nbsp;<em>up</em> your design so it flows differently for desktop browsers. And realize that there aren't only a few screen resolutions. Not only are there iPhones, iPads, and 1080p desktop displays—there are thousands of resolutions in-between.

<span style="font-size: .8em;">*This may be debatable, but the fact is, if you have a content-first design approach and optimize for mobile platforms first (every developer should have a couple mobile devices to test with), the maintenance cost of a responsive design will be much lower (especially when it comes time for major redesigns) than two separate sites.</span>
