---
date: '2008-01-18'
recovered_from: wayback
slug: post-314
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200801\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=314
title: How hard is it to make SQL Express easy?
---


Goal. Make it easy for a end user, say with half as many brain cells as a mollusk, to install a DB driven website.


Particulars. A typical database set up requires creating the database, setting up the logons and users for the anonymous web user, the ASPNET web user and maybe an application user or role. The user then needs to run a TSQL script to install objects. Finally the user needs to set the connection string in the web.config.


Solution so far. If the user has an existing database, user and connection string and can put it in the web.config, I can run the TSQL scripts for him and even detect and create the application user.


Speed Bump. Wouldn’t it be easier if I created everything in advance and put it into App\_Data and connected to it using an user instance? Well, so one would think. It would mean you could use a mdb file without knowing: the server name, the credentials, the file location (except that it is in the usual App\_Data folder)


Here is the magical connection string:


Data Source\=.\\SQLExpress;Integrated Security\=True;User Instance\=True;AttachDBFilename\=\|DataDirectory\|calendar.mdf  
  

Here are the magic error messages (short list, I forgot to copy some of them down)


Invalid value for key ‘attachdbfilename’. 


Failed to generate a user instance of SQL Server due to a failure in starting the process for the user instance. The connection will be closed.


“No connection could be made because the target machine actively refused it”


Unable to open the physical file “C:\\Inetpub\\foo\\App\_Data\\aspnetdb.mdf”


Random things tried:  

Don’t create the mdb file using the “Add New Item” menu in Visual Studio (create DB the old fashion way with Management Studio)  

Change .\\SQLExpress to actual server name, eg. MyBox\\SQLExpress  

Changed \|DataDirectory\| to the actual physical directory.  

Grant rights to NETWORK SERVICES, LOCAL SERVICE, MyBox\\ASPNET to modify files in App\_Data folder (preferably only to the account that the anonymous user is running as, not all three of them)  

Switch from IIS to ASP.NET Development Server (or other way around)  

Delete files found at:  

C:\\Documents and Settings\\\[some user name]\\Local Settings\\Application Data\\Microsoft\\Microsoft SQL Server Data\\SQLEXPRESS  

The above folder holds the various databases that SQLExpress creates upon creating a User Instance  

Don’t use Remote Desktop. When you run a user instance across remote desktop, it is hard to guess what User profile the various system databases will be written to.


Advice\- User Instance, just say “\=false”.  

User Instances are bad. Bad bad bad. They might be okay in a windows application that you are running on a single disconnected machine in a salt mine mile below ground.


AttachDBFilename  

This is only going to work if you have administrator rights. You typically will not give your anonymous account admin rights to the database. So right away, we can see Integrated Security\=True and AttachDBFilename\=… do not go together…unless you are using windows authentication. A brain damaged mollusk doesn’t know how to set up windows authentication, less so on a hosted account where user admin tools are often crippled and incomplete (I’m thinking of the lunarpages control panel here)


Furthermore, \|DataDirectory\| doesn’t always resolve.


So what is left? We have a file that isn’t attached, that ADO can’t find, and we need a priori information about the SQL instance name and a priori information about the user ID, password, and database name. Sigh. Thanks Microsoft. Not a single break.


Final Solution  

Half brained mollusks will have to use conventions. First, assume the server name is “localhost”, second the user will have to find out what the credentials are and hope the credentials have dbo. Finally, the user will have to know what the db name is.


Worse, the user will have to be able to edit the web.config file. I’m now going to work on a web.config generating page, so the user can enter the five magic words and get a web.config file generated for him.


Blogged with [Flock](http://www.flock.com/blogged-with-flock "Flock")