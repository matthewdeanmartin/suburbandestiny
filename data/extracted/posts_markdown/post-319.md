---
date: '2008-01-31'
recovered_from: wayback
slug: post-319
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200801\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=319
title: Learing about ASP.NET output caching
---


How it works  

You add a directive, something like


\<%@ OutputCache Duration\=”3600″ VaryByParam\=”none” %\>


The page then puts the HTML output of the page or user control into the Cache object.  Next time you get a request, the rendering engine loads a cache control instead, something like an HTML literal that gets it’s data from cache.


To test your caching strategy, load your pages twice.


Gotcha: When the control come from cache, you can’t reference that control.   

So all the code behind that references the control need to check to see if the control exists (is equal to null or Nothing)


Gotcha: When you dynamically load a control, it isn’t the same data type if it came from cache


myUC \= LoadControl(“\~/MyUC.ascx”)


If the control came from cache, it isn’t of type, MyUC, it is a cached control.


Gotcha: Code behind in the user control doesn’t run when a user control is loaded from cache.  For example, if your control needs to register a JavaScript or CSS file (which requires modifying the parent pages \<head\> tag), it won’t run.


Gotcha: Tilda URL’s stop working.    

If you reference an image by something like:


    ImageUrl\=”\~/images/mypic.png”


The first time this is rendered, it will calculate the correct relative path.  If this is called again from say a subfolder, it will use the relative path that was correct for the page that called it first.


Gotcha: Programmatically clearing the cache requires adding a dependency to EVERY page and user control.


(I think changing web.config will also clear caches, but this is heavy handed)


General pattern for a cache clearing system: (Ref. <http://aspalliance.com/668>)  

    Create a dependency object on application start.  

        HttpContext.Current.Cache.Insert(“Pages”, DateTime.Now, Nothing, \_  

        System.DateTime.MaxValue, System.TimeSpan.Zero, \_  

        System.Web.Caching.CacheItemPriority.NotRemovable, Nothing)


    Make all pages inherit from a custom page class,  e.g.


        Public Class SmartPage  

            Inherits Web.UI.Page  

     

    In the load event add this:  

       Response.AddCacheItemDependency(“Pages”)  

        

    On an admin page, put this behind a button:  

       HttpContext.Current.Cache.Insert(“Pages”, DateTime.Now, Nothing, \_  

            System.DateTime.MaxValue, System.TimeSpan.Zero, \_  

            System.Web.Caching.CacheItemPriority.NotRemovable, \_  

            Nothing)


When to Use  

So far, given these gotchas, Output caching is best for:


Simple pages (easy to see what the dependencies are)  

Almost static pages (especially if the dynamic parts are derived from slowing changing files, like web.config)  

Completely static pages, such as document oriented pages.


When the page is complex, you may need to switch to data caching, where you cache smaller objects, like dataset that holds a state list.  Caching at an user webcontrol or page level might cause some of the gotchas I’ve mentioned, especially if the state list is on an otherwise highly dynamic page.