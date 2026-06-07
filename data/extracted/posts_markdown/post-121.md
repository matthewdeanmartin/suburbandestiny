---
date: '2006-04-22'
recovered_from: wayback
slug: post-121
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200604\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=121
title: 'Installation: So you think I got time to burn…'
---


The SQL 2005 Installer got to the part where it installs Reporting Services, but it couldn’t find the ASPNET account. Well I had just installed IIS and forgot to run Aspnet\_regiis.exe \-i. Fortunately, I’ve seen this before. The installer recommended reinstalling the 2\.0 framework. Actually, I think the developer who wrote this part of the installer could have been more hostile, he could have suggested repaving the computer and reinstalling from the OS disks. As if I have time! Yet another reason why we don’t use Reporting Services.


D’oh– The install still required doing a ‘repair’ of Visual Studio, which took longer than the original install.


And to add insult to injury, the installer seemed to be consuming a lot of space on my C drive (which has no space) even though I was installing to my F: drive, which has tons of space.


But everything seems to work now.  For now.


But then MS Outlook stopped working and said it wanted to repair itself.  So it asked for–the  MS One Note installation disk. I never use One Note! Maybe it has been the application destabilizing my Outlook installation.