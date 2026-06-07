---
date: '2006-09-09'
recovered_from: wayback
slug: post-170
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200609\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=170
title: SQL Server as an Application Server
---


I agree whole heartedly that a web form or windows form should not have much business logic behind the buttons.  I am not so convinced that IIS is a good place for most business logic and despite wanting to, I still don’t see the purpose of a separate machine holding the DLLs, like COM\+ was supposed to do.  And most importantly, software is about managing complexity.  A three tier system create extra complexity and performance bottlenecks.


However, if you have a database centric application, I think the two tier architecture that puts all of the business logic in SQL Server requires some examination.


SQL 2000 World


The case for putting most or all of your business logic into SQL 2000 is a bit less compelling because you can’t be very object oriented.  You can add behavior to your ‘datatypes’ (that is tables and base data types) with UDF’s and stored procedures, but all the data is globally scoped and SQL doesn’t see the relationship between the 12 function and stored procedures that act upon the collection of tables that represent the ‘account’ or ‘employee’ object.


SQL Function are stateless components.  In this respect they are every bit as good as a COM\+ component. 


Now here is the kicker. Application servers always say they can’t scale if a component is stateful. But a SQL server is all about scaling in the presence of state. 


SQL will maintain high availability of all this code.


SQL manages permissions on all these application things.  COM\+ tended to lead to yet\-another\-redundant\-level of security.


**SQL 2005**


The case for using SQL as an application server gets even better with SQL2005\.


SQL Server 2005 can serve up web services independent of IIS.


SQL can execute .NET components, either a stateless variety (functions) or a stateful variety (stored procedures.)


SQL can do message queue independent of MSMQ or a handwritten SMTP queue.