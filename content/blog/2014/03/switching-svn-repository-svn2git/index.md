---
nid: 2464
title: "Switching an SVN repository to Git with KDE's Svn2Git"
slug: "switching-svn-repository-svn2git"
date: 2014-03-25T14:35:37+00:00
drupal:
  nid: 2464
  path: /blogs/jeff-geerling/switching-svn-repository-svn2git
  body_format: full_html
  redirects:
    - /blogs/jeff-geerling/switching-svn-repository-git2svn
aliases:
  - /blogs/jeff-geerling/switching-svn-repository-git2svn
  - /blogs/jeff-geerling/switching-svn-repository-svn2git
tags:
  - ansible
  - git
  - kde
  - svn
  - svn2git
  - vcs
---

<p>Some places where I've worked have used SVN for version control, and while the supposed simplicity and centralization of SVN can be nice in certain situations, SVN can't hold a torch to Git's speed, flexibility, and ubiquity (nowadays) for source control. Not to mention SVN doesn't have real tags or branches, just quasi-directories that can easily be mangled into a horrific mess (I see this quite often).</p>

<p>I've had to use some incredibly large (10,000+ revisions, 2GB+ total size) SVN repositories, and while I've managed them using <code>git svn</code> sometimes (see <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/switching-svn-repository-git-svn">Switching an SVN repository to Git using git svn</a>), it's much nicer to be able to migrate the entire team from SVN to Git so everyone can work on the repository much more efficiently.</p>

<p>For small repositories, using Git's built-in git-svn tool is not a big issue; it takes a few minutes to clone an entire SVN repository, and as long as the repository follows conventional SVN layout (<code>branches/</code>, <code>tags/</code> and <code>trunk/</code> are the only three root-level directories, and all branches/tags are flat within their respective directories...), it is simple enough to do the initial clone.</p>

<p>But for non-standard and large repositories, you really need some help. There's a nice ruby gem, <a href="https://github.com/nirvdrum/svn2git">svn2git</a>, that wraps git svn and makes it a little easier to use, and perhaps a little faster... but it inherits all of git-svn's inherent issues, and is still dog-slow on large repositories (conversion takes hours, days, or weeks rather than minutes).</p>

<p>Thus, the KDE team introduced <a href="https://gitorious.org/svn2git/svn2git">Svn2Git</a>. Svn2Git requires Qt4 to compile, but once compiled, the application takes a local copy of the entire SVN repository (e.g. the repository directory from the SVN server, <em>not</em> a local checkout), and quickly converts it to a bare Git repository.</p>

<p><em>Note: Additionally, if you're cloning from a remote SVN repo, or even continuing to work with SVN generally, and you're using <code>http://</code>, you should strongly consider using the <code>svn://</code> or <code>svn+ssh://</code> protocol, which requires the <code>svnserve</code> daemon be running on your SVN server. This will speed up SVN operations noticably (sometimes 10x faster!), as it doesn't incur the overhead of a web server (like Apache), plus one separate web request per operation.</em></p>

<h2>
<a name="using-svn2git-instructions-for-centos" class="anchor" href="#using-svn2git-instructions-for-centos"><span class="octicon octicon-link"></span></a>Using Svn2Git (Instructions for CentOS)</h2>

<p>You need to have Qt4 and libsvn-dev installed on your machine to build Svn2Git, so install those now:</p>


```
$ sudo yum install -y qt qt-devel
$ sudo yum install -y subversion-devel
```

<p>Clone Svn2Git to your local machine, then build it with qmake:</p>


```
$ git clone https://git.gitorious.org/svn2git/svn2git.git
$ cd svn2git
$ qmake && make
```

<p><em>Note: If you get a <code>qmake: command not found</code> error, just use the full path to <code>qmake</code>, which is <code>/usr/lib64/qt4/bin/qmake</code> (on CentOS 6.4, at least).</em></p>

<p>You should now have a binary, <code>svn-all-fast-export</code>, in the directory. You will use that to run Svn2Git after all everything is ready. Next you need to make sure you have a few things in place for the conversion:</p>

<ol>
<li>Make sure you have a rules file (in this case, named <code>rules-file</code>; see the examples in the git2svn folder, and check <a href="http://blog.smartbear.com/software-quality/migrating-from-subversion-to-git-lessons-learned/">this post</a> for some helpful advice for tags).</li>
<li>Make sure you have an authors file (in this case, named <code>authors-file</code>) to map svn commit authors to git authors. The format is like <code>[svn-user] = John Doe <john.doe@example.com></code>, with one mapping per line. (To get a list of all committers in the SVN repository, use the command <code>svn log --quiet | awk '/^r/ {print $3}' | sort -u</code>, as demonstrated in <a href="http://stackoverflow.com/a/2495010/100134">this post on Stack Overflow</a>).</li>
<li>Copy the entire svn repository to a local directory, and make sure it's not named the same as the <code>repository</code> in your rules file. Using scp, the command would be something like <code>scp -r user@example.com:/svn/repositories/old-svn-repository old-svn-repository</code>. Using rsync, the command would be something like <code>rsync -chavzP --stats user@example.com:/svn/repositories/old-svn-repository old-svn-repository</code></li>
</ol><p>Now, you can convert the repository:</p>


```
$ /path/to/svn-all-fast-export --identity-map=authors-file --rules=rules-file --stats --add-metadata old-svn-repository
```

<p><em>Note: <code>--add-metadata</code> adds in SVN information to each commit, for easier lookup of old commits/refs, and <code>--stats</code> outputs useful statistics during the conversion.</em></p>

<p>After a long, long time (or a short time, if you have a tiny/newer repo!), the process will complete, and you'll have a simple bare git repository. Hooray!</p>

<h2>
<a name="notes-on-writing-rules-for-svn2git" class="anchor" href="#notes-on-writing-rules-for-svn2git"><span class="octicon octicon-link"></span></a>Notes on writing rules for Svn2Git</h2>

<p>Take a look at all the <a href="https://gitorious.org/svn2git/svn2git/source/samples">samples</a> in the Svn2Git repository—they have a lot of good information in comments and actual rules. In my case, since the SVN repository had a few oddly-located folders in the root directory (alongside trunk/tags/branches), I just decided to remove them by not telling Svn2Git what to do with them (put this at the end of the file):</p>


```
# Ignore all other directories.
match /
end match
```

<p>Also, as Cody Casterline mentioned in his <a href="http://blog.smartbear.com/software-quality/migrating-from-subversion-to-git-lessons-learned/">Lessons Learned</a> post, you can still extract tags from your converted repository (even though the conversion turns tags into branches) by adding a rule like:</p>


```
# Add a prefix to all tag branches so we can fix them later.
match /tags/([^/]+)/
  repository [repository-name]
  branch tag--\1
end match
```

<p>Then, after the conversion is complete, do the following (paste the entire code block below into your terminal and hit Enter):</p>


```
git branch |
# Remove spaces at beginning of line:
sed s/..// |
# Only get 'tag' branches:
grep ^tag-- |
# Strip down to just the tag name:
sed s/tag--// |
while read tagname; do
  git tag -a "$tagname" -m "Tag imported from SVN." "tag--$tagname" >/dev/null 2>/dev/null && echo "tagged: $tagname"
  git branch -D "tag--$tagname" >/dev/null 2>/dev/null && echo "deleted branch: tag--$tagname"
done
```

<p>If you want to delete all the tag branches (after you've made sure the tags converted successfully), run the same command above with <code>git branch -D "tag--$tagname" >/dev/null 2>/dev/null && echo "deleted branch: tag--$tagname";</code> for the command inside the loop.</p>

<p>Finally, if you get errors about branches not conforming to Git branch naming standards, you might need to convert spaces and other special characters to underscores. I had some branches with spaces, so I adjusted the rule for <code>branches</code> (thanks to PovAddictW on the #kde-git IRC channel for the tip!):</p>


```
match /branches/([^/]+)/
  repository [repository-name]
  branch \1
  substitute branch s/ /_/
end match
```

<h2>
<a name="finishing-things-off" class="anchor" href="#finishing-things-off"><span class="octicon octicon-link"></span></a>Finishing things off</h2>

<p>Once I had my new <code>repository.git</code> bare repo, I changed directory into the folder, added a remote to which I could push the repo, then used <code>git push --all</code> and <code>git push --tags</code> to push all branches and tags up to the new remote.</p>

<p>The next step for me is setting up a script (maybe running via cron) that will periodically update the git repo and re-sync the latest changes from SVN. It would be most excellent if I could figure out a way to make the synchronization go both ways, so developers could just use Git if they want... we'll see!</p>

<p>Also, I've added an <a href="https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/svn2git">Svn2Git VM example</a> to my <a href="https://github.com/geerlingguy/ansible-vagrant-examples">Ansible Vagrant Examples</a> project on GitHub—you can easily boot up a Linux VM with everything preconfigured so you can skip ahead to actually running the <code>svn-all-fast-export</code> command within a few minutes (rather than configure and build Svn2Git on your own).</p>

<h2>
<a name="further-reading" class="anchor" href="#further-reading"><span class="octicon octicon-link"></span></a>Further Reading</h2>

<ul>
<li><a href="https://gitorious.org/svn2git/svn2git">Svn2Git</a></li>
<li><a href="http://programminglist.blogspot.com/2013/11/svn2git-svn-all-fast-export-common.html">Svn2Git svn-all-fast-export Common Errors</a></li>
<li><a href="http://techbase.kde.org/Projects/MoveToGit/UsingSvn2Git">Using Svn2Git</a></li>
<li><a href="https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/svn2git">Svn2Git demo VM</a></li>
</ul>
