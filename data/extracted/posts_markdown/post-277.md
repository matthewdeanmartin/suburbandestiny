---
date: '2007-09-07'
recovered_from: wayback
slug: post-277
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200709\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=277
title: 'Getting Subversion to Work: Tips'
---


**Apache Server**. Don’t change versions. Changing versions is a super\-duper\-ultra\-advanced user scenario. Mere super geniuses shouldn’t attempt. Use the version that comes with the Collabnet subversion installer. (The blank URL warning the installer gives you means it doesn’t want http:// in the field.) In fact, this is probably a good idea for all LAMP stack applications—it’s better to have a dozen LAMPs that work than a dozen broken apps using the same LAMP.



**The Passwords.**


htpasswd.exe \-cs passwords.txt matthew  
pause



**The Location.**  The location should look something like this. Ideally you want this over https, but getting apache to run https is a pain.



\<Location /svn\>  
 DAV svn  
 SVNParentPath c:\\svn



 AuthType Basic  
 AuthName “Vienna Subversion Repository”  
 AuthUserFile “C:/Program Files/CollabNet Subversion Server/httpd/bin/passwords.txt”  
  
 Require valid\-user  
\</Location\>



**SSL**. SSL is fairly hard. Your first goal will be to get SSL to work with any certificate at all. The next goal will be to get the SSL certificate to match the URL, expiration date and so on. Even if you get rid of the expiration and URL errors, you will be dogged by certificate authority warnings until you pay money for an SSL cert, which is not worth it.



**Checking Out/Checking In Code**. Use a combination of Ankh and Tortoise.