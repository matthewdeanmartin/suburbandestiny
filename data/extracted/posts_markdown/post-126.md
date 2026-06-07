---
date: '2006-04-28'
recovered_from: wayback
slug: post-126
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200604\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=126
title: Implementing a ‘Separate’ Staging Area for a Data Warehouse
---


Seperate is as separate does. A [staging area](http://www.intelligententerprise.com/020917/515warehouse1_1.jhtml;jsessionid=JLGLRDDBYWV04QSNDBOCKH0CJUMEKJVN) is a place where data goes before it is presented to the user. But that can be a lot of things.


It could be a separate machine.


It could be a separate database on the same machine.


It could be a separate schema in the same database.


It could be a separate namespace (say table with ‘STG\_’ as a prefix)


Any important database has a set of DBA chores and to the extent that the staging area really is separate it double DBA chores, especially once the staging area is on a separate machine.


Here is my take on the pro’s and con’s


**Separate machine.** This double the work for DBAs and doubles the complexity and will cause a performance hit to the final transfer to production. On the other hand, users are isolated from the load of all other steps of the ETL process.


**It could be a separate database on the same machine.** Complexity drops, there is one less linked server to configure. A separate database can get its own recovery mode, backup policy, etc. Bulk loads by plain vanilla INSERTS can cause a the log to explode in size. This hurts performance and creates a risk of stopping the server. To the extend that activites can be isolated from a production server, a separate database is good. However, you will still have to do a final copy to production and that could lead to eplosive log growth. The server will have to deal with the load of each step of ETL, but the production database’s resources (name log space) will not be affected.


**It could be a separate schema in the same database.** Complexity drops further, but now the datawarehouse is subject to both heavy read (from users) and bulk load (from the data services staff) and optimizing for both of these will be hard. However, if all the bulk load task can take place over night, then it is easier to change the databases options according to the time of day, which may be more complicated than just having two databases with static database settings. The production database now has to deal with the bulk loads of each step of the ETL process, not just the last.  

**It could be a separate namespace** (say table with ‘STG\_’ as a prefix) This is much the same as above, except there are security issues regarding creating files with a schema prefix (owner prefix) or a dbo prefix.