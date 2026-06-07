---
date: '2006-06-02'
recovered_from: wayback
slug: post-140
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200606\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=140
title: SSIS Packages and Shared Configurations
---


I have a lot of packages, not all have the same set of connection objects. When I try to let them share the same connection file, I get error messages that say the package might be corrupt because the config file mentions a connection that isn’t in the package. This is getting very aggravating, I’m seriously considering falling back to handwritten configuration code that would read from an .ini.


If a shared config file has 20 configuration items in it, then you have to create 20 objects in every package that uses the config file, even if that particular package uses only 2 of the configurations. And if there were two packages that had the same 20 components, then it probably would be a good candidate for merging into a single package.


Another anti\-pattern would be creating a configuration file for each package.  Since these, say 20 config files mostly have the same information (the names of our 3 favorite servers), this is a lot of duplicate code.