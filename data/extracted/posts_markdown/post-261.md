---
date: '2007-07-25'
recovered_from: wayback
slug: post-261
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200707\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=261
title: Using Random in ASP.NET
---


In C\# and ASP.NET you can generate random numbers like this:


 Random r \= new Random(System.DateTime.Now.Millisecond);


 double d \= r.NextDouble();


But, in an stateless ASP.NET world, you will get the same random number generator starting over at it’s pseudo\-random beginning each time the page posts back and you create a new Random object. To keep a random number generator moving forward with new random numbers, use something like:


 public static double roll() {


 Random r;


 if (HttpContext.Current.Session\["r"] \=\= null)


 {


 r \= new Random(System.DateTime.Now.Millisecond);


 HttpContext.Current.Session\["r"] \= r;


 }


 else


 {


 r \= (Random)HttpContext.Current.Session\["r"];


 }


 


 return r.NextDouble();


 }