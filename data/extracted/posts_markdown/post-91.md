---
date: '2003-10-09'
recovered_from: wayback
slug: post-91
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200310\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=91
title: XML Things I’ve learned
---


1. If you are using an XML api, no problem, you’re XML documents will be valid.
2. If you are using string concatenation, you’ll hit these problems: XML data needs to be escaped for the \& MS Access has a XML import which works nicely, but it will look like the ‘tables’ it finds in your XML file are not available for import because they are greyed out. This is actually means they **are** available for import, but you have to import all of them or none of them and you can’t pick and choose
3. MS Excel will open XML files, but it picks rather awful column names, made up of the full path (\\\\root\\myxml\\mytag) MS Access will use just the tag name for a column name. Access preserves the white space from CDATA stuff.
4. Creating a fixed width XML layout requires: a two line header, a one line footer and alternating columns holding constants that could be tricky for the other programmer to fill in. Also, one must assume that the other programmer is using unescaped ASCII. For example:  

(This looks weird because I’m too lazy to manually escape my greater thans and less thans for blogger to display them correctly)
^?xml version\=”1\.0″^  

^table^  

^row^^col1^^!\[\[CDATA ]]^^/col1^^col2^^!\[\[CDATA ]]^^/col2^^/row^  

^row^^col1^^!\[\[CDATA ]]^^/col1^^col2^^!\[\[CDATA ]]^^/col2^^/row^  

^/table^


From this we can see that the XML file can be created by concatinating 


tag \+ data \+ tag \+ data, etc.


The programmer creating the interface file need not give up the beloved fixed with layout and need only include some cryptic \& variable separators inbetween the data.