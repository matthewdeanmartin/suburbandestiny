---
date: '2007-11-17'
recovered_from: wayback
slug: post-305
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200711\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=305
title: ASP.NET Skills
---


ASP.NET itself was all about recognizing that a web site has a lot of features that are the same across web sites. The Patterns \& Practices Enterprise Library also addressed the fact that a lot of problems need to be solved for all kinds of applications– and to some extend, these cross cutting solutions have been moved into the .NET framework.


Authentication. Determining who the user is.  

Authorization. Making groups of users, deciding what actions groups can do and what things they can touch.  

Security. Making power APIs unavailable to hackers.  

Data Tier. Getting data out of tables and into objects and collections. And putting it there.  

Build. Deployment. Turning source code into a published application.


The problem domain itself. Obviously the problem domain will make some APIs more useful than others and is the most likely to consist of custom code.


Knowing that there are these half dozen problems that all websites face isn’t too useful if you don’t know the expected hosting environment.


**Intranet.** If the app is a private intranet application, then authentication and authorization would likely be done by Active Directory or Adam, security is somewhat less critical to be built into the application because users are employees who fear losing their jobs are not sophisticated hackers (as compared to the internet scenario where attacks are from sophisticated hackers safely in another jurisdiction). A full version of SQL Server is probably available. Full control of the Windows server allows for MSI installs, access to SSL certificates, etc.


**Internet.** If the app is a public internet application, then authentication is going to probably be the SQL provider, authorization will be SQL or Azman, security will be important because random world wide hackers and malware will be attacking your machine even if you aren’t an e\-commerce site. The data tier might be more primative, maybe XML files, like in a Das Blog set up. The hosting account probably doesn’t provide for MSI installs,


**Hybrid Intra/Internet.** This is the most challenging set up because MS didn’t specifically provide for it. In 1\.1 it was very hard, in 2\.0 it is possible but still hard. ’nuff said.


\[Sorry no time to finish writing this post]