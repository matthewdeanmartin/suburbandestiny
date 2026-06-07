---
date: '2006-08-02'
recovered_from: wayback
slug: post-157
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200608\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=157
title: SQL 2000 Read Only Databases
---


1\. The misleading “Can’t issue a BEGIN TRANSACTION statement” error– I’ve seen this error from an ASP page. You can issue BEGIN TRAN/COMMIT TRAN on a read only database as long as you only do SELECT and the like.  

2\. Obviously can’t update anything– no INSERT, UPDATE, DELETE  

3\. All users must be disconnected before switching to or from READ\_ONLY.
The need to disconnect all users to go from READ\_ONLY to READ\_WRITE is possibly the issue that will prevent READ\_ONLY from being used more often, because even a datawarehouse needs to be loaded from time to time and kicking off all users is a bit hostile.


Nevertheless, if the database is usually read only and you can predict when some one is writing to it (like for a monthly data load), then it should be safe to kill open connections (except for connection pooling, see below), and the switch over is instantaneous. Another exclusion would be for stateful windows clients that hold connections open for a long itme. Another option is to patiently wait until the end of the work day when everyone has gone home.  

Sample Code:


– To RW  

ALTER DATABASE mydb SET SINGLE\_USER WITH ROLLBACK IMMEDIATE  

ALTER DATABASE mydb SET READ\_WRITE WITH ROLLBACK IMMEDIATE  

ALTER DATABASE mydb SET MULTI\_USER WITH ROLLBACK IMMEDIATE  

– To RO  

ALTER DATABASE mydb SET SINGLE\_USER WITH ROLLBACK IMMEDIATE  

ALTER DATABASE mydb SET READ\_ONLY WITH ROLLBACK IMMEDIATE  

ALTER DATABASE mydb SET MULTI\_USER WITH ROLLBACK IMMEDIATE


ODBC is rather dim witted when there is a bad connection in the pool. Instead of checking the connection and discarding it and opening another one, it assumes the server is down, the sky is falling and then it sits on it’s ass for two minutes waiting for the server to come back up. In the meanwhile, the user gets an error message. This happens if when we forcably close all the connections (WITH ROLLBACK IMMEDIATE).


The work around is to disable connection pooling. This will cause a small performance hit, which may or may not be equal to the performance gain you get with moving to a READ\_ONLY database.


Application(“ConnectionString”)\=”DSN\=mydb;**OLE DB Services\= \-2**“