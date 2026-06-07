---
date: '2007-06-22'
recovered_from: wayback
slug: post-235
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200706\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=235
title: SQL Style vs AzMan Style rights granting
---


SQL Style  

You can call a method (stored procedure) that access resources (views and tables) on your behalf, but you can’t always access the resources directly. SQL Procedures almost analogous to AzMan task, and tables are analogous to operations. How ever, an AzMan task implies you have access to all the components of the task directly as well as through the task.


AzMan Style  

If you can call any method (task) that uses a resource, you can use that resource directly.


Both styles, make sense, why doesn’t AzMan support them both? Well, in a sense, you could simulate SQL style by making all stored procedures ‘operations’ I think the only disadvantage is that if there is an action, say sending an email, which is implicitly available in one operation, but not another, it might be confusing. For example, if you have a task called, ‘contact customer’, which is make up of ‘lookup address’, ‘send email’– you might decide to change ‘contact customer’ to an operation, since you don’t want the user to ‘send email’ except in the context of the ‘contact customer’ task.