---
date: '2008-06-17'
recovered_from: wayback
slug: post-373
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200806\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=373
title: What is a stp file?
---


If you export a “site definition” from sharepoint (from site settings, look and feel, save as site template), then go to the “site template gallery”, save the file. It is a .stp file, which if you rename to .cab, you can unzip it. I use 7z to unzip it there may be other ways. The file contains .000 files, which are C\# files, there is a large manifest.xml file, which references to the .000 files, which I think are the “customized/unghosted” pages. All other pages and dependencies are referenced by entries in theses lists:


MetaInfo, Details, SiteFeatures, WebFeatures, Structure, Files, UserLists, WebParts.


Some of the above seem to have been serialized into the manifest file, some are obviously just pointers to things that the template expects to already exist in SharePoint.


There can also be large binary blobs in the file, which gives XML viewers and editors a hard time.