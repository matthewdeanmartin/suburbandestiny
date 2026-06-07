---
date: '2008-04-18'
recovered_from: wayback
slug: post-345
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200804\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=345
title: Strange but true
---


You can assign random build numbers to your .NET assemblies


From [MSDN](http://msdn2.microsoft.com/en-us/library/system.reflection.assemblyversionattribute.aspx):


“You can specify all the values or you can accept the default build number, revision number, or both by using an asterisk (\*). For example, \[assembly:AssemblyVersion("2\.3\.25\.1")] indicates 2 as the major version, 3 as the minor version, 25 as the build number, and 1 as the revision number. A version number such as \[assembly:AssemblyVersion("1\.2\.\*")] specifies 1 as the major version, 2 as the minor version, and accepts the default build and revision numbers. A version number such as \[assembly:AssemblyVersion("1\.2\.15\.\*")] specifies 1 as the major version, 2 as the minor version, 15 as the build number, and accepts the default revision number. **The default build number increments daily**. **The default revision number is random.**”


This must be some  sort of unscientific way of avoiding name clashes?  How many people are going to look at these two versions and not realize that either one might be the chronologically earlier version?


* 1\.2\.15\.1235
* 1\.2\.15\.5233


Incrementing build numbers daily likewise is a strange decision.  So if you compile at 9AM, you get the same build version as if you compile at 2PM, but a different build version the compile next day at 9AM.