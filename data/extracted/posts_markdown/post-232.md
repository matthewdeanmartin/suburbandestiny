---
date: '2007-06-18'
recovered_from: wayback
slug: post-232
source_file: data\normalized\tech.wakayos.com\root\__query__\p\232\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=232
title: Group, Role, Task, Operation Design—Some Theory
---


\[This article is looking at authorization design from an AzMan standpoint, with AzMan jargon]



Users are atomic users. Operations are atomic securables, either actions or resources (the right to DO something or the right to do something TO something).



Groups can be any combination of all the users, so when designing groups, you have combinations, so k!/(2\-k)!k! two user groups to consider, K!/(3\-k)!K! three user groups to consider and so on. Of course there is only one ‘everyone’ group. That is a lot of groups. Let’s invent some theory to decide how to create the groups that make sense.



Natural Social Groups. Just ape the social groups that appear on the business organization chart. That chart was meant for controlling chains of command, and may or may not make sense in the context of a petty cash tracking application. Natural social groups have the advantage of being well known, fairly easy to update without much application knowledge.



Risk Driven Grouping. We check access to prevent certain users from doing things. Who do we really want to prevent from doing things? People who could do harm, either by being indiscrete with the information they learn, or by destroying data by deletion or update. By this line of reasoning, you could group people by



 auditability—eg. Anonymous users versus authenticated users



 seniority—more experienced users, users that have completed training can safely get access to more functions



trustworthiness—our own staff is likely to be more loyal and concerned about our data then business partners who work for another organization



legal status—There may be formal groupings, such as a security clearance.



Application driven groups. Let’s say not all supervisors can manage petty cash, and the business organization chart doesn’t have a ‘Petty Cash Managers’ group, so we create a group with the 14 people who can manage petty cash—it might have natural group of sales managers plus all the managers except the engineering department. We will want to create a role.



Roles are idealized work descriptions—or groups of task depending on how you look at it.



Tasks are groups of operations, operations being the atomic securables. A risk driven grouping of tasks would separate securable actions into those that are potentially destructive vs those that are not, for example, update and delete are destructive, create is less destructive and read is a threat to secrecy, but not data integrity.