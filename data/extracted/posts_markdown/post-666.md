---
date: '2012-08-30'
recovered_from: wayback
slug: post-666
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201208\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=666
title: Cross Database Support
---


ADO.NET tried really hard to solve the cross database support problem. And the 2\.0 version (or so), with System.Data.Common namespace does a pretty good job. But when I tried to support SQL and MS\-Access, here is what I ran into:


Connection string management is a pain. If you are configuring an app to support MS\-SQL and MS\-Access (for a library app, in my case a hit counter), you need up to 6 connection strings:  

1\) Oledb Access – Because this is the old Cross\-DB API of choice  

2\) ODBC Access – Because Oledb is deprecated \& the new cross\-DB API of choice  

3\) SQL Oledb – Same template, different provider  

4\) Native SQL – Some things have to be done natively, such as bulk import.


I need something more than a connection string builder, I need a connection string converter. Once I have the SQL native version, I should get the OleDB version and the ODBC version for free.


Next– ADO.NET doesn’t make any effort to convert the SQL text to and from one dialect to another, not even for parameters. So I write this code.


**Cross DB When You Can, Native When you Have To**  

Some application features just require really fast inserts. For MS\-SQL that means bulk copy. For MS\-Access, that means single statement batches and a carefully chosen connection string. The System.Data.Common namespace lets you use factories that return either OleDB or native, but once they are created it is one or the other. What I wish there was, was a systematic way of the code checking for a feature and if it has it, use it, if it doesn’t fall back. Obviously this sort feature testing could be a real paint to write for some features, but for things like, say, stored procedures, why wouldn’t it be hard to check for stored proc support and when it exists, create a temp or perm stored proc to execute a command instead of just raw sql? I haven’t really figured out a way to implement this feature.


**Are you Really Cross DB Compatible?**  

Of course I am. After every compile, I stop and test against all 14 database providers \& configurations. Yeah right. If the application isn’t writing to the DB right now, I’m not testing it. So after I got MS\-Access working, I got SQL working. MS\-Access support broke. Then I got MS\-Access going again. Then they both worked. Then I added a new feature with MS\-SQL as the dev target. Then MS\-Access broke. And so on.


ADO.NET executes one command against one database. What I need to prove that I have cross DB support is “mulit\-cast”. Each command needs to be executed against two or more different databases to prove that the code works with all providers. And this creates a possible interesting feature of data\-tier mirroring, a feature that usually requires a DBA to carefully set it up and depends on a provider’s specific characteristics. With multicast, you can do a heterogeneous mirror– write to a really fast but unreliable datastore and also write to a really slow but reliable datastore.


I plan to implement multi\-cast next.