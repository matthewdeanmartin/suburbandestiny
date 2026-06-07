---
date: '2008-04-15'
recovered_from: wayback
slug: post-342
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200804\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=342
title: 'Hit by a Php Root Kit: ro8kbsmag.txt'
---


I am very annoyed.  I’m down 5 blogs, 2 php apps and I have 2 suspect blogs.


This is new to me. Apparently using SQL injection attacks (or guesses the DB password), the hacker does a select on the user and password table to get MD5 hashes and they create their own cookie. They upload a utility php file using wordpress’s own API, that then starts writing, editing and creating a lot of php files and some wp\_info.txt files, which contain the passwords for the website.  If you are doing a clean up, look for date changed. A clean install should have the same date changed for just about all files.


The virus also starts mucking with wordpress tables in mysql, esp the options table and user table.


The virus will add php code to any php pages it finds, so it can infect files other than wordpress. If the server account that the php script runs as can browser other accounts, it appears to move through the whole file system.


The solution is to wipe the infected directories, replace with new wordpress installation, change the db password, restore from backup if you can, etc. etc.