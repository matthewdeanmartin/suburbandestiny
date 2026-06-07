---
date: '2007-07-14'
recovered_from: wayback
slug: post-252
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200707\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=252
title: Google Checkout
---


Google check out is a 3rd party payment processor. It also is an authentication mechanism, albeit only at time of purchase.


**Pros.**


They are paying customers $10 at time of sign up.


You don’t have to store credit cards at your web site.


Your customers can have fewer passwords for money.


It is a REST based API– meaning your application communicates with Google via HTTP GET commands, instead of HTTP POST. You can build your app in [.net](http://www.windowsdevcenter.com/pub/a/windows/2007/01/09/build-a-net-app-for-google-checkout.html), java or PHP.


Fairly cheap as far as payment processing goes, 2 percent plus 20 cents with discounts for merchants who have big Ad Words bills.


**Cons.**


No two factor identification, like what Paypal has.


You aren’t integrated into the Google authentication infrastructure. So you will still need to create a user account in your own infrastructure, then at time of purchase, the user will be asked for a 2nd password. The only saving grace of this 2nd password is that it is one that they probably already use frequently and can use at other sites that take Google Checkout. The other way to look at it is Google checkout purchases will be treated as if they were a different customer than the one in your custom user table)


Limited Authentication Claims. The merchant doesn’t seem to necessarily get the purchasers email address and can’t correlate all from the same person without some detective work.


**Ready to try it out as a buyer?**