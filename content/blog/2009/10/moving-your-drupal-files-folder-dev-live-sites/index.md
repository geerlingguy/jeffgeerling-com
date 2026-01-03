---
nid: 2269
title: "Moving Your Drupal 'files' Folder - Dev to Live Sites"
slug: "moving-your-drupal-files-folder-dev-live-sites"
date: 2009-10-06T16:46:50+00:00
drupal:
  nid: 2269
  path: /blogs/geerlingguy/moving-your-drupal-files-folder-dev-live-sites
  body_format: full_html
  redirects: []
tags:
  - drupal
  - files
  - management
  - staging
  - testing
  - website
aliases:
  - /blogs/geerlingguy/moving-your-drupal-files-folder-dev-live-sites
---

<p>
	When I was rebuilding www.jeffgeerling.com in Drupal, I decided to use the testing domain <strong>new.jeffgeerling.com</strong>. This presented me with a challenge, once I started working a bit more on the site, as I set up imagecache, the file system, the favicon, the logo, internal images in posts, images inserted into blocks, etc., into my <strong>/sites/new.jeffgeerling.com/files</strong> directory.</p>
<p>
	If I simply renamed the directory to &#39;jeffgeerling.com&#39; and went live, I&#39;d end up with tons of 404 errors. Currently, there&#39;s no easy way to switch the location of your files directory in Drupal. Lacking an easy method, it&#39;s time to get your hands dirty with a little SQL (I entered the following commands via phpMyAdmin, since my host doesn&#39;t yet allow SSH access):</p>
<ul>
	<li>
		Update the files table (which is used by the system as well as imagecache):
		<ul>
			<li>
				<code>UPDATE `files` SET `filepath` = REPLACE(`filepath`, `sites/OLDDOMAIN/files/`, `sites/NEWDOMAIN/files/`);</code></li>
		</ul>
	</li>
	<li>
		Update the boxes table (which is used for all the block content):
		<ul>
			<li>
				<code>UPDATE `boxes` SET `body` = REPLACE(`body`, `sites/OLDDOMAIN/files/`, `sites/NEWDOMAIN/files/`);</code></li>
		</ul>
	</li>
	<li>
		Update the node_revisions table (all the node content is in here... you&#39;ll need to update both the body and the teaser fields):
		<ul>
			<li>
				<code>UPDATE `node_revisions` SET `body` = REPLACE(`body`, `sites/OLDDOMAIN/files/`, `sites/NEWDOMAIN/files/`);</code></li>
			<li>
				<code>UPDATE `node_revisions` SET `teaser` = REPLACE(`teaser`, `sites/OLDDOMAIN/files/`, `sites/NEWDOMAIN/files/`);</code></li>
		</ul>
	</li>
	<li>
		Update the users table &#39;picture&#39; value (if you&#39;re using user pictures):
		<ul>
			<li>
				<code>UPDATE `users` SET `picture` = REPLACE(`picture`, `sites/OLDDOMAIN/files/pictures/`, `sites/NEWDOMAIN/files/pictures/`);</code></li>
		</ul>
	</li>
</ul>
<p>
	Now make sure you clear your cache tables (I just used &#39;Clear caches&#39; in my Admin menu), then empty your watchdog table (<code>TRUNCATE `watchdog`;</code>) and look for any 404 errors. If you find a bunch, there might be another field you need to update with your new filepath.</p>
<p>
	Hopefully Drupal core will be better able to handle file moving in version 7&mdash;I haven&#39;t studied that too much yet, but I&#39;ve heard files will be treated more as &#39;first class citizens.&#39; Until then, you can either have fun with the above MySQL queries, or you could use private file handling (which uses a path such as /system/files, and allows your file path to be whatever you&#39;d like).</p>
<p>
	(One other solution is to set up a folder like /sites/sitename instead of /sites/sitename.com, and set up a symlink to the /sites/sitename folder... that&#39;s okay, I guess... but not ideal. It would be best if Drupal could handle this stuff (path aliasing, etc.) out of the box.).</p>
