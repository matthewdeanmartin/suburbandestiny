---
date: '2006-02-22'
recovered_from: wayback
slug: post-118
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200602\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=118
title: Debugging ASP Classic with Visual Studio 2005
---


0\) Set break points.  You don’t need to click the green arrow, that just sets up the enironment for ASP.NET and wastes your time if you’re just debugging ASP classic.


1\) If you use something other than “low isolation” you will be attaching to dllhost.  There will be several, make your best guess.  Most pages will hit break points, but not all.  

2\)  Better yet, set the isolation level to low, and restart IIS. Attach to inetinfo.exe, there will only be one.  All pages will hit break points and if you aren’t in debugging mode already, everytime you hit an error you will be prompted to start JIT debugging and to select a debugger.


3\) This is for a single user development machine scenario.  If there are other developers or live websites on the box, this is probably not adivisable.