---
date: '2008-11-30'
recovered_from: wayback
slug: post-485
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200811\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=485
title: The given columnMapping does not match up with any column in the source or
  destination
---


The SqlBulkCopy object is good, but probably super twitchy. The fact that it is case sensitive to columnames to me is a sign of likely low code quality, and the error that gives this blog entry its title is another.


Sometimes bulk copy will import a table from text without explicitly setting the columns. Sometimes you have to explicitly set the columns and poof! it works. It may have to do with white space or case sensitivity in the columns, or it may have to do with drivers making inaccurate counts of fields.


SqlBulkCopy bcp \= new SqlBulkCopy(  

“Server\=.;persist security info\=True;initial catalog\=target;Integrated Security\=SSPI”,  

SqlBulkCopyOptions.KeepIdentity \& SqlBulkCopyOptions.KeepNulls);


bcp.BatchSize \= 50000;  

bcp.ColumnMappings.Clear();


for (int i\=0;i {  

string name \= reader.GetName(i).Trim().ToLower();  

bcp.ColumnMappings.Add(name,name);  

}


for (int i \= 0; i \< bcp.ColumnMappings.Count\-1; i\+\+)  

{  

System.Diagnostics.Debug.WriteLine(bcp.ColumnMappings\[i].SourceColumn);  

}  

bcp.DestinationTableName \= file.Name.Split(‘.’)\[0];


bcp.WriteToServer(reader);


bcp.Close();


**NOTE:** Even explicitly listing the columns often is not enough. I eventually gave up and used alternate techniques. The command is poorly documented with respect to what text formats are acceptable for BIT, DATETIME, IMAGE when doing heterogeneous bulkcopy. Until MSDN documents it, this otherwise fantastic tool is only reliable for copying from SQL to SQL with identical schemas and probably identical version and patch levels.