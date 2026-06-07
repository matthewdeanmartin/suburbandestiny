---
date: '2011-01-13'
recovered_from: wayback
slug: post-606
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201101\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=606
title: SQL Compact and MS-Access
---


So I saw SQL Compact 4\.0 was released and I was excited for a whole hour. A data source is as useful as the tools that can connect to it. Just about everything can connect to an MS\-Access database or to a SQL Server database, via Oledb, ODBC,  MS\-Access linked tables, you name it.  You can even get MS\-Access to connect to an XML file or a HTML table.  But HTML isn’t a real file based database and MS\-Access’s JET\-SQL is just different enough from TSQL to be annoying. So it would be nice to be able to have MS\-Access use SQL  Compact as a datasource, esp as a linked table and not as an ADO datasource in VBA scripts.


But as far as I can tell, this just isn’t possible to do \*without writing code\*. MS\-Access used ODBC to talk to unfamiliar datasources and AFAIK, there isn’t an ODBC driver to SQL Compact.  Googling turned up MSDASQL, but that solves the converse problem of getting an Oledb consumer to talk to ODBC. And MS\-Access is an ODBC consumer.


So that leaves either importing all my data from SQL Compact into MS\-Access (not too exciting) or writing VBA code, which might enable some scenarios.  This is one possibility I haven’t completely explored\- MS\-Access can bind to ADO recordsets, maybe including SQL Compact. It’s a possibility.


<http://support.microsoft.com/kb/281998>