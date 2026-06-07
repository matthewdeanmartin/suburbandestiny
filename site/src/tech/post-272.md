---
date: '2007-08-26'
recovered_from: wayback
slug: post-272
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200708\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=272
title: Solving Slow start up for ASP.NET websites
---


ASP.NET websites, especially those that don’t get a steady stream of traffic suffer from slow startup.  For sites that might get 12 evenly spaced visits a day, presumably from highly interested users, you can expect all of them to get a 15 to 60 second delay before the first page loads.


This can be mitigated by:



> Pre compiling the entire web site using a web deployment project.  
> 
> 
> Turning off debugging in web.config
> 
> 
> Update your solution configuration to compile for “Release”
> 
> 
> Somehow pinging the site (see below)


I did that I start up was still slow, which proves that while compiling and removing debug symbols is probably good, its not going to be noticable, at least not for startup purposes.  I think it has to do with some extremely expensive to create object, maybe the Application object or maybe some IIS object, it isn’t obvious.


Obviously, we can’t let these applications get garbage collected or your web site will appear to be down to all but the most patient of visitors.


**RSS to the Rescue**


To restore performance you your website, you will need to add an RSS feed to it.  Add that feed to bloglines.  The ideal RSS feed reports back the time, so that the content will change on each retrieval.  The feed should be as small as possible with no optional sections and most required sections blank or minimally filled in.


You can get the real [RSS Toolkit (with asxh handlers) here](http://blogs.msdn.com/dmitryr/archive/2006/02/21/536552.aspx) (for some reason the copy I keep downloading from CodePlex lacks the ashx pattern.  Things may have changed by the time you read this)


All this page does is return the time.  Subscribe with [Bloglines.com](http://bloglines.com/) and they will ping your site every hour.


\<%@ WebHandler Language\=”VB” Class\=”RssHTenpo” %\>


Imports System  
Imports System.Web  
Imports System.Collections.Generic  
Imports RssToolkit.Rss  
Imports System.Globalization


Public Class RssHTenpo  
    Inherits RssToolkit.Rss.RssDocumentHttpHandler  
    Protected Overloads Overrides Sub PopulateRss(ByVal channelName As String, ByVal userName As String)  
        Rss.Channel \= New RssChannel()  
        Rss.Version \= “2\.0″  
        Rss.Channel.Title \= “tenpo”  
        Rss.Channel.PubDate \= DateTime.Now.ToUniversalTime().ToString(“r”, CultureInfo.GetCultureInfo(“en\-US”).DateTimeFormat) ‘”Tue, 10 Apr 2007 23:01:10 GMT”  
        Rss.Channel.LastBuildDate \= DateTime.Now.ToUniversalTime().ToString(“r”, CultureInfo.GetCultureInfo(“en\-US”).DateTimeFormat) ‘”Tue, 10 Apr 2007 23:01:10 GMT”  
        ‘Rss.Channel.WebMaster \= “webmaster@email.com”  
        Rss.Channel.Description \= “tenpo ni”  
        Rss.Channel.Link \= “\~/tenpo.ashx”


        Rss.Channel.Items \= New List(Of RssItem)()  
        If Not String.IsNullOrEmpty(channelName) Then  
            Rss.Channel.Title \+\= ” ‘” \+ channelName \+ “‘”  
        End If  
        ‘If Not String.IsNullOrEmpty(userName) Then  
        ‘Rss.Channel.Title \+\= ” (generated for ” \+ userName \+ “)”  
        ‘End If


        Dim item As New RssItem()  
        item.Title \= “tenpo ni”  
        item.Description \= DateTime.Now.ToUniversalTime().ToString(“r”, CultureInfo.GetCultureInfo(“en\-US”).DateTimeFormat) ‘”Tue, 10 Apr 2007 23:01:10 GMT”  
        item.Link \= “\~/tenpo.ashx”  
        Rss.Channel.Items.Add(item)  
    End Sub  
End Class


 


‘ Slow startup— be gone!