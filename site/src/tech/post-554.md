---
date: '2009-07-14'
recovered_from: wayback
slug: post-554
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200907\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=554
title: List vs Collection
---


FXCop doesn’t like List. It says use Collection \*if\* you are writing a public API and the List or Collection is exposed to the outside world. 


Why? Because Collection can be extended and List can’t. Put it another way, if use List, you’re locked into the feature set of List


How? They aren’t exactly the same, Collection doesn’t sort. You can’t cast List to Collection (at least not without making a copy, and that would be inefficient)


So this is okay:


class Foo  

{  

 public int foobar()  

 {  

 List blah;  

 //Use it, but don’t ask for it in a parameter or return as value.  

 }  

}