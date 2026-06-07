---
date: '2011-12-09'
recovered_from: wayback
slug: post-640
source_file: data\normalized\tech.wakayos.com\root\__query__\p\640\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=640
title: Opinionated Trace
---


The problem with trace\-debug\-loggers (I’ll call it trace from now on) is that anything goes. I’m going to try to use the System.Diagnostics namespace with the extensions on codeplex.


Trace is a story, it is the moment to moment diary of the application. The audience of trace is a developer. They want to know what the application is doing. Computers do a lot, so trace volume will have to be carefully managed.


**Thou shall not trace in production, unless you have to.**  

Trace can be expensive. I took a representative 1000 repetition integration test that ran in 1/2 second and turned on verbose logging with DebugView running, and it took 17 seconds. This is why there should be some thought put into logging levels and why there should be multiple trace sources, so that most of them can be off most of the time.


**Thou shall be very wary of logging to the same transactional database as the application.**  

[Jeff had a bad experience with this kind of logging](http://www.codinghorror.com/blog/2008/12/the-problem-with-logging.html) and decided to throw the baby \& bath water out. I think they just needed to rethink what trace’s promise and possibilities really are.


**Thou shall use a TraceSource per class.**  

There should be a trace source per class. Typically we’re debugging a few classes at a time and turning off the other trace by commenting it out isn’t a practical solution.


**Thou shall not use System.Diagnostics.Trace or System.Diagnostics.Debug**  

Use TraceSource instead. You can’t turn off these sources as easily as a TraceSource


**Thou shall not reinvent System.Diagnostics. Extend it. Resist using other people’s re\-inventions. Do use other people’s extensions**  

Trace is for maintenance developers. A maintenance developer shows up on the scene and the last thing they want to see is yet another custom solution for a solved problem. How excited would you be to find a code base that shunned System.IO’s file system API and used an entirely custom one? Your app has a bug. You have one problem. You find out all the trace is written using a odd ball trace infrastructure. Now you have two problems.


**Thou shall not do start/end trace with nothing inbetween**  

Entry exit should be recorded for things that have multiple traced steps. If there is nothing in between start/end, it shouldn’t be added to the story \*unless\* you are doing performance. If you are recording enter/exit, you should also record the amount of time. You should use a Dispose patter to ensure that the End is written.


**Thou shall write a unit/integration test that is has been tuned for a good trace story.**  

The trace story should be shorter than a novel, longer than a flippant comment.


**Thou shall not write a Error trace unless we know it will also be error logged via Elmah or the like**  

Trace is not error logging. The maintenance developer is obliged to look at the error log, Trace is only on occasionally and even after tuning could have too much info.


**Thou shall educate the maintenance developer on how to use the existing trace**  

The .NET framework has a couple of trace sources. To get at them, you have to just know that they exist. There isn’t an easy way to query an assembly and ask it what trace sources are there and what switches it takes to activate them.


**Thou shall look for opportunities to replace comments with trace**  

We don’t want code to become less readable because of trace. So apply the same reasoning about deciding when to comment to when to log (don’t log the obvious, like most variable assignments)


**Thou shall not focus on domain specific events**  

These would be things like “John editing record B”, or “Sold book to customer Q”. 


**Thou shall use trace as sort of a poor mans Method\-was\-called Assertion**  

For example, if you are caching an expensive value, then on first call, there should be a trace message from the CreateExpensiveValue method and on the second go round there shouldn’t be any trace message. But unlike a unit test, the assertion is verified by a developer reading code. This shouldn’t be a substitute for using mockign frameworks.


**Thou shall not bother with Warn. Just use Error and throw an Exception.**  

Warnings need to have an audience and trace doesn’t always have an audience. Exceptions have an audience. And when an exception is thrown, we may want to add that to the story, since trace and error logs aren’t necessarily going to be together.


**Thou shall not bother with Verbose. Just use Info**  

Lets say I write a trace and I call it information. Years later it is in a tight loop that is executed 10 times a millisecond. You can’t control or predict in advance if a given message is info or verbose.


**Thou shall see the link between Trace and step through**  

Ever step through code that kept going throw a 3rd class and you though, I wish this would stop stepping through that class? You could add attributes (and remember to remove them later) or you could switch to a trace strategy that allows you to turn off trace for the likely\-just\-fine class.