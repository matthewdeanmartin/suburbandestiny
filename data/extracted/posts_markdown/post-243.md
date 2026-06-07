---
date: '2007-06-27'
recovered_from: wayback
slug: post-243
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200706\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=243
title: GRRRR! Cardspace. What a useless steaming pile…
---


[![NOINFOCARD](https://suburbandestiny.com/tech/wp-content/uploads/2007/06/noinfocard-thumb.png)](https://suburbandestiny.com/tech/wp-content/uploads/2007/06/noinfocard.png)Ok. Cardspace/Infocard is like OpenId.  Password\-less access to websites (or password\-fewer access).


**BUT** 


1\. [You must use SSL](http://www.leastprivilege.com/CardSpaceAndDecryptingTokens.aspx).  Even if you just want to secure your application against your clueless neighbor.  That is a minimum of $40\.


2\. [You must decrypt the response on an account with NTFS access to the private key](http://developers.de/blogs/damir_dobric/archive/2007/06/19/keyset-not-found-error.aspx).  The NT Network Service account is not likely to have read access to the private key on a hosted account.  Good luck explain how and getting co\-operation from your hosting provider.


3\. [Decryption must be done under FULL TRUST](http://www.leastprivilege.com/DecryptingCardSpaceTokensInPartialTrust.aspx).  Many hosted accounts only let you run in medium trust and don’t let you create COM\+ dlls, put stuff in the GAC, etc.


\[[Items 2 and 3 might not even be a good idea](http://forums.microsoft.com/MSDN/ShowPost.aspx?PostID=1307759&SiteID=1).  If the world at large manages to use your web application to maliciously download your SSL cert, I suppose they could do something evil, like pretend they are you]


4\. To get rid of the “[the website isn’t secure for banking or ecommerce](http://www.aspnetpro.com/opinion/2007/06/asp200706jg_o/asp200706jg_o.asp)” you have to spend $1000 on an EV SLL cert.  Oh, sure, pocket change.


5\. And who is issuing managed cards? I can get an SSL based cert from Thawte that says I am the person that controls my email account, but I can’t find anyone who issues managed infocards anywhere.


I’ve about realize that I–a computer profession and programmer, will not be able to implement InfoCard/Cardspace in any form, not for my blog, not for my hobby website, nothing.  Either one has $1040 and ones own entire server or nothing.


If only the top 10 biggest websites can overcome the hurdles posed by infocard, what we are going to see is 5 websites accept infocard and everyone else (mom \& pop websites) continue to use passwords and user ID’s. InfoCard will have a minimal impact on how authentication is done.


This is going to drive small websites into using OpenId.  Consumer will rapidly gain a few dozen OpenId cards.  The rising ubiquity of OpenId–which doesn’t try to be a waterproof authentication method–will take over the world, relegating InfoCard to “that way you logon to Live.com services”.


Come on Microsoft, when are we going to be able to run CardSpace/Info card in “real world” mode?


\[Thanks to [Self\-issued.info](http://self-issued.info/?p=17) for the logo]  \[Actually, I take that back, it is a Microsoft trademark. The [purple box is has a substantial amount of IP self legislation that goes with it](http://self-issued.info/infocard_icon/Information%20Card%20Icon%20Guidelines.pdf).  According to MS's lawyers, I am currently in violation of usage guide lines for the icon.  Let's see how Microsoft silences critics of InfoCard.]