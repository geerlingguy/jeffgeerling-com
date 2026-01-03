---
nid: 2356
title: "Sending emails to multiple receipients with Amazon SES"
slug: "sending-emails-multiple"
date: 2012-01-02T21:50:53+00:00
drupal:
  nid: 2356
  path: /blogs/jeff-geerling/sending-emails-multiple
  body_format: full_html
  redirects: []
tags:
  - amazon
  - api
  - bulk
  - email
  - php
  - ses
  - snippets
---

After reading through a ton of documentation posts and forum topics for <a href="http://aws.amazon.com/ses/">Amazon SES</a> about this issue, I finally found <a href="https://forums.aws.amazon.com/thread.jspa?threadID=61300#jive-message-272933">this post about the string list format</a> that helped me be able to send an email with Amazon SES's sendmail API to multiple recipients.

Every way I tried getting this working, I was receiving errors like <em>InvalidParameter</em> for the sender, <em>Unexpected list element termination</em> for the error code, etc.

Normally, when sending email, you can either pass a single address or multiple addresses as a string, and you'll be fine:

<ul>
<li>Single Address: <code>John Doe <johndoe@example.com></code></li>
<li>Multiple Addresses: <code>John Doe <johndoe@example.com>, Jane Doe <janedoe@example.com></code></li>
</ul>

...just add in a comma between each address, and you're golden. Amazon's SES API documentation says you can pass a 'string/array' for the 'ToAddresses' parameter, and those addresses will be sent an email. They're kinda lacking in implementation details, though, and it took some wrangling to find out that, using Amazon's PHP API class, I had to prepare my addresses like so:

For normal (single) email addresses, I could just go:

```
<?php
  $destination = CFComplexType::map(array(
    'ToAddresses' => 'John Doe <johndoe@example.com>',
  ));
?>
```

(The $destination parameter would be passed into $ses->send_mail).

However, for multiple email addresses, you must pass in an array, with the following structure, and pass that to the CFComplexType object:

```
<?php
  $to = array(
    'member' => array(
      0 => 'John Doe <johndoe@example.com>',
      1 => 'Jane Doe <janedoe@example.com>',
    ),
  );

  $destination = CFComplexType::map(array(
    'ToAddresses' => $to,
  ));
?>
```

I don't know why Amazon can't just accept a normal string with commas designating recipients, as that would make life easier, imo, but oh well.
