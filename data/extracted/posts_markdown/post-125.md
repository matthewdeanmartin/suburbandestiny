---
date: '2006-04-28'
recovered_from: wayback
slug: post-125
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200604\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=125
title: SSIS Notes
---


Executing a stored procedure in the SQL Task is less painful if you use the ADO.NET provider.


Make sure you understand that a ‘data source’ is an XML file outside of your project, while  

Environment variables are portable (unless there is a name clash), but you might not have  

rights to set the enivornment variable.


Packages don’t like sharing package configuration files **if you are setting properties of objects that don’t exist in all packages**. Lets say you have 6 packages, each needs to have the names of 2 servers out of 3\. The 2nd package complains about the 3rd one existing.


Changing a connection manager is brutal. With my current technique, it means deleting all the OLE DB Destinations and sources, remapping, etc.