---
date: '2004-03-26'
recovered_from: wayback
slug: post-110
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200403\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=110
title: Unions vs Outter Joins
---


If you have one table of things, say bills that need to linked to a large number of subsidiary tables that have a wide variety of structures, you can:


Do pairwise joins between your fact table and your subsidiary table then union all of these together. This runs the risk of losing rows or doubling rows if you have data quality problems (having a fact described in two subsidiary tables or in no subsidiary tables). 


The better solution is to have the fact table link by an outter join to all of the subsidiary tables. This will result in a bunch of columns with either a null or the description of the row in the fact table. COALESCE can be used to pick the first non\-null value. This way, you never lose fact rows, you get a description picked at random if there are more than 1 descriptions in the subsidiary tables and you get a null if the description can’t be found.