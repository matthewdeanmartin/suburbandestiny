---
date: '2012-01-06'
recovered_from: wayback
slug: post-647
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201201\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=647
title: Customizations I used with Elmah
---


Elmah isn’t especially secure if assume the error log itself has already been breached. Even if it hasn’t been breeched, sometimes Elmah logs things that the administrator doesn’t want to know, like other people’s passwords.


There are some reliability issues too.


**1\) Don’t log sensitive data.**  

\- Some data is well known, e.g. HTML headers  

\- Some data is not well known, textboxes were you enter your password  

\- Viewstate for the above  

2\) **Don’t refer to DLLs that won’t exist**, for fear that dynamic compilation will fail due to a reference that can’t be found. For example the sqlite. I understand why the main project is set up this way though– the goal was to minimize the number assemblies distributed and still support lots of databases. This could also be a non\-issue. Assembly resolution, for me, has always been black magic.  

3\) **Override Email to use Apps config**, insted of Elmahs config sections in the ErrorMailModule. I don’t like doubled config settings, where my app has a setting and so does the component.  

4\) **Use Apps role system and PrincipalPermission to restrict display to certain roles**  

\- Add PrinciplalPermissions to all classes that view things (but not classes that log things), see end for a list. If you don’t trust your server admins to keep from messing up the web.config, you can put the role checks right into the code: This set worked for me.  

5\) **Stengthen XSS protections.**   

 Change Mask. and HttpUtility.HtmlEncode to AntiXss.HtmlEncode. This creates a dependency on either the AnitXss library or .NET 4\.0\.  

6\) **Add CDATA to javascript blocks**  

7\) **Switch to READ UNCOMMITTED**. The error log must not cause errors (i.e. deadlocking)  

 SqlErrorLog.cs  

8\) **When error log gets really large, it has to be rolled over and truncated to prevent locking issues**. This at least was a problem in SQL 2000 and I think SQL 2005\.


List of classes that could use a security attribute, should you choose such a strategy.


AboutPage.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorDetailPage.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorDigestRssHandler.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorHtmlPage.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorJsonHandler.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorLogDownloadHandler.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorLogPage.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorLogPageFactory.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorLogPageFactory.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorLogPageFactory.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorLogPageFactory.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorRssHandler.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]  

ErrorXmlHandler.cs \[PrincipalPermission(SecurityAction.Demand, Role \= "Admin")]