---
date: '2008-03-07'
recovered_from: wayback
slug: post-331
source_file: data\normalized\tech.wakayos.com\root\__query__\p\331\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=331
title: 'Notes: SQLite for ASP.NET'
---


Why. Safer than MS\-Access. Doesn’t require your hosting account to have any JET drivers for MS\-Access. Simpler than SQL Express User Instances. Doesn’t require understanding or doing the MS\-SQL administrative steps. Doesn’t even need a ODBC DSN to be set up.


**What**. The [SQLite ADO.NET Provider](http://sourceforge.net/projects/sqlite-dotnet2).


How.  

How to configure the Data Provider


From documentation, add this to web.config.


\<configuration\>  

\<system.data\>  

\<DbProviderFactories\>  

\<remove invariant\=”System.Data.SQLite”/\>  

\<add name\=”SQLite Data Provider”  

invariant\=”System.Data.SQLite”  

description\=”.Net Framework Data Provider for SQLite”  

type\=”System.Data.SQLite.SQLiteFactory, System.Data.SQLite” /\>  

\</DbProviderFactories\>  

\</system.data\>  

\</configuration\>


Add System.Data.SQLite.DLL to \\bin\\


Add your SQLite data file to \\App\_Data\\   The framework will not server files in App\_data, so the data will be safe from a user downloading and looking at your data directly.


You do not need to add any other files to the target server! Even though SQLite is a C/C\+\+ based data access API, the System.Data.SQLite.DLL file has everything it needs. It does to interop calls, so the website will probably need to be trusted enough to do interop. It seems the C dll is compiled into the .NET dll, something I didn’t know was possible.


To connect, it helps to have the full file path:


\<connectionStrings\>  

\<add name\=”ConnectionString”  

connectionString\=”Data Source\=d:\\hosting\\mywebbsite\\App\_Data\\data.s3db;New\=False;Version\=3″/\>  

\</connectionStrings\>


The code is straight forward…  

Imports System.Data.SQLite


Partial Class \_Default  

Inherits System.Web.UI.Page


Protected Sub Page\_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load  

Dim con As New Data.SQLite.SQLiteConnection  

con.ConnectionString \= ConfigurationManager.ConnectionStrings(“ConnectionString”).ConnectionString  

Dim com As New Data.SQLite.SQLiteCommand  

con.Open()  

com.Connection \= con  

Dim t As SQLiteTransaction \= con.BeginTransaction()  

com.CommandText \= “SELECT \* FROM Test”  

Me.gvSampleData.DataSource \= com.ExecuteReader  

gvSampleData.DataBind()  

t.Commit()  

con.Close()  

End Sub  

End Class


SQLite Membership Provider. [One exists. I haven’t used it yet](http://www.eggheadcafe.com/articles/20051119.asp).  That one has support for Membership and Roles.  I’m still looking for something with profiles support.  The other ASP.NET 2\.0 database things would be SQL Session and Webparts, neither of which are anything you’d likely do with a small database anyhow.