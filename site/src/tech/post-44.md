---
date: '2006-01-17'
recovered_from: wayback
slug: post-44
source_file: data\normalized\tech.wakayos.com\root\__query__\p\44\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=44
title: SQL DBA Check List- Draft
---


I’m in the mood for lists.  Today’s list is the light touch DBA to\-do list, all the stuff a DBA can do without knowing what is in the database or having much time to co\-ordinate with the application developers


Admin Stuff  

\- Check for weird server and database settings.  Variances from default should have a plausible reason.  

\- Check for absence of  a clever server/database setting. Stuff like turning on ‘check for torn pages’ should be a no\-brainer.  

\- Check growth rate of database. Resizing is expensive.  

\- Check to see how transaction logs are being handled.  Uncontrolled transaction log growth causes headaches, often when you don’t give a damn about the transaction log.  

\- Check for a maintenance plan.  Make it clean everything up even if it is just a development/test box precisely because it is just a development test box.  Do you you want to trouble shoot issues related to re\-indexing on a test box?  

\- What is the reliability/availability needs? Pick a backup restore strategy.  

\- Set up notification emails.  You look silly when a scheduled task has been failing for the last 4 months and you’ve just found out.


Security Stuff  

\- Check for blank SA password (check all servers on network while you are at it for blank sa)  

\- Check for user id \= password


Data Modeling Stuff  

\- Does everything have a meaningless numeric primary key?  

\- Are alternate natural PKs set up to be unique?


Performance Stuff  

\- Are select column indexed?  

\- Are foreign keys indexed?  

\- Are you using lots of disks? The more you can split the various files that SQL uses among different disks the faster SQL goes. This is all transparent to the developers.