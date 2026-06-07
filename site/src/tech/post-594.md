---
date: '2010-05-31'
recovered_from: wayback
slug: post-594
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201005\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=594
title: A build server for home
---


I’ve got a WHS.  So I just finished installing:


**Subversion vs VisualSVN**.  Used AnkhSVN and checked in my code.  Installed WAMP. Found out that my windows home server for some reason had a PHP installation, so I had to update the environment variables to point to the WAMP installation.  I finally got VisualSVN to work with webSVN with windows auth.  It was tricky, required .conf file reading.  Using cygwin I got websvn working.


**TeamCity**.  Didn’t have to install Visual Studio, but did have to copy C:\\program files\\MSBUILD files.  It took an hour but now my unit tests and code coverage tools are all running.


**Issue Tracker.** Team City integrates with only 3 bugtrackers, of which only one is flat out free.  So I’ll be trying out Bugzilla, although several other bug trackers look more interesting.  Update: In frustruation, I gave up on Bugzilla because Perl is for people who enjoy configuration and installation pain and chewing on glass and poking their eyes with ballpoint pens.  I tried next the ruby and rails app “Warehouse”, but the @\#$@\#$ db scripts refused to run and I realized I didn’t have the patience to build my [own inter\-op doohicky for ruby to svn communication](http://warehouseapp.com/installing/ruby-subversion-bindings).  So on to mantis and flyspray.  Superficially, they’re closely matched.  But mantis has plugins and flyspray is more familiar to me because I’ve used it many times before.  So much work just to find out that free tools for developers often come with a heck\-of\-a installation burden.


**Sharepoint homepage.**  I’m still trying  to make WSS3\.0 sharepoint useful.  So far only the link list is useful, but I may see about taking the RSS Feeds from everything above and creating a RSS reader in WSS3\.0 to agregate my feeds which are essentially all intranet feeds.  If it frustrates me too much I’ll install a php base feed reader.