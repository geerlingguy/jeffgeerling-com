---
nid: 2485
title: "Drupal on Mothballs - Convert Drupal 6 or 7 sites to static HTML"
slug: "drupal-on-mothballs-convert-static-html"
date: 2015-04-02T15:35:11+00:00
drupal:
  nid: 2485
  path: /blogs/jeff-geerling/drupal-on-mothballs-convert-static-html
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 6
  - drupal 7
  - drupal 8
  - drupal planet
  - security
  - sitesucker
  - static
aliases:
  - /blogs/jeff-geerling/drupal-on-mothballs-convert-static-html
---

Drupal.org has an excellent resource page to help you <a href="https://www.drupal.org/node/27882">create a static archive of a Drupal site</a>. The page references tools and techniques to take your dynamically-generated Drupal site and turn it into a static HTML site with all the right resources so you can put the site on mothballs.

From time to time, one of Midwestern Mac's hosted sites is no longer updated (e.g. <a href="http://www.lolsaints.com/">LOLSaints.com</a>), or the event for which the site was created has long since passed (e.g. the <a href="http://2014.drupalstl.org/">2014 DrupalCamp STL site</a>).

I though I'd document my own workflow for converting typical Drupal 6 and 7 sites to static HTML to be served up on a simple Apache or Nginx web server without PHP, MySQL, or any other special software, since I do a few special things to preserve the original URL alias structure, keep CSS, JS and images in order, and make sure redirections still work properly.

<h2>1 - Disable forms and any non-static-friendly modules</h2>

The Drupal.org page above has some good guidelines, but basically, you need to make sure to all the 'dynamic' aspects of the site are disabled—turn off all forms, turn off modules that use AJAX requests (like Fivestar voting), turn off search (if it's using Solr or Drupal's built-in search), and make sure AJAX and exposed filters are disabled in all views on the site—a fully static site doesn't support this kind of functionality, and if you leave it in place, there will be a lot of broken functionality.

<h2>2 - Download a verbatim copy of the site with SiteSucker</h2>

CLI utilities like HTTrack and wget can be used to download a site, using a specific set of parameters to make sure the download is executed correctly, but since I only convert one or two sites per year, I like the easier interface provided by <a href="http://www.sitesucker.us/mac/mac.html">SiteSucker</a>.

SiteSucker lets you set options for a download (you can save your custom presets if you like), and then it gives a good overview of the entire download process:

<p style="text-align: center;">{{< figure src="./sitesucker-download-drupal-site.png" alt="SiteSucker Drupal Download Site" width="653" height="305" >}}</p>

I change the following settings from the defaults to make the download go faster and result in a mostly-unmodified download of the site:

<ul>
<li>General
<ul>
<li>General > Ignore Robot Exclusions<br>
(If you have a slower or shared server and hundreds or thousands of pages on the site, you might not want to check this box—Ignoring the exclusions and the crawler delay can greatly increase the load on a slow or misconfigured webserver when crawling a Drupal site).</li>
<li>General > Always Download HTML and CSS</li>
<li>General > File Modification: None</li>
<li>URL > Options > URL Constraint: Host</li>
</ul></li>
</ul>

After the download completes, I zip up the archive for the site, transfer it to my static Apache server, and set up the virtualhost for the site like any other virtualhost. To test things out, I point the domain for my site to the new server in my local <code>/etc/hosts</code> file, and visit the site.

<h2>3 - Make Drupal paths work using Apache rewrites</h2>

Once you're finished getting all the files downloaded, there are some additional things you need to configure on the webserver level—in this case, Apache—to make sure that file paths and directories work properly on your now-static site.

A couple neat tricks:

