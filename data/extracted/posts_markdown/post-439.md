---
date: '2008-09-11'
recovered_from: wayback
slug: post-439
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200809\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=439
title: Securing a public folder in ASP.NET 1.1 (Maybe 2.0 too)
---


Lets say you have a public folder, where users can upload files.  To ensure users can’t upload and execute any code that the .NET compiler can interpret and run, add a we.config file that has errors in it. That will stop any code in that folder from running, malicious or otherwise.