---
date: '2008-01-22'
recovered_from: wayback
slug: post-317
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200801\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=317
title: 'Review: Pervasive Data Integration'
---


I was about to review this product on the basis of their customer service, but fortunately I got a generous 48 hour trial license.  Ironic how Microsoft trusts developers to play with the full feature set of SQL Enterprise Edition (a product that costs upwards of $35,000\) through either a three month trial or the Developer Edition.  [Pervasive Data Integration costs between $10,000 and $20,000](http://www.intelligententerprise.com/showArticle.jhtml?articleID=51201544) and you don’t get a database to go with it.  [Rumor exist about a 14 day trial license](http://labastida.com/get-free-software/).


The tool supports a remarkably long list of data sources. If you happen to be in an organization where you have to put up with 100\+ native data formats, this might be exciting.  In my professional experience, this is not a good or typical integration pattern.  More typical is that organizations dump their native data formats to various text formats before exchanging with other organziations.  Native and binary formats are too brittle (subject to breaking over time due to technological or other changes).  Text, especially fixed width layouts, was the universal data exchange format before there was XML or the like.  That said, native data exchange tend to have more meta\-data in them, so there is less problem of data corruption as the data goes from native to text durring inter\-organizational exchanges.


Also, FYI, if you do have to deal with a native data format, you might be better off using ODBC, JDCBC, ADO, OleDB or the like.  Interacting with native data formats is for applications where it is important to access specific features of the source data platform (like running PL\-SQL, access to indexes), or performance reasons.  If you have extremely high performance requirements for ETL, then ironically, you will probably end up working a lot with text. 


The GUI is Java. So far I’ve only gotten a few JVM error messages.  After more than a decade, Java apps still don’t deploy very smoothly, if I had a nickle for everytime I got a JVM version error, I’d be rich.


The Data Integration uses a system of workspaces, repositories and thingies.  In practice, this means the source code files are stored in a xml database layered over the file system.  I got numerous error messages attempting to save files.  Apparently it is not good enough to save a file, it needs to go into this xml filesystem layer.


The Integration engine itself is without a UI at all.  The various designers have a UI, but feedback is mostly sent to log files.  The choice to use error logs instead of message boxes for the design time experience is bemusing and echos what I think is one of the backwards steps MS took going from DTS classic to SSIS (that is, moving more feedback from the UI to error logs)


I haven’t figured out how the Integration Engine works yet, so it’s hard to say if it is using buffers like SSIS, individual objects like DTS or some other as of yet undiscovered pattern.


The mapping tool is not intuitive.  The message box you get on first open is a strongly worded exhortation to study the documentation, i.e. they know the mapping tool is unintelligible.  I probably will not be able to grok this before the trial license expires.


Pervasive has fallen for the [Wasabi patttern](http://www.joelonsoftware.com/items/2006/09/01b.html), that is inventing a programming language for a single application.  Pervasive uses RIFL, which is supposed to be some sort of VBScript rip off.  Why they didn’t expose a COM interface to their API and just use real VBScript, I don’t know. (Or anyone of a bunch of other scripting languages with broad industry adoption, I mean, Lua, javascript, you name it.)