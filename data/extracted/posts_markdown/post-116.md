---
date: '2004-08-18'
recovered_from: wayback
slug: post-116
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200408\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=116
title: LunarPages
---


Cheap, but if you accidentally run a script that hogs the server, you get kicked off. Each server holds a bunch of websites, so no one can use more than a small percent of the CPU, so many JSP applications (like cocoon) are not allowed. Some applications like MovableType are not allowed (resource hog, insecure). You can write your own code, but if it goes bad the host can either disable the code or disable your account. There are scripts to install common free web applications, but you only can do one on account of the database limit, even though most of these apps would be happy to share one database were you to do a manual install.


I got Internal Error 500 a lot trying to run a trivial PHP script. It means:  

1\) You are not using your domain name (mywebsite.com) and are using something like meteor.lunarpages.com/\~username/ PHP won’t run if you call it by this URL  

2\) Maybe you need to set the execution rights (give world right to execute it, priv’s code is 755\)  

3\) Maybe you need to fiddle with your php.ini or .htaccess files.  

4\) Maybe you need to have uploaded your file as ascii. (source code should be ASCII, not binary)


So far, I’m thinking my problem is \#1, but I won’t know until my domain name starts to work. My domain name is SuburbanDestiny.com, which I plan to use a social website, but if I change my mind, it works well as a blog domain name, or a business domain name. I don’t like that everyone keeps lowercasing my name, so suburbandestiny looks like suburb and estiny, which sounds plain weird. This could be why I’m the first to pay money for the name.


JSP works. A trivial JSP page works great. Since I’m paying extra for Java enabled pages, I’m deterimed to work JSP and Servlets into all the tweaks I make to my open source web applications.