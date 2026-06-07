---
date: '2008-02-27'
recovered_from: wayback
slug: post-327
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200802\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=327
title: 'Notes: Pervasive Data Integrator Repositories'
---


Pervasive (which I keep wanting to call Perversion–makes for funny meetings), has this filesystem abstraction layer between the IDE and the filesystem called the repository.  It is the single greatest barrier to starting to use the IDE.


\[Punchine: the repository/workspace/collection system is so that source code files can find each other after the root directory changes.  Finding data files on the filesystem after the root directory changes requires using macros, such as ($data\_directory)...now back to my notes.]


First the jargon from the “Getting Started”:



> Workspace – “a portable, user\-defined residence for the definition of Repositories”


Huh? Does it have a handle?  Ok.  Undefined object workspace contains undefined objects repository. I think this is a collection of pointers to the directories that hold your source code.



> Repository – “a user\-defined area where Transformation and Process files are stored”


Sounds like a folder or directory.



> Collection – “a subdirectory under Repository”


Sounds like a subdirectory.  Personally, I think all commonly used concepts should be renamed in Esperanto or Icelandic but Workspace, Repository and Collection are fine.


The repository explorer is a combination of a filesystem explorer.  The Repository manager is more like a filesystem explorer and a XML document browser.  The repository explorer will launch the relevant part of the IDE when you click on a file.  The Repository manager will let you drill down into the XML document, which can be very tedious with large XML documents as you must click \*every\* node to view the XML document this way.


The connection string to the repository looks something like


xmldb:ref:///c:/folder/folder


If you change the file system without updating the repository, you won’t be able to open anything.  Sigh.  I think this can be worked around by creating a new repository reference.


Where were they heading with this idea?


**Deployment.** They wanted to make change management easier.  So documents would be referenced relative to a “Workspace/Repository/Collection”.  When these were moved, you would update something to tell the environment where the worksspace/repository/colllections were and you’d be running again. Kind of like setting a path in a .ini or .conf file, but more complicated.


**Change detection.**  Repository manager has some reports for searching for recently changed files and other statistics. 


**Version Control.** Repository Explorer has a CVS and VSS feature. Haven’t grokked it yet.