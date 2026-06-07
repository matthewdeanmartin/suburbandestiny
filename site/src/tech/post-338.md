---
date: '2008-03-30'
recovered_from: wayback
slug: post-338
source_file: data\normalized\tech.wakayos.com\root\__query__\p\338\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=338
title: 'Product(s) Review: SQLite Maestro'
---


Why  

[SQL Maestro](http://www.sqlmaestro.com/) is a database administrator tool for people who work with a lot of different databases.  Wait! Before you say, “I just work with Oracle/MS SQL” or what ever, remember, many times you can expect to have to work with MS Excel, MS Access, CSV and other flat file formats.  Also, your personal website probably runs on MySQL or Postgres.  Most of these layouts either lack a superior administrator tool (such as the open source ones), or at best will be unfamiliar.


What  

It has a graphical query designer.  

It has database and table creation.  

It has table data editing.  

It has SQL script running  

It can export DDL SQL and INSERT statement.


How Much  

It’s fairly cheap.  The AnySQL version (that targets any database behind Oledb/OCBC) is very nice and it is freeware.  I recommend getting that, plus the commercial edition for the database you use day to day.


The Sqlite Code Factory appears to be a subset of features in SQLite Maestro.  It gave me an error messages of “can’t open the database, a process already has it open.”  Uh, which one?  I’m not about to reboot my computer, especially when SQLite Maestro (the other tool) can still connect.  I don’t understand why Sqlite Code Factory can’t connect, probably a bug imho.  If there was a feature of SQLite Code Factory that isn’t in SQLite Maestro, I didn’t figure it out.


I reviewed the SqlLite Data Wizard for it’s ASP.NET data entry page generation.  Two problems: it uses ODBC (which makes it inappropriate for medium trust websites), and it is buggy.  Two of pages for my tables failed the click test–i.e. just loading the page.  After I finally got it to compile by replacing the ODBC with System.Data.Sqlite objects, it raised a lot of warnings for not declaring data types.  Unfortunately, this can’t be fixed.  The templates allow for changing many options, but not the source code for the generated page.


SqlLite Data Wizard also had a task manager and import/export utility that supported a few formats.  Personally, I’d rather use ODBC \+ Talend Open Studio.


 The others  

I didn’t review the others.  SQL Express management studio is pretty usable, so I’m not too excited about the MS SQL Maestro.  I don’t have a need to use any of the others.