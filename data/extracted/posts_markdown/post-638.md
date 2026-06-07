---
date: '2011-12-05'
recovered_from: wayback
slug: post-638
source_file: data\normalized\tech.wakayos.com\root\__query__\p\638\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=638
title: Rude and Passive Aggressive SQL Error Messages
---


First off, some people are just “rude\-deaf” It doesn’t matter what rude language or actions one complains about and they say, “No that wasn’t rude, the error message only said ‘Fuck you and your grandmother’”


Second, you don’t have to have an error message that says “Fuck you and your grandmother” to be rude. Most error messages crimes are being unhelpful and passive aggressive (i.e. hostility through doing nothing, like just watching someone on crutch struggling to open a door)


**Incorrect syntax near ‘%.\*ls’.**  

This message typically is filled in with something like , or ‘ A typical query is choc full of commas. Only a passive aggressive human would tell someone, “There is a spelling mistake in your term paper near one of the spaces” SQL error messages tend to identify the location of a syntax error by a chunky measure, maybe the statement, so the error could be anywhere inside a 1000 line SQL statement. And if the syntax error could provide the previous 100 and succeeding 100 non\-blank characters with a pointer at where SQL first realized something went wrong, that would be helpful.


**Warning: Fatal error %d occurred at %S\_DATE. Note the error and time, and contact your system administrator.**  

First off, the people who read this either are the administrator, or there isn’t an administrator. You might as well swap in some other imaginary figure, like god. “Fatal error. Pray to your gods, fucktard”


**The type ‘%.\*ls’ already exists, or you do not have permission to create it.**  

Oh SQL, you know why this failed. Surely there isn’t a single method called ExistsOrLacksPermissions and the implementers just can’t decide why that exception was thrown. I think this error is rude or fucked up. You decide.


**Finally, be helpful.**  

Is it really so hard to write a suggested fix? “Permission denied, execute “GRANT” command to grant permissions”


Google exists, who ever is working on MS\-SQL ought to google all their own messages and just put a sentence worth of the internet’s collective advice into their error message.