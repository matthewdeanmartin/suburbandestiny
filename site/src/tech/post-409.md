---
date: '2008-08-30'
recovered_from: wayback
slug: post-409
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200808\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=409
title: Medium Trust for 1.1 ASP.NET applications
---



Medium trust apparently wasn’t given much thought for ASP.NET applications until 2\.0, when MS loosened the rules enough to enable SQLPermission and some other things.


I tried to put a 1\.1 app in medium trust…fail. 





Posted in [ASP.NET](http://tech.wakayos.com/?cat=3 "View all posts in ASP.NET") 




# [Moving back to Lunarpages from Webhost4life](http://tech.wakayos.com/?p=405 "Permalink to Moving back to Lunarpages from Webhost4life")



Posted on [August 30, 2008](http://tech.wakayos.com/?p=405 "3:46 pm")  by  [matt](http://tech.wakayos.com/?author=1 "View all posts by matt") 


Well, 4life turns out to be for about 2 or so years.


Webhost4life’s crimes:


\- Fuzzy method of measuring if you are taking your fair share of resources on a shared computer (Lunar pages at times is guilty of this too according to many online reviews, although on my linux account, I never ran into that)


\- Crappy in person service (Lunarpages may be guilty of this, but I’ve had so much less need to deal with lunarpages people, their software up to now has served all my needs)


\- Overloaded and underpowerd machines (My short Lunarpages windows account had this problem, too, but as a hobbist running small sites, that isn’t really a problem)


So why am I going back to Lunarpages?





Posted in [Matthew Martin](http://tech.wakayos.com/?cat=40 "View all posts in Matthew Martin") 




# [Automated Testing Using WebClient and HTML Agility Pack](http://tech.wakayos.com/?p=400 "Permalink to Automated Testing Using WebClient and HTML Agility Pack")



Posted on [August 24, 2008](http://tech.wakayos.com/?p=400 "6:17 am")  by  [matt](http://tech.wakayos.com/?author=1 "View all posts by matt") 


I researched options for [testing my ASP.NET website](http://mistersql.com/tech/?p=396). I decided to use Scott Hanselman’s solution where [simulate IIS using Cassini and simulate a browser using WebClient](http://www.hanselman.com/blog/PermaLink.aspx?guid=944a5284-6b8d-4366-81e8-2e241401e1b3).


**Good Points**  

It works!  

It’s free!  

Doesn’t require a massive refactoring or rewrite.


**Challenges***Cassini should be a singleton*. Unless you are testing something that is IIS dependent, you should not destroy Cassini inbetween each test or test fixture.





Posted in [.NET](http://tech.wakayos.com/?cat=2 "View all posts in .NET"), [ASP.NET](http://tech.wakayos.com/?cat=3 "View all posts in ASP.NET"), [Unit Tests](http://tech.wakayos.com/?cat=59 "View all posts in Unit Tests") 




# [.NET Attributes to use more often](http://tech.wakayos.com/?p=397 "Permalink to .NET Attributes to use more often")



Posted on [August 12, 2008](http://tech.wakayos.com/?p=397 "5:58 pm")  by  [matt](http://tech.wakayos.com/?author=1 "View all posts by matt") 


My theme here are general purpose programming attributes, ones that you might use for any class.


(first seen [here](http://www.acorns.com.au/blog/?p=128))


**DebuggerStepThroughAttribute, \[DebuggerStepThrough()]**  

You can still set breaks here, but normally the debugger will fly right over it. Use this when you find yourself running through the same boiler plate code over \& over again, especially if the code is machine generated, or otherwise not of interest.


**DebuggerNonUserCodeAttrbute.\[DebuggerNonUserCode()]**  

No step through, no breaking, even if you have a breakpoint.


**\[DebuggerDisplay(**





Posted in [.NET](http://tech.wakayos.com/?cat=2 "View all posts in .NET") 




# [Built in Exceptions you should use](http://tech.wakayos.com/?p=394 "Permalink to Built in Exceptions you should use")



Posted on [August 12, 2008](http://tech.wakayos.com/?p=394 "1:52 pm")  by  [matt](http://tech.wakayos.com/?author=1 "View all posts by matt") 


I’ve been using FxCops which looks down on “throw new Exception();”


Here are some more narrow exceptions that already exist in the framework that you should throw, hey it saves you the effort of writing a custom error class.


ArgumentNullException – Argument is null  

ArgumentException – Argument not valid  

ArgumentOutOfRangeException– arguement too big or small, or not on the list  

ArithmeticException — The root of a negative number  

InvalidOperationException \-given state,





Posted in [.NET](http://tech.wakayos.com/?cat=2 "View all posts in .NET"), [ASP.NET](http://tech.wakayos.com/?cat=3 "View all posts in ASP.NET")