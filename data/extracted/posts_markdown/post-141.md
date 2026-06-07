---
date: '2006-06-02'
recovered_from: wayback
slug: post-141
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200606\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=141
title: UI Options For SSIS
---


1\) No user interface.


2\) BIDS as the user interface.  Very flashy, dramatically reduces performance.


3\) Windows forms through scripting task


The first technique I’ve used involved:


Creating a windows form in VS2005\.  Add a public property for communicating with the calling script.  Copy the code for the partial class and the code behind class to a single class, put it in the Scripting window.  Add a reference to System.Drawing.  Add import statements for System.Windows.Forms \& System.Drawing.  Make initialize components visible.  

New up the form class, call intialize components, and .Show()


Add a Do/While loop, with a System.Windows.Forms.Application.DoEvents()  keep the script from exiting and closing the form and to let the window respond to events while polling the public property on the form.


Some day I should rewrite this entry and make it more clear.