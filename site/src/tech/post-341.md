---
date: '2008-04-07'
recovered_from: wayback
slug: post-341
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200804\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=341
title: Live blogging Talend Studio
---


Cheap skates will want to know, exactly was is the difference between the free and commercial version? Or more concisely, does the free version have enough to get my job done?


\[Speaking of being cheap...you still might want to consider the paid version just for the service...while I was writing this a Talend sales rep called up. We talked about what projects I was working on and he told me about joblets, a feature I had just been looking for in the documentation! Talk about a world of difference compared to how Pervasive treats me!]


**Version**. I’m reviewing version 2\.0\.2, latest version is 2\.3\.


**Data Connections in** **Free Version**. These widgets represent the E and L in ETL. Talend has ODBC, MySQL, Oracle, Postgres, SQL Server, and Sybase. That is enough to connect to most RDBMS’s on the market. The Postgres, Oracle and MySQL connectors also support bulk transactions (i.e. using the RDBMS proprietary tools writing directly to to tables bypassing the SQL database engine)


File wise, it can connect to Excel, LDIF (an LDAP format), Email (as a file!), XML.


Textwise, it can deal with delimited by Regex, Position, CSV and other delimiters.


**Paid Version**. Lots more native database and file access.


**Task/Step Widgets**. In an ETL package, ETL widgets are fun, especially if they interact with the ETL environment. Task/Step widgets don’t strongly interact with the ETL environment are not so interesting, lets see how the built in ones rate. For example, a widget that executes a SQL statement or a shell command is not very exciting as batch files, powershell and sqlcmd files do that better and more clearly. Never the less, these are common ETL programming patterns.


RunTask runs an additional Talend package. System is a shell command widget. I may be just dumb, but so far I can not find a Java code step widget.


The file zipper is nice, but even more interesting is you can see the Java code that it represents. A non\-dataflow job step is kind of like a code generation template. When it isn’t obvious how to set the properties, you can examine the source code. For example, when using the file zipper, it wasn’t immediately obvious if the slashes in a windows path should be forward or backward or if the property needed to be wrapped in quotes. From code inspection, it was obvious that the directory property needed to wrapped in double quotes with forward slashes.


**Datapipe/Dataflow/Transformation Widgets**. These widgets affect the data as it flows into and out of the ETL package and are very interesting. Talend calls these “Intermediate Steps,” as they require an input and output data flow.


The free version includes these widgets: Aggregation. Java code transformation. Sorting and External sorting. External sorting is using an external program to sort the data. Unique\-ify rows (discard duplicate rows).


Filter, denormalize, replicate and unite appear to be paid processing components, so if you are using the free version, you’d have to do this by other means, either a Java code component (which would be simple for the filter), or temporary tables or… this Map thing.


The Map component is a very interesting component that can filter and split data flows. I haven’t figured out if it can do unions. The GUI for this widget is very rich. Although some settings take some trial and error, at the end you can refer to the code view to see if it represented your intent correctly.


And somewhere there must be a lookup widget…


**ELT**. ELT, as far as I can tell, means instead of doing JDBC or OleDB inserts, you generate SQL INSERT statements. If I get the intent correct here, this shifts the burden of transformations onto the target server. So column TRIM’s and the like could be done by MySQL instead of the Talend transformation engine. Not sure if I’m right about that yet…


**Expressions and Functions**. This is about the T in ETL. Expressions are done in java in the Map dataflow widget. \[there is more, but I'm out of time today]


**Control of Flow**. The expected “if sucessful/if fail” lines. \[there is more, but I'm out of time today]


**Query Designer**. Ok. Joins were unguessable until I read “You can also very easily create a join between tables. Right\-click on the first table columns to be linked and select Equal on the pop\-up list, to join it with the relevant field of the second table.” However, I still haven’t found a way to automatically generate the Schema from a query. I can retrieve meta data for tables and views, but not custom queries. Apparently I can’t find the right button or Talend isn’t executing a SET **FMTONLY** ON to retrieve the metadata. Intellisense in the query designer is genius, not a lot of query designers have intellisense yet. Lazy person that I am, I create views and retrieve the metadata so I don’t have to type the metadata myself.


**Exporting**. You can export the whole thing as stand alone java code. DTS used to be able to something like this with vbscript.


**Summary.** Being able to see the source code of a built in component as you click on it is genius. Being able to do side by side compares of two versions of the same package is genius.