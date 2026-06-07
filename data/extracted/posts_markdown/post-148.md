---
date: '2006-06-22'
recovered_from: wayback
slug: post-148
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200606\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=148
title: VSS via IIS
---


One article on setting up [VSS on ISS](http://diaryproducts.net/about/operating_systems/windows/sourcesafe_2005_internet_iis).


Here is a short list of my notes on using VSS with SQL. 1st off, I’m imagining that only procedures, views, functions and other objects that look like code will be checked in. Altering tables is rocket science and requires a specialized tool.


VSS/SQL integration mostly means you generate the scripts for all code\-like objects. Then you check those into VSS. Then you edit those files and it is up to the developer to run them against the appropriate server. VSS can make sure that your local copy of the scripts and the code database’s copy of the scripts are in synch, but can’t check for people making changes to their local database’s. A developer could accidentially skip the check out and edit the proc directly in Enterprise Manager and VSS wouldn’t know it, unlike the working copy of scripts, which are set to read only until explicitly checked out. Similarly, when code is checked in, the developer could forget to publish the new proc to his local SQL server.


Also, if the developers are using a shared SQL box, then when the run the SQL script, the last one in wins, unlike VSS, which detects conflicts. This can be solved by using a shadow copy (which publishes the files in VSS to a shared folder), which could be automatically imported into the shared database, say in a nightly build process, or on demand.  

VSS Client: No SQL features (the scripts are just text files), although you can tell VSS to launch your favorite editor.


Query Analyzer: No VSS features


Visual Studio: Some VSS integration, but the work flow is a bit clunky. You have to manually synch up the name of the script file and the name of the object. After exporting objects, you have to manually add the create scripts to the project.  Plus there are two ways to change a procedure, either in the object explorer in the server browser, which doesn’t have VSS features, or in the scripts folder of the database project.


SQL Server Management Studio: Some VSS integration, somewhat similar problems as Visual Studio, although different.


Script export/import: This is the process of synching VSS to SQL. Ideally, we’d want to be able to detect conflicts. Failing that, we’d have to resort to using security rules to keep people from editing the SQL code in SQL directly, or being mean and having a policy that says, the code in VSS always wins, regardless to any changes made directly to the Server.