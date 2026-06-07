---
date: '2003-09-28'
recovered_from: wayback
slug: post-82
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200309\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=82
title: Converting phpNuke to MS SQL Server
---


Darn, I just spent most of the day writing notes about converting phpNuke to MS SQL Server and now I’ve lost my notes.


Anyhow:


Keyword conflicts: especially with keyword TOP and VIEW– they are used as column names in phpNuke and have to be surrounded by \[ ] both in the SQL intialization script and in the code.  

Datatype conflicts: mediumint, unsigned, binary, and many others, had to be replaced.  

Identity: mySQL allows you to insert a number in an autonumber/identity column, or insert a null to get the next number. T\-SQL wants you to list all the column names or call SET IDENTITY\_INSERT tablename ON and doesn’t seem to think it’s okay to use NULL as a place marker. This was a problem in the code and the sql initialization script.


PHP config\- need to turn off the errors, make sure that PHP.exe can see the database extension  

SQL Server Network Config– for some reason I had the wrong TCP IP port , should have been 1433\.  

The code tries to change LIMIT to TOP but the regular expression should test for \[Ll]\[Ii]\[Mm]\[Ii]\[Tt] since the code isn’t consistent with capitals.


I finally gave up, the PHP code gets to a point where it just fails to sent SQL to the database and it doesn’t get anything back. This happens right at a priv’s check, so I’m left without priv’s.


Oh well, I did learn about SQL2000 some and now I’m going to try again with mySQL. PHPNuke should take out the part that says it works with other databases, or at lease mitigate the claims.