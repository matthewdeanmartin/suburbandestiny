---
date: '2007-06-25'
recovered_from: wayback
slug: post-241
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200706\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=241
title: Thought process for defining an AzMan policy
---


Groups vs Roles.  What ever the difference, I think these should slice the universe of users differently.  If groups are based on you are in the organization (a partitioning strategy that can partition everyone), then roles should partition everyone by some other measure, say occupation.  


Another strategy is to assume that the groups are made up by an external organization and are too granular for your purposes.


The final strategy is to have groups \=\= roles.  For each group create one role.  This removes groups from the policy altogether.


Task. Task are tricky.  If you want to give someone the right to send email, update a database and delete a row, but not the right to do any of those individually, then \*don’t\* use a task.  A task means that if some one is able to do one of the operations \*individually\*, it logically follows that they can do them all.  For example, “delete own account”, “delete other accounts”, “delete lapsed accounts”, “delete active account” might be put in a single task.  Then you grant the task to a high level user and save yourself four role associations (over using strictly operations).


If you do want the user to complete a series of actions as a whole, but not individually (for example, he can send email to himself as part of a purchase transaction, but not directly call the email method with arbitrary recipients) then the purchase should be an operation.


And now I’m too tired to keep thinking. Good night folks.  \[Hey this is an un\-edited blog, what'd you think you'd stumbled into? PC Magazine?]