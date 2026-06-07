---
date: '2008-05-08'
recovered_from: wayback
slug: post-352
source_file: data\normalized\tech.wakayos.com\root\__query__\p\352\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=352
title: Recommended to-do list for Classfieds Starter Kit
---


\-1\. Download the [Classifieds Starter Kit](http://www.asp.net/downloads/starter-kits/classifieds/).


0\. Read up on issues address on the [Classified Starter Kit forum](http://forums.asp.net/1021.aspx).


1\. Search for “lorum ipsum” and replace with suitable text. I created a Help.aspx page, since most of the lorum ipsums where place holders for a link list of help/support pages.


2\. Add application name to all providers, especially if you use the same aspnetdb for several applications.


3\. Get yourself access to the Admin folder. I did it this way:


\<location path\=”Admin”\>  

\<system.web\>  

\<authorization\>  

 **\<allow users\=”myuserID”/\>**  

\<allow roles\=”Administrators”/\>  

\<deny users\=”\*”/\>  

\</authorization\>  

\</system.web\>  

\</location\>


Ideally there would be some user/role management pages built into the administrative section.


4\. If you get the “There is no unicode byte order mark:cannot switch to unicode” error, you may need to change your xml declaration for the file App\_Data/site\-config.xml to encoding\=”utf\-8″ or encoding\=”utf\-16″ depending which one works


5\. Switch from user instance to a ordinary instance. You’ll want to run classifieds\-add.sql, modify classifieds\-categories.sql for your tastes and run it. Classifieds\-remove.sql is for restarting from scratch.


6\. You’ll want to update your connectionStrings and mailSettings sections of your web.config, especially the LocalSqlServer connection string which is used by ASP.NET membership providers.


7\. If you are getting “Can’t find page logon.aspx” then you may have a weird set up with cascading web.config files (i.e. web.config files in folders above where you application lives) then you may need to add this:  

\<authorization\>  

\<allow users\=”\*”/\>  

\</authorization\>


That allows the anonymous access users to get to the anonymous pages. If for some reason ASP.NET thinks you are in a secured folder (i.e. forms authentication is active), it will try to forward unauthenticated users to a default page of logon.aspx, even it doesn’t exist!


8\. Update the theme by modifying MasterPage.master. Optimally, one would implement masterpage and theme switching.


9\. Register.aspx has a lorem ipsum help section that seems aimed at helping creating ads instead of users. Also Register.aspx renders wrong on Firefox (labels align to the wrong box!)


9b. Admin/Ads.aspx renders wrong in Firefox.


10\. Error reporting is inadequate. All errors forward an error page that says contact the administrator.


11\. Create User wizard seems unreliable. I think this is because it isn’t properly reporting success and failure (i.e. feedback about password strength)


12\. The site desperately needs an RSS feed. It is unreasonable to expect users to visit the site everyday, like one might for craigslist.


13\. Add google analytics tracking to the masterpage.