---
date: '2007-02-05'
recovered_from: wayback
slug: post-195
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200702\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=195
title: The Search for FAST Souce Control
---


The goal is to check out a big project from the office and edit it on my home PC using the company VPN connection.


Visual Source Safe, while not safe at any speed, isn’t able to reach very high speeds to begin with. I though for a few seconds about using the web services access, but decided slow web services on top of a file based database doesn’t equal faster. (however I will find out what the real numbers are)


Team System has a beautiful source control system, but my company has only 5 licences. And the set up and care and feeding for Team System is a remarkably high barrier to entry. (Soon I will see if it is worse than the others)


CVS is free, but has a user interface only a cave man could love.


Subversion. You are my only hope.


Subversion is a collection of command line applications, one of which can run as a server. The server component can be accessed across the network. There are two protocols that are safe, https:// and svn\_ssh://, the former being Apache 2\.0 and webdav based, the latter being based on ssh tunneling.


Subversion uses some weird protocols plus webdav. The svnserve process talks TCP/IP but has primitive security: passwords stored in plain text, doesn’t look like it encrypts traffic, etc. Webdav is a HTTP protocol that makes your web server work like a windows file share. Sort of. And at least you can encrypt traffic and use apache’s security.


To use webdav you need [Apache 2\.0](http://httpd.apache.org/download.cgi), (not Apache 2\.2!), which by the way is a steaming pile of sh\*t if you need SSL. A newbie can set ssl running on IIS in a hour or two. I just burned a couple of hours trying to get Apache to run SSL. Openssl is also a steaming pile of sh\*t. I don’t see why anyone would go through the significant effort of releasing code to the world without making any effort what so ever to make it work without a day of configuration. \[Update, you need to use [xca](http://sourceforge.net/projects/xca) to generate the key and certificate, and define virtual directories in the conf file, that's what finally worked for me.]


Next you want the latest version of subversion, 1\.4\. Install that and set it up as a windows service.


Finally, you will want Ankh. Get Version 1\.0 or higher. It is a Visual Studio plug in. It doesn’t use the same API that the VSS plug in uses, so don’t expect to find it on the options. You will need to have and see a solution to get the context menu where much of the Ankh action happens. Ankh doesn’t cover all the possible Subversion features, it is more for the basic check in, check out and see what’s changed. Alternatively, you could run the [underlying commands](http://svnbook.red-bean.com/nightly/en/svn.tour.cycle.html)


**Appendix:**


**Subversion Feature List**


\* Working folder caches a copy of original, so change detection can be done entirely locally (to see if you change anything since last check out), saving bandwidth


\* Changes are submitted as deltas (differences), not the entire file. Again, saves bandwidth.


\* Changes are atomic. An update to several files either succeeds entirely or fails entirely. Changes are logged to the client, then executed. If the computer fails midway, changes can be reapplied next time.


\* Working copy can become a mixture of versions. This is a feature or defect depending of your viewpoint.


\* Locking\-Change\-Unlock is possible, but not the default workflow.


\* Copy\-Change\-Merge is the default work flow.


\* Branching is supposed to be easy.


\* A VS2005 plug in exists.


\* Not a relational database, but that’s okay because text and document databases are a poor fit for relational stores. It does however have a real database API behind it, Berkley DB.


\* Free


\* Works with SSH or SSL/Apache/Webdav


\* Supports large repositories, so you needed maintain half a dozen separate repositories like in VSS.


\* Tool support



> [Ankh](http://ankhsvn.tigris.org/) (VS2005 plugin), version 1\.0 or higher.
> 
> 
> Apache (secure network layer), my advice, use the apache that comes with [collabnet’s distribution](http://downloads.open.collab.net/).
> 
> 
> [WebSVN](http://websvn.tigris.org/) (php UI)
> 
> 
> [Tortoise](http://tortoisesvn.net/downloads) (Client/Admin tool, stand alone GUI client, Windows Explorer integration)