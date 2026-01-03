---
nid: 2303
title: "Integrate a Webform (3.x) with PayPal"
slug: "integrate-webform-3x-paypal"
date: 2011-01-31T16:10:25+00:00
drupal:
  nid: 2303
  path: /blogs/jeff-geerling/integrate-webform-3x-paypal
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - payment
  - paypal
  - php
  - webform
---

<p>For quite some time, I've wanted to integrate a particular webform with PayPal, since many nonprofits I help use that payment service. With older versions of PayPal, one could add some PHP code into a webform on the site to do this, but it was (a) hackish, and (b) a much less maintainable and secure way of accomplishing the goal I was trying to achieve. So I never did it.</p>

<p>However, after reading <a href="http://www.drupalcoder.com/story/678-additional-processing-in-drupals-webform-3-module">Additional processing in Drupal's Webform 3 module</a> (from Drupal Coder), I found that Webform 3 has a hook that runs just after webform has saved a form's data to the database, but before the webform returns the user to a predefined redirected page. <code>hook_webform_submission_insert()</code> is the perfect time to hook into Webform's process and send a user to PayPal, along with that user's data.</p><!--break-->

<p>PayPal has relatively robust documentation of it's Website Payments Standard API, and all we need to do is send an HTTP/HTTPS request to PayPal with certain parameters, defining to whom the payment should be sent, what the payment amount is, and some other options (including values sent in via our Webform).</p>

<p>In my site's custom module (I'm running Drupal 7 - code might need minor adaptations for 6.x), I added two simple hooks, shown below with comments to help define what's going on:</p>

```
<?php
/**
 * Implements hook_webform_submission_insert().
 */
function custom_webform_submission_insert($node, $submission) {
  if ($node->nid == 12) {

    // Get mapping of form submission data using private function (see below).
    // Using this, we can use webform field names (like 'first_name') instead
    // of vague mappings like $submission->data['3']['value'][0].
    $mapping = _custom_webform_component_mapping($node);

    /**
     * Set up form to post to PayPal
     * 
     * Preliminary notes:
     *  - PayPal expects a state code in 2-digit caps (no full names)
     *  - Need to break phone number into three strings... [area] [3-digits] [4-digits]
     *  - https://www.paypal.com/cgi-bin/webscr?cmd=_pdn_xclick_prepopulate_outside
     */
    $paypal = array();
    $paypal['cmd'] = '_donations'; // Varies depending on type of payment sent via PayPal
    $paypal['business'] = 'name@example.com';  // PayPal account email
    $paypal['bn'] = 'GM_Donate_WPS_US'; // See PayPal docs on proper formatting - not required, though
    $paypal['page_style'] = 'primary'; // Set this in PayPal prefs, then change here (default = paypal)
    $paypal['amount'] = $submission->data[$mapping['amount']]['value'][0];
    $paypal['item_name'] = 'Description of the type of donation, payment, etc. goes here.';
    $paypal['no_shipping'] = '1'; // Don't prompt user for shipping address
    $paypal['no_note'] = '1'; // Don't prompt user for extra information (note)
    $paypal['tax'] = '0'; // No tax for this payment
    $paypal['rm'] = '1'; // Return method - 1 = browser redirected to return URL by GET method w/o variables
    $paypal['return'] = 'http://example.com/thank-you'; // Page to which user is returned
    $paypal['first_name'] = $submission->data[$mapping['first_name']]['value'][0];
    $paypal['last_name'] = $submission->data[$mapping['last_name']]['value'][0];
    $paypal['email'] = $submission->data[$mapping['email']]['value'][0];
    $paypal['address1'] = $submission->data[$mapping['address']]['value'][0];
    $paypal['address2'] = $submission->data[$mapping['address_2']]['value'][0];
    $paypal['city'] = $submission->data[$mapping['city']]['value'][0];
    $paypal['state'] = $submission->data[$mapping['state']]['value'][0];
    $paypal['zip'] = $submission->data[$mapping['zip']]['value'][0];
    $paypal['country'] = 'US';

    // Build the URL/query for PayPal payment form.
    $query = http_build_query($paypal, '', '&');
    $url = 'https://www.paypal.com/cgi-bin/webscr?' . $query;

    // Redirect user to PayPal...
    drupal_goto($url);
  }
}

/**
 * Function to convert webform submissions into a nicely-mapped array.
 *
 * @see http://www.drupalcoder.com/story/678-additional-processing-in-drupals-webform-3-module
 */
function _custom_webform_component_mapping($node) {
  $mapping = array();
  $components = $node->webform['components'];
  foreach ($components as $i => $component) {
    $key = $component['form_key'];
    $mapping[$key] = $i;
  }
  return $mapping;
}
?>
```

<p>The only thing I was not able to get working correctly was the phone number. Either you need to explicitly request each of the three parts of a user's phone number (area code, exchange, and number), or you need to parse the user-entered value into those three parts. One way makes it harder on the user—the other way on you!</p>

<p>Hopefully this will help many people who don't want to simply have the 'Donate' button (like political campaigners, who need more information) embedded on their sites, and also don't want to deal with the major overhead of having a whole shopping cart system on their site for one donation/payment form.</p>

<p>(The million dollar question is: does anyone want to take the time to make this functionality work in an addon module? The <a href="http://drupal.org/project/webform_payments">Webform payments</a> module hasn't been updated since about a year ago... There's also <a href="http://drupal.org/project/webform_pay">Webform Pay</a>, which has some traction, but doesn't support as many payment methods as I'd like—yet.).</p>
