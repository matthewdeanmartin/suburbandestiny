---
date: '2007-05-29'
recovered_from: wayback
slug: post-217
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200705\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=217
title: Using Web Services from an ASP.NET 2.0 Application
---


Right click, add web service. Enter URL of web service. For example, http://localhost



VS2005 creates an App\_WebReference folder with several XML files. Remember to right click and update reference next time you modify the webservice at localhost.



Web.config now has a new app setting with the URL. Personally, I’d like the application to use this URL instead of the ones found embedded in the XML files in App\_WebReference.



To set the URLBehavior property, as far as I can tell, you need to be using a Web **Application** Project, not a Web **Site** Project. Conversion is not a light undertaking and the developer experience changes as you switch from one to the other.



Fortunately, it seems that the default ULRBehavior is dynamic for Web Site Projects.