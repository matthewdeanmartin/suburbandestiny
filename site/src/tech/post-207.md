---
date: '2007-04-08'
recovered_from: wayback
slug: post-207
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200704\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=207
title: The Great ASP.NET Lunarpages Experiment
---


I tried to move my webhosting account from a Linux server to a windows server at the same webhosting company–Lunarpages. My conclusion is that Lunarpages is a good Linux host, not a good Windows host.


Why


Plesk. Plesk is slow. It is not intuitive to see what is happening when you configure NTFS settings on the filesystem. It is not intuitive to see what is happening when you try to configure IIS virtual directories, websites and applications. And it is slow, at least 10 seconds between every single operation. Every click. Ten. Seconds. Or. More.


If Plesk had a family resemblance to the IIS snap\-in manager or Explorer, then I might have had more success.


MyLittleAdmin. Not to be confused with MySQL, this is a web based admin tool that targets SQL 2005\. And. It. Is. Slow.


I would not be surprised if Lunarpages is greatly overcrowding the servers. Or Plesk and MyLittleAdmin are crap. Or they are poorly configured. Or I won the trifecta.


I couldn’t get ASP.NET to work the way I wanted it. I wanted ASP.NET to be the 1st module to handle all requests, so that ASP.NET security would rule. Unfortunately, Plesk doesn’t allow it. So if I requested an aspx page, I got ASP.NET security. All other pages were public to anonymous users.


I tried setting security using NTFS. That required denying rights to all the anonymous users, but like I said before, Plesk pretty much leaves you in the dark about what is going on and I ended up denying the right to browse a folder to everyone, including myself.


I tried creating more than one ASP.NET application. No dice. The web.config files interfered with each other.


I couldn’t connect directly to MySQL or SQL2005\. Being forced to use web clients for database administration is punishment unbecoming of a webhost. I will not tollerate it.


I’ve moved onto another provider–[webhost4life](http://www.webhost4life.com/default.asp?refid=mattmartin)–and I’m retaining my linux account.