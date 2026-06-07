---
date: '2006-02-24'
recovered_from: wayback
slug: post-119
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200602\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=119
title: ASP.NET Lessons Learned
---


You do not need an MSI installer to deploy a .NET dll.  Just copy the file.


XCopy can wreck share permissions on a UNC share. I’m not sure why, just know it’s possible.


When shadow copying a .NET website from VSS to a test server, .dll files are excluded and the /bin folder doesn’t get checked in to VSS.  I’ve heard this is ‘a good thing’ although I don’t know why.  Right now I have to manually copy the dll files to the shadow copy.


One quirk about .NET 1\.1 is that all pages are compiled into a single DLL.  This means that if one page needs to be deployed, they all need to be deployed.  Alternatively you can use the src page directive, which replaces the inherits directive. This is supposed to force on request compiling.  However, when I try it, all I get are ‘can’t find reference’ errors, even after adding in ‘imports’ commands.  Plus, VS2003 is said to ‘not use’ the src directive and needs to have the imports directive to work, and the ASP interpretor doesn’t use the inherits command, it just uses the already compiled dll.