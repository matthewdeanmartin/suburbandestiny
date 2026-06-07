---
date: '2008-08-12'
recovered_from: wayback
slug: post-397
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200808\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=397
title: .NET Attributes to use more often
---


My theme here are general purpose programming attributes, ones that you might use for any class.


(first seen [here](http://www.acorns.com.au/blog/?p=128))


**DebuggerStepThroughAttribute, \[DebuggerStepThrough()]**  

You can still set breaks here, but normally the debugger will fly right over it. Use this when you find yourself running through the same boiler plate code over \& over again, especially if the code is machine generated, or otherwise not of interest.


**DebuggerNonUserCodeAttrbute.\[DebuggerNonUserCode()]**  

No step through, no breaking, even if you have a breakpoint.


**\[DebuggerDisplay(**