---
date: '2008-11-30'
recovered_from: wayback
slug: post-483
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200811\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=483
title: Telerik Ajax and the Mystery of the missing postback
---


Telerik Ajax on my machine on my project was acting as if on MSIE, but not firefox, as if postbacks were GET’s. Page.IsPostback evaluated to false.


But! If I changed from http://localhost/mysite/MyPageWithTelerikDropDown.aspx


to http://machinename/…etc


Then post backs behaved like postbacks.


Go figure.