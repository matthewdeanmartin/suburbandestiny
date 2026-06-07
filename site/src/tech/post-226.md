---
date: '2007-06-16'
recovered_from: wayback
slug: post-226
source_file: data\normalized\tech.wakayos.com\root\__query__\p\226\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=226
title: More Notes on AzMan- An inconvenient interface
---


When creating an authorization store, make sure you are in Developer mode– Action menu, options, developer mode. Every time you open the azman console, it resets back to administrator mode.


The context menu changes for each node. Top node, you can create a new store, next node you can create an application, next node you can create a user group. These actions are not duplicated in the menu system, so if you were searching the menu’s, ha ha! Fooled you.


You can’t create two applications that differ only by version. So if you do have two applications running at the same time, you ahve to give them two names, like App1 and App2\.


The “Role Definition Properties” page is some what non\-intuitive. The Definition tab has two means:


\- What the role can do


\- What other roles the role is a member of


The difference between Groups and Roles is not clear. They appear to be the same concept, except Groups can be formed from an LDAP query and Roles appear to be strictly nested (i.e. they hold groups, but not individuals) Forcing all roles to nest by at least on level implies to me that there are going to be a lot of degenerate roles (that have exactly one group in them).


And finally it looks like AzMan can only talk to an Activite Directory, Local or Adam authentication store. This is quite a bummer if you were thinking of using AzMan on a hosted website where the account is likely to be running the application under a service account.


I think the one thing I don’t like about this user interface, is that there is nothing in the user interface to suggest what is a suitable operation, task, role or group. When I first started dinking around with the application, I kept wanting to so something like create a operations and tasks with the same name and to create roles and groups with same name. (or worse, confuse roles/groups with operations/tasks)


Another point of confusion I blame on the UI is the scope of the group depends on where it is in the tree. It would have be nice if there was a 2nd attribute on the tree to just state the scope rather than make me infer it from where it is.


Ok, exercise for the reader, rewrite the UI so that all operations can be performed using traceable powershell scripts.


Authorization Store, Application and Scope– A store holds applications, for which each is a complete set of groups, roles, tasks and operations. If your application is a two headed beast, say half store, half customer blogging engine, then you might want to keep separate your roles strategy for the store and the blog. Or you might want to set these up as two different applications. So far the only advantage I can see to having several scopes vs several applications is that you get an additional set of roles with a ‘scope’ that extends over several azman scopes. Ugh, can’t we invent some new jargon instead of reusing jargon that already has well defined meanings?