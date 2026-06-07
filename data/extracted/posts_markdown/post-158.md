---
date: '2006-08-04'
recovered_from: wayback
slug: post-158
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200608\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=158
title: 'Software Review: Free MS-SQL DB Documentation Generation'
---


[SchemaSpy](http://schemaspy.sourceforge.net/) is a free [database documentation](http://schemaspy.sourceforge.net/) generation tool.  It uses Java and JDBC to gather schema information.  The output is a browsable website for each database. It generates ERD’s if you have [Graphviz](http://www.graphviz.org/Download_windows.php) installed.  It also supports a large number of other databases, (important for me, SQL 2005\).  I haven’t figure out how to get intergrate security to work, but it does appear to work with just a user in the db\_datareader role.