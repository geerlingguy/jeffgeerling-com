---
nid: 2463
title: "Switching an SVN repository to Git using git svn"
slug: "switching-svn-repository-git-svn"
date: 2014-08-04T14:28:06+00:00
drupal:
  nid: 2463
  path: /blogs/jeff-geerling/switching-svn-repository-git-svn
  body_format: full_html
  redirects: []
tags:
  - conversion
  - git
  - svn
  - svn2git
aliases:
  - /blogs/jeff-geerling/switching-svn-repository-git-svn
---

Converting from an SVN repository to a Git repository is fairly simple—you just want to move all the commits across, preserve your tags and branches, and make sure all the commit authorship translates properly. The simplest method (though not always fastest) is to use the <code>git svn</code> command to do the full conversion. (Note also that you could interact with an SVN repository with Git as the middle man using <code>git svn</code>... but this blog post is just about doing a full conversion).

<h2>Converting the authors</h2>

Before you convert the SVN repository to Git, you need to get a list of all the SVN commit authors, and then set up the list for <code>git svn</code> to be able to translate SVN commit authors to Git commit authors (the Git format is slightly different, using a name + email combination). First, in a terminal window, run the following command within a local checkout of the SVN repository:

```
svn log -q | awk -F '|' '/^r/ {sub("^ ", "", $2); sub(" $", "", $2); print $2" = "$2" <"$2">"}' | sort -u > authors.txt
```

Next, edit the authors.txt file and change lines to match Git authorship information. So a line like:

```
johndoe = johndoe <johndoe>
```

Might be transformed into:

```
johndoe = John Doe <johndoe@example.com>
```

(The values for the name and email would correspond to what you set in Git using <code>git config --global user.name</code> and <code>user.email</code>).

<h2>Converting the repository</h2>

At its simplest, the <code>git svn</code> command just needs a few arguments:

```
git svn clone SVN_REPOSITORY_URL --no-metadata -A authors.txt --stdlayout LOCAL_DIRECTORY
```

Where:

<ul>
<li><code>SVN_REPOSITORY_URL</code> is the URL of the SVN repository you're converting.</li>
<li><code>authors.txt</code> is the path to the authors file you just created (assuming you're still in the same directory as you were when you created it earlier).</li>
<li><code>LOCAL_DIRECTORY</code> is the directory where the git repository will be created (with the latest master branch revision checked out).</li>
</ul>

Note that files from the master branch (along with a .git folder) will be checked out <em>directly</em> into the local directory; so create an empty folder for this step!

<h3>Caveats for non-standard SVN layouts, preserving tags, etc.</h3>

Because SVN isn't very strict about where things go, and how you can structure branches, tags, etc., you will likely run into situations where you need to tell <code>git svn</code> about weird branch layouts, or tags that don't conform to any rational standard (or have weird characters in their names).

In these cases, please check out John Albin's excellent and more fully-detailed article on <a href="http://john.albin.net/git/convert-subversion-to-git">Converting a Subversion repository to Git</a>.

<h2>Alternative conversion methods</h2>

One major downside to <code>git svn</code> is the time it takes to do the conversion—for small repositories having less than a few hundred commits, it's not an issue... but I've had to convert repositories with hundreds of branches, thousands of tags, and over 10,000 revisions. Initial testing found that the conversion took over 5 days on a pretty fast machine directly connected to the SVN server! I would recommend you check out <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/switching-svn-repository-git2svn">how to convert the repository using SVN2Git</a>, a super-fast SVN to Git conversion application created by the KDE team. What takes days could take minutes using SVN2Git.
