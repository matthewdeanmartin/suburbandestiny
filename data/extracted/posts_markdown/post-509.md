---
date: '2009-01-20'
recovered_from: wayback
slug: post-509
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200901\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=509
title: Sql Compact, it appears to be ready for use
---


In [3\.5 it support AES encryption](http://blogs.msdn.com/laxmi/archive/2008/04/15/sql-server-compact-database-file-security.aspx), which is required for use in US Federal government software development.


It can run run in [ASP.NET, even though it isn’t a “supported” use](http://blogs.msdn.com/stevelasker/archive/2006/11/27/sql-server-compact-edition-under-asp-net-and-iis.aspx).  I read this as the team that is writing it doesn’t have the resources to rigorously check and see how safe or dangerous it is to use Sql Compact in an ASP.NET environment.  Given the success of SQLite (or XML for that matter, e.g. Das Blog) I think file based DBs for small websites are a proven concept, and heck, it’s better than the alternative, given the known failures of MS\-Access.


It uses SQL Sever Management Studio as the primary tool for interaction.


It [supports Linq, especially if you use SQL Metal](http://geekswithblogs.net/steveclements/archive/2007/11/13/linq-to-sql.compact.aspx).


Some [ETL tools exist](http://www.codeplex.com/ExportSqlCE).


On the otherhand, it lacks JDBC, ODBC access.  It doesn’t have the ease of import/export that MS\-Access has.