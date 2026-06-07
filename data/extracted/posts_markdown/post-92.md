---
date: '2003-10-10'
recovered_from: wayback
slug: post-92
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200310\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=92
title: More Thoughts on Using XML
---


One use for XML is for config files– but they are plaintext and thus a bad place to put passwords. The XML file can be encrypted, but I have discovered, config files are useful because they are easy to edit (as compared to registry, which has the world’s scaries warnings, or DB which require a SQL statement to update). Encrypting the file makes them a real pain to edit. Create two config files, encrypt the one with passwords, put everything else into the other config file.