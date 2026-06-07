---
date: '2008-01-21'
recovered_from: wayback
slug: post-315
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200801\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=315
title: Redirecting SNAFUs in global.asax
---


It seemed all so simple.  Check to see if the database is set up, if not redirect to an installation page.  I wanted the check to be done at session start instead of every page to reduce database queries.  Ideally, I only want this check to happen once per web.config modification, but I don’t know how to hook into that event.


First I put this into the global.asax at Session\_Start  

Response.Redirect(“\~/install/installdb.aspx”)


I get a permissions error in Medium trust, but not in Full trust.


Then I try  

Server.TransferRequest(“\~/install/installdb.aspx”)


And I get  

“*This operation requires IIS integrated pipeline mode.”*  
Apparently IIS5 and Cassini can’t deal with TransferRequest.


Then I try  

Server.Transfer(“\~/install/installdb.aspx”) 


Finally, that works.  



Blogged with [Flock](http://www.flock.com/blogged-with-flock "Flock")