---
nid: 2266
title: "Getting a Views Page Display to Appear Inside an Organic Group"
slug: "getting-views-page-display-app"
date: 2010-02-09T18:57:56+00:00
drupal:
  nid: 2266
  path: /blogs/geerlingguy/getting-views-page-display-app
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - og
  - organic groups
  - views
---

<p>
	I have been hitting my head against a wall for a few weeks now, trying to get a few different Views-created pages to appear as if they were normal pages inside an Organic Group (meaning they would appear inside og-menu-enabled menus for that particular group, and group blocks would also appear on the pages.</p>
<p>
	After reading up on the thread &quot;<a href="http://drupal.org/node/650178">Organic Groups and Views 2</a>&quot;, I found that I could use an argument to help solve my dilemma. Here&#39;s how I set up an argument for a particular view:</p>
<p>
	On the page display (I could&#39;ve also done this as a default), I added an argument (&quot;<strong>Organic groups: Groups</strong>&quot;) with the following properties:</p>
<ul>
	<li>
		Title: <strong>&lt;none&gt;</strong></li>
	<li>
		Breadcrumb: <strong>&lt;none&gt;</strong></li>
	<li>
		Action to take if argument is not present: <strong>Provide default argument</strong>
		<ul>
			<li>
				Default argument type: <strong>Fixed entry</strong>
				<ul>
					<li>
						Default Argument: <strong>6116</strong> (this is the node ID for the organic group under which this view is posted)</li>
				</ul>
			</li>
			<li>
				Validator options
				<ul>
					<li>
						Validator: <strong>Group nodes</strong>
						<ul>
							<li>
								Argument type: <strong>Node ID</strong></li>
							<li>
								Validate current user: <strong>&lt;unchecked&gt;</strong></li>
						</ul>
					</li>
					<li>
						Action to take if argument is not present: <strong>Hide view / Page not found (404)</strong></li>
				</ul>
			</li>
		</ul>
	</li>
	<li>
		Allow multiple terms per argument: <strong>&lt;unchecked&gt;</strong></li>
	<li>
		Exclude the argument: <strong>&lt;unchecked&gt;</strong></li>
</ul>
<p>
	Doing this allows Organic Groups to treat the Views page display as if it is actually a page within that particular group. Another problem solved! (I&#39;m really beginning to fall in love with Views... and, apparently, Views 3 is going to be even <a href="http://www.angrydonuts.com/views-3-x-roadmap"><em>more</em></a> full of win!</p>
<h3>
	Another Option - Embed in Page</h3>
<p>
	You can also embed a view directly in a page, using the context of that page in your view to grab the items for the group into which the view is embedded.</p>
<p>
	To do so, create a new page/story/whatever node, with &#39;PHP Code&#39; as the input format. Inside the node, put in <code>
<?php print views_embed_view('group_newsletters'); ?>
</code>and save your node.</p>
<p>
	In the view you wish to embed (name it <code>view_name</code> as you used in the code above), add an argument like the following (with type <strong>Organic Groups: Groups</strong>):</p>
<ul>
	<li>
		Title: <strong>&lt;none&gt;</strong></li>
	<li>
		Breadcrumb: <strong>&lt;none&gt;</strong></li>
	<li>
		Action to take if argument is not present: <strong>Provide default argument</strong>
		<ul>
			<li>
				Default argument type: <strong>PHP Code</strong>
				<ul>
					<li>
						PHP Argument Code:</li>
					<li>
<code>
<?php if ($node = og_get_group_context()) {
$args[0] = $node->nid;
return $args[0];
}
else {
  return NULL;
}?>
</code>					</li>
				</ul>
			</li>
			<li>
				Validator options
				<ul>
					<li>
						Validator: <strong>Group nodes</strong>
						<ul>
							<li>
								Argument type: <strong>Node ID</strong></li>
							<li>
								Validate current user: <strong>&lt;unchecked&gt;</strong></li>
						</ul>
					</li>
					<li>
						Action to take if argument is not present: <strong>Hide view / Page not found (404)</strong></li>
				</ul>
			</li>
		</ul>
	</li>
	<li>
		Allow multiple terms per argument: <strong>&lt;unchecked&gt;</strong></li>
	<li>
		Exclude the argument: <strong>&lt;unchecked&gt;</strong></li>
</ul>
