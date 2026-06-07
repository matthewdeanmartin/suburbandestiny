---
date: '2011-06-13'
recovered_from: wayback
slug: post-620
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201106\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=620
title: Mobile Development and ASP.NET Websites
---


I’ve been ignoring mobile development for the last decade. I have never been rich enough to buy the 300 phones necessary to do WAP development (a prerequisite for creating “hello world” that works across two phones). But iPhones, iPad, iPods and Androids over 3G change things. The network is fast enough, the UI conventions that Apple created make things worth looking at again. Since iPads can read random websites and render them pretty well, you’d think you could take conventional webapps and port them to iPhone/iPad Etc. You will want to use a library that will give you a iPhone theme and widgets, such as jQTouch, iUi or others. But those libraries all fall on their face to varying degrees if you browse them in MSIE (no surprise), Chrome(!), and Firefox. I didn’t check Safari, but I’ve read that many of these iphone targeting framework fail on desktop Safari, too.


You still have to write two websites, testing in two browsers. The only browser that behaves similar enough to an iPhone is [iBB (download here)](http://www.puresimstudios.com/ibbdemo/)


There is only one library that doesn’t fall on it’s face in MSIE, that’s [ComponentOne’s iPhone component library](http://www.componentone.com/SuperProducts/StudioiPhone/). But it costs about a grand. Performance seems sluggish, but that may just be the demo site– production code might be faster (fewer elements for one)


Also, (all?) the libraries seem to encourage MVC style programming. iUi for one, puts multiple forms on a single page, something that non\-MVC ASP.NET can’t easily cope with.