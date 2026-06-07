---
date: '2008-08-24'
recovered_from: wayback
slug: post-400
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200808\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=400
title: Automated Testing Using WebClient and HTML Agility Pack
---


I researched options for [testing my ASP.NET website](http://mistersql.com/tech/?p=396). I decided to use Scott Hanselman’s solution where [simulate IIS using Cassini and simulate a browser using WebClient](http://www.hanselman.com/blog/PermaLink.aspx?guid=944a5284-6b8d-4366-81e8-2e241401e1b3).


**Good Points**  

It works!  

It’s free!  

Doesn’t require a massive refactoring or rewrite.


**Challenges***Cassini should be a singleton*. Unless you are testing something that is IIS dependent, you should not destroy Cassini inbetween each test or test fixture.