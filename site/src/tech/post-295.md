---
date: '2007-10-25'
recovered_from: wayback
slug: post-295
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200710\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=295
title: 'SSIS: Avoiding setting the data down'
---


I’m merging two files.  One file has some measures, the other has some more measures.  When the facts are the same, they need to show up in the same row.  If the fact is missing from on or the other, the row still needs to be in the resulting fact table.  In T\-SQL jargon this would be a full outer join (a join, but everything from both tables)


Idea \#1\.  Union them and sum them.  **Unfortunately the aggregate component can’t take the minimum or maximum of a string column.**  So to get that, I’d have to write the table out to SQL server.  Once it is in SQL server, the data has been set down– I might as well do the rest of the work in TSQL from that point forward.  Idea REJECTED.


Idea \#2\.  Merge Join and sum them.  Same problem, can’t get the correct subtotal because I can’t group by the text column and I can’t take an aggregate of it either. Idea REJECTED.


Idea \#3\. Use SSIS to get the raw files into SQL server, use TSQL exclusively thereafter.  SSIS would be used here just for the first round of data type conversions, simple expressions and lookups.


An exception would be when a Data Flow Tranformation would be handy, for example when populating a constrained table and you want the rows with constraint violations to be redirected.  This is something that TSQL does poorly as a SELECT INTO either succeeds or fails as a single operation and writing TSQL cursors or single row INSERT’s is tedious and ugly in TSQL.