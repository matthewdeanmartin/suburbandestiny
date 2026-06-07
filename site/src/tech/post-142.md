---
date: '2006-06-02'
recovered_from: wayback
slug: post-142
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200606\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=142
title: SSIS Trick
---


BIDS doesn’t sort package names in the Packages folder. To make them sort, exclude all from project and then re\-add existing item. DO NOT re\-add existing project, because that will make a copy of the project instead of adding it as would be intuitive. (This add\-as\-a\-copy behavior only makes sense if you are getting a package from the SQL msdb store)