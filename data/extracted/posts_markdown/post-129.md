---
date: '2006-05-02'
recovered_from: wayback
slug: post-129
source_file: data\normalized\tech.wakayos.com\root\__query__\p\129\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=129
title: Thinking about Logging, Trace, Configuration, Error Handling
---


Today I was busy hitting my head against a wall of semantics. These are all related issues, but for some reason, we have four systems for dealing with them.  

**Logging** is communication aimed at everyone but the end user.  It is all about the about the moment to moment activities of the application. If you log to the windows system, application or security log,the likely audience is the machine administrator. Maintenance developers may or may not be able to read the security log.  Logging to a persistent store requires the same consideration you give to any other valuable data you would put in a database.  We don’t put the companies payroll into a jumbled text file, why should we do the same with application logs?  

**Notification** is logging aimed at the maintenance developer that need response right now. Most logging that is happening while the end user is ignored unless there is a notification. Don’t expect technicians to check system logs on a daily basis, they have lives–of a sort.  

**Trace** is logging to a non\-persistent destination, usually the screen, console or other ephemeral destination.


**Error Handling** is trace about an entirely unexpected event.  If you tried to open a file and the file didn’t exist, the exception means the developer needs to write code to check for the existence of the file.  The only time error handling should be used as a flow of control is the expected, but impossible to test for in advance situation, like a database connection timing out.  The rest of the time, errors should result in a trace, log entry or notification to the administrator or maintenance developer to take action.  Which leads to the exception to the rule: if none of the above can be expected to solve the problem, then the error should be handle in the flow of control with a message to the user to try again.