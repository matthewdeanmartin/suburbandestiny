---
date: '2007-01-08'
recovered_from: wayback
slug: post-186
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200701\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=186
title: Reporting Services and Dynamic Columns
---


If a field is not in a result set, then you can still define it manually. The report will not raise an error if that field is not in the executed result set. HOWEVER, there appears to be no way to test for that condition. IsNothing(Field!MyField.value) doesn’t appear to return anything, although some one on Experts Exchange thought so. I tried many variations on it. Aparently, if the expression tries to evaluate an expression with missing column, the whole expression evaluates to a blank or zero or sometimes ERROR\#, depeding on the partiucular expression.


Other sites recommend dealing with dynamic columns by referencing a parameter, which knows which columns are appearing:


\=cdbl(iif(Parameters!WhichColumn\=1,max(Fields(“MyColumn”).Value),max(Fields(“OtherColumn”).Value)))


This is like trying to embed the result set’s meta data into the parameter set. Ugh.