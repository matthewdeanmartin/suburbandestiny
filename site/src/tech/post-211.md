---
date: '2007-05-07'
recovered_from: wayback
slug: post-211
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200705\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=211
title: Overview of Code Generation in the .NET World
---


Code generation is hand for common coding patterns, like the half dozen lines of code you for a class property. This will save you minutes of labor.



Code generation is really useful for meta\-data drive programming. For example, if you have something that is a database, or looks like one, you may find yourself writing code to do the same half dozen operations with each table, such as fetch by primary key, insert, delete, update, undo an update, update within the context of a transaction, check for string lengths, and so on. Dynamic code that figures out how to do this at run time, for example, Fetch(table\_name as object, pk\_value as object) as object means you are working with late bound data types and it is potentially very expensive to look up the metadata on each call. It would be more efficient to code generate the tables and call Account.Fetch(pk\_value as integer) as Account. And obviously either one of these patterns is more efficient than writing by hand the dozens of lines of code that it takes to fetch a row from a table and fill a business object.



Three big business object frameworks include CSLA, Subsonic, and .nettiers. CSLA and .nettiers are big frameworks with lots of fancy features. Subsonic is a relatively simple framework. It probably is better to pick any of the above than to try to write one’s own.



Metadata drive code generation is also a type of Object Relational Mapping (ORM). There is a “ORM impedance mismatch” between how the world looks from the standpoint of a relational model and an object oriented one. Sometimes the code generation frameworks do are able to translate from a database schema to objects without a change in semantics, sometimes not. For example, .nettiers can’t deal with tables with composite foreign keys.



To get code generation to work, you may have to adapt the templates or change the schema. If you have the luxury of completely rewriting your schema or if you don’t care what the database schema looks like, you might at this point decide to drop code generation and instead use nHibernate or the like, which takes the opposite approach—you write business objects and nHibernate decides how to save them to a database.



Code generation can be done in any language, although JSP/ASP like languages seem to be the preferred way to generate code. Template languages like to mix inline code in document templates. XSLT is an also ran that a bit hard to write. Microsoft itself uses CodeDom, which is like the HTML DOM, except the document is a .NET source file. It also has a reputation for being hard to write.



CodeSmith is almost just like ASP.NET and the code templates in Subsonic are ASP.NET pages. They are ordinary aspx files with source code instead of HTML around the golden nugget—(the inline code).



Code generation will become part of the build process, so a final component of a code generation is editing the nant or msbuild files to include the build. Both are a type of a script language with xml syntax. MsBuild is used by Visual Studio 2005, but nant has more features. MS\-build’s feature list is more competitive once you include : <http://msbuildtasks.tigris.org/>