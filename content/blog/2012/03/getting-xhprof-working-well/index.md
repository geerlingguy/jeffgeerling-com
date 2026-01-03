---
nid: 2363
title: "Getting XHProf working well on Mac OS X Lion"
slug: "getting-xhprof-working-well"
date: 2012-03-19T00:51:42+00:00
drupal:
  nid: 2363
  path: /blogs/jeff-geerling/getting-xhprof-working-well
  body_format: full_html
  redirects: []
tags:
  - analytics
  - devel
  - drupal
  - drupal 6
  - drupal 7
  - drupal planet
  - performance
  - xhprof
aliases:
  - /blogs/jeff-geerling/getting-xhprof-working-well
---

I was inspired today to get XHProf working on my Mac, using MAMP PRO 2.0.5/PHP 5.3.6, after reading <a href="https://twitter.com/#!/davereid/status/181192156227190784">@Dave Reid's tweet</a>. Since I'm not leaving for DrupalCon until tomorrow, what else could I do today? There's an <a href="http://www.lullabot.com/articles/installing-xhprof-mamp-and-php-52-on-mac-os-106-snow-leopard">excellent article on Lullabot</a> that will help you get 85% of the way towards having XHProf up and running on your Mac, working with your Drupal sites, but there are a few missing pieces and little tips that will help you get XHProf fully-armed and operational.

<p style="text-align: center;">{{< figure src="./xhprof-callgraph.png" alt="XHProf Callgraph example" width="251" height="500" >}}
Ooh, pretty visualizations!</p>

First, after you've installed and configured XHProf on your Mac (and restarted MAMP/Apache so the configuration takes effect), you need to do a few things to get it working well with Drupal. For starters, if you have the <a href="http://drupal.org/project/devel">Devel</a> module installed, head over to its configuration page (at <code>admin/config/development/devel</code>), and check the box that says "Enable profiling of all page views and drush requests."

Now, enter the following values in the two fields that appear (note: these paths could be different depending on where you installed xhprof, and how you have your Sites folder/localhost set up. For simplicity, I kept the xhprof stuff in MAMP's htdocs folder):

<ul>
<li><strong>xhprof directory</strong>: <code>/Applications/MAMP/htdocs/xhprof</code></li>
<li><strong>xhprof url</strong>: <code>http://localhost/xhprof/xhprof_html</code></li>
</ul>

Save the configuration, and refresh the page. Scroll down to the bottom of the page, and click on the newly-added link in the Developer information section titled 'XHProf output'. You should see a huge table with large, menacing numbers. Don't worry about interpreting them just yet. (If you got an error, or something other than a table of a bunch of functions and numbers, then XHProf is not configured correctly).

Now, click on the <code>[View Full Callgraph]</code> link towards the top of the page. You'll probably get an error like:

```
Error: either we can not find profile data for run_id [ID-HERE] or the threshold 0.01 is too small or you do not have 'dot' image generation utility installed.
```

This is because <a href="http://www.graphviz.org/">GraphViz</a> (which provides the 'dot' utility) is not installed on your computer, or it's not in your $PATH. So, go ahead and <a href="http://www.ryandesign.com/graphviz/">download the OS X-compiled version of GraphViz</a> appropriate to your computer (I downloaded the Intel version 2.14.1), and install it (it uses the normal Mac installer, and puts the files in <code>/usr/local/graphviz-2.14</code>).

The final step to get dot working correctly is to make a symlink to the dot binary using <code>ln -s</code> (in my case, /usr/local/bin is in my $PATH, as defined in <code>~/.bash_profile</code>):

```
$ sudo ln -s /usr/local/graphviz-2.14/bin/dot /usr/local/bin/dot
```

NOW, go ahead and jump back over to your fancy XHProf data table page, and click the Callgraph link. Wait a minute, and you'll be rewarded with a beautiful graphical representation of where Drupal/PHP spends all its time, with colors, arrows, lines, and numbers to your heart's content!

The last step for getting XHProf would be to install the <a href="http://drupal.org/project/XHProf">XHProf</a> module on your site and get the data displaying inside Drupal—but I haven't been able to install it yet on my own site (there was an installation error), and the standard interface that I get (provided by XHProf itself) is good enough for me.

<em>(Remember to clean out the directory where you're saving your XHProf runs every now and then (this directory is configured in php.ini as the <code>xhprof.output_dir</code> variable); each run will be 100-200KB, and that adds up as you load and reload tons of pages!).</em>
