---
nid: 2591
title: "PHP: It doesn't have to be a bad experience"
slug: "php-it-doesnt-have-be-bad-experience"
date: 2014-04-23T03:30:08+00:00
drupal:
  nid: 2591
  path: /blog/php-it-doesnt-have-be-bad-experience
  body_format: full_html
  redirects: []
tags:
  - essay
  - php
  - php-fig
aliases:
  - /blog/php-it-doesnt-have-be-bad-experience
---

It gets a little bit under my skin when I see a link to <a href="http://me.veekun.com/blog/2012/04/09/php-a-fractal-of-bad-design/">PHP: A fractal of bad design</a> posted in the comments on <em>every</em> article mentioning PHP on tech sites, blogs, and forums.

<p style="text-align: center;"><a href="http://knowyourmeme.com/photos/115682-computer-reaction-faces">{{< figure src="./computer-reaction-face-suspicious.jpg" alt="Computer Reaction Face - Suspicious" width="300" height="299" >}}</p>

PHP developers get it: <em>PHP is full of ugly warts, and is not perfect.</em> Far from it.

Developers brazen enough to admit they don't detest every minute of programming in PHP are blithely dismissed by 'real' developers. Ironically, many of these 'real' developers enjoy using some other dynamically-typed language to which 80% of the arguments against PHP equally apply.

While I primarily develop with PHP, I have developed some smaller projects in Objective C, Java, Python, and JavaScript. I do a fair bit of shell scripting and have dabbled in C, Ruby, and a tiny bit of Go. I'm by no means a master programmer, but I have a decent grasp of fundamental concepts of programming, architecture, and what makes 'good code' and ease of development.

And I have to say, it is easy to write terrible, terrible code in languages other than PHP. Code that is poorly documented (and is not <a href="http://c2.com/cgi/wiki?SelfDocumentingCode">self-documenting</a>), code that has messy variable names, code that is slow due to unnecessary type conversions and poorly-implemented loops. Every language has unintuitive parts—PHP more than most—but if you're an intelligent programmer, you can avoid them.

I think developers hate <em>PHP</em> like writers hate English; the language itself has myriad inconsistencies and oddities, but the thing they hate most is the use and abuse of these things. Much of the PHP <em>code</em> 'in the wild' is terrible (including <a href="http://phpmanualmasterpieces.tumblr.com/">code examples in comments</a> on the official PHP documentation). There are still PHP applications in <em>active</em> development that are using long-past-deprecated functions and worst practices, and have no coding or documentation standards. It's a mess.

Anyways, to my original point and the title of this post: PHP doesn't have to be a bad experience. You can build great things with PHP, and do so in a way that results in performant (for a dynamic language), maintainable, and even beautiful code (at least, if you're not prejudiced against C-style syntax and dollar-sign-prefixed variables). PHP is not suited to every project, but is a relatively powerful language for web development. This post is not meant to be a direct rebuttal to any of the posts highlighting PHP's flaws, but rather a guide to help those who <em>do</em> use PHP.

<h3>Sanity by Documentation</h3>

Though you can use type hinting in PHP for non-scalar variables (objects, callables, arrays, etc.), and type hinting for scalars (string, int, bool, etc.) will be included in upcoming releases, many PHP developers and projects have agreed on one basic principle: You should, at a minimum, document the expected type of every variable passed into a method, and the type of the method's return value (if any).

Bad:

```
```
<?php
// Get $uid records.
function doFoo($uid) {
  ...
  return $records;
}
?>
```
```

Better:

```
```
<?php
/**
 * Get records for a given user ID.
 *
 * @param int $uid
 *   A user ID.
 *
 * @return array
 *   The records for the given user.
 */
function getRecordsForUid($uid) {
  ...
  return $records;
}
?>
```
```

Explicit definitions of parameters and return values make every aspect of this function obvious. And yet, most of the PHP code I've seen in the wild looks like the first example above, or worse—many developers leave no comments at all! This is not a problem restricted to PHP, either. I've seen plenty of Javascript, Ruby, and Python code with the same issue.

Using a descriptive method name and documenting all parameters and return values makes working with a dynamic language like PHP so much easier. In PHP 5.6+, documentation of obvious parameters like IDs could easily be done inline with type hinting:

```
```
<?php
function getRecordsForUid(int $id) { }
?>
```
```

