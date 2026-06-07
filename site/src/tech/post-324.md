---
date: '2008-02-19'
recovered_from: wayback
slug: post-324
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200802\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=324
title: 'ETL Anti-pattern: Checking for more than one problem at a time'
---


Problem.  

I had a set of potentially bad data.  My strategy was to create a constrained table with a foreign key, primary key, and domain restrictions on the columns. I would load data into it a row at a time, rejects would be sent to another table on a row by row basis.


Result.  

There were four things that could go wrong, some of them were expected to go wrong.  Some of them were unexpected.  Because I was checking for several things at a time, I saved lines of code, but could no longer distinguish expected bad rows from unexpected bad rows.  For example, foreign key violations were expected, but nulls for non\-nullable columns were not expected.


Better Pattern  

Dump data into an unconstrained table.  To be completely unconstrained, insert data into a table with no primary keys, no foreign keys, all columns nullable, and pick datatypes for the columns that are wider or more general than what you expect, for example, VARCHAR will hold most datatypes. However,  working with dates stored as VARCHAR is a pain, so you might want to run the small risk of datatype conversion errors and use appropriate datatypes on the intermediate raw data table.


Now if you have 5 things to check (say checking for uniqueness, data type range restrictions and foreign keys), write a query for each.


Also, remember that heaps (tables without primary keys), are sometimes non\-intuitively quirky, especially when dealing with oddities like 100% identical rows, so you might want to have row number primary key.  This won’t prevent/hide logical duplicates, but you will be able to delete and update with a better guarantee of how many rows will actually be changed.