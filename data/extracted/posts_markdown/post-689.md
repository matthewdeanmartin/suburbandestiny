---
date: '2012-10-29'
recovered_from: wayback
slug: post-689
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201210\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=689
title: Reading System.Diagnostics from the Mono sources
---


I’ve been trying to use System.Diagnostics for a while. I think I see why it failed to catch on. It thinks that developers will write a lot of code for a tertiary customer– the production server admin staff. Why do I think this? A good third of the code and complexity of the namespace is related to XML configuration. A production server admin can’t recompile the code, but sometimes in some organizations they can change configuration, say a .config, .ini or registry setting. And through these means they could turn trace on and off. But that is only if the original developers wrote a lot of trace that uses a library that can be turned on and off. System.Net and System.ServiceModel both use System.Diagnostics trace. Most other framework namespaces do not– you can use Reflector or the like to search the .NET API for instances of TraceSource– you find out that there are not a lot. People were using Console.WriteLine, Respone.Write and every other technique they learned in their first Hello World program.


Making Systems.Diagnostics Palatable to Developers  

\* Trace needs to be production safe. Not just for threading but for performance. Write should take a lambda function instead of a string. The listeners shouldn’t have a slow default that writes to a hard to see invisible listener (the DebugString API)  

\* Trace should work well in environments where a real database and possibly the filesystem isn’t available. ASP.NET makes it too hard to write to console because you have to attach the console to the WebDev Server using Win32 API calls, there isn’t a built in Application\[], Cache or Session listener, nor is there an OleDb, MS\-Acess, or Excel listener.  

\* Trace should allow for all components to be customized, Listeners, Sources, Switches, Filters, and Output Formating. The last, formatting, is barely developed in the Systems.Diagnostics API. Switches and Sources have to be completely wrapped to effectively change their behavior. And you can only have 1 Filter per listener and 1 switch per source– big restriction. Another annoyance is that if you do want to extend the API, then currently you have to stick within the constriants of legacy config– so you can’t implement multiple switches per source without abandoning the legacy xml config and writing a whole new xml config section handler.  

\* Trace should have a fluent API. I want to be able to write in a fluent API the configuration scenarios and then use an admin page to turn these scenarios on and off. Some typical scenarios — show me the app trace, show me the sql trace, show me the data trace, show perf trace, show everything, show only the current user, show all users, show me the next 10 minutes, write it to Session and then email it to me. When I have those, I have an incentive to write trace, and then when the code goes to production, the production admin will have a chance of diagnosing what is going on.  

\*