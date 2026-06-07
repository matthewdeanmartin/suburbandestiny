---
date: '2007-08-24'
recovered_from: wayback
slug: post-271
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200708\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=271
title: The file ‘/foo.aspx’ has not been pre-compiled, and cannot be requested.
---


If you put a compiled ASP.NET application into a sub folder of a virtual directory/application, you get this error accessing the child application. Compiled apps don’t like to be in a hierarchy. [Create an IIS ‘application’](http://www.affiliatewiz.com/support/appstartpoint.asp) for the compiled website.



If you are missing a reference, you might get this error message. Think back to what the most recent DLLs that were added to your project. GAC’d dlls are a likely candidate because deployment projects and msi installer projects assume the destination has the same GAC’d file as the development machine.