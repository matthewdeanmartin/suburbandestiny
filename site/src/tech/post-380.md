---
date: '2008-06-26'
recovered_from: wayback
slug: post-380
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200806\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=380
title: Setting a property that does’t exist at compile time in C#
---


Let’s say you need to set a property that won’t exist at compile time, but will at runtime, say through the magic of runtime replacing of objects.



```
System.Reflection.PropertyInfo pi = someObject.GetType().GetProperty("SomeProperty");
pi.SetValue(someObject, "new value", null);
```

In VB.NET, much easier:



```
Object o = someObject
o.SomeProperty="new value"
```