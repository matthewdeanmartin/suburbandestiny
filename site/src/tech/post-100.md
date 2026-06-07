---
date: '2003-11-07'
recovered_from: wayback
slug: post-100
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200311\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=100
title: Droping tables in T-SQL
---


Ideally, we want to have a function that will drop a table if it exists, do nothing if it doesn’t exist. This can be done in T\-SQL or DTS. In DTS we create a single DROP TABLE statement into SQL task and then have the exit arrow set to ‘on completion’ so the code goes on even if the table didn’t exist. This can create a lot of clutter on the DTS drawing board.


Writing pure T\-SQL makes this a pain, but with a T\-SQL function, at least you can shorten the code.  

 `IF dbo.TableExists('myTable')=1 -- THEN  

 drop table myTable  

-- END IF`


The DDL for the above function is :


 `FUNCTION dbo.TableExists(@tableName varchar(250))  

RETURNS bit  

AS  

 BEGIN`


DECLARE @OUT bit


IF EXISTS(SELECT TABLE\_NAME FROM DATA.INFORMATION\_SCHEMA.TABLES  

 WHERE TABLE\_NAME \= LTRIM(RTRIM(@tablename)))  

 SET @OUT \= 1  

ELSE  

 SET @OUT \= 0 


 RETURN @OUT  

 END  




The database name needs to be changed for each database where the function is deployed. Also, notice I’m returning a bit and not a boolean, (which I’m not sure if it is possible), so you have to check for equality to 1 or 0 when using the function.