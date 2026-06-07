---
date: '2008-02-26'
recovered_from: wayback
slug: post-326
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200802\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=326
title: Named SQL 200 Instances
---


SQL 2005 uses SQL Browser to route traffic to the various instances on a box.


SQL 2000 uses “SQL Server Resolution Protocol” It listens on 1434\.  If someone forgot to open this port, you migh thave a hard time seeing the named instance.  Unlike SQL Browser, there is no obvious way to see if SSRP is running, except running portqry (on the client) and netstat \-an (on the server). Also, it appears that SSRP dynamically determines the port of the ports of the instances, so they might be hard to predict if you are trying to communicate through a firewall.  




You can sidestep the issue by:


Statically setting the port of the instance, say to something that likely is open, like 1433\. Do this using the SQL 2000 “Server Network Utility” on the server side.


You will need to update your connection string to use a COMMA to specify the port.  This is highly non\-intuitive, as most protocols use semicolon.


E.g.


MYSERVER,1433\\MYINSTANCE


This would probably work for other ports, like port 80\.


Here is the [KB article I used](http://support.microsoft.com/kb/286303/). [And this one too](http://support.microsoft.com/kb/827422).