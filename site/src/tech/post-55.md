---
date: '2006-02-03'
recovered_from: wayback
slug: post-55
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200602\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=55
title: Visual Studio Database Projects
---


**General Idea**  

Don’t use SQL Server as your master code repository. You can’t see change histories, you can see when an object was changed, who changed it, etc.  Also, if you are BAD and don’t use default ANSI settings, they will need to be set at each ALTER or CREATE of a stored procedure.  Some tools and developers forget to do this.  Also, if you DROP and CREATE a stored procedure, you will also need to regrant rights on the object, unless you are BAD and have a script that grants EXECUTE to public on all objects every five minutes.


**Create a Visual Studio Database Project**All scripts that are needed to create a brand new copy of your database, put into “Create Scripts”


All scripts that tranform your schema from V1\.0 to V2\.0, put into “Change Scripts”  Capturing these requires either creating them by hand or being diciplined when using tools like RedGate SQL Compare, EM or SSMS.


All scripts that you want to keep out of your server, can’t be turned into a stored procedure, are ad hoc but maybe reusable, put them into “Queries”


Create addtional or different folders if you don’t like this kind of logical arrangement because as far as the project is concerned these are all the same.


**Generate Scripts on per object basis**  

If using EM, generate scripts, per object, don’t use Unicode.  VSS6 can’t deal with Unicode, although VSS2005 can. 


If using VS2003, VS will use enterprise manager to generate your scripts when you drag and drop from the Server Explorer to your Solution Explorer.  This allows for 1 file per object.


If using VS2005, VS will generate the script how it damn well pleases, in one great big file, no questions allowed.  I can’t find anywhere in the Tools Options to change this.


**Checking In First Time** Visual Studio really, really wants to check the project in for you. 


However: Visual Studio will check in in how it damn well pleases.  Checking in a database project creates about 5 layers of empty folders. VSS will also try to check in your solution file, which by default ends up in the My Document Folder.  This implies that the next developer to check out your project will have to recreate your Document Settings tree structure, very non\-intuitive.


I say don’t add a database project using the ‘Add to Source Control’  Instead, use the VSS client.  You will get a slew of errors from VSS when you open that project from VSS.  Try Bind and unbind to get them to go away.  It didn’t quite work for me, but with trial and error, things seem to be OK now.


**Running the Scripts**Execute scripts either by creating a command file, which runs one or more scripts through osql, or right click on a single command.  If you have SQL2005, use sqlcmd scripts instead, although I’m not sure if the DB project supports them yet.