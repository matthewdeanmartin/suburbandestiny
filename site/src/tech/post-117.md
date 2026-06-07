---
date: '2004-10-30'
recovered_from: wayback
slug: post-117
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200410\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=117
title: Working with Php Dates
---


I am using Jax Calendar, a free php Calendar. I wanted to display the upcoming events on my front page, separate from the calendar module, but the date is stored as a text, something like “1096761600″, after much research, it was determined that this is the number of seconds since 1970\. If you are using MS\-Access \& ODBC, you need a function like this to convert the string to a date.


`Function DatefromUnix(strIn As String) As Date  

Dim lngSeconds As Long  

lngSeconds = strIn  

Dim datStart As Date  

datStart = #1/1/1970#  

Dim dblDays As Double  

dblDays = lngSeconds / 60 / 60 / 24  

DatefromUnix = dblDays + datStart  

End Function`