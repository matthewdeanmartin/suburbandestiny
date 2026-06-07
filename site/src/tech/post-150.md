---
date: '2006-07-06'
recovered_from: wayback
slug: post-150
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200607\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=150
title: The SQL 2000 Post System Crash DBCC Script
---


Here is the human script.  Now I just need to write some code to check for each condition and to capture the output.


1\. Check for sufficient tempdb drive space: DBCC CHECKDB WITH ESTIMATEONLY  

2\. If server crash was hardware related and you are in business hours: DBCC CHECKDB WITH PHYSICAL\_ONLY  

(run a full check some other time)


3\. If server crash could have been more than just hardware related and you are not in business hours: DBCC CHECKDB WITH NO\_INFOMSGS  

(no news is good news)


4\. If server is slow or database is huge and you are in business hours: DBCC CHECKDB WITH NOINDEX  

(run a full check some other time)  

5\. If server is slow or database is huge and you don’t care if you users have to wait while you run DBCC: DBCC CHECKDB WITH TABLOCK


Loop through all databases.


\* By business hours I mean, the server is being used or otherwise under load.


6\. If errors found, start googling.