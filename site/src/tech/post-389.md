---
date: '2008-07-25'
recovered_from: wayback
slug: post-389
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200807\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=389
title: MS Build Fortune Cookie Manual
---


**Jargon**


PropertyGroup \= Variable declarations  

Task\= Statement/Method Invocation  

Import \= Reference/Include/Using statement  

Target \= Code Bock/Subroutine


**Control of Flow**


Code runs once. So if a project has 10 dependencies that need to be compiled, and other projects depend on some subset of those, they won’t be rebuilt. I think this is what makes a build script different from an ordinary script, like a ps or bat file.