Compare this to an example from Java, which additionally declares the return value:

```
// 'int' declares that the max() method will return an integer.
int max(int num1, int num2) { }
```

Also, adding comments to bits of code that don't do simple/obvious things is a very good idea. And making sure variable names are verbose and meaningful (<code>$row_count</code> instead of <code>$rc</code>, <code>$json_callback</code> instead of <code>$func</code>) helps make code readable, saving future developers (and yourself) immeasurable time in debugging/extending your code. More good discussion about naming conventions: <a href="http://www.bitnative.com/2013/10/18/dynamic-language-naming-matters-more/">Writing in a Dynamic Language? Naming Matters More</a>.

<h3>Use sane return values</h3>

Many developers are lured into a very dangerous trap when using dynamic languages: returning many different variable types from one method:

```
```
<?php
function getResultForID($id) {
  if ($id == 123) {
    return 1;
  elseif ($id == 456) {
    return SomeObject();
  else {
    return false;
  }
}
?>
```
```

Even if you document your method and state that your return value might be an integer, an object, or a boolean, depending on the parameters, this method will be difficult to use; any time the method is called, the caller will need to deal with three different return types—or, if it is only built to handle one type, and another is returned, what then?

If you're returning a boolean, return only a boolean. If you're returning a collection, return an array (or empty <code>array()</code> if nothing was found). If you're returning a string, return a string or an empty string. One potential convenience of PHP is that empty arrays and strings, and the integer 0, evaluate to boolean false if used in a conditional context; there's no need to return false or null if you're just declaring an empty set or nothing found.

If you encountered an error, throw an exception. Don't return false or a string like 'error'.

For more discussion on sanity and return types, please read <a href="http://www.garfieldtech.com/blog/empty-return-values">On empty return values</a>.

<h3>Coding Standards: Have them, use them</h3>

All the most vibrant developer communities I've encountered have had, and upheld, fairly strict coding standards. Many individual developers seem to scoff at regulations on spacing, function and variable naming, and the like, dismissing them in favor of code that 'just works, but isn't fancy'.

The problem is that humans are not compilers. Compilers might not care that you start a file with a short PHP tag (<code>\<?</code>), don't use brackets for simple one-line <code>if</code> statements, or use a tab character instead of two or four spaces for indentation (if you use any indentation at all!). But humans <em>do</em>—if you ever need to work on code with another developer, these seemingly minor things can hinder your forward progress. Think of it this way: coding without standards is like speaking old English in a group of modern English-speaking friends. What you have is a <a href="http://www.youtube.com/watch?v=SnO9Jyz82Ps">failure to communicate</a>.

Coding standards are not arbitrary rules imposed by developers with severe OCD, but are helpful rules borne out of years of experience and collaborative programming that increase readability.

Whenever you develop, you should develop to a certain standard. If you work with an open source project (e.g. Symfony, Drupal, Laravel, etc.), you should learn that project's coding standards and use them—both for contributed code and for code you use on your own projects.

Also, it's easy to integrate code standards review into your PHP code review/deployment process. For example, in <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/ci-deployments-code-analysis-drupal-php">CI: Deployments and Static Code Analysis with Drupal/PHP</a>, I demonstrate how to run your code through a thorough coding standards review using <a href="http://pear.php.net/package/PHP_CodeSniffer/">PHP CodeSniffer</a>, <a href="http://phpmd.org/">PHP Mess Detector</a>, and other tools using <a href="http://jenkins-ci.org/">Jenkins</a>, then see the results graphically via <a href="http://www.sonarqube.org/">SonarQube</a>.

<h3>Don't do things that will burn you later</h3>

There are many seemingly inconsequential things you might be doing that will result in problems—if not now, then next time you or someone else encounters the code you've written. Here are some things you can do to prevent problems when reading, rebuilding, or refactoring PHP:

<ul>
<li>Use brackets with <code>if</code> statements. Always.</li>
<li>Don't use 'alternate syntax' like <code>if: elseif: endif;</code> (except, in some cases, in template files) or "<?" (short open tags).
<li>Use descriptive variable names (not too long, but <code>$username</code> and <code>$price_per_unit</code> are better than <code>$un</code> and <code>$ppu</code>.</li>
<li>Use <code>PDO</code>, and don't use <code>mysql_</code> statements.</li>
<li>Don't mix PHP and markup on anything more complex than a basic one-page demo script.</li>
<li>Don't ever use "?>" in a PHP file, unless it's part of a template using only the most basic PHP constructs.</li>
<li><del>Memorize this: <em>arrays = needle, haystack; strings = haystack, needle</em>. Many people get tripped up on the <code>array_*</code> functions and <code>strpos()</code> and the like. It's weird and annoying, but at least it's consistently so.</del> Nevermind, just rely on your IDE, like I do. Autocomplete, and fill in the needle and haystack accordingly.</li>
</ul>

These are a few of the small, but frustration-inducing, things I've noticed enough to warrant a mention. For a broad overview of PHP best practices, check out <a href="http://www.phptherightway.com/">PHP: The Right Way</a>. While it's not a Bible of PHP, which must be followed to the letter, it does offer a good template for readable, functional PHP.

<h3>Mind your Development Environment</h3>

Many complaints about PHP's function argument ordering, documentation, and debugging can be easily solved by using a good IDE or editor. All the most popular editors (Vim, Emacs, Sublime, TextMate, BBEdit, et all), and most popular IDEs (Eclipse, NetBeans, Aptana, Coda, Xcode, Visual Studio, PHPStorm) have support (either built-in or via plugins) for:

<ul>
<li>Syntax Highlighting</li>
<li>Code Completion</li>
<li>Static Analysis (yes, <a href="/blogs/jeff-geerling/ci-deployments-code-analysis-drupal-php">this is possible</a> with PHP)</li>
<li>Refactoring</li>
<li>Debugging (check out <a href="http://xdebug.org/">Xdebug</a>)</li>
</ul>

<h3>Towards a better future</h3>

This post highlights some of the most basic elements of PHP development that are common stumbling blocks. I didn't discuss old language inconsistencies and php.net user-submitted comment deficiencies, because, frankly, I don't encounter these in my day-to-day development—nor should you.

PHP has tried-and-true modern language features like <a href="http://www.php.net/manual/en/functions.anonymous.php">anonymous functions/closures</a>, <a href="http://www.php.net/manual/en/language.generators.overview.php">generators</a>, <a href="http://www.php.net/manual/en/language.namespaces.php">namespaces</a>, <a href="http://www.php.net/manual/en/language.exceptions.php">exceptions</a>, and <a href="http://www.php.net/manual/en/language.oop5.php">classes and objects</a>. <a href="https://getcomposer.org/">Composer</a> offers simple package/dependency management, and PHP is well-supported by just about every cloud provider and management system on the planet.

Don't be ashamed to be developing in PHP—but don't be too proud, either. The best developers use the best tool (note that I didn't say <em>right</em> tool) for the job, and sometimes, it just so happens that PHP fits that role. It might not be the most elegant language, but it's pretty good in almost every way that counts for web development.

I'm excited about PHP's future prospects, especially as more of the platforms built on PHP adopt modern programming paradigms (look at <a href="http://buytaert.net/why-the-big-architectural-changes-in-drupal-8">Drupal 8</a> for a great example). Projects that are involved with <a href="http://www.php-fig.org/">PHP-FIG</a> are helping drive general PHP development forward into this new era of web development.

There are some bumps in the road, for sure. PHP's core development group wrestles with the RFC process (and with each other!), and some view Facebook's efforts (like Hack and the HipHop VM) as a potentially upsetting fork of the language. But PHP's situation is much like other major languages used for web development. Python is having growing pains in adoption of Python 3 (reminds me very much of <a href="http://pear.php.net/gophp5.php">GoPHP5</a>), Ruby is suffering from its popularity (it's no longer the hipster language of the web, and like PHP, more 'average joe' programmers are breaking down it's oft-portrayed image as a flawless web development language—you can port bad code to <em>any</em> language), and Java still suffers from more complicated tooling and less approachability (besides the stigma of being 'enterprise-y' and hard to deploy).

Whatever the future holds, PHP will continue to be a relevant and important language for web development. If you follow best practices, and learn modern PHP, your experience programming in PHP will be more positive than negative. At the very least, you might stop upvoting every comment that mentions <a href="http://me.veekun.com/blog/2012/04/09/php-a-fractal-of-bad-design/">PHP: a fractal of bad design</a>.
