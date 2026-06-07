---
date: '2007-02-13'
recovered_from: wayback
slug: post-199
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200702\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=199
title: MSDTC Considered Harmful
---


MSDTC creates transactions between two database servers, maybe running on different machines, maybe running on different database engines. That way when you mark down Al’s account in one server for $10 and mark up Bill’s account in the other server for an increase of $10, we don’t end up in weird situations where Bill has $10 and Al still has $10, or Bill has $0 and Al has 0$.



But what if you live in the real world and you want to transfer 1\.21 jigabytes of data from server A to B. First of all, this would create explosive log growth and crash your server. For some reason, SQL Server wants me to involve MSDTC when I do a INSERT INTO ServerA.mydb.dbo.mytable SELECT \* from ServerB.mydb.dbo.mytable



MSDTC has security problems. It uses RPC, lots of ports and as such MS turned it off in Windows 2003\. Re\-enabling it is not as easy as flipping in a switch, you have to get into the constipated bowels of the operating system and edit the registry, services, COM\+ settings and get your hands covered in binary smoo. After this, you reboot the computer and it still won’t work. This process of trial and error takes more hours than you want to spend on it.



I also tried turning automatic transactions off, no such luck.



Fortunately, a SELECT doesn’t start a transaction and using the ADO.NET SqlBulkCopy  

 class will not start a transaction. It is very fast and seems to be smart about data types, so a SELECT \* works as a source query.