<ul>
<li>You can preserve Drupal pager functionality without having to modify the actual links in HTML files by setting <code>DirectorySlash Off</code> (otherwise Apache will inject an extra <code>/</code> in the URL and cause weird side effects), then setting up a specialized rewrite using <code>mod_rewrite</code> rules.</li>
<li>You can redirect links to <code>/node</code> (or whatever was configured as the 'front page' in Drupal) to <code>/</code> with another <code>mod_rewrite</code> rule.</li>
<li>You can preserve links to pages that are now also directories in the static download using another <code>mod_rewrite</code> rule (e.g. if you have a page at <code>/archive</code> that should load <code>archive.html</code>, and there are also pages accessible at <code>/archive/xyz</code>, then you need a rule to make sure a request to <code>/archive</code> loads the HTML file, and doesn't try loading a directory index!).</li>
<li>Since the site is now static, and presumably won't be seeing much change, you can set far future expires headers for all resources so browsers can cache them for a long period of time (see the <code>mod_expires</code> section in the example below).</li>
</ul>

Here's the base set of rules that I put into a .htaccess file in the document root of the static site on an Apache server for static sites created from Drupal sites:

```
<IfModule mod_dir.c>
  # Without this directive, directory access rewrites and pagers don't work
  # correctly. See 'Rewrite directory accesses' rule below.
  DirectorySlash Off
</IfModule>

<IfModule mod_rewrite.c>
  RewriteEngine On

  # Fix /node pagers (e.g. '/node?page=1').
  RewriteCond %{REQUEST_URI} ^/node$
  RewriteCond %{QUERY_STRING} ^page=(.+$)
  RewriteRule ^([^\.]+)$ index-page=%1.html [NC,L]

  # Fix other pagers (e.g. '/archive?page=1').
  RewriteCond %{REQUEST_URI} !^/node$
  RewriteCond %{QUERY_STRING} ^page=(.+$)
  RewriteRule ^([^\.]+)$ $1-page=%1.html [NC,L]

  # Redirect /node to home.
  RewriteCond %{QUERY_STRING} !^page=.+$
  RewriteRule ^node$ / [L,R=301]

  # Rewrite directory accesses to 'directory.html'.
  RewriteCond %{REQUEST_FILENAME} -d
  RewriteCond %{QUERY_STRING} !^page=.+$
  RewriteRule ^(.+[^/])/$ $1.html [NC,L]

  # If no extension included with the request URL, invisibly rewrite to .html.
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^([^\.]+)$ $1.html [NC,L]

  # Redirect non-www to www.
  RewriteCond %{HTTP_HOST} ^example\.com$ [NC]
  RewriteRule ^(.*)$ http://www.example.com/$1 [L,R=301]
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  <FilesMatch "\.(ico|pdf|flv|jpg|jpeg|png|gif|js|css|swf)$">
    ExpiresDefault "access plus 1 year"
  </FilesMatch>
</IfModule>
```

<h2>Alternative method using a localized copy of the site</h2>

Another more time-consuming method is to download a localized copy of the site (where links are transformed to be relative, linking directly to <code>.html</code> files instead of the normal Drupal paths (e.g. <code>/archive.html</code> instead of <code>/archive</code>). To do this, download the site using SiteSucker as outlined above, but select 'Localize' for the 'File Modification' option in the General settings.

There are some regex-based replacements that can clean up this localized copy, depending on how you want to use it. If you use Sublime Text, you can use these for project-wide find and replace, and use the 'Save All' and 'Close All Files' options after each find/replace operation.

I'm adding these regexes to this post in case you might find one or more of them useful—sometimes I have needed to use one or more of them, other times none:

Convert links to index.html to links to `/`:

  - Find: `(<a href=")[\.\./]+?index\.html(")`
  - Replace: `\1/\2`

Remove .html in internal links:

  - Find: `(<a href="[^http].+)\.html(")`
  - Replace: `\1\2`

Fix one-off link problems (e.g. Feedburner links detected as internal links):

  - Find: `(href=").+(feeds2?.feedburner)`
  - Replace: `\1http://\2`

Fix other home page links that were missed earlier:

  - Find: `href="index"`
  - Replace: `href="/"`

Fix relative links like `../../page`:

  - Find: `((href|src)=")[\.\./]+(.+?")`
  - Replace: `\1/\3`

Fix relative links in top-level files:

  - Find: `((href|src)=")([^/][^http].+?")`
  - Replace: `\1/\3`

This secondary method can sometimes make for a static site that's easier to test locally or distribute offline, but I've only ever localized the site like this once or twice, since the other method is generally easier to get going and doesn't require a ton of regex-based manipulation.
