---
nid: 3276
title: "My daughter's school took over my personal Microsoft account"
slug: "my-daughters-school-took-over-my-personal-microsoft-account"
date: 2023-02-25T04:06:53+00:00
drupal:
  nid: 3276
  path: /blog/2023/my-daughters-school-took-over-my-personal-microsoft-account
  body_format: markdown
  redirects: []
tags:
  - accounts
  - active directory
  - azure
  - microsoft
  - office 365
  - schools
---

This weekend I wanted to create a new App in Azure so I could help a local nonprofit automate one of their donor relations processes via email through Office 365.

So I tried [registering an app](https://learn.microsoft.com/en-us/graph/auth-v2-user?context=graph%2Fapi%2F1.0&amp;view=graph-rest-1.0) by visiting the App Registration Portal. I signed in to my personal Microsoft account, clicked 'New registration', then was greeted by this page:

{{< figure src="./azure-you-do-not-have-access.png" alt="Azure you do not have access" width="700" height="448" class="insert-image" >}}

I thought that was a bit strange, since I shouldn't have any restrictions... but then I noticed it listed `[redacted] School` as the reason I couldn't do this.

Then I noticed under my username / account info, it had my personal email, but it showed me as being a member of '[redacted] School'.

I guess somehow they threw me into their system, so surely there's a way for me to sign out of that back into my _personal_ account, right?

Wrong.

First I tried going to the [My Account](https://myaccount.microsoft.com/) portal, as suggested on the support page [Manage organizations for a work or school account in the My Account portal](https://support.microsoft.com/en-us/account-billing/manage-organizations-for-a-work-or-school-account-in-the-my-account-portal-a9b65a70-fec5-4a1a-8e00-09f99ebdea17). I entered my username and got:

{{< figure src="./microsoft-signin-account-portal.png" alt="Microsoft Account Portal Not allowing Personal account sign in" width="500" height="375" class="insert-image" >}}

Okay... well this is weird. And yes, this is my _personal_ account. It was created when I transitioned my Xbox LIVE account to a Microsoft account on 2014-03-07 (the LIVE account was created back in 2006, and neither it nor my Microsoft account were ever joined to any other domains).

So I clicked my username and saw it is listing my daughter's school under my account email:

{{< figure src="./microsoft-account-switch-directory-profile.png" alt="Microsoft Account switch profile directory" width="400" height="297" class="insert-image" >}}

I saw a handy 'Switch directory' link so I clicked that.

Unfortunately, there's only one directory listed... "[redacted] School." So I can't change directories.

Searching around, I also found the URL [https://account.activedirectory.windowsazure.com/](https://account.activedirectory.windowsazure.com/), so I went there and tried logging in... but got:

{{< figure src="./access-denied-azure-personal-account.png" alt="Access Denied Azure personal account" width="700" height="213" class="insert-image" >}}

So at this point I didn't know what else to do. It's a weekend, so I probably won't get ahold of the school's IT person who could help on their end.

Somehow, the school 'adopted' my personal Microsoft account, and now I can't do anything in Azure with it. At least my Xbox Live account and Windows licenses are still working—but could the school revoke that access too?

I have no clue how I got in this pickle. I certainly don't remember receiving an email saying:

> Dear Jeff Geerling, are you okay with **[redacted] School** taking over control of your Microsoft account and not allowing you to do anything in Azure anymore?

So how did it happen? And is there any way I'll be able to regain control of my own account again?

And the bigger question: does this mean it's possible for any org on Office 365 to forcibly adopt users on the platform who log in with their personal accounts?

I'll update this post if I can figure out a way to regain control of my personal Microsoft account again. I also [posted about it on Twitter](https://twitter.com/geerlingguy/status/1629316760586399745), and there are others who mention similar stories of woe.

Hopefully `[redacted] School` can help here. But they shouldn't be able to do what they did in the first place—Microsoft Azure's insane Active Directory behavior isn't their fault!

---

Update: Following [@NeilTheMann's advice](https://twitter.com/NeilTheMann/status/1629347597465862150) on Twitter, I went to [https://myapps.microsoft.com](https://myapps.microsoft.com) and logged in _there_. Then I clicked on my 'JG' account info, and at the bottom of that profile pane, it had a link to 'Manage organizations'. On _that_ page, I see:

{{< figure src="./organizations-list-microsoft-account-myapps.png" alt="Microsoft Account MyAccount Organizations List" width="700" height="228" class="insert-image" >}}

I clicked 'Leave', then got this nice scary warning page:

{{< figure src="./leave-organization-azure-warning-data-loss.png" alt="Microsoft MyAccount Leave Organization data deletion warning" width="700" height="302" class="insert-image" >}}

I'm _assuming_ "deletion of your data" only includes any information that might be associated with the school... hopefully not the rest of my Microsoft account!

Now if I visit 'Manage organizations' I get an error:

{{< figure src="./error-my-organizations-microsoft-account.png" alt="My Organizations error on Microsoft Account" width="500" height="83" class="insert-image" >}}

...and now if I try doing anything in Azure I get this warning:

{{< figure src="./limited-or-no-access-azure-microsoft.png" alt="Limited or No Access Microsoft Azure" width="600" height="356" class="insert-image" >}}

And my account now shows "RESTRICTED TENANT":

{{< figure src="./restricted-tenant-microsoft-account.png" alt="Microsoft Account Azure Restricted Tenant" width="394" height="324" class="insert-image" >}}

So I think I just screwed myself out of even minimal access to Microsoft Azure.

🤷‍♂️

This experience certainly doesn't recommend Microsoft Azure.

---

Update 2: It gets better. Now I can't even log into myapps.microsoft.com:

{{< figure src="./microsoft-account-does-not-exist-in-tenant.png" alt="Microsoft Account does not exist in tenant" width="350" height="358" class="insert-image" >}}

However... I am now able to Register an Application in my personal account—though every page on Azure gives me this big ugly error message:

{{< figure src="./authentication-issues-microsoft-azure-error-message.png" alt="Microsoft Azure authentication issues" width="327" height="398" class="insert-image" >}}

The rabbit hole goes deeper still...
