---
date: '2008-10-16'
recovered_from: wayback
slug: post-468
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200810\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=468
title: Whitelisting and Blacklisting by user-agent headers
---


Some web security strategies depend on co\-operation from the browser. For example, you can ask the browser to not cache or to only send cookies back via ssl, but if the browser doesn’t want to, it won’t.


You can also ask a browser to identify itself (and restrict your application to browsers that are known to be secure browsers), but if it wants to lie, there is nothing to stop it.


On an intranet, you could assume that users will only use the installed software on the computer, but browsers don’t require admin rights to install. On the internet, obviously remote users can use anything they want. Assuming you can prevent all potential users from using an unexpected browser is unrealistic.


What can be done, and this will provide some protection against some scenarios, is to parse the user agent string\- if the browser claims to be an insecure, late model browser, then assume it is being honest and deny it access. After all, why would a hacker lie and claim that they are an insecure browser? This way, unsophisticated users who wouldn’t be expected to know how to hack a user\-agent header would be prevented from browsing with a browser that doesn’t honor do\-not\-cache and use\-ssl\-cookies directives. 


Black listing is a lot of work, as the set of possible user\-agent strings is infinite.A fancy solution might be to provide limited or no access to unrecognized user\-agents until an administrator approves each one.


Protection against the completely custom browser is more difficult. If you use a white list of browsers, you will discover that even MSIE can have a lot of user\-agent strings and predicting future user\-agent strings isn’t realistic. Letting your application break because MSIE’s user\-agent changed is not a good solution.


Presumably your secure application has proper authentication and authorization so any new browsers you see will have a user associated with it, so you could decide which users have to the right to use browser on the black list or off the white list. Or you could include this in the authorization, i.e. this page is can be loaded only by a browser on the white list (restrictive), while those pages can only be loaded by a browser not on the black list (less restrictive).


Custom browsers usually are written by sophisticated software developers with the aim of doing automated mischief on a large number of computers. Another good rule would be to allow a new user\-agent if the user can pass a captcha test.


If an ambitious developer implemented all of these features, the application would still be subject to attack from a manual, custom browser. For that, you will have to rely on proper authentication, authorization and auditing to save you.