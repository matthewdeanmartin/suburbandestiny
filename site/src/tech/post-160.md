---
date: '2006-08-10'
recovered_from: wayback
slug: post-160
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200608\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=160
title: Updating a bazillion rows in SQL
---


It takes a long time to update 27 million rows.  One strategy I used– bcp Export the table to text, write a .NET program to read each line in, update the relevant column, write back out to a file, BULK import \& voila.  Works only if no one is updating your big table during the time between the bcp export and bulk import.


If you have to do it in sql, I recommend doing a UPDATE TOP x, so that the update is done in batches of 50000 or so.