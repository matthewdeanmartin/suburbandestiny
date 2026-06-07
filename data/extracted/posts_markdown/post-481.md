---
date: '2008-11-17'
recovered_from: wayback
slug: post-481
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200811\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=481
title: Cannot get IIS pickup directory.
---


In test and development, sometimes you don’t want to send the mail, you just want to write it to disk for reading as an .eml file.


IIS’s SMTP writes email to C:\\Inetpub\\mailroot\\Pickup


To let ASP.NET use that, first, you can’t do it in medium trust. You can only send email over port 25 in medium trust, not to the drop folder.


YOu will also need this link: http://agileer.com/blog/2007/05/24/CannotGetIISPickupDirectory.aspx


Editing the metabase may be required.