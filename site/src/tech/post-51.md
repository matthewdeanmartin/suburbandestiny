---
date: '2006-01-18'
recovered_from: wayback
slug: post-51
source_file: data\normalized\tech.wakayos.com\root\__query__\p\51\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=51
title: JScript.NET + SMO
---


This could be a cool combination– Javascript, that language we all so painfully learned just before we all realized that Javascript code can only be expected to run on one browser, plus SMO, the object oriented way to talk to SQL server. It beats some of the options, such as batch or sqlcmd. Well I don’t know about enough about sqlcmd. Or JScript.NET.


Jscript.net works at the file level, although files can now “import” a .NET assembly.


With the help of “external commands” and a customized tool bar, I quickly was able to get away from the command line and do most things in Visual Studio 2005\.  

For a Jscript.NET program, the .exe is the project. This is important to understand. If that .exe has a .pdb file (debugging symbols) in the same directory and if you open the original source code page for the .exe, you can debug that file with breakpoints, step through and all the other things you get when debugging something like VB.NET.


Not being able to do that, in my opinion was javascript greatest weakness. Just writing a bunch of alert(x) commands doesn’t cut it for a debugging experience.


Unfortunately, the greatest weakness of JScript.NET is that it doesn’t have intellisense. Might as well use C\# if you are using more than a few objects and properties.