---
date: '2007-09-01'
recovered_from: wayback
slug: post-274
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200709\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=274
title: 'Authentication Mystery: When Membership.GetUser is null'
---


When Membership.GetUser is null or nothing, but login succeeds (and fails on a bad password), check the path as such…


\<authentication mode\=”Forms” \>  
    \<forms …  
               path\=”/”   
               …  \>              
\</authentication\>


Mine was set to path \=”blahblah/blah”.  I changed it to “/” and things worked again.


Has something to do with browsers rejecting the cookie because it didn’t look like it was coming from the right server.