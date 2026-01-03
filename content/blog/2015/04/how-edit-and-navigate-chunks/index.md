---
nid: 2487
title: "How to edit and navigate chunks of a giant text file on Mac/Linux"
slug: "how-edit-and-navigate-chunks"
date: 2015-04-14T20:59:55+00:00
drupal:
  nid: 2487
  path: /blogs/jeff-geerling/how-edit-and-navigate-chunks
  body_format: full_html
  redirects: []
tags:
  - command line
  - editor
  - large file
  - logging
  - sed
  - terminal
---

For most log and text files, simply opening them up in <code>$editor_of_your_choice</code> works fine. If the file is less than a few hundred megabytes, <em>most</em> modern editors (and even some IDEs) shouldn't choke on them too badly.

But what if you have a 1, 2, or 10 GB logfile or giant text file you need to search through? Finding a line with a bit of text is simple enough (and not too slow) if you're using <code>grep</code>. But if you want to grab a chunk of the file and edit that chunk, or split the file into smaller files, there's a simple process that I use, based on <a href="http://stackoverflow.com/a/6874645/100134">this Stack Overflow answer</a>:

<ol>
<li>Run the following once to find the starting line number in the file, then again to find the last line you're interested in:
<code>grep -n 'string-to-search' giant.log | head -n 1</code></li>
<li>Taking the results of the first search (<code>X</code>) and the second (<code>Y</code>), create a smaller chunk of the giant file in the same directory:
<code>sed -n -e 'X,Yp' -e 'Yq' giant.log > small.log</code></li>
</ol>

I usually don't need to reunite the smaller chunks again, but if you do, you can recombine the file using the suggestion in the original <a href="http://stackoverflow.com/a/6874645/100134">Stack Overflow answer</a>.
