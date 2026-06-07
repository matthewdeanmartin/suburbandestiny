---
date: '2007-08-20'
recovered_from: wayback
slug: post-269
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200708\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=269
title: Blowery Compression and MaintainScrollPositionOnPostback Errors
---


The [blowery ASP.NET gzip module](http://www.blowery.org/code/HttpCompressionModule.html) deals poorly with axd files. The axd files aren’t really files on the disk and they [often are already compressed](http://kyle.baley.org/BlowerywebAndASPNETAJAXOrQuotHowToMediateTwixtCompressorsquot.aspx).



I don’t completely understand it, but these are the exclusions I used to get Maintain Scroll Postion On Postback to work. WebResource is related to the scroll position code, scriptresource is an ajax thing, and ebresource, I think that is yet another frameworks piece of code.



\<excludedPaths\>  




    \<add  

path\=“ebResource.axd“/\>  




    \<add  

path\=“ebresource.axd“/\>  




    \<add  

path\=“\*.axd“/\>  




    \<add  

path\=“webresource.axd“/\>  




    \<add  

path\=“WebResource.axd“/\>  




    \<add  

path\=“ScriptResource.axd“/\>  




    \<add  

path\=“scriptresource.axd“/\>  




    \<add  

path\=“%.axd“/\>  




\</excludedPaths\>