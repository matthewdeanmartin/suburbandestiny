---
date: '2008-03-11'
recovered_from: wayback
slug: post-332
source_file: data\normalized\tech.wakayos.com\root\__query__\p\332\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=332
title: Embedded databases for speed and simplicity
---


(blog entry brought to you by time snapper.  This entry would have been lost to an electricity outage if not for my screen recorder.)


When I want a relational database, I might want something that can handle a billion transactions per second, never loses data, and can be updated by 1000 users simutaneously without corrupting data.  If my application just needs a single small table, the overhead of a relational DB is overkill.


\[likewise for ETL scenarios\-\- writing SQL based ETL code in a full\-blown RDBMS for an ETL process incurs a lot of overhead that just slows data processing down.  On the otherhand, dropping back to using text isn't very good either as you forego the power of SQL]  




In particular I want an embedded database that is:


* free
* works in ASP.NET \& ADO.NET
* supports all important SQL statements
* is very fast
* does’t require setting up a secure service (i.e. daemons or windows services)
* Support for bi\-directional databinding in .NET
* Doesn’t require an installer/COM component registration, etc. i.e. nothing that would be a barrier on a hosted account
* Runs in medium trust
* Secure against executable code (should be able to call OS shell functions like one can in MS\-SQL, MS\-Access and the like)
* Can zip up the data with the source code and send in an email


**MS\-SQL 2005, MySQL, etc**These require an install, administrator rights to set up, some non\-trivial know how to configure the database and users.  Nope.  Too much work.  




**Text and Excel**Database drivers for text files tend to be pretty primitive, low performance and often don’t support updating.  Excel has limitations on the number of rows you can deal with.


**MS\-SQL SQL Compact/Mobile Etc**  
  

Doesn’t allow for hosting inside of an ASP.NET worker process. End of story.


**XML**  
  

Not supported for bidirectional databinding with default ASP.NET controls.  I’m pretty sure this works in medium trust  




**MS\-Access/Fox Pro**  
  

If MDAC is available, you probably can use the Microsoft.Jet.OLEDB4\.0 driver.    




**Berkley DB**  
  

Berkley DB was bought by Oracle.  Oracles distribution is slanted towards support of the Java world, but a .NET driver does exist.  




**SQLite**  
  

See my blog entry on SQLite.  Of all my options, this is the one I liked the most.  It runs well in ASP.NET, can support large numbers of users, has Visual Studio support (better in the full version than the express versions).