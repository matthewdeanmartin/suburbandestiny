---
date: '2008-01-31'
recovered_from: wayback
slug: post-320
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200801\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=320
title: Learning about Medium Trust
---


Remove High Powered APIs  

No WMI calls, no SMO calls. The whole point of CAS is that you don’t trust your users to not figure out how to call a potentially dangerous API like WMI or SMO, so you mark the application as untrusted. This makes it impossible for you (or anyone else) to upload code to your website that calls these potentially dangerous API’s  

  

WebPermission  

My site was using a component that pulled and RSS feed from a third site and merged it into my page. That blew up on medium trust, but started working again when added:


\<trust level\=”Medium” originUrl\=”http://del\\.icio\\.us/.\*”/\>


Presumably more URLs could be added to the list using the regex operator \| (meaning or), e.g.


\<trust level\=”Medium” originUrl\=”http://del\\.icio\\.us/.\*\|http://www\\.yahoo\\.com/.\*”/\>


Custom web.config Sections  

My blowery HTTP component blew up on medium trust, but worked again when I added requirePermission\=”false” to the appropriate place under configSection


\<configSections\>  

\<sectionGroup name\=”blowery.web”\>  

\<section name\=”httpCompress”  

type\=”blowery.Web.HttpCompress.SectionHandler, blowery.Web.HttpCompress”  

requirePermission\=”false”  

/\>  

\</sectionGroup\>


Under medium trust, you can’t read most web.config entries directly, except for the above noted pattern.


Response.Flush/Response.Close yeilds SecurityPermission error  

Replace with Response.End and hope for the best