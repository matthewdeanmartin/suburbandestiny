---
date: '2009-11-14'
recovered_from: wayback
slug: post-588
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200911\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=588
title: ASP.NET MAF plugable website working
---


The plug in needs a way to talk to the host app. In ASP.NET, this means things like updating the UI by adding controls, etc. In fact, since in ASP.NET only creates pages, you will eventually have to talk to Page. The host Page isn’t serializable or remotable, so if your Contract has a Page, you won’t be able to create the Add in in a separate AppDomain, i.e. no sandboxing or other isolation, at least not directly. Fortunately, we like to write code and can solve this by writing another layer of indirection.


What I tried next was creating a set of Page and Control wrappers and factory functions. I called the add\-in\-side wrappers “Recipes” because they where recipes for building controls and recipes for building pages. The new contracts no longer had references to System.Web since no WebForms types there seem to be remotabe. In the hosting application I wrote a “Page Automator”, whose job was to implement recipes recommended by the Add\-In and to describe the page for the Add\-In by looping through the controls, putting their current state into a wrapper and then providing it to the Add\-In.


Finally, out\-of\-AppDomain Add\-In activiation works. And I was able to run the add in in minimal trust. If you’ve ever tried to get a non\-trivial website to run under medium trust, you know this is just incredible! I gave up on medium trust because too many of my third party components didn’t play the medium trust way. In a medium trust website, everything in the AppDomain (i.e. the entire website) must refrain from calling forbidden APIs. As soon as there is a single line of code that requires Full\-Trust and if you can’t remove it or change it (because it is both necessary and 3rd party closed source), you have to bump the entire website up to Full Trust. Unless you are using Add\-Ins.


The plug in may need to communicate several things at once in the AddIn’s interface. System.AddIn makes this very, very hard. I tried string\[]. I tried List. I tried IListContract. They all failed. When I used IListContract, the pipeline generator generated interfaces of type IList, and then the addin finder stopped finding addins that supported the contract. Humorously, string\[] failed because System.AddIn said string\[] wasn’t serializable. WTF? These are strings. I finally decided to use Control NextControl(); as a signature to return a collection one at a time. I finally did get IListContract to work, but the type of T needs to be remotable.