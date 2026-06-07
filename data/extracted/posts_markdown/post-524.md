---
date: '2009-04-25'
recovered_from: wayback
slug: post-524
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200904\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=524
title: How to Overengineer the Reference Table/Code Table
---


You probably store this in the database as a table.  It could also have been column constrain, although a column constraint won’t let you run a select. None of these easly allow you to treat the reference table as an enum in C\#, unless you use code generation.


**Worst**  

Create Table  States\_Ref (Id int, Description Varchar(50\))


The code is numeric,  so humans can’t look at raw tables to see data problems.  The data type is too large.  Worse would be bigint, or worst of all, just using image as a datatype in case there are a google of different states.  If all reference tables use Id/Description, then select queries go from


Select customer\_id, state\_id, type\_id, category\_id … etc


to


Select customer\_id, t1\.description, t2\.description, t3\.description… and now all queries require alias. Ugh.


**Better**Create Table  States\_Ref (States char(2\), Description Varchar(200\)).  Everyone can memorize CO, no one can memorize that 31 means Colorado.  Obviously, alphanumeric codes are for the maintenance developers and uber\-power users.  If your users are brain damaged, the actual reference value would be hidden.  In the real world, IT staff will eventually have to learn many of the numeric codes (But don’t get clever with alpha codes, don’t embed a mini\-db into the codes, like CO\_MTN\_STATE\_US.)


**Best**  

Create Table  States\_Ref (States char(2\), State\_Name Varchar(200\), State\_Name\_Short Varchar(50\), Active bit)


The alphanumeric codes are space efficient and human memorizable.  The Active bit allows certain codes to be phase out without going back to legacy data and changing the old code.  The descriptive columns include the table name (In data tables, ie. not reference tables, I wouldn’t add the table name to every column, though)


C\# and ASP.NET **Bad**: Put the drop down list into a DataSet, reload every time. **Better Yet**: Put the list into a Sorted Dictionary or Sorted List. (And do the sorting server side in SQL 1st of course), reload everyt time. **Better Yet:** Batch up requests for reference tables, return them all at once in a multi query  result set.  

**Best**: Put the Sorted Dictionary into the ASP.NET Cache (Or viewstate at least).   DataSets and DataTables both are too big.  Don’t cache the user control– it causes peculiar behaviors


UI\-  

Worst\- Dropdowns that require a mouse to search and select.  

Better\- List boxes that allow viewing all rows (sometimes the list is too long and screen space to sparse, but if you can, show all the items)  

Best\- JavaScript instant filters for long lists


Binding\-  

Worst\- Fail to load or show a blank if the value is no longer Valid  

Best\- Add value to list if binding and the value isn’t on the list.


Any more ideas?