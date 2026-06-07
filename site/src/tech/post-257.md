---
date: '2007-07-18'
recovered_from: wayback
slug: post-257
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200707\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=257
title: Registering the PowerShell MSAccess Provider
---


Compile the provider. It is called a provider, but treated like a snap in.


set\-alias installutil $env:windir\\Microsoft.NET\\Framework\\v2\.0\.50727\\installutil.exe  




installutil c:\\….. path to the .net assembly  




see if it worked  




get\-PSsnapin \-registered  




In the next step use the *snap in* name  




add\-pssnapin “AccessDBProviderPSSnapIn05“  




This was the part I missed. This time the name is the *provider* name.  




New\-PSDrive \-Name AccessDB \-PSProvider FileSystem \-Root “c:\\myaccess.mdb”  

  

To get to the new ‘drive’, use


set\-location … name of drive…


You should now be able to navigate to the MS\-Access database as if it was a file system and use PowerShell file system commands to do stuff.