---
date: '2008-04-03'
recovered_from: wayback
slug: post-340
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200804\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=340
title: Installing Subversion, short edition
---


\- Use the Collabnet installer. It will save you the steps of finding and installing the modules.


Create a folder, say  

f:\\svn\_repositories  

That will be the PARENT FOLDER. You create repositories in the parent folder. If you are a MS\-SQL geek, then f:\\svn\_repositories means “Server” and f:\\svn\_repositories\\mycode means “database”


Each repository has a Apache “Location”. Each “Location” can have a password file.


Be sure to create a repository first with anonymous access and test that. Add this to the location to allow for browsing:


SVNListParentPath on


Ok. Next thing I ran into was that Apache is like Java and can’t find $\#!\+


This failed:  

AuthUserFile passwords.txt


This worked:  

AuthUserFile “D:/folder/otherfolder/passwords.txt”


Now the brower test passed with authentication. Now I can switch to tortoise and set up my repositories.


Next challenge will be moving repositories working folders around.