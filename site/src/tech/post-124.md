---
date: '2006-04-28'
recovered_from: wayback
slug: post-124
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200604\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=124
title: SSIS’s ‘Fast Load’, ‘INSERT BULK’ and Bcp
---


SSIS has an option called ‘Fast Load’. That means using the bcp application to move data to SQL without issuing INSERT commands, bypassing the relational DB engine. It is dramatically faster, but invalidates subsequent transaction log backups.



> insert bulk \[dbo].\[Table Name](\[columnn name] datatype) with (TABLOCK,CHECK\_CONSTRAINTS)


SQL profiler shows the above syntax, which according to Books Online doesn’t exist. It is just SQL profiler’s way of showing what is essentially a binary event, not a T\-SQL event.