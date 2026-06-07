---
date: '2003-09-21'
recovered_from: wayback
slug: post-78
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200309\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=78
title: Can SQL be run in reverse?
---


Can SQL be reversed, say by looking at a trace of SQL and undoing each statement?


SELECT \-\> no operation  

INSERT \-\> DELETE row  

UPDATE \-\> no can do. We don’t know which subset was updated, and we don’t know what values used to be there.  

UPDATE (assume 1 row, primary key and the value being updated is also with the WHERE clause) \-\> UPDATE using appropriate values in WHERE clause  

CREATE TABLE \-\> DROP TABLE Works for similar DDL  

DROP TABLE \-\> no can do. Don’t know what we dropped. Similar problem for other DDL


Seems like it would be easier to reverse engineer the transaction logs, since they have entire row before and after snapshots of each row that changes.