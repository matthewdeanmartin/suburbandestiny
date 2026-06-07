---
date: '2007-06-17'
recovered_from: wayback
slug: post-228
source_file: data\normalized\tech.wakayos.com\root\__query__\p\228\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=228
title: Top 10 Reasons Why You Should Use AzMan
---


1\. **You don’t have to write your own authorization scheme**. (But you don’t get much choice either, Azman works best if you are writing an intranet application, running on XP or Windows 2000 or 2003 using windows authentication.)


\[Update, it seems you can implement "custom principles" which seems like a way to use AzMan with something other than windows authentication. The trick is to make up your own SID's.]


2\. **Freedom from the IT gnomes up the hall**. You don’t have to ask your domain admin to create and maintain groups for you (or convince him to delegate the task to you).


3\. **Freedom from Active Directory**. You don’t have to install your own subdomain controller or ADAM instance. (Unless you enjoy the pain of ADSI scripts, then by all means do so. Write it in assembler, too and sit in on a bed of nails while your at it, and chew broken glass.)


4\. **Granular security without the extra work**. Through the use of tasks, nested groups you can fight degenerate role based security (where everyone over time becomes a member of all groups) and the decision explosion (where fine grained security leads to a explosion in the number of access granting decisions an administror must make)


5\. **Centralize RBAC (role base authorization checks).** You can make access checks dependent on more than just role membership and store that code in the same place that you store your role data.


6\. AzMan is for making access checks that are typical to a business application, not a computer network.


7\. **Open.** The xml store is based on an open format. I suppose a java app could query the xml document directly. (And in longhorn, the store is in SQL tables)


8\. **Managed Code Accessible.** AzMan works with .NET and ASP.NET. And in the case of ASP.NET, you can talk to AzMan through the ASP.NET 2\.0 role manager API or the COM interop API.


9\. **Scalable.** AzMan is designed to work with big applications. While I personally think that 90% of the time a scalable application is likely to be an over engineered one, it’s reassuring to know it can process thousands of authorizations per second (\* see footnote on xml data stores)


10\. If you say it fast, it sounds like, “ass man”


**A few reasons why not**


Significant learning curve. I think this is due to RBAC being a complex idea to start with.


It is COM. Have fun trying to make sure your objects really are disposed of.


It uses VBScript for BizRules. Untyped programming without intellisense, whee…I thought that was all behind me. \[Although with some hoop jumping you can have the VBScript call .NET]


It uses xml as a database. Using any single file as a database is a recipe for inconsistency and deadlock. If you use XML, it would make sense to contrive a user group strategy that doesn’t require adding users to AzMan roles, i.e. if you could assign users to a windows group and then work only with windows groups in the xml file.  Why? So that you would never have to have users update the XML file.  But if you are using custom Auth, then you’ll have to update the file at least one per user creation.  As long as that isn’t happing every few seconds, you might be okay with XML as a database.