---
date: '2008-09-25'
recovered_from: wayback
slug: post-453
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200809\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=453
title: try/finally without catch
---


You will get a YSOD, but the finally block executes before the YSOD.  

 `try  

 {  

 int bar = 1 / int.Parse(this.TextBox1.Text);  

 int z = 21;  

 z++;  

 }  

 finally  

 {  

 int foobar = 1 + 1;  

 }`  

This is kind of like a IDisposable patter at the method and code block level. It means, on the way out of this code block, I want some clean up code to run. Off hand I can’t think of a good reason for this if you aren’t releasing resources. Using it as a control of flow technique looks very iffy especially if it wasn’t the error you were expecting.


Identical behavior to the above, YSOD, but finally block runs just before the YSOD. The following is code you’d see in code generation scenarios where the try/catch/block is code generated with the hope that the developer would fill better error handling later.  

 `try  

 {  

 int bar = 1 / int.Parse(this.TextBox1.Text);  

 int z = 21;  

 z++;  

 z++;  

 z++;  

 }  

 catch (Exception) {  

 throw;  

 }  

 finally  

 {  

 int foobar = 1 + 1;  

 }`


YSOD after line one, no other code after the error is executed  

 `int bar = 1 / int.Parse(this.TextBox1.Text);  

 int z = 21;  

 z++;  

 z++;  

 z++;  

 int foobar = 1 + 1;`