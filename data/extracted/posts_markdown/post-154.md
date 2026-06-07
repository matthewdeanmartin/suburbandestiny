---
date: '2006-07-24'
recovered_from: wayback
slug: post-154
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200607\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=154
title: 'SSIS: Import Export Table Wizard'
---


The new wizard is opaque.  Just by looking at the package, you can barely figure out what is going on. The “Transfer Task” has no designer. The file connections can’t be viewed without firing up notepad.  To get the list of tables included, you have to open and search TableSchema.xml You can’t see the progress of the table copies.  And finally, the UI isn’t friendly.  On my first attempt I ended up with my project in the TEMP folder, files had seemingly randomized names.


Grr, makes me want to go back to bcp and INSERT INTO