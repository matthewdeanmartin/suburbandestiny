---
date: '2007-02-13'
recovered_from: wayback
slug: post-200
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200702\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=200
title: MS Access as a Linked Server
---


I needed to simulate an Oracle server, but didn’t like the idea of trying to install and run Oracle Express. So I created a linked Server pointing to an Access MDB with tables linked to a SQL Server, which had tables dumped from the Oracle Server. This allows for OPENQUERY queries without the “db.dbo” prefix that you’d need if you’d just referenced the SQL database directly. You know a database is hard to use when you can’t convince database professionals to use the free copy installed on their machine.



These are the things I did to get my lined server working:



1. Switch connection string from SQL authentication to Windows Authentication.


Without that, you get can’t find installable ISAM or authentication errors.



What didn’t work



1. Giving more rights to IUSER and ASPNET account (this was only failing in my web app, not in SQL Server Management Studio)
2. Setting the password in the provider string.