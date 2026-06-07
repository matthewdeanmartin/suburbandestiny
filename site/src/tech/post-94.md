---
date: '2003-10-14'
recovered_from: wayback
slug: post-94
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200310\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=94
title: SQL Server & XML Forms
---


If you are in a hurry and can’t build heavyweight rich user interface forms, (like VB6\.0 forms) then you can uses a combination of XSL, XHMTL, and update grams.


Tricky parts:


1. Set up the virtual directories per BOL. Try :  

 `.../myVirtualDirectory?sql=SELECT * FROM myTable&root=sometagname`  

If your leave out the root part, you won’t get a valid XML document back.
2. To get the xml back transformed, you have to put it in a ‘updategram’ with the following in the root tag:  

 `xmlns:sql='urn:schemas-microsoft-com:xml-sql'  

sql:xsl='myStyleSheet.xsl'`
3. You have to put call your update grams like this:  

`myupdategram.xml?contenttype=text/html`  

If you don’t the browser ignores the META tag \& treats the document as XML.
4. The XML document you get back from a successful update is blank. If not, you get a processing instruction\- which is hard to transform into a pretty XHTML document. This kind of match will show the error message, but not clean it up.  

 `<xsl:template match='processing-instruction()'>  

 <xsl:value-of select="."/>`