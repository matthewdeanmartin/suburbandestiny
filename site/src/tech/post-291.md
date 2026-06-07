---
date: '2007-10-15'
recovered_from: wayback
slug: post-291
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200710\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=291
title: 'MS SQL Server: TSQL Float & Real Considered Dangerous'
---


[Sums of floats can change depending on sort order](http://blogs.msdn.com/khen1234/archive/2005/05/13/417153.aspx).



Comparison tools (SQL Redgate in my case) can report two rows are different because some numbers don’t have exact decimal representations, even though these are the same. Likewise, retrieving rows based on a float value is iffy, sometimes requiring that you search for a small range to return the row with a particular float value. This makes testing more complicated, since you get false alarms when comparing the results of two float operations.



Redgate SQL Compare also has an Overflow \= 0, bug. That is, it converts the float to decimal to compare to decimal, one overflows so it decides overflow equals zero.



I’m not picking on Redgate here specifically, these are bugs that could happen anywhere in the development stack (at the TSQL, ODBC, application or third party tool level) when you are using float or real.



My advice is to use the decimal data type unless the decimal data type is failing and there is some compelling reason to use float/real. And if you do use one of these, pick real since it is twice as precise as float.