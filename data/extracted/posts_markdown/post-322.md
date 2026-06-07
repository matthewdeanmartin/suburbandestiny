---
date: '2008-02-11'
recovered_from: wayback
slug: post-322
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200802\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=322
title: Getting Going with Pervasive ETL
---


I get a “DJRepository.Manager.1  Failed to get ClassPath” error opening any Pervasive ETL tool.


I thought, maybe Pervasive could help,  so I called. They said my company would need to rebuy the application and get a new maintenance plan, as our maintenance contract had lapsed..  I think for $10,000 I can solve this class path error myself.  

In case anyone else hits this error, what it means is Data Junction/Pervasive ETL can’t fine your DJ800\.ini file, which it expects to find in the “C:\\Documents and Settings\\{username}\\WINDOWS\\” directory or possible “C:\\WINNT” or possibly “C:\\WINNT\\System32″, but probably the first.  You probably can find a copy of this by doing a global search.


Uh\-oh.  A typical installation is just crawling with dj800\.ini files, some in profiles, some in system folders, some with (copy), “\_” and “x\_” prefixes, probably indicating version upgrades.


Across my favorite machines, I find 3 versions, 8\.4\.19, 8\.14 and 8\.19\.  Only the 8\.4 one has class path problems.  Now the version number appears in the dj800\.ini file, so the reported installed version may just depend on what dj800\.ini file is active at the moment.


Sigh. If the you get a classpath error from Data Junction/Pervasive Data Integrator, upgrade to version 8\.14/8\.19 or later.  It is probably an issue with configuration information being stored in a profile specific fashion.