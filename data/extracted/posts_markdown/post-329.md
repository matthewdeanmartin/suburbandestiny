---
date: '2008-03-05'
recovered_from: wayback
slug: post-329
source_file: data\normalized\tech.wakayos.com\root\__query__\p\329\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=329
title: 'Review: Talend Open Studio'
---


**What**. Talend Open Studio (TOS) is a [ETL package](http://en.wikipedia.org/wiki/Category:ETL_tools). It competes with Data Transformation Services (DTS), Sql Server Integration Services (SSIS) and Pervasive Integration Architect (PIA) nee Data Junction. It also competes with some products I’m not familiar with, such as Informatica, Oracle Data Integrator, IBM Data Stage nee Ardent.


This is first impressions review, based on my “hello world” app, a webcast and an webex demo done by the friendly folk at Talend. Kudos to Vincent Pineau et al.


**Whats to like**. Talend as an organization has their act together. They are not anti\-developer, I didn’t have to talk to ten people to get a trial copy, not like, um, not to name any names, but ok, PERVASIVE. In fact they are offering Talend as FLOSS, it is GPL open source, so you can just download it and start copying tables in pubs or what have you right away. I hope more companies can make the opensource model work because it sure makes it easier to start using a new technology. (And with enough time and gumption I hope to review the other open source ETL packages, since I can actually get my hands on them)  

**Cool Features.**  

**Appears to be buffer driven.** Evidence is that you can have a tranformation feed into a tranformation feed into a transformation. For example, you can have a pipeline with filter, apply expressions to columns, aggregate, look up all without having to write to a table between steps. In DTS, you’d have to write to table or file between each of these. SSIS also uses a buffer architecture, which gives it remarkable performance. I’m guessing Talend would have similar performance, but I haven’t stress tested it yet.


**Source control features are built in**. You can do side by side visual diffs– very cool. To do the same in a comparable environment, you’d have to open two IDE’s of two snapshots of a ETL package. If you checked the generated java code into regular source control, you probably would be able to do a readable text diff, unlike SSIS, whose XML format is not entirely human readable. PIA has semi XML source code, and is sort of readable. The PIA RIFL code is stored in the source as plain text inside CDATA blocks, but the rest of the objects are stored as XML, which isn’t readable as the corresponding code generated Java.


**Real programmign language(S)**. You can write all your functions and expressions in Java (or heaven forbid Perl). This is a leap ahead of SSIS and PIA. SSIS uses it’s own expression langauge (a hybrid of C\# and VB.NET) and PIA uses RIFL, which is VBScript with glasses and a fake mustache. Also, the IDE is Eclipse– a real IDE, which you’ve probably already encountered, if you’ve done any JavaScript development (like Aptana, or Java development with Eclipse itself)


**Straight forward configuration**. By this I mean it should be very simple to move code from dev to test to production with minimal fuss and minimal likelihood of accidental. \[Pending complete review]. I know that SSIS made it’s configuration too complex, DTS managed to permenantly root itself to the place it was written. PIA uses “Macro” files, but has an overly complex and leaves me worried that I’ll run code against the wrong server by accident.


**Same behavior at design time and run time**. It’s code generated, doesn’t have a separate run time engine.


**JavaDoc like documenation generation.** Except it is much better looking. The generate documentation also helps with the “clickity\-click” problems with all ETL IDE’s, i.e. you have to do a lot of clicking to drill down into each property and find out what the \*\#$@$\# is going on.


\[I'll have to finish this later]


**What’s Confusing– the business model.**


**Licensing.** Jasper and Talend seem to both be marketing service contracts for the same code base.


If your organization won’t let you use software without a support contract behind it, there is a [Silver, Gold, Platinum support contract](http://www.talend.com/store/technical-support/technical-support-silver.php). Not clear if one needs to buy a commercial version to be able to buy a support contract. They also sell training courses.


If you want features not in the GPL version, there are 3 commercial versions, Team, Professional and Enterprise edition. If I understand correctly, Team, Pro \& Enterprise include more source control, documentation generation, deployment, and a type of multiserver load balancing feature.


Licensing/Support is per developer (so no need to count CALs, CPU’s, Servers, etc.)