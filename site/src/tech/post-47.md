---
date: '2006-01-17'
recovered_from: wayback
slug: post-47
source_file: data\normalized\tech.wakayos.com\root\__query__\p\47\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=47
title: Red Gate SQL Tools
---


**Red Gate SQL Compare**: It does a better job than Apex SQLDiff, although I liked the UI of Apex SQLDiff better. In particular, Red Gate is more likely to generate a data preserving change script that will run without modification, however, it will choke on hard things like changing the data type of a column in a primary key.


**Red Gate SQL Data Compare**: On large databases, it is a bit slow. No matter how you write this code, the computer needs to read in 20GB of data at least twice, and that is a lot of IO and network chatter. Expect to find yourself resorting to alternative solutions, like replication, table copies, etc. The typical use case would be refreshing the data on a test or development server without blowing away the new stored procedures, indexes, etc on the development server.


**Red Gate DTS Compare**: I got a ‘Library not loaded’ error. Couldn’t test it. (update: it was DSO objects becoming unregisterd, had to reregister with regsrv32\)


**Red Gate SQL Packager**: This is pretty cool, although I’m not sure when I’d use it. The typical use case would be selling an packaged application that depends on a SQL database and you don’t expect an SQL expert to be at the client’s location to set up the database.