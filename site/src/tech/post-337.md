---
date: '2008-03-28'
recovered_from: wayback
slug: post-337
source_file: data\normalized\tech.wakayos.com\root\__query__\p\337\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=337
title: 'Pervasive Integration Architect: Dealing with workspaces'
---


Workspaces were invented by a misanthropist so that your collection of source code files would never be able to find each other. If you are familiar with Visual Studio, workspaces \+repositories roughly correspond to fuction served by solution files and project files.


**Detecting something is wrong**. The first sign you will get of something being wrong is failing to find the macrofiles. When a process designer file is open, going to tools/macros should bring up the right macrofile (i.e. the one that has the right connection strings, etc) Validation does not check for this. Since macros are buried in property pages, it won’t be visibly obvious if the macro file the IDE is pointed at doesn’t go with the currently open process designer file.


**Undoing the damage**. There are literally billions of UI deadends in the IDE, making the proper way to open a process designer file nearly undiscoverable.


\- File/Manage Workspaces


\- Click the down pointing triangle next to the “Workspaces Root Directory” dropdown. The tool tip is “Changes Workspace Root Directory”


\- Find the directory that is **one level above** “Workspace1″ Workspace1 may be named something else, so you may have to look for the folder than has a “xmldb” folder in it.


\- Don’t forget to double click. The property page is poorly designed, i.e. selections made in the visible tree don’t commit until you double click. Also, you can’t just type in the path of the ‘workspace root’


**Verifying the selection in “Workspace Manager”.** 


Expect the repository to say something like “xmldb01″, “FILESYSTEM”, “./xmldb”


Expect the workspaces to say something like “Workspaces1″


Expect when you open something to find the open dialog’s “Look in” section to say:


xmldb:ref:///{YOUR WORKSPACE ROOT}/Workspace1/xmldb


Open a file and double check that the macro file has the expected values and appears to be the one at {YOUR WORKSPACE ROOT}\\Workspace1\\macrodef.xml


**UI Dead Ends.** It is possible to have multiple repositories, multiple workspaces open. The semantics are unclear and it isn’t clear what macro file you will end up using. In any case, you should avoid features that rely on having multiple workspaces, repositories active at one time if for no other reason than maintenance developers won’t be able to figure out what the hell is going on.