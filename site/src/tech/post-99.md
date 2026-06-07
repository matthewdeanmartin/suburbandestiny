---
date: '2003-11-03'
recovered_from: wayback
slug: post-99
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200311\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=99
title: TSQL programming with MS-Access
---


**Pros**  

Fast  

Doesn’t corrupt  

Can handle a lot of data (unless you are using MDBE)  

Some DDL chores are easier in access than enterprise manager  

Gives a MS\-Access front end to SQL6\.5  

TSQL is a more expressive SQL dialect than JET SQL


**Cons**  

Hard to use VBScript functions, VB functions can’t be called from inside a stored procedure.  

Impossible to figure out how to change connection timeout  

Impossible to figure out how to globally turn off the ‘rowcount 10000′ feature.  

On account of the previous 2 problems I run almost all of my queries in Query Analyzer  

Requires extra step to graphically update joined tables  

Screws up the formatting of TSQL– default formatting isn’t very readable  

Can’t graphically view common constructs like CASE/WHEN/THEN  

Defaults to creating a table valued function instead of a stored procedure  

Have to split data accross lots of tables if you are using MSDE  

Heterogenous joins between local and linked tables have lousy performance (as compared to joining local tables to linked tables in an Access .mdb)  

Linked tables have cumbersome names, like SERVER\_DATABASE\_DBO\_TABLENAME, which is a pain when the “SERVER\_DATABASE\_DBO\_” part never changes! Why couldn’t they have used a shorter alias?  

Can’t see date/time a table or procedure was created (although the data can be seen in enterprise manager!)


**Tricks**  

To graphically update the join of 2 tables, create a view and then update the view.