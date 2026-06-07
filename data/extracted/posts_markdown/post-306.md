---
date: '2007-12-05'
recovered_from: wayback
slug: post-306
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200712\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=306
title: MCTS Exam Review Books
---


Oh my god, these aren’t books, they are unedited blogs in the form of books.  When will IT publishers learn that consistently formatted does not mean edited?


Clearly, the only way to get value out of this study guide is to edit it.  If you can find all the mistakes, errors, clunky explanations, spelling errors, sample code bugs and repair them, then you will pass the test and become a master copyeditor to boot.


Web Based Client Development


Chapter 1, Lesson 1\- Book states the maximum URL length for MSIE and IIS is 1024\.  [This doesn’t appear to be a consensus](http://www.boutell.com/newfaq/misc/urllength.html) and certainly doesn’t reflect the capabilities of IIS or non MSIE browsers.


Book states POST “removes the size constraint on data”, which is not true for ASP.NET ([default value for web.config 4096KB](http://support.microsoft.com/default.aspx?scid=kb;EN-US;295626), modifiable upward to 4GB) and for IIS the maximum if 4GB.


Book states “Although its name comes from the POST verb, it is possible to perform a PostBack using the GET method…”  The book doesn’t explain how this happens.  I think if a book is going to say up is down and black is white and ignorance is strength, then it needs to explain why.  In this case, if you set on the form tag, method\=”GET” ASP.NET will switch to putting the event validation and viewstate into the querystring. Page.IsPostBack will be true, Request.RequestType will be GET and Request.QueryString will contain two additional value pairs.


Book recommends using Microsoft Network Monitor to trace HTTP traffic.  Why not use an electron microscope?  Instead use a HTTP specific traffic tracing tool, like [Fiddler](http://www.fiddlertool.com/fiddler/), which MS itself recommends.  


Chapter 2, Lesson 2\-


To be continued