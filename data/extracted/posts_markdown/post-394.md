---
date: '2008-08-12'
recovered_from: wayback
slug: post-394
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200808\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=394
title: Built in Exceptions you should use
---


I’ve been using FxCops which looks down on “throw new Exception();”


Here are some more narrow exceptions that already exist in the framework that you should throw, hey it saves you the effort of writing a custom error class.


ArgumentNullException – Argument is null  

ArgumentException – Argument not valid  

ArgumentOutOfRangeException– arguement too big or small, or not on the list  

ArithmeticException — The root of a negative number  

InvalidOperationException \-given state,