---
date: '2007-02-15'
recovered_from: wayback
slug: post-201
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200702\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=201
title: Moving Bits Faster
---


Everyone has to move files every once in a while. You might have two machine both with high speed internet connections, but maybe the connection is an unreliable VPN connection, or maybe it is just a very large file. For some reason, windows file shares across VPN just isn’t has high performance as you might want and there is very little that can be done about it, except zip it.


**Get 7z.** 7z currently has the best compressions ratios of almost any format, it is free and very fast. CPU nowadays is cheaper than bandwidth.


484MB\-\>31MB So I’m going 15 times faster. But download with file shares over VPN is at 40Kb/sec


Get “**Get Right**“. Get Right is a file download manager. It has an accelerated mode where it opens 4 connections and downloads the file in four parts. It can also talk “Z mode” to FTP servers. “Get Right” costs money, though. And it does resume. And so forth.


Get **Filezilla Server**. Filezilla is free, supports Z\-mode compression and FTP clients that accelerate by using multiple connections.


Bam, 86 Kb/sec and I was able to resume when the VPN connection died.


All together, Compression\+FTP\+FTP download managers can increase your bit throughput by 30x (neglecting compression and decompression time , which in my case was about a minute or two at 2MB/sec\-6MB/sec.


Now what I’d like to hear is, what’s up Microsoft? Why can’t SMB file shares work like that?


Apparently I’m not the only one that has noticed that [SMB performance is subpar](http://www.netpredict.com/solutions/usecases/fileshare.htm). And [Microsoft has mostly been comparing SMB against Samba](http://www.oreilly.com/catalog/samba/chapter/book/appb_01.html). A protocol and a reverse engineering of the same protocol are likely to perform similarly. One of the key finding I see from these links is that there are not a lot of things a computer pro can do to tune SMB, while there are several compression and FTP tools.