---
date: '2012-09-11'
recovered_from: wayback
slug: post-672
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201209\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=672
title: Production Trace
---


Assume you work in a large organization, you write code, you really would like to see some diagnostic trace from your app in Test, Staging or Production, but a server admin owns all of them. You can’t have the event logs, remote desktop access, or ask that the web.config be edited to add or a remove a System.Diagnostics section. Just imagine.


Production trace needs to be:  

\- high performing, if it slows down the app, which may already be under load, not good.  

\- secure, since trace exposes internals, it should have some authorization restrictions  

\- not require change of code or config files, because large organizations often have paralyzing change management processes  

\- support a variety of listeners that will meet the requirements above (and if those listeners are write only, then a reader will need to be written)


System.Diagnostics \-File\-  

\- Perf\- Not very performant, will likely have contention for the file.


System.Diagnostics\-Console, DebugString, Windows Event Log  

\- You can’t see it. End of story.


ASP.NET Trace.axd and In Page  

\- Perf\- not so good.  

\- Security\- it’s well known, so security teams often disable it  

\- Config\- Can sort of enable on a by page/by user basis if you use a master page or base page to check rights and maybe a query string.


Custom Session Listener  

Write to session.  

\- Okay for single user trace. Need a page to dump the results.  

\- Perf probably okay, could hog memory.  

\- Security, pretty good, by default you can only see your own stuff.


Custom Cache Listener  

\- Write trace to cache  

\- Will have locking problems  

\- Won’t hog memory because of cache eviction  

\- Cache eviction could remove trace too fast.


HttpContext.Items listener \+Base page to dump contents at end of request  

\- Only shows one page of trace at a time  

\- Probably high perf.  

\- Won’t show other users