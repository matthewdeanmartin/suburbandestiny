---
date: '2003-10-15'
recovered_from: wayback
slug: post-95
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200310\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=95
title: XSL Pains
---


Usually you want to format either the text inside of a set of elements or the value of an attribute in a set of elements (usually a repeating element). This poses two problems, what is the best way to identify the the set of elements and what indicates which values you want.


1. To get the data, try : `value-of select="."` or try `value-of select="text()"` or for an attribute you use `value-of select="@attributename"`  

I haven’t figured out how to get the data inside an attribute value that was indicated by the XPath expression (the way value\-of select\=”.” works)
2. To point at the data you want use an XPath express. First try just the bare tag name `template match="myTag"`  

If that doesn’t work, try absolute naming `template match="/root/row/myTag"`  

If that doesn’t work try relative naming, `template match="row/myTag"`  

If that doesn’t work try wildcard naming, `template match="row/*"`
3. For some reason, I can’t get /@\* to work. (Gee that expression kinda looks like a comic book curseword)