---
date: '2009-05-11'
recovered_from: wayback
slug: post-531
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200905\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=531
title: Webservices and WCF- eatting one’s own dogfood
---


The official line for WCF and webservices is that they are for interop especially between organizations and between different technology stacks, e.g. Java and .NET or COBOL and .NET.


**Who wants to build an open API when no one has asked for it? Who will ask for an open API if one doesn’t already exist?  For WCF/webservices to happen at all you have to image a use case for these that would be useful now.**


**Three reason why you’d wan’t to consume your own webservices:**


**Javascript to .NET interop**.  This allows for Aptana driven development against a C\# application.  This becomes especially compelling if you have webservices returning JSON,  and RSS, because the client will be simpler to write.


**Testability**.  The webservices API is more testable than the webforms that do much the same thing.


**Data access**.  XML is a datatype too.  It can be handy to have one more dataformat in the data monkey’s toolbox.


**Compatibility with future versions.** WCF especially\- The web service as a programming model might be low performance, but it is remarkably resiliant to changes in implementation.  So much thought has gone into defining an interface that works with everyone, it will even work with that foreign application called “Your Application, version next”