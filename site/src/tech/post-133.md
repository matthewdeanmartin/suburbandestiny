---
date: '2006-05-08'
recovered_from: wayback
slug: post-133
source_file: data\normalized\tech.wakayos.com\root\__query__\p\133\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=133
title: Whee, recovering a crashed SQL Server
---


I unplugged my workstation accidentally. On reboot I got, right after the trace for ‘starting up master’:  

**17207 : udopen: Operating system error 3(The system cannot find the path specified.) during the creation/opening of physical device .**  

and


**FCB::Open failed: Could not open device for virtual device number (VDN) 2\.** 


and


**Error: 5105, Severity: 16, State: 4\.**


Possible causes: database files being held open by virus scan, database files marked as readonly, or the master is hosed.


So I suppose master is hosed. I check for advice on [restoring master](http://www.phptr.com/articles/article.asp?p=27566&seqNum=1). I tried the rebuild master utility, which kept failing with error \-1\. A [BUG: report](http://support.microsoft.com/default.aspx?scid=kb;EN-US;q273572) said I might need to restore from a copy of the install files from harddrive, not a copy from disk.


I publish more if I ever get the server back up without just doing a reinstall of the server.


**Update**: It was faster to reinstall SQL Server than to figure out how restore the master.