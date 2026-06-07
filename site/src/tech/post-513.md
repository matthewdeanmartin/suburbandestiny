---
date: '2009-01-20'
recovered_from: wayback
slug: post-513
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200901\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=513
title: Datagrid and Gridview, just don’t cut it anymore.
---


Long ago I was happy.  I always used the SqlDataSource and my GridViews bound with all the features I could ever want.   I didn’t have to write 1000s of lines of code to page and sort.  It worked so well, I mistakenly thought the magic was due to the GridView or the xxxDataSource technology.  Actually, the paging and sorting is irregularlly implemented depending on datasource.


New datasources appeared on the scene, like SQLite, SQL Compact, and data generated data access layers, like SubSonic.  I realized that as soon as you bind to an ObjectDataSource, a dataset/datatable, you are responsible for paging and sorting.  At best you’ll be able to register all your grids to some common code. (I gotta look up that link for the technique)– you quickly find yourself back in the world of the DataGrid, with 1000s of lines of code to write.


Now I’m thinking everyone should pick a grid that at minimum supports paging and sorting.  I’m choosing Telerik’s grid, which can sort and page any datasource so long as you use the NeedData event for binding.