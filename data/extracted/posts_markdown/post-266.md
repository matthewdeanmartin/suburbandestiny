---
date: '2007-08-10'
recovered_from: wayback
slug: post-266
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200708\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=266
title: 'Mod_aspdotnet: Some investigations'
---


[Mod\_aspdotnet](http://sourceforge.net/project/platformdownload.php?group_id=175077) is an semi\-abandoned application. The latest snapshot can run ASP.NET 2\.0 on Apache 2\.2, I’ve done it once against a DevSide WAMP stack: (<http://www.devside.net/> ) It was pretty cool to see ASP.NET run on Apache. Why?


* Apache can run on a thumb drive, IIS can’t
* If asp.net ran on apache on a thumb drive, then web apps could be run in a disconnected location off a thumb drive
* Admittedly, you’d need a host machine with .NET already set up and administrator rights to install the Apache.Web.dll. So you could take home your development environment, but not do development at say a locked down library or internet cafe machine.


I tried to reproduce the trick on a second machine with XAMPP, no joy, permanently stuck with:


\[notice] mod\_aspdotnet: CorBindToRuntimeEx has loaded version v2\.0\.50727 of the .NET CLR engine.  

\[error] (\-2146304894\)Unknown error: mod\_aspdotnet: Could not create the .NET interface for the Apache.Web.HostFactory.  

\[crit] (\-2146304894\)Unknown error: mod\_aspdotnet: Failed to start Asp.Net Apache.Web host factory


The error happens what appears to be a call to a constructor. So it behaved as if the class couldn’t load. So I tried uninstall/reinstall. No joy. I tried manual regasm/gacutil. That reported success, but still no joy, the error persists. I tried comparing httpd.conf files, no significant difference.


If I removed the “load mod\_aspdotnet” from the httpd.conf, apache ran, so I know everything else was working.


I tried theories involving code access policies and ntfs permission, but no luck. I turned off IIS on a theory that IIS was interfering, no luck.


Some factoids I’ve learned: the release files are an MSI. They can be unzipped and examined using TotalCmd. I also checked out the MSI using orca, which wasn’t too illuminating. There is an Apache.Web.Dll, which is a COM object that must be registered with regasm and then put into the GAC with GACUtil. The installer does this for you. The installer also seems to want to know where the apache folder is, so it can put the mod\_aspdotnet.mo into the right folder and two more files. The source code can be downloaded, but it doesn’t have enough files to compile by a naïve non\-C\+\+ developer like myself. You can also get a view of it using reflector and if you set a reference to it (it is a COM object), you can browse the same with the object browser.


I know, if I had tried to get ASP.NET 1\.1 working, I probably would have had more success, but I have no interest in working with 1\.1 unless I’m doing maintenance development.