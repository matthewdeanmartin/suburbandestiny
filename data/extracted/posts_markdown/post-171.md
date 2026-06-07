---
date: '2006-08-15'
recovered_from: wayback
slug: post-171
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200608\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=171
title: Actually trying to use MS-Words HTML editing is not a good idea
---


I was determined to use MSWord for my website’s frontpage.  It was a time consuming determination.


Here is some advice in case you are crazy enough to try it:


Enable the view script icon. (You have to add it to the menu bar, then enable view script, then double click on the script icons to edit the script)


Set up a custom php.ini file which overrides default php.ini.  It needs to say asp\_tags\=1\.  This will allow you to use the \< script language\=php \> tags. Without these tags, Word will reformat your php turning it into a mess you can’t read and the interpreter will reject.


Set up tables with relative measures (20% of screen, etc)


Links should be full URLS.  Word gets confused with relative URLs.  Normally relative URLs are a best practice, so that you can move your website around without changing every link.


Turn off smart quotes, dont use the single character version of … or the single character em\-dash from word.  They don’t always show up correctly in HTML browsers.


The HTML is still a mess.  One solution is the [Microsoft tidy tool.](http://www.microsoft.com/downloads/details.aspx?FamilyID=209ADBEE-3FBD-482C-83B0-96FB79B74DED&displaylang=EN)  One solution is [HTML tidy](http://www.w3.org/People/Raggett/tidy/).  One other solution is a [PERL HTML tidy script](http://dev.w3.org/cvsweb/2002/cleanwordhtml/cleanwordhtml.perl?rev=1.5).


Here is some explanation on why [MS\-Word HTML looks so screwy](http://www.helical-library.net/desk/hg_word.asp).  Manually tidying a Word document is not worth the effort, unless it is a one time conversion, not very useful if you intend to do any further work in MS\-Word.


Also, use the Styles feature of Word.  In case you don’t use styles, a style is a bundle of font family, size, weight, etc.  If you don’t use a style, word will wrap every single paragraph with bulky formatting code.  If you use styles, Word will use CSS and merely wrap every single paragraph with a named CSS style, which is a better practice.