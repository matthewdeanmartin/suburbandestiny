---
date: '2008-03-25'
recovered_from: wayback
slug: post-336
source_file: data\normalized\tech.wakayos.com\root\__query__\p\336\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=336
title: 'Observations: Pervasive Integration Architect Process and Map Designer'
---


**If you are here, you might rather be at the [Pervasive Integration Support Forum](http://mistersql.com/tech/wp-admin/%5C%22http://www.pervasive.com/devtalk/integration/default.asp%5C%22).**  

Unfortunately, one one has answered a question there since 2005! Oh well.


**Dead Locks**  

My first attempt to test some code led to a deadlock. Clicking \[Abort] doesn’t successfully abort anything. You will have to kill the process, either in SSMS or Task Manager. Elegant.


**Default Transaction**   

By default, Sessions are “Serializable.” Serializable maximizes locking, minimizes performance and minimizes concurrency. The poorly described “Global Transaction” seems to be a way of making tasks that use that session run in a transaction that rolls back if the “Process” fails. This is different from “Run in tranasaction” in DTS, which makes a package run in a transaction.


**Integration Querybuilder**  

This is yet another query designer. For a tool that is aimed at non\-experts (the sort that don’t write their SQL from scratch), this tool is hard to set up. It isn’t smart enough to notice that you’ve already told the Map Designer what connection you are using. Instead you have to create a new connection. Today, for me, \[Query/Execute] doesn’t do anything and the tool refuses to draw the diagram for the sample query I gave it.


**Session Proliferation**  

If connection inside the map changes, on opening it you’ll be asked to create a some new sessions. If you try to change the session back to what it was, it will quietly undo that. This is GUI dishonesty. To get a session to link to the right one, you have to add the new junk sessions, delete them, open the map, and select pre\-existing sessions at that point. If you don’t manage your sessions, then the whole idea of sessions breaks down as 100′s of session objects overwhelm the session folder. It will not be obvious what sessions are actually referenced by anything without reading the XML files or a considerable about of clicking. You can get rid of the extra sessions by going down the list and attempting to delete each one. Unused sessions will be deleted, used sessions will raise an error.


Also interesting is Session orphaning.  If you rename a session, the steps that referenced that a session are orphaned and won’t be fixed until you click on the step upon which you’ll be prompted to create or attach to existing sessions.


**Connection Proliferation**  

A connection is a connection string and a table. A source table is different from a destination table. I recommend saving source and destination connections as files– however! These saved connection are templates. The resulting transformation file will not reference the original connections. Instead the connection data is copied into the tf.xml file.


**Process Navigator**  

The process navigator is a series of folders of which 3 are interesting: “Process Steps”, “Process Variables”, “SQL Sessions”. Process steps lists all the steps. Double clicking a step will bring up the property page. However, if you have a large complicated Process, then clicking on a step will not help you identify which process that corresponds to on the designer surface. Process Variables are just global variables referencable in RIFL. SQL Sessions are for active connections. If you are using SQL 2000, don’t forget you can have only 1 active result set on a connection– this means you need 2 sessions to do a table copy. In SQL2005, which has MARS, this may be different.


Queue Sessions, Iterators, Aggregators, Message Objects all appear to be premium priced features, something to do with EDI or something.