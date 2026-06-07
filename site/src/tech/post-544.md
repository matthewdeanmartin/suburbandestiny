---
date: '2009-06-08'
recovered_from: wayback
slug: post-544
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200906\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=544
title: The sorry state of application security audit logging
---


Security oriented audit logging records what happened and who did it. So lots of logging frameworks fail because they aren’t very well integrated into the authentication scheme. Ideally, the log entries would non\-deniable and read and write\-only (i.e. no updates and deletes) by a non\-administrator. And super\-ideal would be a rich, granular permissions system. For example, NTFS rights are read/write. There isn’t an append\-only right for files. And ordinary users need to be able to write to the log. Logging isn’t useful if only the administrator can write a log entry. And ordinary users need to be able to review the log, although not necessarily the same ordinary users that wrote to the log. 


This excludes logging techniques where you can write 


Log(“I committed a crime”);  

DeleteLogs(); //or update logs


Likewise, this should’t happen when running as user John Doe:


Log(“Bill committed a crime”); //Not me!


**Windows Event Log.**  

 Requires pinvoke/win32 API calls to record event with user Id.  

 Can log to Application from ASP.NET with blank user from C\#.  

 You might not even be able to tell which website or application wrote the error log entry.  

 Looks like it only works with windows authentication, and not custom authentication, e.g. GenericPricincipal.  

 Only an administrator can create a new log/event source.


**Sql Event Log**  

 No user (except SPID) is recorded  

 Xp\_Logevent requires membership in dbo in master, or systeadmin, or explicit rights


 EXECUTE master..xp\_logevent 50003,’hello world E’, ERROR  

 RAISERROR (‘hello world from raiserror’, 500000,1\) WITH LOG –Requires sysadmin rights to use WITH LOG


**IIS Log **Response.AppendToLog(“Action recorded by Austin Powers, really.”);  

 Has the cs\-username field, but it is the service name, not the real user.  

[For IIS5/6 you need to write an ISAPI filter to hook into the code writing to that log to change cs\-username](http://www.velocityreviews.com/forums/t362252-setting-csusername-from-an-aspnet-site.html).****