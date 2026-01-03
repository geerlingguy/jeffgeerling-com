---
nid: 2268
title: "Allowing Organic Groups Administrators the Ability to Unpublish/Publish and Schedule Content"
slug: "allowing-organic-groups-admini"
date: 2010-03-08T16:04:01+00:00
drupal:
  nid: 2268
  path: /blogs/geerlingguy/allowing-organic-groups-admini
  body_format: full_html
  redirects: []
tags:
  - administration
  - drupal
  - drupal planet
  - organic groups
  - scheduling
---

<p>
	One requirement of the Archdiocese of St. Louis&#39; website is that group administrators are able to publish and unpublish the content inside their groups, and they should also be able to schedule posts for automated publishing and unpublishing at a later time.</p>
<p>
	To do this, I used the following modules:</p>
<ul>
	<li>
		<a href="http://drupal.org/project/og_user_roles">OG User Roles</a></li>
	<li>
		<a href="http://drupal.org/project/scheduler">Scheduler</a></li>
	<li>
		<a href="http://drupal.org/project/publishcontent">Publish Content</a></li>
	<li>
		[EDIT: I&#39;m now using the <a href="http://drupal.org/project/override_node_options">Override Node Options</a> module rather than Publish Content - it gives more fine-grained control over visibility of node form options.]</li>
</ul>
<p>
	After enabling these modules, I spent a while in the Permissions page, and also created a new user role, &quot;administer nodes.&quot; Ironically, I didn&#39;t assign the &#39;administer nodes&#39; permission to this role, because doing so causes a huge mess (&#39;administer nodes&#39; gives waaay too much power to anyone except the site admin&mdash;it&#39;s best to leave that beast unchecked in most cases).</p>
<p class="rtecenter">
	{{< figure src="./scheduling-publishing-unpublishing.png" alt="Scheduling and Publishing options inside a group" width="600" height="289" class="noborder" >}}</p>
<p>
	For the &#39;administer nodes&#39; role, I checked the box next to &#39;schedule (un)publishing of nodes&#39;, which allows users with this role to schedule the publish/unpublish time of a given node. I also checked boxes next to &#39;publish &lt;content type&gt;&#39; and &#39;unpublish &lt;content type&gt;&#39; for each of the content types I wanted users to be able to publish or unpublish (these permissions are under the &quot;publishcontent module&quot; permissions section).</p>
<p>
	Then I went into the OG User Roles module&#39;s configuration page (at admin/og/og_user_roles), and checked the box to allow the &#39;administer nodes&#39; role to be set per group, and also set that as the default role to be added to any user in a group that is made an admin of that group.</p>
<p>
	The OG User Roles module basically assigns all the permissions you assign to a given role within a user&#39;s group only. So you can give some permissions that you&#39;d be very cautious giving out otherwise, because those permissions only affect the user&#39;s group, rather than all sections of the website. (However, there are still some permissions that can wreak havoc on your access control, like &#39;administer nodes&#39;&mdash;always test!).</p>
<p>
	Now, users can schedule content to be posted whenever they&#39;d like, and they can publish or unpublish any content inside their own group(s)!</p>
