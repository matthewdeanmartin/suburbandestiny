---
date: '2008-09-12'
recovered_from: wayback
slug: post-443
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200809\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=443
title: Unit Test Checklist for .NET business objects
---


1 test per method  

1 assertion per method (unless it is testing something trivial, like null on return object)  

Always check for null on return object unless null means something.  

Always add ExpectedException test for System.ArguementNullException, unless null means something or if it is an optional parameter. (NullReferenceException just isn’t as useful because you see it so often.)  

Repeat tests for each constructor.