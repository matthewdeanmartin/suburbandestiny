---
date: '2007-05-31'
recovered_from: wayback
slug: post-218
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200705\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=218
title: 'Review: Google Gears'
---


Ok, I think I grok it now. Google Gears is a huge cookie that can store files and SQL data. It also acts as a web server should the real internet be down. The API is all JavaScript.


The only caveat I see so far is getting people to install the Google Gears plug in. For MSIE, you get warning after warning about the plug in. You also seem to need to be an administrator to install the plug in. Without a sophisticated user base or a sympathetic IT department, the ActiveX component installation could be a show stopper.


As for integration with ASP.NET, ASP.NET has never been very friendly to JavaScript developers. ASP.NET changes the element ID’s, so you will need to code generate some JavaScript with \<%\= ClientId %\> golden nuggets each time you reference a controls ID.


JavaScript counts as an out of bound call