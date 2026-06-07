---
date: '2012-09-21'
recovered_from: wayback
slug: post-686
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201209\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=686
title: Compiler Error 128
---


Many things cause compiler error 128\. [Ref, here](http://www.hanselman.com/blog/ASPNETCompilerError128AndMicrosoftSupport.aspx).


Sometimes reregistering aspnet with iis works.


In my case, I had attached a console to a running asp.net app. Then I uploaded the correct release build over the top of that (the release build doesn’t attach a console) and then I got compiler error 128\. It cleared up on iisreset. If in doubt, pull the power out.