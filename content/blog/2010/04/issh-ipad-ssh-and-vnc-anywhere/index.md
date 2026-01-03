---
nid: 1873
title: "iSSH on the iPad - SSH and VNC from Anywhere"
slug: "issh-ipad-ssh-and-vnc-anywhere"
date: 2010-04-05T06:28:37+00:00
drupal:
  nid: 1873
  path: /blog/2010/issh-ipad-ssh-and-vnc-anywhere
  body_format: full_html
  redirects: []
tags:
  - ipad
  - remote access
  - ssh
  - vnc
---

<p>
	[<strong>UPDATED</strong>: The developer of iSSH emailed me this morning with a couple of tidbits that will be useful for any early iSSH adopters on the iPad - see my updated notes in bold.]</p>
<p>
	One app I haven&#39;t had a lot of time to work with (yet) is iSSH on the iPad. I tried the iPhone version, but the tiny iPhone screen simply couldn&#39;t keep up with a productive SSH or VNC session.</p>
<p>
	The iPad changes the game, though; I can actually log in via SSH, do some real work, then go back to doing whatever I was doing on the iPad. Since the iSSH developers didn&#39;t have a ton of time to work on an actual iPad, there are some pretty annoying bugs right now&mdash;but these bugs will be fixed soon. Some of the bugs:</p>
<ul>
	<li>
		It is very hard to set up an RSA/DSA key pairing from the iPad to your server(s). You will probably have to type in your password on each connection for now :(</li>
	<li>
		The interface is a little iffy, and jittery; feels almost like working on a PC.</li>
	<li>
		Sometimes, the command prompt gets hidden behind the keyboard (even when the keyboard is in transparent mode). (<strong>UPDATE from developer</strong>:&nbsp;<em>That missing command prompt is due to a rotation bug not found in the simulator. It&#39;s already fixed and ready as part of this week&#39;s update. A workaround for the moment is to rotate the iPad to portrait and back and the issue will resolve itself.</em>)</li>
</ul>
<p>
	But the upside? See the picture below:</p>
<p class="rtecenter">
	{{< figure src="./iterm-ipad.jpg" alt="iTerm on iPad" width="600" height="450" class="blog-image" >}}<br />
	SSH on the iPad. Glorious.</p>
<p>
	In my <a href="/reviews/2010/review-apples-ipad-32gb-tested">review of the iPad</a>, I mention that it&#39;s pretty easy to type on the iPad. However, there are some characters that take too long to type in iSSH (namely, the forward slash (/), the tilde (~), and arrow keys). Hopefully there will be a nice shortcut bar or something similar to allow me to set up keystroke shortcuts. I can dream, can&#39;t I? (<strong>UPDATE from developer</strong>:&nbsp;one can use the custom key pie menu today to do that. See here for going about setting it up: <a href="http://www.zingersoft.com/support_g_2.html">http://www.zingersoft.com/support_g_2.html</a>).</p>
<p>
	I haven&#39;t tried VNC yet (apparently you can even create a tunnel through SSH and VNC to a remote computer), but I will probably try this once or twice as a possible alternative to LogMeIn (I don&#39;t want to pay for their iPad app).</p>
